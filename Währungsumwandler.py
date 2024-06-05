from abc import get_cache_token
import tkinter as tk
import currencyapicom
client = currencyapicom.Client('cur_live_nQra2J0SGFy6q39HriU9LkK8lRUzXoOe4ELKIENr')

root = tk.Tk()
root.title('Währungsumwandler')
root.geometry('500x500')


label_wahrung = tk.Label(root, text='Währungsumwandler', font=('Helvetica', 12))
label_wahrung.pack(pady=20)


frame = tk.Frame(root)
frame.pack(pady=10)

options = ['EUR', 'TRY', 'CNY', 'USD', 'COP', 'HUF', 'PHP', 'VB', 'PLN', 'RUB', 'KGS', 'GBP', 'JPY', 'THB', 'ALL', 'KRW', 'SOS']

selected_option = tk.StringVar(root)
selected_option.set(options[0])

dropdown1 = tk.OptionMenu(frame, selected_option, *options)
dropdown1.pack(side=tk.LEFT)

selected_option2 = tk.StringVar(root)
selected_option2.set(options[1])

dropdown2 = tk.OptionMenu(frame, selected_option2, *options)
dropdown2.pack(side=tk.RIGHT)



def berechnen():
    ###Funktion zum Umwandeln
    result = client.latest()
    #Quellwaehrung:
    qw = selected_option.get()
    q = result['data'][qw]['value']

    #Zielwaehrung
    zw = selected_option2.get()
    z = result['data'][zw]['value']

    #umzuwandeln = 1

    ergebnis =(float (entry_var.get())/q) * z
    output_var.set(round(ergebnis,2))
   
def reset():
  entry_var.set('')
  output_var.set('')


entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var)
entry.pack()
output_var = tk.StringVar()
output_field = tk.Entry(root, textvariable=output_var, state='readonly')
output_field.pack()



berechnen_button = tk.Button(root, text='Berechnen', command=berechnen)
berechnen_button.pack(padx=150,pady=5)
zurucksetzen_button = tk.Button(root, text='Zurücksetzen', command=reset)
zurucksetzen_button.pack(padx=10)

# Herr Alkan bester Lehrer ❤


'''
# Legende/Wechselkurse
def create_window():
    window = tk.Toplevel(root)
    
b1 = tk.Button(root, text="Wechselkurse", command=create_window)
b1.pack(side=tk.RIGHT, anchor=tk.SE, padx=10, pady=10)  # Move the button to the slightly up and left
'''

def open_legende():
    
    rootlegende = tk.Tk()
    rootlegende.title ('Legende')
    rootlegende.geometry('300x450')

    label_euro =tk.Label(rootlegende, text='EUR=EURO')
    label_euro.pack()

    label_lira=tk.Label(rootlegende, text='TRY=TÜRKISCHE LIRA(TÜRKEI)')
    label_lira.pack()

    label_yuan=tk.Label(rootlegende, text='CNY=RENMINBI YUAN(CHINA)')
    label_yuan.pack()

    label_dollar=tk.Label(rootlegende, text='USD=US-DOLLAR(USA)')
    label_dollar.pack()

    label_peso=tk.Label(rootlegende, text='COP=PESO(KOLUMBIEN)')
    label_peso.pack()

    label_forint=tk.Label(rootlegende, text='HUF=FORINT(UNGARN)')
    label_forint.pack()

    label_philipinische_peso=tk.Label(rootlegende, text='PHP= PESO(PHILIPPINIEN)')
    label_philipinische_peso.pack()

    label_vbucks=tk.Label(rootlegende, text='VB=V-BUCKS(FORTNITE)')
    label_vbucks.pack()

    label_zloty=tk.Label(rootlegende, text='PLN=ZLOTY(POLEN)')
    label_zloty.pack()

    label_rubel=tk.Label(rootlegende, text='RUB=RUBEL(RUSSLAND)')
    label_rubel.pack()

    label_pfund=tk.Label(rootlegende, text='GBP=PFUND STERLING(VEREINIGTES KÖNIGREICH)')
    label_pfund.pack()

    label_yen=tk.Label(rootlegende, text='JPY=YEN(JAPAN)')
    label_yen.pack()

    label_baht=tk.Label(rootlegende, text='THB=BAHT(THAILAND)')
    label_baht.pack()

    label_lek=tk.Label(rootlegende, text='ALL=LEK(ALBANIEN)')
    label_lek.pack()

    label_won=tk.Label(rootlegende, text='KRW=WON(SÜDKOREA)')
    label_won.pack()

    label_sol=tk.Label(rootlegende, text='SOL=Somalia Schilling (Somalia)')


b2 = tk.Button(root, text="Legende", command=open_legende)
b2.pack(side=tk.RIGHT, anchor=tk.SE, padx=10, pady=10) 
# New button for "Legende"








root.mainloop()

    








