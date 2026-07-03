class Geral:
    def _init_(self, root):
        self.root = root

        self.figuras = [] #guarda todas as figuras desenhadas
        self.figura_nova = None #figura que esta sendo criada naquele momento

        self.cores = ["black", "red", "orange", "yellow", "green", "blue", "purple", "white"] #cores a serem escolhidas

        self.tipo = StringVar() #variaveis do tkinter
        self.cor = StringVar(value = self.cores[0]) #cor da borda
        self.bg = StringVar(value = self.cores[0]) #cor do preenchimento

# ----- interface gráfica -----
    def interface (self, label, option_menu, canvas):
        self.label = Label(frame, text='Linha, Livre, Retangulo, Oval ou Circulo')
        self.label.grid(column=0, row=0, sticky=W, **paddings)

        self.tipo.get() = StringVar(window)
        self.option_menu = OptionMenu(frame, self.tipo.get(), 
                                    'Linha', 'Livre', 'Oval', 'Retangulo', 'Circulo')
        self.option_menu.grid(column=1, row=0, sticky=W, **paddings)

        self.canvas = Canvas(frame, bg='white', width=900, height=900)
        self.canvas.grid(column=0, row=1, columnspan=2, sticky=W, **paddings)

        self.frame.pack()

# ----- eventos -----
    def iniciar(self, event): #chamada quando o usuario pressiona o mouse
        tipo = self.tipo.get() #obtem o tipo escolhido de imagem pelo usuario

        if tipo == 'Linha':
            self.figura_nova = Linha(event.x, event.y, event.x, event.y, self.cor.get()) #inicialmente começo e fim são iguais, por isso o ponto fica "duplicado"
        elif tipo == 'Circulo':
            self.figura_nova = Circulo(event.x, event.y, 0, self.cor.get(), self.bg.get()) #raio comeca de tamanho nulo
        elif tipo == 'Oval':
            self.figura_nova = Oval(event.x, event.y, event.x, event.y, self.cor.get(), self.bg.get()) #os cantos sao os mesmos 
        elif tipo == 'Retangulo':
            self.figura_nova = Retangulo(event.x, event.y, event.x, event.y, self.cor.get(), self.bg.get()) #os cantos sao os mesmos
        else: #sobrou só livre
            self.figura_nova = Livre(self.cor.get())
            self.figura_nova.adicionar_ponto(event.x, event.y) #o primeiro ponto é adicionado a lista

    def mover(self, event):
        tipo = self.tipo.get()

        if tipo == 'Livre':
            self.figura_nova.adicionar_ponto(event.x, event.y)
        elif tipo == 'Circulo':
            self.figura_nova.r = ((event.x - self.figura_nova.x)**2 + (event.y - self.figura_nova.y)**2)**0.5
        else:
            self.figura_nova.x2, self.figura_nova.y2 = event.x, event.y

    def incluir(self, event): #quando o desenho, termina, verifica se a figura é valida, e, se sim, esta sera adicionada a lista de definitiva
        if not self.figura_nova.incompleta():
            self.figuras.append(self.figura_nova)

        atualizar()

    def atualizar(self):
        t = Canvas_draw()
        t.desenhar(self.figuras[])

