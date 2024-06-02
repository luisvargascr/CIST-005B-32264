"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 05/18/2024

File Name: graph.py
Description: This file is NOT of my authorship. This file is from the book "Fundamentals of Python Data Structures",
2nd edition by Kenneth A. Lambert.
Author: Kenneth A. Lambert.
This file contains several supporting classes to represent graphs and it is used under copyright terms.
All terminology, variable names, logic, contents, etc. are of Mr. Lambert's authorship.
Classes in this file: LinkedEdge, LinkedVertex, and LinkedDirectedGraph

IMPORTANT NOTE: Although the file is not of my authorship, I did make several modifications to it to adapt it
to the needs of Final Part 1 and my program.
"""
from typing import List

from abstractcollection import AbstractCollection
from myprofile import MyProfile


class LinkedEdge(object):

    # An edge has a source vertex, a destination vertex,
    # a weight, and a mark attribute.

    def __init__(self, fromVertex, toVertex, weight=None) -> None:
        self.vertex1 = fromVertex
        self.vertex2 = toVertex
        self.weight = weight
        self.mark = False

    def clearMark(self) -> None:
        """Clears the mark on the edge."""
        self.mark = False

    def __eq__(self, other) -> bool:
        """Two edges are equal if they connect
        the same vertices."""
        if self is other: return True
        if type(self) != type(other):
            return False
        return self.vertex1 == other.vertex1 and \
            self.vertex2 == other.vertex2

    def getOtherVertex(self, thisVertex):
        """Returns the vertex opposite thisVertex."""
        if not thisVertex or thisVertex == self.vertex2:
            return self.vertex1
        else:
            return self.vertex2

    def getToVertex(self):
        """Returns the edge's destination vertex."""
        return self.vertex2

    def getWeight(self):
        """Returns the edge's weight."""
        return self.weight

    def isMarked(self):
        """Returns True if the edge is marked
        or False otherwise."""
        return self.mark

    def setMark(self):
        """Sets the mark on the edge."""
        self.mark = True

    def setWeight(self, weight):
        """Sets the weight on the edge to weight."""
        self.weight = weight

    def __str__(self):
        """Returns the string representation of the edge."""
        return str(self.vertex1) + ">" + \
            str(self.vertex2) + ":" + \
            str(self.weight)


class LinkedVertex(object):

    # A vertex has a label, a list of incident edges,
    # and a mark attribute.

    def __init__(self, profile: MyProfile):
        """Constructor for this class."""
        self.profile = profile
        self.edgeList = list()
        self.mark = False

    def clearMark(self):
        """Clears the mark on the vertex."""
        self.mark = False

    def getProfile(self):
        """Returns the label of the vertex."""
        return self.profile

    def isMarked(self):
        """Returns True if the vertex is marked
        or False otherwise."""
        return self.mark

    def setLabel(self, profile, g):
        """Sets the vertex's label to label."""
        g.vertices.pop(self.profile, None)
        g.vertices[profile] = self
        self.profile = profile

    def setMark(self):
        """Sets the mark on the vertex."""
        self.mark = True

    def __str__(self):
        """Returns the string representation of the vertex."""
        return str(self.profile.get_name())

    def __eq__(self, other):
        """Two vertices are equal if they have
        the same labels."""
        if self is other: return True
        if type(self) != type(other): return False
        return self.profile.get_name() == other.profile.get_name()

    def __hash__(self):
        """Supports hashing on a vertex."""
        return hash(self.profile.get_name())

    # Methods used by LinkedGraph

    def addEdgeTo(self, toVertex: object, weight: int):
        """Connects the vertices with an edge."""
        edge = LinkedEdge(self, toVertex, weight)
        self.edgeList.append(edge)

    def getEdgeTo(self, toVertex: object):
        """Returns the connecting edge if it exists, or
        None otherwise."""
        edge = LinkedEdge(self, toVertex)
        try:
            return self.edgeList[self.edgeList.index(edge)]
        except:
            return None

    def incidentEdges(self):
        """Returns the incident edges of this vertex."""
        return iter(self.edgeList)

    def neighboringVertices(self):
        """Returns the neighboring vertices of this vertex."""
        vertices = list()
        for edge in self.edgeList:
            vertices.append(edge.getOtherVertex(self))
        return iter(vertices)

    def removeEdgeTo(self, toVertex: object):
        """Returns True if the edge exists and is removed,
        or False otherwise."""
        edge = LinkedEdge(self, toVertex)
        if edge in self.edgeList:
            self.edgeList.remove(edge)
            return True
        else:
            return False


