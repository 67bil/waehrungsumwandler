from abc import get_cache_token
import tkinter as tk

def update_option(*args):
    selected_option.set(entry.get())

root = tk.Tk()
root.title('Währungsumrechner')
root.geometry('500x500')

options = ['EUR', 'TRY', 'CNY', 'USD', 'COP', 'HUF', 'PHP', 'VB', 'PLN', 'RUB', 'KGS', 'GBP', 'JPY', 'THB', 'ALL', 'KRW']

selected_option = tk.StringVar(root)
selected_option.set(options[0])  # 

# Label for Währung
label_wahrung = tk.Label(root, text='Währung', font=('Helvetica', 12))
label_wahrung.pack(pady=20)


frame = tk.Frame(root)
frame.pack(pady=10)

dropdown1 = tk.OptionMenu(frame, selected_option, *options[:len(options)//2])
dropdown1.pack(side=tk.LEFT)

selected_option2 = tk.StringVar(root)
selected_option2.set(options[len(options)//2]) 

dropdown2 = tk.OptionMenu(frame, selected_option2, *options[len(options)//2:])
dropdown2.pack(side=tk.RIGHT)

# Legende/Wechselkurse
def create_window():
    window = tk.Toplevel(root)

b1 = tk.Button(root, text="Wechselkurse", command=create_window)
b1.pack(side=tk.RIGHT, anchor=tk.SE, padx=10, pady=10)  

# 
def show_legende():
    legend_window = tk.Toplevel(root)
    legend_window.title("Legende")
    import legende.py as legende
    # 

b2 = tk.Button(root, text="Legende", command=show_legende)
b2.pack(side=tk.RIGHT, anchor=tk.SE, padx=10, pady=10)

root.mainloop()
