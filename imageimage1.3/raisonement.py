from outils_internet import *
from outils_fichier import *

class raisonement:


        #rajouter des condition,
        #un crayon par exemple
        #et faire des fonctions
        #cuillere fonction ?


    def liste(self):
        
        self.liste = []

        self.liste_appuie = []
        
        self.liste_appuie_vivant = []
        self.liste_appuie_non_vivant = []

        self.liste_appuie_vole = []
        self.liste_appuie_vole_meca = []

        self.liste_appuie_eau = []
        self.liste_appuie_eau2 = []

        self.liste_appuie_vivant2 = []
        self.liste_appuie_non_vivant2 = []

        self.liste_appuie_vole2 = []
        self.liste_appuie_vole_meca2 = []

        self.liste_appuie_consomation = []
        self.liste_appuie_consomation2 = []



    def question(self):

        self.premiere = "{} est-il vivant ?"        
        self.premier1 = "{} à quoi ca sert ?"
        
        #est ce un animal
        #est ce un homme
        #est ce un plante

    
        self.deuxieme = "{} a t-il des ailes ?"
        
        self.toisieme = "{} domestique"
        
        self.quatrieme = "{} habitation"
        #eau terre air
        #air/terre
        #eau/terre
        self.cinquieme = "{} composition"

        self.sixieme = "{} habitation"

        self.septième = "{} mange quoi ?"


    def réponse(self):


        self.un = ["respiration","respire","cardiaque",
                   "fréquence cardiaque","espèce","race","génétique","respiration",
                   "corporelle","mammifère","poisson","biologie","vertébrés",
                   "vertébré"]
        self.unun = ["matériaux", "carburant", "électri","machine",
                     "invent","construi","robot","pilote",
                     "instrumen","appareil"]

        
        self.deux = ["ailes","aile","ciel","s'appuie sur l'air",
                     "s'appuient sur l'air","soutient dans l'air",
                     "air"]
        self.deuxdeux = ["portance","ail","propul","décoll",
                         "moteur", "rotors","atterri","aéro"]


        self.trois = ["eau", "branchies","nageoire","marin","sous marin",
                      "océan","rivière","l'eau", "cétacés","cétacé"]


        self.quattre = ["os"]
        self.quattrequattre = ["fer","métal"]


        self.cinq = ["carnivore", "végétarien"]
        self.cinqcinq = ["carburant", "électricité"]

        #si ca vit pas et ste liste == objet
        self.six = []

        #si c self.six fonction ? eclairage, mangeage, sport , jouer, quotidien?
        self.sept = []
        
    def recherche(self, mot):
        raisonement.liste(self)
        raisonement.réponse(self)

        self.mot = mot

        #vivant ou pas?
        outils_internet.recherche_propri(self, self.mot, self.un,
                                  self.liste, self.liste_appuie_vivant,
                                  self.liste_appuie_vivant2)
        #pas vivant
        outils_internet.recherche_propri(self, self.mot , self.unun,
                                  self.liste, self.liste_appuie_non_vivant,
                                  self.liste_appuie_non_vivant2)


        #ca vole
        outils_internet.recherche_propri(self, self.mot , self.deux,
                                  self.liste, self.liste_appuie_vole,
                                  self.liste_appuie_vole2)
        #vole pas
        outils_internet.recherche_propri(self, self.mot, self.deuxdeux,
                                  self.liste, self.liste_appuie_vole_meca,
                                  self.liste_appuie_vole_meca2)

        #ca vit dans l'eau?
        outils_internet.recherche_propri(self, self.mot, self.trois,
                                  self.liste, self.liste_appuie_eau,
                                  self.liste_appuie_eau2)


        #ca mange nouriture ? juste 1 choix
        outils_internet.recherche_propri(self, self.mot, self.cinq,
                                         self.liste, self.liste_appuie_consomation,
                                         self.liste_appuie_consomation2)
        
        #mange pas nouriture
        outils_internet.recherche_propri(self, self.mot, self.cinqcinq,
                                         self.liste, self.liste_appuie_consomation,
                                         self.liste_appuie_consomation2)

        
    def compteur(self, liste, liste3, message,liste_trait):
        
        self.liste = liste
        self.liste3 = liste3
        self.liste_trait = liste_trait
        
        self.message = message

        
        c = 0
        for i in self.liste:
            c+=1

        if c >= len(self.liste3) -  len(self.liste3) + 5:
            self.liste_trait.append(self.message)

            
    def compteur1(self, liste, liste1):

        self.liste = liste
        self.liste1 = liste1
 
        if self.liste != []:
            self.liste1.append(self.liste[0])

  
            
    def compteur_2(self, liste, liste2, liste3, liste4, message, liste_trait):

        
        self.liste = liste
        self.liste2 = liste2
        self.liste3 = liste3
        self.liste4 = liste4
        self.liste_trait = liste_trait
        
        self.message = message

        
        c = 0
        for i in self.liste:
            c+=1
            
        c2 = 0
        for i in self.liste2:
            c2 += 1

        if c >= len(self.liste3) - len(self.liste3) + 5 and \
           c2 >= len(self.liste4)- len(self.liste4) +5:
            self.liste_trait.append(self.message)

            
    def déduction(self, liste_trait):

        self.liste_trait = liste_trait

       
        raisonement.compteur_2(self, self.liste_appuie_vivant2, self.liste_appuie_eau2,
                   self.un, self.trois,          
                   "vivant dans l'eau",
                   self.liste_trait)    


        raisonement.compteur_2(self, self.liste_appuie_vivant2, self.liste_appuie_vole2,
                             self.un, self.deux,
                             "vivant et ca vole",
                             self.liste_trait)


        raisonement.compteur_2(self, self.liste_appuie_non_vivant2, self.liste_appuie_vole_meca2,
                             self.unun, self.deuxdeux,
                             "c'est une machine et ca vole",
                             self.liste_trait)

            
        raisonement.compteur(self, self.liste_appuie_vivant2, self.un,
                           "vivant",
                           self.liste_trait)


        raisonement.compteur(self, self.liste_appuie_non_vivant2, self.unun,
                           "c'est une machine",
                            self.liste_trait)

        raisonement.compteur(self, self.liste_appuie_eau, self.trois,
                           "vie dans l'eau",
                           self.liste_trait)

    def déduction2(self, liste):

        self.liste = liste
        
        #carni ou carbu
        raisonement.compteur1(self, self.liste_appuie_consomation2, self.liste)

    def propriété(self, liste, liste_trait, mot):
        #propriété(self, self.liste_traitement)

        self.mot = mot
        self.liste_trait = liste_trait
    
        raisonement.réponse(self)

        self.liste = liste
        
        c = 0
        liste = []
        
        for i in self.liste:
            try:
                if self.liste[c][1] == "Nom commun":
                    liste.append(self.liste[c][0])
            except:
                pass
            finally:
                c+=1

        raisonement.recherche(self, self.mot)
        raisonement.déduction(self, self.liste_trait)



    def propriété2(self, liste):
        self.liste = liste
        raisonement.déduction2(self, self.liste)
   



#if __name__ == "__main__":

#    liste = []
#    liste2 = []
#    yo = raisonement()
#    yo.recherche("chat")
#    yo.déduction(liste)
#    yo.déduction2(liste2)
#    print(liste)
#    print(liste2)
