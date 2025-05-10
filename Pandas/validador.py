import os
import pandas as pd
import time  # ✅ Adicionado
from concurrent import futures
# só existe no branch primeiro_branch
# Definindo as colunas obrigatórias
REQUIRED_COLUMNS = {'NOME', 'IDADE', 'EMAIL'}

def validate_excel(filename):
    """Valida se a planilha contém as colunas obrigatórias."""
    start_time = time.time()  # ✅ Início do timer

    try:
        df = pd.read_excel(filename)

        # Verifica se todas as colunas obrigatórias estão presentes
        missing_cols = REQUIRED_COLUMNS - set(df.columns)
        if missing_cols:
            end_time = time.time()  # ✅ Final do timer
            elapsed = end_time - start_time  # ✅ Tempo decorrido
            return (False, f"Colunas obrigatórias ausentes: {list(missing_cols)}", elapsed)

        end_time = time.time()  # ✅ Final do timer
        elapsed = end_time - start_time  # ✅ Tempo decorrido
        return (True, "Planilha válida! Contém todas as colunas obrigatórias.", elapsed)

    except Exception as e:
        end_time = time.time()  # ✅ Final do timer
        elapsed = end_time - start_time  # ✅ Tempo decorrido
        return (False, f"Erro ao ler o arquivo: {str(e)}", elapsed)


def main():
    """Função principal que processa todas as planilhas da pasta 'Pandas'."""
    current_dir = "C:\\desenv\\curso_python"
    target_dir = os.path.join(current_dir, "Pandas")

    if not os.path.exists(target_dir):
        print(f"⚠️ Diretório não encontrado: {target_dir}")
        return

    print(f"🔍 Buscando planilhas em: {target_dir}")
    excel_files = [os.path.join(target_dir, f) for f in os.listdir(target_dir) if f.endswith('.xlsx')]

    if not excel_files:
        print("⚠️ Nenhum arquivo Excel encontrado na pasta 'Pandas'.")
        return

    print(f"🔍 Encontrados {len(excel_files)} arquivos. Iniciando validação em paralelo...")
    results = []

    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_file = {executor.submit(validate_excel, file): file for file in excel_files}

        for future in futures.as_completed(future_to_file):
            filename = future_to_file[future]
            try:
                is_valid, message, elapsed = future.result()  # ✅ Receber tempo
                results.append((filename, is_valid, message, elapsed))
            except Exception as exc:
                results.append((filename, False, f"Erro fatal: {str(exc)}", 0))

    # Exibe resultados
    successful = [f for f in results if f[1]]
    failed = [f for f in results if not f[1]]

    print("\n✅ Resultados:")
    if successful:
        print(f"\n✅ {len(successful)} planilha(s) validada(s) com sucesso:")
        for file, valid, msg, elapsed in successful:
            # ✅ Formatar tempo com 2 casas decimais
            print(f"  ✔️ {os.path.basename(file)} | Tempo: {elapsed:.2f} s")

    if failed:
        print(f"\n❌ {len(failed)} planilha(s) com problemas:")
        for file, valid, msg, elapsed in failed:
            print(f"  ❌ {os.path.basename(file)} | Tempo: {elapsed:.2f} s:")
            print(f"     {msg}")

if __name__ == "__main__":
    main()