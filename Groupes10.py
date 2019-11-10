#coding:utf-8class 

Agent:
     def__init __ (self, nom, prenom, poste):
        self.nom=""
        self.prenom=""
        self.poste=""
        
        
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
