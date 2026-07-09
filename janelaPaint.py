from tkinter import *
from tkinter import ttk

class JanelaPaint:
  def __init__(self): #abrir a janela tkinter
    self.root = Tk()
    self.frame = Frame(self.root)
    self.frame.pack()

    #vetor das cores a serem escolhidas
    self.cores = ["black", "red", "orange", "yellow", "green", "blue", "purple", "white"]

    #definindo a cor de desenho, o tipo de imagem/figura a ser desenhado e a sua cor de preenchimento
    self.tipo = StringVar(value='Linha')
    self.cor = StringVar(value = self.cores[0])
    self.bg = StringVar(value = self.cores[0])

    #Label, o que vai aparecer como "título" do programa
    Label(self.frame,
         text = 'Linha, Livre, Retangulo, Oval ou Circulo'
          ).grid(column=1, row=0, padx=5, pady=5)
  
    #Menu, as opções de coisas a serem desenhadas
    OptionMenu(self.frame, self.tipo,
            'Linha', 'Livre', 'Oval', 'Retangulo', 'Circulo'
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
    
    #Area de desenho
    self.canvas = Canvas(self.frame,
                      bg= 'white',
                      width= 700,
                      height= 500)
  
    self.canvas.grid(column=1, row=10, columnspan= 2)

    
