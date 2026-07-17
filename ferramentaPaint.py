from dataclasses import dataclass
from abc import ABC, abstractmethod
from tkinter import *
from janelaPaint import JanelaPaint
from modeloFiguras import *
from modeloDesenho import Desenho

@dataclass
class Ferramenta(ABC):
    visao: JanelaPaint
    desenho: Desenho

    def __post_init__(self):
        self.canvas = self.visao.canvas

    @abstractmethod
    def iniciar(self, event):
        pass

    @abstractmethod
    def mover(self, event):
        pass

    #o incluir é o msm pra todas as figuras, exceto pra o Selecionar, então não tem método incluir nos tipos de figura
    def incluir(self, event, dash=()):
        if self.figura_atual is None: 
            return
        
        if not self.figura_atual.incompleta():
            self.desenho.adicionar_figura(self.figura_atual)
            
            self.desenho.atualizar(dash=dash)


#Em cada uma dessas classes vamos fazer os eventos específicos pra cada tipo de figura sem precisar colocar vários if e else no Controlador
    #Aqui cada figura inicia e se move de acordo com sua individualidade
@dataclass
class Linha_ferramenta(Ferramenta):
    figura_atual: Linha = None

    def iniciar(self, event):
        self.figura_atual = Linha(event.x, event.y, event.x, event.y, self.visao.cor.get())  

    def mover(self, event):
        self.figura_atual.x2, self.figura_atual.y2 = event.x, event.y

        self.desenho.atualizar(dash=(5, 2))  # Atualiza o desenho com a linha tracejada
        self.figura_atual.desenhar(self.canvas, dash=(5, 2))  # Desenha a linha tracejada no canvas 


@dataclass
class Livre_ferramenta(Ferramenta):
    figura_atual: Livre = None

    def iniciar(self, event):
        self.figura_atual = Livre(self.visao.cor.get())
        self.figura_atual.adicionar_ponto(event.x, event.y)

    def mover(self, event):
        self.figura_atual.adicionar_ponto(event.x, event.y)

        self.desenho.atualizar(dash=(5, 2))  # Atualiza o desenho com a mão livre tracejada
        self.figura_atual.desenhar(self.canvas, dash=(5, 2))  # Desenha a mão livre tracejada no canvas

  
@dataclass
class Oval_ferramenta(Ferramenta):
    figura_atual: Oval = None

    def iniciar(self, event):
        self.figura_atual = Oval(event.x, event.y, event.x, event.y, self.visao.cor.get(), self.visao.bg.get())

    def mover(self, event):
        self.figura_atual.x2, self.figura_atual.y2 = event.x, event.y

        self.desenho.atualizar(dash=(5, 2))  # Atualiza o desenho com o oval tracejado
        self.figura_atual.desenhar(self.canvas, dash=(5, 2)) # Desenha o oval tracejado no canvas 
    

@dataclass
class Retangulo_ferramenta(Ferramenta):
    figura_atual: Retangulo = None

    def iniciar(self, event):
        self.figura_atual = Retangulo(event.x, event.y, event.x, event.y, self.visao.cor.get(), self.visao.bg.get())

    def mover(self, event):
        self.figura_atual.x2, self.figura_atual.y2 = event.x, event.y

        self.desenho.atualizar(dash=(5, 2))  # Atualiza o desenho com o retangulo tracejado
        self.figura_atual.desenhar(self.canvas, dash=(5, 2))  # Desenha o retangulo tracejado no canvas 


@dataclass
class Triangulo_ferramenta(Ferramenta):
    figura_atual: Triangulo = None

    def iniciar(self, event):
        self.figura_atual = Triangulo(event.x, event.y, event.x, event.y, self.visao.cor.get(), self.visao.bg.get())

    def mover(self, event):
        self.figura_atual.x2, self.figura_atual.y2 = event.x, event.y

        self.desenho.atualizar(dash=(5, 2))  # Atualiza o desenho com o retangulo tracejado
        self.figura_atual.desenhar(self.canvas, dash=(5, 2))  # Desenha o retangulo tracejado no canvas 


@dataclass
class Quadrado_ferramenta(Ferramenta):
    figura_atual: Quadrado = None

    def iniciar(self, event, dash=()):
        self.figura_atual = Quadrado(event.x, event.y, event.x, event.y, self.visao.cor.get(), self.visao.bg.get())

    def mover(self, event):
        self.figura_atual.x2, self.figura_atual.y2 = event.x, event.y

        self.desenho.atualizar(dash=(5, 2))  # Atualiza o desenho com o quadrado tracejado
        self.figura_atual.desenhar(self.canvas, dash=(5, 2))  # Desenha ao quadrado tracejado no canvas 
    


@dataclass
class Circulo_ferramenta(Ferramenta):
    figura_atual: Circulo = None

    def iniciar(self, event):
        self.figura_atual = Circulo(event.x, event.y, 0, self.visao.cor.get(), self.visao.bg.get())
    
    def mover(self, event):
        self.figura_atual.r = ((event.x - self.figura_atual.x)**2 + (event.y - self.figura_atual.y)**2)**0.5

        self.desenho.atualizar(dash=(5, 2))  # Atualiza o desenho com o oval tracejado
        self.figura_atual.desenhar(self.canvas, dash=(5, 2)) # Desenha o oval tracejado no canvas 



class Selecionar_ferramenta(Ferramenta): #a classe selecao
    figura_selecionada : Figura = None

    ultimo_x : int = 0 
    ultimo_y : int = 0

    def iniciar(self, event):
        item = self.canvas.find_closest(event.x, event.y) #essa função do Tkinter pega a figura mais próxima ao clique do usuário na área de desenho
        id_figura = item[0] #essa função retorna uma tupla, onde a primeira posição é o ID da figura

        self.figura_selecionada = self.desenho.buscar_figura(id_figura) #agora que já tem o ID vai buscar qual figura tem esse ID 

        self.ultimo_x, self.ultimo_y = event.x, event.y #atualiza o ultimo x e y 

        self.desenho.atualizar(figura_selecionada = self.figura_selecionada) #atualizando a figura com as modificações

    def mover(self, event):
        if self.figura_selecionada is None:
            return

        dx = event.x - self.ultimo_x #dx representa a quantidade de pixels que foram movidos no eixo x entre o ultimo ponto e o atual
        dy = event.y - self.ultimo_y #dy representa a quantidade de pixels que foram movidos no eixo y entre o ultimo ponto e o atual

        self.figura_selecionada.mover(dx, dy) #a própria figura sabe se mover
        self.desenho.atualizar(figura_selecionada = self.figura_selecionada) #atualiza a figura

        self.ultimo_x, self.ultimo_y = event.x, event.y 

    def incluir (self, event):
        pass
