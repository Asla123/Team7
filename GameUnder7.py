from random import*
compte=600
while True:
	print("============================")
	print("*********** Under 7 **********")
	print("\n			Compte=",compte,"€")
	while True:
		choix=int(input("\nChoisissez entre ces propositions\n\n[1] Moins(2.3)\n[2] Sept(5.3)\n[3] Plus(2.3)\n\nQue choisissez-vous? "))
		if choix>3 or choix<1:
			print("Choix non disponible,ressayez!")
		else:
			break
	while True:
		p=float(input("\nPlacer le pari(200€ minimum) \n"))
		if compte-p<0:
			print(" Le solde est insuffisant,ressayez !")
		elif p<200:
			print(" Le pari mini est de 200€")
		else:
			break
	d1=randint(1,6)
	d2=randint(1,6)
	print("\na= ",d1,"\nb= ",d2)
	if d1+d2<7 and choix==1:
		print("\nVous avez gagné ",2.3*p,"€")
		compte=compte-p+2.3*p
		print("_____________________________________\n")
	elif d1+d2==7 and choix==2:
		print("\nVous avez gagné ",5.3*p,"€")
		compte=compte-p+5.3*p
		print("____________________________________\n")
	elif d1+d2>7 and choix==3:
		print("\nVous avez gagné ",2.3*p,"€")
		compte=compte-p+2.3*p
		print("____________________________________\n")
	else:
		print("\nVous avez perdu !")
		print("____________________________________\n")
		compte=compte-p
	if compte<200:
		print("Vous ne pouvez plus jouer à Under 7, car vous n'avez plus d'argent necessaire.")
		break