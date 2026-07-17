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

class Quadrado(Figura): #classe Quadrado herda os atributos e métodos de Retangulo
    def __init__(self, x1, y1, x2, y2, cor, bg):
        super().__init__(cor, bg) #herda da classe retangulo
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

    def desenhar(self, canvas, dash=()):
        lado = min(abs(self.x2 - self.x1), abs(self.y2 - self.y1)) #o lado do quadrado é definido pelo menor valor entre a largura e a altura do retangulo
        #a função abs() retorna o valor absoluto de um número, desconsiderando o seu sinal
         
        #verificando para qual lado o usuário arrastou o mouse
        if self.x2 < self.x1: #se o segundo ponto estiver à esquerda do primeiro (mouse arrastado para a esquerda)
            self.x2 = self.x1 - lado #o segundo ponto é ajustado para a esquerda
        else:
            self.x2 = self.x1 + lado #caso contrário, o segundo ponto é ajustado para a direita (mouse arrastado para a direita)

        if self.y2 < self.y1: #se o segundo ponto estiver acima do primeiro (usuário arrastou para cima)
            self.y2 = self.y1 - lado #o segundo ponto é ajustado para cima
        else:
            self.y2 = self.y1 + lado #caso contrário, o segundo ponto é ajustado para baixo (usuário arrastou para baixo)

        #desenhando o quadrado no canvas, com as coordenadas ajustadas e as cores definidas
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2,
                                outline=self.cor, fill=self.bg, dash=dash)

    def incompleta(self):
        return (self.x1, self.y1) == (self.x2, self.y2) #mesma coisa que retangulo

class Livre(Figura):
    def __init__(self, cor):
        super().__init__(cor, "")
        self.pontos = [] #é criada uma lista para armazenar os pontos do rabisco

    def adicionar_ponto(self, x, y):
        self.pontos.append((x, y)) #a cada passada de mouse, as coordenadas registradas sao armazenadas na lista

    def desenhar (self, canvas, dash=()):
        if len(self.pontos) > 1: #o tkinter interliga todos os pontos da lista
            canvas.create_line(self.pontos, fill = self.cor, dash=dash)

    def incompleta(self): #se tem apenas um ponto, nao ha linha
        return len(self.pontos) <= 1
    



    
