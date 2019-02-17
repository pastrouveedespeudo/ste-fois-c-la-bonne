
from path import *
import os
import shutil

class outils_fichier:

    def requete_py(self, fichier, element, liste):

        self.fichier = fichier
        self.element = element
        self.liste = liste
        
        with open(str(self.fichier),"w", errors = "ignore") as file:
            file.write(str(self.element))
                        
        with open(self.fichier,"r") as file2:
            b = file2.read()

        self.liste.append(b)


    def dossier_creer_fonction_phrase(self, compteur):
        self.compteur = compteur

        b = int(self.compteur / 2)
        for i in range(b):
            a = str(i)
            os.chdir(r"C:\Users\jeanbaptiste\ste fois c la bonne\imageimage1.3\image")
            os.mkdir(str(a))

    def suppression_pour_nouvelle_phrase(self):

        os.chdir(r"C:\Users\jeanbaptiste\ste fois c la bonne\imageimage1.3\image")
        liste = os.listdir()
        for i in liste:
            shutil.rmtree(i)


    def image(self, element, compteur):
        self.compteur = compteur
        self.element = element
        path_image = r"C:\Users\jeanbaptiste\ste fois c la bonne\imageimage1.3\image\{}".format(self.compteur)
        shutil.move(self.element, path_image)

    def image_in_dossier(self, compteur):
        self.compteur = compteur

        os.chdir(r"C:\Users\jeanbaptiste\ste fois c la bonne\imageimage1.3\image\{}".format(self.compteur))
        liste = os.listdir()
        print(liste)
     





























