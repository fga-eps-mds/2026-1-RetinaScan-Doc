import os
import requests
import json
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()

ZENHUB_TOKEN = os.getenv("ZENHUB_TOKEN")
ZENHUB_URL = "https://api.zenhub.com/public/graphql"
WORKSPACE_ID = "69bd9cee544e2d00306abb69"

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
          # Estrutura oficial para capturar metadados do Milestone do GitHub atrelado à issue
          milestone {
            number
            title
          }
        }
      }
    }
  }
}
"""

variables = {"workspaceId": WORKSPACE_ID}

print("🔄 Solicitando mineração COMPLETA de dados do Zenhub...")

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
        
        for sprint in sprints_list:
            velocity_by_sprint[sprint["name"]] = {
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
        
        ignored_titles = ["R1", "R2", "R3", "RM6", "Autenticação e Controle de Acesso", 
                          "Cadastro e Upload de Exames", "Histórico e Consulta", "Processamento e IA"]
        
        milestones_dict = {}  

        for pipe in ws_data.get("pipelines", []):
            pipe_name = pipe["name"]
            issues_list = pipe.get("issues", {}).get("nodes", [])
            
            for issue in issues_list:
                title = issue["title"].strip()
                state = issue["state"]
                points = issue["estimate"]["value"] if issue.get("estimate") else 0.0
                card_sprints = [s["name"] for s in issue.get("sprints", {}).get("nodes", [])]
                ms_info = issue.get("milestone")
                
                # Ignora issues fakes que usavam nome de release ou epics macros vazios
                if title in ignored_titles or "Release MAJOR" in title or title in ["R1", "R2", "R3", "RM6"]:
                    continue
                
                if ms_info:
                    ms_num = ms_info["number"]
                    if ms_num not in milestones_dict:
                        milestones_dict[ms_num] = {
                            "number": ms_num,
                            "title": ms_info["title"],
                            "state": "OPEN", # Padrão para visualização no dashboard
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
                    "milestone": ms_info["title"] if ms_info else None
                }
                
                target_pipe = "Closed" if state == "CLOSED" else pipe_name
                if target_pipe in clean_pipelines:
                    clean_pipelines[target_pipe].append(issue_obj)
                
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
            
        print(f"\n💾 Sucesso: O arquivo '{nome_arquivo}' foi gerado com os dados lapidados!")

    else:
        print(f"❌ Erro HTTP {response.status_code}: {response.text}")

except Exception as e:
    print(f"❌ Falha crítica de execução: {e}")