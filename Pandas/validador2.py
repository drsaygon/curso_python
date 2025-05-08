import os
import pandas as pd
import time
from concurrent import futures

def process_excel(filename):
    """Processa a planilha para contar ocorrências de 'Maria' na coluna 'NOME'."""
    start_time = time.time()

    try:
        df = pd.read_excel(filename)

        # Verifica se a coluna 'NOME' existe
        if 'NOME' not in df.columns:
            end_time = time.time()
            elapsed = end_time - start_time
            return (False, filename, 0, 0, f"Coluna 'NOME' não encontrada na planilha.")

        # Conta total de linhas e ocorrências de 'Maria'
        total_rows = len(df)
        maria_count = df['NOME'].str.contains('Maria', case=False).sum()

        end_time = time.time()
        elapsed = end_time - start_time

        return (True, filename, total_rows, maria_count, elapsed)

    except Exception as e:
        end_time = time.time()
        elapsed = end_time - start_time
        return (False, filename, 0, 0, f"Erro ao ler o arquivo: {str(e)}")


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

    print(f"🔍 Encontrados {len(excel_files)} arquivos. Iniciando processamento em paralelo...")
    
    results = []

    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_file = {executor.submit(process_excel, file): file for file in excel_files}

        for future in futures.as_completed(future_to_file):
            try:
                result = future.result()
                results.append(result)
            except Exception as exc:
                results.append((False, future_to_file[future], 0, 0, f"Erro fatal: {str(exc)}"))

    # Exibe resultados
    successful = [r for r in results if r[0]]
    failed = [r for r in results if not r[0]]

    print("\n📊 Resultados do Processamento:")
    if successful:
        print(f"\n✅ {len(successful)} planilha(s) processada(s) com sucesso:")
        for status, filename, total_rows, maria_count, elapsed in successful:
            print(f"  📄 {os.path.basename(filename)}")
            print(f"     Linhas totais: {total_rows}")
            print(f"     Nome 'Maria' encontrado: {maria_count} vez(es)")
            print(f"     Tempo: {elapsed:.2f} s\n")

    if failed:
        print(f"\n❌ {len(failed)} planilha(s) com problemas:")
        for status, filename, _, _, error_msg in failed:
            print(f"  ❌ {os.path.basename(filename)}")
            print(f"     Erro: {error_msg}\n")

if __name__ == "__main__":
    main()