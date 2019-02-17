class langage:



    def lang_verbe(self):
        pass
        #que fais les nom commun?


    def lang_ponctuation(self, liste, liste2):
        self.liste = liste
        self.liste2 = liste2
        nvelle_liste = []
        
        for i in self.liste[0:]:
            for j in i:

                
                if j == ",":
                    langage.trouve_ponctu(self, liste, nvelle_liste, i)
                    expli1 = "exprime un repos, une reprise du souffle"
                    self.liste2.append(expli1)
                    
                elif j == ".":
                    langage.trouve_ponctu(self, liste, nvelle_liste, i)
                    expli2 = "exprime une fin d'idée"
                    self.liste2.append(expli2)
                    
                elif j == "!":
                    langage.trouve_ponctu(self, liste, nvelle_liste, i)
                    expli3 = "expime l'exclamation"
                    self.liste2.append(expli3)
                    
                elif j == "?":
                    langage.trouve_ponctu(self, liste, nvelle_liste, i)
                    expli4 = "exprime la surprise"
                    self.liste2.append(expli4)
                    
                elif j == ":":
                    langage.trouve_ponctu(self, liste, nvelle_liste, i)
                    expli5 = "exprime une précision"
                    self.liste2.append(expli5)
             

    def trouve_ponctu(self, liste, liste2, i):
        self.liste = liste
        self.liste2 = liste2
        self.i = i
        
        index = self.liste.index(self.i)
        self.liste2 = []
        self.liste2.append(self.liste[index][-1])
        del self.liste[index][-1]
        new = index + 1
        self.liste.insert(new, self.liste2)
        self.liste2 = []
















    def temps_regle(self):
        pass

        #si passé simple alors répondre par du
        #imparfait alors répondre par


    
    def maisouestdoncornicar(self):
        liste = ["mais","ou","et","donc","or","ni","car"]

    def adverbe(self):
        pass
        #alors marque un résultat ou une agression
    
    def préposition(self):
        pass
        #apres marque la visualisation du futur ou avant apres
        #apres jte dis jmen balec, apres avoir fais ca




    #le chien a gauche du chat, il mange des croquettes
    #le chien court apres le chat



    #tu vas devoir changer les images
    #en faire une sorte d'histoire
    #le but c que le truk raconte l'histoire






    
#--------------------------------------------------------------------
    def lang_pronom(self, liste, liste2, liste3):
        
        self.liste = liste
        self.liste2 = liste2
        self.liste3 = liste3
  

        pronom_nom_commun = []


        #va falloir chercher les synonymes
        c = 0
        for i in self.liste:

            try:
                
            

                #condition narateur
                if self.liste[c][1] == "Pronom personnel" and\
                   self.liste[c][0] == "je":
                    self.liste3.append("un narrateur parle")

                    
                elif self.liste[c][1] == "Pronom personnel" and\
                   self.liste[c][0] == "tu":
                    self.liste3.append("un narrateur s'adresse a une autre personne")


                elif self.liste[c][1] == "Pronom personnel" and\
                   self.liste[c][0] == "nous":
                    print("PRONOMMMMMMM")
                    #inclus tous les nom commun

                    
                elif self.liste[c][1] == "Pronom personnel" and\
                   self.liste[c][0] == "vous":
                    print("PRONOMMMMMMM")
                    #exclus le nom commun



                #condition pronom
                elif self.liste[c][1] == "Pronom personnel" and\
                   self.liste[c][0] == "il":
                    
                    if langage.indicateur(self, self.oInput) == True:
                        langage.indicateur_pronom(self, self.liste_traitement, self.liste2)
                        
                    else:
                        langage.il(self, self.liste, self.liste2)


                elif self.liste[c][1] == "Pronom personnel" and\
                   self.liste[c][0] == "elle":

                    if langage.indicateur_fem(self, self.oInput) == True:
                        langage.indicateur_pronom_fem(self, self.liste_traitement, self.liste2)
                        
                    else:
                        langage.elle(self, self.liste, liste2)

                    
                elif self.liste[c][1] == "Pronom personnel" and\
                   self.liste[c][0] == "ils":
                    langage.ils(self, self.liste, self.liste2)
                                                            


                elif self.liste[c][1] == "Pronom personnel" and\
                   self.liste[c][0] == "elles":
                    langage.elles(self, self.liste, liste2)

                    
                elif i == []:
                    pass
              
            except:
                pass

            finally:
                c+=1







 


    def elle(self, liste, liste2):
        self.liste = liste
        self.liste2 = liste2

        c = 0
        for i in self.liste:
            a = str(self.liste[c]).find("nom féminin")
            if self.liste[c][1] == "Nom commun" and\
               a >= 0:
                self.liste2.append(self.liste[c][0])
                break
        c += 1

        
    def elles(self, liste, liste2):
        self.liste = liste
        self.liste2 = liste2
        
        c = 0
        for i in self.liste:
            a = str(self.liste[c]).find("nom féminin")
            if self.liste[c][1] == "Nom commun" and\
               a >= 0:
                self.liste2.append(self.liste[c][0])

                c+=1
            else:
                c += 1


    def nous(self):
        pass

    def vous(self):
        pass

    def je(self):
        pass

    def tu(self):
        pass



    def il(self, liste, liste2):

        self.liste = liste
        self.liste2 = liste2

        c = 0
        for i in self.liste:
            if self.liste[c][1] == "Nom commun":
                self.liste2.append(self.liste[c][0])
                break
            c += 1


    def ils(self, liste, liste2):
        
        self.liste = liste
        self.liste2 = liste2

        c = 0
        for i in self.liste:
            if self.liste[c][1] == "Nom commun":
                self.liste2.append(self.liste[c][0])

                c+=1
            else:
                c += 1
   


    def indicateur(self, liste):

        self.liste = liste

        self.indicateur = ["ce dernier"]

        for i in self.indicateur:
            a = str(liste).find(str(i))
            if a >= 0:
                return True
    def indicateur_pronom(self, liste, liste2):
        
        self.liste = liste
        self.liste2 = liste2
        liste3 = []

        c = 0
        for i in self.liste:
            b = self.liste[c][0]
            
            if self.liste[c][1] == "Nom commun":
                liste3.append(b)
                self.liste2.append(liste3[-1])
                del self.liste2[:-1]
            c += 1


            
    def indicateur_fem(self, liste):

        self.liste = liste

        self.indicateur = ["cette derniere", "cete dernière"]

        for i in self.indicateur:
            a = str(liste).find(str(i))
            if a >= 0:
                return True
    def indicateur_pronom_fem(self, liste, liste2):
        
        self.liste = liste
        self.liste2 = liste2
        liste3 = []

        c = 0
        for i in self.liste:
            b = self.liste[c][0]
            
            if self.liste[c][1] == "Nom commun" and\
               self.liste[c][4] == "nom féminin":
                liste3.append(b)
                self.liste2.append(liste3[-1])
                del self.liste2[:-1]
            c += 1
        









    
