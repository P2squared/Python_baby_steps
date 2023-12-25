""""
Empty Graph Template to implement :D
Github: https://www.github.com/kying18  """

# Markov Chain approach to graph composer
import random

class Vertex(object):
    def __init__(self, value):
        self.value = value # assign a value to every vertex, this value is the word
        self.adjacent = {} # list of other vertices that have an edge from this vertex
        self.nebors = []
        self.nebors_weights = []

    def add_edge_to(self, vertex, weight=0): #add edge from 'self' vertex to new vertex & assign weight
        self.adjacent[vertex] = weight # assign weight to every edge

    def increment_edge(self, vertex): # increment weight of an edge when its found during creating the graph
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_adjacent_nodes(self):
        return self.adjacent.keys()

    # initializes probability map
    def get_probability_map(self): # probability map for every vertex
        for (vertex, weight) in self.adjacent.items():
            self.nebors.append(vertex)
            self.nebors_weights.append(weight)

    def next_word(self): # Choose next word from nebors based on weights
        return random.choices(self.nebors, weights =self.nebors_weights)[0] # Return only one item



class Graph(object):
    def __init__(self):
        self.vertices = {} # list of all vertices in the graph

    def get_vertex_values(self): # get values of all vertices (all words )
        return set(self.vertices.keys())

    def add_vertex(self, value):
        self.vertices[value] = Vertex(value) # This function accesses/executes class Vertex

    def get_vertex(self, value):
        if value not in self.vertices: # If a value is not in any vertex already
            self.add_vertex(value) # add that vertex
        return self.vertices[value] # return vertex object of this value

    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self): # generate probability map for entire graph
        for vertex in self.vertices.values():
            vertex.get_probability_map() # generate map for every vertex in the graph
