import networkx as nx
import osmnx as ox
import matplotlib.pyplot as plt


def premier_choix():

    choix = 0
    while (choix != 1 and choix != 2):
        choix = int(input("Tapez 1 ou 2 : "))
        if (choix != 1 and choix != 2):
            print("La valeur donnée ne correspond pas à une réponse.")
    return choix

def drone():
    print("\n\nVous avez choisit de parcourir Montréal avec le drone. Pour le Drone nous avons fait le choix dans ce script de dire que sa vitesse est infiniment grande, nous ne la prendront donc pas en compte.")
    choix = 0
    while (choix != 1 and choix != 2 and choix != 3):
        print("Nous vous proposons 3 algorithme différents :\n[1] Cycle Eulérien : Rajoute des arêtes, ne sera lancé que sur les quartiers et non sur la ville entière uniqument sur les routes pour les voitures, peut prendre jusqu'à 20min d'éxécution\n[2] TSP : ne sera lancé que sur les quartiers et non sur la ville entière, sur toutes les routes (routes piétonnes, ...), peut prendre jusqu'à 4 heures d'exécution\n[3] BFS : Sera lancé sur tout montréal sur toutes les routes, environ 3 minutes")
        choix = int(input("Tapez 1, 2 ou 3 : "))
        if (choix != 1 and choix != 2 and choix != 3):
            print("La valeur donnée ne correspond pas à une réponse.")
    if choix == 1 :
        print("Vous avez choisis l'algorithme du cycle eulérien, calcul en cours, cela peut prendre plusieurs minute (environ 20minutes)")
        distance_Outremont, parcours_Outremont = eulerian("Outremont, Montréal, Canada")
        distance_Verdun, parcours_Verdun = eulerian("Verdun, Montréal, Canada")
        distance_Saint, parcours_Saint = eulerian("Saint-Léonard, Montréal, Canada")
        distance_Rivière, parcours_Rivière = eulerian("Rivière-des-prairies-pointe-aux-trembles, Montréal, Canada")
        distance_Plateau, parcours_Plateau = eulerian("Plateau-Mont-Royal, Montréal, Canada")
        distance_Outremont /= 1000
        distance_Verdun /= 1000
        distance_Saint /= 1000
        distance_Rivière /= 1000
        distance_Plateau /= 1000
        choix2 = 0
        print("\n\nLe calcul est terminé ! Des fichier png ont été enregistrés dans le dossier drone_eulerian/ ils correpondent au chemin parcouru par le drone en Bleu du clair au foncé en focntionde l'ordre dans lequel l'arête a été parcourue, si il y a du gris c'est une arête non parcourue\n Les résultats pour le cycle Eulerien en mode 'drive' uniqument :")
        print("Distance et coût :")
        print("Pour Outremont : ")
        print("La distance paroucue est : " + str(distance_Outremont) + " kilomètres.")
        print("Le coût serait donc de (sans prendre en compte le coût a la journée): " + str(distance_Outremont * 0.01 )+ " euros.")
        print("Pour Verdun : ")
        print("La distance paroucue est : " + str(distance_Verdun) + " kilomètres.")
        print("Le coût serait donc de (sans prendre en compte le coût a la journée): "  + str(distance_Verdun * 0.01) + " euros.")
        print("Pour Saint-Léonard : ")
        print("La distance paroucue est : " + str(distance_Saint) + " kilomètres.")
        print("Le coût serait donc de (sans prendre en compte le coût a la journée): "+str(distance_Saint * 0.01) + " euros.")
        print("Pour Rivière-des-prairies-pointe-aux-trembles : ")
        print("La distance paroucue est : " + str(distance_Rivière) + " kilomètres.")
        print("Le coût serait donc de (sans prendre en compte le coût a la journée): " + str(distance_Rivière * 0.01) + " euros.")
        print("Pour Plateau-Mont-Royal : ")
        print("La distance paroucue est : " + str(distance_Plateau) + " kilomètres.")
        print("Le coût serait donc de (sans prendre en compte le coût a la journée): " +str(distance_Plateau * 0.01) + " euros.")
        print("Total : ")
        print("La distance totale paroucue est : " + str(distance_Outremont + distance_Plateau + distance_Verdun + distance_Rivière + distance_Saint) + " kilomètres.")
        print("Le coût serait donc de: " + str((distance_Outremont + distance_Plateau + distance_Verdun + distance_Rivière + distance_Saint) * 0.01 + 100 )+ " euros.")
    if choix == 2:
        print("Vous avez choisis l'algorithme TSP, calcul en cours, cela peut prendre plusieurs heures (eniron 4heures)")
        distance_Outremont, parcours_Outremont = parcourt_tsp("Outremont, Montréal, Canada")
        distance_Verdun, parcours_Verdun = parcourt_tsp("Verdun, Montréal, Canada")
        distance_Saint, parcours_Saint = parcourt_tsp("Saint-Léonard, Montréal, Canada")
        distance_Rivière, parcours_Rivière = parcourt_tsp("Rivière-des-prairies-pointe-aux-trembles, Montréal, Canada")
        choix2 = 0
        distance_Plateau, parcours_Plateau = parcourt_tsp("Plateau-Mont-Royal, Montréal, Canada")
        distance_Outremont /= 1000
        distance_Verdun /= 1000
        distance_Saint /= 1000
        distance_Rivière /= 1000
        distance_Plateau /= 1000
        while (choix2 != 1 and choix2 != 2 and choix2 != 3):
            print("\n\nLe calcul est terminé, des fichier png ont été enregistrés dans le dossier drone_tsp/ ils correpondent au chemin parcouru par le drone en Bleu du clair au foncé en focntionde l'ordre dans lequel l'arête a été parcourue, si il y a du gris c'est une arête non parcourue,\n[1] Vous voulez afficher les valeurs coût et temps brutes.\n[2] Après calcul avec coefficient de 1,5.\n[3] Les deux.")
            choix2 = int(input("Tapez 1, 2 ou 3 : "))
            if (choix2 != 1 and choix2 != 2 and choix2 != 3):
                print("La valeur donnée ne correspond pas à une réponse.")
        if (choix2 == 1 or choix2 == 3):
            print("Distance et coût sans remise à niveau par rapport au cycle eulérien :")
            print("Pour Outremont : ")
            print("La distance paroucue est : " + str(distance_Outremont) + " kilomètres.")
            print("Le coût serait donc de (sans prendre en compte le coût a la journée): " +str(distance_Outremont * 0.01) + " euros.")
            print("Pour Verdun : ")
            print("La distance paroucue est : " + str(distance_Verdun) + " kilomètres.")
            print("Le coût serait donc de (sans prendre en compte le coût a la journée): " +str(distance_Verdun * 0.01) + " euros.")
            print("Pour Saint-Léonard : ")
            print("La distance paroucue est : " + str(distance_Saint) + " kilomètres.")
            print("Le coût serait donc de (sans prendre en compte le coût a la journée): " +str(distance_Saint * 0.01) + " euros.")
            print("Pour Rivière-des-prairies-pointe-aux-trembles : ")
            print("La distance paroucue est : " + str(distance_Rivière) + " kilomètres.")
            print("Le coût serait donc de (sans prendre en compte le coût a la journée): "+str(distance_Rivière * 0.01) + " euros.")
            print("Pour Plateau-Mont-Royal : ")
            print("La distance paroucue est : " + str(distance_Plateau) + " kilomètres.")
            print("Le coût serait donc de (sans prendre en compte le coût a la journée): " +str(distance_Plateau * 0.01 )+ " euros.")
            print("Total : ")
            print("La distance totale paroucue est : " + str(distance_Outremont + distance_Plateau + distance_Verdun + distance_Rivière + distance_Saint) + " kilomètres.")
            print("Le coût serait donc de : " +  str((distance_Outremont + distance_Plateau + distance_Verdun + distance_Rivière + distance_Saint) * 0.01 + 100) + " euros.")

        if (choix2 == 2 or choix2 == 3):
            print("Distance et coût avec remise à niveau par rapport au cycle eulérien :")
            print("Pour Outremont : ")
            print("La distance paroucue est : " + str(distance_Outremont * 1.5) + " kilomètres.")
            print("Le coût serait donc de (sans prendre en compte le coût a la journée): "+ str(distance_Outremont * 1.5* 0.01) + " euros.")
            print("Pour Verdun : ")
            print("La distance paroucue est : " + str(distance_Verdun* 1.5) + " kilomètres.")
            print("Le coût serait donc de (sans prendre en compte le coût a la journée): " +str(distance_Verdun* 1.5 * 0.01 )+ " euros.")
            print("Pour Saint-Léonard : ")
            print("La distance paroucue est : " + str(distance_Saint* 1.5) + " kilomètres.")
            print("Le coût serait donc de (sans prendre en compte le coût a la journée): " +str(distance_Saint* 1.5 * 0.01) + " euros.")
            print("Pour Rivière-des-prairies-pointe-aux-trembles : ")
            print("La distance paroucue est : " + str(distance_Rivière* 1.5) + " kilomètres.")
            print("Le coût serait donc de (sans prendre en compte le coût a la journée): " +str(distance_Rivière* 1.5 * 0.01 )+ " euros.")
            print("Pour Plateau-Mont-Royal : ")
            print("La distance paroucue est : " + str(distance_Plateau * 1.5) + " kilomètres.")
            print("Le coût serait donc de (sans prendre en compte le coût a la journée): " +str(distance_Plateau* 1.5 * 0.01 )+ " euros.")
            print("Total : ")
            print("La distance totale paroucue est : " + str(distance_Outremont* 1.5 + distance_Plateau* 1.5 + distance_Verdun * 1.5+ distance_Rivière* 1.5 + distance_Saint* 1.5 )+ " kilomètres.")
            print("Le coût serait donc de : " + str((distance_Outremont* 1.5 + distance_Plateau* 1.5 + distance_Verdun * 1.5+ distance_Rivière * 1.5+ distance_Saint* 1.5) * 0.01 + 100) + " euros.")
    if choix == 3:
        print("\n\nVous avez choisi le parcours BFS pour l'ensemble de la ville, calcul en cours, cela sera rapide, environ trois minute: ")
        distance, parcours = bfs_drone()
        distance /= 1000
        cout = str(distance * 0.01 + 100)
        print("Calcul terminé,\nLa distance parcourue est de " + str(distance) + "kilomètres\nLe coût sera de : " + cout +" euros.\nAttention, un parcours bfs n'est pas un cycle.\nUn graphe montrant le parcours du drone en bleu et le zones non parcourues en gris s'est enregistré sous le format chemin_Montréal_drone.png dans le dossier drone_bfs/")

         
        
        


