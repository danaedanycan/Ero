import sys

import osmnx as ox
import networkx as nx
from graph_tool.all import *
import itertools as iter
import utils
from utils import nb_Km
import itertools as iter
from numpy import ceil
class Vehicule:
    def __init__(self, vehicule_type):
        self.vehicule_type = vehicule_type
        self.cout_total = 0.0
        self.nb_heure = 0.0
        if vehicule_type == 1:
            self.cout_fixe_par_jour = 500
            self.cout_kilometrique = 1.1
            self.cout_horaire_8h = 1.1
            self.cout_horaire_plus_8h = 1.3
            self.vitesse_moyenne = 10
        elif vehicule_type == 2:
            self.cout_fixe_par_jour = 800
            self.cout_kilometrique = 1.3
            self.cout_horaire_8h = 1.3
            self.cout_horaire_plus_8h = 1.5
            self.vitesse_moyenne = 20

    def set_cout_total_km(self, nb_km):
        temps = nb_km/self.vitesse_moyenne
        
        self.cout_fixe_par_jour =  nb_km * self.cout_kilometrique
        self.nb_heure += temps

    def set_cout_total(self):
        if (self.nb_heure > 8):
            self.cout_total += 8*self.cout_horaire_8h  + (self.nb_heure-8) * self.cout_horaire_plus_8h
        else:
            self.cout_total += self.nb_heure *  self.cout_horaire_8h