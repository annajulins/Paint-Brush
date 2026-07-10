from modelo.desenho import *
from modelo.figuras import *
from janelaPaint import *


class ControladorPaint:

  def __init__(self, desenho: Desenho, visao: JanelaPaint): #a janela gráfica e onde as figuras serão armazenadas
    self.desenho = desenho
    self.visao = visao
    self.figura_nova = None #armazena a figura que está sendo desenhada naquele momento, e, enquanto arrasta o mouse, essa figura é atualizada

    self.canvas = self.visao.canvas #atalho para não precisar escrever self.visao.canvas o tempo todo

    #associação de eventos do mouse à execução do que precisa ser feito pelo programa
    self.canvas.bind('<ButtonPress-1>', self.iniciar)
    self.canvas.bind('<B1-Motion>', self.mover)
    self.canvas.bind('<ButtonRelease-1>', self.incluir)

    self.visao.cor.trace_add("write", self.mudar_cor)
    self.visao.bg.trace_add("write", self.mudar_bg)

  #---cor---
  def mudar_cor(self, *args):
    self.desenho.atualizar(dash=())

  def mudar_bg(self, *args):
    self.desenho.atualizar(dash=())

  #---eventos---
  def iniciar(self, event): #descobrir a figura escolhida
    tipo = self.visao.tipo.get()

    if tipo == 'Linha':
      self.figura_nova = Linha(event.x, event.y, event.x, event.y, self.visao.cor.get())
    elif tipo == 'Circulo':
      self.figura_nova = Circulo(event.x, event.y, 0, self.visao.cor.get(), self.visao.bg.get())
    elif tipo == 'Oval':
      self.figura_nova = Oval(event.x, event.y, event.x, event.y, self.visao.cor.get(), self.visao.bg.get())
    elif tipo == 'Retangulo':
      self.figura_nova = Retangulo(event.x, event.y, event.x, event.y, self.visao.cor.get(), self.visao.bg.get())
    else: #sobrou so livre
      self.figura_nova = Livre(self.visao.cor.get())
      self.figura_nova.adicionar_ponto(event.x, event.y)

  def mover(self, event): #executado enquanto o mouse está sendo arrastado
    if self.figura_nova is None:
      return #se não existe figura em execução não é retornado nada, o código vai adiante

    tipo = self.visao.tipo.get()
    if tipo == 'Livre':
      self.figura_nova.adicionar_ponto(event.x, event.y)
    elif tipo == 'Circulo':
      self.figura_nova.r = ((event.x - self.figura_nova.x)**2 + (event.y - self.figura_nova.y)**2)**0.5
    else:
      self.figura_nova.x2, self.figura_nova.y2 = event.x, event.y

    self.desenho.adicionar_figura(self.figura_nova)
    self.figura_nova.desenhar(self.canvas, dash=(4,2)) #desenho provisório (figura tracejada)
    self.desenho.atualizar(dash=(4, 2)) #atualização da tela, redesenha tudo
      
  #executado quando o usuário solta o mouse
  def incluir(self, event, dash=()):
    if self.figura_nova is None: #verifica se a figura é válida
      return
    if not self.figura_nova.incompleta():
      self.desenho.adicionar_figura(self.figura_nova)
      
    #a figura deixa de ser tracejada e vira definitiva
    self.desenho.atualizar(dash=dash)
