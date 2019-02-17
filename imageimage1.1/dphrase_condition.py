from internet import *
from image import *
from propriete import *

class phrase:





    def temps(self):

        self.indice_temps = ["hier","passé","demain","après demain","aujourd'hui"]
        self.temps = ["Passé","Imparfait"]


        #sert pour la final condition a == True ou pas True
        



    


        
        



    def nom_commun(self, liste):    #RIEN COMPRIS
        #a regarder
        c1 = 0
        self.liste = liste

        for i in self.liste:
            if i == []:
                pass
            else:
                for i in range(len(self.liste[c1])):
                    art = str(self.liste[c1]).find(str("Article"))
                    art1 = str(self.liste[c1]).find(str("article"))
                    print(self.liste[c1][1])
                    if self.liste[c1][1] == "Nom commun":
                
                        Dico.nom_adj(self, self.liste_image)
                    break
            c1 += 1

                    

    def proprio(self, liste):
        propriete.path(self)
        propriete.réponse(self)

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

        print(liste)
        for i in liste:
            print(i)
            propriete.recherche(self, i)
            propriete.déduction(self)
            print("\n")
        
            
            #refaire déduction
            #la déduction se met dans les fichier








    def maisouestdoncornicar(self, liste, liste2, liste3):
        liste_maisouest = ["mais","ou","et","donc","or","ni","car"]
        
        self.liste = liste
        self.liste2 = liste2
        self.liste3 = liste3
        liste1 = []

        c = 0
        for i in self.liste:
            if self.liste[c][0] == "et":
                for i in self.liste:
                    if self.liste[c][1] == "Nom commun":
                        liste1.append(self.liste[c][0])

        image.image(self, self.liste2[0], self.liste2[1],
              0, 0, 0, self.liste_image_phase1)


    def verbe(self):
        pass
        #On récupere internet infinitif
        #on recup image
        #on affiche






    def ponctuation(self):
        pass



    def taille(self):
        pass
        #le petit chien parle avec le gros chat


    def adverbe(self):
        pass
        #alors marque un résultat ou une agression
    
    def préposition(self):
        pass
        #apres marque la visualisation du futur ou avant apres
        #apres jte dis jmen balec, apres avoir fais ca

        

#-----------------------------------------------------------------------------------------


    def nom_adj(self, liste1, liste2):
 
        c5 = 0
        liste = []
        self.liste1 = liste1
        self.liste2 = liste2
        liste3 = []
        
        for i in self.liste2:
            if i == []:
                pass
            else:
                liste.append(self.liste2[c5][1])
                liste3.append(self.liste2[c5][2])
            c5 += 1


        c = 0
        c6 = 0
        for i in liste:

            try:
                if liste[c] == "Nom commun" and liste[c + 1] == "Adjectif":
                    print("oui",liste[c],liste[c + 1])
                    internet.recherche_image(self, self.liste2[c][0],
                                             self.liste2[c + 1][0], self.liste1)
                    
                    
            except:
                pass


            try:    
                if liste[c] == "Nom commun" and liste3[c + 2] == "Verbe" and liste[c + 2] == "Adjectif":
                    print("ui",liste[c],liste[c + 2], liste3[c+2])
                    internet.recherche_image(self, self.liste2[c][0],
                                             self.liste2[c + 2][0], self.liste1)
                    
                   
            except:
                pass

            
            try:    
                if liste[c] == "Nom commun":
                    print("ouais", liste[c])
                    internet.recherche_image_phrase(self, self.liste2[c][0], self.liste1)

                    
            except:
                pass
           
            
            finally:
                c+=1
                

    def pos_fonction(self):#fini le truk wikipédia ex voiture -> se diriger
                            #vers tous les liens et faire le truk



        #IMAGE
        #la table est en dessous - > verbe
        #au dessus de la table -> commence par 
        self.liste_direction = [["à droite", "droite"],
                                ["à gauche", "gauche"],
                                ["haut","sur", "au dessus"],
                                ["en dessous", "bas", "en bas"]]


        self.liste_image_phase1 = []

        liste = []
        c = 0

        for i in range(self.compteur1 + 1):
            for i in self.liste_direction:
                for j in i :

                    if self.liste_traitement[c][0] == j:
                        
                        if j in self.liste_direction[0]:
                            image.image(self, self.liste_image[1], self.liste_image[0],
                                        0,0,0, self.liste_image_phase1)
                            
                        elif j in self.liste_direction[1]:
                            image.image(self, self.liste_image[0], self.liste_image[1],
                                        0,0,0, self.liste_image_phase1)
                            
                        elif j in self.liste_direction[2]:
                            image.image_haut_bas(self,self.liste_image[1], self.liste_image[0],
                                           self.liste_image_phase1)

                        elif j in self.liste_direction[3]:
                            image.image_haut_bas(self,self.liste_image[0], self.liste_image[1],
                                           self.liste_image_phase1)
                        else:
                            print("no matches bitches")
                            
            c+=1

        print(self.liste_image_phase1)


    def prenom_premier(self, liste):#oki
        
        c = 0
        self.liste = liste
        
        for i in self.liste:

            try:
                if self.liste[c][3] == "prénom" and self.liste[c][1] == "Article défini"\
                   or self.liste[c][1] == "Article indéfini":
                    del self.liste[c][3]
                    self.liste[c].append("pas prénom")
            except:
                pass
            try:   
                if self.liste[c][3] == "prénom" and self.liste[c+1][1] == "Nom commun":
                    del self.liste[c][3]
                    self.liste[c].append("pas prénom")
            except:
                pass

            try:
                if self.liste[c][3] == "prénom" and self.liste[c-1][1] == "Article défini":
                    del self.liste[c][3]
                    self.liste[c].append("pas prénom")
            except:
                pass

            try:
                if self.liste[c][3] == "prénom" and self.liste[c+1][2] == "Verbe":
                    pass
            except:
                pass

            try:
                if self.liste[c][3] == "prénom" and self.liste[c-1][2] == "Préposition":
                    pass
            except:
                pass
                
            finally :    
                c+=1

        #a plus remplir vérifier les conditions ou c un prenom ou pas
        #le jean est bleu ca marche dans les deux sens...       




    def condition_article(self, liste):     #OKI

        #Article + Verbe ex le crayon (correction auto)
        #si y'a un article alors le prochain truk ne peux pas etre un verbe

        self.liste = liste

        
        c1 = 0
        c2 = 0
        for i in self.liste:
            if i == []:
                pass
            else:
                for i in range(len(liste[c1])):
                    art = str(self.liste[c1]).find(str("Article"))
                    art1 = str(self.liste[c1]).find(str("article"))
                    art2 = str(self.liste[c1]).find(str("Lettre"))
                    art3 = str(self.liste[c1]).find(str("Préposition"))
                    if art > 0 or art1 > 0 or art2 > 0 or art3 > 0 and self.liste[c1 + 1][2] == "Verbe":
                        del self.liste[c1 + 1][2]
                        
                    c2+=1
                    break
                    
            c1 += 1
            c2 = 0
        










