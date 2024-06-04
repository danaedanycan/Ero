import sys

import osmnx as ox
import networkx as nx

import utils
from utils import nb_Km
import itertools as iter
from numpy import ceil


# Step 1 : We find all the vertices with odd degree
def odd_vertices(G):
    odd_nodes = []
    for node in G.nodes():
        if G.degree[node] % 2 == 1:
            odd_nodes.append(node)
    return odd_nodes

def n(G):
    return len(odd_vertices(G))

# Step 2 : List all possible pairings of odd vertices
#          For n odd vertices total number of pairings
#          possible are, (n-1) * (n-3) * (n -5)... * 1

#   List all the pairs
def pairs(oddNodes):
    pairings = []
    for i in range(len(oddNodes)):
        for j in range(i + 1, len(oddNodes)):
            pairings.append((oddNodes[i], oddNodes[j]))
    return pairings

def groups(pairs, G):
    comb = iter.combinations(pairs, int(ceil(n / 2)))
    print("COMB = ", list(comb))
    print("Combination is OK")
    return utils.filterSet(utils.isSet, comb)



# Step 4 : For each set of pairings, find the shortest
#          path connecting them.

#Take only the paths with key = 0
def compute_edge_weight(G, u, v, k):
     return G.edges[u, v, k]['length']


def computeCoupleWeight(G, u, v):
    total_weight = 0
    if nx.has_path(G, u, v):
        shortest_path = nx.shortest_path(G, u, v, 'length')
        if len(shortest_path) == 1:
            total_weight = G.edges[u, v, 0]['length']
        for i in range(len(shortest_path) - 1):
            u = shortest_path[i]
            v = shortest_path[i + 1]
            total_weight += G.edges[u, v, 0]['length']
    return total_weight


def computeGroupWeight(G, group):
    total_weight = 0
    for couple in group:
        (u, v) = couple
        total_weight += computeCoupleWeight(G, u, v)
    return total_weight


# Step 5 : Find the pairing with minimum shortest path
#          connecting pairs.
def getCheapestGroup(G, groups):
    if len(groups) == 0:
        return []
    cheapestGroup = groups[0]
    minLength = sys.maxsize
    for group in groups:
        length = computeGroupWeight(G, group)
        if minLength > length > 0:
            minLength = length
            cheapestGroup = group
    return cheapestGroup


# Step 6 : Modify the graph by adding all the edges that
#          have been found in step 5.
def addEdges(G, group):
    for u, v in group:
        if nx.has_path(G, u, v):
            shortestPath = nx.shortest_path(G, u, v)
            if len(shortestPath) == 1:
                G.add_edge(u, v, length=compute_edge_weight(G, u, v))
            for i in range(len(shortestPath) - 1):
                w = shortestPath[i]
                x = shortestPath[i + 1]
                G.add_edge(w, x, 1, length=compute_edge_weight(G, w, x))


place_name = "Outremont, Montreal, Canada"

G = ox.graph_from_place(place_name, network_type="drive")


vertices = odd_vertices(G)
n = len(vertices)
pairs = pairs(vertices)
print("pairs = ", len(pairs))
gps = groups(pairs, G)
print("groups = ", list(gps))
# g = getCheapestGroup(G, gps)
# print("group = ", g)
# print(G)
# print("degree  = ", G.degree[11009055923])
# G.add_edge(11009055923, 11778731416, 0)
#
# G.add_edge(11009055923, 11778731416, 1)
# G.add_edge(11009055923, 11778731416, 2)
# G.add_edge(11009055923, 11778731416, 3)
# print("degree  = ", G.degree[11009055923])
#
# print(G)

# pairs = pairs(odd_vertices(G))
# print(simpleGroup(pairs))
# print("odds = ", len(odd_vertices(G)))
# for pair in simpleGroup(pairs):
#     G.add_edge(pair[0], pair[1], 1)
# print("odds = ", len(odd_vertices(G)))
#
# totalKm = 0 # kMeters
# for u, v, k, data in G.edges(data=True, keys=True):
#     lat_u, lon_u = G.nodes[u]['y'], G.nodes[u]['x']
#     lat_v, lon_v = G.nodes[v]['y'], G.nodes[v]['x']
#     totalKm += nb_Km(lat_u, lon_u, lat_v, lon_v)
# print("total Km = ", totalKm)