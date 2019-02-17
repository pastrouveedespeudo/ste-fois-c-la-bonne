# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from path import *
from outils_fichier import *
import urllib.request
import json
from PIL import Image
from outils_fichier import *
from path import *

class outils_internet: 

    def search(self, mot, liste1):

        self.mot = mot
        
        self.liste1 = liste1
        self.liste = []

        path = DICO_DEF.format(self.mot)
        
        requete = requests.get(path)
        page = requete.content
        
        soup = BeautifulSoup(page, "html.parser")      
        propriete = soup.find_all("div", {"class":"defbox"})
        
        for i in propriete:
            outils_fichier.requete_py(self, "requete.py", i, self.liste)
            pos1 = str(self.liste).find("<span>") + 3
            pos2 = str(self.liste).find("</span>") - 3
            a = self.liste[0][pos1:pos2]
            self.liste = []
            
            autre_def = str(i).find("Autre définition")
            autre_def1 = str(i).find("Aucun mot trouvé")

            if autre_def > 0:
                pass
            
            elif autre_def1 > 0:
                pass
            
            elif a == "Définitions corespondante à votre recherche":
                mot_sing = mot[:-1]
                mot_trouvé = str(propriete).find(str(mot_sing))
                mot_fem_plur = mot[:-2]
                mot_fem_plur_trouvé = str(propriete).find(str(mot_fem_plur))
                
                if mot_trouvé > 0:                                  #sing
                    path_sing = DICO_DEF.format(str(mot_sing))
                    requete = requests.get(path_sing)
                    page = requete.content
                    soup = BeautifulSoup(page, "html.parser")      
                    propriete = soup.find_all("div", {"class":"defbox"})

                    for i in propriete:
                        outils_fichier.requete_py(self, "requete.py", i, self.liste)
                        pos1 = str(self.liste).find("<span>") + 3
                        pos2 = str(self.liste).find("</span>") - 3
                        a = self.liste[0][pos1:pos2]
                        mot_trouvé2 = str(a).find(str("Autre définition"))
                                                                                    #plur fem
                        if a == "Définitions corespondante à votre recherche"\
                           and mot_fem_plur_trouvé > 0:
                            path_fem = DICO_DEF.format(str(mot_fem_plur))
                            requete = requests.get(path_fem)
                            page = requete.content
                            soup = BeautifulSoup(page, "html.parser")      
                            propriete = soup.find_all("div", {"class":"defbox"})

                            for i in propriete:
                                
                                outils_fichier.requete_py(self, "requete.py", i, self.liste)
                                pos1 = str(self.liste).find("<span>") + 3
                                pos2 = str(self.liste).find("</span>") - 3
                                a = self.liste[0][pos1:pos2]
                                if a == "Définitions corespondante à votre recherche":
                                    pass
                                else:
                                    self.liste1.append(a)
                                self.liste = []
                                
                        elif mot_trouvé2 > 0:
                            pass
                        else:
                            self.liste1.append(a)
                            self.liste = []
                    
                        
            else:
                self.liste1.append(a)

        self.liste1 = set(self.liste1)


    def search_verbe(self,path, recherche, liste, fichier, mode, mode2):
        
        self.path = path 
        self.recherche = recherche
        self.liste = liste
        self.fichier = fichier
        self.mode = mode
        self.mode2 = mode2

        path_verbe = DICO_VERBE.format(str(self.recherche))
        requete = requests.get(path_verbe)
        page = requete.content
        soup = BeautifulSoup(page, "html.parser")      
        propriete = soup.find("blockquote")

        with open(self.fichier, self.mode) as file:
            file.write(str(propriete))
                    
        with open(self.fichier, self.mode2) as file2:
            b = file2.read()

        pos1 = str(b).find("VERBE")
        
        if pos1 > 0:
            self.liste.append("Verbe")
        
        else:
            self.liste.append("None")


    def temps_verbe(self, recherche, liste3):

        self.recherche = recherche

        liste = []
        liste2 = []
        self.liste3 = liste3
        path_verbe = DICO_VERBE.format(str(self.recherche))
        requete = requests.get(path_verbe)
        page = requete.content
        soup = BeautifulSoup(page, "html.parser")      
        propriete = soup.find_all("table")

        with open("requete.py", "w") as file:
            file.write(str(propriete))
                    
        with open("requete.py", "r") as file2:
            b = file2.read()
        liste.append(b)
        
        a = str(liste).find(str(str(self.recherche)))
        if a > 0:
            liste2.append(liste[0][a - 600:a+20])
            b = str(liste2).find(str(str('<a href="#">')))
            liste3 = liste2[0][b+2:-250]

            c = str(liste3).find(str('</a>'))
            d = str(liste3).find(str('#">'))
            self.liste3.append(liste3[d + 3:c])



        
    def prenom(self, nom, liste):

        self.nom = nom
        self.liste = liste
        
        path = "https://www.prenoms.com/prenom/{}.html".format(self.nom)
        requete = requests.get(path)
        page = requete.content
        soup = BeautifulSoup(page, "html.parser")  
        propriete = soup.find("title")
        
        a = str(propriete).find("Trouvez un prénom")
        if a < 0:
            #print("prenom")
            self.liste.append("prénom")
        else:
            #print("pas prénom")
            self.liste.append("pas prénom")



    def fem_masc(self, mot, liste_fem, liste_masc):
    
        self.mot = mot
        self.liste_fem = liste_fem
        self.liste_masc = liste_masc
        self.liste = []
        
        path = "https://www.larousse.fr/dictionnaires/francais/{}"
        recherche = path.format(self.mot)

        requete = requests.get(recherche)
        page = requete.content
        soup = BeautifulSoup(page, "html.parser")  
        for p in soup.find_all("p"):
            self.liste.append(p.text)

        a = str(self.liste).find("nom masculin")
        b = str(self.liste).find("nom féminin")
        if a > 0:
            self.liste_masc.append("nom masculin")
            
        elif b > 0:
            self.liste_fem.append("nom féminin")
  
        else:
             self.liste_masc.append("None")
            

    
    def recherche_propri(self, recherche, mot_liste,
                         liste, liste_appuie, liste_appuie_carac):
        
        #attention wikipedia ex : https://fr.wikipedia.org/wiki/Voiture
            #plusieurs choix ex voiture


        #si Cette page d’homonymie
        #répertorie les différents sujets et articles partageant un même nom.
                    #fais le

        self.recherche = recherche
        self.mot_liste = mot_liste
        self.liste_appuie = liste_appuie
        self.liste_appuie_carac = liste_appuie_carac
        self.liste = liste
        b = ""
        self.one = "https://fr.wikipedia.org/wiki/{}".format(self.recherche)
        
        requete = requests.get(self.one)
        page = requete.content
        soup = BeautifulSoup(page, "html.parser")  
        for p in soup.find_all("p"):
            self.liste.append(p.text)
        
        c = 0
        
        #print(self.recherche)
        for i in self.mot_liste:
            
            a = str(self.liste).find(str(i))
            if a > 0 :
                c += 1
                #print(i,a)
                b = True
                self.liste_appuie_carac.append(i)
                
                
        self.liste = []
        
        if b == True:
            self.liste_appuie.append(self.recherche)

        #print(self.liste_appuie)
        #print(self.liste_appuie_carac)
        #print("\n")


    def recherche_image(self, mot_cle, mot_cle1, compteur):

        self.compteur = compteur        
        self.mot_cle = mot_cle
        self.mot_cle1 = mot_cle1

        liste = []
        self.liste1 = liste1
        
        path =  "https://www.google.co.in/search?q={0}+{1}&source=lnms&tbm=isch"
        path1 = path.format(self.mot_cle, self.mot_cle1)
        requete = requests.get(path1)
        page = requete.content
        soup = BeautifulSoup(page, "html.parser")  
        propriete = soup.find_all("img")
        
        with open("requete.py", "w") as file:
            file.write(str(propriete))
                    
        with open("requete.py", "r") as file2:
            b = file2.read()
        liste.append(b)


        for i in range(1):
            
            a = str(liste).find(str("src"))
            b = str(liste).find(str('" width='))
            
            url = liste[0][a+2:b-3]
            image = str("image"+str(self.mot_cle)+str(self.mot_cle1)+".jpg")

            liste[0] = liste[0][b:-3]

            urllib.request.urlretrieve(str(url), image)
            outils_fichier.image(self, image, self.compteur)
            
        

    def recherche_image_phrase(self, phrase, compteur):

        self.compteur = compteur 
        self.phrase = phrase

        liste = []

        
        path =  "https://www.google.co.in/search?q={0}&source=lnms&tbm=isch"
        path1 = path.format(self.phrase)
        requete = requests.get(path1)
        page = requete.content
        soup = BeautifulSoup(page, "html.parser")  
        propriete = soup.find_all("img")
        
        with open("requete.py", "w") as file:
            file.write(str(propriete))
                    
        with open("requete.py", "r") as file2:
            b = file2.read()
        liste.append(b)


        for i in range(1):
            a = str(liste).find(str("src"))
            b = str(liste).find(str('" width='))
            
            url = liste[0][a+2:b-3]
            image = str("image"+str(phrase)+".jpg")

            liste[0] = liste[0][b:-3]

            urllib.request.urlretrieve(str(url), image)
            outils_fichier.image(self, image, self.compteur)



    def recherche_image_verbe(self, mot_cle, compteur):
        #recherche_image_verbe(self, i, self.liste_verbe_image)
        
        self.mot_cle = mot_cle
        self.compteur = compteur

        liste = []
        self.liste1 = liste1
        
        path =  "https://www.google.co.in/search?q={0}&source=lnms&tbm=isch"
        path1 = path.format(self.mot_cle)
        requete = requests.get(path1)
        page = requete.content
        soup = BeautifulSoup(page, "html.parser")  
        propriete = soup.find_all("img")
        
        with open("requete.py", "w") as file:
            file.write(str(propriete))
                    
        with open("requete.py", "r") as file2:
            b = file2.read()
        liste.append(b)


        for i in range(1):
            
            a = str(liste).find(str("src"))
            b = str(liste).find(str('" width='))
            
            url = liste[0][a+2:b-3]
            image = str(self.mot_cle+".jpg")

            liste[0] = liste[0][b:-3]

            urllib.request.urlretrieve(str(url), image)
            outils_fichier.image(self, image, self.compteur)
 


























