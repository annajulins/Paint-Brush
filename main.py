#importações dos demais arquivos
from modelo.figuras import *
from janelaPaint import *
from modelo.desenho import *
from controladorPaint import *

visao = JanelaPaint()
desenho = Desenho(visao)
controlador = ControladorPaint(desenho, visao)
visao.root.mainloop()
