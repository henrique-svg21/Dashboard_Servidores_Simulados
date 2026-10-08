import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px
import time

# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Painel de Monitoramento de Servidores",
    page_icon="📊",
    layout="wide"
)

# ============================================================
# PALETA WEG
# Baseada na paleta apresentada no material enviado.
# ============================================================

WEG_AZUL = "#05569B"
WEG_AZUL_2 = "#176097"
WEG_CIANO = "#1FB4D0"
WEG_AZUL_CLARO = "#A4C8D8"

FUNDO = "#FFFFFF"
FUNDO_SIDEBAR = "#F3F3F3"
TEXTO = "#1F2D3D"
BORDA = "#D9E3E8"

# ============================================================
# ESTILO VISUAL
# ============================================================

st.markdown(
    f"""
    <style>
        /* Fundo geral */
        .stApp {{
            background-color: {FUNDO};
        }}

        /* Sidebar */
        section[data-testid="stSidebar"] {{
            background-color: {FUNDO_SIDEBAR};
            border-right: 1px solid {BORDA};
        }}

        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {{
            color: {WEG_AZUL};
        }}

        /* Títulos */
        h1, h2, h3 {{
            color: {TEXTO};
        }}

        /* Cabeçalho */
        .weg-header {{
            border-bottom: 4px solid {WEG_CIANO};
            padding: 0.25rem 0 0.9rem 0;
            margin-bottom: 1.4rem;
        }}

        .weg-title {{
            color: {WEG_AZUL};
            font-weight: 700;
            text-align: center;
            line-height: 1.15;
            margin: 0;
        }}

        /* Linha decorativa */
        .weg-accent {{
            height: 5px;
            width: 72px;
            background: {WEG_CIANO};
            margin: 8px auto 0 auto;
            border-radius: 3px;
        }}

        /* Métricas nativas do Streamlit */
        div[data-testid="stMetric"] {{
            background: #F7FAFC;
            border: 1px solid {BORDA};
            border-left: 5px solid {WEG_AZUL};
            border-radius: 8px;
            padding: 0.8rem 1rem;
            margin-bottom: 0.7rem;
        }}

        div[data-testid="stMetricLabel"] {{
            color: {WEG_AZUL_2};
        }}

        div[data-testid="stMetricValue"] {{
            color: {TEXTO};
        }}

        /* Caixa dos servidores */
        .server-title {{
            color: {WEG_AZUL};
            font-weight: 700;
            border-bottom: 2px solid {WEG_AZUL_CLARO};
            padding-bottom: 5px;
            margin-bottom: 10px;
        }}

        /* Expander */
        div[data-testid="stExpander"] {{
            border: 1px solid {BORDA};
            border-top: 4px solid {WEG_CIANO};
            border-radius: 7px;
        }}

        /* ============================
           CONTROLES DA SIDEBAR
           ============================ */

        /* Textos dos controles */
        section[data-testid="stSidebar"] label {{
            color: {WEG_AZUL_2} !important;
        }}

        /* Selectbox */
        section[data-testid="stSidebar"] div[data-baseweb="select"] > div {{
            border: 1px solid {WEG_AZUL_CLARO} !important;
            box-shadow: none !important;
        }}

        section[data-testid="stSidebar"] div[data-baseweb="select"] > div:focus-within {{
            border: 2px solid {WEG_AZUL} !important;
            box-shadow: 0 0 0 1px {WEG_AZUL} !important;
        }}

        /* Menu aberto do selectbox */
        section[data-testid="stSidebar"] ul[role="listbox"] {{
            border-top: 3px solid {WEG_CIANO};
        }}

        /* Slider: trilho */
        section[data-testid="stSidebar"] div[data-testid="stSlider"] [data-baseweb="slider"] > div > div {{
            background: linear-gradient(
                to right,
                {WEG_AZUL} 0%,
                {WEG_AZUL} 50%,
                {WEG_AZUL_CLARO} 50%,
                {WEG_AZUL_CLARO} 100%
            ) !important;
        }}

        /* Slider: botão */
        section[data-testid="stSidebar"] div[data-testid="stSlider"] [role="slider"] {{
            background-color: {WEG_AZUL} !important;
            border-color: {WEG_AZUL} !important;
            box-shadow: 0 0 0 2px #FFFFFF !important;
        }}

        /* Valor mostrado acima do slider */
        section[data-testid="stSidebar"] div[data-testid="stSlider"] [data-testid="stThumbValue"] {{
            color: {WEG_AZUL} !important;
        }}

        /* ============================
           TABELAS / CAMPOS
           ============================ */

        section[data-testid="stSidebar"] input {{
            accent-color: {WEG_AZUL};
        }}

        /* Info */
        div[data-testid="stAlert"] {{
            border-left-color: {WEG_CIANO};
        }}
    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# CARREGAMENTO DOS DADOS
# ============================================================

def carregar_dados(limite=100):
    conn = sqlite3.connect("telemetria.db", timeout=10)

    query = f"""
        SELECT timestamp, server_id, temp_CPU, uso_RAM, uso_CPU, latencia
        FROM leituras_servidores
        ORDER BY id DESC
        LIMIT {limite}
    """

    df = pd.read_sql_query(query, conn)
    conn.close()

    if not df.empty:
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df = df.sort_values("timestamp")

    return df


# ============================================================
# CABEÇALHO
# ============================================================

col_logo_weg, col_titulo, col_logo_senai = st.columns([1, 5, 1])

with col_logo_weg:
    st.image("weg.png", width=100)

with col_titulo:
    st.markdown(
        f"""
        <div class="weg-header">
            <h1 class="weg-title">
                Monitoramento de servidores<br>
                em tempo real
            </h1>
            <div class="weg-accent"></div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col_logo_senai:
    st.image("senai.png", width=120)


# ============================================================
# BARRA LATERAL DE CONTROLE
# ============================================================

st.sidebar.markdown(
    f"""
    <h2 style="color:{WEG_AZUL}; margin-top:0;">
        Filtros de controle
    </h2>
    """,
    unsafe_allow_html=True
)

intervalo_atualizacao = st.sidebar.slider(
    "Frequência de atualização (segundos):",
    1,
    10,
    2
)

quantidade_registros = st.sidebar.slider(
    "Histórico de leituras:",
    30,
    300,
    120
)


# Linha de identidade visual da WEG na sidebar
st.sidebar.markdown(
    f'''
    <div style="
        margin-top: 1.8rem;
        height: 5px;
        width: 100%;
        background: linear-gradient(
            to right,
            {WEG_AZUL} 0%,
            {WEG_AZUL} 45%,
            {WEG_CIANO} 45%,
            {WEG_CIANO} 70%,
            {WEG_AZUL_CLARO} 70%,
            {WEG_AZUL_CLARO} 100%
        );
        border-radius: 3px;
    "></div>
    ''',
    unsafe_allow_html=True
)

# ============================================================
# CARREGAMENTO
# ============================================================

df = carregar_dados(limite=quantidade_registros)


if df.empty:

    st.info(
        "Aguardando dados... Certifique-se de que o 'simulator.py' está rodando."
    )

else:

    servidores_disponiveis = df["server_id"].unique().tolist()

    servidor_selecionado = st.sidebar.selectbox(
        "Filtrar por Servidor:",
        ["Todos"] + servidores_disponiveis
    )

    if servidor_selecionado != "Todos":
        df_filtrado = df[df["server_id"] == servidor_selecionado]
    else:
        df_filtrado = df


    # ========================================================
    # INDICADORES
    # ========================================================

    st.subheader("Últimas leituras registradas")

    ultimos = df_filtrado.groupby("server_id").last().reset_index()

    cols = st.columns(len(ultimos))

    for idx, row in ultimos.iterrows():

        with cols[idx]:

            st.markdown(
                f"""
                <div class="server-title">
                    {row["server_id"]}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.metric(
                "Temperatura da CPU",
                f'{row["temp_CPU"]:.2f} °C'
            )

            st.metric(
                "Uso de RAM",
                f'{row["uso_RAM"]:.2f} %'
            )

            st.metric(
                "Uso de CPU",
                f'{row["uso_CPU"]:.2f} %'
            )

            st.metric(
                "Latência",
                f'{row["latencia"]:.2f} ms'
            )


    st.markdown("---")


    # ========================================================
    # GRÁFICOS
    # ========================================================

    col_g1, col_g2 = st.columns(2)

    # Ordem das cores da paleta WEG
    cores_weg = [
        WEG_AZUL,
        WEG_AZUL_2,
        WEG_CIANO,
        WEG_AZUL_CLARO
    ]


    with col_g1:

        fig_temp_CPU = px.line(
            df_filtrado,
            x="timestamp",
            y="temp_CPU",
            color="server_id",
            title="Temperatura da CPU (°C) ao longo do tempo",
            markers=True,
            color_discrete_sequence=cores_weg
        )

        fig_temp_CPU.update_layout(
            font=dict(color=TEXTO),
            title_font=dict(color=WEG_AZUL),
            plot_bgcolor="white",
            paper_bgcolor="white",
            legend_title_text="Servidor",
            xaxis_title="Horário",
            yaxis_title="Temperatura (°C)"
        )

        fig_temp_CPU.update_xaxes(
            showgrid=True,
            gridcolor="#E8EEF2"
        )

        fig_temp_CPU.update_yaxes(
            showgrid=True,
            gridcolor="#E8EEF2"
        )

        st.plotly_chart(
            fig_temp_CPU,
            use_container_width=True
        )


    with col_g2:

        fig_uso_RAM = px.line(
            df_filtrado,
            x="timestamp",
            y="uso_RAM",
            color="server_id",
            title="Uso de RAM do servidor (%) ao longo do tempo",
            markers=True,
            color_discrete_sequence=cores_weg
        )

        fig_uso_RAM.update_layout(
            font=dict(color=TEXTO),
            title_font=dict(color=WEG_AZUL),
            plot_bgcolor="white",
            paper_bgcolor="white",
            legend_title_text="Servidor",
            xaxis_title="Horário",
            yaxis_title="Uso de RAM (%)"
        )

        fig_uso_RAM.update_xaxes(
            showgrid=True,
            gridcolor="#E8EEF2"
        )

        fig_uso_RAM.update_yaxes(
            showgrid=True,
            gridcolor="#E8EEF2"
        )

        st.plotly_chart(
            fig_uso_RAM,
            use_container_width=True
        )


    # ========================================================
    # TABELA
    # ========================================================

    with st.expander("Visualizar tabela de registros"):

        st.dataframe(
            df_filtrado.sort_values(
                "timestamp",
                ascending=False
            ),
            use_container_width=True
        )


# ============================================================
# ATUALIZAÇÃO AUTOMÁTICA
# ============================================================

time.sleep(intervalo_atualizacao)

st.rerun()
