from time import time
from math import *
from numpy import *
from random import *
from json import *
from copy import*

##############
# SAE S01.01 #
##############

def nb_villes(villes):
    """Retourne le nombre de villes"""
    return len(villes)//3


def noms_villes(villes):
    """Retourne un tableau contenant le nom des villes"""
    noms_v = []
    i = 0
    while 3*i < len(villes):
        noms_v.append(villes[3*i])
        i += 1
    return noms_v


def d2r(nb):
    return nb*pi/180


def distance(long1, lat1, long2, lat2):
    """retourne la distance entre les points (long1, lat1) et (long2, lat2)"""
    lat1 = d2r(lat1)
    long1 = d2r(long1)
    lat2 = d2r(lat2)
    long2 = d2r(long2)
    R = 6370.7
    d = R*arccos(sin(lat1)*sin(lat2)+cos(lat1)*cos(lat2)*cos(long2-long1))
    return d


def indexCity(ville,villes):
    """
    Cette fonction retourne la position de la ville passée en paramètre dans le tableau villes
    """
    i=0 # Initialisation de la boucle while
    while i <len(villes): 
        if ville == villes[i]: # Tant que la ville passée en paramètre ne correspond pas à lindice i alors on avancera dans le tableau "villes" 
            return i
        i+=1
    return -1


def distance_noms(nom1, nom2, villes):
    """Retourne la distance entre les villes nom1 et nom2 
       en fonction de la structure de données villes
    """
    index1 = indexCity(nom1, villes)
    index2 = indexCity(nom2, villes)

    if index1 == -1 or index2 == -1:
        d = -1
    else:
        d = distance(villes[index1+1], villes[index1+2],
                     villes[index2+1], villes[index2+2])
    return d


def lecture_villes(path):
    """Retourne la structure de données villes en fonction des données du fichier path"""
    f_in = open(path, encoding='utf-8', mode='r')
    villes = []
    li = f_in.readline()
    li = li.strip()
    while li != '':
        tab_li = li.split(';')
        villes.append(tab_li[0])
        villes.append(float(tab_li[1]))
        villes.append(float(tab_li[2]))
        li = f_in.readline()
        li = li.strip()
    f_in.close()
    return villes


def long_tour(villes, tournee):
    """Retourne la longueur d'une tournée en fonction de la structure de données villes"""
    long = 0
    i = 0
    while i+1 < len(tournee):
        long += distance_noms(tournee[i], tournee[i+1], villes)
        i += 1
    long += distance_noms(tournee[i], tournee[0], villes)
    return long


##############
# SAE S01.02 #
##############



def dictionary_cities(villes):
    '''
    Cette fonction retourne un dictionnaire de distances contenant les distances entre les villes du tableau passé en paramètre
    
    '''
    dico = {}                # Initialisation du dictionnaire de distances
    i = 0                    # Initialisation de l'indice de la ville principale
    while i < len(villes):   # Boucle principale sur les villes
        j = 0                 # Initialisation de l'indice pour les autres villes
        y = {}                # Initialisation du dictionnaire temporaire pour les distances
        while j < len(villes):   # Boucle interne sur les autres villes
            if i != j:           # Vérifier que la ville n'est pas la même que la ville principale
                y[villes[j]] = distance_noms(villes[i], villes[j], villes)  # Calcul de la distance et ajout au dictionnaire temporaire
            j += 3  # Incrémenter j par 3 pour passer à la prochaine ville
            
        dico[villes[i]] = y  # Ajout du dictionnaire temporaire au dictionnaire principal
        i += 3  # Incrémenter i par 3 pour passer à la prochaine ville
    
    return dico  # Retourner le dictionnaire de distances


def distances_cities(ville1, ville2, dico):
    '''
    Cette fonction retourne la distance entre deux villes à partir du dictionnaire de distances passé en paramètre.
    Retourne la distance entre les deux villes si elles existent dans le dictionnaire, sinon -1
    '''
    if ville1 in dico and ville2 in dico:
        return dico[ville1][ville2]
    return -1

def tour_length(tour, dico):
    '''
    Cette fonction calcule la longueur totale d'un tour basée sur un dictionnaire de distances entre les villes.

    '''
    i = 0  # Initialisation de la variable d'index pour parcourir la liste des villes dans le tour
    somme = 0  # Initialisation de la variable pour stocker la longueur totale du tour

    # Boucle while pour itérer à travers la liste des villes dans le tour
    while i < len(tour) - 1:
        # Ajout de la distance entre la ville actuelle et la ville suivante à 'somme'
        somme += distances_cities(tour[i], tour[i + 1], dico)
        i += 1  # Incrémentation de l'index

    # Ajout de la distance entre la première et la dernière ville du tour à 'somme'
    somme += distances_cities(tour[0], tour[len(tour) - 1], dico)

    return somme  # Retourne la longueur totale du tour

