import streamlit as st
import pandas as pd
from glob import glob
from datetime import datetime, timedelta, timezone
import plotly.graph_objects as go
import json
import os

# REVISADO: Removido o ISSUES_FILES_PATH que não é mais necessário no escopo principal
from src.config import REPO_BASE_NAME, REPOS_LANGUAGE, SONAR_FILES_PATH
from src.data_layer import build_raw_components_dataframe, load_zenhub_sprints_raw
from src.metrics import build_aggregated_metrics_dataframe, calculate_scrum_evm_metrics, calculate_process_metrics
from src.templates import inject_custom_css, build_product_html_template, PROJECT_EVM_TEMPLATE, build_process_html_template


def render_product_plots(df_atual):
    col_graf1, col_graf2 = st.columns(2)
    df_atual['rotulo_x'] = df_atual['version'] + " (" + df_atual['datetime'].dt.strftime('%d/%m') + ")"
    
    with col_graf1:
        st.subheader("📈 Linha de Evolução Histórica")
        fig_base = go.Figure()
        fig_base.add_trace(go.Scatter(x=df_atual.index, y=df_atual['complexity'], name='Complexity', mode='lines+markers', line=dict(width=3, color='#0F6E56')))
        fig_base.add_trace(go.Scatter(x=df_atual.index, y=df_atual['comments'], name='Comments', mode='lines+markers', line=dict(width=3, color='#185FA5')))
        fig_base.add_trace(go.Scatter(x=df_atual.index, y=df_atual['duplication'], name='Duplication', mode='lines+markers', line=dict(width=3, color='#EF9F27')))
        fig_base.add_trace(go.Scatter(x=df_atual.index, y=df_atual['coverage'], name='Coverage', mode='lines+markers', line=dict(width=3, color='#D85A30')))
        fig_base.update_layout(height=300, margin=dict(l=20, r=20, t=20, b=20), hovermode="x unified",
                               xaxis=dict(tickmode='array', tickvals=df_atual.index, ticktext=df_atual['rotulo_x']))
        st.plotly_chart(fig_base, use_container_width=True)
        
    with col_graf2:
        st.subheader("🏆 Histórico do Score Total")
        fig_total = go.Figure()
        fig_total.add_trace(go.Scatter(x=df_atual.index, y=df_atual['total'], name='Total Score', mode='lines+markers', fill='tozeroy', line=dict(width=4, color='black')))
        fig_total.update_layout(height=300, yaxis=dict(range=[0, 1.1]), margin=dict(l=20, r=20, t=20, b=20), hovermode="x unified",
                                xaxis=dict(tickmode='array', tickvals=df_atual.index, ticktext=df_atual['rotulo_x']))
        st.plotly_chart(fig_total, use_container_width=True)

