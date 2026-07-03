class Oval(Figura):
    def __init__(self, x1, y1, x2, y2, cor, bg):
        super().__init__(cor, bg)
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

    def desenhar(self, canvas):
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, 
                           outline = self.cor, fill = self.bg)

    def incompleta(self):
        return (self.x1, self.y1) == (self.x2, self.y2)
