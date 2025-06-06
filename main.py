#Group Members: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

#Date: 6/3/25

#Course: Spr25_CS_034 CRN 39575
#----------------------------------------------
from typing import Optional, List
from collections import deque
from BTree import Tree234
import random
import matplotlib.pyplot as plt
import networkx as nx

def visualize_tree(root):
    """
    Builds an instance of a 2-3-4 Tree starting from the root node and visualizes it using the networkx and matplotlib libraries.

    Parameters
    ----------
    root : root node of the 2-3-4 Tree
    
    Returns
    -------
    None. Displays the Graph representation of the 2-3-4 Tree
    """ 
    G = nx.DiGraph()
    pos = {}
    labels = {}

    def add_node(node, parent_id=None, depth=0, pos_x=0, sibling_offset=1.0):
        """
        Adds the nodes of a 2-3-4 Tree to an instance of a DiGraph from the networkx library     
        Parameters
        ----------
        node : Node234 instnance
        depth : int
        pos_x : float
        sibling_offset : float
        
        Returns
        -------
        None. 
        """ 
        node_id = id(node)
        label = ','.join(map(str, node.keys))
        G.add_node(node_id)
        labels[node_id] = label
        pos[node_id] = (pos_x, -depth)

        if parent_id is not None:
            G.add_edge(parent_id, node_id)

        n_children = len(node.children)
        if n_children > 0:
            width = sibling_offset * (n_children - 1)
            start_x = pos_x - width / 2
            for i, child in enumerate(node.children):
                add_node(child, node_id, depth + 1, start_x + i * sibling_offset, sibling_offset / 2)

    add_node(root)
    plt.figure(figsize=(8, 4))
    nx.draw(G, pos, labels=labels, with_labels=True, node_size=2000, node_color='lightblue', font_size=10)
    plt.title("2-3-4 Tree Visualization")
    plt.show()

# Demo Main()
def main():
    """
    Builds an instance of a 2-3-4 Tree starting from the root node, inserts random integers that are multiples of 7 from 1 to 100, 
    visualizes the tree, and traverses the Tree in order. Performs a test on the contain() and remove() methods from the Tree234 class.

    Parameters
    ----------
    None
    
    Returns
    -------
    None. Visualizes the 2-3-4 Tree after the insert(), remove(), and contain() methods are called, as well as th visualization of
    the in-order traversal of the 2-3-4 Tree.
    """ 
    tree = Tree234()
    values = random.sample(range(1, 101), 7)
    for v in values:
        tree.insert(v)
        print(f"Inserted {v}")
        print(tree.visualize())
        print()


    print("In-Order Traversal:")
    print(tree.inOrderTraversal())
    
    visualize_tree(tree.root)

    for v in values:
        print(f"Searching for {v}: {'Found' if tree.contain(v) else 'Not Found'}")
        print()

    random_key = random.sample(range(1, 101), 1)
    for v in random_key:
        print(f"Searching for a random value {v}: {'Found' if tree.contains(v) else 'Not Found'}")
        print()

    for v in values:
        tree.remove(v)
        print(f"Removed {v}")
        print(tree.visualize())
        print()


    print("In-Order Traversal:")
    print(tree.inOrderTraversal())

    visualize_tree(tree.root)

if __name__ == "__main__":
    main()
