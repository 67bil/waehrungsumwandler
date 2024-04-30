from abc import get_cache_token
import tkinter as tk

def validate_input(input):
    if input.isdigit():
        return True
    else:
        return False

root = tk.Tk()
root.title('Währungsumrechner')
root.geometry('500x500')

options = ['EUR', 'TRY', 'CNY', 'USD', 'COP', 'HUF', 'PHP', 'VB', 'PLN', 'RUB', 'KGS', 'GBP', 'JPY', 'THB', 'ALL', 'KRW']

label_wahrung = tk.Label(root, text='Währung', font=('Helvetica', 12))
label_wahrung.pack(pady=20)

frame = tk.Frame(root)
frame.pack(pady=10)

selected_option = tk.StringVar(root)
selected_option.set(options[0])

dropdown1 = tk.OptionMenu(frame, selected_option, *options)
dropdown1.pack(side=tk.LEFT)

selected_option2 = tk.StringVar(root)
selected_option2.set(options[0])

dropdown2 = tk.OptionMenu(frame, selected_option2, *options)
dropdown2.pack(side=tk.RIGHT)

def validate_decimal_input(input):
    if input.replace('.', '', 1).isdigit():
        return True
    else:
        return False



start_wahrung_label = tk.Label(root, text='Startwährung', font=('Helvetica', 12))
start_wahrung_label.pack(side=tk.LEFT)
ziel_wahrung_label = tk.Label(root, text='Zielwährung', font=('Helvetica', 12))
ziel_wahrung_label.pack(side=tk.LEFT)

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var)
entry.pack()
output_var = tk.StringVar()
output_field = tk.Entry(root, textvariable=output_var, state='readonly')
output_field.pack()




def reset():
  entry_var.set('')
  output_var.set('')

berechnen_button = tk.Button(root, text='Berechnen')
berechnen_button.pack(side=tk.LEFT, padx=10)
zurucksetzen_button = tk.Button(root, text='Zurücksetzen', command=reset)
zurucksetzen_button.pack(side=tk.RIGHT, padx=10)

root.mainloop()