def render_dashboard_layout(repo_key, dict_metrics):
    if repo_key not in dict_metrics or dict_metrics[repo_key].empty:
        st.warning(f"Sem métricas processadas para o repositório: {repo_key}")
        return

    df_atual = dict_metrics[repo_key].sort_values('datetime').reset_index(drop=True)
    ultima_sprint = df_atual.iloc[-1]
    
    html_rendered = build_product_html_template(repo_key, ultima_sprint)
    st.components.v1.html(html_rendered, height=650, scrolling=True)
    
    render_product_plots(df_atual)

    st.markdown("### 📝 Análise Crítica dos Gráficos")
    
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    raiz_do_projeto = os.path.dirname(diretorio_atual) 
    
    NOME_PASTA_NOTAS = "historico_analises"
    pasta_destino = os.path.join(raiz_do_projeto, NOME_PASTA_NOTAS)
    
    os.makedirs(pasta_destino, exist_ok=True)
    
    data_hoje = datetime.now().strftime("%Y-%m-%d")
    arquivo_notas = os.path.join(pasta_destino, f"{data_hoje}_analise_graficos_{repo_key.lower()}.txt")
    
    texto_salvo = ""
    if os.path.exists(arquivo_notas):
        with open(arquivo_notas, "r", encoding="utf-8") as f:
            texto_salvo = f.read()
            
    comentario = st.text_area(
        label=f"Escreva aqui a sua interpretação técnica diária para o histórico da {repo_key}:",
        value=texto_salvo,
        placeholder="Ex: Identificamos um aumento na duplicação na versão v1.2 devido ao refactoring do módulo X...",
        height=120,
        key=f"txt_{repo_key}"
    )
    
    if st.button(f"💾 Salvar Análise da {repo_key}", key=f"btn_{repo_key}"):
        with open(arquivo_notas, "w", encoding="utf-8") as f:
            f.write(comentario)
        st.success(f"Análise salva em: `{NOME_PASTA_NOTAS}/{os.path.basename(arquivo_notas)}`")
    
    st.markdown("---")
    
    st.subheader("📋 Tabela Consolidada de Versões e Auditoria Q-Rapids")
    
    colunas_auditoria = [
        'version', 'datetime_str', 'ncloc',
        'complexity', 'comments', 'duplication',      
        'test_success', 'fast_tests', 'coverage',     
        'Maintainability', 'Reliability', 'total'     
    ]
    
    colunas_presentes = [col for col in colunas_auditoria if col in df_atual.columns]
    tabela_exibicao = df_atual[colunas_presentes].copy()
    
    mapeamento_nomes = {
        'version': 'Versão',
        'datetime_str': 'Data do Dump',
        'ncloc': 'Ncloc',
        'complexity': 'Complexity',
        'comments': 'Comments',
        'duplication': 'Duplication',
        'test_success': 'Test Success',
        'fast_tests': 'Fast Tests',
        'coverage': 'Coverage',
        'Maintainability': 'Maintainability',
        'Reliability': 'Reliability',
        'total': 'Score Total'
    }
    tabela_exibicao.columns = [mapeamento_nomes[col] for col in tabela_exibicao.columns]
    
    config_colunas = {}
    
    colunas_float = [
        'Complexity', 'Comments', 'Duplication',
        'Test Success', 'Fast Tests', 'Coverage',
        'Maintainability', 'Reliability', 'Score Total'
    ]
    
    for col in colunas_float:
        if col in tabela_exibicao.columns:
            config_colunas[col] = st.column_config.NumberColumn(col, format="%.2f")
            
    if 'Ncloc' in tabela_exibicao.columns:
        config_colunas['Ncloc'] = st.column_config.NumberColumn('Ncloc', format="%.0f")
        
    st.dataframe(
        tabela_exibicao.sort_index(ascending=False), 
        use_container_width=True, 
        hide_index=True,
        column_config=config_colunas
    )

    csv_dados = tabela_exibicao.sort_index(ascending=False).to_csv(index=False, sep=";", encoding="utf-8-sig")

    st.download_button(
        label="📥 Exportar Tabela para Excel (CSV)",
        data=csv_dados,
        file_name=f"auditoria_qrapids_{repo_key.lower()}_{data_hoje}.csv",
        mime="text/csv",
        key=f"btn_export_csv_{repo_key}"
    )

