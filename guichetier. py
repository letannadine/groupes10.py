#fait par ALBERT WEFE 18A179FS

﻿from Agent import Agent
from Agent import Agent
class Guichetier(Agent):
	# définition de la méthode spéciale __init__
  def __init__(self,nom="",solde=0,prenom="",poste=""):
	"""Initialisation du compte avec la valeur soldeInitial."""
      # assignation de l'attribut d'instance solde
      Agent.__init__(self,nom)
      self.solde = float(solde)
 	 # définition de la méthode NouveauSolde()
   def NouveauSolde(self, montant):
      """Nouveau solde de compte avec la valeur montant."""
      self.solde = float(montant)
	# définition de la méthode Solde()
  def consultesolde (self):
	"""Retourne le solde."""
      return self.soldesolde
  def retire (self,montant):
	"""retire le compte de la valeur montant. Retourne le solde."""
     self.solde -= montant
     print("Nouveau solde : {:+.2f} €".format(self.solde))
     return self.solde
  def versement (self, montant):
	"""versement le compte de la valeur montant. Retourne le solde."""
     self.solde+=montant
     print("Nouveau solde : {:+.2f} €".format(self.solde))
     return self.solde
  def virement (self,comptc):
	"""le virement le compte de la valeur montant."""
    self.retire(self,montant)
    comptc.versement(self,montant)
  def operation(self):
      self.versement(self,montant)
      self.retire(self,montant)
