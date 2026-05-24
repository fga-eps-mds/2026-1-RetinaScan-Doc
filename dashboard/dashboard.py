import streamlit as st
import pandas as pd
from glob import glob
from datetime import datetime, timedelta, timezone
import plotly.graph_objects as go
import json
import os

from src.config import REPO_BASE_NAME, REPOS_LANGUAGE, SONAR_FILES_PATH, ISSUES_FILES_PATH
from src.data_layer import build_raw_components_dataframe, load_zenhub_sprints_raw
from src.metrics import build_aggregated_metrics_dataframe, calculate_scrum_evm_metrics
from src.templates import inject_custom_css, build_product_html_template, PROJECT_EVM_TEMPLATE


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
    st.components.v1.html(html_rendered, height=460, scrolling=False)
    
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
    
    st.subheader("📋 Tabela Consolidada de Versões")
    tabela_exibicao = df_atual[['version', 'datetime_str', 'Maintainability', 'Reliability', 'total', 'ncloc']].copy()
    tabela_exibicao.columns = ['Versão', 'Data do Dump', 'Manutenibilidade', 'Confiabilidade', 'Score Total', 'NCLOC']
    st.dataframe(tabela_exibicao.sort_index(ascending=False), use_container_width=True, hide_index=True)

def render_project_metrics_tab():
    sprints_raw = load_zenhub_sprints_raw()
    
    if not sprints_raw:
        st.error("❌ Não foi possível carregar os dados de Sprints do arquivo zenhub_analytics.json.")
        return

    evm = calculate_scrum_evm_metrics(sprints_raw)
    
    linhas_html = ""
    hoje = datetime.now(timezone.utc)
    
    for s in evm["sprints_lista_tabela"]:
        if s["state"] == "CLOSED" or s["end_at"] < hoje:
            pill = '<span class="pill pill-ok">Fechado</span>'
        elif s["state"] == "ACTIVE" or (s["start_at"] <= hoje <= s["end_at"]):
            pill = '<span class="pill pill-warn">Em andamento</span>'
        else:
            pill = '<span class="pill pill-fut">Planejado</span>'
            
        linhas_html += f"""
        <tr>
            <td>{s['name']}</td>
            <td>{s['end_at'].strftime('%d/%m')}</td>
            <td>{int(s['delivered_sp'])} SP</td>
            <td>{pill}</td>
        </tr>
        """

    html_pronto = (
        PROJECT_EVM_TEMPLATE
        .replace("__SPRINT_ATUAL_NOME__", evm["sprint_atual_nome"])
        .replace("__KPI_BAC__", str(int(evm["bac"])))
        .replace("__KPI_EV__", str(int(evm["ev_acumulado"])))
        .replace("__KPI_SPI__", f"{evm['spi_atual']:.2f}")
        .replace("__KPI_VELOCITY__", str(int(evm["ultima_velocity"])))
        .replace("__KPI_SCORE__", str(evm["score_zenhub"]))
        
        .replace("__BURNUP_LABELS__", json.dumps(evm["burnup_labels"]))
        .replace("__BURNUP_PV__", json.dumps(evm["burnup_pv"]))
        .replace("__BURNUP_EV__", json.dumps(evm["burnup_ev"]))
        .replace("__BURNUP_IDEAL__", json.dumps(evm["burnup_ideal"]))
        
        .replace("__VELOCITY_LABELS__", json.dumps(evm["velocity_labels"]))
        .replace("__VELOCITY_DATA__", json.dumps(evm["velocity_data"]))
        .replace("__VELOCITY_COLORS__", json.dumps(evm["velocity_colors"]))
        
        .replace("__SPI_LABELS__", json.dumps(evm["spi_labels"]))
        .replace("__SPI_DATA__", json.dumps(evm["spi_data"]))
        .replace("__SPI_REF__", json.dumps(evm["spi_ref"]))
        
        .replace("__TABELA_LINHAS__", linhas_html)
    )

    st.components.v1.html(html_pronto, height=580, scrolling=True)

    st.markdown("---")
    st.markdown("### 📝 Parecer de Gestão do Cronograma (Agile EVM)")
    
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    raiz_do_projeto = os.path.dirname(diretorio_atual)
    
    NOME_PASTA_NOTAS = "historico_analises"
    pasta_destino = os.path.join(raiz_do_projeto, NOME_PASTA_NOTAS)
    os.makedirs(pasta_destino, exist_ok=True)
    
    data_hoje = datetime.now().strftime("%Y-%m-%d")
    arquivo_notas_evm = os.path.join(pasta_destino, f"{data_hoje}_analise_projeto_evm.txt")
    
    texto_salvo_evm = ""
    if os.path.exists(arquivo_notas_evm):
        with open(arquivo_notas_evm, "r", encoding="utf-8") as f:
            texto_salvo_evm = f.read()
            
    comentario_evm = st.text_area(
        label="Espaço para justificativas diárias de desvios de prazo (SPI < 1.0) ou alterações de escopo:",
        value=texto_salvo_evm,
        placeholder="Ex: O atraso verificado na Sprint 3 decorreu do impedimento técnico com o deploy do SonarQube...",
        height=120,
        key="txt_evm"
    )
    
    if st.button("💾 Salvar Análise do Projeto", key="btn_evm"):
        with open(arquivo_notas_evm, "w", encoding="utf-8") as f:
            f.write(comentario_evm)
        st.success(f"Parecer salvo em: `{NOME_PASTA_NOTAS}/{os.path.basename(arquivo_notas_evm)}`")

    st.markdown("---")
    st.subheader("ℹ️ Memória de Cálculo e Critérios do Agile EVM")
    st.markdown(
        """
        As métricas exibidas no painel acima são computadas de forma dinâmica e automatizada pelo ecossistema do dashboard, 
        extraindo o histórico de Sprints e Marcos em tempo real:

        * **BAC (Budget at Completion):** É o escopo total estimado para a release. Definido matematicamente pela somatória de todos os *Story Points* ($SP$) planejados ao longo do cronograma:
          $$BAC = \sum (SP_{Sprints})$$
        * **PV (Planned Value):** Representa o volume de pontos acumulados que a equipe deveria ter entregue linearmente até a data atual.
        * **EV (Earned Value):** Volume real acumulado de escopo entregue pelo time (Sprints finalizadas ou sob execução).
        * **SPI (Schedule Performance Index):** Eficiência do cronograma ($SPI = EV / PV$).
        * **Milestones / Sprints — Status:** Cronograma unificado que mescla as iterações de desenvolvimento (Sprints) e as entregas de valor (Milestones), calculando dias de atraso dinamicamente caso um marco expire sem conclusão.
        """
    )

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

    aba_api, aba_web, aba_projeto = st.tabs([
        "🔌 RetinaScan-Api (Backend)", 
        "💻 RetinaScan-Web (Frontend)",
        "📅 Planejamento & EVM (Eixo Projeto)"
    ])

    with aba_api: 
        render_dashboard_layout('Api', processed_metrics)
        
    with aba_web: 
        render_dashboard_layout('Web', processed_metrics)
        
    with aba_projeto: 
        render_project_metrics_tab()

if __name__ == "__main__":
    main()