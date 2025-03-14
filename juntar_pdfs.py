import PyPDF2
from tqdm import tqdm
import time

def juntar_pdfs(arquivos, saida):
    """Junta múltiplos arquivos PDF em um único arquivo, com barra de progresso."""
    mesclador = PyPDF2.PdfMerger()

    print("📌 Iniciando a junção dos PDFs...\n")
    
    for arquivo in tqdm(arquivos, desc="Processando", unit="arquivo"):
        try:
            mesclador.append(arquivo)
            time.sleep(0.5)  # Apenas para visualizar melhor a barra de progresso
        except Exception as e:
            print(f"❌ Erro ao adicionar {arquivo}: {e}")

    mesclador.write(saida)
    mesclador.close()
    print(f"\n✅ PDFs mesclados com sucesso em '{saida}'!")

# 🔹 Defina aqui os PDFs que deseja juntar
arquivos_pdf = [
   "inserir arquivos aqui"
]

# 🔹 Nome do arquivo de saída
arquivo_saida = "resultado.pdf"

# 🔹 Chama a função para juntar os PDFs
juntar_pdfs(arquivos_pdf, arquivo_saida)
