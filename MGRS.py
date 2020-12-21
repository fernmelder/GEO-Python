#!/usr/bin/python3
# Version 1.4
# Markus Schaper
# https://pypi.org/project/mgrs/
# pip3 install mgrs

import mgrs

latitude = 50.883954
longitude = 7.090628

print("Diese Adresse: Bartholomäusstraße 30, 51145 Köln wird in einen Längen- und Breitgrad umgewandelt.\n")
print("Es werden zwei Variabeln definiert:", latitude, "und", longitude, "\n")

m = mgrs.MGRS()
c = m.toMGRS(latitude, longitude)

print("Ausgabe UTM Rev oder MGRS Koordinate:", c, "\n")

print(c[0:3], c[3:5], c[5:10], c[10:15])