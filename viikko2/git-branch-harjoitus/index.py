# tehdään alussa importit
from tulo import tulo
from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan ohjelma")

x = int(input("luku 1: "))
y = int(input("luku 2: "))

print(f"{x} + {y} = {summa(x, y)}") # muutos mainissa
print(f"{x} - {y} = {erotus(x, y)}") # muutos mainissa
print(f"{x} * {y} = {tulo(x, y)}")

logger("lopetetaan ohjelma")
print("goodbye!")

