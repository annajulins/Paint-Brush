class Geral:
    def _init_(self, root):
        self.root = root

        self.figuras = [] #guarda todas as figuras desenhadas
        self.figura_nova = None #figura que esta sendo criada naquele momento

        self.cores = ["black", "red", "orange", "yellow", "green", "blue", "purple", "white"] #cores a serem escolhidas

        self.tipo = StringVar() #variaveis do tkinter
        self.cor = StringVar(value = self.cores[0]) #cor da borda
        self.bg = StringVar(value = self.cores[0]) #cor do preenchimento
