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
    "./Berserk/1 (1).pdf",
    "./Berserk/1 (2).pdf",
    "./Berserk/1 (2).pdf",
    "./Berserk/1 (3).pdf",
    "./Berserk/1 (4).pdf",
    "./Berserk/1 (5).pdf",
    "./Berserk/1 (6).pdf",
    "./Berserk/1 (7).pdf",
    "./Berserk/1 (8).pdf",
    "./Berserk/1 (9).pdf",
    "./Berserk/1 (10).pdf",
    "./Berserk/1 (11).pdf",
    "./Berserk/1 (12).pdf",
    "./Berserk/1 (13).pdf",
    "./Berserk/1 (14).pdf",
    "./Berserk/1 (15).pdf",
    "./Berserk/1 (16).pdf",
    "./Berserk/1 (17).pdf",
    "./Berserk/1 (18).pdf",
    "./Berserk/1 (19).pdf",
    "./Berserk/1 (20).pdf",
    "./Berserk/1 (21).pdf",
    "./Berserk/1 (22).pdf",
    "./Berserk/1 (23).pdf",
    "./Berserk/1 (24).pdf",
    "./Berserk/1 (25).pdf",
    "./Berserk/1 (26).pdf",
    "./Berserk/1 (27).pdf",
    "./Berserk/1 (28).pdf",
    "./Berserk/1 (29).pdf",
    "./Berserk/1 (30).pdf",
    "./Berserk/1 (31).pdf",
    "./Berserk/1 (32).pdf",
    "./Berserk/1 (33).pdf",
    "./Berserk/1 (34).pdf",
    "./Berserk/1 (35).pdf",
    "./Berserk/1 (36).pdf",
    "./Berserk/1 (37).pdf",
    "./Berserk/1 (38).pdf",
    "./Berserk/1 (39).pdf",
    "./Berserk/1 (40).pdf",
    "./Berserk/1 (41).pdf",
    "./Berserk/1 (42).pdf",
]

# 🔹 Nome do arquivo de saída
arquivo_saida = "resultado.pdf"

# 🔹 Chama a função para juntar os PDFs
juntar_pdfs(arquivos_pdf, arquivo_saida)
