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
    
