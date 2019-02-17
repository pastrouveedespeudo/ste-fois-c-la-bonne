
class syntaxe:
    
    def lang_ponctuation(self, liste, liste2):
        self.liste = liste
        self.liste2 = liste2
        nvelle_liste = []

        for i in self.liste:

            for k in i:
                for j in k: 

                    if j == ",":
            
                        expli1 = "exprime un repos, une reprise du souffle"
                        self.liste2.append(expli1)
                        
                    elif j == ".":
        
                        expli2 = "exprime une fin d'idée"
                        self.liste2.append(expli2)
                        
                    elif j == "!":
                  
                        expli3 = "expime l'exclamation ou de l'exitation"
                        self.liste2.append(expli3)
                        
                    elif j == "?":
              
                        expli4 = "exprime la surprise ou une demande"
                        expli4_1 = "la voix monte dans les aigue"
                        self.liste2.append(expli4)
                        
                    elif j == ":":
              
                        expli5 = "exprime une précision"
                        self.liste2.append(expli5)

                    elif j == "'" or j == '"':
              
                        expli6 = "debut, fin: exprime une reprise de discourd"
                        self.liste2.append(expli6)


    
                
                
    def prenom_premier(self, liste, liste2):
        #prenom_premier(self, self.liste_traitement)

        self.liste = liste
        self.liste2 = liste2
        
        c = 0
        
        for i in self.liste:

            if i == [] or i == "":
                pass
            else:
          
                if self.liste[c] == ["Article défini"] or self.liste[c] == ["Article indéfini"]\
                   and self.liste2[c+1] == ["prénom"]:

                    del self.liste2[c+1]
                    self.liste2.insert(c+1, ["pas prénom"])

    
                if self.liste2[c] == ["prénom"] and self.liste[c+1] == ["Nom commun"]:
 
                    del self.liste2[c]
                    self.liste2.insert(c, ["pas prénom"])


                if self.liste[c] == ["Article défini"] and self.liste2[c] == ["prénom"]:

                    del self.liste2[c]
                    self.liste2.insert(c, ["pas prénom"])

                c+=1


    

    def condition_article(self, liste, liste2):    
        #condition_article(self, self.liste_traitement)

        self.liste = liste
        self.liste2 = liste2
        
        c = 0
        
        for i in self.liste:
            if i == []:
                pass
            else:
                for i in self.liste:
        
                    try:
                        
                        if self.liste[c] == ["Article défini"] and self.liste2[c] == ["Verbe"]:
                            del self.liste2[c]
                            self.liste2.insert(c, ["pas verbe"])
                            
                        elif self.liste[c] == ["Article indéfini"] and self.liste2[c] == ["Verbe"]:
                            del self.liste2[c]
                            self.liste2.insert(c, ["pas verbe"])
                            
                        elif self.liste[c] == ["Nom commun"] and self.liste2[c] == ["Verbe"]:
                            del self.liste2[c]
                            self.liste2.insert(c, ["pas verbe"])
                        
                        elif self.liste[c] == ["Lettre"] and self.liste2[c] == ["Verbe"]:
                            del self.liste2[c]
                            self.liste2.insert(c, ["pas verbe"])
                        
                        elif self.liste[c] == ["Préposition"] and self.liste2[c] == ["Verbe"]:
                            del self.liste2[c]
                            self.liste2.insert(c, ["pas verbe"])

                            
                        elif self.liste[c] == ["Préposition"] and self.liste2[c + 1] == ["Verbe"]:
                            del self.liste2[c+1]
                            self.liste2.insert(c + 1, ["pas verbe"])

                        elif self.liste[c] == ["Article défini"] and self.liste2[c + 1] == ["Verbe"]:
                            del self.liste2[c + 1]
                            self.liste2.insert(c + 1, ["pas verbe"])

                        elif self.liste[c] == ["Article indéfini"] and self.liste2[c + 1] == ["Verbe"]:
                            del self.liste2[c + 1]
                            self.liste2.insert(c + 1, ["pas verbe"])
                            
                        elif self.liste[c] == ["Lettre"] and self.liste2[c + 1] == ["Verbe"]:
                            del self.liste2[c + 1]
                            self.liste2.insert(c + 1, ["pas verbe"])
                    except:
                        pass

                    
                    c += 1
 
        
        #attention si y'au n blem, ici, y'a peut etre une faure au 1er paragraphes
        #Article + Verbe ex le crayon (correction auto)
        #si y'a un article alors le prochain truk ne peux pas etre un verbe








                        
                 

#j'apprend -> je apprend(verbe ? e), l'apostrophe -> la apostrophe(nf ? a)
#l'elephant(nm ? le elephant)
