#importações dos demais arquivos
from modeloFiguras import *
from janelaPaint import *
from modeloDesenho import *
from controladorPaint import *
from arquivosPaint import *
from ferramentaPaint import *

visao = JanelaPaint()
desenho = Desenho(visao)
controlador = ControladorPaint(desenho, visao)
arquivos = Arquivos(desenho, visao)


visao.arquivos = arquivos
visao.root.mainloop()
