import streamlit as st
import pandas as pd

# === Centralizar a logo acima do título ===
col1, col2, col3 = st.columns([6, 10, 1])  # col1 e col3 para espaçamento, col2 para o título/logo
with col2:
    st.image("logobranca.png", width=160)  # Ajuste o tamanho conforme sua logo


st.title("📊 Calculadora Meta Faturamento")

mes = st.text_input("MÊS:")
realizado = st.number_input("REALIZADO ANO ANTERIOR (R$):", min_value=0.0, step=100.0)
meta_percentual = st.number_input("% META (%):", min_value=0.0, step=1.0)
meta_ticket_medio = st.number_input("META TICKET MÉDIO (R$):", min_value=0.0, step=100.0)
dias = st.number_input("DIAS À TRABALHAR:", min_value=1, step=1)
semanas = st.number_input("QTD SEMANAS À TRABALHAR:", min_value=1, step=1)
funcionarios = st.number_input("QTD COLABORADORES:", min_value=1, step=1)

if st.button("Calcular"):
    meta_total = realizado * (1 + meta_percentual / 100)
    meta_diaria = meta_total / dias
    meta_semanal = meta_total / semanas
    meta_ticketmedio = meta_total/meta_ticket_medio
    meta_ticket_semanal = meta_ticketmedio/semanas
    meta_ticket_diaria = meta_ticketmedio / dias
    meta_diaria_individual = meta_diaria / funcionarios
    meta_semanal_individual = meta_semanal / funcionarios
    meta_mensal_individual = meta_total / funcionarios
    meta_ticket_individual = meta_ticketmedio/funcionarios
    meta_ticket_semanal_individual = meta_ticket_semanal /funcionarios
    meta_ticket_diaria_individual = meta_ticket_diaria /funcionarios

    # === Resultados lado a lado ===
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h3 style='text-align: center;'>📌 Meta Loja</h3><br>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center;'>▫️Faturamento▫️</h5>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta total: R$ {meta_total:,.2f}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta semanal: R$ {meta_semanal:,.2f}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta diária: R$ {meta_diaria:,.2f}</p><br>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center;'>▫️Quantidade de vendas▫️</h5>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Qtd Vendas: {meta_ticketmedio:,.2f}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Qtd Vendas semanal: {meta_ticket_semanal:,.2f}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Qtd Vendas diária: {meta_ticket_diaria:,.2f}</p>", unsafe_allow_html=True)
        

    with col2:
        st.markdown("<h3 style='text-align: center;'>👤 Meta por Colaborador</h3><br>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center;'>▫️Faturamento▫️</h5>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta mensal individual: R$ {meta_mensal_individual:,.2f}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta semanal individual: R$ {meta_semanal_individual:,.2f}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta diária individual: R$ {meta_diaria_individual:,.2f}</p><br>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center;'>▫️Quantidade de vendas▫️</h5>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Qtd Vendas Individual: {meta_ticket_individual:,.2f}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Qtd Vendas semanal Individual: {meta_ticket_semanal_individual:,.2f}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Qtd Vendas diária Individual: {meta_ticket_diaria:,.2f}</p>", unsafe_allow_html=True)
        

    # Exportar para Excel
    df = pd.DataFrame([{
        "Mês": mes,
        "Meta Total": meta_total,
        "Meta Semanal": meta_semanal,
        "Meta Diária": meta_diaria,
        "Meta Mensal Individual": meta_mensal_individual,
        "Meta Semanal Individual": meta_semanal_individual,
        "Meta Diária Individual": meta_diaria_individual,
        "Meta Qtd Vendas mensal Individual": meta_ticket_individual,
        "Meta Qtd Vendas semanal Individual": meta_ticket_semanal_individual,
        "Meta Qtd Vendas diária Individual": meta_ticket_diaria_individual,
        

    }])
    # Espaço para alinhar centralizado
    st.write("")
    st.write("")

    btn_col1, btn_col2, btn_col3 = st.columns([2, 2, 2])
    with btn_col2:
        st.download_button(
            label="⬇️ Exportar Excel",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="metas.csv",
            mime="text/csv"
        )

