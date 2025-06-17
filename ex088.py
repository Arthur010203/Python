import random
from time import sleep

# Lista principal para armazenar os jogos
jogos = []

print("-" * 40)
print("  GERADOR DE PALPITES MEGA SENA   ")
print("-" * 40)

quantidade_jogos = int(input("Quantos jogos você quer que eu sorteie? "))
jogos = []

for i in range(quantidade_jogos):
    jogo = sorted(random.sample(range(1, 61), 6))
    jogos.append(jogo)

print("\nSorteando os jogos...\n")
sleep(1)

for i, jogo in enumerate(jogos, 1):
    print(f"Jodo {i}: {jogo}")
    sleep(0.5)

print("\nBoa sorte!🍀")