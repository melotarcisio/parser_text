from tkinter import *
from tkinter import ttk

from TextParser import TextParser

class TkUI:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Parser Text v1.0")
        self.tk.geometry("725x500")
        self.tk.resizable(0, 0)
        self.init()

    def init(self):
        frm = ttk.Frame(self.tk, padding=1).grid(row=1)
        Label(frm, width=9).grid(column=1, row=0)

        input = Text(frm, height=20, width=40)
        input.grid(column=0, row=0)
        input.insert(END, 'Entre com o texto aqui\nCaso queira parsear um arquivo pdf, sinalize' + \
                     ' com $<caminho_do_arquivo>$.\nExemplo:\t"$C:/Desktop/teste.pdf$"')
        output = Text(frm, height=20, width=40)
        output.grid(column=2, row=0)
        output.insert(END, "O resultado aparecerá aqui!")

        options = self.options()

        Label(frm,text="Buscar").grid(column=2, row=1)
        src = Text(frm, height=1, width=40)
        src.grid(column=2,row=2)
        Label(frm,text="Substituir").grid(column=2, row=3)
        sub = Text(frm, height=1, width=40)
        sub.grid(column=2,row=4)
        Label(frm,text="Separador").grid(column=2, row=5)
        sep = Text(frm, height=1, width=40)
        sep.grid(column=2,row=6)

        Button(self.tk, text=options[0], command= lambda: self.button_option(1, input.get("1.0", "end-1c"), output, src.get("1.0", "end-1c"), sub.get("1.0", "end-1c"), sep.get("1.0", "end-1c"))).grid(column=0,row=1)
        Button(self.tk, text=options[1], command=lambda: self.button_option(2, input.get("1.0", "end-1c"), output, src.get("1.0", "end-1c"), sub.get("1.0", "end-1c"), sep.get("1.0", "end-1c"))).grid(column=0, row=2)
        Button(self.tk, text=options[2], command= lambda: self.button_option(3, input.get("1.0", "end-1c"), output, src.get("1.0", "end-1c"), sub.get("1.0", "end-1c"), sep.get("1.0", "end-1c"))).grid(column=0,row=3)
        Button(self.tk, text=optins[3], command=lambda: self.button_option(4, input.get("1.0", "end-1c"), output, src.get("1.0", "end-1c"), sub.get("1.0", "end-1c"), sep.get("1.0", "end-1c"))).grid(column=0, row=4)
        Button(self.tk, text=options[4], command=lambda: self.button_option(5, input.get("1.0", "end-1c"), output, src.get("1.0", "end-1c"), sub.get("1.0", "end-1c"), sep.get("1.0", "end-1c"))).grid(column=0, row=5)

    def button_option(self, option, text_input, output, src, sub, sep):
        if text_input == "":
            pass
        else:
            text_parser = TextParser()
            output.delete('1.0', END)
            output_text = text_parser.run(option, text_input, src, sub, sep)
            output.insert(END, output_text)

    def options(self):
        return [
            'Apenas Texto',
            'Extrair números',
            'Substituir Texto',
            'Substituir Regex',
            'Buscar Regex'
        ]