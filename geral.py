# ==== APLICANDO ====
class Geral:
    def __init__(self, root):
        self.root = root

        self.figuras = []
        self.figura_nova = None

        self.cores = ["black", "red", "orange", "yellow", "green", "blue", "purple", "white"]

        self.tipo = StringVar(value='Linha')
        self.cor = StringVar(value = self.cores[0])
        self.bg = StringVar(value = self.cores[0])

        self.interface()

    # ----- Interface gráfica -----
    def interface (self):
        self.frame = Frame(self.root)
        self.frame.pack()

        Label(self.frame,
               text='Linha, Livre, Retangulo, Oval ou Circulo:'
               ).grid(column=0, row=0, padx=5, pady=5)

        OptionMenu(self.frame, self.tipo, 
                    'Linha', 'Livre', 'Oval', 'Retangulo', 'Circulo'
                    ).grid(column=1, row=0)

        self.canvas = Canvas(self.frame, 
                             bg='white', 
                             width=700, 
                             height=500)
        
        self.canvas.grid(column=0, row=1, columnspan=2)

        OptionMenu(
            self.root,
            self.cor,
            *self.cores
        ).pack()

        OptionMenu(
            self.root,
            self.bg,
            *self.cores
        ).pack()

        self.canvas.bind('<ButtonPress-1>', self.iniciar)
        self.canvas.bind('<B1-Motion>', self.mover)
        self.canvas.bind('<ButtonRelease-1>', self.incluir)

        self.cor.trace_add("write", self.mudar_cor)
        self.bg.trace_add("write", self.mudar_bg)

    # ----- cor -----
    def mudar_cor(self, *args):
        self.atualizar()

    def mudar_bg(self, *args):
        self.atualizar()

    # ----- eventos -----
    def iniciar(self, event):
        tipo = self.tipo.get()

        if tipo == 'Linha':
            self.figura_nova = Linha(event.x, event.y, event.x, event.y, self.cor.get())
        elif tipo == 'Circulo':
            self.figura_nova = Circulo(event.x, event.y, 0, self.cor.get(), self.bg.get())
        elif tipo == 'Oval':
            self.figura_nova = Oval(event.x, event.y, event.x, event.y, self.cor.get(), self.bg.get())
        elif tipo == 'Retangulo':
            self.figura_nova = Retangulo(event.x, event.y, event.x, event.y, self.cor.get(), self.bg.get())
        else: #sobrou só livre
            self.figura_nova = Livre(self.cor.get())
            self.figura_nova.adicionar_ponto(event.x, event.y)

    def mover(self, event):
        if self.figura_nova is None:
            return
    
        tipo = self.tipo.get()

        if tipo == 'Livre':
            self.figura_nova.adicionar_ponto(event.x, event.y)
        elif tipo == 'Circulo':
            self.figura_nova.r = ((event.x - self.figura_nova.x)**2 + (event.y - self.figura_nova.y)**2)**0.5
        else:
            self.figura_nova.x2, self.figura_nova.y2 = event.x, event.y

        self.atualizar()


    def incluir(self, event):
        if self.figura_nova is None:
            return 
        
        if not self.figura_nova.incompleta():
            self.figuras.append(self.figura_nova)

        self.figura_nova = None

        self.atualizar()

    def atualizar(self):
        self.canvas.delete("all")

        for figura in self.figuras:
            figura.desenhar(self.canvas)

        if self.figura_nova is not None:
            self.figura_nova.desenhar(
                self.canvas,
                dash=(4, 2)
            )
