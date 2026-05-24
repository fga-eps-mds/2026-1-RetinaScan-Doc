# src/metrics.py
import pandas as pd
from .config import WEIGHT_CODE_QUALITY, WEIGHT_TESTING_STATUS, WEIGHT_PSC1, WEIGHT_PSC2, WEIGHT_PC1, WEIGHT_PC2
from datetime import datetime, timezone

def get_files_sub_df(df: pd.DataFrame) -> pd.DataFrame:
    files_df = df[df['qualifier'] == 'FIL']
    return files_df.dropna(subset=['complexity', 'comment_lines_density', 'duplicated_lines_density'], how='all')

def calculate_ncloc(df: pd.DataFrame) -> int:
    trk_df = df[df['qualifier'] == 'TRK']
    if not trk_df.empty:
        return int(pd.to_numeric(trk_df['ncloc'], errors='coerce').iloc[0])
    return int(pd.to_numeric(df[df['qualifier'] == 'FIL']['ncloc'], errors='coerce').sum())

def calculate_complexity_score(df: pd.DataFrame) -> float:
    f_df = get_files_sub_df(df)
    f_df = f_df[pd.to_numeric(f_df['functions'], errors='coerce') > 0].copy()
    if f_df.empty:
        trk_df = df[df['qualifier'] == 'TRK']
        if not trk_df.empty:
            comp = pd.to_numeric(trk_df['complexity'], errors='coerce').iloc[0]
            func = pd.to_numeric(trk_df['functions'], errors='coerce').iloc[0]
            return 1.0 if func > 0 and (comp / func) < 10 else 0.0
        return 0
    comp = pd.to_numeric(f_df['complexity'], errors='coerce')
    func = pd.to_numeric(f_df['functions'], errors='coerce')
    return len(f_df[(comp / func) < 10]) / len(f_df)

def calculate_comments_score(df: pd.DataFrame) -> float:
    f_df = get_files_sub_df(df)
    if f_df.empty:
        trk_df = df[df['qualifier'] == 'TRK']
        if not trk_df.empty:
            dens = pd.to_numeric(trk_df['comment_lines_density'], errors='coerce').iloc[0]
            return 1.0 if (dens > 10 and dens < 30) else (dens / 30.0 if dens <= 10 else 0.0)
        return 0
    dens = pd.to_numeric(f_df['comment_lines_density'], errors='coerce')
    return len(f_df[(dens > 10) & (dens < 30)]) / len(f_df)

def calculate_duplication_score(df: pd.DataFrame) -> float:
    f_df = get_files_sub_df(df)
    if f_df.empty:
        trk_df = df[df['qualifier'] == 'TRK']
        if not trk_df.empty:
            dup = pd.to_numeric(trk_df['duplicated_lines_density'], errors='coerce').iloc[0]
            return 1.0 if dup < 5 else 0.0
        return 0
    dup = pd.to_numeric(f_df['duplicated_lines_density'], errors='coerce')
    return len(f_df[dup < 5]) / len(f_df)

def calculate_test_success_score(df: pd.DataFrame) -> float:
    uts_df = df[df['qualifier'] == 'UTS']
    if uts_df.empty:
        trk_df = df[df['qualifier'] == 'TRK']
        if not trk_df.empty:
            errors = pd.to_numeric(trk_df.get('test_errors', 0), errors='coerce').fillna(0).iloc[0]
            failures = pd.to_numeric(trk_df.get('test_failures', 0), errors='coerce').fillna(0).iloc[0]
            return 1.0 if (errors + failures) == 0 else 0.0
        return 0
    errors = uts_df.get('test_errors', pd.Series([0]*len(uts_df))).fillna(0)
    failures = uts_df.get('test_failures', pd.Series([0]*len(uts_df))).fillna(0)
    passed_tests = len(uts_df[(errors + failures) == 0])
    return passed_tests / len(uts_df)

def calculate_fast_tests_score(df: pd.DataFrame) -> float:
    uts_df = df[df['qualifier'] == 'UTS'].fillna(0)
    uts_df = uts_df.dropna(subset=['test_execution_time'])
    if uts_df.empty: 
        return 1.0 
    fast = len(uts_df[pd.to_numeric(uts_df['test_execution_time'], errors='coerce') < 300000])
    return fast / len(uts_df)

def calculate_coverage_score(df: pd.DataFrame) -> float:
    f_df = get_files_sub_df(df)
    if f_df.empty:
        trk_df = df[df['qualifier'] == 'TRK']
        if not trk_df.empty:
            cov = pd.to_numeric(trk_df['coverage'], errors='coerce').iloc[0]
            return 1.0 if cov > 60 else (cov / 100.0)
        return 0
    cov = pd.to_numeric(f_df['coverage'], errors='coerce')
    return len(f_df[cov > 60]) / len(f_df)

