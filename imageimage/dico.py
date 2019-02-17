from internet import *
from path import *
from doc_question import *
from image import *

#                                   FINI TOUS LES PETITS TRUKS
#                                   gros truk ouais



class Dico:

    def question(self):
        print("le chien noir est à droite du chat roux")
        self.oInput = input("rentre une phrase simple")
        
        liste_self_oInput = []
        liste_self_oInput.append(str(self.oInput))
        fichier.ecriture_phrase(self, liste_self_oInput)


    def dictionnaire(self):

        self.liste_input = [[],[],[],[],[],[],[],[],[],[],[],[],
                            [],[],[],[],[],[],[],[]]

        self.liste_mot_dico = []
        self.liste_verbe = []
        self.liste_prenom = []
        
        liste_ecriture = []

        self.liste_traitement = [[],[],[],[],[],[],[],[],[],[],[],[],
                                [],[],[],[],[],[],[],[]]


        self.liste_image_phase1 = []

        self.compteur1 = 0
        c = 0
        a = ""
        for i in self.oInput:
            if i == " ":
                self.compteur1 += 1
            else:
                self.liste_input[self.compteur1].append(i)

        for i in self.liste_input:
            if i == []:
                pass
            else:
                i = "".join(i)
                print(i)
                
                internet.search(self, i, self.liste_mot_dico)
                
                internet.search_verbe(self, DICO_VERBE, i,
                                        self.liste_verbe, "requete.py", "w", "r")
    
                print(self.liste_mot_dico)
                print(self.liste_verbe)
                
                internet.prenom(self, i, self.liste_prenom)
                
                liste_i = []
                liste_i.append(i)
                
                self.liste_traitement[c].append(i)
                try:
                    self.liste_traitement[c].append(self.liste_mot_dico[0])
                except:
                    pass
                
                self.liste_traitement[c].append(self.liste_verbe[0])
                self.liste_traitement[c].append(self.liste_prenom[0])

                
                    
                liste2 = []
                if self.liste_verbe[0] == "Verbe":
                    internet.temps_verbe(self, i, liste2)
                    Dico.temps(self)
                    for i in self.temps :
                        try:
                            if i == liste2[0]:
                                a = True
                                liste2 = []
                        except:
                            pass

                c += 1
                self.liste1 = []
                liste_i = []
                self.liste_mot_dico = []
                self.liste_verbe = []
                self.liste_prenom = []
                
                print("\n")
        print(self.liste_traitement)
        
        self.liste_image = []


        #passé
        if a == True :
            Dico.nom_adj(self, self.liste_image)
            
        else:
            Dico.nom_adj(self, self.liste_image)
            

        print(self.liste_image)
        




    def nom_adj(self, liste1):
        
        c5 = 0
        liste = []
        self.liste1 = liste1
        for i in self.liste_traitement:
            if i == []:
                pass
            else:
                liste.append(self.liste_traitement[c5][1])
            c5 += 1


        c = 0
        c6 = 0
        for i in liste:
            #tu peux factoriser tout ca
            try:
                if liste[c] == "Nom commun" and liste[c + 1] == "Adjectif":
                    print("oui",liste[c],liste[c + 1])
                    internet.recherche_image(self, self.liste_traitement[c][0],
                                             self.liste_traitement[c + 1][0], self.liste1)
                    image.image_seule(self, self.liste_image[c6], self.liste1)
                    c6 += 1
                    
            except:
                pass


            try:    
                if liste[c] == "Nom commun" and liste[c + 2] == "Adjectif":
                    print("ui",liste[c],liste[c + 2])
                    internet.recherche_image(self, self.liste_traitement[c][0],
                                             self.liste_traitement[c + 2][0], self.liste1)
                    image.image_seule(self, self.liste_image[c6], self.liste1)
                    c6 += 1
                   
            except:
                pass

            
            try:    
                if liste[c] == "Nom commun":
                    print("ouais", liste[c])
                    internet.recherche_image_phrase(self, self.liste_traitement[c][0], self.liste1)
                    image.image_seule(self, self.liste_image[c6], self.liste1)
                    c6 += 1
                    #inclusion exclusion exlu 1 image
                    
            except:
                pass
           
            
            finally:
                c+=1
                

    def pos_fonction(self):

        
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
                            
            c+=1

        print(self.liste_image_phase1)


    #fini le truk wikipédia ex voiture -> se diriger vers tous les liens et faire le truk

    
    def prenom_premier(self, liste):
        
        c = 0
        self.liste = liste
        
        for i in self.liste:
            
            if self.liste[c][3] == "prénom" and self.liste[c][1] == "Article défini"\
               or self.liste[c][1] == "Article indéfini":
                print("pas prénom")
                
            elif self.liste[c][3] == "prénom" and self.liste[c+1][1] == "Nom commun":
                print("pas prénom")

            elif self.liste[c][3] == "prénom" and self.liste[c+1][2] == "Verbe":
                print("prenom")
                
            elif self.liste[c][3] == "prénom" and self.liste[c-1][2] == "Préposition":
                print("prénom")
                
            c+=1

        #a plus remplir vérifier les conditions ou c un prenom ou pas
        #le jean est bleu ca marche dans les deux sens...


    def condition_article(self):

        #Article + Verbe ex le crayon (correction auto)
        #si y'a un article alors le prochain truk ne peux pas etre un verbe
        
        c1 = 0
        c2 = 0
        for i in liste:
            if i == []:
                pass
            else:
                for i in range(len(liste[c1])):
                    art = str(liste[c1]).find(str("Article"))
                    art1 = str(liste[c1]).find(str("article"))
                    if art > 0 or art1 > 0 and liste[c1 + 1][2] == "Verbe":
                        del liste[c1 + 1][2]
                    print(liste[c1][0], liste[c1][1])
                    c2+=1
                    break

            c1 += 1
            c2 = 0

        print(liste)




    def nom_commun(self, liste):
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

                    



       
    def temps(self):

        self.indice_temps = ["hier","passé","demain","après demain","aujourd'hui"]
        self.temps = ["Passé","Imparfait"]


        #sert pour la final condition a == True ou pas True
        




    def taille(self):
        pass
        #le petit chien parle avec le gros chat
            
    def maisouestdoncornicar(self):
        liste = ["mais","ou","et","donc","or","ni","car"]

    def adverbe(self):
        pass
        #alors marque un résultat ou une agression
    
    def préposition(self):
        pass
        #apres marque la visualisation du futur ou avant apres
        #apres jte dis jmen balec, apres avoir fais ca

        

    def verbe(self):
        pass
        #action ici
        #self.phrase -> article nom commun adj et ca arrange le truk avec un seul nom commun
        # si y'a une phrase longue coller les 2 images de 4 images


           
