#!/usr/bin/env python
'''Divisió. Divisió entre dos nombres enters.
Institut Icària
Programació - 1r Batxillerat - Curs 2023-24
Procediment matemàtic mitjançant el qual un nombre enter és dividit per un
altre nombre enter. Dividir dos nombres. Divisió, quocient i residu
'''
__author__ = "Daniel Sousa"
__email__ = "dsousa@instituticaria.cat"
__date__ = "2025/10/20"

Dividend = int(input("Introduir dividend"))
Divisor = int(input("Introduir divisor"))
Quocient = (Dividend) // (Divisor)
Residu = (Dividend) % (Divisor)
print(f"Divisió: {Dividend}/{Divisor}")
print(f"Quocient: {Quocient}")
print(f"Residu: {Residu}")
