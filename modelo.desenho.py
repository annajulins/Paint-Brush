from janelaPaint import * #a janela e o canvas onde ocorre o desenho
from modelo.figuras import *

class Desenho: #representa o desenho completo do usuário, que ficarão armazenadas dentro do objeto
    def __init__(self, canvas1 : JanelaPaint): #o construtor recebe uma janela do estilo JanelaPaint
        self.figuras = [] #esta lista armazenará todas as figuras criadas
        self.canvas1 = canvas1 #guarda uma referência pra janela, para que a classe possa acessar o canvas

    def adicionar_figura(self, figura):
        self.figuras.append(figura) #recebe uma figura qualquer e a adiciona à lista

    def atualizar(self, dash=()): #redesenha tudo que existe na lista
        self.canvas1.canvas.delete("all") #apaga tudo da figura, pois o tkinter não atualiza figuras automaticamente (é melhor apagar tudo e desenhar de novo) 

        for figura in self.figuras: #percorre todas as figuras armazenadas
            figura.desenhar(self.canvas1.canvas, dash=dash) #desenhando cada figura por polimorfismo: o código não precisa saber qual figura está sendo desenhada, ele executa o código equivalente a cada tipo de figura
            #dash: faz com que todas as figuras sejam desenhadas temporariamente (tracejadas), servindo de pré-visualização enquanto o usuário está arrastando o mouse
