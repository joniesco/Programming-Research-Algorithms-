from sys import maxsize
from itertools import permutations
from collections import defaultdict
from typing import Callable, Any
import unittest
from unittest import TestCase

"""
in this question we write a sistem that give some solutions to the known  TSP and supports:
•  two types of input -  distances only, or also names of cities.
•  two types of output - the entire route, or just the length of the route.
•  two algorithms. Greedy and brute force. 

**Input:
 # we check if the input is only weights or city names and weights , if we get a tuple-
    # it means that in the first place we have a list of city names and in the second place we have a matrix with all the distances
    # otherwise our graph is just a matrix of distances 
    
    **Output:
    there are two types the entire route, or just the length of the route.
    our 2 algorithm returns the path and the weight so in case we want the path we will 
    
    algorithms:
    1.Greedy - every time go to the chipest city. Complixety- O(N2*log2N)
    2. brutforce -  calculate al pathes and take the cheepest . Complixety-O(n!)
"""


# main algorithm system
def travellingSalesmanProblem(algorithm: Callable, graph: tuple, s: int, output_type: int):
    if isinstance(graph, tuple):  # city names + weights
        city_names, dist_matrix = graph
    else:  # only weights
        city_names, dist_matrix = ([i for i in range(len(graph))], graph)
    if output_type == 1:
        return algorithm(dist_matrix, city_names, s)
    if output_type == 0:
        return algorithm(dist_matrix, dist_matrix[1], s)


# implementation of traveling Salesman Problem Brute Force (BF) Based on
# https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/
def bruteForce(graph, city_names, s):
    # store all vertex apart from source vertex
    vertex = []
    for i in range(len(graph)):
        if i != s:
            vertex.append(i)
    # store minimum weight Hamiltonian Cycle
    min_path_weight = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:
        # store current Path weight(cost)
        current_pathweight = 0
        current_path = [city_names[s]]
        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
            current_path.append(city_names[k])
        current_pathweight += graph[k][s]
        # update minimum
        if current_pathweight < min_path_weight:
            min_path_weight = current_pathweight
            min_path = current_path
    print("Minimum Cost is :", min_path_weight)
    print("path is :", min_path)
    return  min_path_weight,min_path



# implementation of traveling Salesman Problem greedy Based on
# https://www.geeksforgeeks.org/travelling-salesman-problem-greedy-approach/
def greedy(graph, city_names, s):
    sum = 0
    counter = 0
    j = 0
    i = 0
    mini = 100000000
    path = []
    visitedRouteList = defaultdict(int)

    # Starting from the 0th indexed
    # city i.e., the first city
    visitedRouteList[0] = 1
    route = [0] * len(graph)  ## a array

    # Traverse the adjacency
    # matrix tsp[][]
    while i < len(graph) and j < len(graph[i]):
        # Corner of the Matrix
        if counter >= len(graph[i]) - 1:
            break
        # If this path is unvisited then
        # and if the cost is less then
        # update the cost
        if j != i and (visitedRouteList[j] == 0):  ## when j=i its the route from the vertex to himself
            if graph[i][j] < mini:
                mini = graph[i][j]
                # path.append(graph[i][j])
                route[counter] = j + 1
        j += 1
        # Check all paths from the
        # ith indexed city
        if j == len(graph[i]):
            sum += mini
            path.append(city_names[i])
            mini = 100000000
            visitedRouteList[route[counter] - 1] = 1
            j = 0
            i = route[counter] - 1
            counter += 1
    # Update the ending city in array
    # from city which was last visited
    i = route[counter - 1] - 1
    for j in range(len(graph)):
         if (i != j) and graph[i][j] < mini:
            mini = graph[i][j]
            route[counter] = j + 1
    sum += mini
    path.append(city_names[i])
    # Started from the node where
    # we finished as well.
    print("Minimum Cost is :", sum )
    print("path is :", path)
    return sum, path

class TestFindRoot(TestCase):

    def test_List(self):
       graph1 = [[1000000000, 10, 15, 20],
                 [10, 1000000000, 35, 25],
                 [15, 35, 1000000000, 30],
                 [20, 25, 30, 1000000000]]
       graph_with_cities1 = \
    (["tel-aviv", "jerusalem", "haifa", "eilat"],
     [[1000000000, 10, 15, 20],
      [10, 1000000000, 35, 25],
      [15, 35, 1000000000, 30],
      [20, 25, 30, 1000000000]])
       graph2 = [[1000000000, 20, 42, 35],
                 [20, 1000000000, 30, 34],
                 [42, 30, 1000000000, 12],
                 [35, 34, 12, 1000000000]]
       graph_with_cities2 = \
    (["Ariel", "Netania", "afula", "bat-yam"],
                [[1000000000, 20, 42, 35],
                 [20, 1000000000, 30, 34],
                 [42, 30, 1000000000, 12],
                 [35, 34, 12, 1000000000]])
       graph3 = [[1000000000, 9, 6, 7,10],
                 [9, 1000000000, 3, 8,10],
                 [6, 3, 1000000000, 5,4],
                 [7, 8, 5, 1000000000,8],
                 [10, 10, 4, 8,1000000000]]
       graph_with_cities3 = \
    (["Brussles", "Berlin", "Rome", "Madrid","Paris"],
                [[1000000000, 9, 6, 7,10],
                 [9, 1000000000, 3, 8,10],
                 [6, 3, 1000000000, 5,4],
                 [7, 8, 5, 1000000000,8],
                 [10, 10, 4, 8,1000000000]])
       travellingSalesmanProblem(bruteForce,graph3,0,1)
       travellingSalesmanProblem(greedy,graph3,0,1)

       ## first case - in this graph greedy and brute returns the same answer
       self.assertEqual(travellingSalesmanProblem(greedy, graph_with_cities1, 0, 0), (80, [10, 1000000000, 25, 35]))
       self.assertEqual(travellingSalesmanProblem(greedy, graph_with_cities1, 0, 1), (80, ['tel-aviv', 'jerusalem', 'eilat', 'haifa']))
       self.assertEqual(travellingSalesmanProblem(bruteForce, graph_with_cities1, 0, 1), (80, ['tel-aviv', 'jerusalem', 'eilat', 'haifa']))
       self.assertEqual(travellingSalesmanProblem(bruteForce, graph1, 0, 0), (80, [10, 1000000000, 25, 35]))
       self.assertEqual(travellingSalesmanProblem(bruteForce, graph2, 0, 1), (97, [0, 1, 2, 3]))
       self.assertNotEqual(travellingSalesmanProblem(greedy, graph2, 0, 1), (97, [0, 1, 2, 3])) # here greedy gives a wrong answer
       self.assertEqual(travellingSalesmanProblem(bruteForce, graph_with_cities2, 0, 1), (97, ['Ariel', 'Netania', 'afula', 'bat-yam']))
       self.assertEqual(travellingSalesmanProblem(bruteForce, graph3, 0, 1), (31, [0, 1, 2, 4, 3]))
       self.assertEqual(travellingSalesmanProblem(greedy, graph_with_cities3, 0, 0), (29, [9, 3, 1000000000, 8, 10]))
       self.assertEqual(travellingSalesmanProblem(bruteForce, graph_with_cities3, 0, 1), (31, ['Brussles', 'Berlin', 'Rome', 'Paris', 'Madrid']))







if __name__ == '__main__':
    unittest.main()