def render_project_metrics_tab():
    sprints_raw = load_zenhub_sprints_raw()
    
    if not sprints_raw:
        st.error("❌ Não foi possível carregar os dados de Sprints do arquivo zenhub_analytics.json.")
        return

    evm = calculate_scrum_evm_metrics(sprints_raw)
    
    linhas_dados_grafico = ""
    PS = 5.0  # Total de sprints planejadas para a R3
    
    for i in range(1, len(evm["burnup_labels"])):
        s_nome = evm["burnup_labels"][i].split('\n')[0]  
        n = i  
        
        ppc_porcentagem = (n / PS) * 100
        ppc_str = f"{ppc_porcentagem:.1f}%"
        
        pv_val = evm["burnup_pv"][i]
        
        idx_arrays = i - 1
        
        if evm["burnup_ev"][i] is not None:
            ev_val = f"R$ {evm['burnup_ev'][i]:,.2f}"
            apc_porcentagem = (evm["burnup_ev"][i] / evm["bac"]) * 100
            apc_str = f"{apc_porcentagem:.1f}%"
        else:
            ev_val = "-"
            apc_str = "-"
            
        if idx_arrays < len(evm["velocity_data"]):
            vel_val = f"{evm['velocity_data'][idx_arrays]} SP"
        else:
            vel_val = "-"

        if i < len(evm["spi_data"]) and evm["spi_data"][i] is not None:
            spi_val = f"{evm['spi_data'][i]:.2f}"
        else:
            spi_val = "-"

        linhas_dados_grafico += f"""
        <tr>
            <td><b>{s_nome}</b></td>
            <td><span style="color:#6c757d;">{ppc_str}</span> &rarr; <b>R$ {pv_val:,.2f}</b></td>
            <td><span style="color:#6c757d;">{apc_str}</span> &rarr; <b>{ev_val}</b></td>
            <td>{vel_val}</td>
            <td><b>{spi_val}</b></td>
        </tr>
        """

    linhas_html = ""
    hoje = datetime.now(timezone.utc)
    
    for s in evm["sprints_lista_tabela"]:
        s_start = s["start_at"] if s["start_at"] else hoje
        s_end = s["end_at"] if s["end_at"] else hoje

        if s["state_raw"] == "CLOSED" or s_end < hoje:
            pill = '<span class="pill pill-ok">Fechado</span>'
        elif s["state_raw"] == "ACTIVE" or (s_start <= hoje <= s_end):
            pill = '<span class="pill pill-warn">Em andamento</span>'
        else:
            pill = '<span class="pill pill-fut">Planejado</span>'
            
        end_txt = s_end.strftime('%d/%m') if s["end_at"] else "N/A"
        linhas_html += f"""
        <tr>
            <td>{s['name']}</td>
            <td>{end_txt}</td>
            <td>{int(s['delivered_sp'])} SP</td>
            <td>{pill}</td>
        </tr>
        """

    burnup_labels_json = json.dumps(evm["burnup_labels"])
    burnup_pv_json = json.dumps(evm["burnup_pv"])
    burnup_ev_json = json.dumps(evm["burnup_ev"]) 
    burnup_ideal_json = json.dumps(evm["burnup_ideal"])
    
    spi_data_json = json.dumps(evm["spi_data"])
    cpi_data_json = json.dumps(evm["cpi_data"])
    spi_ref_json = json.dumps(evm["spi_ref"])

    html_pronto = (
        PROJECT_EVM_TEMPLATE
        .replace("__SPRINT_ATUAL_NOME__", evm["sprint_atual_nome"])
        .replace("__KPI_BAC__", f"R$ {evm['bac']:,.2f}")
        .replace("__KPI_EV__", f"R$ {evm['ev_acumulado']:,.2f}")
        .replace("__KPI_SPI__", f"{evm['spi_atual']:.2f}")
        .replace("__KPI_ETC__", f"R$ {evm['etc_atual']:,.2f}")
        .replace("__KPI_SCORE__", f"{evm['score_zenhub']}/100")
        
        .replace("__TABELA_DADOS_GRAFICO_LINHAS__", linhas_dados_grafico)
        .replace("__TABELA_AUDITORIA_EVM__", evm["tabela_auditoria_evm"])
        
        .replace("__BURNUP_LABELS__", burnup_labels_json)
        .replace("__BURNUP_PV__", burnup_pv_json)
        .replace("__BURNUP_EV__", burnup_ev_json)
        .replace("__BURNUP_IDEAL__", burnup_ideal_json)
        
        .replace("__SPI_DATA__", spi_data_json)
        .replace("__CPI_DATA__", cpi_data_json)
        .replace("__SPI_REF__", spi_ref_json)
        
        .replace("__VELOCITY_LABELS__", json.dumps(evm["velocity_labels"]))
        .replace("__VELOCITY_DATA__", json.dumps(evm["velocity_data"]))
        .replace("__VELOCITY_COLORS__", json.dumps(evm["velocity_colors"]))
        
        .replace("__TABELA_LINHAS__", linhas_html)
    )

    st.components.v1.html(html_pronto, height=1100, scrolling=True)

    st.markdown("---")
    st.markdown("### 📝 Parecer de Gestão do Cronograma (Agile EVM)")
    
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    raiz_do_projeto = os.path.dirname(diretorio_atual)
    
    NOME_PASTA_NOTAS = "historico_analises"
    pasta_destino = os.path.join(raiz_do_projeto, NOME_PASTA_NOTAS)
    os.makedirs(pasta_destino, exist_ok=True)
    
    texto_salvo_evm = ""
    
    arquivos_historico = sorted(glob(os.path.join(pasta_destino, "*_analise_projeto_evm.txt")))
    
    if arquivos_historico:
        arquivo_notas_evm = arquivos_historico[-1]
        with open(arquivo_notas_evm, "r", encoding="utf-8") as f:
            texto_salvo_evm = f.read()
            
    comentario_evm = st.text_area(
        label="Espaço para pareceres técnicos (Apenas salvar localmente. Para atualizar na nuvem, faça o commit do arquivo gerado):",
        value=texto_salvo_evm,
        placeholder="Ex: O atraso verificado na Sprint 3 decorreu do impedimento técnico...",
        height=120,
        key="txt_evm"
    )
    
    if st.button("💾 Salvar Análise do Projeto (Local)", key="btn_evm"):
        data_hoje = datetime.now().strftime("%Y-%m-%d")
        arquivo_para_salvar = os.path.join(pasta_destino, f"{data_hoje}_analise_projeto_evm.txt")
        
        with open(arquivo_para_salvar, "w", encoding="utf-8") as f:
            f.write(comentario_evm)
            
        st.success(f"Parecer salvo em: `{NOME_PASTA_NOTAS}/{os.path.basename(arquivo_para_salvar)}`")
        st.info("Gere o commit e dê push nesse arquivo para que ele apareça atualizado na nuvem!")

    st.markdown("---")
    st.subheader("ℹ️ Memória de Cálculo e Critérios do Agile EVM")
    st.markdown(
        """
        As métricas exibidas no painel seguem estritamente a modelagem matemática estabelecida por **Sulaiman, Barton e Blackburn (2006)** no artigo *"AgileEVM - Earned Value Management in Scrum Projects"*, aplicando equações do PMBOK adaptadas ao framework Scrum utilizando **Story Points (SP)** de *User Stories* como métrica de esforço e integrando o controle orçamentário real...
        """
    )

