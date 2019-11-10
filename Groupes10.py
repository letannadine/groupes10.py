#coding:utf-8
class Agent:
     def__init __ (self, nom, prenom, poste):
        self.nom=""
        self.prenom=""
        self.poste=""
        self.email=""
        self.tel=""
        
        
     def_str_(self):
        retourne (self.nom, self.prenom, self.poste)

class Client:
   
 def __init__(self, nom, prénom, âge, adresse):#consructeur de clients
        print("")   
        print("     ****CREATION D'UN NOUVEAU CLIENT DE LA BANQUE****")
        self.nom = nom
        self.prénom = prénom
        self.âge = âge
        self.adresse = adresse
        print("")
        print("    * informations personnelles du client *")
        
c1 = Client("ALIMATOU", "BOUBAKARI", 45, "ngaoundéré")#objet c1
print("")
print(" Nom du client: "+c1.nom)#concaaténation
print(" Prénom du client: "+c1.prénom)
print(" Âge du client: {}".format(c1.âge)+" ans")#limite de la concaténation car pas possible entre string et int passsons aux textes préformaté
print(" Adresse du client: "+c1.adresse)     

def ajouteCompte(self,compte):
    self.__mesComptes.opend(compte)
    compte.assigneTitulaire(self)
    
def identifieCompte(self):#elle dépendra de la classe compte 
    print ("Sur quel compte ?")
    x=input("?")
    for c in self.__mesComptes:
        if c.donneNumero() == x:
            return c
    
def emprunt(self):
    c=self.identifieCompte()
    print ("quel montant ?")
    x=int(input("?"))
    c.retire(x)
    
def depose(self):
    c=self.identifieCompte()
    print ("quel montant ?")
    x=int(input("?"))
    c.depose(x)

﻿#fait par ALBERT WEFE 18A179FS
from Agent import Agent
from Agent import Agent
class Guichetier(Agent):
	# définition de la méthode spéciale __init__
  def __init__(self,nom="",solde=0,prenom="",poste=""):
	"""Initialisation du compte avec la valeur soldeInitial."""
      # assignation de l'attribut d'instance solde
      Agent.__init__(self,nom)
      self.solde = float(input("entre votre solde"))
	self.montant = float(input("entre votre montant"))

   def _get_montant(self):
       
 	print("\t__Compte__\n\nVotre numéro de compte est : {0} \n".format(self._montant))
   
     return self._montant    
   
   def _get_solde(self):
       
 	print("\t__Compte__\n\nVotre solde est de {0} FCFA \n".format(self._solde))
   
     return self._solde
    

   def _set_solde(self,new_solde):
    
    	print("\t__Compte__\n\nVotre nouveau solde est de {0} FCFA \n".format(new_solde))
       
	 self._solde = new_solde

  def _set_montant(self,new_solde):
    
    	print("\t__Compte__\n\nVotre nouveau solde est de {0} FCFA \n".format(new_solde))
       
	 self._montant = new_montant    
    
 	 # définition de la méthode NouveauSolde()
   def NouveauSolde(self, montant):
      """Nouveau solde de compte avec la valeur montant."""
      self.solde = float(montant)

	# définition de la méthode Solde()
  def consultesolde (self):
	"""Retourne le solde."""
      return self.solde

  def retire (self,montant):
	"""retire le compte de la valeur montant. Retourne le solde."""
     if self.solde ˂= self.montant:
          print ("impossible de ce faire retraire")
      else:
        self.solde-=self.montant
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

class controleur(Agent):
	def __init__(self, nom, prenom ,solde,montant):
		Agent.__init__(self, nom, prenom)
		solde.verifications_montants()
		ifi(solde = montant)
print(" le montant du transactions jornalieres correspondant a la solde est :")
print(" affiche OK")
print(" sinom")
print(" affiche NON")

class Gestionnaires(Agent):
    def __init__(self,nom,tel,email):
        self.nom= nom
        self.tel= tel
        self.email= email
        return "gestionnaire{0},nimero telephone{1},compte email{2}".format(self.nom,self.tel,self.email)
        gestionnaire=gestionnaire("Mamat haman",+1055000000,wourden@email.com)
        Banque.__init__(self,nom,email)
        self.tel=tel
        


