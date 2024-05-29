from abc import get_cache_token
import tkinter as tk
import currencyapicom
client = currencyapicom.Client('cur_live_nQra2J0SGFy6q39HriU9LkK8lRUzXoOe4ELKIENr')

root = tk.Tk()
root.title('Währungsumrechner')
root.geometry('500x500')


label_wahrung = tk.Label(root, text='Währung', font=('Helvetica', 12))
label_wahrung.pack(pady=20)


frame = tk.Frame(root)
frame.pack(pady=10)

options = ['EUR', 'TRY', 'CNY', 'USD', 'COP', 'HUF', 'PHP', 'VB', 'PLN', 'RUB', 'KGS', 'GBP', 'JPY', 'THB', 'ALL', 'KRW']

selected_option = tk.StringVar(root)
selected_option.set(options[0])

dropdown1 = tk.OptionMenu(frame, selected_option, *options)
dropdown1.pack(side=tk.LEFT)

selected_option2 = tk.StringVar(root)
selected_option2.set(options[1])

dropdown2 = tk.OptionMenu(frame, selected_option2, *options)
dropdown2.pack(side=tk.RIGHT)



# Herr Alkan bester Lehrer ❤



# Legende/Wechselkurse
def create_window():
    window = tk.Toplevel(root)
    
b1 = tk.Button(root, text="Wechselkurse", command=create_window)
b1.pack(side=tk.RIGHT, anchor=tk.SE, padx=10, pady=10)  # Move the button to the slightly up and left


 
# New button for "Legende"

def open_legende():
    window = tk.Toplevel(root)
    

    # Add your content for the legend window here
 
b2 = tk.Button(root, text="Legende", command=open_legende)
b2.pack(side=tk.RIGHT, anchor=tk.SE, padx=10, pady=10)  # Move the "Legende" button to the slightly up and left


#quell_waehrung_label = tk.Label(root, text='Quellwährung', font=('Helvetica', 12))
#quell_waehrung_label.pack(side=tk.LEFT)
#ziel_waehrung_label = tk.Label(root, text='Zielwährung', font=('Helvetica', 12))
#ziel_waehrung_label.pack(side=tk.LEFT)


entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var)
entry.pack()
output_var = tk.StringVar()
output_field = tk.Entry(root, textvariable=output_var, state='readonly')
output_field.pack()




#Testen:
print(round(ergebnis,2))

# ergebnis muss in output
###Funktion zu Ende



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

    ergebnis =(int (entry_var.get())/q) * z
    output_var.set(round(ergebnis,2))
    
def reset():
  entry_var.set('')
  output_var.set('')

berechnen_button = tk.Button(root, text='Berechnen', command=berechnen)
berechnen_button.pack(side=tk.LEFT, padx=10)
zurucksetzen_button = tk.Button(root, text='Zurücksetzen', command=reset)
zurucksetzen_button.pack(side=tk.RIGHT, padx=10)





root.mainloop()
