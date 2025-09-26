import streamlit as st
import pandas as pd
import io

def format_brl(valor, casas_decimais=2):
    return f"{valor:,.{casas_decimais}f}".replace(",", "X").replace(".", ",").replace("X", ".")

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
        st.markdown(f"<p style='text-align: center;'>Meta Total : R$ {format_brl(meta_total)}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Semanal : R$ {format_brl(meta_semanal)}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Diária : R$ {format_brl(meta_diaria)}</p><br>", unsafe_allow_html=True)

        st.markdown("<h5 style='text-align: center;'>▫️Quantidade de Vendas▫️</h5>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Mensal : {format_brl(meta_ticketmedio, 0)} Vendas</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Semanal : {format_brl(meta_ticket_semanal, 0)} Vendas</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Diária : {format_brl(meta_ticket_diaria, 0)} Vendas</p>", unsafe_allow_html=True)

    with col2:
        st.markdown("<h3 style='text-align: center;'>👤 Meta por Colaborador</h3><br>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center;'>▫️Faturamento▫️</h5>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Mensal Individual : R$ {format_brl(meta_mensal_individual)}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Semanal Individual : R$ {format_brl(meta_semanal_individual)}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Diária Individual : R$ {format_brl(meta_diaria_individual)}</p><br>", unsafe_allow_html=True)

        st.markdown("<h5 style='text-align: center;'>▫️Quantidade de Vendas▫️</h5>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Mensal Individual : {format_brl(meta_ticket_individual, 0)} Vendas</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Semanal Individual : {format_brl(meta_ticket_semanal_individual, 0)} Vendas</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Meta Diária Individual : {format_brl(meta_ticket_diaria_individual, 0)} Vendas</p>", unsafe_allow_html=True)

        

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
    
    # Criar buffer de memória e salvar o Excel nele
    excel_buffer = io.BytesIO()
    with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Metas')
    excel_buffer.seek(0)

    # Espaço para alinhar centralizado
    st.write("")
    st.write("")

    btn_col1, btn_col2, btn_col3 = st.columns([2, 2, 2])
    with btn_col2:
        st.download_button(
            label="⬇️ Exportar Excel",
            data=excel_buffer,
            file_name="metas.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
