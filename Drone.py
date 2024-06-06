import networkx as nx
import osmnx as ox
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random

from utils import *

class Drone:
    total_cost = 100
    total_km = 0
    secteur = Secteurs[1]
    def __init__(self, cost_per_km=0.01):
        self.cost_per_km = cost_per_km

    def SetSecteur(self, secteur):
        self.secteur=secteur
    def Set_km(self,km):
        self.total_km += km
        self.total_cost+=km*self.cost_per_km
    def bfs_drone(self):

        graph = ox.graph_from_place(self.secteur, network_type="drive")


        visited = {}

        path_graph = nx.Graph()

        path_graph.graph["crs"] = graph.graph["crs"]

        def bfs(graph, start):
            queue = [] 
            queue.append((start, 0)) 
            
            while queue:
                node, distance = queue.pop(0)
                
                if node not in visited:
                    visited[node] = True
                    
                    path_graph.add_node(node)
                    
                    for neighbor in graph.neighbors(node):
                        if neighbor not in visited or path_graph.has_edge(neighbor, node):
                            edge_data = graph.get_edge_data(node, neighbor)
                            edge_distance = edge_data[0]['length']
                            path_graph.add_edge(node, neighbor, length=edge_distance)
                            queue.append((neighbor, distance + edge_distance))

        start_node = list(graph.nodes())[0]

        bfs(graph, start_node)

        total_distance = sum([data['length'] for u, v, data in path_graph.edges(data=True)])


        tsp_graph = graph.subgraph(path_graph)

        edge_colors = plt.cm.Reds(range(len(tsp_graph.edges())))

        fig, ax = ox.plot_graph(ox.project_graph(graph), show=False, edge_color='gray', node_color='none')
        fig, ax = ox.plot_graph(ox.project_graph(tsp_graph), ax=ax, edge_color=edge_colors, node_size=10, bgcolor='white', node_color='none')

        #plt.savefig('drone_bfs/' + place_name  + 'dronebfs.png', bbox_inches='tight')
        self.Set_km(total_distance/1000)
        return path_graph

    def eulerian(self):
        graph = ox.graph_from_place(self.secteur, network_type='drive')
        total_distance = 0

        G = graph.to_undirected()

        G = nx.eulerize(G)

        eulerian_cycle = nx.eulerian_circuit(G)
        shortest_distance = 0
        res= list(eulerian_cycle)
        total_distance = sum(G[u][v][0]['length'] for u, v in eulerian_cycle)
        tsp_graph = G.subgraph(G)

        for u, v, key, data in graph.edges(keys=True, data=True):
            data['lanes'] = random.uniform(2.5, 15) # height of snow = weight of the edge

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
        plt.savefig('drone/' +self.secteur.split(',')[0] + '_eulerian.png', bbox_inches='tight')
        self.Set_km(total_distance/1000)
        
        return res

    

