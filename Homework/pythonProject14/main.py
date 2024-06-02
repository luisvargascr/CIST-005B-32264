"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 05/04/2024

Description: main
This file is used to test the graph class.

The following file performs the following actions:

1) Creates a graph representing a social network.
1.a) Adds some people (vertices) to the network
1.b) then creates friendships (edges) among some of them.
2) Creates a graph representing a map between cities.
2.a) Adds some cities (vertices) to the map like Cupertino, Los Angeles, San Jose, and San Francisco,
2.b) then creates roads (edges) between them with different weights.
"""

from graph import LinkedDirectedGraph


def create_social_network():
    my_social_network = LinkedDirectedGraph()
    my_social_network.add("John")
    my_social_network.add("Luka")
    my_social_network.add("Tim")
    my_social_network.add("Josh")
    my_social_network.add("Tom")
    my_social_network.add("Jeff")
    my_social_network.add("Ally")
    my_social_network.add("Tina")
    my_social_network.add("Alison")
    my_social_network.add("Taylor")
    my_social_network.add("Marie")
    my_social_network.add("Kimberly")
    my_social_network.add("Ashley")
    # In social media such as Facebook, the weight in the relationship is equal, and it is set to 1.
    my_social_network.addEdge("John", "Alison", 1)
    my_social_network.addEdge("Alison", "Taylor", 1)
    my_social_network.addEdge("Marie", "Alison", 1)
    my_social_network.addEdge("Alison", "Luka", 1)
    my_social_network.addEdge("Luka", "Tim", 1)
    my_social_network.addEdge("Josh", "Tom", 1)
    my_social_network.addEdge("Tom", "Taylor", 1)
    my_social_network.addEdge("Taylor", "Jeff", 1)
    my_social_network.addEdge("Tina", "Luka", 1)
    my_social_network.addEdge("Tina", "Marie", 1)
    my_social_network.addEdge("Taylor", "Kimberly", 1)
    my_social_network.addEdge("Alison", "Ashley", 1)
    print("The social network has these friends: \n" + str(my_social_network))
    print("Incident edges of Alison:", list(map(str, my_social_network.incidentEdges("Alison"))))


def create_map_among_cities():
    my_map = LinkedDirectedGraph()
    my_map.add("San Jose")
    my_map.add("Santa Clara")
    my_map.add("Sunnyvale")
    my_map.add("Mountain View")
    my_map.add("Palo Alto")
    my_map.add("Menlo Park")
    my_map.add("Redwood City")
    my_map.add("San Mateo")
    my_map.add("San Bruno")
    my_map.add("South San Francisco")
    my_map.add("San Francisco")
    # In a map, the weight between cities corresponds to the distance (below in miles) between the two connected cities.
    my_map.addEdge("San Jose", "Santa Clara", 4.8)
    my_map.addEdge("Santa Clara", "Sunnyvale", 7.8)
    my_map.addEdge("Sunnyvale", "Mountain View", 3.3)
    my_map.addEdge("Mountain View", "Palo Alto", 8.5)
    my_map.addEdge("Palo Alto", "Menlo Park", 2.7)
    my_map.addEdge("Menlo Park", "Redwood City", 3.7)
    my_map.addEdge("Redwood City", "San Mateo", 8.5)
    my_map.addEdge("San Mateo", "San Bruno", 8.8)
    my_map.addEdge("San Bruno", "South San Francisco", 2.2)
    my_map.addEdge("South San Francisco", "San Francisco", 9.9)
    print("The map has these points: \n" + str(my_map))
    print("Incident edges of San Jose:", list(map(str, my_map.incidentEdges("San Jose"))))


if __name__ == "__main__":
    create_social_network()
    create_map_among_cities()
