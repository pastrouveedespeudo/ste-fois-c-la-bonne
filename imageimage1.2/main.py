from outils_fichier import *
from outils_internet import *
from outils_image import *
from outils_main import *

from mémoire import *

from syntaxe import *
from grammaire import *

from imv import *
from raisonement import *
from path import *



#objetctif la expliquer chaques phrase

class main:

    def question(self):

        #les apostrophes les transformer
        #reflechir sur les pronoms
        print("Sacha, il aime les livres. La dernière fois il a acheté un livre qui parle\
              qui parlait des animaux, ce dernier était rouge. Pierre lui a volé\
              Sacha grave vénére lui a pété les genoux. Il était 10 heures du matin")
        #explique phrase possible ? impossible? image
        print("Bonjour")
        self.oInput = input("Répond !")

        liste_self_oInput = []
        liste_self_oInput.append(str(self.oInput))
        outils_fichier.ecriture_phrase(self, liste_self_oInput)



    def liste(self):
        mémoire.liste(self)


    def main(self):

        a = ""
        c = 0
        self.compteur1 = 0
        
        for i in self.oInput:
            if i == " ":
                self.compteur1 += 1
            else:
                self.liste_input[self.compteur1].append(i)
                
        
        syntaxe.lang_ponctuation(self, self.liste_input, self.explication)
        syntaxe.phrase(self, self.liste_input, self.ponctuation)
        
        d = 0
        b = 0
        for i in self.ponctuation:
            if i == []:
                pass
            elif self.ponctuation[-1] and self.ponctuation[-2] == ["."]:
                del self.ponctuation[-1]
                break
            
        for i in self.ponctuation:
            if i == ["."]:
                    d += 1
                    
        for i in self.ponctuation:
            if i == []:
                pass
            else:
                self.ponctuation2.append(i)


        c = 0
        d = 0
        b = 0
        self.phrase = [[],[],[],[],[],[]]
        
        for i in self.ponctuation2:
            if i == ["."]:
                c += 1
                self.phrase[c].append(i)
                c += 1
            else:
                self.phrase[c].append(i)
        for i in self.phrase:
            for j in i:
                if j == ["."]:
                    d+=2


        self.b = 0    
        c = 0
    

        for j in self.phrase:
            for i in j:
                if i == [] or i == [""] or i == [" "]or i == [ ]:
                    pass
                else:
                    i = "".join(i)
                    print(i)
                    
                    self.liste_traitement[c].append(i)

                    
                    outils_internet.search(self, i, self.liste_mot_dico)
                    try:
                        self.liste_traitement[c].append(self.liste_mot_dico[0])
                    except:
                        pass

                    
                    outils_internet.search_verbe(self, DICO_VERBE, i,
                                                 self.liste_verbe, "requete.py", "w", "r")
                    self.liste_traitement[c].append(self.liste_verbe[0])


                    outils_internet.prenom(self, i, self.liste_prenom)
                    self.liste_traitement[c].append(self.liste_prenom[0])


                    outils_internet.fem_masc(self, i, self.liste_fem, self.liste_masc)
                    try:
                        self.liste_traitement[c].append(self.liste_fem[0])
                    except:
                        pass
                    try:
                        self.liste_traitement[c].append(self.liste_masc[0])    
                    except:
                        pass


                    if self.liste_traitement[c][1] == "Nom commun" :
                        raisonement.propriété(self, self.liste_traitement, self.liste_trait, i)
                        raisonement.propriété2(self, self.liste_trait)
                        try:
                            self.liste_traitement[c].append(self.liste_trait[-2])
                            self.liste_traitement[c].append(self.liste_trait[-1])
                        except:
                            print("nan")
                    else:
                        pass

                    
                    if self.liste_verbe[0] == "Verbe":
                        outils_internet.temps_verbe(self, i, self.liste_verbe2)
                    
                    c+=1
                    self.b +=1

                    print(self.liste_mot_dico)
                    print(self.liste_verbe)
                    print(self.liste_prenom)
                    print("masc: ", self.liste_masc)
                    print("fem : ", self.liste_fem)
                    print(self.liste_trait)
                    print(self.liste_verbe2)
                    print("\n")
                    
                self.liste_mot_dico = []
                self.liste_verbe = []
                self.liste_prenom = []
                self.liste_fem = []
                self.liste_masc = []
                self.liste_trait = []
                
            syntaxe.prenom_premier(self, self.liste_traitement)         
            syntaxe.condition_article(self, self.liste_traitement)
            grammaire.lang_pronom(self, self.liste_traitement, self.liste_pronom,
                                  self.explication1)


            print(self.liste_pronom)                            
        print(self.liste_traitement)
            



        



    def nettoyage_liste_trait(self):
        outils_main.pos_liste_traitement(self, self.liste_traitement, self.liste_indication_pos,
                                         self.compteur1)


    def phrase_image(self):

        c = 0
        d = 0
        try:
            for i in self.liste_traitement:
                if self.liste_traitement[c][0] == ".":
                    d+=1
                self.liste_traitement3[d].append(self.liste_traitement[c])
                c+=1
        except:
            pass
  
        f = 0
        for i in self.liste_traitement3:
            if i == [] or i == [""] or i == [" "] or i == [ ]:
                pass
            else:
                #print(self.liste_traitement3[f])
                a = ""
                c = 0
                imv.image_nom_commun_adj(self, self.liste_image, self.liste_traitement3[f])
                #print(self.liste_image)
                imv.image_verbe(self, self.liste_traitement3[f], self.liste_verbe_image)
                #print(self.liste_verbe_image)
                
                try:
                    imv.pos_nom_commun(self, self.liste_indication_pos, self.liste_traitement3[f],
                                        self.compteur1, self.liste_image, self.liste_image_phase1)
                                   
                    syntaxe.maisouestdoncornicar(self, self.liste_traitement,
                                                 self.liste_image, self.liste_image,
                                                 self.liste_image_phase1)
                except:
                    pass

                #print(self.liste_image_phase1)
                #print(self.liste_image_phase2)

                self.liste_verbe3 = self.liste_verbe2
                for i in self.temps :
                    try:
                        if i == self.liste_verbe2[0]:
                            a = True
                    except:
                        pass
                    try:
                        del self.liste_verbe2[0]
                    except:
                        pass
                    
                #print(a)
                    
                if a == True and self.liste_image_phase1 != []:
                    #print("oui")
                    outils_image.couleur_passé(self, "image.png")
                    try:
                        outils_image.couleur_passé(self, self.liste_verbe_image[0])
                    except:
                        pass
                    
                elif a != True and self.liste_image_phase1 != []:
                    #print("ouais")
                    outils_image.couleur_pas_passé(self, "image.png")
                    try:
                        outils_image.couleur_pas_passé(self, self.liste_verbe_image[0])
                    except:
                        pass
                    
                    
                else:
                    #print("ouioui")
                    d = 0
                    for i in self.liste_image:
                        try:
                            outils_image.couleur_pas_passé(self, self.liste_image[d])
                    
                            outils_image.couleur_pas_passé(self, self.liste_verbe_image[0])
                        except:
                            pass
                        finally:
                            d+=1
                    
                    


                self.liste_image = []
                self.liste_image_phase1 = []
                self.liste_verbe_image = []
                #print(self.liste_traitement)


                f+=1


    def explication_liste(self):


        print("\n")
        print(self.liste_traitement3)
        outils_main.ajout_verbe(self, self.liste_verbe3, self.b)
        raisonement.affichage(self, self.liste_traitement3, self.liste_verbe3)
        #est ce possible que le chat mange le chien?
        #raisonement             et mettre langage.affi dans raisonement.affi
                    #aussi langage c pas encore



        #je pense que oui car
        #je pense que non car

        #notion de chaine alimentaire
        #notion de superirité

        #le chien peut etre mort

        #une baleine ne peut pas se battre contre un lion


    def langage(self):
        print(self.explication)
        print(self.explication1)
        #si debut commence par politesse
            #arbre
        #sinon
            #arbre


if __name__ == "__main__":

    aquaman = main()
    aquaman.question()
    aquaman.liste()
    aquaman.main()
    aquaman.nettoyage_liste_trait()
    aquaman.phrase_image()
    aquaman.explication_liste()



#comment reconnait t-on un chat ?
#est - ce une chaise ?







    
