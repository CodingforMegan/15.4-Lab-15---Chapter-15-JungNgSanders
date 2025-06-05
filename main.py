#Group Members: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

#Date: 6/3/25

#Course: Spr25_CS_034 CRN 39575
#----------------------------------------------

from typing import Optional, List
from collections import deque
import matplotlib.pyplot as plt
import networkx as nx
from BTree import Node234, Tree234

def visualize_tree(root):
    G = nx.DiGraph()
    pos = {}
    labels = {}

    def add_node(node, parent_id=None, depth=0, pos_x=0, sibling_offset=1.0):
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
    if __name__ == "__main__":
    tree = Tree234()
    for value in [10, 20, 5, 6, 12, 30, 25]:
        tree.insert(value)
        print(f"Inserted {value}")
        print(tree.visualize())
        print()

    visualize_tree(tree.root)


if __name__ == "__main__":
    main()
