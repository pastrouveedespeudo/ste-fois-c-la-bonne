from outils_internet import *

class imv:


    def image_nom_commun_adj(self, liste1, liste2):
        
        c5 = 0
        liste = []
        liste3 = []
        self.liste1 = liste1
        self.liste2 = liste2
        
        for i in self.liste2:
            if i == []:
                pass
            else:
                liste.append(self.liste2)
                liste3.append(self.liste2)
                
            c5 += 1

        c = 0
        c6 = 0


        
        for i in liste:

            try:
                if liste[0][c][1] == "Nom commun" and liste[0][c + 1][1] == "Adjectif":
                    print("oui",liste[0][c][1],liste[0][c + 1][1])
                    outils_internet.recherche_image(self, self.liste2[c][0],
                                             self.liste2[c + 1][0], self.liste1)
                    
                    
            except:
                pass


            try:    
                if liste[0][c][1] == "Nom commun" and liste3[0][c + 2][1] == "Verbe" and liste[0][c + 2][1] == "Adjectif":
                    print("ui",liste[0][c][1],liste[0][c + 2][1], liste3[0][c+2][1])
                    outils_internet.recherche_image(self, self.liste2[c][0],
                                             self.liste2[c + 2][0], self.liste1)
                    
                   
            except:
                pass

            
            try:    
                if liste[0][c][1] == "Nom commun":
                    print("ouais", liste[0][c][1])
                    outils_internet.recherche_image_phrase(self, self.liste2[c][0], self.liste1)

                    
            except:
                pass
           
            
            finally:
                c+=1
                






    def pos_nom_commun(self, liste_main, liste_traitement, compteur, liste_image, liste_image2):
 
        self.compteur = compteur
        self.liste_main = liste_main
        self.liste_image = liste_image
        self.liste_image2 = liste_image2
        self.liste_traitement = liste_traitement
        
        c = 0
        liste = []
        self.liste_image_phase1 = []

        try:
            for i in range(self.compteur + 1):
                for i in self.liste_main:
                    for j in i :

                        if self.liste_traitement[c][0] == j:
                            print(self.liste_traitement[c][0], j)
                            if j in self.liste_main[0]:
                
                                outils_image.image_position_dg(self, self.liste_image[1], self.liste_image[0],
                                            0,0,0, self.liste_image2)
                                
                            elif j in self.liste_direction[1]:
                 
                                outils_image.image_position_dg(self, self.liste_image[0], self.liste_image[1],
                                            0,0,0, self.liste_image2)
                                
                            elif j in self.liste_direction[2]:
                      
                                outils_image.image_position_haut_bas(self,self.liste_image[1], self.liste_image[0],
                                               self.liste_image2)

                            elif j in self.liste_direction[3]:
                        
                                outils_image.image_position_haut_bas(self,self.liste_image[0], self.liste_image[1],
                                               self.liste_image2)
                            else:
                                print("no matches bitches")
                                
                c+=1
        except:
            pass

            

        
        #fini le truk wikipédia ex voiture -> se diriger
        #vers tous les liens et faire le truk

        #la table est en dessous - > verbe
        #au dessus de la table -> commence par 


    def image_verbe(self, liste, liste1):
        
        self.liste = liste
        self.liste1 = liste1

        c = 0
        for i in self.liste:
            for j in i:
                if j == "Verbe":
           
                    outils_internet.recherche_image_verbe(self, self.liste[c][0], self.liste1)
            c += 1












