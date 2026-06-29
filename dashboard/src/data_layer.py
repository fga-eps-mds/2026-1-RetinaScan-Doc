import os
import json
import pandas as pd
from .config import REPOS_LANGUAGE, SONAR_METRIC_LIST

def unmarshall_json(json_path: str) -> dict:
    with open(json_path, encoding='utf-8') as json_file:
        return json.load(json_file)

def extract_metrics_per_file(json_dict: dict) -> list:
    file_json = []
    base_comp = json_dict.get('baseComponent', {})
    if base_comp:
        measures = {m['metric']: float(m.get('value', 0)) for m in base_comp.get('measures', [])}
        base_comp['measures_dict'] = measures
        base_comp['qualifier'] = 'TRK'
        file_json.append(base_comp)
        
    for component in json_dict.get('components', []):
        measures = {m['metric']: float(m.get('value', 0)) for m in component.get('measures', [])}
        component['measures_dict'] = measures 
        qualifier = component.get('qualifier')
        ncloc = measures.get('ncloc', 0)
        if (qualifier == 'FIL' and ncloc > 0) or qualifier in ['DIR', 'UTS', 'TRK']:
            file_json.append(component)
    return file_json

def generate_component_rows(metrics_list, file_component_data, target_lang):
    rows = []
    for file in file_component_data:
        measures = file.get('measures_dict', {})
        row = {m: measures.get(m, None) for m in metrics_list} 
        row.update({
            'qualifier': file.get('qualifier'),
            'language': file.get('language'),
            'path': file.get('path')
        })
        if file['qualifier'] == 'FIL':
            lang = file.get('language')
            if lang == target_lang or (target_lang == 'py' and lang == 'python'):
                rows.append(row)
        else:
            rows.append(row)
    return rows

def build_raw_components_dataframe(json_list: list) -> pd.DataFrame:
    df_res = pd.DataFrame()
    for json_path in json_list:
        file_component = unmarshall_json(json_path)
        base_name = os.path.basename(json_path)
        parts = base_name.split("-")
        repo_key = parts[6] if len(parts) > 6 else None
        
        if repo_key and repo_key in REPOS_LANGUAGE:
            rows = generate_component_rows(SONAR_METRIC_LIST, extract_metrics_per_file(file_component), REPOS_LANGUAGE[repo_key])
            file_df = pd.DataFrame(rows)
            file_df['filename'] = base_name
            file_df['repository'] = "-".join(parts[0:7])
            file_df['datetime_str'] = "-".join(parts[7:13])
            file_df['version'] = parts[13].replace(".json", "")
            df_res = pd.concat([df_res, file_df], ignore_index=True)
            
    if df_res.empty: 
        return df_res
        
    df_res['datetime'] = pd.to_datetime(df_res['datetime_str'], format='%m-%d-%Y-%H-%M-%S', errors='coerce')
    if df_res['datetime'].isna().all():
        df_res['datetime'] = pd.to_datetime(df_res['datetime_str'], errors='coerce')
        
    return df_res.sort_values(by=['repository', 'datetime'])

def load_zenhub_sprints_raw() -> dict:
    """Carrega o dicionário bruto completo do arquivo analytics."""
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    raiz_do_projeto = os.path.dirname(os.path.dirname(diretorio_atual))
    caminho_json = os.path.join(raiz_do_projeto, "zenhub_analytics.json")
    
    if not os.path.exists(caminho_json):
        caminho_alternativo = os.path.join(raiz_do_projeto, "analytics", "raw-data", "zenhub_analytics.json")
        if os.path.exists(caminho_alternativo):
            caminho_json = caminho_alternativo
        else:
            return {}

    with open(caminho_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    return data if isinstance(data, dict) else {}

def load_github_runs_raw() -> list:
    """Varre e unifica as listas de workflow_runs de todos os arquivos de Runs na pasta raw-data."""
    import glob
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    raiz_do_projeto = os.path.dirname(os.path.dirname(diretorio_atual))
    
    # Busca por todos os padrões de arquivos de Runs gerados pela automação
    caminho_runs = os.path.join(raiz_do_projeto, "analytics", "raw-data", "GitHub_API-Runs-*.json")
    arquivos = glob.glob(caminho_runs)
    
    all_runs = []
    for arquivo in arquivos:
        try:
            dados = unmarshall_json(arquivo)
            if "workflow_runs" in dados:
                all_runs.extend(dados["workflow_runs"])
        except Exception as e:
            print(f"Erro ao ler arquivo de runs {arquivo}: {e}")
            
    return all_runs