def bfs_drone():
    place_name = " Outremont, Montréal, Canada"

    graph = ox.graph_from_place(place_name, network_type="drive")


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
    return total_distance, path_graph

def eulerian(place_name):
    graph = ox.graph_from_place(place_name, network_type='drive')
    total_distance = 0

    G = graph.to_undirected()

    G = nx.eulerize(G)
    print(total_distance)
    eulerian_cycle = nx.eulerian_circuit(G)
    shortest_distance = 0
    
    total_distance = sum(G[u][v][0]['length'] for u, v in eulerian_cycle)
    tsp_graph = G.subgraph(G)

    edge_colors = plt.cm.Blues(range(len(tsp_graph.edges())))
    fig, ax = ox.plot_graph(ox.project_graph(graph),  show=False, edge_color='gray', node_color='none')
    fig, ax = ox.plot_graph(ox.project_graph(tsp_graph), ax=ax, edge_color=edge_colors, node_size=10, bgcolor='white', node_color='none')
    #plt.savefig('drone_eulerian/' +place_name + 'eulerian.png', bbox_inches='tight')
    print(list(eulerian_cycle))
    return total_distance, eulerian_cycle


def parcourt_tsp(place_name):
    graph = ox.graph_from_place(place_name, network_type='all')
    G = graph.to_undirected()
    tsp_path = nx.approximation.traveling_salesman_problem(G)
    total_distance = sum(G[u][v][0]['length'] for u, v in zip(tsp_path[:-1], tsp_path[1:]))
    tsp_graph = G.subgraph(tsp_path)
    start_node = tsp_path[0]
    end_node = tsp_path[-1]
    edge_colors = plt.cm.Blues(range(len(tsp_graph.edges())))
    node_colors = ['red' if node == start_node else 'green' if node == end_node else 'gray' for node in G.nodes()]
    fig, ax = ox.plot_graph(ox.project_graph(graph),  show=False, edge_color='gray', node_color='none')
    fig, ax = ox.plot_graph(ox.project_graph(tsp_graph), ax=ax, edge_color=edge_colors, node_size=10, bgcolor='white', node_color='none')
    plt.savefig('drone_tsp/chemin_' + place_name +'_tsp.png', bbox_inches='tight')
    return total_distance, tsp_path

