import datetime
from datetime import timedelta
from tkinter import messagebox
import exceptions as e


class Moneta():
    """Klasa przechowująca monety akceptowane przez parkomat
        lista nominal zawiera dopuszczalne nominały
        lista drobne zawiera drobne pieniądze czyli te w monetach
    """
    nominal = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50]
    drobne = [x for x in nominal if x <= 5]

    def __init__(self, wartosc):
        if wartosc in self.nominal:
            self.wartosc = wartosc
            self.listaMonet = []
            self.licznikMonet = []
        else:
            raise AttributeError(f'"{wartosc}" nie jest akceptowanym nominałem')
    def get_wartosc(self):
        """Funkcja zwraca wartosc danej monety"""
        return self.wartosc
    def get_nominal(self):
        """Funkcja zwraca liste dostepnych nominałów"""
        return self.nominal
    def get_drobne(self):
        """Funkcja zwraac listę drobnych"""
        return self.drobne

class Parkomat_pieniadze(Moneta):
    """Klasa zajmuje obsługą pieniędzy w parkomacie. Dziedziczy po klasie Moneta"""
    def __init__(self, wartosc):
        super().__init__(wartosc)
        self.listaMonet=[]
        self.licznikMonet = []

    def dodajMonete(self, moneta, ile=1):
        """Funckcja umożliwia wrzucenie monety do listy monet"""
        try:
            if len(self.licznikMonet) > 199:
                raise e.PrzepelnienieDrobnych
            if isinstance(moneta, Moneta):
                for i in range(ile):
                    if len(self.licznikMonet) > 199:
                        raise e.PrzepelnienieDrobnych
                    self.listaMonet.append(moneta)
                    if (moneta.get_wartosc() in self.get_drobne()):
                        self.licznikMonet.append(moneta)
            else:
                print("Przesłany obiekt nie jest monetą")
        except (e.PrzepelnienieDrobnych):
            messagebox.showwarning("Zbyt dużo monet. Maksymalnie można wrzucić 200 monet", e.PrzepelnienieDrobnych.message)

    def budget(self):
        """Funkcja zwraca aktualnie wrzuconą kwotę"""
        return sum([moneta.get_wartosc() for moneta in self.listaMonet])

    def oplaconyCzas(self):
        """Funkcja konwertuje wrzucone pieniądze na ilość sekund parkowania"""
        if(self.budget() <= 2):
            return self.budget()*1800
        elif(self.budget()>2 and self.budget() <= 6):
            return 3600 + (self.budget()-2)*900
        else:
            return 7200 + (self.budget()-6)*720


class Parkomat_czas(Parkomat_pieniadze):
    """Klasa zajmuje się zarządzaniem opłaconym czasem. Dziedziczy po klasie Parkomat_pieniadze"""
    def __init__(self, wartosc):
        super().__init__(wartosc)
        self.wyjazd = datetime.datetime.now()
        self.teraz = datetime.datetime.now()

    def ustaw_rano(self, data):
        """Funkcja ustawia czas na godzinę 8 rano"""
        while True:
            data = data + timedelta(seconds=1)
            if data.hour == 8:
                return data

    def ustaw_poniedzialek(self, data):
        """Funkcja ustawia dzień tygodnia na poniedziałek"""
        while True:
            data = data + timedelta(days=1)
            if data.weekday() == 0:
                return data
    def aktualizujCzas(self):
        """Funkcja aktualizuje czas wyjazdu zgodnie z zapłaconą kwotą"""
        i = 0
        czas_wyjazdu = self.wyjazd
        while True:
            if i == self.oplaconyCzas():
                break
            if (czas_wyjazdu.hour < 8 or czas_wyjazdu.hour >= 20):
                czas_wyjazdu = self.ustaw_rano(czas_wyjazdu)
            if (czas_wyjazdu.weekday() > 4):
                czas_wyjazdu = self.ustaw_rano(czas_wyjazdu)
                if (czas_wyjazdu.weekday() > 4):
                    czas_wyjazdu = self.ustaw_poniedzialek(czas_wyjazdu)
                    czas_wyjazdu = czas_wyjazdu + timedelta(seconds=1)
                else:
                    czas_wyjazdu = czas_wyjazdu + timedelta(seconds=1)
                    i += 1
            else:
                czas_wyjazdu = czas_wyjazdu + timedelta(seconds=1)
                i += 1
        return czas_wyjazdu
    def nowy_czas(self, data):
        """Funkcja zwraca czas z teraz"""
        self.teraz = data
        return data

def czasFormat(data):
    """Funckja służy do ustawiania daty i godziny w odpowiednim formacie"""
    pom = (str(data)).split(" ")
    czas = pom[0]
    pom = pom[1].split(":")
    czas = czas + " " + pom[0] + ":" + pom[1]
    return czas
parkomat = Parkomat_czas(1)
