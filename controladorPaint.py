from modeloDesenho import *
from modeloFiguras import *
from janelaPaint import *
from ferramentaPaint import *


class ControladorPaint:
  def __init__(self, visao : JanelaPaint, desenho : Desenho): #a janela gráfica e onde as figuras serão armazenadas
    self.visao = visao
    self.desenho = desenho

    self.ferramentas = {'Linha': Linha_ferramenta(self.visao, self.desenho),
                        'Circulo': Circulo_ferramenta(self.visao, self.desenho),
                        'Oval': Oval_ferramenta(self.visao, self.desenho),
                        'Retangulo': Retangulo_ferramenta(self.visao, self.desenho),
                        'Triangulo': Triangulo_ferramenta(self.visao, self.desenho),
                        'Quadrado': Quadrado_ferramenta(self.visao, self.desenho),
                        'Livre': Livre_ferramenta(self.visao, self.desenho),
                        'Selecionar' : Selecionar_ferramenta(self.visao, self.desenho)}
    
    self.ferramenta_desenho = self.ferramentas['Linha'] #a ferramenta de desenho é escolhida de acordo com a figura selecionada na interface, mas eis o caso base
    self.figura_nova = None #armazena a figura que está sendo desenhada naquele momento, e, enquanto arrasta o mouse, essa figura é atualizada
    self.figura_copiada = None

    #quando o usuário muda a figura, a ferramenta de desenho também muda
    self.visao.tipo.trace_add("write", self.mudar_ferramenta)
    self.canvas = self.visao.canvas #atalho para não precisar escrever self.visao.canvas o tempo todo

    #associação de eventos do mouse à execução do que precisa ser feito pelo programa
    self.canvas.bind('<ButtonPress-1>', self.iniciar)
    self.canvas.bind('<B1-Motion>', self.mover)
    self.canvas.bind('<ButtonRelease-1>', self.incluir)
    
    #associação de eventos do teclado à execução do que precisa ser feito pelo programa
    #self.visao.root.bind('<Key>', self.teclado)
    self.canvas.bind("<Delete>", self.excluir)
    self.canvas.bind("<Right>", self.mover_frente)
    self.canvas.bind("<Left>", self.mover_tras)
    self.canvas.bind("<Up>", self.mover_topo)
    self.canvas.bind("<Down>", self.mover_fundo)
    self.canvas.bind("<Control-c>", self.copiar)
    self.canvas.bind("<Control-v>", self.colar)

    #associação de eventos do tkinter à execução do que precisa ser feito pelo programa
    self.visao.cor.trace_add("write", self.mudar_cor)
    self.visao.bg.trace_add("write", self.mudar_bg)

  #---------------------------------escolhe a ferramenta de acordo com a escolha do usuário----------------------------------
  def mudar_ferramenta(self, *args):
    figura = self.visao.tipo.get() #descobre qual figura foi escolhida na interface

    if figura != 'Selecionar': #para desmarcar a seleção quando o usuário vai utilizar outra ferramenta
        self.ferramenta_desenho.figura_selecionada = None
        self.desenho.atualizar() #para nao desenhar o retangulo tracejado

    self.ferramenta_desenho = self.ferramentas[figura] #salva nessa variável a ferramenta referente ao dicionário
    
  #------------------------------cores-----------------------------------------
  def mudar_cor(self, *args):
    figura = self.ferramentas['Selecionar']

    if figura.figura_selecionada is not None: #se houver uma figura selecionada
      figura.figura_selecionada.mudar_cor(self.visao.cor.get()) #mudar a cor da figura selecionada
      self.desenho.atualizar(figura_selecionada = figura.figura_selecionada) #atualizar ela após isso
    else:
      self.desenho.atualizar(dash=()) 


  def mudar_bg(self, *args):
    figura = self.ferramentas['Selecionar']

    if figura.figura_selecionada is not None:
      figura.figura_selecionada.mudar_bg(self.visao.bg.get())
      self.desenho.atualizar(figura_selecionada = figura.figura_selecionada)
    else:
      self.desenho.atualizar(dash=())

  
  #---------------------------- eventos mouse --------------------------
  #manter qual das iniciar?
  def iniciar(self, event): #descobrir a figura escolhida, o mouse_pressionado
    self.canvas.focus_set() #se o usuário clicar em outro widget da interface, o canvas perde o foco e não recebe mais os eventos do teclado, entao devemos chamar o método focus_set() para garantir que o canvas esteja em foco e receba os eventos do teclado
    self.ferramenta_desenho.iniciar(event)

  def mover(self, event): #executado enquanto o mouse está sendo arrastado
    self.ferramenta_desenho.mover(event)
  
  def incluir(self, event, dash=()): #executado quando o usuário solta o mouse
    self.ferramenta_desenho.incluir(event)

  #----------------------------eventos teclado--------------------------  
  def excluir(self, event):
      selecao = self.ferramentas['Selecionar']
      figura = selecao.figura_selecionada

      if figura and figura in self.desenho.figuras:
          self.desenho.figuras.remove(figura)

          selecao.figura_selecionada = None

          self.desenho.atualizar()


  def mover_frente(self, event):
      selecao = self.ferramentas['Selecionar']
      figura = selecao.figura_selecionada

      if figura and figura in self.desenho.figuras:
        idx = self.desenho.figuras.index(figura)

        if idx < len(self.desenho.figuras) - 1:
            self.desenho.figuras[idx], self.desenho.figuras[idx + 1] = \
            self.desenho.figuras[idx + 1], self.desenho.figuras[idx]

            self.desenho.atualizar(figura_selecionada=figura)           


  def mover_tras(self, event):
    selecao = self.ferramentas['Selecionar']
    figura = selecao.figura_selecionada

    if figura and figura in self.desenho.figuras:
        idx = self.desenho.figuras.index(figura)

        if idx > 0:
            self.desenho.figuras[idx], self.desenho.figuras[idx - 1] = \
            self.desenho.figuras[idx - 1], self.desenho.figuras[idx]

            self.desenho.atualizar(figura_selecionada=figura)

  
  def mover_topo(self, event): #leva a figura diretamente para a ultima posição da lista
    selecao = self.ferramentas['Selecionar']
    figura = selecao.figura_selecionada

    if figura and figura in self.desenho.figuras:
        self.desenho.figuras.remove(figura)
        self.desenho.figuras.append(figura)
        self.desenho.atualizar(figura_selecionada=figura)


  def mover_fundo(self, event): #leva a figura diretamente para a primeira posição da lista
    selecao = self.ferramentas['Selecionar']
    figura = selecao.figura_selecionada

    if figura and figura in self.desenho.figuras:
        self.desenho.figuras.remove(figura)
        self.desenho.figuras.insert(0, figura)
        self.desenho.atualizar(figura_selecionada=figura)


  def copiar(self, event):
    figura = self.ferramentas['Selecionar'].figura_selecionada

    if figura:
        self.figura_copiada = figura.copiar()


  def colar(self, event):
    if self.figura_copiada:
        nova = self.figura_copiada.copiar()

        nova.mover(10, 10) #para evitar que cópia apareça exatamente em cima da original, e, como todas tem o mover, funciona para qualquer tipo de figura
        self.desenho.figuras.append(nova)
        self.desenho.atualizar()
