from outils_image import *

class syntaxe:

                
    def prenom_premier(self, liste):
        #prenom_premier(self, self.liste_traitement)

        self.liste = liste

        c = 0
        
        for i in self.liste:

            try:
                if self.liste[c][3] == "prénom" and self.liste[c][1] == "Article défini"\
                   or self.liste[c][1] == "Article indéfini":
                    del self.liste[c][3]
                    print("fait")
                    self.liste[c].append("pas prénom")
            except:
                pass

            
            try:   
                if self.liste[c][3] == "prénom" and self.liste[c+1][1] == "Nom commun":
                    del self.liste[c][3]
                    print("fait1")
                    self.liste[c].append("pas prénom")
            except:
                pass


            try:
                if self.liste[c][3] == "prénom" and self.liste[c-1][1] == "Article défini":
                    del self.liste[c][3]
                    print("fait2")
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



    def condition_article(self, liste):    
        #condition_article(self, self.liste_traitement)

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
                    try:
                        if art > 0 and self.liste[c1 + 1][2] == "Verbe":
                            print(self.liste[c1 + 1][2])
                            del self.liste[c1 + 1][2]
                            print("fait")
                        elif art1 > 0 and self.liste[c1 + 1][2] == "Verbe":
                            print(self.liste[c1 + 1][2])
                            del self.liste[c1 + 1][2]
                            print("fait")
                        elif art2 > 0 and self.liste[c1 + 1][2] == "Verbe":
                            print(self.liste[c1 + 1][2])
                            del self.liste[c1 + 1][2]
                            print("fait")
                        elif art3 > 0 and self.liste[c1 + 1][2] == "Verbe":
                            print(self.liste[c1 + 1][2])
                            del self.liste[c1 + 1][2]
                            print("fait")


                            
                    except:
                        pass
                    finally:
                        c2+=1
                        break
                    
            c1 += 1
            c2 = 0
        
        
        
        
        #Article + Verbe ex le crayon (correction auto)
        #si y'a un article alors le prochain truk ne peux pas etre un verbe



    

    def maisouestdoncornicar(self, liste, liste2, liste3, liste4):
        #maisouestdoncornicar(self, liste, liste2, liste3, self.liste_image_phase1)
        
        
        
        self.liste = liste
        self.liste2 = liste2
        self.liste3 = liste3
        self.liste4 = liste4
        
        liste1 = []

        c = 0

        try:
            for i in self.liste:
                if self.liste[c][0] == "et":
                    liste1.append(self.liste[c][0])
                    outils_image.image_position_dg(self, self.liste2[0], self.liste2[1],
                                            0, 0, 0, self.liste4)
                c+=1
                
        except:
            pass
        
        


    def lang_ponctuation(self, liste, liste2):
        self.liste = liste
        self.liste2 = liste2
        nvelle_liste = []
        
        for i in self.liste:
            for j in i:

                if j == ",":
                    syntaxe.trouve_ponctu(self, liste, nvelle_liste, i)
                    expli1 = "exprime un repos, une reprise du souffle"
                    self.liste2.append(expli1)
                    
                elif j == ".":
                    syntaxe.trouve_ponctu(self, liste, nvelle_liste, i)
                    expli2 = "exprime une fin d'idée"
                    self.liste2.append(expli2)
                    
                elif j == "!":
                    syntaxe.trouve_ponctu(self, liste, nvelle_liste, i)
                    expli3 = "expime l'exclamation"
                    self.liste2.append(expli3)
                    
                elif j == "?":
                    syntaxe.trouve_ponctu(self, liste, nvelle_liste, i)
                    expli4 = "exprime la surprise"
                    self.liste2.append(expli4)
                    
                elif j == ":":
                    syntaxe.trouve_ponctu(self, liste, nvelle_liste, i)
                    expli5 = "exprime une précision"
                    self.liste2.append(expli5)
             

    def trouve_ponctu(self, liste, liste3, i):
        self.liste = liste
        self.liste3 = liste3
        self.i = i

        index = self.liste.index(self.i)
        self.liste3 = []
        self.liste3.append(self.liste[index][-1])
        del self.liste[index][-1]
        new = index + 1
        self.liste.insert(new, self.liste3)
        self.liste3 = []
        

    def phrase(self, liste, liste2):
        self.liste = liste
        self.liste2 = liste2
        liste = []
        
        c = 0
        for i in self.liste:

            if i == [] or i == [""] or i == [" "]:
                pass
            elif i == ["."]:
                break
            
            else:
                self.liste.append(["."])
                break

        for i in self.liste:
            if i == [""] or i == [] or i == [ ] or i == [" "]:
                pass
            else:
                self.liste2.append(i)


            
            
                


























            
