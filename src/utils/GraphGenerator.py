import networkx as nx

"""
Helper class for generating various random graphs, which are meant to
simulate actual populations. These graphs are contrived and do not
represent actual populations.
"""


class GraphGenerator:
    """
    Very simple (toy) population model:
        - All nodes are sexed M or F, and link with a spouse at [reproductive_percentage]
        - Couples have [avg_num_children] children
        - All nodes 'reproduce' between ages of [fertility_start], [fertility_end]
        - Individuals cheat at rate [avg_rate_infidelity]
        -

        params:
            num_nodes :: number of nodes in graph
            avg_num_children :: Average number of children per couple, default 2
            reproductive_percentage :: Percent of population that procreates.
            avg_rate_infidelity :: Percentage of time individuals procreate w/o spouse.
            fertility_start :: Age that nodes begin to reproduce
            fertility_end :: Age that nodes stop reproducing

    """

    def very_simple_population_model(
        num_nodes=100000,
        initial_population=10000
        avg_num_children=2.5,
        reproductive_percentage=0.8,
        avg_rate_infidelity=0.1,
        fertility_start=20,
        fertility_end=45,
    ):
        if initial_population > num_nodes:
            raise Exception("Initial population cannot exceed graph size")

        G = nx.Graph()
        male, female = set(), set()


        ## Generate Initial Population
        G.add_nodes_from(range(initial_population))
        print(G.number_of_nodes())

a = GraphGenerator().very_simple_population_model()
