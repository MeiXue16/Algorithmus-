#图形用户界面 (Graphical user interface)
import tkinter
import tkinter.messagebox

def main():
    flag= True

    #korrigeren den Text auf Label
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg =('red', 'hello, welcome to hier') if flag else ('yellow', 'soory, failed to login')
        label.config(text = msg, fg= color)

    #exit
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('Tip', 'Sure you want to quit?'):
            top.quit()

    #Erstellen von Top-Level-Fenstern
    top =tkinter.Tk()
    # Fenstergröße einstellen
    top.geometry('360x240')
    #titel
    top.title('small game')
    #label objekt erstellen
    label =tkinter.Label(top, font='Arial -32', text='hello, welcome to hier', fg='red')
    label.pack(expand=1)
    # einen Container für Buttons Erstellen
    panel =tkinter.Frame(top)
    ## Button-Objekt erstellen Festlegen,
    # welchem Container es hinzugefügt werden soll
    # Ereignis-Callback-Funktion über Befehlsparameter binden
    button1 = tkinter.Button(panel, text='korrigieren', command=change_label_text)
    button1.pack(side='left')
    button2 =tkinter.Button(panel,text='quit', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    #Hauptereignisschleife
    tkinter.mainloop()

if __name__== '__main__':
    main()

