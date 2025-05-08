import streamlit as st
import pandas as pd

# Definindo o template esperado
TEMPLATE_COLUMNS = {
    'NOME': str,
    'IDADE': int,
    'EMAIL': str
}

def validate_excel(file):
    try:
        df = pd.read_excel(file)
        
        # Verifica se todas as colunas estão presentes
        missing_cols = [col for col in TEMPLATE_COLUMNS if col not in df.columns]
        if missing_cols:
            return False, f"Colunas ausentes: {missing_cols}", None
        
        # Verifica tipos (opcional)
        for col, dtype in TEMPLATE_COLUMNS.items():
            if not pd.api.types.is_dtype_equal(df[col].dtype, dtype):
                return False, f"Tipo incorreto na coluna '{col}'. Esperado: {dtype}, Encontrado: {df[col].dtype}", None
        
        return True, "Planilha válida!", df
    
    except Exception as e:
        return False, f"Erro ao ler o arquivo: {str(e)}", None


st.title("✅ Validação de Planilhas Excel")

uploaded_files = st.file_uploader(
    "Envie seus arquivos Excel (.xlsx)",
    type=["xlsx"],
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        st.markdown(f"### 📄 Arquivo: **{file.name}**")
        is_valid, message, df = validate_excel(file)
        
        if is_valid:
            st.success(message)
            st.dataframe(df.head())
        else:
            st.error(message)
else:
    st.info("Nenhum arquivo foi enviado ainda.")


# Para rodar
# streamlit run validador_excel.py    