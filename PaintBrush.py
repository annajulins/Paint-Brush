# Paint-Brush, etapa 1
from tkinter import *
#window = Tk()

#Cores a serem usadas para definir as cores
cores = [
    "black",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
    "white"
]

def mudar_cor(*args):
    desenhar_figuras()

def mudar_back(*args):
    desenhar_figuras() 

# Quando o mouse é pressionado
def iniciar_figura_nova(event): 
    global figura_nova #a função vai modificar a variável global
    if tipo_figura_var.get() == 'Linha':
        figura_nova = ("linha", (event.x, event.y, event.x, event.y), cor_escolhida.get(), '') 
    elif tipo_figura_var.get() == 'Circulo':
        figura_nova = ("Circulo", (event.x, event.y, 0), cor_escolhida.get(), back_escolhida.get())
    elif tipo_figura_var.get() == 'Oval':
        figura_nova = ("Oval", (event.x, event.y, event.x, event.y), cor_escolhida.get(), back_escolhida.get())
    elif tipo_figura_var.get() == 'Retangulo':
        figura_nova = ("Retangulo", (event.x, event.y, event.x, event.y), cor_escolhida.get(), back_escolhida.get())
    else :
        figura_nova = ("rabisco", [(event.x, event.y)], cor_escolhida.get(), '')

# Quando o mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova
    if figura_nova[0] == "rabisco":
        figura_nova[1].append((event.x, event.y))
    elif figura_nova[0] == "Circulo":
        figura_nova = ("Circulo", (figura_nova[1][0], figura_nova[1][1], ((event.x - figura_nova[1][0])**2 + (event.y - figura_nova[1][1])**2)**0.5), cor_escolhida.get(), back_escolhida.get())
    elif figura_nova[0] == "Oval":
        figura_nova = ("Oval", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), cor_escolhida.get(), back_escolhida.get())
    elif figura_nova[0] == "Retangulo":
        figura_nova = ("Retangulo", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), cor_escolhida.get(), back_escolhida.get())
    else : # figura_nova[0] == "linha"
        figura_nova = ("linha", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), cor_escolhida.get(), '')
    desenhar_figuras()
    desenhar_figura_nova()

# Quando o mouse é solto
def incluir_figura_nova(event): 
    if not incompleta(figura_nova): # para evitar incluir figuras incompletas, como uma linha sem comprimento ou um rabisco com um único ponto
        figuras.append(figura_nova) 
    desenhar_figuras()

def desenhar_figuras():
    canvas.delete("all")
    for fig, values, cor, bg in figuras:
        if fig == "linha":
            canvas.create_line(values[0], values[1], values[2], values[3], fill=cor) 
        elif fig == "Circulo":
            canvas.create_oval(values[0] - values[2], values[1] - values[2], values[0] + values[2], values[1] + values[2], outline=cor, fill=bg)
        elif fig == "Oval":
            canvas.create_oval(values[0], values[1], values[2], values[3], outline=cor, fill=bg)
        elif fig == "Retangulo":
            canvas.create_rectangle(values[0], values[1], values[2], values[3], outline=cor, fill=bg)
        else : # fig == "rabisco"
            canvas.create_line(values, fill=cor) #tava fill e eu troquei por outline

def desenhar_figura_nova():
    fig, values, cor, bg = figura_nova
    if fig == "linha":
        canvas.create_line(values[0], values[1], values[2], values[3], dash=(4, 2), fill=cor) #dash tem a ver com o design  os pontilhados
    elif fig == "Circulo":
        canvas.create_oval(
            values[0] - values[2],
            values[1] - values[2],
            values[0] + values[2],
            values[1] + values[2],
            outline=cor,
            dash=(4, 2),
            fill= bg
      )
    elif fig == "Oval":
        canvas.create_oval(values[0],
                           values[1],
                           values[2],
                           values[3],
                           outline=cor,
                           dash=(4, 2),
                           fill= bg
    )
    elif fig == "Retangulo":
        canvas.create_rectangle(values[0],
                                values[1],
                                values[2],
                                values[3],
                                outline=cor,
                                dash=(4, 2),
                                fill= bg
        )
    else : # fig == "rabisco"
        canvas.create_line(values, dash=(4, 2), fill=cor)

def incompleta(figura):
    fig, values, cor, bg = figura
    if fig == "linha":
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == "Circulo":
        return values[2] == 0
    elif fig == "Oval":
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == "Retangulo":
        return (values[0], values[1]) == (values[2], values[3])
    else : # fig == "rabisco"
        return len(values) <= 1




#******* MAIN *******#

figuras = []       # Todas as figuras desenhadas
figura_nova = None # Figura que está sendo desenhada, mas ainda não foi incluída em figuras

window = Tk()
frame = Frame(window)

# Widgets arranjados com Layout grid dentro de frame
paddings = {'padx': 5, 'pady': 5} 

# label
label = Label(frame,  text='Linha, Rabisco, Retangulo, Oval ou  Circulo:')
label.grid(column=0, row=0, sticky=W, **paddings)

# option menu
tipo_figura_var = StringVar(window) # Guarda o tipo de figura selecionado no option menu (linha ou rabisco)
option_menu = OptionMenu(frame, tipo_figura_var,
                             'Linha', 'Rabisco', 'Oval', 'Retangulo', 'Circulo')
option_menu.grid(column=1, row=0, sticky=W, **paddings)

# Área de desenho
canvas = Canvas(frame, bg='white', width=600, height=600)
canvas.grid(column=0, row=1, columnspan=2, sticky=W, **paddings)

frame.pack()

# Eventos de mouse associados ao canvas - com seus callbacks
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

cor_escolhida = StringVar()
cor_escolhida.set(cores[0])  # cor inicial

back_escolhida = StringVar()
back_escolhida.set(cores[0])

menu_cor = OptionMenu(window, cor_escolhida, *cores)
menu_back = OptionMenu(window, back_escolhida, *cores)

menu_cor.pack()
menu_back.pack()


cor_escolhida.trace_add("write", mudar_cor)
back_escolhida.trace_add("write", mudar_back)

window.mainloop()