def calc_nb_den(dist):
    t1 = 0
    t2 = 0
    const_dist = dist
    t = 0
    c = 0
    while (dist > 0):
        if (dist > 80):
            if (dist <= 160):
                t = dist /(40 * (t2 + 1))
            t2+=1
        else:
            t1+=1
            if (t2 != 0):
                t = 4 
            else :
                t = dist / 20
        dist -= 160

    if (t1 == 0) :
        c = t2 * 800 + const_dist * 1.3
    else:
        if (t2 == 0):
            c = 500 + 1.1 * const_dist
        else :
            c = t2 * 800 + t1 * 500 + 160 * t2 * 1.3 + (const_dist-160*t2) * 1.1
    return t1,t2,t,c



def déneigeuse():
    print("Vous avez choisi la simulation des déneigeuses :\nPréférez vous un parcours DFS ou un parcourt BFS, sachant que le parcourt DFS et plus efficace :\n[1] BFS\n[2] DFS")
    choix = 0
    while (choix != "1" and choix != "2"):
        choix = input("Tapez 1 ou 2 : ")
        if (choix != "1" and choix != "2"):
            print("La valeur donnée ne correspond pas à une réponse.")
    if choix == "1" :
        print("\n\nVous avez choisi un parcours BFS, calcul de la distance, du temps, du nombre de déneigeuse et du coût, cela devrait être assez rapide :")
        distance_Outremont, parcours_Outremont = den_bfs("Outremont, Montréal, Canada")
        distance_Verdun, parcours_Verdun = den_bfs("Verdun, Montréal, Canada")
        distance_Saint, parcours_Saint = den_bfs("Saint-Léonard, Montréal, Canada")
        distance_Rivière, parcours_Rivière = den_bfs("Rivière-des-prairies-pointe-aux-trembles, Montréal, Canada")
        distance_Plateau, parcours_Plateau = den_bfs("Plateau-Mont-Royal, Montréal, Canada")
        distance_Outremont /= 1000
        distance_Verdun /= 1000
        distance_Saint /= 1000
        distance_Rivière /= 1000
        distance_Plateau /= 1000
        t1_O, t2_O, t_O,c_O = calc_nb_den(distance_Outremont)
        t1_V, t2_V, t_V,c_V = calc_nb_den(distance_Verdun)
        t1_S, t2_S, t_S,c_S = calc_nb_den(distance_Saint)
        t1_R, t2_R, t_R,c_R = calc_nb_den(distance_Rivière)
        t1_P, t2_P, t_P,c_P = calc_nb_den(distance_Plateau)
        print("\n\nCalcul terminé !\nUn graphe pour chaque quartier s'est enregistré dans le dossier den_bfs/. Il représente juste le parcours global qu'il faut faire : en rouge clair la ou le chemin commence et il se fonce petit à petit pour montrer le parcours, les arêtes grise représentent les arêtes non parcourues, les déneigeuses partant chacune là où la précédente termine, ce n'est pas affiché sur le graphe\nDistance, nombre de déneigeuse et coût :")
        print("\nPour Outremont : ")
        print("La distance paroucue est : " + str(distance_Outremont) + " kilomètres.\nLe nombre de déneigeuse nécessaire est : " + str(t1_O) + " type1 et " + str(t2_O) + " type2.\nLe temps nécessaire pour déneiger le quartier est : " + str(t_O) +" heures\nLe coût serait de " + str(c_O) +" euros.")
        print("\nPour Verdun : ")
        print("La distance paroucue est : " + str(distance_Verdun) + " kilomètres.\nLe nombre de déneigeuse nécessaire est : " + str(t1_V) + " type1 et " + str(t2_V) + " type2.\nLe temps nécessaire pour déneiger le quartier est : " + str(t_V) +" heures\nLe coût serait de " + str(c_V) +" euros.")
        print("\nPour Saint-Léonard : ")
        print("La distance paroucue est : " + str(distance_Saint) + " kilomètres.\nLe nombre de déneigeuse nécessaire est : " + str(t1_S) + " type1 et " + str(t2_S) + " type2.\nLe temps nécessaire pour déneiger le quartier est : " + str(t_S) +" heures\nLe coût serait de " + str(c_S) +" euros.")
        print("\nPour Rivière-des-prairies-pointe-aux-trembles : ")
        print("La distance paroucue est : " + str(distance_Rivière) + " kilomètres.\nLe nombre de déneigeuse nécessaire est : " + str(t1_R) + " type1 et " + str(t2_R) + " type2.\nLe temps nécessaire pour déneiger le quartier est : " + str(t_R) +" heures\nLe coût serait de " + str(c_R) +" euros.")
        print("\nPour Plateau-Mont-Royal : ")
        print("La distance paroucue est : " + str(distance_Plateau) + " kilomètres.\nLe nombre de déneigeuse nécessaire est : " + str(t1_P) + " type1 et " + str(t2_P) + " type2.\nLe temps nécessaire pour déneiger le quartier est : " + str(t_P) +" heures\nLe coût serait de " + str(c_P) +" euros.")
        print("\nTotal : ")
        print("La distance totale paroucue est : " + str(distance_Plateau +distance_Plateau + distance_Saint +  distance_Verdun + distance_Outremont) + " kilomètres.\nLe nombre de déneigeuse nécessaire est : " + str(t1_P + t1_S + t1_V + t1_O + t1_R) + " type1 et " + str(t2_P + t2_O+t2_R+t2_S+t2_V) + " type2.\nLe temps nécessaire pour déneiger le quartier est : " + str(max(max(t_P, t_V),max(max( t_O, t_R),t_S))) +" heures\nLe coût serait de " + str(c_P + c_S + c_O +c_R + c_V) +" euros.")
    else :
        print("\n\nVous avez choisi un parcours DFS, calcul de la distance, du temps, du nombre de déneigeuse et du coût, cela devrait être assez rapide :")
        distance_Outremont, parcours_Outremont = den_dfs("Outremont, Montréal, Canada")
        distance_Verdun, parcours_Verdun = den_dfs("Verdun, Montréal, Canada")
        distance_Saint, parcours_Saint = den_dfs("Saint-Léonard, Montréal, Canada")
        distance_Rivière, parcours_Rivière = den_dfs("Rivière-des-prairies-pointe-aux-trembles, Montréal, Canada")
        distance_Plateau, parcours_Plateau = den_dfs("Plateau-Mont-Royal, Montréal, Canada")
        distance_Outremont /= 1000
        distance_Verdun /= 1000
        distance_Saint /= 1000
        distance_Rivière /= 1000
        distance_Plateau /= 1000
        t1_O, t2_O, t_O,c_O = calc_nb_den(distance_Outremont)
        t1_V, t2_V, t_V,c_V = calc_nb_den(distance_Verdun)
        t1_S, t2_S, t_S,c_S = calc_nb_den(distance_Saint)
        t1_R, t2_R, t_R,c_R = calc_nb_den(distance_Rivière)
        t1_P, t2_P, t_P,c_P = calc_nb_den(distance_Plateau)
        print("\n\nCalcul terminé !\nUn graphe pour chaque quartier s'est enregistré dans le dossier den_dfs. Il représente juste le parcours global qu'il faut faire : en rouge clair la ou le chemin commence et il se fonce petit à petit pour montrer le parcours, les arêtes grise représentent les arêtes non parcourues, les déneigeuses partant chacune là où la précédente termine, ce n'est pas affiché sur le graphe\nDistance, nombre de déneigeuse et coût :")
        print("\nPour Outremont : ")
        print("La distance paroucue est : " + str(distance_Outremont) + " kilomètres.\nLe nombre de déneigeuse nécessaire est : " + str(t1_O) + " type1 et " + str(t2_O) + " type2.\nLe temps nécessaire pour déneiger le quartier est : " + str(t_O) +" heures\nLe coût serait de " + str(c_O) +" euros.")
        print("\nPour Verdun : ")
        print("La distance paroucue est : " + str(distance_Verdun) + " kilomètres.\nLe nombre de déneigeuse nécessaire est : " + str(t1_V) + " type1 et " + str(t2_V) + " type2.\nLe temps nécessaire pour déneiger le quartier est : " + str(t_V) +" heures\nLe coût serait de " + str(c_V) +" euros.")
        print("\nPour Saint-Léonard : ")
        print("La distance paroucue est : " + str(distance_Saint) + " kilomètres.\nLe nombre de déneigeuse nécessaire est : " + str(t1_S) + " type1 et " + str(t2_S) + " type2.\nLe temps nécessaire pour déneiger le quartier est : " + str(t_S) +" heures\nLe coût serait de " + str(c_S) +" euros.")
        print("\nPour Rivière-des-prairies-pointe-aux-trembles : ")
        print("La distance paroucue est : " + str(distance_Rivière) + " kilomètres.\nLe nombre de déneigeuse nécessaire est : " + str(t1_R) + " type1 et " + str(t2_R) + " type2.\nLe temps nécessaire pour déneiger le quartier est : " + str(t_R) +" heures\nLe coût serait de " + str(c_R) +" euros.")
        print("\nPour Plateau-Mont-Royal : ")
        print("La distance paroucue est : " + str(distance_Plateau) + " kilomètres.\nLe nombre de déneigeuse nécessaire est : " + str(t1_P) + " type1 et " + str(t2_P) + " type2.\nLe temps nécessaire pour déneiger le quartier est : " + str(t_P) +" heures\nLe coût serait de " + str(c_P) +" euros.")
        print("\nTotal : ")
        print("La distance totale paroucue est : " + str(distance_Plateau +distance_Plateau + distance_Saint +  distance_Verdun + distance_Outremont) + " kilomètres.\nLe nombre de déneigeuse nécessaire est : " + str(t1_P + t1_S + t1_V + t1_O + t1_R) + " type1 et " + str(t2_P + t2_O+t2_R+t2_S+t2_V) + " type2.\nLe temps nécessaire pour déneiger le quartier est : " + str(max(max(t_P, t_V),max(max( t_O, t_R),t_S))) +" heures\nLe coût serait de " + str(c_P + c_S + c_O +c_R + c_V) +" euros.")

