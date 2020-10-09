#kasutaja sisend
from random import randint

poialpoisid = int(input("Sisestage mitu pöialpoissi tahab õunu: "))

ounad_kokku = 14

if(poialpoisid > 0):
    for kord in range(1, poialpoisid+1,1):
        ounad = randint(1, 2)
        print(ounad)
        ounad_kokku = ounad_kokku - ounad

print(str(ounad_kokku))