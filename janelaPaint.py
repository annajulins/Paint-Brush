from tkinter import *
from tkinter import ttk 
from tkinter import filedialog, messagebox
from tkinter import PhotoImage
from icones_base64 import *

class JanelaPaint:
  def __init__(self): #abrir a janela tkinter
    self.root = Tk()

    self.root.title("Paint Brush")
    self.root.configure(bg="#ECECEC")

    #------------------------------------Criando os Frames---------------------------------------------

    #criando uma barra de ferramentas acima da área de desenho para deixar o programa visualmente mais bonito
    self.toolbar = Frame(
        self.root,
        bg="#BFEFFF",
        height=45
    )
    self.toolbar.pack(fill=X)

    #o frame é tipo o recipiente para organizar widgets, esse é o principal
    self.frame_principal = Frame(
          self.root,
          bg="#ECECEC"
        ) 
    self.frame_principal.pack(fill=BOTH, expand=True) #o pack coloca o frame dentro da janela

    #criando 2 outros frames dentro do frame principal para fazer uma barra lateral de ferramentas
    self.frame_canvas = Frame(self.frame_principal)
    self.frame_canvas.pack(side='left', fill = 'both', expand = True)

    self.frame_lateral = Frame(
      self.frame_principal,
      width = 250,
      bg = "#BFEFFF"
    )
    self.frame_lateral.pack(side="right", fill="y")
    self.frame_lateral.pack_propagate(False) #isso impede que a largura diminua por causa dos botões

    #---------------------------------------------------------------------------------------------

    #vetor das cores a serem escolhidas
    self.cores = ["black", "red", "orange", "yellow", "green", "blue", "purple", "white"]

    #definindo (e armazenando) a cor de desenho, o tipo de imagem/figura a ser desenhado e a sua cor de preenchimento
    self.tipo = StringVar(value='Linha')
    self.cor = StringVar(value = self.cores[0])
    self.bg = StringVar(value = self.cores[0])

    # ------------------------------------Botões---------------------------------------------

    #Criando os botões dos tipos de figura e adicionando eles na barra de ferramentas lateral

    ##Salvando em variáveis os ícones dos tipos de figura do arquivo dos ícones 
    self.img_linha = PhotoImage(data=LINHA)
    self.img_circulo = PhotoImage(data=CIRCULO)
    self.img_oval = PhotoImage(data=OVAL)
    self.img_retangulo = PhotoImage(data=RETANGULO)
    self.img_quadrado = PhotoImage(data=QUADRADO)
    self.img_livre = PhotoImage(data=LIVRE)

    Button(
      self.frame_lateral,
      image = self.img_linha,
      command = lambda : self.tipo.set("Linha"),
      relief = "flat",
      bg = "#BFEFFF",
      activebackground="#99D9EA",
      bd = 0,
      highlightthickness=0
    ).grid(row=1, column=0, padx=3, pady=3)

    Button(
      self.frame_lateral,
      image = self.img_circulo,
      command = lambda : self.tipo.set("Circulo"),
      relief = "flat",
      bg = "#BFEFFF",
      activebackground="#99D9EA",
      bd = 0,
      highlightthickness=0
    ).grid(row=0, column=0, padx=3, pady=3)

    Button(
      self.frame_lateral,
      image = self.img_oval,
      command = lambda : self.tipo.set("Oval"),
      relief = "flat",
      bg = "#BFEFFF",
      activebackground="#99D9EA",
      bd = 0,
      highlightthickness=0
    ).grid(row=0, column=2, padx=3, pady=3)

    Button(
      self.frame_lateral,
      image = self.img_retangulo,
      command = lambda : self.tipo.set("Retangulo"),
      relief = "flat",
      bg = "#BFEFFF",
      activebackground="#99D9EA",
      bd = 0,
      highlightthickness=0
    ).grid(row=1, column=1, padx=3, pady=3)

    Button(
      self.frame_lateral,
      image = self.img_quadrado,
      command = lambda : self.tipo.set("Quadrado"),
      relief = "flat",
      bg = "#BFEFFF",
      activebackground="#99D9EA",
      bd = 0,
      highlightthickness=0
    ).grid(row=1, column=2, padx=3, pady=3)

    Button(
      self.frame_lateral,
      image = self.img_livre,
      command = lambda : self.tipo.set("Livre"),
      relief = "flat",
      bg = "#BFEFFF",
      activebackground="#99D9EA",
      bd = 0,
      highlightthickness=0
    ).grid(row=0, column=1, padx=3, pady=3)

    #Salvando em variáveis os ícones de cor do arquivo dos ícones
    self.img_preto = PhotoImage(data=PRETO)
    self.img_vermelho = PhotoImage(data=VERMELHO)
    self.img_laranja = PhotoImage(data=LARANJA)
    self.img_amarelo = PhotoImage(data=AMARELO)
    self.img_verde = PhotoImage(data=VERDE)
    self.img_azul = PhotoImage(data=AZUL)
    self.img_roxo = PhotoImage(data=ROXO)
    self.img_branco = PhotoImage(data=BRANCO)

    #Mensagem acima das cores de linha
    Label(
        self.frame_lateral,
        text="Cor da linha:",
        bg="#BFEFFF",
        font=("Arial", 10, "bold")
    ).grid(row=4, column=0, columnspan=4, pady=(40,16))

    #Botões das cores da linha
    Button(
      self.frame_lateral,
      image = self.img_preto,
      command = lambda : self.cor.set("black"),
      relief = "flat",
      bg = "#BFEFFF",
      activebackground="#99D9EA",
      bd = 0,
      highlightthickness=0
    ).grid(row=5, column=0, padx=3, pady=3)

    Button(
      self.frame_lateral,
      image = self.img_vermelho,
      command = lambda : self.cor.set("red"),
      relief = "flat",
      bg = "#BFEFFF",
      activebackground="#99D9EA",
      bd = 0,
      highlightthickness=0
    ).grid(row=5, column=1, padx=3, pady=3)

    Button(
      self.frame_lateral,
      image = self.img_laranja,
      command = lambda : self.cor.set("orange"),
      relief = "flat",
      bg = "#BFEFFF",
      activebackground="#99D9EA",
      bd = 0,
      highlightthickness=0
    ).grid(row=5, column=2, padx=3, pady=3)

    Button(
      self.frame_lateral,
      image = self.img_amarelo,
      command = lambda : self.cor.set("yellow"),
      relief = "flat",
      bg = "#BFEFFF",
      activebackground="#99D9EA",
      bd = 0,
      highlightthickness=0
    ).grid(row=5, column=3, padx=3, pady=3)

    Button(
      self.frame_lateral,
      image = self.img_verde,
      command = lambda : self.cor.set("green"),
      relief = "flat",
      bg = "#BFEFFF",
      activebackground="#99D9EA",
      bd = 0,
      highlightthickness=0
    ).grid(row=6, column=0, padx=3, pady=3)

    Button(
      self.frame_lateral,
      image = self.img_azul,
      command = lambda : self.cor.set("blue"),
      relief = "flat",
      bg = "#BFEFFF",
      activebackground="#99D9EA",
      bd = 0,
      highlightthickness=0
    ).grid(row=6, column=1, padx=3, pady=3)

    Button(
      self.frame_lateral,
      image = self.img_roxo,
      command = lambda : self.cor.set("purple"),
      relief = "flat",
      bg = "#BFEFFF",
      activebackground="#99D9EA",
      bd = 0,
      highlightthickness=0
    ).grid(row=6, column=2, padx=3, pady=3)

    Button(
      self.frame_lateral,
      image = self.img_branco,
      command = lambda : self.cor.set("white"),
      relief = "flat",
      bg = "#BFEFFF",
      activebackground="#99D9EA",
      bd = 0,
      highlightthickness=0
    ).grid(row=6, column=3, padx=3, pady=3)

    #Mensagem acima das cores de preenchimento
    Label(
        self.frame_lateral,
        text="Cor de preenchimento:",
        bg="#BFEFFF",
        font=("Arial", 10, "bold")
    ).grid(row=8, column=0, columnspan=4, pady=(40,16))

    #Botões das cores de preenchimento
    Button(
      self.frame_lateral,
      image = self.img_preto,
      command = lambda : self.bg.set("black"),
      relief = "flat",
      bg = "#BFEFFF",
      activebackground="#99D9EA",
      bd = 0,
      highlightthickness=0
    ).grid(row=9, column=0, padx=3, pady=3)

    Button(
      self.frame_lateral,
      image = self.img_vermelho,
      command = lambda : self.bg.set("red"),
      relief = "flat",
      bg = "#BFEFFF",
      activebackground="#99D9EA",
      bd = 0,
      highlightthickness=0
    ).grid(row=9, column=1, padx=3, pady=3)

    Button(
      self.frame_lateral,
      image = self.img_laranja,
      command = lambda : self.bg.set("orange"),
      relief = "flat",
      bg = "#BFEFFF",
      activebackground="#99D9EA",
      bd = 0,
      highlightthickness=0
    ).grid(row=9, column=2, padx=3, pady=3)

    Button(
      self.frame_lateral,
      image = self.img_amarelo,
      command = lambda : self.bg.set("yellow"),
      relief = "flat",
      bg = "#BFEFFF",
      activebackground="#99D9EA",
      bd = 0,
      highlightthickness=0
    ).grid(row=9, column=3, padx=3, pady=3)

    Button(
      self.frame_lateral,
      image = self.img_verde,
      command = lambda : self.bg.set("green"),
      relief = "flat",
      bg = "#BFEFFF",
      activebackground="#99D9EA",
      bd = 0,
      highlightthickness=0
    ).grid(row=10, column=0, padx=3, pady=3)

    Button(
      self.frame_lateral,
      image = self.img_azul,
      command = lambda : self.bg.set("blue"),
      relief = "flat",
      bg = "#BFEFFF",
      activebackground="#99D9EA",
      bd = 0,
      highlightthickness=0
    ).grid(row=10, column=1, padx=3, pady=3)

    Button(
      self.frame_lateral,
      image = self.img_roxo,
      command = lambda : self.bg.set("purple"),
      relief = "flat",
      bg = "#BFEFFF",
      activebackground="#99D9EA",
      bd = 0,
      highlightthickness=0
    ).grid(row=10, column=2, padx=3, pady=3)

    Button(
      self.frame_lateral,
      image = self.img_branco,
      command = lambda : self.bg.set("white"),
      relief = "flat",
      bg = "#BFEFFF",
      activebackground="#99D9EA",
      bd = 0,
      highlightthickness=0
    ).grid(row=10, column=3, padx=3, pady=3)
    

    #criando os botões pra salvar e abrir os arquivos e adicionando na barra de ferramentas
    self.img_salvar = PhotoImage(data=SALVAR)
    self.img_abrir = PhotoImage(data=ABRIR)

    Button(
      self.toolbar,
      image = self.img_salvar,
      command = self.salvar_arquivo,
      relief = "flat",
      bg = "#BFEFFF",
      activebackground="#99D9EA",
      bd = 0,
      highlightthickness=0
    ).pack(side=LEFT, padx=2)

    Button(
      self.toolbar,
      image = self.img_abrir,
      command = self.abrir_arquivo,
      relief = "flat",
      bg = "#BFEFFF",
      activebackground="#99D9EA",
      bd = 0,
      highlightthickness=0
    ).pack(side=LEFT, padx=2)

    #--------------------------------------------------------------------------------------------

    #Area de desenho
    self.canvas = Canvas(self.frame_canvas,
                      bg= "#FAFAFA",
                      width= 1215,
                      height= 600)
    
    self.canvas.grid(column=1, row=10, columnspan= 2)

  #----------------------------------------------------------------------------------------------

  #metodos de salvar e abrir arquivos, as importações do tkinter no começo do view permite que o usuário escolha um nome para seu arquivo e salve onde quiser
  def salvar_arquivo(self):
    nome = filedialog.asksaveasfilename(
        defaultextension=".pnt",
        filetypes=[("Arquivos Paint", "*.pnt")]
    )

    if nome: 
      self.arquivos.salvar(nome)
      messagebox.showinfo("Salvar", "Projeto salvo com sucesso!")

  def abrir_arquivo(self):
    nome = filedialog.askopenfilename(
        filetypes=[("Arquivos Paint", "*.pnt")]
    )

    if nome:
      self.arquivos.abrir(nome)
      messagebox.showinfo("Abrir", "Projeto carregado com sucesso!")
    
