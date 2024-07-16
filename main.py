import random
import numpy as np

print("-----------------------------------")
print("Sua senha de 6 dígitos")
print("-----------------------------------")

def gerar_senha():
    x = np.random.randint(0,10, (1,6))
    print(x)

gerar_senha()