l1 = int(input("Lado 1: "))
l2 = int(input("Lado 2: "))
l3 = int(input("Lado 3: "))

if li > (l2 + l3) or l2 > (l1 + l3) or l3 > (l1 + l2):
	print "Não pode ser um triangulo"
elif l1 == l2 == l3:
	print "Equilatero"
elif l1 == l2 or l1 == l3 or l2 == l3:
	print "Isósceles"
else:
	print "Escaleno"
	
	