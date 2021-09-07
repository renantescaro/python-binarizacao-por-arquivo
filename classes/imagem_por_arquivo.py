import cv2
import numpy
from PIL import Image
from datetime import datetime as dt


class ImagemPorArquivo:
    def __init__(self, caminho_origem='', caminho_destino='') -> None:
        self.caminho_origem = caminho_origem
        self.caminho_destino = caminho_destino
        self.extensao_imagem = '.png' 


    def ler(self, nome_imagem):
        caminho_imagem = str(self.caminho_origem)+'/'+str(nome_imagem)
        imagem = cv2.imread(caminho_imagem)
        imagem = cv2.cvtColor(imagem,cv2.COLOR_BGR2RGB)
        return Image.fromarray(imagem)


    def gravar(self, imagem, nome_imagem=None):
        imagem = cv2.cvtColor(numpy.asarray(imagem), cv2.COLOR_RGB2BGR)
        nome   = self._gerar_nome_imagem(nome_imagem)
        cv2.imwrite(nome, imagem)


    def _gerar_nome_imagem(self, nome_imagem=None):
        if nome_imagem is None:
            data_hora = str(dt.today().strftime('%d-%m-%Y_%H-%M-%S'))
            return str(self.caminho_destino)+'/'+str(data_hora)+str(self.extensao_imagem)

        nome_imagem = self._remover_extensao_nome_imagem(nome_imagem)
        return str(self.caminho_destino)+'/'+str(nome_imagem)+str(self.extensao_imagem)


    def _remover_extensao_nome_imagem(self, nome_imagem:str):
        nome_imagem = nome_imagem.lower()
        nome_imagem = nome_imagem.replace('.png', '')
        nome_imagem = nome_imagem.replace('.jpg', '')
        return nome_imagem
        