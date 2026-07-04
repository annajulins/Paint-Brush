class Circulo(Figura):
    def __init__(self, x, y, r, cor, bg): #são armazenados o centro do circulo, bem como seu raio e as cores de preenchimento e 
        super().__init__(cor, bg)
        self.x, self.y, self.r = x, y, r

    def desenhar(self, canvas, dash=()): #como o tkinter não tem um método para circulo, é utilizado o de ovais com a lógica de calculo de distancia de dois pontos para encontrar o raio
        canvas.create_oval(self.x - self.r, self.y - self.r, 
                           self.x + self.r, self.y + self.r, 
                           outline = self.cor, fill = self.bg, dash=dash)
        
    def incompleta(self):
        return self.r == 0 #em aso de figura incompleta, o raio tem comprimento 0
