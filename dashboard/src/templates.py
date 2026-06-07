# No seu arquivo de visualização/dashboard (onde está o build_product_html_template)
import streamlit as st

def inject_custom_css():
    st.markdown("""
    <style>
    .qh{display:flex;align-items:center;gap:10px;margin-bottom:1.25rem;padding-top:1rem}
    .qa{width:8px;height:36px;background:#534AB7;border-radius:3px;flex-shrink:0}
    .qt{font-size:16px;font-weight:500;margin:0}
    .qs{font-size:12px;color:var(--color-text-secondary);margin:0}
    .qb{margin-left:auto;font-size:11px;background:#EEEDFE;color:#3C3489;padding:3px 10px;border-radius:var(--border-radius-md)}
    .kgq{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin-bottom:1.25rem}
    .kpq{background:var(--color-background-secondary);border-radius:var(--border-radius-md);padding:12px 14px}
    .knum{font-size:20px;font-weight:500}
    
    /* CLASSES PARA A NOVA MEMÓRIA DE CÁLCULO INTEGRADA */
    .f-card {background:var(--color-background-primary);border:0.5px solid var(--color-border-tertiary);border-radius:var(--border-radius-lg);padding:1rem 1.25rem;margin-bottom:1.25rem}
    .f-title {font-size:12px;font-weight:600;color:var(--color-text-primary);margin:0 0 10px 0;text-transform:uppercase;letter-spacing:0.5px}
    .f-grid {display:grid;grid-template-columns:repeat(2,1fr);gap:12px;font-size:11px;color:var(--color-text-secondary);background:var(--color-background-secondary);padding:12px;border-radius:var(--border-radius-md);border:0.5px solid var(--color-border-tertiary)}
    .f-item {line-height:1.5}
    .f-item code {background:#EEEDFE;padding:2px 5px;border-radius:3px;font-family:monospace;color:#3C3489;font-weight:600;font-size:10.5px}
    .f-math {font-family:"Courier New", monospace;font-weight:bold;color:var(--color-text-primary);display:block;margin:4px 0}
    
    .qcard{background:var(--color-background-primary);border:0.5px solid var(--color-border-tertiary);border-radius:var(--border-radius-lg);padding:1rem 1.25rem}
    .qct{font-size:13px;font-weight:500;color:var(--color-text-primary);margin:0 0 12px}
    .si-row{display:flex;align-items:stretch;gap:12px;margin-bottom:1rem}
    .si-label{writing-mode:vertical-rl;text-orientation:mixed;transform:rotate(180deg);font-size:11px;font-weight:500;color:var(--color-text-secondary);display:flex;align-items:center;justify-content:center;padding:4px 0;min-width:22px;border-right:2px solid var(--color-border-secondary)}
    .si-body{flex:1;display:flex;flex-direction:column;gap:6px}
    .factor-row{display:grid;grid-template-columns:140px 1fr;gap:8px;align-items:start}
    .factor-label{font-size:11px;color:var(--color-text-secondary);padding-top:4px;line-height:1.4}
    .metrics-group{display:flex;flex-direction:column;gap:4px}
    .metric-item{display:flex;align-items:center;gap:8px}
    .m-dot{width:10px;height:10px;border-radius:50%;flex-shrink:0}
    .dot-green{background:#1D9E75}
    .dot-yellow{background:#EF9F27}
    .dot-red{background:#E24B4A}
    .m-name{font-size:11px;color:var(--color-text-primary);flex:1}
    .m-val{font-size:11px;font-weight:500;min-width:36px;text-align:right}
    .m-bar-wrap{width:80px;height:6px;background:var(--color-background-secondary);border-radius:3px;overflow:hidden}
    .m-bar{height:100%;border-radius:3px}
    .divider{height:0.5px;background:var(--color-border-tertiary);margin:6px 0}
    .legend-row{display:flex;gap:14px;font-size:11px;color:var(--color-text-secondary);margin-bottom:10px;align-items:center}
    .legend-row span{display:flex;align-items:center;gap:5px}
    .legend-row b{width:10px;height:10px;border-radius:50%;display:inline-block}
    </style>
    """, unsafe_allow_html=True)

