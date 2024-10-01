import random

def ziehung():
    zahlen = list(range(1, 46))
    gezogene_zahlen = []

    for _ in range(6):
        zufallsindex = random.randint(0, len(zahlen) - 1)
        gezogene_zahl = zahlen.pop(zufallsindex)
        gezogene_zahlen.append(gezogene_zahl)

    return gezogene_zahlen


def statistik_ziehung():
    statistik = {i: 0 for i in range(1, 46)}
    alle_ziehungen = []

    for _ in range(1000):
        gezogene_zahlen = ziehung()
        alle_ziehungen.append(gezogene_zahlen)
        for zahl in gezogene_zahlen:
            statistik[zahl] += 1

    return statistik, alle_ziehungen

# einmal Ziehung
print("Einmalige Ziehung:")
print(ziehung())

# 1000 Ziehungen und genauen Zahlen daneben
print("\nStatistik nach 1000 Ziehungen:")
statistik, alle_ziehungen = statistik_ziehung()

for zahl, haeufigkeit in sorted(statistik.items()):
    print(f"Zahl {zahl}: {haeufigkeit} mal gezogen")

print("\nAlle 1000 Ziehungen:")
for idx, ziehung in enumerate(alle_ziehungen, start=1):
    print(f"Ziehung {idx}: {ziehung}")
