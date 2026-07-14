from tkinter import *
from tkinter import ttk 
from tkinter import filedialog, messagebox

class JanelaPaint:
  def __init__(self): #abrir a janela tkinter
    self.root = Tk()

    self.root.title("Paint Brush")
    self.root.configure(bg="#ECECEC")

    #criando uma barra de ferramentas para deixar o programa visualmente mais bonito
    self.toolbar = Frame(
        self.root,
        bg="#D9D9D9",
        height=45
    )
    self.toolbar.pack(fill=X)

    #o frame é tipo o recipiente para organizar widgets
    self.frame = Frame(
          self.root,
          bg="#ECECEC"
        ) 
    self.frame.pack(fill=BOTH, expand=True) #o pack coloca o frame dentro da janela

    #vetor das cores a serem escolhidas
    self.cores = ["black", "red", "orange", "yellow", "green", "blue", "purple", "white"]

    #definindo (e armazenando) a cor de desenho, o tipo de imagem/figura a ser desenhado e a sua cor de preenchimento
    self.tipo = StringVar(value='Linha')
    self.cor = StringVar(value = self.cores[0])
    self.bg = StringVar(value = self.cores[0])

    #Criando os botões e adicionando eles na barra de ferramentas 
    #Label, o que vai aparecer ao lado do botão dos tipos de figura
    Label(self.toolbar, text = 'Tipo:', bg="#D9D9D9").pack(side=LEFT, padx=(10,2)) 
  
    #botão das figuras
    OptionMenu(self.toolbar, 
               self.tipo,
              'Linha', 'Livre', 'Oval', 'Retangulo', 'Circulo', 'Quadrado'
             ).pack(side=LEFT)

    #texto bonitinho ao lado da opção das cores
    Label (self.toolbar, text = 'Cor:', bg="#D9D9D9").pack(side=LEFT, padx=(15,2)) 

    #botão das cores da linha
    OptionMenu(
            self.toolbar,
            self.cor,
            *self.cores
        ).pack(side=LEFT)

    #Texto ao lado da opção das cores de preenchimento
    Label (self.toolbar, text = 'Preenchimento:', bg="#D9D9D9").pack(side=LEFT, padx=(15,2)) 

    #botão das cores de preenchimento
    OptionMenu(
          self.toolbar,
          self.bg,
          *self.cores
        ).pack(side=LEFT)
    #o * desempacota a lista de cores

    #Area de desenho
    self.canvas = Canvas(self.frame,
                      bg= "#FAFAFA",
                      width= 1000,
                      height= 500)
    
    self.canvas.grid(column=1, row=10, columnspan= 2)

    #criando os botões pra salvar e abrir os arquivos
    botao_salvar = Button(
      self.toolbar,
      text = "Salvar projeto",
      command = self.salvar_arquivo
    ).pack(side=LEFT, padx=7, pady=5)

    botao_abrir = Button(
      self.toolbar,
      text = "Abrir projeto",
      command = self.abrir_arquivo
    ).pack(side=LEFT, padx=7, pady=5)

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
    
