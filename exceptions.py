class Error(Exception):
    """klasa bazowa dla wyjątków"""
    pass


class PrzepelnienieDrobnych(Error):
    message = "Parkomat przepelniony! Maksymalna ilość wrzuconych monet to 200."


class RejestracjaMaleLitery(Error):
    message = "Rejestracja moze skladac sie jedynie z duzych liter.\nWprowadz nr rejetracji samochodu jeszcze raz!"


class NieWprowadzonoNumeruRejestracyjnego(Error):
    message = "Wprowadź numer rejestracyjny!"


class NieWrzuconoMonet(Error):
    message = "Nie wrzucono żadnej monety!"

class NiepoprawnyCzas(Error):
    message = "Podano niepoprawną godzinę!"