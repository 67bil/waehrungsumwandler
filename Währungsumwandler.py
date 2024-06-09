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

# Auswählbare Währungen
options = ['EUR', 'USD', 'TRY', 'CNY', 'RUB', 'GBP', 'COP', 'HUF', 'PHP', 'PLN', 'KGS', 'JPY', 'THB', 'ALL', 'KRW', 'SOS', 'VB'] 

# Auswählbare Währungen in den Dropdowns
selected_option = tk.StringVar(root) # Auswahl bekommt einen Wert
selected_option.set(options[0]) # Auswahl wird bei Start auf 0 (EUR) gesetzt
dropdown1 = tk.OptionMenu(frame, selected_option, *options) # Erste Dropdown Auswahl
dropdown1.pack(side=tk.LEFT) # Position 
dropdown1.config(font=('Courier', 12)) # Schrift

selected_option2 = tk.StringVar(root) # Auswahl bekommt einen Wert
selected_option2.set(options[1]) # Auswahl wird bei Start auf 1 (TRY) gesetzt
dropdown2 = tk.OptionMenu(frame, selected_option2, *options) # Zweite Dropdown Auswahl
dropdown2.pack(side=tk.RIGHT) # Position 
dropdown2.config(font=('Courier', 12)) # Schrift

### Funktion zum Berechnen/Umwandeln
def berechnen():
    result = client.latest() # Ergebnisse sollen die neusten Werte haben

    # Quellwährung
    qw = selected_option.get() # Auswahl aus Dropdown wird gegettet
    if qw == 'VB':
        q = 950 / 10 # 950 V-Bucks = 10 EUR -> 1 V-Buck = 10 / 950 EUR
    else:
        q = result['data'][qw]['value']  # Ergebnis mit der

    # Zielwährung
    zw = selected_option2.get()
    if zw == 'VB':
        z = 950 / 10
    else:
        z = result['data'][zw]['value']

    ergebnis = (float(entry_var.get()) / q) * z
    output_var.set(round(ergebnis, 2))

### Funktion zum Zurücksetzen
def reset():
    entry_var.set('')
    output_var.set('')

### Ein- und Ausgabefelder
entry_var = tk.StringVar() # Speichert die Eingabe
entry = tk.Entry(root, textvariable=entry_var) # Eingabefeld
entry.pack()
output_var = tk.StringVar() # Speichert das Ergebnis
output_field = tk.Entry(root, textvariable=output_var, state='readonly') # Ausgabefeld welches durch readonly schreibgeschützt ist
output_field.pack()

### Knöpfe für das Berechnen und Zurücksetzen
berechnen_button = tk.Button(root, text='Berechnen', font=('Courier', 10), command=berechnen) 
berechnen_button.pack(padx=150, pady=5) # Position
zurucksetzen_button = tk.Button(root, text='Zurücksetzen', font=('Courier', 10), command=reset) 
zurucksetzen_button.pack(padx=10) # Position

# Herr Alkan bester Lehrer ❤

### Legende
legende_window = None

def open_legende():
    global legende_window #Variable für nächste Zeile
    if legende_window is not None and legende_window.winfo_exists(): #Überprüft ob bereits ein Legedne Fenster offen ist
        legende_window.destroy()
    
    legende_window = tk.Tk()
    legende_window.title('Legende')
    legende_window.geometry('300x350')
    

    ### Texte 
    label_euro = tk.Label(legende_window, text='EUR=EURO') 
    label_euro.pack()

    label_dollar = tk.Label(legende_window, text='USD=US-DOLLAR(USA)')
    label_dollar.pack()

    label_lira = tk.Label(legende_window, text='TRY=TÜRKISCHE LIRA(TÜRKEI)')
    label_lira.pack()

    label_yuan = tk.Label(legende_window, text='CNY=RENMINBI YUAN(CHINA)')
    label_yuan.pack()

    label_rubel = tk.Label(legende_window, text='RUB=RUBEL(RUSSLAND)')
    label_rubel.pack()

    
    label_pfund = tk.Label(legende_window, text='GBP=PFUND STERLING(VEREINIGTES KÖNIGREICH)')
    label_pfund.pack()
    
    label_peso = tk.Label(legende_window, text='COP=PESO(KOLUMBIEN)')
    label_peso.pack()

    label_forint = tk.Label(legende_window, text='HUF=FORINT(UNGARN)')
    label_forint.pack()

    label_philipinische_peso = tk.Label(legende_window, text='PHP=PESO(PHILIPPINIEN)')
    label_philipinische_peso.pack()

    label_zloty = tk.Label(legende_window, text='PLN=ZLOTY(POLEN)')
    label_zloty.pack()


    label_yen = tk.Label(legende_window, text='JPY=YEN(JAPAN)')
    label_yen.pack()

    label_baht = tk.Label(legende_window, text='THB=BAHT(THAILAND)')
    label_baht.pack()

    label_lek = tk.Label(legende_window, text='ALL=LEK(ALBANIEN)')
    label_lek.pack()

    label_won = tk.Label(legende_window, text='KRW=WON(SÜDKOREA)')
    label_won.pack()

    label_sol = tk.Label(legende_window, text='SOL=Somalia Schilling (Somalia)')
    label_sol.pack()

    label_vb = tk.Label(legende_window, text='VB=VBucks (Fortnite)')
    label_vb.pack()

ButtonLegende = tk.Button(root, text="Legende", font=('Courier', 10),command=open_legende) # Knopf 'Legende'
ButtonLegende.pack(side=tk.RIGHT, anchor=tk.SE, padx=10, pady=10) # Position

root.mainloop()
