class Canvas:
    def __init__(self, canvas):
        self.canvas = canvas
    
    def desenhar(self, figuras):
        self.canvas.delete("all")
        for f in figuras:
            f.desenhar(self.canvas)
