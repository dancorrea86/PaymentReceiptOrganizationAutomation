# -*- coding: UTF-8 -*-
import shutil
import os
from os import listdir
from os.path import isfile, join
from xml.dom.expatbuilder import parseString

class MoveArquivos:

    def __init__(self, pastaOrigem, pastaDestino = os.getcwd):
        self.pastaOrigem = pastaOrigem
        self.pastaDestino = pastaDestino
        self.listaArquivos = os.listdir(self.pastaOrigem)

    def main(self):
        self.separarArquivosPasta()

    def separarArquivosPasta(self):
        listArquivosParaMover = []

        for arquivo in self.listaArquivos:
            if (arquivo.split(" ")[-1].lower() == "comprovante.pdf" or arquivo.split(" ")[-1].lower() == "pago.pdf"):
                listArquivosParaMover.append(arquivo)
            else:
                pass

        self.moverArquivos(listArquivosParaMover)

    def moverArquivos(self, listArquivosParaMover):
        print("Movendo Arquivos...")

        for arquivo in listArquivosParaMover:
            print ('{}{}{}'.format(self.pastaOrigem, "\\", arquivo))
            
            if (not os.path.exists('{}{}{}'.format(self.pastaDestino, "\\",arquivo[0:7]))):
                os.makedirs('{}{}{}'.format(self.pastaDestino, "\\",arquivo[0:7]))

            shutil.move('{}{}{}'.format(self.pastaOrigem, "\\", arquivo), '{}{}{}{}{}'.format(self.pastaDestino, "\\",arquivo[0:7], "\\", arquivo))
        

if __name__ == "__main__":
    app = MoveArquivos(r"C:\Users\danie\Desktop", r"G:\Meu Drive\Documentos\Comprovantes\Mae\2022")
    app.main()
    