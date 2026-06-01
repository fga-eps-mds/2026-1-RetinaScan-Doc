import os
import requests
import json
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()

ZENHUB_TOKEN = os.getenv("ZENHUB_TOKEN")
ZENHUB_URL = "https://api.zenhub.com/public/graphql"
WORKSPACE_ID = "69bd9cee544e2d00306abb69"

# 🔥 CONFIGURAÇÃO DOS FILTROS DA R3
TAG_USER_STORY = "US" 
TERMO_RELEASE = "R3" 

# 🗓️ INTERVALO DE DATAS DA R3 (Garante pegar as 5 sprints sem depender do texto do nome)
DATA_INICIO_R3 = datetime(2026, 5, 25, 0, 0, 0, tzinfo=timezone.utc)
DATA_FIM_R3    = datetime(2026, 6, 28, 23, 59, 59, tzinfo=timezone.utc)

if not ZENHUB_TOKEN:
    print("❌ Erro: ZENHUB_TOKEN não encontrado no arquivo .env")
    exit(1)

headers = {
    "Authorization": f"Bearer {ZENHUB_TOKEN}",
    "Content-Type": "application/json"
}

query = """
query GetWorkspaceAgileData($workspaceId: ID!) {
  workspace(id: $workspaceId) {
    name
    sprints(first: 50) {
      nodes {
        id
        name
        startAt
        endAt
        state
      }
    }
    pipelines {
      id
      name
      issues(first: 100) {
        nodes {
          id
          number
          title
          state
          createdAt
          closedAt
          estimate {
            value
          }
          sprints(first: 3) {
            nodes {
              id
              name
              state
            }
          }
          milestone {
            number
            title
          }
          labels(first: 10) {
            nodes {
              name
            }
          }
          releases(first: 5) {
            nodes {
              id
              title
              state
            }
          }
        }
      }
    }
  }
}
"""

variables = {"workspaceId": WORKSPACE_ID}

print(f"🔄 Solicitando dados do Zenhub (Filtrando cronologicamente as Sprints da R3)...")

try:
    response = requests.post(ZENHUB_URL, json={"query": query, "variables": variables}, headers=headers)
    
    if response.status_code == 200:
        res_data = response.json()
        if "errors" in res_data:
            print("❌ Erro no GraphQL:")
            print(json.dumps(res_data["errors"], indent=2))
            exit(1)
            
        ws_data = res_data["data"]["workspace"]
        print(f"✅ Conexão homologada com o quadro: {ws_data['name']}")
        
        sprints_list = ws_data.get("sprints", {}).get("nodes", [])
        velocity_by_sprint = {}
        sprints_validas_nomes = set() # Guarda o nome exato das sprints que estão no período da R3
        
        # 1. FILTRAGEM DINÂMICA DE SPRINTS POR DATA
        for sprint in sprints_list:
            start_at_str = sprint.get("startAt")
            if start_at_str:
                # Converte o timestamp do Zenhub para objeto datetime
                sprint_start = datetime.fromisoformat(start_at_str.replace("Z", "+00:00"))
                
                # Se a sprint começou dentro do período da R3, ela é válida
                if DATA_INICIO_R3 <= sprint_start <= DATA_FIM_R3:
                    sprint_name = sprint["name"]
                    sprints_validas_nomes.add(sprint_name)
                    
                    velocity_by_sprint[sprint_name] = {
                        "id": sprint["id"],
                        "start_at": sprint["startAt"],
                        "end_at": sprint["endAt"],
                        "state": sprint["state"],
                        "delivered_story_points": 0.0,
                        "completed_issues_count": 0
                    }
        
        clean_pipelines = {
            "New Issues": [], "Icebox": [], "Product Backlog": [], 
            "Sprint Backlog": [], "In Progress": [], "Review/QA": [], 
            "Waiting PO Approval": [], "Done": [], "Closed": []
        }
        
        milestones_dict = {}  

        for pipe in ws_data.get("pipelines", []):
            pipe_name = pipe["name"]
            issues_list = pipe.get("issues", {}).get("nodes", [])
            
            for issue in issues_list:
                # FILTRO 1: Se não for US, pula
                labels = [label["name"] for label in issue.get("labels", {}).get("nodes", [])]
                if TAG_USER_STORY not in labels:
                    continue
                
                # FILTRO 2: Se não for da Release R3, pula
                issue_releases = [r["title"] for r in issue.get("releases", {}).get("nodes", [])]
                pertence_a_r3 = any(TERMO_RELEASE in r_title for r_title in issue_releases)
                if not pertence_a_r3:
                    continue
                
                title = issue["title"].strip()
                state = issue["state"]
                points = issue["estimate"]["value"] if issue.get("estimate") else 0.0
                
                # Associa à issue apenas as sprints que pertencem ao período da R3
                card_sprints = [s["name"] for s in issue.get("sprints", {}).get("nodes", []) if s["name"] in sprints_validas_nomes]
                
                ms_info = issue.get("milestone")
                if ms_info:
                    ms_num = ms_info["number"]
                    if ms_num not in milestones_dict:
                        milestones_dict[ms_num] = {
                            "number": ms_num,
                            "title": ms_info["title"],
                            "state": "OPEN",
                            "total_issues": 0,
                            "closed_issues": 0
                        }
                    milestones_dict[ms_num]["total_issues"] += 1
                    if state == "CLOSED":
                        milestones_dict[ms_num]["closed_issues"] += 1
                
                issue_obj = {
                    "number": issue["number"],
                    "title": title,
                    "state": state,
                    "created_at": issue["createdAt"],
                    "closed_at": issue.get("closedAt"),
                    "story_points": points,
                    "sprints": card_sprints,
                    "milestone": ms_info["title"] if ms_info else None,
                    "releases": issue_releases,
                    "labels": labels
                }
                
                target_pipe = "Closed" if state == "CLOSED" else pipe_name
                if target_pipe in clean_pipelines:
                    clean_pipelines[target_pipe].append(issue_obj)
                
                # Acumula velocidade se a sprint calculada for uma das sprints válidas da R3
                if state == "CLOSED" and issue.get("closedAt"):
                    for s_name in card_sprints:
                        if s_name in velocity_by_sprint:
                            velocity_by_sprint[s_name]["delivered_story_points"] += points
                            velocity_by_sprint[s_name]["completed_issues_count"] += 1

        github_milestones = sorted(list(milestones_dict.values()), key=lambda x: x["number"])

        dashboard_payload = {
            "workspace_name": ws_data["name"],
            "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "milestones": github_milestones, 
            "sprints_velocity": velocity_by_sprint, 
            "metrics_by_pipeline": clean_pipelines
        }
        
        nome_arquivo = "zenhub_analytics.json"
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            json.dump(dashboard_payload, f, indent=4, ensure_ascii=False)
            
        print(f"\n💾 Sucesso: O arquivo '{nome_arquivo}' foi gerado com todas as sprints do intervalo da R3!")

    else:
        print(f"❌ Erro HTTP {response.status_code}: {response.text}")

except Exception as e:
    print(f"❌ Falha crítica de execução: {e}")