def build_aggregated_metrics_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    res = []
    for v in df['datetime_str'].unique():
        v_df = df[df['datetime_str'] == v]
        res.append({
            'complexity': calculate_complexity_score(v_df), 
            'comments': calculate_comments_score(v_df), 
            'duplication': calculate_duplication_score(v_df),
            'test_success': calculate_test_success_score(v_df), 
            'fast_tests': calculate_fast_tests_score(v_df), 
            'coverage': calculate_coverage_score(v_df),
            'repository': v_df['repository'].iloc[0], 
            'version': v_df['version'].iloc[0], 
            'datetime': v_df['datetime'].iloc[0], 
            'ncloc': calculate_ncloc(v_df), 
            'datetime_str': v
        })
        
    metrics_df = pd.DataFrame(res)
    if metrics_df.empty:
        return metrics_df
        
    metrics_df['code_quality'] = (
        (metrics_df['complexity'] * WEIGHT_CODE_QUALITY[0]) + 
        (metrics_df['comments'] * WEIGHT_CODE_QUALITY[1]) + 
        (metrics_df['duplication'] * WEIGHT_CODE_QUALITY[2])
    ) * WEIGHT_PSC1
    
    metrics_df['testing_status'] = (
        (metrics_df['test_success'] * WEIGHT_TESTING_STATUS[0]) + 
        (metrics_df['fast_tests'] * WEIGHT_TESTING_STATUS[1]) + 
        (metrics_df['coverage'] * WEIGHT_TESTING_STATUS[2])
    ) * WEIGHT_PSC2
    
    metrics_df['Maintainability'] = metrics_df['code_quality'] * WEIGHT_PC1
    metrics_df['Reliability'] = metrics_df['testing_status'] * WEIGHT_PC2
    metrics_df['total'] = metrics_df['Maintainability'] + metrics_df['Reliability']
    
    return metrics_df

def calculate_scrum_evm_metrics(sprints_raw: dict) -> dict:
    """Calcula métricas dinâmicas de EVM com base no histórico real do ZenHub."""
    def parse_iso(dt_str):
        if not dt_str: return datetime.min.replace(tzinfo=timezone.utc)
        return datetime.fromisoformat(dt_str.replace("Z", "+00:00"))

    sprints_lista = []
    for name, info in sprints_raw.items():
        if info.get("start_at") and info.get("end_at"):
            sprints_lista.append({
                "name": name,
                "start_at": parse_iso(info["start_at"]),
                "end_at": parse_iso(info["end_at"]),
                "completed_sp": float(info.get("completed_issues_count", 0)), 
                "delivered_sp": float(info.get("delivered_story_points", info.get("delivered_sp", 0))),
                "state": info.get("state", "CLOSED").upper()
            })
            
    sprints_lista = sorted(sprints_lista, key=lambda x: x["start_at"])
    
    bac = sum(s["delivered_sp"] for s in sprints_lista)
    if bac == 0: bac = 60.0 
    
    hoje = datetime.now(timezone.utc)
    
    burnup_labels = ["S0"]
    burnup_pv = [0]
    burnup_ev = [0]
    burnup_ideal = [0]
    
    velocity_labels = []
    velocity_data = []
    velocity_colors = []
    
    spi_labels = []
    spi_data = []
    
    acumulado_pv = 0
    acumulado_ev = 0
    sprints_concluidas_count = 0
    sprint_atual_nome = "Não identificada"
    ultima_velocity = 0.0

    passo_ideal = bac / len(sprints_lista) if sprints_lista else 15.0

    for idx, s in enumerate(sprints_lista):
        s_label = f"S{idx+1}"
        
        if s["state"] == "ACTIVE" or (s["start_at"] <= hoje <= s["end_at"]):
            sprint_atual_nome = s["name"]

        start_txt = s["start_at"].strftime("%b%d")
        end_txt = s["end_at"].strftime("%b%d")
        burnup_labels.append(f"{s_label}\\n{start_txt}")
        velocity_labels.append(f"{start_txt}\\n{end_txt}")
        
        acumulado_pv += s["delivered_sp"] if s["delivered_sp"] > 0 else passo_ideal
        burnup_pv.append(round(acumulado_pv, 1))
        
        burnup_ideal.append(round((idx + 1) * passo_ideal, 1))
        
        if s["start_at"] <= hoje or s["state"] == "ACTIVE":
            acumulado_ev += s["delivered_sp"]
            burnup_ev.append(round(acumulado_ev, 1))
            
            velocity_data.append(s["delivered_sp"])
            velocity_colors.append("#185FA5") 
            
            spi = acumulado_ev / acumulado_pv if acumulado_pv > 0 else 1.0
            spi_data.append(round(spi, 2))
            spi_labels.append(s_label)
            
            if s["state"] != "ACTIVE":
                ultima_velocity = s["delivered_sp"]
        else:
            burnup_ev.append(None)
            velocity_data.append(0)
            velocity_colors.append("#D3D1C7") 

    spi_atual = spi_data[-1] if spi_data else 1.0
    score_zenhub = int(spi_atual * 100)
    if score_zenhub > 100: score_zenhub = 100

    return {
        "sprint_atual_nome": sprint_atual_nome,
        "bac": round(bac, 1),
        "ev_acumulado": round(acumulado_ev, 1),
        "spi_atual": spi_atual,
        "ultima_velocity": ultima_velocity,
        "score_zenhub": score_zenhub,
        "burnup_labels": burnup_labels,
        "burnup_pv": burnup_pv,
        "burnup_ev": burnup_ev,
        "burnup_ideal": burnup_ideal,
        "velocity_labels": velocity_labels,
        "velocity_data": velocity_data,
        "velocity_colors": velocity_colors,
        "spi_labels": spi_labels,
        "spi_data": spi_data,
        "spi_ref": [1.0] * len(spi_data),
        "sprints_lista_tabela": sprints_lista
    }