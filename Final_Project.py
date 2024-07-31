import networkx as nx

Graphing = nx.read_edgelist("network_edges_1.txt",nodetype=str,data=(("weight", int),))
shortest_path = {}

class Dijkstra_Algorithm():
    def __init__(self):
        self

        
    def searchin_process(self,starting_point): 
        charging_stations = ['H', 'K', 'Q', 'T']
        
        for i in Graphing:
                 if i in charging_stations:
                  road = nx.dijkstra_path(Graphing, starting_point, i)
                  distance = nx.dijkstra_path_length(Graphing, starting_point, i)
                  shortest_path[i] = (road, distance)

        nearest_station = min(shortest_path, key=lambda i: shortest_path[i][1])
        best_path, min_length = shortest_path[nearest_station]
        return nearest_station, best_path, min_length

    def efficient_path(self):
        
        return self.searchin_process(starting_point= input())
    
algorithm_object = Dijkstra_Algorithm()

while True:
    print("Dijkstra's Algorithm")
    start_position =  input("Pick a starting point from A to W: ").strip().upper()
    nearest_station, best_path, min_length  = algorithm_object.searchin_process(start_position)
     
    print(f"The most efficient route is to the charging station at {nearest_station}.")
    print(f"Path: {best_path} with total distance {min_length}.")
