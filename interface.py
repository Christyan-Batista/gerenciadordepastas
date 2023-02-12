from tkinter import *

class App:
    def __init__(self):

        self.window = Tk()

        self.imginterface = PhotoImage(file='interface.png')
        self.imgbotaogerar = PhotoImage(file='botaogerar.png')
        self.imgbotaoapagar = PhotoImage(file='botaoapagar.png')
        self.logo = PhotoImage(file='logo-vektor.png')

        self.interface()
        self.botoes()
        self.entrys()
        self.checkbox()
        self.window.mainloop()

    def interface(self):
        self.window.geometry('500x500')
        self.window.title('Gerenciador de Pastas')

        self.label = Label(self.window,image=self.imginterface)
        self.label.pack()

        self.label_logo = Label(self.window, image = self.logo, background='#001637')
        self.label_logo.place(x=165, y=25)

    def botoes(self):
        self.botaogerar = Button(self.window, image=self.imgbotaogerar)
        self.botaogerar.place(width='150', height= '43', x=55, y=400)
        self.botaoapagar = Button(self.window, image=self.imgbotaoapagar)
        self.botaoapagar.place(width='150', height= '43', x=300, y=400)

    def entrys(self):
        self.inputcliente = Entry(self.window, font=('Open Sans Light', 15), justify=LEFT, bd=2)
        self.inputcliente.place(width='400', height= '44',x=50, y=180)

    def checkbox(self):
        self.sb = Checkbutton(self.window, text='S.B')
        self.sb.place(x=50,y=250)
        self.tg = Checkbutton(self.window, text='T.G')
        self.tg.place(x=168,y=250)
        self.la = Checkbutton(self.window, text='L.A')
        self.la.place(x=286,y=250)
        self.dt = Checkbutton(self.window, text='D.T')
        self.dt.place(x=405,y=250)

App()