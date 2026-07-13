import pickle
from desenho import Desenho

class Arquivos:
    def __init__(self, desenho : Desenho, visao):
        self.desenho = desenho
        self.visao = visao

    def salvar (self, nome_arquivo):
        with open(nome_arquivo, "wb") as arquivo:
            pickle.dump(self.desenho.figuras, arquivo)
    
    def abrir(self, nome_arquivo):
        with open(nome_arquivo, "rb") as arquivo:
            self.desenho.figuras = pickle.load(arquivo)

        #Limpar o canvas antes de redesenhar
        self.visao.canvas.delete("all")

        for forma in self.desenho.figuras:
            forma.desenhar(self.visao.canvas)
