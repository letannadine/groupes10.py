class Agent:
	def __init__(self, nom, prenom):
		self.nom = nom
		self.prenom = prenom
class controleur(Agent):
	def __init__(self, nom, prenom ,solde,montant):
		Agent.__init__(self, nom, prenom)
		solde.verifications_montants()
		ifi(solde = montant)
print(" le montant du transactions jornalieres correspondant a la solde est :")
print(" affiche OK")
print(" sinom")
print(" affiche NON")

