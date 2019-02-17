from path import *
from fichier import *
from internet import *
from dphrase_condition import *
from propriete import *
from image import *
from langage import *



class Dico:

    def question(self):
        print("le chien noir est à droite du chat roux")
        print("jean boit du thé")
        print("le jean noir")
        print("le crayon vert")
        print("le chien à gauche du chat")
        print("le chien était à gauche du chat")
        print("la voiture à gauche du chat")
        print("le chien et le chat")
        print("le chien et le chat, ils vont à la piscine.")
        print("le chien ce dernier, il")
        print("chat chien, ce dernier il")
        print("le requin et le dauphin")
        print("le requin et le dauphin vont au marché")
        print("car super u et intermaché ca marche pas ni les apostrophes")

        
        self.oInput = input("rentre une phrase simple")

        liste_self_oInput = []
        liste_self_oInput.append(str(self.oInput))
        fichier.ecriture_phrase(self, liste_self_oInput)


    def dictionnaire(self):


        #on définie
        self.liste_input = [[],[],[],[],[],[],[],[],[],[],[],[],
                            [],[],[],[],[],[],[],[]]

        self.liste_mot_dico = []
        self.liste_verbe = []
        self.liste_prenom = []
        
        self.liste_image = []
        self.liste_image2 = []
        
        liste_ecriture = []

        self.liste_traitement = [[],[],[],[],[],[],[],[],[],[],[],[],
                                 [],[],[],[],[],[],[],[],
                                 [],[],[],[],[],[],[],[],[],[],[],[],
                                 [],[],[],[],[],[],[],[],
                                 [],[],[],[],[],[],[],[],[],[],[],[],
                                 [],[],[],[],[],[],[],[]]

        self.liste_image_phase1 = []

                
        self.liste_appuie_vivant = []
        self.liste_appuie_non_vivant = []

        self.liste_appuie_vole = []
        self.liste_appuie_vole_meca = []

        self.liste_appuie_eau = []
        
        self.explication = []
        self.explication1 = []


        #ici mettre le truk a chaque ponctuation
        self.ponctuation = [[],[],[],[],[],[],[],[],[],[],[],[],
                            [],[],[],[],[],[],[],[],
                            [],[],[],[],[],[],[],[],[],[],[],[],
                            [],[],[],[],[],[],[],[],
                            [],[],[],[],[],[],[],[],[],[],[],[],
                            [],[],[],[],[],[],[],[]]



        self.liste_fem = []
        self.liste_masc = []

        
        
        self.compteur1 = 0
        c = 0
        a = ""
  









        #on nettoie 
        for i in self.oInput:
            if i == " ":
                self.compteur1 += 1
            else:
                self.liste_input[self.compteur1].append(i)
       
        print("\n")
        langage.lang_ponctuation(self, self.liste_input, self.explication)
        print("\n")
        
            

        for i in self.liste_input:
            if i == []:
                pass
            else:
                i = "".join(i)
                print(i)





                

                #on cherche
                internet.search(self, i, self.liste_mot_dico)
                
                internet.search_verbe(self, DICO_VERBE, i,
                                        self.liste_verbe, "requete.py", "w", "r")

                internet.prenom(self, i, self.liste_prenom)

                internet.fem_masc(self, i, self.liste_fem, self.liste_masc)





                

        

                #on ajoute
                liste_i = []
                liste_i.append(i)
                
                self.liste_traitement[c].append(i)
                try:
                    self.liste_traitement[c].append(self.liste_mot_dico[0])
                except:
                    pass
                
                self.liste_traitement[c].append(self.liste_verbe[0])
                


                try:
                    self.liste_traitement[c].append(self.liste_fem[0])
                except:
                    print("nan")
                try:
                    self.liste_traitement[c].append(self.liste_masc[0])   
                
                except:
                    print("nan")


                self.liste_traitement[c].append(self.liste_prenom[0])



                #on valide condition
                liste2 = []
                self.temps = ["Passé","Imparfait"]
                self.indice_temps = ["hier","passé","demain",
                                     "après demain","aujourd'hui"]
                
                if self.liste_verbe[0] == "Verbe":
                    internet.temps_verbe(self, i, liste2)
                    for i in self.temps :
                        try:
                            if i == liste2[0]:
                                a = True
                        except:
                            pass








                #on affiche
                print(self.liste_mot_dico)
                print(self.liste_verbe)
                print(liste2)
                print(self.liste_prenom)
                print("masc: ", self.liste_masc)
                print("fem : ", self.liste_fem)

            







                #on efface
                c += 1
                
                self.liste_mot_dico = []
                self.liste_verbe = []
                self.liste_prenom = []
                liste2 = []
                self.liste_fem = []
                self.liste_masc = []
                print("\n")

        






        #on traite  
        phrase.prenom_premier(self, self.liste_traitement)
        phrase.condition_article(self, self.liste_traitement)
        phrase.nom_adj(self, self.liste_image, self.liste_traitement)
        phrase.pos_fonction(self)
        #phrase.proprio(self, self.liste_traitement)






        #liste phase 2
        liste_pronom = []




        #langage 
        langage.lang_pronom(self, self.liste_traitement, liste_pronom,
                            self.explication1)
        
        
        











        #on affiche les test
        print(self.liste_traitement)
        #print(self.liste_image)
        #print(self.liste_image_phase1)
        #print(a)
        print("pronom pris en compte dans la phrase", liste_pronom)




        #on preeatblis regle affichage
        phrase.maisouestdoncornicar(self, self.liste_traitement,
                                   self.liste_image,
                                   self.liste_image)





        #on affiche image
        if a == True and self.liste_image_phase1 != []:
            image.couleur_passé(self, "image.png")
            

        elif a != True and self.liste_image_phase1 != []:
            image.couleur_pas_passé(self, "image.png")

        elif a == True and self.liste_image != [] :
            image.couleur_passé(self, "image.png")


        for i in self.liste_image[1:]:
            print(i)

        try:
            for i in self.liste_image[2:]:
                image.couleur_pas_passé(self, i)
        except:
            pass










        
        #on explique
        print(self.explication)
        print(self.explication1)

















