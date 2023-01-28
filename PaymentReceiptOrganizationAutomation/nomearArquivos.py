import os
import time
from time import gmtime, strftime
from datetime import datetime

class NomearArquivos:

    def __init__(self, arquivo):
        self.arquivo = arquivo

    def nomear_arquivos(self):
        data_criacao_string = self.get_data_criacao(self.arquivo)
        nome_arquivo = self.get_nome_arquivo()
        caminho_pasta_arquivo = self.alterar_caminho_arquivo()
        print(caminho_pasta_arquivo + "\\" + data_criacao_string + "_-_" + nome_arquivo)
        

    def alterar_caminho_arquivo(self):
        caminho_arquivo = self.arquivo.split("\\")[0:-1]
        caminho_arquivo = '\\'.join(caminho_arquivo)
        print(caminho_arquivo)
        return caminho_arquivo

    def get_data_criacao(self, arquivo):
        data_criacao = os.path.getctime(arquivo)
        data_criacao = time.ctime(data_criacao) 
        data_criacao = time.strptime(data_criacao , '%a %b %d %H:%M:%S %Y')
        data_criacao_string = strftime("%Y-%m-%d", data_criacao)

        return data_criacao_string

    
    def get_nome_arquivo(self):
        nome_arquivo = self.arquivo.split("\\")[-1]
        nome_arquivo = self.marcar_comprovante_ou_boleto(nome_arquivo)
        nome_arquivo = self.remover_espacos_nome_arquivo(nome_arquivo)

        return nome_arquivo
    
    def marcar_comprovante_ou_boleto(self, nome_arquivo):
        "Comprovante_IPTU_Terreno_07_de_11.pdf"
        primeira_palavra = nome_arquivo.split(" ")[0]

        nome_arquivo_sem_extensao = nome_arquivo.split(".")[0]
        
        if (primeira_palavra == "Comprovante"):
            nome_arquivo = nome_arquivo_sem_extensao + " Comprovante.pdf"

        return nome_arquivo


    def remover_espacos_nome_arquivo(self, nome_arquivo):
        nome_arquivo = nome_arquivo.replace(" ", "_")
        
        return nome_arquivo


app = NomearArquivos(r"G:\Meu Drive\Documentos\Comprovantes\Mae\2021\2021-08\Comprovante IPTU Terreno 07 de 11.pdf")
app.nomear_arquivos()