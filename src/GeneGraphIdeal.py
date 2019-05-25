import numpy as np
import networkx as nx

"""
Class: GeneGraphIdeal
----------------

The goal of GeneGraphIdeal is to identify indivuals solely based off of their genetic information.
We begin by assuming we have access to a complete graph G = (V,E) of a given population
(check out GeneGraph.py for a version without this assumption). We also have access to some subset of
V, called V_star, representing genes of individuals which are available in public databases.

Given the genome of an individual x, we wish to identify which node in V corresponds to x.
We have access to a function T(G, x, v), which given our graph, a target genome x, and a public genome v,
outputs a vector of size |V|. This vector corresponds to a probability distribution over the nodes in V,
and is a computed likelihood of any given node being x.

We compute T(G, x, v) for every v in V_star, and combine the information from these probability
distributions to identify the highest likelihood node in V.

"""


class GeneGraphIdeal:
    def __init__(G, V_star, T):
        self.G = G
        self.V_star = V_star
        self.T = T

    ## Returns the ID of the most likely node to be x.
    def identify(x):
        num_public, num_total = len(self.V_star), G.number_of_nodes()
        distributions = np.zeros((num_public, num_total))

        for idx, v in enumerate(self.V_star):
            distributions[idx, :] = self.T(G, x, v)

        return np.argmax(distributions.sum(0))
