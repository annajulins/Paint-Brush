from tkinter import *
from tkinter import ttk

class JanelaPaint:
  def interface(self):
    self.frame = Frame(self.root)
    self.frame.pack()

  #Label
  Label(self.frame,
         text = 'Linha, Livre, Retangulo, Circulo'
          .grid(column=1, row=0, padx=5, pady=5)
  
  #Area de desenho
  self.canvas = Canvas(self.frame,
                      bg= 'white',
                      width= 700,
                      height= 500)
  
  self.canvas.grid(column=1, row=0, columnspan= 2)
  
  #Menu
  OptionMenu(self.frame, self.tipo,
            'Linha', 'Livre', 'Oval', 'Retangulo', 'Circulo'
             ).grid(column= 1, row= 0)

  OptionMenu(
    self.root
    self.cor
    self.cores
  ).pack()
  
  
  #OptionMenu(
   # self.root
    #self.cor
    self.cores
  ).pack()
