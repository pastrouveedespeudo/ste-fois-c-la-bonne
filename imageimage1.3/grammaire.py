from mémoire import *

class grammaire:

    def lang_pronom(self, liste, liste2, liste3, liste4, liste5, liste6, liste7, liste8):

        
        self.liste = liste
        self.liste2 = liste2
        self.liste3 = liste3
        self.liste4 = liste4
        self.liste5 = liste5
        self.liste6 = liste6
        self.liste7 = liste7
        self.liste8 = liste8
        
        pronom_nom_commun = []


        #va falloir chercher les synonymes
        c = 0
        liste3_compteur = 0
        for i in self.liste:
            if i == [] or i == "":
                pass
            else:
                
                #condition narateur
                if self.liste[c] == ["Pronom personnel"]:
                    for j in self.liste2:
                        for i in j:
                            if i == "je" or i == "Je":
                                self.liste3[liste3].append("un narrateur parle, 1er personne sing")
                                liste3_compteur+=1
                    
                    
                            elif i == "tu" or i == "Tu":
                                self.liste3[liste3].append("un narrateur s'adresse a une autre personne, 2eme pers sing")
                                liste3_compteur+=1


                            elif i == "nous" or i == "Nous":
                                self.liste3[c].append("un narrateur s'englobe dans un groupe1er pers plur")
                                liste3_compteur+=1


                            elif i == "vous" or i =="Vous":
                                self.liste3[c].append("Politesse ou narateur vers un groupe de personne ou 1 + plusieurs")
                                liste3_compteur+=1

                                
                            elif i == "il" or i == "Il":
                                if self.ce_dernier == True:
                                    grammaire.ce_dernier(self, self.indicateur, liste, liste3, liste4, liste5, liste6, liste7)
                                    break
                                else:
                                    grammaire.il(self, self.liste, self.liste4, self.liste7, self.liste8)
                                    break
                                     
                            elif i == "elle" or i ==  "Elle":
                                if self.ce_dernier == True:
                                    grammaire.ce_dernier(self, self.indicateur1, liste, liste3, liste4, liste5, liste6, liste7)
                                    break
                                else:
                                    grammaire.elle(self, self.liste, self.liste4, self.liste7, self.liste8)
                                    break

                            elif i == "elles" or i == "Elles":
                                grammaire.elles(self, self.liste, self.liste4, self.liste8)
                            

                                
                            elif i == "ils" or i == "Ils":
                                grammaire.ils(self, self.liste, self.liste4)

                                
                    break

                c+=1



    def ce_dernier(self, liste0, liste, liste3, liste4, liste5, liste6, liste7):
        
        self.liste = liste
        self.liste0 = liste0
        self.liste3 = liste3
        self.liste4 = liste4
        self.liste5 = liste5
        self.liste6 = liste6
        self.liste7 = liste7
        
        liste = []
        
        for i in self.liste0:
            for j in self.liste6:
                a = str(j).find(str(i))
                if a >= 0:
                    c = 0
                    for i in self.liste:
   
                        if self.liste[c] == ["Nom commun"]:
                            liste.append(self.liste4[c])
                            self.ce_dernier = True
                        c+=1

    
        try:
            self.liste7.append(liste[-1])
            
        except:
            pass



    def il(self, liste, liste4, liste7, liste8):

        self.liste = liste
        self.liste3 = liste3
        self.liste4 = liste4
        self.liste7 = liste7
        self.liste8 = liste8

        liste = []
        c = 0
  
        for i in self.liste:
            if i == [] or i == "":
                pass
            else:
                if self.liste[c] == ["Nom commun"]and\
                   self.liste8[c] == ["nom masculin"]:
                    liste.append(self.liste4[c])
                   
                c += 1

        try:
            self.liste7.append(liste[-1])
            
        except:
            pass
        
    def elle(self, liste,liste4, liste7, liste8):

        self.liste = liste
        self.liste4 = liste4
        self.liste7 = liste7
        self.liste8 = liste8

        liste = []
        
        c = 0
        for i in self.liste:
            if i == [] or i == "":
                pass
            else:
                if self.liste[c] == ["Nom commun"] and\
                   self.liste8[c] == ["nom féminin"]:

                    liste.append(self.liste4[c])
                    
                c += 1

        try:
            self.liste7.append(liste[-1])
            
        except:
            pass


    def elles(self, liste, liste4, liste8):
        
        self.liste = liste
        self.liste4 = liste4
        self.liste8 = liste8


        c = 0
        for i in self.liste:
            if i == [] or i == "":
                pass
            else:
                if self.liste[c] == ["Nom commun"] and\
                   self.liste8[c] == ["nom féminin"]:
                    
                    self.liste_pronom.append(self.liste4[c])
                c+=1



    def ils(self, liste, liste4):
        
        self.liste = liste
        self.liste4 = liste4
   

        liste = []
        c = 0
        for i in self.liste:
            if i == [] or i == "":
                pass
            else:

                if self.liste[c] == ["Nom commun"]:
                    self.liste_pronom.append(self.liste4[c])
      
                c+=1









