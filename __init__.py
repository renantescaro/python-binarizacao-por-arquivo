from classes.binarizacao import Binarizacao
from classes.listar_arquivos import ListarArquivos
from classes.imagem_por_arquivo import ImagemPorArquivo

limiar_binarizacao = 93
caminho_origem  = 'assets/imagens_originais'
caminho_destino = 'assets/imagens_binarizadas'

imagens_originais = ListarArquivos(caminho_origem).listar()
img_por_arquivo   = ImagemPorArquivo(caminho_origem, caminho_destino)

for nome_imagem in imagens_originais:
    img_binarizada = Binarizacao(
        imagem = img_por_arquivo.ler(nome_imagem),
        limiar = limiar_binarizacao
    ).processar()
    img_por_arquivo.gravar(img_binarizada, nome_imagem)