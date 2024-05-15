from abc import get_cache_token
import tkinter as tk


root = tk.Tk()
root.title ('Legende')
root.geometry('300x450')

label_euro =tk.Label(root, text='EUR=EURO')
label_euro.pack()

label_lira=tk.Label(root, text='TRY=TÜRKISCHE LIRA(TÜRKEI)')
label_lira.pack()

label_yuan=tk.Label(root, text='CNY=RENMINBI YUAN(CHINA)')
label_yuan.pack()

label_dollar=tk.Label(root, text='USD=US-DOLLAR(USA)')
label_dollar.pack()

label_peso=tk.Label(root, text='COP=PESO(KOLUMBIEN)')
label_peso.pack()

label_forint=tk.Label(root, text='HUF=FORINT(UNGARN)')
label_forint.pack()

label_philipinische_peso=tk.Label(root, text='PHP= PESO(PHILIPPINIEN)')
label_philipinische_peso.pack()

label_vbucks=tk.Label(root, text='VB=V-BUCKS(FORTNITE)')
label_vbucks.pack()

label_zloty=tk.Label(root, text='PLN=ZLOTY(POLEN)')
label_zloty.pack()

label_rubel=tk.Label(root, text='RUB=RUBEL(RUSSLAND)')
label_rubel.pack()

label_pfund=tk.Label(root, text='GBP=PFUND STERLING(VEREINIGTES KÖNIGREICH)')
label_pfund.pack()

label_yen=tk.Label(root, text='JPY=YEN(JAPAN)')
label_yen.pack()

label_baht=tk.Label(root, text='THB=BAHT(THAILAND)')
label_baht.pack()

label_lek=tk.Label(root, text='ALL=LEK(ALBANIEN)')
label_lek.pack()

label_won=tk.Label(root, text='KRW=WON(SÜDKOREA)')
label_won.pack()