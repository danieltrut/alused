#kasutaja sisend
ringide_arv = int(input("Sisestage ringide arv: "))
ring_nr = 1
porgandi_arv = 0
#arvutused
while(ring_nr <= ringide_arv):
    print(ring_nr)
    if(ring_nr % 2 == 0):
        # arvutused 2
        porgandi_arv = porgandi_arv + ring_nr
        # valjastus
        print("said " + str(ring_nr) + " porgandid")
        print("kokku hetkel on " + str(porgandi_arv) + " porgandid")
    ring_nr += 1
 # valjastus
print("porgandite arv " + str(porgandi_arv))