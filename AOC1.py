with open(r"C:\Users\user\Desktop\input.txt", 'r') as file:
    contenu = file.read().replace('\n', '   ')
    array = [element.strip() for element in contenu.split('   ') if element.strip()]

#for i in array:
#    print(i)

#array = [1,2,3,4,5,6,7,8]  #juste pour tester si ma fonction marchait
#print("tableau de base :",array)

liste_droite = []  # tableau qui contiendra les nombres de la 2ème colonne de input.txt 
liste_gauche = []  # tableau qui contiendra les nombres de la 1ère colonne de input.txt 

def remplir_liste():
    for i, element in enumerate(array):
        if i % 2 == 0:
            liste_gauche.append(int(element))
        else:
            liste_droite.append(int(element))

remplir_liste()
#print("Liste gauche :", liste_gauche)
#print("Liste droite :", liste_droite)

#j'aurais pu utiliser sorted() mais bon je m'en suis rendue compte trop tard
def trier_liste(liste):
    for i in range(len(liste)):
        min_indice = i  # indice du plus petit element de ma liste
        for j in range(i + 1, len(liste)):
            if liste[j] < liste[min_indice]:
                min_indice = j
        liste[i], liste[min_indice] = liste[min_indice], liste[i]

trier_liste(liste_droite)
trier_liste(liste_gauche)

liste_somme = []

def somme(liste1, liste2):
    for i in range(len(liste1)):
        somme = abs(liste1[i] - liste2[i])
        liste_somme.append(somme)

somme(liste_gauche, liste_droite)

resultat = liste_somme[0]
for i in range(1, len(liste_somme)):
    resultat = resultat + liste_somme[i]

#print("Le résultat du puzzle 1 est :",resultat)   

occ = []
liste_occ = []

def occurence():
    for i in range(len(liste_gauche)):
        occ = liste_droite.count(liste_gauche[i])
        produit = occ * liste_gauche[i]
        liste_occ.append(produit)

occurence()

res = liste_occ[0]
for i in range(1, len(liste_occ)):
    res = res + liste_occ[i]

print("Le résultat du puzzle 2 est :", res)
