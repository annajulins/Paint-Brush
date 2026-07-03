class Linha(Figura):
    def __init__(self, x1, y1, x2, y2, cor):
        super().__init__(cor, "") #a linha não tem bg, por isso o ""
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2 #as quatro coordenadas, equivalentes ao ponto inicia e ao final, são armazenadas

    def desenhar(self, canvas): #no caso de arrasto do mouse, a linha é criada a partir do ponto inicial e do ponto final, sendo a sua cor definida por "fill"
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, 
                           fill = self.cor) 

    def incompleta(self): #se o mouse não sair do lugar, é retornada uma linha de comprimento 0
        return (self.x1, self.y1) == (self.x2, self.y2)
