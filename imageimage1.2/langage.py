from mémoire import *
from outils_fichier import *
from politesse import *
from outils_internet import *

#Regle
    #ne seront maqué que les truk importants

    #dans mémoire str.find la liste, si ya pas on ajoute fais le
    #ca fait ia


class langage:

    def début1(self):
        #début1(self, oInput)
        #self.oInput = oInput
        politesse.politesse(self)
        self.oInput = input("salut")
        self.oInput = self.oInput.lower()
        langage.exception()
        print(self.oInput)

        
        c = 0
        for i in self.politesse:
            if self.oInput != i:
                pass
            elif self.oInput == i:
                c+=1
        if c <= 0:
            outils_fichier.ecris_propri(self, self.oInput, "politesse.py")

    def exception(self):

        exception1 = "ça va"
        
        if self.oInput == "ca va" or self.oInput == "ca va ?" :
            self.oInput = self.oInput.replace("c","ç")
        
        elif self.oInput == "hey" or self.oInput == "Hey":
            pass

    def début1_1(self):
        mémoire.liste(self)
        
        liste = []
        liste1 = [[],[],[],[],[],[],[],[],[],[],[],[],[]]
        
        self.liste_langage = []       #liste importante
        self.ponctu = []            #2eme lsite importante
        
        liste.append(self.oInput)

        c = 0
        for i in liste:
            for j in i:
                if j == " ":
                    c+=1
                else:
                    liste1[c].append(j)
                    
        for i in self.liste_ponctuation:
            for j in liste1:
                if j == [] or j == [""] or j == [" "] or j == [ ]:
                    pass
                else:
                    j = "".join(j)
                    if i == j :
                        
                        langage.début1_1_outils( "?", self.liste_langage, self.intero, i)
                        langage.début1_1_outils( "!", self.liste_langage, self.excla, i)
                        langage.début1_1_outils( ".", self.liste_langage, self.point, i)
                        langage.début1_1_outils( ",", self.liste_langage, self.virgule, i)
                        langage.début1_1_outils( "'", self.liste_langage, self.guillemet, i)
                        langage.début1_1_outils( ":", self.liste_langage, self.deuxpoints, i)
                        langage.début1_1_outils( "?!", self.liste_langage, self.interoexcla, i)
                        self.ponctu = self.oInput[-1]
                        self.oInput = self.oInput[:-1]

        
        if self.liste_langage == []:
            self.liste_langage.append("aucune ponctuation")
            
        print(self.liste_langage)

        
    def début1_1_outils(self, ponctuation, liste, késako, i):
        mémoire.liste(self)

        self.i = i
        self.liste = liste
        self.késako = késako
        self.ponctuation = ponctuation
        
        if self.i == self.ponctuation:
            self.liste.extend(self.késako)

    def début1_reponse(self):

        pass

        
    def définition_context_phrase(self):
        
        
        liste = []
        outils_internet.recherche_langage(self, self.oInput, liste)
        
        self.politesse = ""
        

        a = ["forme de politesse", "Forme de politesse", "Marque de politesse",
             "Formule de salutation", "salutation", "Salutation", "Formule de politesse"]

        for i in a:
    
            formule_politesse = str(liste).find(str(i))
    
            if formule_politesse > 0:
                print(self.oInput + " beauté, c deja un bon debut !")
                #formule de politesse
                self.politesse = True
                break

        if self.politesse == True:
            pass
            #passe a la suite sinon
            #faut trouvé ce que le pelo raconte





langage = langage()
langage.début1()
langage.début1_1()
langage.définition_context_phrase()                      
