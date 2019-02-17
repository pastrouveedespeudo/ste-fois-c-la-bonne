liste = [['le', 'Article défini', 'None', 'prénom'],
         ['chien', 'Nom commun', 'None', 'pas prénom'],
         ['noir', 'Article défini', 'None', 'pas prénom']]

c = 0



for i in liste:
    
    if liste[c][3] == "prénom" and liste[c][1] == "Article défini"\
       or liste[c][1] == "Article indéfini":
        print("pas prénom")
        
    elif liste[c][3] == "prénom" and liste[c+1][1] == "Nom commun":
        print("pas prénom")

    elif liste[c][3] == "prénom" and liste[c+1][2] == "Verbe":
        print("prenom")
    elif liste[c][3] == "prénom" and liste[c-1][2] == "Préposition":
        print("prénom")
        
    c+=1
