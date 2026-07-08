from janelaPaint import *
from modelo.figuras import *

class Desenho:
    def __init__(self, canvas1 : JanelaPaint):
        self.figuras = []
        self.canvas1 = canvas1

    def adicionar_figura(self, figura):
        self.figuras.append(figura)

    def atualizar(self, dash=()):
        self.canvas1.canvas.delete("all")

        for figura in self.figuras:
            figura.desenhar(self.canvas1.canvas, dash=dash)
