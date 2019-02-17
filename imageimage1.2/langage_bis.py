from mémoire import *
from début import *
from outils_fichier import *

class langage_bis:
    
    def debut(self):
        print("salut")

    def jesaispas(self):
        début.début(self)
        #print(self.debut)

    def initialisation_phrase(self, phrase):

        self.phrase = phrase
        self.oInput = input()
        
    def traitement(self):

        self.liste_oInput = []
        self.liste_oInput.append(self.oInput)
        
        #print(self.liste_oInput)
        #print("\n")

        liste_comptage = []
        
        c = 0
        d = 0
        try:
            continuer = True
            while continuer:
                for i in self.debut[c]:
                    if self.liste_oInput == i:
                        #print(self.debut[c][d + 1])
                        liste_comptage.append(self.debut[c][d + 1])

                #print("\n")
                c+=1
                        
        except:
            pass
        finally:
            
            liste_reponse = [[""]]
            recurence = 0
            
            #print(liste_comptage)
            for i in liste_comptage:
                a = liste_comptage.count(i)
                #print(i, a)
                if a > recurence:
                    recurence = a
                    del liste_reponse[0]
                    liste_reponse.append(i)
            print("reponse:",liste_reponse)
            self.liste_oInput = []
            liste_reponse = []



if __name__ == "__main__":
    
    langage_bis = langage_bis()
    langage_bis.debut()
    langage_bis.jesaispas()
    ocontinuer = True
    while ocontinuer :

        langage_bis.initialisation_phrase("")
        langage_bis.traitement()

