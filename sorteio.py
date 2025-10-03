import random
import time
import os
import pyfiglet  

def sorteio(inicio, fim):
    vencedor = random.randint(inicio, fim)

    print("Iniciando sorteio...\n")
    time.sleep(1)

    for _ in range(20):  
        num = random.randint(inicio, fim)
        print(f"🔢 {num}", end="\r", flush=True)
        time.sleep(0.1)

    time.sleep(0.5)
    os.system("cls" if os.name == "nt" else "clear") 

    ascii_banner = pyfiglet.figlet_format(f"{vencedor}")
    print("🎉 O NÚMERO SORTEADO FOI... 🎉\n")
    print(ascii_banner)
    print("Parabéns ao vencedor!!! ")

# Exemplo de uso
sorteio(1, 50)
