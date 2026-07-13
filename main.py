#importações dos demais arquivos
from modelo.figuras import *
from janelaPaint import *
from modelo.desenho import *
from controladorPaint import *
from arquivosPaint import *
from ferramentaPaint import *

visao = JanelaPaint()
desenho = Desenho(visao)
controlador = ControladorPaint(desenho, visao)
arquivos = Arquivos(desenho, visao)


visao.arquivos = arquivos
visao.root.mainloop()
