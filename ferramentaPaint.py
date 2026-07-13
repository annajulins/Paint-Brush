from dataclasses import dataclass
from abc import ABC, abstractmethod
from tkinter import *
from view import JanelaPaint
from beca import Linha, Circulo, Oval, Retangulo, Quadrado, Livre
from desenho import Desenho

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

    @abstractmethod
    def incluir(self, event, dash=()):
        pass

#linha
@dataclass
class Linha_ferramenta(Ferramenta):
    figura_atual: Linha = None

    def iniciar(self, event):
        self.figura_atual = Linha(event.x, event.y, event.x, event.y, self.visao.cor.get())  

    def mover(self, event):
        self.figura_atual.x2, self.figura_atual.y2 = event.x, event.y

        self.desenho.atualizar(dash=(5, 2))  # Atualiza o desenho com a linha tracejada
        self.figura_atual.desenhar(self.canvas, dash=(5, 2))  # Desenha a linha tracejada no canvas 

    def incluir(self, event, dash=()):
        if self.figura_atual is None: #verifica se a figura é válida
            return
        
        if not self.figura_atual.incompleta():
            self.desenho.adicionar_figura(self.figura_atual)
            
            #a figura deixa de ser tracejada e vira definitiva
            self.desenho.atualizar(dash=dash)

#mão livre
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
    
    def incluir(self, event, dash=()):
        if self.figura_atual is None: #verifica se a figura é válida
            return
        
        if not self.figura_atual.incompleta():
            self.desenho.adicionar_figura(self.figura_atual)
            
            #a figura deixa de ser tracejada e vira definitiva
            self.desenho.atualizar(dash=dash)

#oval      
@dataclass
class Oval_ferramenta(Ferramenta):
    figura_atual: Oval = None

    def iniciar(self, event):
        self.figura_atual = Oval(event.x, event.y, event.x, event.y, self.visao.cor.get(), self.visao.bg.get())

    def mover(self, event):
        self.figura_atual.x2, self.figura_atual.y2 = event.x, event.y

        self.desenho.atualizar(dash=(5, 2))  # Atualiza o desenho com o oval tracejado
        self.figura_atual.desenhar(self.canvas, dash=(5, 2)) # Desenha o oval tracejado no canvas 
    
    def incluir(self, event, dash=()):
        if self.figura_atual is None: #verifica se a figura é válida
            return
        
        if not self.figura_atual.incompleta():
            self.desenho.adicionar_figura(self.figura_atual)
            
            #a figura deixa de ser tracejada e vira definitiva
            self.desenho.atualizar(dash=dash)
    
#retangulo
@dataclass
class Retangulo_ferramenta(Ferramenta):
    figura_atual: Retangulo = None

    def iniciar(self, event):
        self.figura_atual = Retangulo(event.x, event.y, event.x, event.y, self.visao.cor.get(), self.visao.bg.get())

    def mover(self, event):
        self.figura_atual.x2, self.figura_atual.y2 = event.x, event.y

        self.desenho.atualizar(dash=(5, 2))  # Atualiza o desenho com o retangulo tracejado
        self.figura_atual.desenhar(self.canvas, dash=(5, 2))  # Desenha o retangulo tracejado no canvas 

    def incluir(self, event, dash=()):
        if self.figura_atual is None: #verifica se a figura é válida
            return
        
        if not self.figura_atual.incompleta():
            self.desenho.adicionar_figura(self.figura_atual)
            
            #a figura deixa de ser tracejada e vira definitiva
            self.desenho.atualizar(dash=dash)


#quadrado
@dataclass
class Quadrado_ferramenta(Ferramenta):
    figura_atual: Quadrado = None

    def iniciar(self, event, dash=()):
        self.figura_atual = Quadrado(event.x, event.y, event.x, event.y, self.visao.cor.get(), self.visao.bg.get())

    def mover(self, event):
        self.figura_atual.x2, self.figura_atual.y2 = event.x, event.y

        self.desenho.atualizar(dash=(5, 2))  # Atualiza o desenho com o quadrado tracejado
        self.figura_atual.desenhar(self.canvas, dash=(5, 2))  # Desenha ao quadrado tracejado no canvas 

    def incluir(self, event, dash=()):
        if self.figura_atual is None: #verifica se a figura é válida
            return
        
        if not self.figura_atual.incompleta():
            self.desenho.adicionar_figura(self.figura_atual)
            
            #a figura deixa de ser tracejada e vira definitiva
            self.desenho.atualizar(dash=dash)
    

#circulo
@dataclass
class Circulo_ferramenta(Ferramenta):
    figura_atual: Circulo = None

    def iniciar(self, event):
        self.figura_atual = Circulo(event.x, event.y, 0, self.visao.cor.get(), self.visao.bg.get())
    
    def mover(self, event):
        self.figura_atual.r = ((event.x - self.figura_atual.x)**2 + (event.y - self.figura_atual.y)**2)**0.5

        self.desenho.atualizar(dash=(5, 2))  # Atualiza o desenho com o oval tracejado
        self.figura_atual.desenhar(self.canvas, dash=(5, 2)) # Desenha o oval tracejado no canvas 

    def incluir(self, event, dash=()):
        if self.figura_atual is None: #verifica se a figura é válida
            return
        
        if not self.figura_atual.incompleta():
            self.desenho.adicionar_figura(self.figura_atual)
            
            #a figura deixa de ser tracejada e vira definitiva
            self.desenho.atualizar(dash=dash)



