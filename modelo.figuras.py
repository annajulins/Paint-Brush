from tkinter import *
from abc import ABC, abstractmethod

# ==== CLASSE PAI(ABSTRATA) ====
class Figura(ABC):
    def __init__(self, cor, bg): #definição de cor (preenchimento ou desenho) e de background
        self.cor = cor
        self.bg = bg
        
    @abstractmethod
    def desenhar (self, canvas):
        pass #serve para desenhar as figuras, e, como cada uma tem sua forma de desenho, serão especificadas nas subclasses
        
    @abstractmethod
    def incompleta(self): #verificação se a figura desenhada está ou não finalizada
        return False

class Linha(Figura):
    def __init__(self, x1, y1, x2, y2, cor):
        super().__init__(cor, "") #a linha não tem bg, por isso o ""
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2 #as quatro coordenadas, equivalentes ao ponto inicia e ao final, são armazenadas

    def desenhar(self, canvas, dash=()): #no caso de arrasto do mouse, a linha é criada a partir do ponto inicial e do ponto final, sendo a sua cor definida por "fill"
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, 
                           fill = self.cor, dash=dash) 

    def incompleta(self): #se o mouse não sair do lugar, é retornada uma linha de comprimento 0
        return (self.x1, self.y1) == (self.x2, self.y2)

class Circulo(Figura):
    def __init__(self, x, y, r, cor, bg): #são armazenados o centro do circulo, bem como seu raio e as cores de preenchimento e 
        super().__init__(cor, bg)
        self.x, self.y, self.r = x, y, r

    def desenhar(self, canvas, dash=()): #como o tkinter não tem um método para circulo, é utilizado o de ovais com a lógica de calculo de distancia de dois pontos para encontrar o raio
        canvas.create_oval(self.x - self.r, self.y - self.r, 
                           self.x + self.r, self.y + self.r, 
                           outline = self.cor, fill = self.bg, dash=dash)
        
    def incompleta(self):
        return self.r == 0 #em caso de figura incompleta, o raio tem comprimento 0
        # raio_x = abs(self.x2 - self.x1)
        # raio_y = abs(self.y2 - self.y1)

        # return raio_x == 0 or raio_y == 0
    
class Oval(Figura):
    def __init__(self, x1, y1, x2, y2, cor, bg):
        super().__init__(cor, bg)
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2 #armazena as coordenadas dos "cantos"

    def desenhar(self, canvas, dash=()):
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, 
                           outline = self.cor, fill = self.bg, dash=dash)

    def incompleta(self):
        return (self.x1, self.y1) == (self.x2, self.y2) #se os dois cantos forem iguais, o oval nao tem tamanho
        # return self.x1 == self.x2 or self.y1 == self.y2
    
class Retangulo(Figura):
    def __init__(self, x1, y1, x2, y2, cor, bg):
        super().__init__(cor, bg)
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2 #cantos armazenados por meio de dois pares de coordenadas

    def desenhar(self, canvas, dash=()):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, 
                                outline = self.cor, fill = self.bg, dash=dash)

    def incompleta(self):
        return (self.x1, self.y1) == (self.x2, self.y2) #raciocinio parece com o de oval, ja que, na igualdade dos cantos, o retangulo nao tem tamanho
        # return self.x1 == self.x2 or self.y1 == self.y2
    
