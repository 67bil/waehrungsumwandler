import tkinter as tk
import currencyapicom #API
client = currencyapicom.Client('cur_live_nQra2J0SGFy6q39HriU9LkK8lRUzXoOe4ELKIENr') #API Key

root = tk.Tk()
root.title('Währungsumwandler')
root.geometry('500x500')

label_wahrung = tk.Label(root, text='Währungsumwandler', font=('Arial', 12)) #Währungsumwandler Text (Überschrift)
label_wahrung.pack(pady=20) #Position

frame = tk.Frame(root) #Frame von 'dropdown1' und 'dropdown2'
frame.pack(pady=10) #Position

#Auswählbare Währungen
options = ['EUR', 'USD', 'TRY', 'CNY', 'RUB', 'GBP', 'COP', 'HUF', 'PHP', 'PLN', 'KGS', 'JPY', 'THB', 'ALL', 'KRW', 'SOS', 'VB'] 

#Auswählbare Währungen in den Dropdowns
selected_option = tk.StringVar(root) #Auswahl bekommt einen Wert
selected_option.set(options[0]) #Auswahl wird bei Start auf 0 (EUR) gesetzt
dropdown1 = tk.OptionMenu(frame, selected_option, *options) #Erste Dropdown Auswahl
dropdown1.pack(side=tk.LEFT) #Position 
dropdown1.config(font=('Courier', 12)) #Schrift

selected_option2 = tk.StringVar(root) #Auswahl bekommt einen Wert
selected_option2.set(options[1]) #Auswahl wird bei Start auf 1 (TRY) gesetzt
dropdown2 = tk.OptionMenu(frame, selected_option2, *options) #Zweite Dropdown Auswahl
dropdown2.pack(side=tk.RIGHT) #Position 
dropdown2.config(font=('Courier', 12)) #Schrift

###Funktion zum Berechnen/Umwandeln
def berechnen():
    result = client.latest() #Ergebnisse sollen die neusten Werte haben

    #Quellwährung
    qw = selected_option.get() #Auswahl aus Dropdown wird gegettet
    if qw == 'VB':
        q = 950 / 10 # 950 V-Bucks = 10 USD oder 1 V-Buck = 10 / 950 USD (Alte Preise)
    else:
        q = result['data'][qw]['value']  # result=client.latest, data=Wechselkurse, qw=Quellwährung, value= Wechselkurs der Währung
        #Kurzgesagt: Wechselkurse der Quellwährung
    #Zielwährung
    zw = selected_option2.get()
    if zw == 'VB':
        z = 950 / 10
    else:
        z = result['data'][zw]['value'] #result=client.latest, data=Wechselkurse, zw=Zielwährung, value = Wechselkurs der Währung
        #Kurzgesagt: Wechselkurse der Zielwährung

    ergebnis = (float(entry_var.get()) / q) * z #Rechnung
    output_var.set(round(ergebnis, 2)) #Gerundet auf zwei Nachkommastellen

###Funktion zum Zurücksetzen
def reset():
    entry_var.set('')
    output_var.set('')

###Ein- und Ausgabefelder
entry_var = tk.StringVar() #Speichert die Eingabe
entry = tk.Entry(root, textvariable=entry_var) #Eingabefeld
entry.pack()
output_var = tk.StringVar() #Speichert das Ergebnis
output_field = tk.Entry(root, textvariable=output_var, state='readonly') #Ausgabefeld welches durch readonly schreibgeschützt ist
output_field.pack()

###Knöpfe für das Berechnen und Zurücksetzen
berechnen_button = tk.Button(root, text='Berechnen', font=('Courier', 10), command=berechnen) 
berechnen_button.pack(padx=150, pady=5) #Position
zurucksetzen_button = tk.Button(root, text='Zurücksetzen', font=('Courier', 10), command=reset) 
zurucksetzen_button.pack(padx=10) #Position

# Herr Alkan bester Lehrer ❤

###Legende
def open_legende():
    rootlegende = tk.Tk()
    rootlegende.title('Legende')
    rootlegende.geometry('300x350')

    ###Texte 
    label_euro = tk.Label(rootlegende, text='EUR=EURO') 
    label_euro.pack()

    label_dollar = tk.Label(rootlegende, text='USD=US-DOLLAR(USA)')
    label_dollar.pack()

    label_lira = tk.Label(rootlegende, text='TRY=TÜRKISCHE LIRA(TÜRKEI)')
    label_lira.pack()

    label_yuan = tk.Label(rootlegende, text='CNY=RENMINBI YUAN(CHINA)')
    label_yuan.pack()

    label_rubel = tk.Label(rootlegende, text='RUB=RUBEL(RUSSLAND)')
    label_rubel.pack()

    
    label_pfund = tk.Label(rootlegende, text='GBP=PFUND STERLING(VEREINIGTES KÖNIGREICH)')
    label_pfund.pack()
    
    label_peso = tk.Label(rootlegende, text='COP=PESO(KOLUMBIEN)')
    label_peso.pack()

    label_forint = tk.Label(rootlegende, text='HUF=FORINT(UNGARN)')
    label_forint.pack()

    label_philipinische_peso = tk.Label(rootlegende, text='PHP=PESO(PHILIPPINIEN)')
    label_philipinische_peso.pack()

    label_zloty = tk.Label(rootlegende, text='PLN=ZLOTY(POLEN)')
    label_zloty.pack()


    label_yen = tk.Label(rootlegende, text='JPY=YEN(JAPAN)')
    label_yen.pack()

    label_baht = tk.Label(rootlegende, text='THB=BAHT(THAILAND)')
    label_baht.pack()

    label_lek = tk.Label(rootlegende, text='ALL=LEK(ALBANIEN)')
    label_lek.pack()

    label_won = tk.Label(rootlegende, text='KRW=WON(SÜDKOREA)')
    label_won.pack()

    label_sol = tk.Label(rootlegende, text='SOL=Somalia Schilling (Somalia)')
    label_sol.pack()

    label_vb = tk.Label(rootlegende, text='VB=VBucks (Fortnite)')
    label_vb.pack()

b2 = tk.Button(root, text="Legende", font=('Courier', 10), command=open_legende) #Knopf 'Legende'
b2.pack(side=tk.RIGHT, anchor=tk.SE, padx=10, pady=10) #Position

root.mainloop()
