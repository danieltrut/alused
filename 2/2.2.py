#kasutaja sisend
nimi = input("Sisestage leedu prerekonnanimi: ")
if (nimi[-2:] == "ne"):
print("abiellus")
elif(nimi[-2:] == "te"):
print("vallaline")
elif(nimi[-1:] == "e" and (nimi[-2:] != "ne" or nimi[-2:] != "te")):
print("maaramata")