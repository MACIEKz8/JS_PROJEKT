# Parkomat
## Opis zadania
- Parkomat przechowuje informacje o monetach/banknotach znajdujacych sie w nim (1, 2, 5, 10, 20, 50gr, 1, 2, 5, 10, 20, 50zł)
- Okno z polem tekstowym na numerrejestracyjny pojazdu, aktualng data (rok, miesiac, dzien, godzina, minuta), data wyjazdu z parkingu (rok, miesigc, dzieh, godzina, minuta), przyciskami pozwalajgcymi na wrzucanie monet (prosze umiescic pole pozwalajace wpisać liczbe wrzucanych monet), oraz przyciskiem “Zatwierdź’.
- Program powinien zawierac pole pozwalajace na przestawienie aktualnego czasu.
- Zasady strefy parkowania:
    - Strefa platnego parkowania obowigzuje w godzinach od 8 do 20 od poniedziatku do piatku.
    - Pierwsza godzina ptatna 2zł.
    - Druga godzina platna 4zł.
    - Trzecia i kolejne godziny ptatne po 5zł.
    - Czas wychodzacy poza obowiazywanie platnego parkowania przechodzi na kolejny dzien
        - Wykupienie godziny parkowania o 19:20 w pigtek pozwala na parkowanie do 8:20 w poniedziatek (koniec 0 20:20, wychodzi 20 minut poza ptatne parkowanie, przechodzi na kolejny ptatny dzien).
- Po kazdym wrzuceniu monety termin wyjazdu aktualizuje sie zgodnie z cala wrzuconą kwota.
- Jesli wrzucone zostato mniej pieniedzy niz potrzeba na optacenie petnej godziny, to optacana jest niepetna godzina:
    - Wrzucenie 1zt pozwala na parkowanie 30 minut,
    - Wrzucenie 5zt pozwala na parkowanie 1 godzine i 45 minut (2zt na optacenie pierwszej godziny, zostato 3z!, a potrzeba 4z! na oplacenie kolejnej, co daje 3/4 godziny: 45 minut).
- Po wcisnieciu przycisku “Zatwierdz” wyswietlane jest okno z potwierdzeniem optacenia parkingu: numerrejestracyjny pojazdu, czas zakupui termin wyjazdu.
- Numer rejestracyjny moze skladaé sie tylko z wielkich liter od A do Z i cyfr.
- W automacie miesci sie dowolna liczba banknotoéw (10, 20, 50zt) i po 200 monet kazdego rodzaju. Préba wrzucenia monety ponadlimit powoduje wyswietlenie informacji o przepetnieniu parkomatu i prosbe o wrzucenie innego nominatu.

## Testy
1. Ustaw niepoprawna godzine. Oczekiwany komunikat o btedzie. Ustawié godzine na 12:34.
2. Wrzucić 2zt, oczekiwany termin wyjazdu godzine po aktualnym czasie. Dorzuc 4zt, oczekiwany termin wyjazdu dwie godziny po aktualnym czasie. Dorzué 5zł, oczekiwany termin wyjazdu trzy godziny po aktualnym czasie. Dorzué kolejne 5zł, oczekiwany termin wyjazdu cztery godziny po aktualnym czasie.
3. Wrzucic tyle pieniedzy, aby termin wyjazdu przeszedt na kolejny dzien, Zgodnie z zasadami-- wrzucic tyle monet aby termin wyjazdu byt po godzinie 19:00, dorzuci¢é monete 5zt,
4. Wrzucic tyle pieniedzy, aby termin wyjazdu przeszedt na kolejny tydzien, zgodnie z zasadami- wrzucic tyle monet aby termin wyjazdu byt w piatek po godzinie 19:00,a potem dorzucić monete 5zł,
5. Wrzucić 1zt, oczekiwany termin wyjazdu pot godziny po aktualnym czasie,
6. Wrzucić 200 monet 1gr, oczekiwany termin wyjazdu godzine po aktualnym czasie.
7. Wrzucić 201 monet 1gr, oczekiwana informacja 0 przepetnieniu parkomatu.
8. Wciśniecie “Zatwierdz” bez wrzucenia monet-- oczekiwanainformacja o bledzie.
9. Wciśniecie “Zatwierdz” bez wpisania numeru rejestracyjnego -- oczekiwana informacja o bledzie. Wcisniecie “Zatwierdz” po wpisaniu niepoprawnego numeru rejestracyjnego -- oczekiwana informacja o bledzie.