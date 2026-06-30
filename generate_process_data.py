import json
import os
from datetime import datetime, timezone

import requests
from dotenv import load_dotenv

load_dotenv()

ZENHUB_TOKEN = os.getenv("ZENHUB_TOKEN")
ZENHUB_URL = "https://api.zenhub.com/public/graphql"
WORKSPACE_ID = "69bd9cee544e2d00306abb69"

# Range completo do semestre corrente de 2026 para abranger o Throughput Acumulado total
DATA_INICIO_SEMESTRE = datetime(2026, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
DATA_FIM_SEMESTRE = datetime(2026, 7, 28, 23, 59, 59, tzinfo=timezone.utc)

if not ZENHUB_TOKEN:
    print("❌ Erro: ZENHUB_TOKEN não encontrado no arquivo .env")
    exit(1)

headers = {
    "Authorization": f"Bearer {ZENHUB_TOKEN}",
    "Content-Type": "application/json",
}

# Query ajustada de volta para o teto estrito de 100 itens exigido pelo ZenHub
query = """
query GetWorkspaceCompleteAgileData($workspaceId: ID!) {
  workspace(id: $workspaceId) {
    name
    sprints(first: 100) {
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
          sprints(first: 5) {
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
          labels(first: 15) {
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

print("🔄 Conectando ao ZenHub para extração total do ecossistema RetinaScan...")

try:
    response = requests.post(
        ZENHUB_URL, json={"query": query, "variables": variables}, headers=headers
    )

    if response.status_code == 200:
        res_data = response.json()
        if "errors" in res_data:
            print("❌ Erro no GraphQL:")
            print(json.dumps(res_data["errors"], indent=2))
            exit(1)

        ws_data = res_data["data"]["workspace"]
        print(f"✅ Conexão homologada com o Workspace: {ws_data['name']}")

        sprints_list = ws_data.get("sprints", {}).get("nodes", [])
        sprints_validas_nomes = set()

        for sprint in sprints_list:
            start_at_str = sprint.get("startAt")
            if start_at_str:
                sprint_start = datetime.fromisoformat(
                    start_at_str.replace("Z", "+00:00")
                )
                if DATA_INICIO_SEMESTRE <= sprint_start <= DATA_FIM_SEMESTRE:
                    sprints_validas_nomes.add(sprint["name"])

        # Estrutura crua de mapeamento total
        total_issues_list = []
        issues_processadas = set()

        for pipe in ws_data.get("pipelines", []):
            pipe_name = pipe["name"]
            issues_list = pipe.get("issues", {}).get("nodes", [])

            for issue in issues_list:
                num = issue["number"]
                if num in issues_processadas:
                    continue
                issues_processadas.add(num)

                labels = [
                    label["name"] for label in issue.get("labels", {}).get("nodes", [])
                ]
                issue_releases = [
                    r["title"] for r in issue.get("releases", {}).get("nodes", [])
                ]

                # SEM FILTROS: Entra tudo (US, Bug, Task, Infra, etc.)
                total_issues_list.append(
                    {
                        "number": num,
                        "title": issue["title"].strip(),
                        "state": issue["state"].upper().strip(),
                        "pipeline_atual": pipe_name,
                        "created_at": issue["createdAt"],
                        "closed_at": issue.get("closedAt"),
                        "story_points": issue["estimate"]["value"]
                        if issue.get("estimate")
                        else 0.0,
                        "sprints": [
                            s["name"] for s in issue.get("sprints", {}).get("nodes", [])
                        ],
                        "labels": labels,
                        "releases": issue_releases,
                    }
                )

        # SALVANDO EM UM ARQUIVO NOVO E ISOLADO
        nome_arquivo = "zenhub_all_issues.json"
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            json.dump(total_issues_list, f, indent=4, ensure_ascii=False)

        print(f"\n💾 Arquivo '{nome_arquivo}' gerado com sucesso!")
        print(f"📊 Total de artefatos catalogados: {len(total_issues_list)}")

    else:
        print(f"❌ Erro HTTP {response.status_code}: {response.text}")

except Exception as e:
    print(f"❌ Falha crítica de execução: {e}")
