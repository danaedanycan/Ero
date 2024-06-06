from utils import *
from Vehicules import Vehicule
from Drone import Drone

import networkx as nx
import osmnx as ox
import matplotlib.pyplot as plt
import random

def getSectorIndexes(number):
    indexList = []
    for i in range(len(number)):
        indexList.append(int(number[i]))
    return indexList

def create_simulation():
    print("Bonjour, bienvenue dans votre session de Simulation du déneigement de Montréal.")
    print("Nous allons commencer par choisir les données de la simulation.")
    print("Nous pouvons déneiger ces secteurs 1: Outremont, 2:Verdun ,3: Anjou, 4:Rivière-des-prairies-pointe-aux-trembles et 5: Le Plateau-Mont-Royal")
    print("Pour choisir vos quartiers veuillez entrez leur numéro sans espaces. Par exemple : 135 = quartier 1, 3 et 5:")
    quartier= [False]* 5
    drones = [None]*5
    machines = [None]*5
    pairs = [None] *5
    cout = [0]*5
    for i in getSectorIndexes(input("Choisissez vos quartiers : ")):
        quartier[i-1] =True
    print("Maintenant, il est temps de parametrer ces quartiers.")
    for i in range (len(quartier)):
        if(quartier[i]):
            drones[i]=Drone()
            drones[i].SetSecteur(Secteurs[i+2])
            print("Pour le quartier: "+Secteurs[i+2]+", voulez vous une déneigeuse A ou B ?")
            choix = int(input("1: déneigeuse A , 2: déneigeuse B -> "))
            machines[i]=Vehicule(choix)
    for i in range (len(quartier)):
        if(drones[i] != None):
            pairs[i]=(drones[i].eulerian())
            cout[i]+=drones[i].total_cost 

    for i in range (len(quartier)):
        if(machines[i]!=None):
            machines[i].parcours_vehicule(pairs[i])
            cout[i]+=machines[i].cout_total

    for i in range (len(quartier)):
        if(quartier[i]):
            print("Pour le quartier: "+Secteurs[i+2]+", le cout est de :" + str(cout[i]))        

    print("Le coût total est de: "+ str(sum(cout)))
    
create_simulation()