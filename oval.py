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
