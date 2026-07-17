from janelaPaint import * #a janela e o canvas onde ocorre o desenho
from modeloFiguras import * #tem que ser modeloFiguras

class Desenho: #representa o desenho completo do usuário, que ficarão armazenadas dentro do objeto
    def __init__(self, canvas1 : JanelaPaint): #o construtor recebe uma janela do estilo JanelaPaint
        self.figuras = [] #esta lista armazenará todas as figuras criadas
        self.canvas1 = canvas1 #guarda uma referência pra janela, para que a classe possa acessar o canvas


    def adicionar_figura(self, figura):
        self.figuras.append(figura) #recebe uma figura qualquer e a adiciona à lista


    def atualizar(self, dash=(), figura_selecionada = None): 
        self.canvas1.canvas.delete("all") #apaga tudo da figura e desenha dnv

        for figura in self.figuras: 
            figura.desenhar(self.canvas1.canvas) #desenhando cada figura por polimorfismo

            if figura == figura_selecionada:
                self.desenhar_selecao(figura) 


    #método para desenhar um retângulo em volta da figura selecionada para identificar qual a figura selecionada
    def desenhar_selecao(self, figura):
        x1, y1, x2, y2 = self.canvas1.canvas.bbox(figura.id_canvas) #bbox é uma função do próprio Tkinter que retorna os pontos desse retangulo
        self.canvas1.canvas.create_rectangle(
            x1 - 4, # esse 4 é pra dar um espaçamento entre esse retângulo e a figura
            y1 - 4,
            x2 + 4,
            y2 + 4,
            dash=(5, 2) #o retângulo é tracejado
        )

    #método para buscar o id da figura dentro do vetor de figuras e retornar qual é essa figura lá pra o FerramentaPaint
    def buscar_figura(self, id_figura):
        for figura in self.figuras:
            if figura.id_canvas == id_figura:
                return figura 
        return None #caso n encontre nada
        