total_distance = 0
def den_dfs(place_name) :
    graph = ox.graph_from_place(place_name, network_type="drive")

    graph = graph.to_directed()

    visited = {}
    

    path_graph = nx.DiGraph()

    path_graph.graph["crs"] = graph.graph["crs"]
    def dfs(graph, node, distance):
        global total_distance

        visited[node] = True
        path_graph.add_node(node)

        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                edge_data = graph.get_edge_data(node, neighbor)
                edge_distance = edge_data[0]['length']

                total_distance += edge_distance  

                path_graph.add_edge(node, neighbor, length=edge_distance)

                dfs(graph, neighbor, total_distance)

    start_node = list(graph.nodes())[0]

    dfs(graph, start_node, 0)


    tsp_graph = graph.subgraph(path_graph)

    edge_colors = plt.cm.Reds(range(len(tsp_graph.edges())))

    fig, ax = ox.plot_graph(ox.project_graph(graph),  show=False, edge_color='gray', node_color='none')
    fig, ax = ox.plot_graph(ox.project_graph(tsp_graph), ax=ax,edge_color=edge_colors, node_size=10, bgcolor='white', node_color='none')


    plt.savefig('den_dfs/' + place_name+ '_dendfs', bbox_inches='tight')
    return total_distance, path_graph
