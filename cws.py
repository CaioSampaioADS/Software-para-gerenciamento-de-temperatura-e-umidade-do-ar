from tkinter import *
import matplotlib as plt
from tkinter import ttk
import pymysql
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



class UserWindow:

    def __init__(self):
        self.root = Tk()
        self.root.title('CWS')
        self.root['bg'] = 'white'
        self.root.geometry('1200x610')



        Label(self.root, text='Community Weather Station - CWS', bg='white', pady=10, fg='#23B0DC', font=('Times', '19')).pack()

        Button(self.root, text='Temperatura', fg='white', width=10, relief='flat', bg='#848686', cursor='fleur', command=self.matplotlib).place(x=960, y=70)
        Button(self.root, text='Umidade', fg='white', width=10, relief='flat', bg='#2BB1DB',cursor='fleur', command=self.matplotlib2).place(x=840, y=70)

        self.mainframe = Frame(self.root, height='5c', width='7c', highlightbackground="black", highlightthickness=1, bg='white').place(x=430, y=70)

        Label(self.mainframe, text='Sensores', bg='white', font=('helvetica', '12'),fg='#135A9C').place(x=525, y=80)

        Label(self.mainframe, text='HR202', bg='white', font=('helvetica', '12'), fg='#23B0DC').place(x=440, y=120)

        Label(self.mainframe, text='Generic NTC', bg='white', font=('helvetica', '12'), fg='#23B0DC').place(x=440, y=150)

        Label(self.mainframe, text='DS1820B', bg='white', font=('helvetica', '12'), fg='#23B0DC').place(x=440, y=180)

        self.temperaturaFrame = Frame(self.root, height='2c', width='7c', bg='#135A9C').place(x=70, y=70)

        Label(self.mainframe, text='28°C', bg='#135A9C', font=('helvetica', '17'), fg='white').place(x=175, y=90)

        self.UmidadeFrame = Frame(self.root, height='2c', width='7c', bg='#23B0DC').place(x=70, y=180)

        Label(self.mainframe, text='55%', bg='#23B0DC', font=('helvetica', '17'), fg='white').place(x=175, y=200)

        Button(self.root, text='Dados Nacionais', width=15, bg='#578CEB', relief='flat').place(x=140, y=600)

        Button(self.root, text='Banco de Dados', width=15, bg='#578CEB', relief='flat', command=self.MostrarBD).place(x=490, y=600)



        
        
        
        


        self.GraficoPizza()


        self.GraficoDuasBarras()


        self.root.mainloop()

    def matplotlib(self):
        self.frame = Frame(self.root, height=250, width=250)
        self.frame.place(x=750, y=120)
        f = Figure(figsize=(4, 4), dpi=100)
        a = f.add_subplot(111)

        try:
            conexao = pymysql.connect(
                host='cws1.mysql.uhserver.com',
                user='caio12',
                password='teste',
                db='cws1',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from weather_records')
                resultado = cursor.fetchall()
        except:
            print('erro no banco de dados')

        temperatura = []

        for linha in resultado:
            temperatura.append(linha['temperature'])

        x = list(range(0, len(temperatura)))

        a.plot(x, temperatura)
        canvas = FigureCanvasTkAgg(f, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

    def matplotlib2(self):

        try:
            conexao = pymysql.connect(
                host='cws1.mysql.uhserver.com',
                user='caio12',
                password='caio@sampaio12',
                db='cws1',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from weather_records')
                resultado = cursor.fetchall()
        except:
            print('erro no banco de dados')

        umidade = []

        for linha in resultado:
            umidade.append(linha['humidity'])

        x = list(range(0, len(umidade)))

        self.frame = Frame(self.root, height=250, width=250)
        self.frame.place(x=750, y=120)
        f = Figure(figsize=(4, 4), dpi=100)
        a = f.add_subplot(111)

        a.bar(x, umidade)

        canvas = FigureCanvasTkAgg(f, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

    def GraficoPizza(self):
        self.mainframe2 = Frame(self.root, height='5c', width='7c', bg='white')
        self.mainframe2.place(x=410, y=280)
        label = ['Ano', 'Outubro']
        dados = [21.16, 24.2]

        f = Figure(figsize=(3, 3), dpi=100)
        a = f.add_subplot(111)


        cores = ['#61D3EF', '#7A3CF1']

        a.pie(dados, labels=label, autopct='%1.1f%%', shadow=True, startangle=True, colors=cores)



        canvas = FigureCanvasTkAgg(f, master=self.mainframe2)
        canvas.draw()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

    def GraficoDuasBarras(self):
        import numpy as np
        self.mainframe3 = Frame(self.root, height='5c', width='7c', bg='white')
        self.mainframe3.place(x=60, y=280)
        atual = [28, 55]
        media = [21, 65]

        barwidth = 0.25
        x = 0
        f = Figure(figsize=(3, 3), dpi=100)
        a = f.add_subplot(111)

        r1 = np.arange(len(atual))
        r2 = [x + barwidth for x in r1]

        a.bar(r1, atual, color='#6A5ACD', width=barwidth, label='atual')

        a.bar(r2, media, color='#6495ED', width=barwidth, label='media')

        canvas = FigureCanvasTkAgg(f, master=self.mainframe3)
        canvas.draw()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)


    def MostrarBD(self):
        MostrarBD = Toplevel()
        MostrarBD.title('Banco de dados')

        self.tree = ttk.Treeview(MostrarBD, selectmode="browse",
                                 column=("column1", "column2", "column3"),
                                 show='headings')

        self.tree.column("column1", width=300, stretch=NO)
        self.tree.heading('#1', text='Horario')

        self.tree.column("column2", width=100, stretch=NO)
        self.tree.heading('#2', text='Temperatura')

        self.tree.column("column3", width=100, stretch=NO)
        self.tree.heading('#3', text='umidade')



        self.tree.grid(row=0, column=4, padx=10, pady=10, columnspan=3, rowspan=6)

        self.MostrarBDBackEnd()

        MostrarBD.mainloop()

    def MostrarBDBackEnd(self):

        try:
            conexao = pymysql.connect(
                host='cws1.mysql.uhserver.com',
                user='caio12',
                password='caio@sampaio12',
                db='cws1',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from weather_records')
                resultado = cursor.fetchall()
        except:
            print('erro no banco de dados')

        linhaV = []



        for linha in resultado:
            linhaV.append(linha['time'])
            linhaV.append(linha['temperature'])
            linhaV.append(linha['humidity'])



            self.tree.insert("", END, values=linhaV, tag='1')

            linhaV.clear()



UserWindow()