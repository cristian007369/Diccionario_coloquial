from tkinter import *

ventana_principal =Tk()
ventana_principal.geometry("500x500")

text_uno = Text(ventana_principal, bg="white", fg="gray", font=("Times New Roman", 25), bd=0, width=13, height=1)
text_uno.insert("1.0", f"texto predeterminado")
text_uno.bind("<Button-1>", lambda event: text_uno.delete("1.0", "end") if text_uno.get("1.0", "end-1c") == "texto predeterminado" else text_uno.config(bg="black", fg="yellow"))


text_uno.place(x=25, y=26)

text_un = Text(ventana_principal, bg="white", fg="gray", font=("Times New Roman", 25), bd=0, width=13, height=1)
text_un.insert("1.0", f"texto predeterminado")
text_un.place(x=25, y=100)
ventana_principal.mainloop()