def den_bfs(place_name):
    graph = ox.graph_from_place(place_name, network_type="drive")

    graph = graph.to_directed()

    visited = {}

    path_graph = nx.DiGraph()

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
                    if neighbor not in visited:
                        edge_data = graph.get_edge_data(node, neighbor)
                        edge_distance = edge_data[0]['length']
                        
                        path_graph.add_edge(node, neighbor, length=edge_distance)
                        
                        queue.append((neighbor, distance + edge_distance))  


    start_node = list(graph.nodes())[0]

    bfs(graph, start_node)

    total_distance = sum([data['length'] for u, v, data in path_graph.edges(data=True)])


    tsp_graph = graph.subgraph(path_graph)

    edge_colors = plt.cm.Reds(range(len(tsp_graph.edges())))

    fig, ax = ox.plot_graph(ox.project_graph(graph),  show=False, edge_color='gray',  node_color='none')
    fig, ax = ox.plot_graph(ox.project_graph(tsp_graph), ax=ax, edge_color=edge_colors, node_size=10, bgcolor='white', node_color='none')

    plt.savefig('den_bfs/' + place_name + '_denbfs.png', bbox_inches='tight') 
    return total_distance, path_graph


def script():
    while(True):
        choix = premier_choix()
        
        if (choix== 1):
            drone( )
        
        déneigeuse()
        print("\n\nVous avez désormais terminé cette simulation.\nVous pouvez continuer pour tester d'autre choix ou effecteur controle C pour quitter\nPour continuer a tester :\n[1] Simulation Drone.\n[2] Simulation Déneigeuse.")
script()