def closest_city(city,cities,dico):
    """
        Cette fonction recherche la ville la plus proche de la ville spécifiée dans une liste de villes.

    """
    i = 0  # Initialisation de l'indice pour parcourir la liste des villes
    res = i  # Initialisation du résultat avec la première position
    plus_petit = distances_cities(city, cities[i], dico)  # Initialisation de la distance minimale

    # Boucle while pour parcourir la liste des villes
    while i < len(cities) - 1:
        x = distances_cities(city, cities[i + 1], dico)  # Distance entre 'city' et la ville suivante
        if x < plus_petit:
            # Mise à jour de 'plus_petit' et de 'res' si la distance est plus petite
            plus_petit = distances_cities(city, cities[i + 1], dico)
            res = i + 1

        i += 1  # Incrémentation de l'indice

    return res  # Retourne l'indice de la ville la plus proche 

def tour_from_closest_city(ville, dico):
    """
    Cette fonction génère un tour de villes en partant de la ville spécifiée, en choisissant
    à chaque étape la ville la plus proche non encore visitée.
    """
    tour = [ville]  # Initialisation du tour avec la ville de départ
    x = list(dico.keys())  # Liste de toutes les villes
    y = indexCity(ville, x)  # Obtention de l'indice de la ville de départ dans la liste
    x.pop(y)  # Suppression de la ville de départ de la liste

    # Boucle while pour ajouter des villes au tour jusqu'à ce que toutes les villes soient incluses
    while len(tour) < len(dico):
        # Obtention de l'indice de la ville la plus proche et ajout au tour
        index_ville_a_ajouter = closest_city(ville, x, dico)
        ville_a_ajouter = x[index_ville_a_ajouter]
        tour.append(ville_a_ajouter)
        x.remove(ville_a_ajouter)  # Retrait de la ville ajoutée de la liste
        ville = ville_a_ajouter  # Mise à jour de la ville actuelle pour la prochaine itération

    return tour  # Retourne le tour des villes

def best_tour_from_closest_city(dico):
    """
    Cette fonction génère le meilleur tour parmi tous les tours possibles en partant de chaque ville,
    en choisissant celui qui a la longueur minimale.
    """
    x = list(dico.keys())       # Liste de toutes les villes
    i = 0                       # Initialisation de l'indice
    res = tour_from_closest_city(x[i], dico)  # Initialisation du résultat avec le tour généré en partant de la première ville

    # Boucle externe parcourant toutes les villes
    while i < len(x):
        tour_courant = tour_from_closest_city(x[i], dico)
        # Comparaison de la longueur du tour généré en partant de la ville actuelle avec le résultat actuel
        if tour_length(tour_courant, dico) < tour_length(res, dico):
            # Mise à jour du résultat si un tour plus court est trouvé
            res = tour_courant
        # Incrémentation de l'indice
        i += 1

    # Retourne le résultat, qui représente le meilleur tour obtenu avec la longueur minimale
    return res

def reverse_part_tour(tour,ind_b,ind_e):
    """
    Cette fonction inverse une partie spécifique d'un tour entre deux indices donnés.

    """
    while ind_b < ind_e:
        val_temp = tour[ind_b]  # Stockage temporaire de l'élément à l'indice 'ind_b'
        tour[ind_b] = tour[ind_e]  # Échange des éléments aux indices 'ind_b' et 'ind_e'
        tour[ind_e] = val_temp  # Restauration de l'élément à l'indice 'ind_e'
        ind_b += 1  # Incrémentation de l'indice de début
        ind_e -= 1  # Décrémentation de l'indice de fin

    return tour  # Retourne le tour modifié avec la partie inversée

def inversion_length_diff(dico,tournee,ind_b,ind_e):
    """
    Cette fonction calcule la différence de longueur entre un tour initial et un tour résultant
    de l'inversion d'une partie spécifique du tour initial.

    """
    x = tour_length(tournee, dico)  # Calcul de la longueur du tour initial
    nouveau_tour = reverse_part_tour(tournee, ind_b, ind_e)  # Inversion de la partie spécifiée du tour
    z = tour_length(nouveau_tour, dico)  # Calcul de la longueur du tour résultant après l'inversion
    return x - z  # Retourne la différence de longueur entre les deux tours

def better_inversion(tournee, dico):
    '''
    Cette fonction vérifie s'il existe une inversion de deux villes dans le tour initial qui
    améliore la longueur totale du tour.

    '''
    x = tour_length(tournee, dico)  # Calcul de la longueur du tour initial
    i = 1

    # Boucle while pour itérer à travers les indices du tour initial, en sautant l'indice 2
    while i < len(tournee):
        if i == 2:
            i += 1
        nouvelle_tournee = reverse_part_tour(tournee, i, 2)  # Inversion de la partie spécifiée du tour
        i += 1

        # Vérification si la longueur du tour résultant après l'inversion est plus courte
        if tour_length(nouvelle_tournee, dico) < x:
            return True

    return False  # Aucune inversion n'améliore la longueur du tour initial

def best_obtained_with_inversions(tour, d_cities):
    """
    Cette fonction renvoie le meilleur tour en utlisaant la foonction  better_inversion et retourne le nombre de fois que celle-ci
    à été utilisé
    """
    i = 0
    while better_inversion(tour, d_cities): #Tant que better inversion retourne True 
        i += 1
    return i # On retourne le nombre de fois qu'on utilise la fonction