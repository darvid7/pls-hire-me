"""
@author: David Lei
@since: 23/08/2016
@modified: 

Based Vertex and Edge clases
- a bit too generic too be honest
- should be speific for use
"""
class Vertex:
    def __init__(self, x=None, point=None, rep=None):
        self.name = x                                   # integer 'name' or index....why did I call this name?
        self.pointer = point                            # points to a linked list in adjacency list
        self.rep = rep                                  # string representation
        self.distance = None
        self.index = x                                  # made this because I didn't want to refactor to change .name to .index everywhere.


class Edge:
    def __init__(self, origin, destination, x=None, weight=None, capacity=None, flow=None, residual_capacity=None, residual_flow=None):
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.capacity = capacity
        self.name = x
        self.flow = flow
        self.residual_capacity = residual_capacity
        self.residual_flow = residual_flow

    def get_endpoints(self):
        return self.origin, self.destination

    def get_opposite(self, vertex):
        """Return the vertex that is opposite v on this edge"""
        return self.destination if vertex is self.origin else self.origin

    def to_string(self, ends_vertex_obs = False):
        if ends_vertex_obs:
            return "og: " + str(self.origin.name) + " to: " + str(self.destination.name)
        return "og: " + str(self.origin) + " to: " + str(self.destination)
