import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

class OrganizadorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Organizador de Arquivos")
        self.root.geometry("500x200")

        self.pasta_selecionada = tk.StringVar()

        # Frame para seleção de pasta
        frame_selecao = tk.Frame(self.root, pady=10)
        frame_selecao.pack()

        label_instrucao = tk.Label(frame_selecao, text="Selecione a pasta que deseja organizar:")
        label_instrucao.pack()

        botao_selecionar = tk.Button(frame_selecao, text="Selecionar Pasta", command=self.selecionar_pasta)
        botao_selecionar.pack(pady=5)

        label_pasta = tk.Label(frame_selecao, textvariable=self.pasta_selecionada, fg="blue")
        label_pasta.pack()

        # Frame para o botão de organizar
        frame_organizar = tk.Frame(self.root, pady=10)
        frame_organizar.pack()

        botao_organizar = tk.Button(frame_organizar, text="Organizar", command=self.organizar)
        botao_organizar.pack()

    def selecionar_pasta(self):
        pasta = filedialog.askdirectory()
        if pasta:
            self.pasta_selecionada.set(pasta)

    def organizar(self):
        pasta = self.pasta_selecionada.get()
        if not pasta:
            messagebox.showwarning("Aviso", "Por favor, selecione uma pasta primeiro.")
            return

        try:
            organizar_arquivos(pasta)
            messagebox.showinfo("Sucesso", f"Arquivos na pasta '{pasta}' organizados com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# O restante do seu código permanece o mesmo
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
            # Ignora as pastas de categorias para não movê-las
            if arquivo in categorias.keys() or arquivo == 'Outros':
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

        if not movido and os.path.isfile(caminho_arquivo):
            pasta_outros = os.path.join(pasta, 'Outros')
            os.makedirs(pasta_outros, exist_ok=True)
            shutil.move(caminho_arquivo, os.path.join(pasta_outros, arquivo))


if __name__ == "__main__":
    root = tk.Tk()
    app = OrganizadorGUI(root)
    root.mainloop()
