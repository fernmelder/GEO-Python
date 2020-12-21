#!/usr/bin/python3
# Version 1.0
# Markus Schaper
# https://pypi.org/project/mgrs/
# pip3 install mgrs

import mgrs

latitude = 50.883954
longitude = 7.090628

print("Es werden zwei Variabeln definiert: latitude und longitude")
print("Adresse: Bartholomäusstraße 30, 51145 Köln")

print(latitude)
print(longitude)

m = mgrs.MGRS()
c = m.toMGRS(latitude, longitude)

print("Ausgabe UTM Rev oder MGRS Koordinate:")
print(c)
