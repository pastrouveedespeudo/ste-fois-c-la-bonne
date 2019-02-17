
from internet import *
from fichier import *

class propriete:

    
    #métaphore ou non
    #que ce soi complet ou pas tant que ca marche pour les exemples

    #je vole avec une baleine
    # je nage avec elle

    def question(self):

        self.premiere = "{} est-il vivant ?"        
        self.premier1 = "{} à quoi ca sert ?"
        
        
        self.deuxieme = "{} a t-il des ailes ?"
        
        self.toisieme = "{} domestique"
        
        self.quatrieme = "{} habitation"

        self.cinquieme = "{} composition"

        self.sixieme = "{} habitation"

        
    def path(self):

        self.one = "https://fr.wikipedia.org/wiki/{}"
        
        self.two = "https://fr.wikipedia.org/wiki/Anatomie_du_{}"

  

    def réponse(self):

        #on pourrait trouvé le mot qui apparait le plus, si c vivant on l'ajoute
        #a la liste

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

        #le blem avec ce gnre de truk c qui faut en mettre
        #et regler le truk de mot mini...  chier

    def recherche(self, mot):

        #inte

        liste = []
        self.mot = mot

        self.liste_appuie = []
        
        self.liste_appuie_vivant = []
        self.liste_appuie_non_vivant = []

        self.liste_appuie_vole = []
        self.liste_appuie_vole_meca = []

        self.liste_appuie_eau = []

        self.liste_appuie_vivant2 = []
        self.liste_appuie_non_vivant2 = []

        self.liste_appuie_vole2 = []
        self.liste_appuie_vole_meca2 = []

        self.liste_appuie_eau2 = []
        
        propriete.réponse(self)


        #vivant ou pas?
        internet.recherche_propri(self, self.mot, self.un,
                                  liste, self.liste_appuie_vivant,
                                  self.liste_appuie_vivant2)
        #pas vivant
        internet.recherche_propri(self, self.mot , self.unun,
                                  liste, self.liste_appuie_non_vivant,
                                  self.liste_appuie_non_vivant2)


        #ca vole ou pas?
        internet.recherche_propri(self, self.mot , self.deux,
                                  liste, self.liste_appuie_vole,
                                  self.liste_appuie_vole2)
        #vole pas
        internet.recherche_propri(self, self.mot, self.deuxdeux,
                                  liste, self.liste_appuie_vole_meca,
                                  self.liste_appuie_vole_meca2)

        #ca vit dans l'eau?
        internet.recherche_propri(self, self.mot, self.trois,
                                  liste, self.liste_appuie_eau,
                                  self.liste_appuie_eau2)



        
    def déduction(self):

        try:
            propriete.compteur_2(self, self.liste_appuie_vivant2, self.liste_appuie_eau2,
                       self.un, self.trois,          
                       "vivant dans l'eau",
                       self.liste_appuie[0], "propriete_vivant_eau.py")    


            propriete.compteur_2(self, self.liste_appuie_vivant2, self.liste_appuie_vole2,
                                 self.un, self.deux,
                                 "vivant et ca vole",
                                 self.liste_appuie[0], "propriete_vivant_vol.py")


            propriete.compteur_2(self, self.liste_appuie_non_vivant2, self.liste_appuie_vole_meca2,
                                 self.unun, self.deuxdeux,
                                 "c'est une machine et ca vole",
                                 self.liste_appuie[0], "propriete_non_vivant_vol.py")

                
            propriete.compteur(self, self.liste_appuie_vivant2, self.un,
                               "vivant",
                               self.liste_appuie[0], "propriete_vivant_air.py")


            propriete.compteur(self, self.liste_appuie_non_vivant2, self.unun,
                               "c'est une machine",
                               self.liste_appuie[0], "propriete_pas_vivant.py")

            propriete.compteur(self, self.liste_appuie_eau, self.trois,
                               "vie dans l'eau",
                               self.liste_appuie[0], "")

        except:
            print("y'a eu une erreur")

    #c un objet


            
    def compteur_2(self, liste, liste2, liste3, liste4, message, appuie, file):
        
        self.liste = liste
        self.liste2 = liste2
        self.liste3 = liste3
        self.liste4 = liste4
        
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
            fichier.ecris_propri(self, self.appuie, self.file)


    def compteur(self, liste, liste3, message, appuie, file):
        
        self.liste = liste
        self.liste3 = liste3
        
        self.message = message
        self.appuie = appuie
        self.file = file
        
        c = 0
        for i in self.liste:
            c+=1

        if c >= len(self.liste3) -  len(self.liste3) + 5:
            print(self.message)
            fichier.ecris_propri(self, self.appuie, self.file)




        #rajouter des condition,
        #un crayon par exemple
        #et faire des fonctions
        #cuillere fonction ?





    def dessin(self):
        pass

