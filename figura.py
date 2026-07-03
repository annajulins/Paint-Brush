class Figura:
    def ___init__(self, cor, bg): #definição de cor (preenchimento ou desenho) e de background
        self.cor = cor
        self.bg = bg

    def desenhar (self, canvas):
        pass #serve para "redesenhar" as figuras antes feitas

    def incompleta(self): #verificação se a figura desenhadas está ou não finalizada
        return False
    
