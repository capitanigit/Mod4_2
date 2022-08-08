#Mod 4 zad 2
import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="calc_logfile.log")

def dodawanie(x, y):
    logging.info("Dodaję %s i %s" % (x, y))
    return x + y
def odejmowanie(x, y):
    logging.info("Odejmuję %s i %s" % (x, y))
    return x - y
def iloczyn(x, y):
    logging.info("Mnożę %s i %s" % (x, y))
    return x * y
def iloraz(x, y):
    logging.info("Dzielę %s i %s" % (x, y))
    return x / y

print("Wybierz działanie: 1. Dodawanie, 2. Odejmowanie, 3. Mnożenie, 4. Dzielenie")
while True:
    act = input("Wybierz działanie 1/2/3/4): ")
    if act in ('1', '2', '3', '4'):
        num1 = float(input("Wpisz pierwszą liczbę: "))
        num2 = float(input("Wpisz drugą liczbę: "))
        if act == '1':
            print(f"Dodawanie", num1, "i", num2, "=", dodawanie(num1, num2))
        elif act == '2':
            print(f"Odejmowanie", num1, "-", num2, "=", odejmowanie(num1, num2))
        elif act == '3':
            print(f"Mnożenie", num1, "*", num2, "=", iloczyn(num1, num2))
        elif act == '4':
            print(f"Dzielenie", num1, "/", num2, "=", iloraz(num1, num2))
        act_next = input("Czy chcesz wykonać kolejne obliczenia ? (tak/nie): ")
        if act_next == "nie":
          break
    else:
        print("zły wybór ;]")