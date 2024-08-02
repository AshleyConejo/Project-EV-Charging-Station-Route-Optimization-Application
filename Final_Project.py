import networkx as nx


Graphing = nx.read_edgelist("network_edges_1.txt",nodetype=str,data=(("weight", int),))
shortest_path = {}
all_paths = {}

class Dijkstra_Algorithm():
    def __init__(self):
        self

        
    def searching_process(self,starting_point): 
        charging_stations = ['H', 'K', 'Q', 'T']
        
        for i in Graphing:
                 if i in charging_stations:
                  road = nx.dijkstra_path(Graphing, starting_point, i)
                  distance = nx.dijkstra_path_length(Graphing, starting_point, i)
                  shortest_path[i] = (road, distance)

        nearest_station = min(shortest_path, key=lambda i: shortest_path[i][1])
        best_path, min_length = shortest_path[nearest_station]
        return nearest_station, best_path, min_length

    def allshort_paths(self,starting_point):
         charging_stations = ['H', 'K', 'Q', 'T']
        
         for i in Graphing:
                 if i in charging_stations:
                  roads = list(nx.all_shortest_paths(Graphing, starting_point, i, weight='weight', method='dijkstra' ))
                  distance = nx.dijkstra_path_length(Graphing, starting_point, i)
                  all_paths[i] = (roads, distance)
                  testing_stations = roads
                  all_paths[i] = (testing_stations, distance)
         return all_paths        

 
algorithm_object = Dijkstra_Algorithm()

while True:
    print("Dijkstra's Algorithm")
    start_position =  input("Pick a starting point from A to W: ").strip().upper()
    nearest_station, best_path, min_length  = algorithm_object.searching_process(start_position)
    test = algorithm_object.allshort_paths(start_position)

     
    
    for station, (paths, distance) in test.items():
      print(f"The shortest path to the charging station {station} is:")
      print(f"Path: {paths} with a total distance of {distance}")
      print()

    print(f"The most efficient route to the closest charging station {nearest_station} is:")
    print(f"Path: {best_path} with a total distance of {min_length}.")
    print()
  
        