def get_semaphore_color(value: float, max_value: float = 1.0) -> tuple:
    pct = value / max_value if max_value > 0 else 0
    if pct >= 0.75:
        return "#1D9E75", "dot-green"
    elif pct >= 0.50:
        return "#EF9F27", "dot-yellow"
    else:
        return "#E24B4A", "dot-red"

def build_product_html_template(repo_key, ultima_sprint) -> str:
    cor_total, _ = get_semaphore_color(ultima_sprint['total'], max_value=1.0)
    cor_maint, class_maint = get_semaphore_color(ultima_sprint['Maintainability'], max_value=0.5)
    cor_rel, class_rel = get_semaphore_color(ultima_sprint['Reliability'], max_value=0.5)
    
    _, class_comp = get_semaphore_color(ultima_sprint['complexity'])
    _, class_comm = get_semaphore_color(ultima_sprint['comments'])
    _, class_dup = get_semaphore_color(ultima_sprint['duplication'])
    _, class_ts = get_semaphore_color(ultima_sprint['test_success'])
    _, class_fast = get_semaphore_color(ultima_sprint['fast_tests'])
    _, class_cov = get_semaphore_color(ultima_sprint['coverage'])

    width_total = ultima_sprint['total'] * 100
    width_maint = (ultima_sprint['Maintainability'] / 0.5) * 100
    width_rel = (ultima_sprint['Reliability'] / 0.5) * 100

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <style>
    :root {{
        --color-background-primary: #ffffff;
        --color-background-secondary: #f8f9fa;
        --color-border-secondary: #e9ecef;
        --color-border-tertiary: #dee2e6;
        --color-text-primary: #212529;
        --color-text-secondary: #495057;
        --color-text-tertiary: #6c757d;
    }}
    body {{ font-family: sans-serif; margin: 0; padding: 10px; background: transparent; }}
    
    .db-header {{ display:flex; align-items:center; gap:10px; margin-bottom:1.25rem; padding-top:1rem; }}
    .db-accent {{ width:8px; height:36px; background:#534AB7; border-radius:3px; flex-shrink:0; }}
    .db-title {{ font-size:16px; font-weight:500; color:var(--color-text-primary); margin:0; }}
    .db-sub {{ font-size:12px; color:var(--color-text-secondary); margin:0; }}
    .db-badge {{ margin-left:auto; font-size:11px; background:#EEEDFE; color:#3C3489; padding:3px 10px; border-radius:4px; }}
    
    .kpi-grid {{ display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:10px; margin-bottom:1.25rem; }}
    .kpi {{ background:var(--color-background-secondary); border-radius:4px; padding:12px 14px; border: 0.5px solid var(--color-border-tertiary); }}
    .kpi-label {{ font-size:11px; color:var(--color-text-secondary); margin-bottom:4px; }}
    .kpi-val {{ font-size:22px; font-weight:500; }}

    .card {{ background:var(--color-background-primary); border:0.5px solid var(--color-border-tertiary); border-radius:8px; padding:1rem 1.25rem; margin-bottom: 1rem; }}
    .card-title {{ font-size:13px; font-weight:500; color:var(--color-text-primary); margin:0; }}
    
    /* CAIXA DA MEMÓRIA DE CÁLCULO IDENTICA AO DO EVM */
    .formula-box {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; font-size: 11.5px; color: var(--color-text-secondary); background: var(--color-background-secondary); padding: 12px; border-radius: 6px; border: 0.5px solid var(--color-border-tertiary); margin-bottom: 0.5rem; }}
    .formula-item {{ padding: 4px; line-height: 1.4; }}
    .formula-item code {{ background: #EEEDFE; padding: 2px 5px; border-radius: 3px; font-family: monospace; color: #3C3489; font-weight: bold; font-size: 11px; }}

    .si-row {{ display: flex; align-items: stretch; gap: 12px; margin-top: 10px; }}
    .si-label {{ writing-mode: vertical-rl; text-orientation: mixed; transform: rotate(180deg); font-size: 11px; font-weight: 500; color: var(--color-text-secondary); display: flex; align-items: center; justify-content: center; padding: 4px 0; min-width: 22px; border-right: 2px solid var(--color-border-secondary); }}
    .si-body {{ flex: 1; display: flex; flex-direction: column; gap: 6px; }}
    
    .factor-row {{ display: grid; grid-template-columns: 140px 1fr; gap: 8px; align-items: start; }}
    .factor-label {{ font-size: 11px; color: var(--color-text-secondary); padding-top: 4px; line-height: 1.4; }}
    .metrics-group {{ display: flex; flex-direction: column; gap: 4px; }}
    .metric-item {{ display: flex; align-items: center; gap: 8px; }}
    
    .m-dot {{ width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; }}
    .dot-green {{ background: #1D9E75; }}
    .dot-yellow {{ background: #EF9F27; }}
    .dot-red {{ background: #E24B4A; }}
    
    .m-name {{ font-size: 11px; color: var(--color-text-primary); flex: 1; }}
    .m-val {{ font-size: 11px; font-weight: 500; min-width: 36px; text-align: right; }}
    .m-bar-wrap {{ width: 80px; height: 6px; background: var(--color-background-secondary); border-radius: 3px; overflow: hidden; border: 0.5px solid var(--color-border-tertiary); }}
    .m-bar {{ height: 100%; border-radius: 3px; }}
    .divider {{ height: 0.5px; background: var(--color-border-tertiary); margin: 6px 0; }}
    
    .legend {{ display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 8px; font-size: 11px; color: var(--color-text-secondary); }}
    .legend span {{ display: flex; align-items: center; gap: 5px; }}
    .legend b {{ width: 10px; height: 10px; display: inline-block; border-radius: 50%; }}
    </style>
    </head>
    <body>

    <div class="db-header">
      <div class="db-accent"></div>
      <div>
        <p class="db-title">Eixo Produto — modelo Q-Rapids sobre dados SonarQube / GitHub</p>
        <p class="db-sub">Métricas do repositório <strong>{repo_key}</strong> · {int(ultima_sprint['ncloc'])} NCLOC</p>
      </div>
      <div class="db-badge">Versão atual: {ultima_sprint['version']}</div>
    </div>

    <div class="kpi-grid">
      <div class="kpi">
        <div class="klq">Indicador estratégico</div>
        <div class="kvq">Product Quality (Total Score)</div>
        <div class="knum" style="color:{cor_total}">{ultima_sprint['total']:.2f}</div>
        <div style="height:4px;background:var(--color-border-secondary);border-radius:2px;margin-top:6px;overflow:hidden">
            <div style="width:{width_total:.1f}%;height:100%;background:{cor_total};border-radius:2px"></div>
        </div>
      </div>

      <div class="kpi">
        <div class="klq">Fator de Qualidade</div>
        <div class="kvq">Maintainability (Manutenibilidade)</div>
        <div class="knum" style="color:{cor_maint}">{ultima_sprint['Maintainability']:.2f}</div>
        <div style="height:4px;background:var(--color-border-secondary);border-radius:2px;margin-top:6px;overflow:hidden">
            <div style="width:{width_maint:.1f}%;height:100%;background:{cor_maint};border-radius:2px"></div>
        </div>
      </div>

      <div class="kpi">
        <div class="klq">Fator de Qualidade</div>
        <div class="kvq">Reliability (Confiabilidade)</div>
        <div class="knum" style="color:{cor_rel}">{ultima_sprint['Reliability']:.2f}</div>
        <div style="height:4px;background:var(--color-border-secondary);border-radius:2px;margin-top:6px;overflow:hidden">
            <div style="width:{width_rel:.1f}%;height:100%;background:{cor_rel};border-radius:2px"></div>
        </div>
      </div>
    </div>

    <div class="card">
      <p class="card-title" style="margin-bottom: 8px;">Memória de Cálculo &amp; Fórmulas Utilizadas</p>
      <div class="formula-box">
        <div class="formula-item">
          <code>Code Quality</code> = (Complexity * 0.33) + (Comments * 0.33) + (Duplication * 0.33) <br>
          <small style="color:var(--color-text-tertiary)">Mapeia a conformidade de arquivos (FIL) para complexidade &le; 10, comentários 10-30% e duplicação &lt; 5%.</small>
        </div>
        <div class="formula-item">
          <code>Testing Status</code> = (Test Success * 0.25) + (Fast Tests * 0.25) + (Coverage * 0.50) <br>
          <small style="color:var(--color-text-tertiary)">Mapeia suítes de testes (UTS) 100% estáveis, execuções rápidas (&lt; 5 min) e arquivos com cobertura &gt; 60%.</small>
        </div>
        <div class="formula-item">
          <code>Maintainability</code> = Code Quality &times; 0.50 <br>
          <small style="color:var(--color-text-tertiary)">Fator de peso regulamentado pela constante PC1 sobre os indicadores de qualidade de código.</small>
        </div>
        <div class="formula-item">
          <code>Reliability</code> = Testing Status &times; 0.50 <br>
          <small style="color:var(--color-text-tertiary)">Fator de peso regulamentado pela constante PC2 sobre o ecossistema de testes.</small>
        </div>
      </div>
    </div>

    <div class="card">
      <p class="card-title" style="margin-bottom: 10px;">Fatores e métricas avaliadas — Product Quality</p>
      
      <div class="legend" style="margin-bottom: 12px;">
        <span><b class="dot-green"></b> verde &ge; 0.75 (aprovado)</span>
        <span><b class="dot-yellow"></b> amarelo 0.50–0.74 (atenção)</span>
        <span><b class="dot-red"></b> vermelho &lt; 0.50 (crítico)</span>
      </div>
      
      <div class="si-row">
        <div class="si-label">Product Quality</div>
        <div class="si-body">
        
          <div class="factor-row">
            <div class="factor-label">Code Quality<br><small style="color:var(--color-text-tertiary)">Maintainability · SonarQube</small></div>
            <div class="metrics-group">
              <div class="metric-item">
                <span class="m-dot {class_comp}"></span>
                <span class="m-name">Complexity — arquivos não complexos (ciclomática/função &le; 10)</span>
                <div class="m-bar-wrap"><div class="m-bar" style="width:{ultima_sprint['complexity']*100:.0f}%; background:{"#1D9E75" if class_comp=="dot-green" else "#EF9F27" if class_comp=="dot-yellow" else "#E24B4A"}"></div></div>
                <span class="m-val" style="color:{"#1D9E75" if class_comp=="dot-green" else "#EF9F27" if class_comp=="dot-yellow" else "#E24B4A"}">{ultima_sprint['complexity']:.2f}</span>
              </div>
              <div class="metric-item">
                <span class="m-dot {class_comm}"></span>
                <span class="m-name">Comments — arquivos com linhas de comentários aceitáveis (&lt; 30%)</span>
                <div class="m-bar-wrap"><div class="m-bar" style="width:{ultima_sprint['comments']*100:.0f}%; background:{"#1D9E75" if class_comm=="dot-green" else "#EF9F27" if class_comm=="dot-yellow" else "#E24B4A"}"></div></div>
                <span class="m-val" style="color:{"#1D9E75" if class_comm=="dot-green" else "#EF9F27" if class_comm=="dot-yellow" else "#E24B4A"}">{ultima_sprint['comments']:.2f}</span>
              </div>
              <div class="metric-item">
                <span class="m-dot {class_dup}"></span>
                <span class="m-name">Duplication — arquivos com &lt; 5% linhas duplicadas</span>
                <div class="m-bar-wrap"><div class="m-bar" style="width:{ultima_sprint['duplication']*100:.0f}%; background:{"#1D9E75" if class_dup=="dot-green" else "#EF9F27" if class_dup=="dot-yellow" else "#E24B4A"}"></div></div>
                <span class="m-val" style="color:{"#1D9E75" if class_dup=="dot-green" else "#EF9F27" if class_dup=="dot-yellow" else "#E24B4A"}">{ultima_sprint['duplication']:.2f}</span>
              </div>
            </div>
          </div>
          
          <div class="divider"></div>
          
          <div class="factor-row">
            <div class="factor-label">Testing Status<br><small style="color:var(--color-text-tertiary)">Reliability · SonarQube</small></div>
            <div class="metrics-group">
              <div class="metric-item">
                <span class="m-dot {class_ts}"></span>
                <span class="m-name">Test success — (unit tests &minus; erros &minus; falhas) / unit tests</span>
                <div class="m-bar-wrap"><div class="m-bar" style="width:{ultima_sprint['test_success']*100:.0f}%; background:{"#1D9E75" if class_ts=="dot-green" else "#EF9F27" if class_ts=="dot-yellow" else "#E24B4A"}"></div></div>
                <span class="m-val" style="color:{"#1D9E75" if class_ts=="dot-green" else "#EF9F27" if class_ts=="dot-yellow" else "#E24B4A"}">{ultima_sprint['test_success']:.2f}</span>
              </div>
              <div class="metric-item">
                <span class="m-dot {class_fast}"></span>
                <span class="m-name">Fast tests — builds de testes rápidos (&lt; 5 min)</span>
                <div class="m-bar-wrap"><div class="m-bar" style="width:{ultima_sprint['fast_tests']*100:.0f}%; background:{"#1D9E75" if class_fast=="dot-green" else "#EF9F27" if class_fast=="dot-yellow" else "#E24B4A"}"></div></div>
                <span class="m-val" style="color:{"#1D9E75" if class_fast=="dot-green" else "#EF9F27" if class_fast=="dot-yellow" else "#E24B4A"}">{ultima_sprint['fast_tests']:.2f}</span>
              </div>
              <div class="metric-item">
                <span class="m-dot {class_cov}"></span>
                <span class="m-name">Coverage — arquivos com cobertura de código ideal (&gt; 60%)</span>
                <div class="m-bar-wrap"><div class="m-bar" style="width:{ultima_sprint['coverage']*100:.0f}%; background:{"#1D9E75" if class_cov=="dot-green" else "#EF9F27" if class_cov=="dot-yellow" else "#E24B4A"}"></div></div>
                <span class="m-val" style="color:{"#1D9E75" if class_cov=="dot-green" else "#EF9F27" if class_cov=="dot-yellow" else "#E24B4A"}">{ultima_sprint['coverage']:.2f}</span>
              </div>
            </div>
          </div>
          
        </div>
      </div>
    </div>
    </body>
    </html>
    """


PROJECT_EVM_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
:root {
    --color-background-primary: #ffffff;
    --color-background-secondary: #f8f9fa;
    --color-border-secondary: #e9ecef;
    --color-border-tertiary: #dee2e6;
    --color-text-primary: #212529;
    --color-text-secondary: #495057;
    --color-text-tertiary: #6c757d;
}
body { font-family: sans-serif; margin: 0; padding: 10px; background: transparent; }
.db-header { display:flex; align-items:center; gap:10px; margin-bottom:1.25rem; padding-top:1rem; }
.db-accent { width:8px; height:36px; background:#185FA5; border-radius:3px; flex-shrink:0; }
.db-title { font-size:16px; font-weight:500; color:var(--color-text-primary); margin:0; }
.db-sub { font-size:12px; color:var(--color-text-secondary); margin:0; }
.db-badge { margin-left:auto; font-size:11px; background:#E6F1FB; color:#0C447C; padding:3px 10px; border-radius:4px; }
.kpi-grid { display:grid; grid-template-columns:repeat(5,minmax(0,1fr)); gap:10px; margin-bottom:1.25rem; }
.kpi { background:var(--color-background-secondary); border-radius:4px; padding:12px 14px; border: 0.5px solid var(--color-border-tertiary); }
.kpi-label { font-size:11px; color:var(--color-text-secondary); margin-bottom:4px; }
.kpi-val { font-size:22px; font-weight:500; }

.card { background:var(--color-background-primary); border:0.5px solid var(--color-border-tertiary); border-radius:8px; padding:1rem 1.25rem; margin-bottom: 1rem; }
.card-header-flex { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }
.card-title { font-size:13px; font-weight:500; color:var(--color-text-primary); margin:0; }
.legend { display:flex; flex-wrap:wrap; gap:12px; margin-bottom:8px; font-size:11px; color:var(--color-text-secondary); }
.legend span { display:flex; align-items:center; gap:5px; }
.legend b { width:20px; height:3px; display:inline-block; border-radius:2px; }

.sprint-table { width:100%; font-size:12px; border-collapse:collapse; }
.sprint-table th { text-align:left; font-weight:500; color:var(--color-text-secondary); padding:6px 8px; border-bottom:1px solid var(--color-border-tertiary); font-size:11px; background: var(--color-background-secondary); }
.sprint-table td { padding:6px 8px; border-bottom:0.5px solid var(--color-border-secondary); color:var(--color-text-primary); }
.sprint-table tr:last-child td { border-bottom:none; }

.formula-box { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; font-size: 11.5px; color: var(--color-text-secondary); background: var(--color-background-secondary); padding: 12px; border-radius: 6px; border: 0.5px solid var(--color-border-tertiary); margin-bottom: 0.5rem; }
.formula-item { padding: 4px; line-height: 1.4; }
.formula-item code { background: #eef1f6; padding: 2px 5px; border-radius: 3px; font-family: monospace; color: #0c447c; font-weight: bold; font-size: 11px; }

.pill { font-size:10px; padding:2px 7px; border-radius:10px; font-weight:500; }
.pill-ok { background:#EAF3DE; color:#27500A; }
.pill-warn { background:#FAEEDA; color:#633806; }
.pill-bad { background:#FCEBEB; color:#791F1F; }
.pill-fut { background:#F1EFE8; color:#444441; }

.btn-export { background: #185FA5; color: #fff; border: none; padding: 4px 10px; font-size: 11px; font-weight: 500; border-radius: 4px; cursor: pointer; display: flex; align-items: center; gap: 4px; }
.btn-export:hover { background: #0c447c; }
</style>
</head>
<body>

<div class="db-header">
  <div class="db-accent"></div>
  <div>
    <p class="db-title">Eixo Projeto — Agile EVM &amp; acompanhamento de releases</p>
    <p class="db-sub">Release Major 3</p>
  </div>
  <div class="db-badge">Sprint atual: __SPRINT_ATUAL_NOME__</div>
</div>

<div class="kpi-grid">
  <div class="kpi"><div class="kpi-label">BAC (SP planejados)</div><div class="kpi-val" style="color:var(--color-text-primary)">__KPI_BAC__</div></div>
  <div class="kpi"><div class="kpi-label">EV acumulado</div><div class="kpi-val" style="color:#185FA5">__KPI_EV__</div></div>
  <div class="kpi"><div class="kpi-label">SPI</div><div class="kpi-val" style="color:#3B6D11">__KPI_SPI__</div></div>
  <div class="kpi"><div class="kpi-label">Velocity (última sprint)</div><div class="kpi-val" style="color:#185FA5">__KPI_VELOCITY__ SP</div></div>
  <div class="kpi"><div class="kpi-label">Score ZenHub</div><div class="kpi-val" style="color:#639922">__KPI_SCORE__</div></div>
</div>

<div class="card">
  <p class="card-title" style="margin-bottom: 8px;">Memória de Cálculo &amp; Fórmulas Utilizadas</p>
  <div class="formula-box">
    <div class="formula-item">
      <code>BAC</code> <b>Budget at Completion</b> = Total de Story Points planejados para o escopo inicial da Release 3.
    </div>
    <div class="formula-item">
      <code>PV</code> <b>Planned Value</b> = <i>BAC</i> &times; <i>PPC</i> <br>
      <small style="color:var(--color-text-tertiary)">(Onde Progresso Planejado <i>PPC</i> = Sprint Atual / Total de Sprints)</small>
    </div>
    <div class="formula-item">
      <code>EV</code> <b>Earned Value</b> = <i>BAC</i> &times; <i>APC</i> <br>
      <small style="color:var(--color-text-tertiary)">(Onde Progresso Real <i>APC</i> = Pontos Entregues Acumulados / Escopo Updated)</small>
    </div>
    <div class="formula-item">
      <code>SPI</code> <b>Schedule Performance Index</b> = <i>EV</i> / <i>PV</i> <br>
      <small style="color:var(--color-text-tertiary)">(Mede a eficiência do cronograma. Valores &ge; 1.0 indicam adiantamento)</small>
    </div>
  </div>
</div>

<div class="card">
  <p class="card-title">Tabela de Rastreabilidade do Agile EVM</p>
  <table class="sprint-table" style="margin-top: 5px;">
    <thead>
      <tr>
        <th>Sprint</th>
        <th>Planejado (PPC &rarr; PV)</th>
        <th>Entregue Acumulado (APC &rarr; EV)</th>
        <th>Ideal Teórico</th>
        <th>Velocity (Sprint)</th>
        <th>SPI (Eficiência)</th>
      </tr>
    </thead>
    <tbody>
      __TABELA_DADOS_GRAFICO_LINHAS__
    </tbody>
  </table>
</div>

<div style="display:grid; grid-template-columns:3fr 2fr; gap:14px; margin-bottom:1rem;">
  <div class="card">
    <p class="card-title">Burnup — Story points planejados × entregues por sprint</p>
    <div class="legend">
      <span><b style="background:#B5D4F4"></b> PV (planejado)</span>
      <span><b style="background:#185FA5"></b> EV (realizado)</span>
      <span><b style="background:#D3D1C7; border-top:2px dashed #D3D1C7; height:0"></b> Ideal</span>
    </div>
    <div style="position:relative;width:100%;height:190px;">
      <canvas id="burnupC" role="img"></canvas>
    </div>
  </div>
  <div class="card">
    <p class="card-title">Velocity por sprint (SP entregues)</p>
    <div style="position:relative;width:100%;height:190px;">
      <canvas id="velC" role="img"></canvas>
    </div>
  </div>
</div>

<div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-bottom:1rem;">
  <div class="card">
    <p class="card-title">SPI por sprint</p>
    <div class="legend">
      <span><b style="background:#185FA5"></b> SPI</span>
      <span><b style="background:#B4B2A9; border-top:2px dashed #B4B2A9; height:0"></b> Referência 1.0</span>
    </div>
    <div style="position:relative;width:100%;height:150px;">
      <canvas id="spiC" role="img"></canvas>
    </div>
  </div>
  <div class="card">
    <p class="card-title">Sprints — status</p>
    <table class="sprint-table">
      <thead><tr><th>Sprint</th><th>Due</th><th>SP Entregues</th><th>Status</th></tr></thead>
      <tbody>
        __TABELA_LINHAS__
      </tbody>
    </table>
  </div>
</div>

<div class="card">
  <div class="card-header-flex">
    <p class="card-title">Mapeamento e Auditoria Completa de Siglas do Agile EVM</p>
    <button class="btn-export" onclick="exportTableToCSV('agile_evm_metrics.csv')">
      📥 Exportar CSV
    </button>
  </div>
  <table class="sprint-table" id="auditTable" style="text-align: center;">
    <thead>
      <tr>
        <th style="text-align: center;">Sprint</th>
        <th style="text-align: center;">PRP₀</th>
        <th style="text-align: center;">BAC</th>
        <th style="text-align: center;">PA</th>
        <th style="text-align: center;">PRPₙ</th>
        <th style="text-align: center;">PS</th>
        <th style="text-align: center;">PPC</th>
        <th style="text-align: center;">RPC</th>
        <th style="text-align: center;">APC</th>
        <th style="text-align: center;">PV</th>
        <th style="text-align: center;">EV</th>
        <th style="text-align: center;">SPI</th>
      </tr>
    </thead>
    <tbody>
      __TABELA_AUDITORIA_EVM__
    </tbody>
  </table>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<script>
const isDark = matchMedia('(prefers-color-scheme: dark)').matches;
const grid = isDark ? 'rgba(255,255,255,0.08)' : 'rgba(0,0,0,0.06)';
const txtColor = isDark ? '#aaa' : '#888';
const baseOpts = { responsive:true, maintainAspectRatio:false, plugins:{ legend:{ display:false } }, scales:{ x:{ grid:{ color:grid }, ticks:{ color:txtColor, font:{ size:11 } } }, y:{ grid:{ color:grid }, ticks:{ color:txtColor, font:{ size:11 } } } } };

new Chart(document.getElementById('burnupC'), {
  type:'line',
  data:{
    labels: __BURNUP_LABELS__,
    datasets:[
      { label:'PV', data: __BURNUP_PV__, borderColor:'#B5D4F4', backgroundColor:'rgba(181,212,244,0.15)', borderWidth:2, pointRadius:4, pointBackgroundColor:'#B5D4F4', tension:0.1 },
      { label:'EV', data: __BURNUP_EV__, borderColor:'#185FA5', backgroundColor:'rgba(24,95,165,0.08)', borderWidth:2.5, pointRadius:5, pointBackgroundColor:'#185FA5', tension:0.1, spanGaps: true },
      { label:'Ideal', data: __BURNUP_IDEAL__, borderColor:'#D3D1C7', borderWidth:1.5, borderDash:[5,4], pointRadius:0, fill:false, tension:0 }
    ]
  },
  options:{ ...baseOpts, scales:{ x:{ grid:{ color:grid }, ticks:{ color:txtColor, font:{ size:10 }, maxRotation:0 } }, y:{ grid:{ color:grid }, ticks:{ color:txtColor, font:{ size:11 } }, min:0, title:{ display:true, text:'Story Points', color:txtColor, font:{ size:10 } } } } }
});

new Chart(document.getElementById('velC'), {
  type:'bar',
  data:{
    labels: __VELOCITY_LABELS__,
    datasets:[{ label:'Velocity', data: __VELOCITY_DATA__, backgroundColor: __VELOCITY_COLORS__, borderRadius:4 }]
  },
  options:{ ...baseOpts, scales:{ x:{ grid:{ color:grid }, ticks:{ color:txtColor, font:{ size:10 }, maxRotation:0 } }, y:{ grid:{ color:grid }, ticks:{ color:txtColor, font:{ size:11 } }, min:0, title:{ display:true, text:'SP entregues', color:txtColor, font:{ size:10 } } } } }
});

new Chart(document.getElementById('spiC'), {
  type:'line',
  data:{
    labels: __SPI_LABELS__,
    datasets:[
      { label:'SPI', data: __SPI_DATA__, borderColor:'#185FA5', backgroundColor:'rgba(24,95,165,0.1)', borderWidth:2.5, pointRadius:5, pointBackgroundColor:'#185FA5', tension:0.2, fill:true },
      { label:'Ref 1.0', data: __SPI_REF__, borderColor:'#B4B2A9', borderWidth:1.5, borderDash:[5,4], pointRadius:0, fill:false }
    ]
  },
  options:{ ...baseOpts, scales:{ x:{ grid:{ color:grid }, ticks:{ color:txtColor, font:{ size:11 } } }, y:{ grid:{ color:grid }, ticks:{ color:txtColor, font:{ size:11 }, callback: v => v.toFixed(2) }, min:0, max:3.0 } } }
});

function exportTableToCSV(filename) {
    var csv = [];
    var rows = document.querySelectorAll("#auditTable tr");
    
    for (var i = 0; i < rows.length; i++) {
        var row = [], cols = rows[i].querySelectorAll("td, th");
        for (var j = 0; j < cols.length; j++) {
            let text = cols[j].innerText.trim();
            if (text.includes(';')) {
                text = '"' + text + '"';
            }
            row.push(text);
        }
        csv.push(row.join(";"));
    }

    // Usa String.fromCharCode(10) para pular de linha sem usar caracteres de barra que dão conflito no Python
    var quebraLinha = String.fromCharCode(10);
    var csvContent = String.fromCharCode(65279) + csv.join(quebraLinha);
    var csvFile = new Blob([csvContent], {type: "text/csv;charset=utf-8;"});
    
    var downloadLink = document.createElement("a");
    downloadLink.download = filename;
    downloadLink.href = window.URL.createObjectURL(csvFile);
    downloadLink.style.display = "none";
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
}
</script>
</body>
</html>
"""