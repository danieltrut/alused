import random # Funktsioon
def kalorite_arv(x, y):
    kalorite_arv = ((x * y)/ 1000)*120
    return kalorite_arv

print(float(kalorite_arv(7,30)))

# Küsime kasutajalt sisestatda andmed
baseini_pikkus = int(input("Mitu meetrit on üks basseini pikkus: "))
kord_arv = int(input("Mitu korda käisid: "))
basseiniotsad = []
kalorit_kulus = 0


x = kord_arv
while x > 0:
    basseiniotsad = random.randint(30, 50)

    kulumine = kalorite_arv(basseiniotsad, baseini_pikkus)
    kalorit_kulus += kulumine
    print("Kaloreid kulus: " + str(round(kulumine, 1)))
    x -= 1


print("Kokku kulus: "+str(round(kalorit_kulus, 1)))