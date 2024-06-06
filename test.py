import networkx as nx
import osmnx as ox
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import geopandas as gpd
import pandas as pd
import random

import utils
from Vehicules import Vehicule

from Drone import Drone
from utils import nb_Km

  
visited = {}

place_name = [{"city": "Outremont", "state": "Montreal", "country": "Canada"}]
              #{"city": "Verdun", "state": "Montreal", "country": "Canada"},
              #{"city": "Anjou", "state": "Montreal", "country": "Canada"},
              #{"city": "Rivière-des-prairies-pointe-aux-trembles", "state": "Montreal", "country": "Canada"},
              #{"city": "Le Plateau-Mont-Royal", "state": "Montreal", "country": "Canada"}]

graph = ox.graph_from_place(place_name, network_type="drive", retain_all=True)
graph.get_edge_data
"""for u, v, key, data in graph.edges(keys=True, data=True):
    data['lanes'] = random.uniform(2.5, 15) # height of snow = weight of the edge
    data['name'] = False # boolean weather the edge was visited or not

edge_weights = [data['lanes'] for u, v, key, data in graph.edges(keys=True, data=True)]

cmap = plt.colormaps['RdYlGn_r']
norm = mcolors.Normalize(vmin=2.5, vmax=15)
edge_colors = [cmap(norm(length)) for length in edge_weights]
# Créer une liste de couleurs pour chaque edge
edge_color_map = {}
for (u, v, key, data), color in zip(graph.edges(keys=True, data=True), edge_colors):
    edge_color_map[(u, v, key)] = color

# Fonction de couleur pour les edges
def get_edge_color(u, v, key, data):
    return edge_color_map[(u, v, key)]

# Tracer le graphe avec des couleurs d'edges personnalisées
fig, ax = ox.plot_graph(
    graph,
    edge_color=[get_edge_color(u, v, key, data) for u, v, key, data in graph.edges(keys=True, data=True)],
    edge_linewidth=1,
    node_size=0
)

# Afficher le graphique
plt.show()

# Function to check if a node is an endpoint of an edge
def est_noeud_extremite(graph, node):
    return graph.degree[node] == 1

# Function to propagate adjustments of lanes values
def propager_ajustements(graph, limite, drone):
    ajustements_effectues = False
    total = 0
    for u, v, key, data in graph.edges(keys=True, data=True):
        print(u, v)
        node_u_data = graph.nodes[u]
        node_v_data = graph.nodes[v]
    
        lat_u, lon_u = node_u_data['y'], node_u_data['x']
        lat_v, lon_v = node_v_data['y'], node_v_data['x']
        nb_km =nb_Km(lat_u,lon_u,lat_v,lon_v)
        total+=nb_km
        drone.calculate_cost(nb_km)
    print(total)
    return ajustements_effectues



test = Drone()
# Loop to propagate adjustments until all edges > limite are accessible by other edges > limite
while propager_ajustements(graph, 7,test):
    pass


edge_lanes = [data['lanes'] for u, v, key, data in graph.edges(keys=True, data=True)]

# Create a list of colors for each edge based on lanes values
edge_colors = [cmap(norm(lanes)) if lanes >= 7 else 'black' for lanes in edge_lanes]

# Convert color strings to RGBA tuples
edge_colors_rgba = [mcolors.to_rgba(color) for color in edge_colors]

# Plot the graph using GeoPandas
gdf_edges = ox.graph_to_gdfs(graph, nodes=False)

# Create a GeoDataFrame for edges
gdf_edges['color'] = edge_colors_rgba

# Plot the edges
ax = gdf_edges.plot(color=gdf_edges['color'], linewidth=2, alpha=0.7)
plt.show()
# Display the plot

print("size = ", utils.size(graph))

for edge in graph.edges():
    print(edge)"""

