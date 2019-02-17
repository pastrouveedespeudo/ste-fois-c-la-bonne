from mémoire import *
from syntaxe import *
from outils_internet import *
from raisonement import *
from grammaire import *
from imv import *


class main:

    def importation(self):
        mémoire.position(self)

    def debut(self):
        print("salut")

    def initialisation_phrase(self, phrase):

        self.phrase = phrase
        self.oInput = input("->")

        
    def decoupage_oInput(self):
        mémoire.liste(self)

        c = 0
        for i in self.oInput:
            for j in i :
                if j == " ":
                    c+=1
  
                elif j == "." or j == "?"\
                     or j == "!" or j == ","\
                     or j == "'"or j == ":"or\
                     j =="?!":
                    
                    c+=1
                    self.liste_input[c].append(j)
  
                else:
                    self.liste_input[c].append(j)
            
        c1 = 0
        for i in self.liste_input:
            if i == []:
                pass
            elif i == ["."] or i == [","]\
                 or i == ["!"] or i == ["?"]\
                 or i == ["'"] or i == [":"]  or i == ["?!"] :
                c1+=1
                self.liste_traitement[c1].append(i)
                c1+=1
            else:
                self.liste_traitement[c1].append("".join(i))

    def mise_en_liste_oinput(self):


        c = 0
        for i in self.liste_traitement:
            for j in i :
                self.liste_oInput_decoupage[c].append(j)
                c+=1

    
    def mise_point_si_pas(self):
        self.liste_oInput.append(self.oInput)
        #expliquer les intonations
        
        c = 0
  
        for i in self.liste_traitement:
            if i == []:
                pass
            else:

                if self.liste_traitement[c] == [["."]]:
                    c+=1
                    
                elif self.liste_traitement[c+1] == [["."]] or self.liste_traitement[c+1] == [[","]]\
                     or self.liste_traitement[c+1] == [["?"]] or self.liste_traitement[c+1] == [["!"]]\
                     or self.liste_traitement[c+1] == [[":"]] or self.liste_traitement[c+1] == [["'"]]\
                     or self.liste_traitement[c+1] == [["?!"]]:
                    c+=2
                    
                
                elif self.liste_traitement[c+1] == [["."]]:
                    c+=1
                    
                elif self.liste_traitement[c+1] != [["."]]:
                    self.liste_traitement[c+1].append(["."])
                    c+=1
                    break



     
       
       
    def premiere_explication(self):
        mémoire.explication(self)
        syntaxe.lang_ponctuation(self, self.liste_traitement, self.explication)
        

        
    def recherche_syntaxe(self):

  
        c = 0
        for j in self.liste_traitement:
            for i in j:
                if i == [] or i == [["."]]:
                    pass
                else:
                    outils_internet.search(self, i, self.liste_mot_dico)
                    try:
                        self.syntaxe[c].append(self.liste_mot_dico[0])
                    except:
                        pass
                    finally:
                        self.syntaxe_all.append(self.liste_mot_dico)
                        self.liste_mot_dico = []
                        c+=1

                        
    def compteur_creation_dossier(self):
        self.compteur_dossier = 0
        for i in self.liste_traitement:
            if i == [] or i == "":
                pass
            else:
                self.compteur_dossier+=1
                
        outils_fichier.dossier_creer_fonction_phrase(self, self.compteur_dossier)

    def recherche_verbe(self):
    #expliquer la notion de temps par exemple
        
        c = 0
        for j in self.liste_traitement:
            for i in j:
                if i == [] or i == [["."]]:
                    pass
                else:
    
                    outils_internet.search_verbe(self, DICO_VERBE, i,
                                                 self.liste_verbe, "requete.py", "w", "r")
                    self.verbe[c].append(self.liste_verbe[0])
                    
                    if self.liste_verbe[0] == "Verbe":
                        outils_internet.temps_verbe(self, i, self.temps_verbe)
                        
                    c+=1
                    self.liste_verbe = []
           
        
 
    def recherche_prenom(self):

        c = 0
        for j in self.liste_traitement:
            for i in j:
                if i == [] or i == [["."]]:
                    pass
                else:
                    outils_internet.prenom(self, i, self.liste_prenom[c])
                c+=1


    def recherche_genre(self):

        c = 0
        self.liste_fem = []
        self.liste_masc = []
        for j in self.liste_traitement:
            for i in j:
                if i == [] or i == [["."]]:
                    pass
                else:
                    
                    outils_internet.fem_masc(self, i, self.liste_fem, self.liste_masc)
                    try:
                        self.liste_genre[c].append(self.liste_fem[0])
                        self.liste_fem = []
                        self.liste_masc = []
                    except:
                        pass
                    try:
                        self.liste_genre[c].append(self.liste_masc[0])
                        self.liste_fem = []
                        self.liste_masc = []
                    except:
                        pass
                    finally:
                        c+=1

                    
    def cherche_propriete(self):
        
        c = 0
        for j in self.liste_traitement:
            for i in j:
                if i == [] or i == [["."]]:
                    pass
                else:
                    
                    if self.syntaxe[c] == ["Nom commun"] :

                        raisonement.propriété(self, self.liste_traitement, self.liste_trait, i)
                        raisonement.propriété2(self, self.liste_trait)
                        try:
                            self.liste_propriete[c].append(self.liste_trait[-2])
                            self.liste_propriete[c].append(self.liste_trait[-1])
                        except:
                            pass
                    else:
                        pass
                
                c+=1

                
    def regle(self):

        syntaxe.prenom_premier(self, self.syntaxe, self.liste_prenom)
        syntaxe.condition_article(self, self.syntaxe, self.verbe)
        
        grammaire.lang_pronom(self, self.syntaxe, self.liste_traitement,
                               self.explication1, self.liste_oInput_decoupage, self.liste_propriete,
                               self.liste_oInput, self.liste_pronom, self.liste_genre)




    def image(self):
        a = int(self.compteur_dossier/2)
        
        imv.image_nom_commun_adj(self, self.syntaxe, self.verbe, self.liste_oInput_decoupage, a)
        imv.image_verbe(self, self.verbe, a)

    def position_image(self):
        
        imv.pos_nom_commun(self, self.liste_indication_pos, self.liste_oInput_decoupage)


    def affichage(self):
        pass
        #print(self.compteur_dossier/2)
        #print(self.liste_oInput_decoupage)
        #print(self.liste_oInput)    
        #print(self.liste_traitement)
        #print(self.explication[:-1])
        #print(self.syntaxe)
        #print(self.syntaxe_all)

        #print(self.verbe)
        #print(self.temps_verbe)

        #print(self.liste_prenom)

        #print(self.liste_genre)
        #print(self.liste_propriete)
        #print(self.liste_pronom)
        #print(self.explication1)
        
    def suppression_dossier(self):
        try:
            outils_fichier.suppression_pour_nouvelle_phrase(self)
        except:
            pass


if __name__ == "__main__":

    aquaman = main()
    aquaman.importation()
    aquaman.debut()

    ocontinuer = True
    while ocontinuer :
        
        aquaman.initialisation_phrase("")
        aquaman.decoupage_oInput()
        aquaman.mise_en_liste_oinput()
        aquaman.mise_point_si_pas()
        
        aquaman.premiere_explication()
        
        aquaman.recherche_syntaxe()
        aquaman.compteur_creation_dossier()
        
        #aquaman.recherche_verbe()
        #aquaman.recherche_prenom()
        #aquaman.recherche_genre()
        #aquaman.cherche_propriete()

        aquaman.regle()
        
        aquaman.image()
        aquaman.position_image()
        
        aquaman.affichage()
        

        aquaman.suppression_dossier()





    
#demande toi si le point dans la liste ou dehors pour le stockage...
