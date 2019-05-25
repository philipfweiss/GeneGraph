import networkx as nx

"""
Helper class for generating various random graphs, which are meant to
simulate actual populations. These graphs are contrived and do not
represent actual populations.
"""

class GraphGenerator():
    """
    Very simple population model:
        - All nodes are sexed M or F.
        - All nodes 'reproduce' between ages of [fertility_start], [fertility_end]
        - Individuals stay with spouse, but cheat at rate [avg_rate_infidelity]

        options: {
            avg_num_children :: Average number of children per couple, default 2
            reproductive_percentage :: Percent of population that procreates.
            avg_rate_infidelity :: Percentage of time individuals procreate w/o spouse.
            fertility_start :: Age that nodes begin to reproduce
            fertility_end :: Age that nodes stop reproducing
        }
    """
    def very_simple_population_model(num_nodes, options):
        if initial_population > num_nodes: raise Exception("Initial population cannot exceed graph size")

        sex_map = {}
