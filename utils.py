import math

import osmnx.stats


def nb_Km(lat1,lon1,lat2,lon2):
        # Rayon de la Terre en kilomètres
    R = 6371.0

    # Convertir les degrés en radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Différences de latitude et de longitude
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Formule de haversine
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance en kilomètres
    distance = R * c

    return distance

# Returns the size of the graph = the total length of all the edges
def size(G):
    osmnx.distance.add_edge_lengths(G)
    return osmnx.stats.edge_length_total(G)

def isSet(l):
    seen = []
    is_set = True
    for x, y in l:
        if x in seen or y in seen:
            is_set = False
            break
        seen.append(x)
        seen.append(y)
    return is_set

def filterSet(predicate, iterable):
    for x in iterable:
        if predicate(x):
            yield x