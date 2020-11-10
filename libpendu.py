"""
    IPSA IN21 TP2 : jeu du pendu
    Ce module utilise un fichier dictionnaire de mots français sous licence GNU
    récupéré depuis : http://www.winedt.org/Dict/
    Les définitions des mots sont tirées du site cnrtl.fr
    IPSA - BONNEFOI - 2017
"""

def motAléatoire():
    """ retourne un mot tiré aléatoirement depuis un fichier dictionnaire
        le dictionnaire utilisé est en open source sur le site de winedt
    """
    import random
    location = "fr_utf8.dic"
    FDico = open(location,'r',encoding='utf-8')     # ouverture du fichier
    #total_lignes = sum(1 for line in FDico)        # nombre de ligne du fichier
    #FDico.seek(0)
    total_lignes = 338989
    num_mot_alea = random.randrange(0, total_lignes)# no aléatoire
    mot = FDico.readlines()[num_mot_alea]           # lecture de la ligne aléatoire
    mot = mot[:-1]                                  # retrait du caractère 'nouvelle ligne'
    return mot

def getWebDefinition(mot):
    """
    retourne une chainne de caractère conrtenant les définitions
    du mot passé en paramètre
    les définitions sont obtenue en effectuant une requète HTTP
    sur le site du cnrtl.

    """
    import urllib.request               # faire des requètes web
    import xml.etree.ElementTree as ET  # analyse de page web
    import html                         # pour convertir les résultats html en unicode

    url = "http://www.cnrtl.fr/definition/" # début de l adresse
    url = url+urllib.parse.quote(mot)       # mot avec caractere speciaux convertis en ascii/HTTP
    a=urllib.request.urlopen(url)           # requète web
    #str1 = a.readall()                      # lecture de la réponse in python 3.5 read()
    str1 = a.read()                         # python 3.5 lecture de la réponse in python 3.5 read()
    tree = ET.fromstring(html.unescape(str1.decode())) # construction de l'arbre XML
    defi = tree.findall("*//{http://www.w3.org/1999/xhtml}span[@class='tlf_cdefinition']") # récupération des balises span d'attribut class=...
    return defi

def printOneDef(mot):
    print("définition du CNRTL : http://www.cnrtl.fr/definition/")
    deff = getWebDefinition(mot)
    print(deff[0].text)

def printAllDef(mot):
    print("définitions du CNRTL : http://www.cnrtl.fr/definition/")
    deff = getWebDefinition(mot)
    for d in deff:
        print("-",d.text) 

def getAllDef(mot):
    deff = getWebDefinition(mot)
    L=list()
    for d in deff:
        L.append(d.text)
    return L

def getAllDefStr(mot):
    deff = getWebDefinition(mot)
    S=''
    for d in deff:
        S = S+(d.text)+"\n"
    return S

if __name__ == '__main__':
    mot  = motAléatoire()
    print(mot)
    printAllDef(mot)

