import tkinter as tk 
from tkinter import *
import os
from time import strftime

root = tk.Tk()
root.title('RELOGIO')
root.geometry("300x320")
root.maxsize(900, 800)
root.minsize(900, 800)
root.configure(background='#1d1d1d')

light = PhotoImage(file='bringtness.png')
dark = PhotoImage(file='dark.png')

def toggle_dark_mode():
   if root['bg'] == '#1d1d1d':
      root['bg'] = 'white'
      tela['bg'] = 'white'
      saudacao['bg'] = 'white'
      horas['bg'] = 'white'
      dark_mode_button['image'] = light
      dark_mode_button['image'] = 'white'

   else:
      root['bg'] = '#1d1d1d'
      tela['bg'] = '#1d1d1d'
      saudacao['bg'] = '#1d1d1d'
      horas['bg'] = '#1d1d1d'
      dark_mode_button['image'] = dark
      dark_mode_button['image'] = '#1d1d1d'
        
def get_saudacao():
      nome_usuario = os.getlogin()
      saudacao.config(text='Olá, seja muito bem vind0(a), ' + nome_usuario)

def get_data():
      data_atual = strftime('%a,%d %b %y')
      data.config(text=data_atual)

def get_horas():  
    hora_atual = strftime ('%H:%M:%S')
    horas.config(text=hora_atual)
    horas.after(1000, get_horas)
    

dark_mode_button = Button(root, command=toggle_dark_mode)
dark_mode_button.config(image=dark, bd=0, bg='#1d1d1d')
dark_mode_button.pack(pady=10)
tela = tk.Canvas(root, width=600, height=20, bg='#1d1d1d', bd=0, highlightthickness=0, relief='ridge')

tela.pack()
saudacao = Label(root, bg='#1d1d1d', fg='#8e27ea', font=('Montserrat', 16))
saudacao.pack()
data = Label (root, bg='#1d1d1d', fg='#8e27ea', font=('Montserrat', 14, 'bold'))
data.pack(pady=2)
horas = Label(root, bg='#1d1d1d', fg='#8e27ea', font=('Montserrat', 14, 'bold'))

horas.pack(pady=2)
get_saudacao()
get_data()
root.mainloop()










