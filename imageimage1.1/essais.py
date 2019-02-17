liste = [[['le', 'Article défini', 'None', 'nom masculin', 'pas prénom'],
          ['chat', 'Nom commun', 'None', 'pas prénom', 'nom masculin', 'vivant'],
          ['mange', 'Verbe', 'pas prénom', 'None'],
          ['le', 'Article défini', 'None', 'nom masculin', 'pas prénom'],
          ['chien', 'Nom commun', 'None', 'pas prénom', 'nom masculin', 'vivant']],
          [['.', 'None', 'pas prénom', 'None'], ["il"], ["aime"], ["les"], ["anchois"]]



         ]


#self.liste2 = liste2

c = 0
d = 0
for i in liste:
    for j in i:
        for k in j:
            if k == "Nom commun":
                print(j[0], j[-1], k)
            elif k == "Verbe":
                print(j[0])
                print(self.liste2[c])

         
    c+=1
