from tkinter import *
from tkinter import ttk 

class JanelaPaint:
  def __init__(self): #abrir a janela tkinter
    self.root = Tk()
    self.frame = Frame(self.root) #o frame é tipo o recipiente para organizar widgets
    self.frame.pack() #o pack coloca o frame dentro da janela

    #vetor das cores a serem escolhidas
    self.cores = ["black", "red", "orange", "yellow", "green", "blue", "purple", "white"]

    #definindo (e armazenando) a cor de desenho, o tipo de imagem/figura a ser desenhado e a sua cor de preenchimento
    self.tipo = StringVar(value='Linha')
    self.cor = StringVar(value = self.cores[0])
    self.bg = StringVar(value = self.cores[0])

    #Label, o que vai aparecer como "título" do programa (título da interface)
    Label(self.frame,
         text = 'Linha, Livre, Retangulo, Oval, Circulo ou Quadrado'
          ).grid(column=1, row=0, padx=5, pady=5) #grid() posiciona o widget numa tabela, e os pads são os espaçamentos
  
    #Menu, as opções a serem desenhadas
    OptionMenu(self.frame, self.tipo,
            'Linha', 'Livre', 'Oval', 'Retangulo', 'Circulo', 'Quadrado'
             ).grid(column= 1, row= 1)

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
    #o * desempacota a lista de cores

    #Area de desenho
    self.canvas = Canvas(self.frame,
                      bg= 'white',
                      width= 700,
                      height= 500)
  
    self.canvas.grid(column=1, row=10, columnspan= 2)

    #criando os botões pra salvar e abrir os arquivos
    botao_salvar = Button(
      self.frame,
      text = "Salvar projeto",
      command = self.salvar_arquivo
    )

    botao_abrir = Button(
      self.frame,
      text = "Abrir projeto",
      command = self.abrir_arquivo
    )

    #colocando os botões de salvar e abrir na tela
    botao_salvar.grid(column=1, row=11)

    botao_abrir.grid(column=2, row=11)

  def salvar_arquivo(self):
    self.arquivos.salvar("teste.pnt")

  def abrir_arquivo(self):
    self.arquivos.abrir("teste.pnt")
    