def render_process_metrics_tab():
    """Renderiza a nova aba de processo e fluxo de esteiras."""
    # O isolamento está garantido: calculate_process_metrics encapsula a leitura do zenhub_all_issues.json
    process_metrics = calculate_process_metrics(build_yml_name="code-analysis")
    process_html = build_process_html_template(process_metrics)
    st.components.v1.html(process_html, height=850, scrolling=True)


def main():
    st.set_page_config(page_title="Analytics - RetinaScan Quality Dashboard", page_icon="📊", layout="wide")
    inject_custom_css()
    
    st.title("Dashboard Analytics — RetinaScan")
    st.caption(f"Análise de evolução histórica baseada no modelo de qualidade Q-RAPIDS · Atualizado em: {datetime.now().strftime('%d/%m/%Y')}")
    st.markdown("---")

    sonar_files = glob(SONAR_FILES_PATH)
    file_component_df = build_raw_components_dataframe(sonar_files)
    
    repos_dataframes = []
    if not file_component_df.empty:
        for repo_key in REPOS_LANGUAGE.keys():
            dataframe = file_component_df[file_component_df['repository'] == REPO_BASE_NAME + repo_key]
            if not dataframe.empty:
                repos_dataframes.append({'name': repo_key, 'df': dataframe})

    processed_metrics = {r['name']: build_aggregated_metrics_dataframe(r['df']) for r in repos_dataframes}

    if not processed_metrics:
        st.error("Nenhum ficheiro JSON foi encontrado na pasta `analytics-raw-data`.")
        return

    aba_api, aba_web, aba_projeto, aba_processo = st.tabs([
        "🔌 RetinaScan-Api (Backend)", 
        "💻 RetinaScan-Web (Frontend)",
        "📅 Planejamento & EVM (Eixo Projeto)",
        "⚙️ Processo & Fluxo de Entrega (CI/CD)"
    ])

    with aba_api: 
        render_dashboard_layout('Api', processed_metrics)
        
    with aba_web: 
        render_dashboard_layout('Web', processed_metrics)
        
    with aba_projeto: 
        render_project_metrics_tab()

    with aba_processo:
        render_process_metrics_tab()

if __name__ == "__main__":
    main()