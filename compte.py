import Agent
class compte(Agent):
    def __unit__(self):
        self.nom = "nom"
        self.solde = 0
        Agent.__init__(self,nom)
clients={}
reponse="oui"
while reponse=="oui":
    nom=input("quel est le nom du client ?")
    montant=input("quel est le montant stocké par le client?")
    type=input("quel est le type de compte sollicité?")
    clients[nom]=compte()
    clients[nom].nom=nom
    clients[nom].solde=montant
    reponse=input("voulez vous continuer avec un autre client oui/non\n")
print("les comptes enregistrés sont:\n")
for client in clients.values():
    print("{} a stocké {}".format(client.nom,client.solde))