class LinkedDirectedGraph(AbstractCollection):

    # A graph has a count of vertices, a count of edges,
    # and a dictionary of label/vertex pairs.

    def __init__(self, sourceCollection=None) -> None:
        """Constructor for this class."""
        self.edgeCount = 0
        self.vertices = {}
        AbstractCollection.__init__(self, sourceCollection)

    # Methods for clearing, marks, sizes, string rep

    def clear(self) -> None:
        """Clears the graph."""
        self.size = 0
        self.edgeCount = 0
        self.vertices = {}

    def clearEdgeMarks(self) -> None:
        """Clears all the edge marks."""
        for edge in self.edges():
            edge.clearMark()

    def clearVertexMarks(self) -> None:
        """Clears all the vertex marks."""
        for vertex in self.getVertices():
            vertex.clearMark()

    def sizeEdges(self) -> int:
        """Returns the number of edges."""
        return self.edgeCount

    def sizeVertices(self) -> int:
        """Returns the number of vertices."""
        return len(self)

    def __str__(self) -> str:
        """Returns the string representation of the graph."""
        result = str(self.sizeVertices()) + " Vertices: "
        for vertex in self.vertices:
            result += " " + str(vertex)
        result += "\n"
        result += str(self.sizeEdges()) + " Edges: "
        for edge in self.edges():
            result += " " + str(edge)
        return result

    def add(self, profile: MyProfile) -> None:
        """For compatibility with other collections."""

        self.addVertex(profile)

    # Vertex related methods

    def addVertex(self, profile: MyProfile) -> None:
        """Adds a vertex with the given label to the graph."""
        self.vertices[profile.get_name()] = LinkedVertex(profile)
        self.size += 1

    def containsVertex(self, profile: str) -> bool:
        """Checks in the graph to determine if a profile exists."""
        return profile in self.vertices

    def getVertex(self, profile: MyProfile) -> LinkedVertex | None:
        """Gets a vertex in the graph by receiving the profile object to go off and search for."""
        if not profile or profile.get_name() not in self.vertices:
            return None
        return self.vertices[profile.get_name()]

    def getVertexByName(self, name: str) -> LinkedVertex | None:
        """Gets a vertex in the graph by receiving the profile name to look for. """
        if name not in self.vertices:
            return None
        return self.vertices[name]

    def updateVertex(self, old_profile: MyProfile, updated_profile: MyProfile) -> bool:
        """Updates a vertex with new information."""
        old_profile_name = old_profile.get_name()
        new_profile_name = updated_profile.get_name()
        if old_profile_name in self.vertices:
            old_vertex = self.vertices[old_profile_name]
            old_incident_edges = old_vertex.incidentEdges()
            self.removeVertex(old_profile)
            self.addVertex(updated_profile)
            new_profile_name = self.vertices[new_profile_name]

            for edge in old_incident_edges:
                self.addEdge(new_profile_name.profile, edge.vertex2.profile,1)
                self.addEdge(edge.vertex2.profile, new_profile_name.profile, 1)
            return True
        else:
            return False

    def getIncidentEdges(self, profile: MyProfile) -> List[str]:
        """Returns the list of edges' names for a particular vertex."""
        profile_name = profile.get_name()
        friends_list = []
        incident_edges = None
        if profile_name in self.vertices:
            incident_edges = self.incidentEdges(profile)

        if incident_edges:
            for edge in incident_edges:
                friends_list.append(edge.vertex2.profile.get_name())

        return friends_list

    def removeVertex(self, profile: MyProfile) -> bool:
        """Returns True if the vertex was removed, or False otherwise."""
        removedVertex = self.vertices.pop(profile.get_name(), None)
        if removedVertex is None:
            return False

        # Examine all other vertices to remove edges
        # directed at the removed vertex
        for vertex in self.getVertices():
            if vertex.removeEdgeTo(removedVertex):
                self.edgeCount -= 1

        # Examine all edges from the removed vertex to others
        for edge in removedVertex.incidentEdges():
            self.edgeCount -= 1
        self.size -= 1
        return True

    # Methods related to edges

    def addEdge(self, fromProfile, toProfile, weight):
        """Connects the vertices with an edge with the given weight."""
        fromVertex = self.getVertex(fromProfile)
        toVertex = self.getVertex(toProfile)
        fromVertex.addEdgeTo(toVertex, weight)
        self.edgeCount += 1

    def containsEdge(self, fromLabel, toLabel):
        """Returns True if an edge connects the vertices,
        or False otherwise."""
        return self.getEdge(fromLabel, toLabel) if None else False

    def getEdge(self, fromLabel, toLabel):
        """Returns the edge connecting the two vertices, or None if
        no edge exists."""
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)
        return fromVertex.getEdgeTo(toVertex)

    def removeEdge(self, fromProfile: MyProfile, toProfile: MyProfile):
        """Returns True if the edge was removed, or False otherwise."""
        fromVertex = self.getVertex(fromProfile)
        toVertex = self.getVertex(toProfile)
        edgeRemovedFlg = fromVertex.removeEdgeTo(toVertex)
        if edgeRemovedFlg:
            self.edgeCount -= 1
        return edgeRemovedFlg

    def removeEdgeByNames(self, fromProfile: str, toProfile: str):
        """Returns True if the edge was removed, or False otherwise."""
        fromVertex = self.getVertexByName(fromProfile)
        toVertex = self.getVertexByName(toProfile)
        edgeRemovedFlg = fromVertex.removeEdgeTo(toVertex)
        if edgeRemovedFlg:
            self.edgeCount -= 1
        return edgeRemovedFlg

    # Iterators

    def __iter__(self):
        """Supports iteration over a view of self (the vertices)."""
        return self.vertices()

    def edges(self):
        """Supports iteration over the edges in the graph."""
        result = list()
        for vertex in self.getVertices():
            result += list(vertex.incidentEdges())
        return iter(result)

    def getVertices(self):
        """Supports iteration over the vertices in the graph."""
        return iter(self.vertices.values())

    def incidentEdges(self, profile: MyProfile):
        """Supports iteration over the incident edges of the
        given vertex."""
        return self.getVertex(profile).incidentEdges()

    def neighboringVertices(self, profile: MyProfile):
        """Supports iteration over the neighboring vertices of the
        given vertex."""
        return self.getVertex(profile).neighboringVertices()
