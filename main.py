#MAIN
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
