import streamlit as st
import pandas as pd
import locale


# Configurar a localidade para o padrão brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

st.title("📊 Calculadora Meta Faturamento")

mes = st.text_input("MÊS:")
realizado = st.number_input("REALIZADO ANO ANTERIOR (R$):", min_value=0.0, step=100.0)
meta_percentual = st.number_input("% META (%):", min_value=0.0, step=1.0)
meta_ticket_medio = st.number_input("META TICKET MÉDIO (R$):", min_value=0.0, step=100.0)
dias = st.number_input("DIAS À TRABALHAR:", min_value=1, step=1)
funcionarios = st.number_input("QTD COLABORADORES:", min_value=1, step=1)
semanas = 4
st.markdown(f"<p style='text-align: center;'><b>QTD SEMANAS À TRABALHAR:</b> {semanas} Semanas</p>", unsafe_allow_html=True)


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
        st.markdown(f"<p style='text-align: center;'>Meta Total : R$ {locale.format_string('%.2f', meta_total, grouping=True)}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Semanal : R$ {locale.format_string('%.2f', meta_semanal, grouping=True)}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Diária : R$ {locale.format_string('%.2f', meta_diaria, grouping=True)}</p><br>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center;'>▫️Quantidade de Vendas▫️</h5>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Mensal : {locale.format_string('%.0f', meta_ticketmedio, grouping=True)}  Vendas</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Semanal : {locale.format_string('%.0f', meta_ticket_semanal, grouping=True)}  Vendas</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Diária : {locale.format_string('%.0f', meta_ticket_diaria, grouping=True)}  Vendas</p>", unsafe_allow_html=True)
        

    with col2:
        st.markdown("<h3 style='text-align: center;'>👤 Meta por Colaborador</h3><br>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center;'>▫️Faturamento▫️</h5>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Mensal Individual : R$ {locale.format_string('%.2f', meta_mensal_individual, grouping=True)}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Semanal Individual : R$ {locale.format_string('%.2f', meta_semanal_individual, grouping=True)}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Diária Individual : R$ {locale.format_string('%.2f', meta_diaria_individual, grouping=True)}</p><br>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center;'>▫️Quantidade de Vendas▫️</h5>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Mensal Individual : {locale.format_string('%.0f', meta_ticket_individual, grouping=True)}  Vendas</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Semanal Individual : {locale.format_string('%.0f', meta_ticket_semanal_individual, grouping=True)}  Vendas</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Diária Individual : {locale.format_string('%.0f', meta_ticket_diaria, grouping=True)}  Vendas</p>", unsafe_allow_html=True)
        

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

