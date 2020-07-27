import sys

"""
=========================================================================================================
dijkstra's_algorithm.py
=========================================================================================================

Goal: This is a comment
    I am implementing Dijkstra's Algorithm in Python, following along with tutorial by Amitabha Dey

Sources:
    [1] Amitabha Dey's Youtube Video: https://www.youtube.com/watch?v=Ub4-nG09PFw
    [2] Amitabha Dey's Github Gist: https://gist.github.com/amitabhadey/37af83a84d8c372a9f02372e6d5f6732
    [3] Logging Tutorial https://docs.python.org/3.1/library/logging.html

Disclaimer(s):
    I do not claim any credit for this code. It was following along with [2] and the end result pretty much [1].
    However, I have spent significant time and effort refactoring and optimizing.
    I do however, claim credit for the ascii art, as I'm quite proud of it.

directed_graph_a: Besides nodes G & H, all other nodes have one-way edges.

          > > > >  [D]   > > > > > >  [G]
 [A]  > > >           >             >
    >            >     >          >
  v   > >      >        >       >
          >                 [E]       v ^
  v        [C]                  >     v ^
             >>       >          >
  v    >      >>                  >
                >>                 >
 [B]  > > > > >  [F]   >> >> >> >>    [H]


undirected_graph_a: All edges are 2-way.

      / - - - - [  A  ]
   [F]       //// |  \
 |||| \    ////   |   \\\
 ||||  \  ////    |      \
 ||||  [E]   -   [D]  -   [B]
 ||||  /            \    //
    [C]    -    -    [G]

"""

directed_graph_a = {
    'A': {'B': 3, 'C': 4, 'D': 7},
    'B': {'C': 1, 'F': 5},
    'C': {'F': 6, 'D': 2},
    'D': {'E': 3, 'G': 6},
    'E': {'G': 3, 'H': 4},
    'F': {'E': 1, 'H': 8},
    'G': {'H': 2},
    'H': {'G': 2}
}

undirected_graph_a = {
    'A': {'B': 5, 'D': 3, 'E': 12, 'F': 5},
    'B': {'A': 5, 'D': 1, 'G': 2},
    'C': {'E': 1, 'F': 16, 'G': 2},
    'D': {'A': 3, 'B': 1, 'E': 1, 'G': 1},
    'E': {'A': 12, 'C': 1, 'D': 1, 'F': 2},
    'F': {'A': 5, 'C': 16, 'E': 2},
    'G': {'B': 2, 'C': 2, 'D': 1}
}


def dijkstras_algorithm(graph, start_node, end_node, infinity=sys.maxsize):
    path, node_predecessor = [], {}  # Final Path, {Node_N: 2nd-to-last Node in shortest path to N}
    unseen_nodes = graph.copy()  # Make a copy so we don't alter the input graph. (In case user needs it later).
    shortest_distance = {node: (infinity if node != start_node else 0)  # Least cost to a given node from start_node
                         for node in unseen_nodes}  # This will be updated as we iterate and find better paths.

    while unseen_nodes:  # Step 1: 'See' all nodes and register them appropriately to data structures above
        min_distance_node = None  # By Default, Least-Path-Connection-Nodes are set to None
        for node in unseen_nodes:  # Step 1a: Iterate through all unseen nodes to find lowest cost
            if min_distance_node is None or shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node  # min_distance_node = node by default or if new node has lower cost

        path_options = graph[min_distance_node].items()  # Get child nodes of current lowest cost node

        for child_node, weight in path_options:  # Iterate through path_options to see if reduced-cost paths present.
            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                node_predecessor[child_node] = min_distance_node  # Updates least_cost & associated parent node

        del unseen_nodes[min_distance_node]  # We'll break the while loop after registering all nodes & paths

    current_node = end_node  # Work backwards from end/goal node, then grab Least-Path-Connection-Nodes in sequence

    while current_node != start_node:
        try:
            path.insert(0, current_node)  # Add to beginning of list
            current_node = node_predecessor[current_node]  # Next node will be this node's Least-Path-Connection-Node
        except KeyError:  # Error Handling
            print("You have entered a key that does not exist in the requested dictionary 'node_predecessor'.")

    path.insert(0, start_node)  # Append Starting Node

    if shortest_distance[end_node] != infinity:  # If shortest_distance[end_node] = infinity, path does not exist
        return path, shortest_distance[end_node]

    return None, None


shortest_path, least_cost = dijkstras_algorithm(undirected_graph_a, 'A', 'H')
print('Shortest distance from {0} to {1} is {2}, and is obtained by taking the optimized path below:\n\t{3}'
      .format(shortest_path[0], shortest_path[-1], least_cost, shortest_path))
