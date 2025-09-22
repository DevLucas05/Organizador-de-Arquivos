import os
import shutil


# Defina o caminho da pasta que você deseja organizar
pasta_alvo = r"C:\Users\SeuUsuário\Downloads"

categorias = {
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documentos': ['.pdf', '.doc', '.docx', '.xls', '.xlsx'],
    'Videos': ['.mp4', '.avi', '.mov'],
    'Musica': ['.mp3', '.wav'],
    'Compactados': ['.zip', '.rar', '.7z']
}


def organizar_arquivos(pasta):
    for arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, arquivo)

        if os.path.isdir(caminho_arquivo):
            continue

        _, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()

        movido = False
        for categoria, extensoes in categorias.items():
            if extensao in extensoes:
                pasta_categoria = os.path.join(pasta, categoria)
                if not os.path.exists(pasta_categoria):
                    os.makedirs(pasta_categoria)
                shutil.move(caminho_arquivo, os.path.join(pasta_categoria, arquivo))
                movido = True
                break

        if not movido:
            pasta_outros = os.path.join(pasta, 'Outros')
            os.makedirs(pasta_outros, exist_ok=True)
            shutil.move(caminho_arquivo, os.path.join(pasta_outros, arquivo))
            print(f'Movido: {arquivo} -> Outros')

if __name__ == "__main__":
    organizar_arquivos(pasta_alvo)
    print("\n✅ Organização concluída!")


