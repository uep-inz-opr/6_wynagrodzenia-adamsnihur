class Pracownik:
    def __init__ (self, imie_pracownika, wynagrodzenie_brutto):
      self.imie_pracownika = imie_pracownika
      self.wynagrodzenie_brutto = wynagrodzenie_brutto

    def wynik(self, imie_pracownika, wynagrodzenie_brutto):
      a = int(wynagrodzenie_brutto)
      b = a
      c = round((0.0976*a) + (0.015*a) + (0.0245*a), 2)
      d = b - c
      e = round(d * 0.09, 2)
      f = round(d * 0.0775, 2)
      g = 111.25
      h = round(a - g - c, 0)
      i = round(h * 0.18 - 46.33, 2)
      j = round(i - f, 0)
      k = round(a - c - e - j, 2)
      l = round((0.0976 * a) + (0.065 * a) + (0.0193 * a) + (0.0245 * a) + (0.001 *a), 2)
      ł = round(a + l, 2)
      
      return print (imie_pracownika, (f"{k:.2f}"), (f"{round(ł-a,2):.2f}"), (f"{ł:.2f}"))


    def koszt_pracodawcy(self, wynagrodzenie_brutto) -> float:
      a = int(wynagrodzenie_brutto)
      l = round((0.0976 * a) + (0.065 * a) + (0.0193 * a) + (0.0245 * a) + (0.001 *a), 2)
      ł = round(a + l, 2)

      return ł

  

liczba_pracownikow = int(input())
pracownicy = []

for i in range(liczba_pracownikow):
    temp = input().strip()
    temp = temp.split(' ')
    pracownicy.append(Pracownik(temp[0],temp[1]))

laczny_koszt = 0

for i in range(liczba_pracownikow):
    pracownicy[i].wynik(pracownicy[i].imie_pracownika, pracownicy[i].wynagrodzenie_brutto)

for x in range(len(pracownicy)):
    laczny_koszt += pracownicy[x].koszt_pracodawcy(pracownicy[x].wynagrodzenie_brutto)

print(f"{round(laczny_koszt, 2):.2f}")
