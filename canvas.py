class Canvas_draw: #essa classe gere os canavs do tkinter
    def __init__(self, canvas):
        self.canvas = canvas #recebe o real canvas
    
    def desenhar(self, figuras):
        self.canvas.delete("all") #limpa tudo
        for f in figuras:
            f.desenhar(self.canvas) #desenha todas as figuras armazenadas(polimorfismo)
