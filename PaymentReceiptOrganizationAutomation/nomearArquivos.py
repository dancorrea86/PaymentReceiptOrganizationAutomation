import os
import time
from time import gmtime, strftime
from datetime import datetime

class NomearArquivosNovosEVelhosComData:

    def __init__(self, arquivo):
        self.arquivo = arquivo

    def nomear_arquivos_com_data(self):
        data_criacao_string = self.retorna_data_modificacao_arquivo()
        nome_arquivo = self.retorna_nome_arquivo()
        caminho_pasta_arquivo = self.retorna_caminho_arquivo(data_criacao_string, nome_arquivo)
        self.renomar_arquivo(caminho_pasta_arquivo)

    def retorna_data_modificacao_arquivo(self):
        data_criacao = os.path.getmtime(self.arquivo)
        data_criacao = time.ctime(data_criacao) 
        data_criacao = time.strptime(data_criacao , '%a %b %d %H:%M:%S %Y')
        data_criacao_string = strftime("%Y-%m-%d", data_criacao)
        return data_criacao_string

    def retorna_nome_arquivo(self):
        nome_arquivo = self.arquivo.split("\\")[-1]
        return nome_arquivo

    def retorna_caminho_arquivo(self, data_criacao_string, nome_arquivo):
        caminho_arquivo = self.arquivo.split("\\")[0:-1]
        caminho_arquivo = '\\'.join(caminho_arquivo)
        novo_caminho_arquivo = caminho_arquivo + "\\" + data_criacao_string + " - " + nome_arquivo
        return novo_caminho_arquivo
 
    def renomar_arquivo(self, novo_nome):
        os.rename(self.arquivo, novo_nome)
        
class InserirFinalArquivo:

    def __init__(self, arquivo):
        #C:\Users\danie\Desktop\Teste\2021-09-30 - Comprovante Cartão Extra.pdf
        self.arquivo = arquivo
    
    def marcar_comprovante_ou_boleto_pago_arquivo(self):
        nome_arquivo = self.arquivo.split('\\')[-1]
        nome_arquivo_sem_data = nome_arquivo.split(' - ')[-1]
        primeira_palavra_arquivo = nome_arquivo_sem_data.split(' ')[0]
                
        if (primeira_palavra_arquivo.lower() == "comprovante"):
            novo_nome_arquivo = self.arquivo.split('.p')[0] + ' Comprovante.pdf'
            self.renomar_arquivo(novo_nome_arquivo)
        elif(primeira_palavra_arquivo.lower() == "boleto"):
            novo_nome_arquivo = self.arquivo.split('.p')[0]  + ' Boleto Pago.pdf'
            self.renomar_arquivo(novo_nome_arquivo)

    def renomar_arquivo(self, novo_nome):
        os.rename(self.arquivo, novo_nome)

    


    # def retirar_dia_nome_arquivo(self, nome_arquivo):
    #     nome_arquivo = nome_arquivo.split(" - ")[1]
    #     nome_arquivo_sem_extensao = nome_arquivo.split(".p")[0]
    #     primeira_palavra = nome_arquivo_sem_extensao.split(" ")[0]

    #     if (primeira_palavra.lower() == "comprovante"):
    #         nome_arquivo = nome_arquivo_sem_extensao + " Comprovante.pdf"
    #     elif (primeira_palavra.lower() == "boleto"):
    #         nome_arquivo = nome_arquivo_sem_extensao + " Boleto Pago.pdf"

    #     return nome_arquivo
        
    
    # def marcar_comprovante_ou_boleto(self, nome_arquivo):
    #     "Comprovante_IPTU_Terreno_07_de_11.pdf"
    #     primeira_palavra = nome_arquivo.split(" ")[0]

    #     nome_arquivo_sem_extensao = nome_arquivo.split(".p")[0]

        
    #     if (primeira_palavra == "Comprovante"):
    #         nome_arquivo = nome_arquivo_sem_extensao + " Comprovante.pdf"

    #     return nome_arquivo


    # def remover_espacos_nome_arquivo(self, nome_arquivo):
    #     nome_arquivo = nome_arquivo.replace(" ", "_")
        
    #     return nome_arquivo





# for arquivo in arquivos:
#     caminho_arquivo = (r'C:\Users\danie\Desktop\Teste' + "\\" + arquivo)
#     app = NomearArquivosComData(caminho_arquivo)
#     app.nomear_arquivos_com_data()

def nomear_arquivos_novos_velhos_com_data(pasta):
    # arquivos = os.listdir(r'C:\Users\danie\Desktop\Teste')
    arquivos = os.listdir(pasta)
    for arquivo in arquivos:
        caminho_arquivo = (r'C:\Users\danie\Desktop\Teste' + "\\" + arquivo)
        app = NomearArquivosNovosEVelhosComData(caminho_arquivo)
        app.nomear_arquivos_com_data()

def inserir_final_arquivo(pasta):
    arquivos = os.listdir(pasta)
    for arquivo in arquivos:
        caminho_arquivo = (r'C:\Users\danie\Desktop\Teste' + "\\" + arquivo)
        app = InserirFinalArquivo(caminho_arquivo)
        app.marcar_comprovante_ou_boleto_pago_arquivo()
