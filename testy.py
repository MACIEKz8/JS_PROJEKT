import unittest
from backend import *
from exceptions import *
from UserInterface import *

class Test_parkomat(unittest.TestCase):
    def setUp(self):
        self.parkomat = Parkomat_czas(1)


    def test_oplacony_czas(self):
        """test sprawdzajacy czy po wrzuceniu 2zł będzie opłacona pierwsza godzina (3600 sekund),
        po dorzuceniu 4zł będzie opłacona druga godzina (7200 sekund) itd."""
        self.parkomat.dodajMonete(Moneta(2))
        self.assertEqual(3600, self.parkomat.oplaconyCzas())

        self.parkomat.dodajMonete(Moneta(2))
        self.parkomat.dodajMonete(Moneta(2))
        self.assertEqual(7200, self.parkomat.oplaconyCzas())

        self.parkomat.dodajMonete(Moneta(5))
        self.assertEqual(10800, self.parkomat.oplaconyCzas())

        self.parkomat.dodajMonete(Moneta(5))
        self.assertEqual(14400, self.parkomat.oplaconyCzas())



    def test_nastepny_dzien(self):
        """test sprawdzający czy po opłaceniu kolejnej godziny po 19 termin wyjazdu przejdzie na kolejny dzień"""
        while self.parkomat.aktualizujCzas().hour != 19:
            self.parkomat.dodajMonete(Moneta(2))
        self.parkomat.dodajMonete(Moneta(5))
        if(datetime.datetime.now().hour>20):
            self.assertEqual(self.parkomat.aktualizujCzas().day, int(datetime.datetime.now().day)+2)
        else:
            self.assertEqual(self.parkomat.aktualizujCzas().day, int(datetime.datetime.now().day) + 1)


    def test_nastepny_tydzien(self):
        """test sprawdzający czy po opłaceniu kolejnej godziny po 19 w piątek termin wyjazdu przejdzie na kolejny tydzień"""
        while self.parkomat.aktualizujCzas().weekday() != 5:
            self.parkomat.dodajMonete(Moneta(5))
            if self.parkomat.aktualizujCzas().weekday() == 0:
                break

        self.parkomat.dodajMonete(Moneta(5))
        self.assertEqual(self.parkomat.aktualizujCzas().weekday(), 0)


    def test_1_zl(self):
        """test sprawdzający czy po wrzuceniu 1zł opłacone będzie 30 minut czyli 1800 sekund"""
        self.parkomat.dodajMonete(Moneta(1))
        self.assertEqual(1800, self.parkomat.oplaconyCzas())
        print(parkomat.budget())


    def test_200_1gr(self):
        """test sprawdzający czy po wrzuceniu 200 monet 1 gr opłacona zostanie jedna godzina (3600 sekund)"""
        i = 0
        while i < 200:
            self.parkomat.dodajMonete(Moneta(0.01))
            i+=1
        self.assertEqual(3600, int(self.parkomat.oplaconyCzas()))


    def test_201_1gr(self):
        """test sprawdzający czy po wrzuceniu 201 monet 1 gr wyskoczy błąd"""
        self.assertRaises(PrzepelnienieDrobnych, self.parkomat.dodajMonete, Moneta(0.01))
