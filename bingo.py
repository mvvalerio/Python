from random import randint
import time
import os

sorteados = set()
while 1:
    num = randint(1, 100)
    if num in sorteados:
        print(f"Número repetido ({num})! Acabou o sorteio.")
        break
        
    sorteados.add(num)
    print(f"Número sorteado: {num}")
     
    time.sleep(1)
    os.system("clear")