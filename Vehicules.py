import networkx as nx
import osmnx as ox
import matplotlib.pyplot as plt

from utils import *

class Vehicule:
    def __init__(self, vehicule_type):
        
        self.vehicule_type = vehicule_type
        self.nb_heure = 0.0
        self.secteur = Secteurs[1]
        if vehicule_type == 1:
            self.cout_total = 500
            self.cout_kilometrique = 1.1
            self.cout_horaire_8h = 1.1
            self.cout_horaire_plus_8h = 1.3
            self.vitesse_moyenne = 10
        elif vehicule_type == 2:
            self.cout_total = 800
            self.cout_kilometrique = 1.3
            self.cout_horaire_8h = 1.3
            self.cout_horaire_plus_8h = 1.5
            self.vitesse_moyenne = 20

    def set_cout_total_km(self, nb_km):
        temps = nb_km/self.vitesse_moyenne
        
        self.cout_total +=  nb_km * self.cout_kilometrique
        self.nb_heure += temps
        if (self.nb_heure > 8):
            self.cout_total += 8*self.cout_horaire_8h  + (self.nb_heure-8) * self.cout_horaire_plus_8h
        else:
            self.cout_total += self.nb_heure *  self.cout_horaire_8h
    
    def Setsecteur(self, secteur):
        self.secteur =  secteur

   

    def parcours_vehicule(self, parcours=None) :
        
    
        graph = ox.graph_from_place(self.secteur, network_type="drive")
        graph = graph.to_directed()
        nb_km = 0

        for (i,j) in parcours :
            edge = graph.get_edge_data(i,j)
            if(edge != None):
                nb_km += (edge[0]['length'])
        self.set_cout_total_km(nb_km/1000)