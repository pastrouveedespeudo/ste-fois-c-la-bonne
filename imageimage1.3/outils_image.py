from PIL import *
import shutil
from outils_fichier import *

class outils_image:
   
    def image_position_dg(self, image1, image2, pos1, pos2, pos4, compteur):

        outils_fichier.image_in_dossier(self, compteur)
        print("yo")
        self.image1 = image1            
        self.image2 = image2
         
        self.pos1 = pos1
        self.pos2 = pos2
        self.pos4 = pos4

        self.compteur = compteur
        
        picture1 = Image.open(self.image1)
        height1 = picture1.height 
        width1 = picture1.width

        picture2 = Image.open(self.image2)
        height2 = picture2.height 
        width2 = picture2.width

        result_width = width1 + width2
        result_height = max(height1, height2)

        result = Image.new('RGB', (result_width, result_height))
        result.paste(im = picture1, box = (self.pos1, self.pos2))
        result.paste(im = picture2, box =(width1, self.pos4))
        
        a = result.save("image.png")
        
        outils_fichier.image(self, element, compteur)


    def image_position_haut_bas(self, image1, image2, liste):
     
        self.image1 = image1            
        self.image2 = image2
        self.liste = liste


        
        picture1 = Image.open(self.image1)
        height1 = picture1.height 
        width1 = picture1.width

        picture2 = Image.open(self.image2)
        height2 = picture2.height 
        width2 = picture2.width

        result_width = max(width1, width2)
        result_height = height1 + height2

        result = Image.new('RGB', (result_width, result_height))
        result.paste(im = picture1, box = (0, height2))
        result.paste(im = picture2, box =(0,0))
        a = result.save("image.png")
        self.liste.append(a)

    def image_seule(self, image1, liste):

        self.image1 = image1
        picture1 = Image.open(self.image1)
        self.liste.append(picture1)
        picture1.show()

    def couleur_passé(self,image):
        self.image = image

        picture = Image.open(self.image).convert("LA")
        
        picture.show()
        picture.save("passé_"+self.image+".png")

    def couleur_pas_passé(self,image):
        self.image = image

        picture = Image.open(self.image)
        #3 heures a refaire toutes mes conditions pour ca lol
        picture.show()
        picture.save("pas_passè_"+self.image+".png")

    def image_fin(self):
        pass

 
