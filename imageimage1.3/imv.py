from outils_internet import *
from outils_image import *
class imv:


    def image_nom_commun_adj(self, liste1, liste2, liste3, comp):


        self.comp = comp
        self.liste1 = liste1
        self.liste2 = liste2
        self.liste3 = liste3

        c = 0
        b = 0
        for i in self.liste3:
            if i == "" or i == []:
                pass
            else:

                if self.liste3[c] == [['.']]:
                    b+=1
                    
                elif self.liste1[c] == ["Nom commun"] and self.liste1[c + 1] == ["Adjectif"]:
                        outils_internet.recherche_image(self, self.liste3[c][0],
                                                        self.liste3[c + 1], b)
                    
                          
                elif self.liste1[c] == ["Nom commun"]:
                        outils_internet.recherche_image_phrase(self, self.liste3[c][0],b)

                c+=1
            
                
    def image_verbe(self, liste, compteur):
        
        self.liste = liste
        self.compteur = compteur


        c = 0
        b = 0
        for i in self.liste3:
            if i == "" or i == []:
                pass
            else:
                try:
                    if self.liste3[c] == [['.']]:
                        b+=1
                        
                    for i in self.liste:
                        for j in i:
                            if j == "Verbe":
                                outils_internet.recherche_image_verbe(self, self.liste[c], b)
                        c += 1


                except:
                    pass

    def pos_nom_commun(self, liste, liste2):
 
   
        self.liste = liste
        self.liste2 = liste2

        
        c = 0
        b = 0
        for i in self.liste3:
            if i == "" or i == []:
                pass
            else:

                if self.liste3[c] == [['.']]:
                    b+=1
                print(b)
                for i in self.liste:
                    for j in i :
                        print(self.liste2[0][c])
                        if j == self.liste2[0][c]:
                            print("oui")
                            outils_image.image_position_dg(self,"","","","","", b)
                
                c+=1


            

        
        #fini le truk wikipédia ex voiture -> se diriger
        #vers tous les liens et faire le truk

        #la table est en dessous - > verbe
        #au dessus de la table -> commence par 
















                    

