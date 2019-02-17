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


    def compteur(self, liste, liste3, message, appuie, file, liste_trait):
        
        self.liste = liste
        self.liste3 = liste3
        self.liste_trait = liste_trait
        
        self.message = message
        self.appuie = appuie
        self.file = file
        
        c = 0
        for i in self.liste:
            c+=1

        if c >= len(self.liste3) -  len(self.liste3) + 5:
            print(self.message)
            self.liste_trait.append(self.message)
            outils_fichier.ecris_propri(self, self.appuie, self.file)



    def compteur1(self, liste, liste1):

        self.liste = liste
        self.liste1 = liste1
        print(self.liste)
        if self.liste != []:
            self.liste1.append(self.liste[0])
        print(self.liste1)

            
    def compteur_2(self, liste, liste2, liste3, liste4, message, appuie, file, liste_trait):

        
        self.liste = liste
        self.liste2 = liste2
        self.liste3 = liste3
        self.liste4 = liste4
        self.liste_trait = liste_trait
        
        self.message = message
        self.appuie = appuie
        self.file = file
        
        c = 0
        for i in self.liste:
            c+=1
            
        c2 = 0
        for i in self.liste2:
            c2 += 1

        if c >= len(self.liste3) - len(self.liste3) + 5 and \
           c2 >= len(self.liste4)- len(self.liste4) +5:
            print(self.message)
            self.liste_trait.append(self.message)
            outils_fichier.ecris_propri(self, self.appuie, self.file)


    def déduction(self, liste_trait):

        self.liste_trait = liste_trait

        try:
            raisonement.compteur_2(self, self.liste_appuie_vivant2, self.liste_appuie_eau2,
                       self.un, self.trois,          
                       "vivant dans l'eau",
                       self.liste_appuie[0], "propriete_vivant_eau.py", self.liste_trait)    


            raisonement.compteur_2(self, self.liste_appuie_vivant2, self.liste_appuie_vole2,
                                 self.un, self.deux,
                                 "vivant et ca vole",
                                 self.liste_appuie[0], "propriete_vivant_vol.py", self.liste_trait)


            raisonement.compteur_2(self, self.liste_appuie_non_vivant2, self.liste_appuie_vole_meca2,
                                 self.unun, self.deuxdeux,
                                 "c'est une machine et ca vole",
                                 self.liste_appuie[0], "propriete_non_vivant_vol.py", self.liste_trait)

                
            raisonement.compteur(self, self.liste_appuie_vivant2, self.un,
                               "vivant",
                               self.liste_appuie[0], "propriete_vivant_air.py", self.liste_trait)


            raisonement.compteur(self, self.liste_appuie_non_vivant2, self.unun,
                               "c'est une machine",
                               self.liste_appuie[0], "propriete_pas_vivant.py", self.liste_trait)

            raisonement.compteur(self, self.liste_appuie_eau, self.trois,
                               "vie dans l'eau",
                               self.liste_appuie[0], "", self.liste_trait)
            
        except:
            print("y'a eu une erreur")



            
    def déduction2(self, liste):

        self.liste = liste
        
        #carni ou carbu
        raisonement.compteur1(self, self.liste_appuie_consomation2, self.liste)

        print(self.liste_appuie_consomation)


           
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
        print("fait")
        
#-------------------------------PART 2----------------------------------------------------------------
        
    def affichage(self, liste, liste2):
        self.liste = liste
        self.liste2 = liste2

        c = 0
        d = 0
        
        for i in self.liste:
            if i == [] or i == [""] or i == [" "] or i == [ ]:
                pass
            else:
                for j in i:

                    for k in j:

                        if k == "Nom commun":
                            print(j[0],"est un",j[-2],"il est", j[-1])
                            
                        elif k == "Verbe":
                            print(j[0], self.liste2[c])
                            
            c+=1


    def explication_nom_commun_liste(self):
        pass

    def explication_verbe_liste(self):
        pass

    def explication_phrase(self):
        pass

    

#if __name__ == "__main__":

    #yo = raisonement()
    #yo.recherche("panda géant")




    
