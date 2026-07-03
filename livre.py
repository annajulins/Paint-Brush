class Livre(Figura):
    def __init__(self, cor):
        super().__init__(cor, "")
        self.pontos = []

    def adicionar_ponto(self, x, y):
        self.pontos.append((self.x, self.y))

    def desenhar (self, canvas):
        if len(self.pontos) > 1:
            canvas.create_line(self.pontos, fill = self.cor)

    def incompleta(self):
        return len(self.pontos) <= 1
