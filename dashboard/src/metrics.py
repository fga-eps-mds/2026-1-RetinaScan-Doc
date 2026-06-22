# src/metrics.py
import pandas as pd
from .config import WEIGHT_CODE_QUALITY, WEIGHT_TESTING_STATUS, WEIGHT_PSC1, WEIGHT_PSC2, WEIGHT_PC1, WEIGHT_PC2
from datetime import datetime, timezone, timedelta
import json

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
    """Calcula as métricas de AgileEVM expandidas incluindo SC e ETC."""
    def parse_iso(dt_str):
        if not dt_str: return None
        try:
            return datetime.fromisoformat(str(dt_str).replace("Z", "+00:00"))
        except Exception:
            return None

    if isinstance(sprints_raw, dict) and "sprints_velocity" in sprints_raw:
        sprints_dict_para_loop = sprints_raw.get("sprints_velocity", {})
    else:
        sprints_dict_para_loop = sprints_raw

    pipelines = sprints_raw.get("metrics_by_pipeline", {}) if isinstance(sprints_raw, dict) else {}
    issues_fechadas = pipelines.get("Closed", [])

    sprints_lista = []
    issues_ja_alocadas = set()

    for name, info in sprints_dict_para_loop.items():
        if isinstance(info, dict) and info.get("start_at") and info.get("end_at"):
            pontos_concluidos = float(info.get("delivered_story_points", info.get("delivered_sp", 0)))
            
            start_at = parse_iso(info["start_at"])
            end_at_original = parse_iso(info["end_at"])
            end_at_com_tolerancia = end_at_original + timedelta(days=2) if end_at_original else None
            
            issues_desta_sprint = []
            nome_sprint_limpo = str(name).strip().lower()
            
            for issue in issues_fechadas:
                issue_id = issue.get("number", "N/A")
                if issue_id in issues_ja_alocadas:
                    continue
                    
                data_fechamento = parse_iso(issue.get("closed_at"))
                sprints_da_issue = issue.get("sprints", [])
                
                primeira_sprint_nome = ""
                if sprints_da_issue:
                    f_sprint = sprints_da_issue[0]
                    if isinstance(f_sprint, dict):
                        primeira_sprint_nome = str(f_sprint.get("title", f_sprint.get("name", ""))).strip().lower()
                    else:
                        primeira_sprint_nome = str(f_sprint).strip().lower()
                
                vinculou = False
                if primeira_sprint_nome and (primeira_sprint_nome in nome_sprint_limpo or nome_sprint_limpo in primeira_sprint_nome):
                    vinculou = True
                elif data_fechamento and start_at and end_at_com_tolerancia:
                    if start_at <= data_fechamento <= end_at_com_tolerancia:
                        vinculou = True
                
                if vinculou:
                    issues_desta_sprint.append({
                        "number": issue_id,
                        "title": issue.get("title", "Sem título"),
                        "story_points": float(issue.get("story_points", 0))
                    })
                    issues_ja_alocadas.add(issue_id)

            if pontos_concluidos > 0 and not issues_desta_sprint:
                soma_acumulada = 0.0
                for issue in issues_fechadas:
                    issue_id = issue.get("number", "N/A")
                    sp_issue = float(issue.get("story_points", 0))
                    if issue_id not in issues_ja_alocadas and sp_issue > 0:
                        if soma_acumulada + sp_issue <= pontos_concluidos + 5:
                            issues_desta_sprint.append({
                                "number": issue_id,
                                "title": issue.get("title", "Sem título"),
                                "story_points": sp_issue
                            })
                            issues_ja_alocadas.add(issue_id)
                            soma_acumulada += sp_issue
                        if soma_acumulada >= pontos_concluidos:
                            break

            sprints_lista.append({
                "name": name,
                "start_at": start_at,
                "end_at_original": end_at_original,
                "end_at": end_at_com_tolerancia, 
                "pc_n": pontos_concluidos,         
                "delivered_sp": pontos_concluidos, 
                "pa_n": float(info.get("points_added", 0)), 
                "state_raw": info.get("state", "CLOSED").upper(),
                "issues": issues_desta_sprint
            })
            
    sprints_lista = sorted(sprints_lista, key=lambda x: x["start_at"] if x["start_at"] else datetime.min.replace(tzinfo=timezone.utc))
    
    PS = 5.0      
    PRP_0 = 79.0   
    bac = 16931.54 
    CUSTO_SEMANAL = 3386.31
    hoje = datetime.now(timezone.utc)
    
    burnup_labels = ["S7"]; burnup_pv = [0.0]; burnup_ev = [0.0]; burnup_ideal = [0.0]
    velocity_labels = []; velocity_data = []; velocity_colors = []
    spi_labels = []; spi_data = []
    
    sprint_atual_nome = "Não identificada"
    ultima_velocity = 0.0
    spi_atual = 1.0
    total_pa = 0.0  
    total_rpc = 0.0 
    acumulado_ac = 0.0
    etc_atual = bac

    linhas_auditoria_html = []
    linhas_tabela_status = []
    linhas_tabela_dados_grafico = []

    for idx, s in enumerate(sprints_lista):
        n = idx + 1  
        num_sprint_real = 8 + idx
        s_label = f"S{num_sprint_real}" 
        
        s_start = s["start_at"] if s["start_at"] else hoje
        s_end = s["end_at"] if s["end_at"] else hoje
        
        if s_start <= hoje <= s_end:
            s["state"] = "ACTIVE"
            sprint_atual_nome = s["name"]
        elif hoje > s_end:
            s["state"] = "CLOSED"
        else:
            s["state"] = "FUTURE"

        start_txt = s_start.strftime("%b%d") if s["start_at"] else "N/A"
        end_txt = s["end_at_original"].strftime("%b%d") if s["end_at_original"] else "N/A"
        
        burnup_labels.append(f"{s_label} ({start_txt})")
        velocity_labels.append(f"{s_label} ({start_txt})")
        
        total_pa += s["pa_n"]
        prp_n = PRP_0 + total_pa
        ppc = n / PS                                                                                                                                                                                                                                                                                                                                        
        
        pv_oficial = n * CUSTO_SEMANAL
        if pv_oficial > bac: pv_oficial = bac
        burnup_ideal.append(round((n / PS) * bac, 2))
        burnup_pv.append(round(pv_oficial, 2))
        
        pc_individual = s["pc_n"]
        
        if hoje >= s_start:
            total_rpc += s["pc_n"]
            apc_n = total_rpc / prp_n if prp_n > 0 else 0.0
            ev_oficial = apc_n * bac
            burnup_ev.append(round(ev_oficial, 2))
            velocity_data.append(s["pc_n"])
            velocity_colors.append("#185FA5") 
            
            sprint_cost = CUSTO_SEMANAL
            acumulado_ac += sprint_cost
            
            spi = ev_oficial / pv_oficial if pv_oficial > 0 else 1.0
            sv = ev_oficial - pv_oficial
            cv = ev_oficial - acumulado_ac
            cpi = ev_oficial / acumulado_ac if acumulado_ac > 0 else 1.0
            eac = acumulado_ac + ((bac - ev_oficial) / cpi) if cpi > 0 else bac
            
            etc = eac - acumulado_ac
            etc_atual = etc
            
            spi_data.append(round(spi, 2))
            spi_labels.append(s_label)
            
            if s["state"] != "ACTIVE":
                ultima_velocity = s["pc_n"]
                
            spi_audit_val = spi; ev_audit_val = ev_oficial; apc_audit_val = apc_n; rpc_audit_val = total_rpc
            
            txt_td_pv = f"{(n / PS) * 100:.0f}% &rarr; R$ {pv_oficial:,.2f}"
            txt_td_ev = f"{apc_audit_val * 100:.1f}% &rarr; R$ {ev_audit_val:,.2f}"
            txt_td_velocity = f"{pc_individual:.1f} SP"
            txt_td_spi = f"{spi_audit_val:.2f}"
        else:
            burnup_ev.append(None) 
            velocity_data.append(0) 
            velocity_colors.append("#D3D1C7") 
            sprint_cost = 0.0
            spi_audit_val = 0.0; ev_audit_val = 0.0; apc_audit_val = total_rpc / prp_n if prp_n > 0 else 0.0; rpc_audit_val = total_rpc
            cv = 0.0; sv = 0.0; cpi = 0.0; eac = 0.0; etc = 0.0
            
            txt_td_pv = f"{(n / PS) * 100:.0f}% &rarr; R$ {pv_oficial:,.2f}"
            txt_td_ev = "- &rarr; -"
            txt_td_velocity = "0 SP"
            txt_td_spi = "-"

        linhas_tabela_dados_grafico.append(f"""
        <tr>
            <td>{s_label} ({start_txt})</td>
            <td>{txt_td_pv}</td>
            <td>{txt_td_ev}</td>
            <td>{txt_td_velocity}</td>
            <td>{txt_td_spi}</td>
        </tr>
        """)

        pill_class = 'pill-ok' if s["state"] == "CLOSED" else 'pill-warn' if s["state"] == "ACTIVE" else 'pill-fut'
        linhas_tabela_status.append(f"""
        <tr>
            <td>{s_label}</td>
            <td>{end_txt}</td>
            <td>{pc_individual:.1f} SP</td>
            <td><span class="pill {pill_class}">{s["state"]}</span></td>
        </tr>
        """)

        linhas_issues_html = []
        lista_issues = s.get("issues", [])
        if lista_issues:
            for issue in lista_issues:
                num = issue.get("number", "N/A")
                title = issue.get("title", "Sem título").replace("'", '"').replace("\n", " ")
                sp = issue.get("story_points", 0.0)
                linhas_issues_html.append(
                    f"<tr>"
                    f"  <td style='padding:6px 8px; border-bottom:0.5px solid var(--color-border-secondary);'><code>#{num}</code></td>"
                    f"  <td style='text-align:left; padding:6px 8px; border-bottom:0.5px solid var(--color-border-secondary);'>{title}</td>"
                    f"  <td style='padding:6px 8px; border-bottom:0.5px solid var(--color-border-secondary);'><b>{sp:.1f} SP</b></td>"
                    f"</tr>"
                )
            sub_tabela_html = f"""
            <table class="sprint-table" style="margin: 5px 0; background: var(--color-background-secondary); width:100%; border-collapse:collapse;">
                <thead>
                    <tr style="background: var(--color-border-tertiary);">
                        <th style="width: 15%; padding:4px;">Issue</th>
                        <th style="text-align:left; width: 65%; padding:4px;">Título</th>
                        <th style="width: 20%; padding:4px;">Story Points</th>
                    </tr>
                </thead>
                <tbody>{"".join(linhas_issues_html)}</tbody>
            </table>
            """
        else:
            sub_tabela_html = "<p style='margin:5px; font-size:11px; color:gray; font-style: italic;'>Nenhuma issue fechada vinculada a esta Sprint.</p>"

        linhas_auditoria_html.append(f"""
        <tr onclick="document.getElementById('details-{s_label}').style.display = document.getElementById('details-{s_label}').style.display === 'none' ? 'table-row' : 'none'" style="cursor:pointer;" title="Clique para ver as issues detalhadas">
            <td><b>{s_label} 🔍</b></td>
            <td>{PRP_0:.1f} SP</td>
            <td>R$ {bac:,.2f}</td>
            <td>{s["pa_n"]:.1f} SP</td>
            <td>{prp_n:.1f} SP</td>
            <td>{PS:.1f} SP</td>
            <td>{ppc:.2f}</td>
            <td>{pc_individual:.1f} SP</td>
            <td>{rpc_audit_val:.1f} SP</td>
            <td>{apc_audit_val:.2f}</td>
            <td>R$ {pv_oficial:,.2f}</td>
            <td>R$ {ev_audit_val:,.2f}</td>
            <td>R$ {sprint_cost:,.2f}</td>
            <td>R$ {acumulado_ac:,.2f}</td>
            <td>R$ {cv:,.2f}</td>
            <td>R$ {sv:,.2f}</td>
            <td>{cpi:.2f}</td>
            <td>{spi_audit_val:.2f}</td>
            <td>R$ {eac:,.2f}</td>
            <td>R$ {etc:,.2f}</td>
        </tr>
        <tr id="details-{s_label}" style="display:none; background-color: var(--color-background-secondary);">
            <td colspan="20" style="padding: 10px 15px; text-align: left; border-bottom: 1px solid var(--color-border-tertiary);">
                <div style="font-weight: 600; color: #185FA5; margin-bottom: 5px; font-size:12px;">Issues que compõem o PC ({pc_individual:.1f} SP):</div>
                {sub_tabela_html}
            </td>
        </tr>
        """)

    if spi_data: spi_atual = spi_data[-1]
    score_zenhub = max(0, min(100, int(spi_atual * 100)))

    return {
        "sprint_atual_nome": sprint_atual_nome, 
        "bac": bac,
        "ev_acumulado": round(total_rpc / (PRP_0 + total_pa) * bac if (PRP_0 + total_pa) > 0 else 0.0, 2),
        "spi_atual": spi_atual, 
        "ultima_velocity": ultima_velocity, 
        "score_zenhub": score_zenhub,
        "etc_atual": round(etc_atual, 2),
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
        "sprints_lista_tabela": sprints_lista, 
        "tabela_dados_grafico_linhas": "\n".join(linhas_tabela_dados_grafico),
        "tabela_linhas": "\n".join(linhas_tabela_status),
        "tabela_auditoria_evm": "\n".join(linhas_auditoria_html)
    }