class Livre(Figura):
    def __init__(self, cor):
        super().__init__(cor, "")
        self.pontos = [] #é criada uma lista para armazenar os pontos do rabisco

    def adicionar_ponto(self, x, y):
        self.pontos.append((x, y)) #a cada passada de mouse, as coordenadas registradas sao armazenadas na lista

    def desenhar (self, canvas):
        if len(self.pontos) > 1: #o tkinter interliga todos os pontos da lista
            canvas.create_line(self.pontos, fill = self.cor)

    def incompleta(self): #se tem apenas um ponto, nao ha linha
        return len(self.pontos) <= 1
