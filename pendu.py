#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" IPSA IN21 TP2: jeu du pendu 
    Ce code utilise un fichier dictionnaire de mots français
    sous licence GNU GPL : http://www.winedt.org/Dict/
    Les définitions des mots sont tirées du CNRTL: cnrtl.fr
"""

import libpendu as lp


print("============= JEU DU PENDU =============\n")

reponse="oui"
points=0

while(reponse == "oui"):
    print("_____________________________________________\n")
    print("Niveaux de difficulté\nFacile: 1\nNormal: 2\nDifficile: 3")
    niv=0
    
    while(niv!=1 and niv!=2 and niv!=3):
        niv=int(input("Choix du niveau de difficulté: "))
    
    mot=lp.motAléatoire()
    nb_essais=0
    
    if niv==1:
        max_essais=int(1.5*len(mot))
    elif niv==2:
        max_essais=int(1.3*len(mot))
    elif niv==3:
        max_essais=int(len(mot))

    #print("*mot aléatoire:",mot)
    print("*Le mot recherché a",len(mot),"lettres.")
    print("*Nombre maximum d'essais:",max_essais)
    print("\nPour sortir du jeu, tapez 'stop'.")
    print("_____________________________________________\n")

    mot_trouve=['.' for i in range(len(mot))]
    liste_essais=[]


    while (nb_essais < max_essais) and (("".join(mot_trouve)) != mot):
        print("*Encore",(max_essais-nb_essais),"essais restants")
        print("*Mot du joueur:","".join(mot_trouve)) 
   
        l=input("Saississez une lettre: ")
        
        
        if l=="stop":
            break
        
        if l in liste_essais:
            print("\n...Vous avez déjà choisi cette lettre...")
            nb_essais=nb_essais
        else:
            liste_essais.append(l)
            print("*Lettres jouées:",liste_essais)
            nb_essais+=1
            if l in mot:
                print("\nbien joué! le mot contient cette lettre!")
            else:
                print("\noups, ce mot ne contient pas cette lettre...") 
            
        for i in range(len(mot)):
            if (mot[i]==l):
                mot_trouve[i]=l
        
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    if (nb_essais==0) or ("".join(mot_trouve)!=mot):
        
        #-------------------------------------------------------------#
        #si (nb_essais>=max_essais) est vérifiée, on peut perdre alors#
        #qu'il nous reste 1 essai... Dans la pratique, on perd quand  #
        #on n'a plus d'essais.                                        #
        #-------------------------------------------------------------#
        print("*********** Dommage, vous avez perdu... *********")
        print("Le mot était:",mot)
        points=points
        print("Vous avez",points,"points.")
        print("*************************************************\n")
    else:
        print("********** Félicitations, c'est gagné! **********")
        print("Mot du joueur: ",mot)
        points+=1
        print("Vous avez",points,"points.")
        print("*************************************************\n")
        #lp.printAllDef(mot)
    
    reponse=input("Recommencer? (oui ou non): ")
    
    if reponse=="non":
        break
    
    

    

