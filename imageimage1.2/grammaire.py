class grammaire:

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
                   self.liste[c][0] == "je" or self.liste[c][0] == "Je":
                    self.liste3.append("un narrateur parle")

                    
                elif self.liste[c][1] == "Pronom personnel" and\
                   self.liste[c][0] == "tu" or self.liste[c][0] == "Tu":
                    self.liste3.append("un narrateur s'adresse a une autre personne")


                elif self.liste[c][1] == "Pronom personnel" and\
                   self.liste[c][0] == "nous" or self.liste[c][0] == "Nous":
                    print("PRONOMMMMMMM")
                    #inclus tous les nom commun

                    
                elif self.liste[c][1] == "Pronom personnel" and\
                   self.liste[c][0] == "vous" or self.liste[c][0] == "Vous":
                    print("PRONOMMMMMMM")
                    #exclus le nom commun



                #condition pronom
                elif self.liste[c][1] == "Pronom personnel" and\
                   self.liste[c][0] == "il" or self.liste[c][0] == "Il":
                    print("ouiiiiiiii")
                    if grammaire.indicateur(self, self.oInput) == True:
                        grammaire.indicateur_pronom(self, self.liste_traitement, self.liste2)
                        
                    else:
                        
                        grammaire.il(self, self.liste_traitement, self.liste2)


                elif self.liste[c][1] == "Pronom personnel" and\
                   self.liste[c][0] == "elle" or self.liste[c][0] == "Elle":

                    if grammaire.indicateur_fem(self, self.oInput) == True:
                        grammaire.indicateur_pronom_fem(self, self.liste_traitement, self.liste2)
                        
                    else:
                        grammaire.elle(self, self.liste_traitement, liste2)

                    
                elif self.liste[c][1] == "Pronom personnel" and\
                   self.liste[c][0] == "ils" or self.liste[c][0] == "Ils":
                    grammaire.ils(self, self.liste_traitement, self.liste2)
                                                            


                elif self.liste[c][1] == "Pronom personnel" and\
                   self.liste[c][0] == "elles" or self.liste[c][0] == "Elles":
                    grammaire.elles(self, self.liste_traitement, liste2)

                    
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
        

