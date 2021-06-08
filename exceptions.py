class Error(Exception):
    """klasa bazowa dla wyjątków"""
    pass


class PrzepelnienieDrobnych(Error):
    """Klasa wyjątku dla przepełnienia ilości drobnych w parkomacie"""
    message = "Parkomat przepelniony! Maksymalna ilość wrzuconych monet to 200."


class RejestracjaMaleLitery(Error):
    """Klasa wyjątku odpowiedzialna za niepoprawny numer rejestracyjny"""
    message = "Rejestracja moze skladac sie jedynie z duzych liter.\nWprowadz nr rejetracji samochodu jeszcze raz!"


class NieWprowadzonoNumeruRejestracyjnego(Error):
    """Klasa wyjątku odpowiedzialna za brak wprowadzonego numeru rejestracyjnego"""
    message = "Wprowadź numer rejestracyjny!"


class NieWrzuconoMonet(Error):
    """Klasa wyjątku odpowiedzialna za brak wrzuconej monety"""
    message = "Nie wrzucono żadnej monety!"

class NiepoprawnyCzas(Error):
    """Klasa odpowiedzialna za wyjątek podania niepoprawnej godziny"""
    message = "Podano niepoprawną godzinę!"