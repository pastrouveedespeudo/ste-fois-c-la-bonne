
from internet import *

class propriete:

    
    #métaphore ou non
    #que ce soi complet ou pas tant que ca marche pour les exemples

    #je vole avec une baleine
    # je nage avec elle

    
    def propriete(self):

        pass


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
        self.unun = ["matériaux", "carburant", "électricité","machine",
                     "inventé par", "inventeur","inventé","électrique",
                     "robot"]

        
        self.deux = ["ailes","aile","ciel","s'appuie sur l'air",
                     "s'appuient sur l'air","soutient dans l'air",
                     "air"]
        self.deuxdeux = ["portance","principe de la portance","propulsion",
                         "moteur", "rotors","motopropulseur","train atterissage"]


        self.trois = ["eau", "branchies","nageoire","marin","sous marin",
                      "océan","rivière","l'eau", "cétacés","cétacé"]


        self.quattre = ["os"]
        self.quattrequattre = ["fer","métal"]



    def recherche(self):

        #inte

        liste = []
        
        self.liste_appuie_vivant = []
        self.liste_appuie_non_vivant = []

        self.liste_appuie_vole = []
        self.liste_appuie_vole_meca = []

        self.liste_appuie_eau = []
        
        propriete.réponse()

        #vivant ou pas?
        internet.recherche_propri(self, "baleine", self.un,
                                  liste, self.liste_appuie_vivant)
        #pas vivant
        internet.recherche_propri(self, "baleine", self.unun,
                                  liste, self.liste_appuie_non_vivant)


        #ca vole ou pas?
        internet.recherche_propri(self, "baleine", self.deux,
                                  liste, self.liste_appuie_vole)
        #vole pas
        internet.recherche_propri(self, "baleine", self.deuxdeux,
                                  liste, self.liste_appuie_vole_meca)

        #ca vit dans l'eau?
        internet.recherche_propri(self, "baleine", self.trois,
                                  liste, self.liste_appuie_eau)

        
    def déduction(self):


        if self.liste_appuie_vivant != [] and self.liste_appuie_eau != []:
            print("vivant dans l'eau")
            fichier.ecris_propri(self, self.liste_appuie[0], "propriete_vivant_eau.py")

         
        elif self.liste_appuie_vivant != [] and self.liste_appuie_vole != []:
            print("vivant et ca vole")
            fichier.ecris_propri(self, self.liste_appuie[0], "propriete_vivant_vol.py")

 
        elif self.liste_appuie_non_vivant != [] and self.liste_appuie_vole_meca != []:
            print("c'est une machine et ca vole")
            fichier.ecris_propri(self, self.liste_appuie[0], "propriete_non_vivant_vol.py")


        elif self.liste_appuie_vivant != []:
            print("vivant")
            fichier.ecris_propri(self, self.liste_appuie[0], "propriete_vivant_air.py")

        

        elif self.liste_appuie_non_vivant != []:
            print("c'est une machine")
            fichier.ecris_propri(self, self.liste_appuie[0], "propriete_non_vivant.py")

    def dessin(self):
        pass

