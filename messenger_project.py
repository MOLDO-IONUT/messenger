from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import sqlite3
import socket
import threading
def baza():
    conn = sqlite3.connect('bazaproiect.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS date_utilizatori(nume text primary key, prenume text not null,universitatea text not null, facultatea text not null, domiciliu text not null, varsta integer not null,gen not null,culoare text not null, Email text not null, parola text not null)")
    conn.commit()
    conn.close()
baza()
def inregistrare():
    if nume_entry.get() =='' or prenume_entry.get() =='' or universitatea_entry.get() =='' or facultatea_entry.get() =='' or  domiciliu_entry.get() =='' or varsta_entry.get() =='' or alegere_gen.get() =='' or alegere_culoare.get() =='' or email_entry.get() =='' or name_entry_parola.get() =='':
        mesaj_inregistrare.set("Campuri goale")
    else:
        mesaj_inregistrare.set("")
        baza()
        conn = sqlite3.connect('bazaproiect.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO date_utilizatori VALUES (:nume_entry, :prenume_entry, :universitatea_entry, :facultatea_entry, :domiciliu_entry, :varsta_entry, :alegere_gen, :alegere_culoare, :email_entry, :name_entry_parola)",
                        {
                            'nume_entry':nume_entry.get(),
                            'prenume_entry': prenume_entry.get(),
                            'universitatea_entry': universitatea_entry.get(),
                            'facultatea_entry': facultatea_entry.get(),
                            'domiciliu_entry': domiciliu_entry.get(),
                            'varsta_entry': varsta_entry.get(),
                            'alegere_gen': alegere_gen.get(),
                            'alegere_culoare': alegere_culoare.get(),
                            'email_entry': email_entry.get(),
                            'name_entry_parola': name_entry_parola.get()
                        })
        messagebox.showinfo(title="Database", message="Utilizator adaugat")
        conn.commit()
        conn.close()
    nume_entry.delete(0, END)
    prenume_entry.delete(0, END)
    universitatea_entry.delete(0, END)
    facultatea_entry.delete(0, END)
    domiciliu_entry.delete(0, END)
    varsta_entry.delete(0, END)
    alegere_gen.delete(0, END)
    email_entry.delete(0, END)
    name_entry_parola.delete(0, END)
fereastra_meniu = Tk()
fereastra_meniu.iconphoto(False, PhotoImage(file='bbbb.png'))
mesaj_inregistrare=StringVar()
fereastra_meniu.title('Student Chat')
bg = PhotoImage(file=r"Untitled design.png")
label1 = Label(fereastra_meniu, image=bg)
label1.place(x=0, y=0)
#MESAJ BUN VENIT
def prezentare():
    Prezentare = Label(fereastra_meniu, text='Bun venit pe platforma Student Chat', bg='yellow', height=2,font=('arial', 14, 'bold'))
    Prezentare.place(x=870, y=100) 
#CREEAZA CONT
def creeaza_cont():
    fereastra_creeaza_cont = Toplevel(fereastra_meniu)
    fereastra_creeaza_cont.title('Creeaza cont')
    fereastra_creeaza_cont.iconphoto(False, tk.PhotoImage(file='bbbb.png'))
    label = Label(fereastra_creeaza_cont, background='#00425F')
    label.place(x=0, y=0, width=400, height=400)
    
    nume_titlu = Label(fereastra_creeaza_cont, text='Nume', font=('arial', 14, 'bold'),fg="white", bg="#00425F")
    nume_titlu.place(x=120, y=55)
    global nume_entry
    nume_entry = StringVar()
    nume_entry = Entry(fereastra_creeaza_cont, textvariable=nume_entry)
    nume_entry.place(x=180, y=60, width=200)

    prenume_titlu = Label(fereastra_creeaza_cont, text='Preume', font=('arial', 14, 'bold'),fg="white", bg="#00425F")
    prenume_titlu.place(x=100, y=80)
    global prenume_entry
    prenume_entry = StringVar()
    prenume_entry = Entry(fereastra_creeaza_cont, textvariable=prenume_entry)
    prenume_entry.place(x=180, y=84,width=200)
    
    universitatea_titlu = Label(fereastra_creeaza_cont, text='Universitatea', font=('arial', 14, 'bold'),fg="white", bg="#00425F")
    universitatea_titlu.place(x=50, y=104)
    global universitatea_entry
    universitatea_entry = StringVar()
    universitatea_entry = Entry(fereastra_creeaza_cont, textvariable=universitatea_entry)
    universitatea_entry.place(x=180, y=108,width=200)

    facultatea_titlu = Label(fereastra_creeaza_cont, text='Facultatea', font=('arial', 14, 'bold'),fg="white", bg="#00425F")
    facultatea_titlu.place(x=75, y=130)
    global facultatea_entry
    facultatea_entry = StringVar()
    facultatea_entry = Entry(fereastra_creeaza_cont, textvariable=facultatea_entry)
    facultatea_entry.place(x=180, y=132,width=200)

    domiciliu_titlu = Label(fereastra_creeaza_cont, text='Domiciliu', font=('arial', 14, 'bold'),fg="white", bg="#00425F")
    domiciliu_titlu.place(x=85, y=153)
    global domiciliu_entry
    domiciliu_entry = StringVar()
    domiciliu_entry = Entry(fereastra_creeaza_cont, textvariable=domiciliu_entry)
    domiciliu_entry.place(x=180, y=156,width=200)

    varsta_titlu = Label(fereastra_creeaza_cont, text='Varsta', font=('arial', 14, 'bold'),fg="white", bg="#00425F")
    varsta_titlu.place(x=110, y=178)
    global varsta_entry
    varsta_entry = StringVar()
    varsta_entry = Entry(fereastra_creeaza_cont, textvariable=varsta_entry)
    varsta_entry.place(x=180, y=180,width=200)

    gen_titlu = Label(fereastra_creeaza_cont, text='Gen', font=('arial', 14, 'bold'),fg="white", bg="#00425F")
    gen_titlu.place(x=132, y=202)
    global alegere_gen
    alegere_gen = ttk.Combobox(fereastra_creeaza_cont, text='Gen', textvariable="gen", state="readonly")
    alegere_gen['values'] = ("Masculin", "Feminin")
    alegere_gen.place(x=180, y=204,width=200)

    culoare_titlu = Label(fereastra_creeaza_cont, text='Culoarea preferata', font=('arial', 14, 'bold'),fg="white", bg="#00425F")
    culoare_titlu.place(x=0, y=226)
    global alegere_culoare
    alegere_culoare = ttk.Combobox(fereastra_creeaza_cont, textvariable="culoare", state="readonly")
    alegere_culoare['values'] = ("Rosu", "Orange", "Galben", "Verde", "Albastru", "Indigo", "Violet")
    alegere_culoare.place(x=180, y=228,width=200)
    
    email_titlu = Label(fereastra_creeaza_cont, text='E-mail', font=('arial', 14, 'bold'),fg="white", bg="#00425F")
    email_titlu.place(x=112, y=250)
    global email_entry
    email_entry = StringVar()
    email_entry = Entry(fereastra_creeaza_cont, textvariable=email_entry)
    email_entry.place(x=180, y=252,width=200)

    parola_titlu = Label(fereastra_creeaza_cont, text='Parola', font=('arial', 14, 'bold'),fg="white", bg="#00425F")
    parola_titlu.place(x=110, y=274)
    global name_entry_parola
    name_entry_parola = StringVar()
    name_entry_parola = Entry(fereastra_creeaza_cont, textvariable=name_entry_parola, show="*")
    name_entry_parola.place(x=180, y=276,width=200)
    
    inregistare_Buton = Button(fereastra_creeaza_cont, text='Inregistrare', command=inregistrare, bg='yellow', font=('arial', 14, 'bold'))
    inregistare_Buton.place(x=220, y=324, width=125, height=30)
    meniu_principal= Button(fereastra_creeaza_cont, text='Meniu',fg='white',bg='green',bd=2, font=('arial', 14, 'bold'),command=lambda: [fereastra_creeaza_cont.destroy(),fereastra_meniu.state('zoomed')])
    meniu_principal.place(x=240, y=12)
    campuri_libere = Label(fereastra_creeaza_cont, text='',textvariable=mesaj_inregistrare, font=('arial', 10, 'italic'),fg="white", bg="#00425F")
    campuri_libere.place(x=240, y=300)
    fereastra_meniu.state('icon')
    fereastra_creeaza_cont.geometry('400x400+790+290')
    fereastra_creeaza_cont.resizable(False, False)
    fereastra_creeaza_cont.mainloop()
#AUTENTIFICARE 
s = socket.socket()
def trimite1():
    baza()
    fereastra_autentificare
    conn = sqlite3.connect('bazaproiect.db')
    cursor = conn.cursor()
    global chatTT
    chatTT = Text(fereastra5, font=("Serif", 12))
    chatTT.place(x=10, y=10, width=480, height=445)
    x=cursor.execute("SELECT nume, prenume FROM date_utilizatori WHERE Email=? and parola=?",(email_conectare_entry.get(), parola_conectare_entry.get(),)).fetchone()
    s.connect(('localhost',1234))
    def primeste():
        try:
            while True:
                mesaj = s.recv(1024).decode()
                chatTT.insert(END, mesaj)     
        except:
            print("Error") 
    def trimite():
            mesaj = text_text.get()
            s.send(f'{x}: {mesaj} \n'.encode())
            text_text.delete(0, END)
    trimite_button=Button(fereastra5, text='Trimite',command=trimite,bg='yellow', relief='ridge',height=2,bd=2,font=('arial', 8, 'bold'))
    trimite_button.place(x=440, y=458)
    t2 = threading.Thread(target=primeste)
    t2.start()   
    conn.commit()
    conn.close()
    scrollbar = Scrollbar(fereastra5, command=chatTT.yview)
    scrollbar.place(x=480,y=10, height=445, width=20)
    chatTT['yscrollcommand'] = scrollbar.set
def chat():
    global fereastra5
    fereastra5 = Toplevel(fereastra_meniu)
    fereastra5.iconphoto(False, tk.PhotoImage(file='bbbb.png'))
    fereastra5.title("Chat")
    global text_text
    text_text = Entry(fereastra5)
    text_text.place(x=10, y=458, width=430, height=40)
    trimite1()
    fereastra5.geometry('500x500+790+290')
    fereastra5.resizable(False, False)
global mesaj_conectare
mesaj_conectare=StringVar()
def conectare():
    if email_conectare_entry.get()=='' or parola_conectare_entry.get()=='':
        mesaj_conectare.set("Campuri goale")
    else:
        mesaj_conectare.set("")      
    conn = sqlite3.connect('bazaproiect.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM date_utilizatori WHERE Email = ? AND parola = ?""", (email_conectare_entry.get(), parola_conectare_entry.get(),))
    if cursor.fetchone():
        messagebox.showinfo(title="Database", message="Utilizator existent")
        chat() 
    else:
        messagebox.showerror(title="Eroare", message="Utilizator inexistent")         
    conn.commit()
    conn.close()
def autentificare():
    global fereastra_autentificare
    fereastra_autentificare = Toplevel(fereastra_meniu)
    fereastra_autentificare.title('Autentificare')
    fereastra_autentificare.iconphoto(False, tk.PhotoImage(file='bbbb.png'))
    label2 = Label(fereastra_autentificare, background='#00425F')
    label2.place(x=0, y=0, width=300, height=200)
    
    email_conectare_titlu = Label(fereastra_autentificare, text='E-mail', font=('arial', 14, 'bold'),fg="white", bg="#00425F")
    email_conectare_titlu.place(x=2, y=56)
    global email_conectare_entry
    email_conectare_entry = StringVar()
    email_conectare_entry = Entry(fereastra_autentificare, textvariable=email_conectare_entry)
    email_conectare_entry.place(x=68, y=60,width=220)

    parola_conectare_titlu = Label(fereastra_autentificare, text='Parola', font=('arial', 14, 'bold'),fg="white", bg="#00425F")
    parola_conectare_titlu.place(x=2, y=90)
    global parola_conectare_entry
    parola_conectare_entry = StringVar()
    parola_conectare_entry = Entry(fereastra_autentificare, textvariable=parola_conectare_entry, show="*")
    parola_conectare_entry.place(x=68, y=94,width=220)
    
    campuri_libere = Label(fereastra_autentificare, text='',textvariable=mesaj_conectare, font=('arial', 10, 'italic'),fg="white", bg="#00425F")
    campuri_libere.place(x=140, y=116 )
    conectare_Buton = Button(fereastra_autentificare, text='Conectare',bg='yellow', font=('arial', 14, 'bold'), borderwidth=3, command=conectare)
    conectare_Buton.place(x=120, y=136, width=125, height=30)
    meniu_principal = Button(fereastra_autentificare, text='Meniu', font=('arial', 14, 'bold'),fg='white',bg='green',bd=2,command=lambda: [fereastra_autentificare.destroy(),fereastra_meniu.state('zoomed')])
    meniu_principal.place(x=146, y=14)
    fereastra_meniu.state('icon')
    fereastra_autentificare.geometry('300x200+830+320')
    fereastra_autentificare.resizable(False, False)
#AM UITAT PAROLA
mesaj_reset=StringVar()                
def resetare_parola():
    conn = sqlite3.connect('bazaproiect.db')
    cursor = conn.cursor()
    if  email_am_uitat_parola_entry.get() =='' or  alegere_culoare_am_uitat_parola_entry.get() =='' or varsta_am_uitat_parola_entry.get() =='' or parola_noua_entry.get() =='':
        mesaj_reset.set("Campuri goale")
    else:
        mesaj_reset.set("") 
    cursor.execute("""SELECT Email AND culoare AND varsta FROM date_utilizatori WHERE Email=? AND culoare=? AND varsta=?""", (email_am_uitat_parola_entry.get(),alegere_culoare_am_uitat_parola_entry.get(),varsta_am_uitat_parola_entry.get(),))
    if cursor.fetchall():
        cursor.execute("""UPDATE date_utilizatori SET parola=? WHERE email=? AND culoare=? AND varsta=?""",(parola_noua_entry.get(), email_am_uitat_parola_entry.get(), alegere_culoare_am_uitat_parola_entry.get(), varsta_am_uitat_parola_entry.get()))
        messagebox.showinfo(title="Baza de date", message="Parola a fost actualizata cu succes")
    else:
        messagebox.showerror(title="Baza de date", message="Date incorecte")   
    conn.commit()
    conn.close()
    email_am_uitat_parola_entry.delete(0, END)
    alegere_culoare_am_uitat_parola_entry.delete(0, END)
    varsta_am_uitat_parola_entry.delete(0, END)
    parola_noua_entry.delete(0, END)
def am_uitat_parola():
    global fereastra_am_uitat_parola
    fereastra_am_uitat_parola = Toplevel(fereastra_meniu)
    fereastra_am_uitat_parola.title('Am uitat parola')
    fereastra_am_uitat_parola.iconphoto(False, tk.PhotoImage(file='bbbb.png'))
    label3 = Label(fereastra_am_uitat_parola, background='#00425F')
    label3.place(x=0, y=0, width=450, height=300)

    email_am_uitat_parola_titlu = Label(fereastra_am_uitat_parola, text='E-mail', font=('arial', 14, 'bold'),fg="white", bg="#00425F")
    email_am_uitat_parola_titlu.place(x=135, y=55)
    global email_am_uitat_parola_entry
    email_am_uitat_parola_entry = StringVar()
    email_am_uitat_parola_entry = Entry(fereastra_am_uitat_parola, textvariable=email_am_uitat_parola_entry)
    email_am_uitat_parola_entry.place(x=200, y=60,width=200)

    alegere_culoare_titlu = Label(fereastra_am_uitat_parola, text='Culoarea preferata', font=('arial', 14, 'bold'),fg="white", bg="#00425F")
    alegere_culoare_titlu.place(x=20, y=90)
    global alegere_culoare_am_uitat_parola_entry
    alegere_culoare_am_uitat_parola_entry = ttk.Combobox(fereastra_am_uitat_parola, textvariable="culoarea", state="readonly")
    alegere_culoare_am_uitat_parola_entry['values'] = ("Rosu", "Orange", "Galben", "Verde", "Albastru", "Indigo", "Violet")
    alegere_culoare_am_uitat_parola_entry.place(x=200, y=94,width=200)

    varta_am_uitat_parola_titlu = Label(fereastra_am_uitat_parola, text='Varsta', font=('arial', 14, 'bold'),fg="white", bg="#00425F")
    varta_am_uitat_parola_titlu.place(x=132, y=124)
    global varsta_am_uitat_parola_entry
    varsta_am_uitat_parola_entry = StringVar()
    varsta_am_uitat_parola_entry = Entry(fereastra_am_uitat_parola, textvariable=varsta_am_uitat_parola_entry)
    varsta_am_uitat_parola_entry.place(x=200, y=128,width=200)

    parola_noua_titlu = Label(fereastra_am_uitat_parola, text='Parola noua', font=('arial', 14, 'bold'),fg="white", bg="#00425F")
    parola_noua_titlu.place(x=80, y=160)
    global parola_noua_entry
    parola_noua_entry = StringVar()
    parola_noua_entry = Entry(fereastra_am_uitat_parola, textvariable=parola_noua_entry, show="*")
    parola_noua_entry.place(x=200, y=164,width=200)

    campuri_libere = Label(fereastra_am_uitat_parola, text='',textvariable=mesaj_reset, font=('arial', 10, 'italic'),fg="white", bg="#00425F")
    campuri_libere.place(x=258, y=186 )
    ok_button = Button(fereastra_am_uitat_parola, text='Ok', font=('arial', 14, 'bold'),bg='yellow',bd=4, command=resetare_parola)
    ok_button.place(x=280, y=210)
    meniu_principal = Button(fereastra_am_uitat_parola, text='Meniu',fg='white',bg='green',bd=4, font=('arial', 14, 'bold'), command=lambda: [fereastra_am_uitat_parola.destroy(), fereastra_meniu.state('zoomed')])
    meniu_principal.place(x=260, y=10 )
    # functie de slavare parola noua
    fereastra_meniu.state('icon')
    fereastra_am_uitat_parola.geometry('450x300+790+290')
    fereastra_am_uitat_parola.resizable(False, False)
#MENIU PRINCIPAL
prezentare()
creeaza_cont_Buton = Button(fereastra_meniu, text='Creeaza cont', command=creeaza_cont, bg='yellow', height=2,bd=10,relief='ridge',font=('arial', 17, 'bold'))
creeaza_cont_Buton.place(x=720, y=400)
autentificare_Buton = Button(fereastra_meniu, text='Autentificare', command=autentificare, bg='yellow', height=2,bd=10,relief='ridge',font=('arial', 17, 'bold'))
autentificare_Buton.place(x=1200, y=400)
am_uitat_parola_Buton = Button(fereastra_meniu, text='Am uitat parola',activebackground='orange', command=am_uitat_parola, bg='yellow', relief='ridge',height=2,bd=10,font=('arial', 17, 'bold'))
am_uitat_parola_Buton.place(x=960, y=400)
iesire_buton = Button(fereastra_meniu, text='Iesire', command=fereastra_meniu.destroy, bg='orange', height=2,width=10,bd=3,font=('arial', 18, 'bold'),relief='ridge')
iesire_buton.place(x=990, y=540)
fereastra_meniu.geometry('1920x1080+0+0')
fereastra_meniu.resizable(False, False)
fereastra_meniu.mainloop()
