import shutil
import os
import sqllite_connection
from conta import Conta
from pathlib import Path, PureWindowsPath, PurePath

class MoveArquivos:
   
    def __init__(self, pasta_origem, pasta_destino = os.getcwd):
        self.pasta_origem = pasta_origem
        self.pasta_destino = pasta_destino
        self.lista_arquivos = os.listdir(self.pasta_origem)

    def main(self):
        self.separar_arquivos_pasta()

    def separar_arquivos_pasta(self):
        lista_arquivos_para_mover = []

        for arquivo in self.lista_arquivos:
            if (arquivo.split(" ")[-1].lower() == "comprovante.pdf"):
                self.salvar_banco_dados(arquivo)
                lista_arquivos_para_mover.append(arquivo)
            elif(arquivo.split(" ")[-1].lower() == "pago.pdf"):
                lista_arquivos_para_mover.append(arquivo)
            else:
                pass

        self.mover_arquivos(lista_arquivos_para_mover)

    def salvar_banco_dados(self, arquivo):
        data = arquivo.split(" - ")[0]
        descricao = arquivo.split(" - ")[1]
        caminho_arquivo = self.gerar_caminho_arquivo_banco(arquivo)
        # arquivopath = self.criar_caminho_pasta_destino(arquivo)
        # arquivopath2 = self.pasta_comprovantes + '/' + arquivo
        conta = Conta(descricao, data, caminho_arquivo)
        sqllite_connection.insert_conta(conta)

    def gerar_caminho_arquivo_banco(self, arquivo):
        caminho_arquivo_banco = self.criar_caminho_pasta_destino(arquivo)
        caminho_arquivo_banco = caminho_arquivo_banco.replace('\\', '/')
        return caminho_arquivo_banco

    def mover_arquivos(self, lista_arquivos_para_mover):
        print("Movendo Arquivos...")
        for arquivo in lista_arquivos_para_mover:
            self.mostrar_log(arquivo)            
            self.criar_pasta_se_nao_existir(arquivo)
            shutil.move(self.criar_caminho_pasta_origem(arquivo), self.criar_caminho_pasta_destino(arquivo))

    def mostrar_log(self, arquivo):
        print ('{}{}{}'.format(self.pasta_origem, "\\", arquivo))

    def criar_pasta_se_nao_existir(self, arquivo):
        if (not os.path.exists('{}{}{}{}{}'.format(self.pasta_destino, "\\", arquivo[0:4], "\\", arquivo[0:7]))):
                os.makedirs('{}{}{}{}{}'.format(self.pasta_destino, "\\", arquivo[0:4], "\\", arquivo[0:7]))

    def criar_caminho_pasta_origem(self, arquivo):
        caminho_pasta_arquivo = '{}{}{}'.format(self.pasta_origem, "\\", arquivo)
        return caminho_pasta_arquivo

    def criar_caminho_pasta_destino(self, arquivo):
        caminho_pasta_arquivo = '{}{}{}{}{}{}{}'.format(self.pasta_destino, "\\", arquivo[0:4], "\\", arquivo[0:7], "\\", arquivo)
        return caminho_pasta_arquivo

if __name__ == "__main__":
    app = MoveArquivos(r"C:\Users\danie\Desktop", r"G:\Meu Drive\Documentos\Comprovantes\Mae")
    app.main()
    