class Circulo(Figura):
    def __init__(self, x, y, r, cor, bg):
        super().__init__(cor, bg)
        self.x, self.y, self.r = x, y, r

    def desenhar(self, canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r, 
                           self.x + self.r, self.y + self.r, 
                           outline = self.cor, fill = self.bg)
        
    def incompleta(self):
        return self.r == 0
