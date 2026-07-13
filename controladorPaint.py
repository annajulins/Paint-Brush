from modelo.desenho import *
from modelo.figuras import *
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
                        'Quadrado': Quadrado_ferramenta(self.visao, self.desenho),
                        'Livre': Livre_ferramenta(self.visao, self.desenho)}
    
    self.ferramenta_desenho = self.ferramentas['Linha'] #a ferramenta de desenho é escolhida de acordo com a figura selecionada na interface, mas eis o caso base
    self.figura_nova = None #armazena a figura que está sendo desenhada naquele momento, e, enquanto arrasta o mouse, essa figura é atualizada

    #quando o usuário muda a figura, a ferramenta de desenho também muda
    self.visao.tipo.trace_add("write", self.mudar_ferramenta)
    self.canvas = self.visao.canvas #atalho para não precisar escrever self.visao.canvas o tempo todo

    #associação de eventos do mouse à execução do que precisa ser feito pelo programa
    self.canvas.bind('<ButtonPress-1>', self.iniciar)
    self.canvas.bind('<B1-Motion>', self.mover)
    self.canvas.bind('<ButtonRelease-1>', self.incluir)
    
    #associação de eventos do tkinter à execução do que precisa ser feito pelo programa
    self.visao.cor.trace_add("write", self.mudar_cor)
    self.visao.bg.trace_add("write", self.mudar_bg)

  #com a mudança do option menu, a ferramenta de desenho também muda
  def mudar_ferramenta(self, *args):
    figura = self.visao.tipo.get() #descobre qual figura foi escolhida na interface
    self.ferramenta_desenho = self.ferramentas[figura] #muda a ferramenta de desenho para a correspondente à figura escolhida
    
  #---cor---
  def mudar_cor(self, *args):
    self.desenho.atualizar(dash=())

  def mudar_bg(self, *args):
    self.desenho.atualizar(dash=())
  
  #---eventos---
  def iniciar(self, event): #descobrir a figura escolhida, o mouse_pressionado
    self.ferramenta_desenho.iniciar(event)

  def mover(self, event): #executado enquanto o mouse está sendo arrastado
    self.ferramenta_desenho.mover(event)
  
  def incluir(self, event, dash=()): #executado quando o usuário solta o mouse
    self.ferramenta_desenho.incluir(event)
