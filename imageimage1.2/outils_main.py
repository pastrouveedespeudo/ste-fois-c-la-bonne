class outils_main:

                    
    def pos_liste_traitement(self, liste, liste_main, compteur):

        self.liste = liste
        self.compteur = compteur
        self.liste_main = liste_main
   
        c = 0
        for i in range(self.compteur + 1):
  
            for i in self.liste_main:
                for j in i :
                    if self.liste[c][0] == j:
                        del self.liste[c][1]
            
            c+=1

    def ajout_verbe(self, liste, compteur):

        self.liste = liste
        self.compteur = compteur

        c = 0
        
        for i in self.liste:
            print(self.liste[c])
            break
            c += 1
            
        print(c)
        print(self.compteur)
        if c < self.compteur:
            for i in range(self.compteur):
                self.liste.append("présent ou future faire la fonction")
