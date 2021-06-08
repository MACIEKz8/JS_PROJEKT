from tkinter import *
from tkinter import messagebox
import backend as p
import datetime
import exceptions as e
color = "#cfcaca"
class interfejs:
    """Klasa bazowa dla interfejsu użytkownika"""
    def wyswietlCzas(tekst, przycisk):
        """Funkcja aktualizuje czas po kliknięciu przycisku"""
        przycisk.config(text=tekst)

    def wyswietlBudget(tekst, przycisk):
        """Funkcja aktualizuje budżet wrzuceniu monety (kliknięciu przycisku danej monety)"""
        przycisk.config(text=tekst)
    def ZatwierdzFun(self):
        """Funkcja odpowiedzialna za przycisk Zatwierdź.
        W przypadku poprawnego wpisania numeru rejestracyjnego oraz wrzuceniu odpowiedniej ilości monet zwraca bilet parkingowy (messageBox)"""
        try:
            if p.parkomat.budget() == 0:
                raise e.NieWrzuconoMonet
            if numer_rejestracyjny.get() == " ":
                raise e.NieWprowadzonoNumeruRejestracyjnego
            if not numer_rejestracyjny.get().isupper():
                raise e.RejestracjaMaleLitery
            messagebox.showinfo("BILET PARKINGOWY",
                                "Numer rejestracyjny: " + numer_rejestracyjny.get() + "\nAktualna data: " + p.czasFormat(
                                    datetime.datetime.now()) + "\nData planowanego wyjazdu: " + p.czasFormat(
                                    p.parkomat.aktualizujCzas()))
            exit(1)
        except(e.RejestracjaMaleLitery):
            messagebox.showerror("Rejestracja blad", e.RejestracjaMaleLitery.message)
        except(e.NieWprowadzonoNumeruRejestracyjnego):
            messagebox.showerror("Rejetracja blad", e.NieWprowadzonoNumeruRejestracyjnego.message)
        except(e.NieWrzuconoMonet):
            messagebox.showerror("Monety blad", e.NieWrzuconoMonet.message)

    def gui(self):
        """Funckja w której implementujemy wszelką zawartość graficzną"""
        rejestracja_podaj = Label(root, text="Podaj nr rejestracyjny pojazdu:", bg="#404040", foreground="#FFFFFF")
        rejestracja_podaj.grid(row=0, column=0, columnspan=3, pady=10)
        global numer_rejestracyjny
        numer_rejestracyjny = Entry(root, width=50, bg="#404040", foreground="#FFFFFF")
        numer_rejestracyjny.grid(row=1, column=0, columnspan=3, pady=10)
        numer_rejestracyjny.insert(1, ' ')

        dziesiec_zl = Button(root, text='10 zł', height=5, width=15, activebackground="#404040", bg=color,
                             command=lambda: [p.parkomat.dodajMonete(p.Moneta(10), int(ilosc_monet.get())), self.wyswietlBudget(p.parkomat.budget(), wrzucono), self.wyswietlCzas(p.czasFormat(p.parkomat.aktualizujCzas()), d4)])
        dziesiec_zl.grid(row=2, column = 0)
        dwadziescia_zl = Button(root, text='20 zł', height=5, width=15, activebackground="#404040", bg=color,
                                command=lambda: [p.parkomat.dodajMonete(p.Moneta(20), int(ilosc_monet.get())), self.wyswietlBudget(p.parkomat.budget(), wrzucono), self.wyswietlCzas(p.czasFormat(p.parkomat.aktualizujCzas()), d4)])
        dwadziescia_zl.grid(row=2, column=1)
        piecdziesiat_zl = Button(root, text='50 zł', height=5, width=15, activebackground="#404040", bg=color,
                                 command=lambda: [p.parkomat.dodajMonete(p.Moneta(50), int(ilosc_monet.get())), self.wyswietlBudget(p.parkomat.budget(), wrzucono), self.wyswietlCzas(p.czasFormat(p.parkomat.aktualizujCzas()), d4)])
        piecdziesiat_zl.grid(row=2, column=2)

        zlotowka = Button(root, text='1 zł', height=5, width=15, activebackground="#404040", bg=color,
                          command=lambda: [p.parkomat.dodajMonete(p.Moneta(1), int(ilosc_monet.get())), self.wyswietlBudget(p.parkomat.budget(), wrzucono), self.wyswietlCzas(p.czasFormat(p.parkomat.aktualizujCzas()), d4)])
        zlotowka.grid(row=3, column=0)
        dwa_zl = Button(root, text='2 zł', height=5, width=15, activebackground="#404040", bg=color,
                        command=lambda: [p.parkomat.dodajMonete(p.Moneta(2), int(ilosc_monet.get())), self.wyswietlBudget(p.parkomat.budget(), wrzucono), self.wyswietlCzas(p.czasFormat(p.parkomat.aktualizujCzas()), d4)])
        dwa_zl.grid(row=3, column=1)
        piec_zl = Button(root, text='5 zł', height=5, width=15, activebackground="#404040", bg=color,
                         command=lambda: [p.parkomat.dodajMonete(p.Moneta(5), int(ilosc_monet.get())), self.wyswietlBudget(p.parkomat.budget(), wrzucono), self.wyswietlCzas(p.czasFormat(p.parkomat.aktualizujCzas()), d4)])
        piec_zl.grid(row=3, column=2)

        dziesiec_gr = Button(root, text='0.10 zł', height=5, width=15, activebackground="#404040", bg=color,
                             command=lambda: [p.parkomat.dodajMonete(p.Moneta(0.10), int(ilosc_monet.get())), self.wyswietlBudget(p.parkomat.budget(), wrzucono), self.wyswietlCzas(p.czasFormat(p.parkomat.aktualizujCzas()), d4)])
        dziesiec_gr.grid(row=4, column=0)
        dwadziescia_gr = Button(root, text='0.20 zł', height=5, width=15, activebackground="#404040", bg=color,
                                command=lambda: [p.parkomat.dodajMonete(p.Moneta(0.20), int(ilosc_monet.get())), self.wyswietlBudget(p.parkomat.budget(), wrzucono), self.wyswietlCzas(p.czasFormat(p.parkomat.aktualizujCzas()), d4)])
        dwadziescia_gr.grid(row=4, column=1)
        piecdziesiat_gr = Button(root, text='0.50 zł', height=5, width=15, activebackground="#404040", bg=color,
                                 command=lambda: [p.parkomat.dodajMonete(p.Moneta(0.50), int(ilosc_monet.get())), self.wyswietlBudget(p.parkomat.budget(), wrzucono), self.wyswietlCzas(p.czasFormat(p.parkomat.aktualizujCzas()), d4)])
        piecdziesiat_gr.grid(row=4, column=2)

        grosz = Button(root, text='0.01 zł', height=5, width=15, activebackground="#404040", bg=color,
                       command=lambda: [p.parkomat.dodajMonete(p.Moneta(0.01), int(ilosc_monet.get())), self.wyswietlBudget(p.parkomat.budget(), wrzucono), self.wyswietlCzas(p.czasFormat(p.parkomat.aktualizujCzas()), d4)])
        grosz.grid(row=5, column = 0)
        dwa_grosze = Button(root, text='0.02 zł', height=5, width=15, activebackground="#404040", bg=color,
                            command=lambda: [p.parkomat.dodajMonete(p.Moneta(0.02), int(ilosc_monet.get())), self.wyswietlBudget(p.parkomat.budget(), wrzucono), self.wyswietlCzas(p.czasFormat(p.parkomat.aktualizujCzas()), d4)])
        dwa_grosze.grid(row=5, column=1)
        piec_groszy = Button(root, text='0.05 zł', height=5, width=15, activebackground="#404040", bg=color,
                             command=lambda: [p.parkomat.dodajMonete(p.Moneta(0.05), int(ilosc_monet.get())), self.wyswietlBudget(p.parkomat.budget(), wrzucono), self.wyswietlCzas(p.czasFormat(p.parkomat.aktualizujCzas()), d4)])
        piec_groszy.grid(row=5, column=2)


        zatwierdz = Button(root, text="Zatwierdź ", height=3, width=48, bg="#48fc38",
                    command=lambda: self.ZatwierdzFun(self))
        zatwierdz.grid(row=6, column=0, columnspan=3)

        ile_monet = Label(root, text="Ilość monet:", bg="#404040", foreground="#FFFFFF")
        ile_monet.grid(row=7, column=0, columnspan=2, pady=10)
        ilosc_monet = Entry(root, width=15, bg="#404040", foreground="#FFFFFF")
        ilosc_monet.insert(0, 1)
        ilosc_monet.grid(row=7, column=2, columnspan=2, pady=10)

        d1 = Label(root, text="Aktualna data: ", height=3, bg="#404040", foreground="#FFFFFF")
        d1.grid(row=8, column=0, columnspan = 2)
        d2 = Label(root, text=p.czasFormat(datetime.datetime.now()), bg="#404040", foreground="#FFFFFF")
        d2.grid(row=8, column=2)

        zmien_date= Button(root, text="Zmień aktualną datę", height=1, width=15, bg="#5e5d5d", command=lambda: self.wyswietlCzas(p.parkomat.nowy_czas(nowa_data.get()), d2))
        zmien_date.grid(row=9, column=0, columnspan=2)
        nowa_data = Entry(root, width=15, bg="#404040", foreground="#FFFFFF")
        nowa_data.insert(1, ' ')
        nowa_data.grid(row=9, column=2)


        d3 = Label(root, text="Przewidziany wyjazd", height=3, bg="#404040", foreground="#FFFFFF")
        d3.grid(row=10, column=0, columnspan = 2)
        d4 = Label(root, text=p.czasFormat(p.parkomat.aktualizujCzas()), bg="#404040",
                   foreground="#FFFFFF")
        d4.grid(row=10, column=2)

        wrzucono = Label(root, text="Wrzucono: ", height=3, bg="#404040", foreground="#FFFFFF")
        wrzucono.grid(row=11, column=0, columnspan=2)
        wrzucono = Label(root, text=p.parkomat.budget(), bg="#404040", foreground="#FFFFFF")
        wrzucono.grid(row=11, column=1, columnspan=2)
        zl = Label(root, text="zł", bg="#404040", foreground="#FFFFFF")
        zl.grid(row=11, column=2)

root = Tk()
root.configure(bg="#404040")
root.title("Parkomat")
projekt = interfejs
projekt.gui(interfejs)
root.mainloop()
