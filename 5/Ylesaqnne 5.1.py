#loemem andmed failist ja lisame uhe kaupa nimekirja
fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []
for rida in fail:
    vastuvõetud.append(int(rida))
    fail.close()

#kontrollime et andmed on loetud
    print(vastuvõetud)

#kusime aasrta taisarvust

aasta = int(input("Sisesta aasta vahemikus 2011 2019"))

#aastane nimekiri
aastad = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

#kontrollime aasta olemasolu
if aasta in aastad:
    # on vaja teada millise indexiga antud aasta nimekirjas on
    i = aastad.index(aasta)
    # printdime sama indeksiga vaartus vastuvoetud
    print("Aastas" + str(aasta) + "v]eti vastu" + str(vastuvõetud[i]))