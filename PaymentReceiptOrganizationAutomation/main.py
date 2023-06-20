import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from nomearArquivos import nomear_arquivos_novos_velhos_com_data, inserir_final_arquivo, retirar_data_arquivo
from moverArquivos import mover_arquivos


class windows(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.wm_title("Organizar de comprovantes")
        self.geometry("400x200")

        container = tk.Frame(self, height=400, width=600)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # for F in (MainPage, SidePage):
        frame = MainPage(container, self)

        self.frames[MainPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()


class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        current_directory = filedialog.askdirectory()

        buttonNomear = tk.Button(self, text="Nomear Arquivos",
                                 command=lambda: nomear_arquivos_novos_velhos_com_data(current_directory))
        buttonNomear.pack(side="top", fill=tk.X)

        buttonInserirFinal = tk.Button(self, text="Inserir Final Arquivos",
                                       command=lambda: inserir_final_arquivo(current_directory))
        buttonInserirFinal.pack(side="top", fill=tk.X)

        buttonRetirarData = tk.Button(self, text="Retirar Data Arquivos",
                                      command=lambda: retirar_data_arquivo(current_directory))
        buttonRetirarData.pack(side="top", fill=tk.X)

        buttonMover = tk.Button(self, text="Mover Arquivos", command=lambda: mover_arquivos(current_directory))
        buttonMover.pack(side="top", fill=tk.X)

        buttonSair = tk.Button(self, text="Quit", command=self.destroy)
        buttonSair.pack(padx=20, pady=20)

    # def getAdir(self):
    #     self.folder_selected = tkFileDialog.askdirectory(parent=stepOne, title='Please select a directory')


if __name__ == "__main__":
    testObj = windows()
    testObj.mainloop()
