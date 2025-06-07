# Created by: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

# Date: 6/3/25

# Course: Spr25_CS_034 CRN 39575
#--------------------------------------------------------------------------------------------

from typing import Optional, List
from collections import deque
#import random
#import matplotlib.pyplot as plt
#import networkx as nx


class Node234:
    """
    Implements a node in a 2-3-4 Tree.

    Attributes
    ----------
    keys : List of ints
    children : List of Node234 instances that contain up to 4 keys

    Methods
    -------
    is_leaf()
        Returns a bool checking if a node has no children.
    is_full()
        Returns a bool checking if the node has the full amount of keys, which is 3 for a 2-3-4 Tree.
    insert(key, leftChild=None, rightChild=None)
        Inserts a node in a 2-3-4 Tree based on the rules for a 2-3-4 Tree.       
        
    """

    def __init__(self, keys=None, children=None):
        self.keys = keys if keys else []
        self.children = children if children else []

    
    def is_leaf(self):
        """
        Returns a bool checking if a node has no children.

        Returns
        -------
        Bool
        """

        return len(self.children) == 0

    
    def is_full(self):
        """
        Returns a bool checking if the node has the full amount of keys, which is 3 for a 2-3-4 Tree.

        Returns
        -------
        Bool
        """

        return len(self.keys) == 3

    def insert(self, key, leftChild=None, rightChild=None):
        """
        Inserts a node in a 2-3-4 Tree based on the rules for a 2-3-4 Tree in sorted order. Inserts pointers to child nodes 
        if it is split.
        
        Parameters
        ----------
        key : int
        leftChild : Any  
        rightChild : Any
        
        """

        if key in self.keys:
            print(f"Key {key} already exists. Skipping insertion.")
            return

        if self.is_full():
            raise ValueError("Cannot insert into a full 4-node. Must split first.")

        self.keys.append(key)
        self.keys.sort()

        if leftChild is not None and rightChild is not None:
            idx = self.keys.index(key)
            self.children.insert(idx, leftChild)
            self.children.insert(idx + 1, rightChild)
            if len(self.children) > 4:
                self.children = self.children[:4]

# =================================
# =================================
class Tree234:
    """
    Implements a 2-3-4 Tree.

    Attributes
    ----------
    root : Node234 instance
    
    Methods
    -------
    inOrderTraversal()
        Recursively traverses the 2-3-4 Tree in-order.
    contain(key)
        Returns a bool checking if a key is contained in the 2-3-4 Tree
    insert(key)
        Inserts a key in a 2-3-4 Tree based on the rules for a 2-3-4 Tree using node splitting   
    _find_index(keys, key)
        Searches for the index of where the key should be inserted into among sorted keys
    split_node(node, parent=None, index=None)
        Splits a node by replacing the old child node with new left and right in parent's children list. If the node is the root, the node is
        split into two nodes.
    remove(key)
        Removes a key from the 234 Tree and uses successor replacement and preemptive merging to preserve the properties of the 2-3-4 Tree
        if needed
    _find_successor(node)
        Finds the successor node which is used for removing an internal nodef in the remove() method
    _handle_underflow(node, key)
        Handles the case when merging is necessary to preserve the properties of a 2-3-4 Tree
    _find_parent()
        Finds the parent of a node
    _borrow_from_left_sibling(node, child)
        Borrows a key from the left sibling to prep for a left rotation
    _borrow_from_right_sibling(parent, idx)
        Borrows a key from the right sibling to prep for a right rotation
    _merge_with_siblings(parent, idx)
        Performs a left or right rotation based on the properties of the 2-3-4 Tree and merges
    visualize()
        Produces a string visualization of the 2-3-4 Tree
    """

    def __init__(self):
        self.root = None
    
    def inOrderTraversal(self):
        """
        Recursively traverses the 2-3-4 Tree in-order.
    
        Returns
        -------
        result : list of ints
        """

        result = []
        def _inOrderTraversal(node):
            if node:
                for i, key in enumerate(node.keys):
                    if i < len(node.children):
                        _inOrderTraversal(node.children[i])
                    result.append(key)
                if len(node.children) > len(node.keys):
                    _inOrderTraversal(node.children[-1])
        _inOrderTraversal(self.root)
        return result

    def contains(self, key):
        """
        Returns a bool checking if a key is contained in the 2-3-4 Tree
        
        Parameters
        ----------
        key : int
        
        Returns
        -------
        Bool
        """

        def _search(node, key):
            if not node:
                return False
            for i, k in enumerate(node.keys):
                if key == k:
                    return True
                if key < k:
                    return _search(node.children[i], key) if not node.is_leaf() else False
            return _search(node.children[-1], key) if not node.is_leaf() else False
        return _search(self.root, key)
    
    def insert(self, key):
        """
        Inserts a key in a 2-3-4 Tree based on the rules for a 2-3-4 Tree using node splitting   
        
        Parameters
        ----------
        key : int
        """

        # Case 1: empty tree
        if not self.root:
            self.root = Node234([key])
            return

        # Case 2: Full root
        if self.root.is_full():
            self.root = self.split_node(self.root, None)
     
        # Top-Down Traverse the tree to find the insertion point
        # Along the way, dynamically split full nodes encountered
        node = self.root
        while not node.is_leaf():
            # a. Find the correct child to descend into
            idx = self._find_index(node.keys, key)
            child = node.children[idx]

            # b. Split full child nodes preemptively
            if child.is_full():
                self.split_node(child, node, idx)
                # After splitting, the parent (curr node) has gained a new key at index idx
                # and its children list has been updated
                # If the key we are inserting is greater than the newly promoted key
                # We move to the next child index
                if key > node.keys[idx]:
                    idx += 1
                # Update the child variable to the correct child after the split
                child = node.children[idx]

            # c. Move to the chosen child node for the next iteration
            node = child

        # Insert the key into the leaf node
        node.insert(key)

    
    def _find_index(self, keys, key):
        """
        Searches for the index of where the key should be inserted into among sorted keys
        
        Parameters
        ----------
        keys : list of ints
        key : int

        Returns
        -------
        i : int which is the index of where they key should be inserted
        """

        for i, k in enumerate(keys):
            if key < k:
                return i
        return len(keys)


    def split_node(self, node, parent=None, index=None):
        """
        Splits a node by replacing the old child node with new left and right in parent's children list. If the node is the root, the node is
        split into two nodes.        
        Parameters
        ----------
        node : Node234 instance
        parent : optional, Node234 instance
        index : optional, int

        Returns
        -------
        Node234 if the original node was the root. None in other cases.
        """

        left = Node234(node.keys[:1], node.children[:2])
        right = Node234(node.keys[2:], node.children[2:])
        mid_key = node.keys[1]

        if parent is None:
            return Node234([mid_key], [left, right])
        else:
            # Replace the old child node with new left and right in parent's children list
            parent.children.pop(index)
            parent.insert(mid_key, left, right)


    def remove(self, key):
        """
        Removes a key from the 234 Tree and uses successor replacement and preemptive merging to preserve the properties of the 2-3-4 Tree
        if needed.
        
        Parameters
        ----------
        key : int

        Raises
        ------
        ValueError if the tree is empty
        """

        if not self.root:
            raise ValueError("Tree is empty. Cannot remove key.")

        def _remove(node, key):
            if key in node.keys:
                if node.is_leaf():
                    node.keys.remove(key)
                    if not node.keys:
                        self._handle_underflow(node, key)
                else:
                    idx = node.keys.index(key)
                    if idx + 1 < len(node.children):
                        successor = self._find_successor(node.children[idx + 1])
                        node.keys[idx] = successor
                        _remove(node.children[idx + 1], successor)
            else: # Key not in current node
                if node.is_leaf():
                    # Key not found and it's a leaf node, so key is not in the tree
                    return
                # Key not found and it's an internal node, descend to the appropriate child
                for i, k in enumerate(node.keys):
                    if key < k:
                        _remove(node.children[i], key)
                        return # Return after recursive call

                # If key is greater than all keys in the node, descend to the last child
                _remove(node.children[-1], key)

        _remove(self.root, key)


    def _find_successor(self, node):
        """
        Finds the successor node which is used for removing an internal node in the remove() method
      
        Parameters
        ----------
        node : Node234 instance

        Returns
        -------
        Any, the smallest key of the subtree, which is the in-order successor
        """

        while node.children:
            node = node.children[0]
        return node.keys[0]


    def _handle_underflow(self, node, key):
        """
        Rebalances the tree when a node has fewer keys as a result of a key deletion. Uses key borrowing from a sibling or merging 
        with a sibling to update the tree to be balanced according to the properties of a 2-3-4 Tree.
      
        Parameters
        ----------
        node : Node234 instance
        key : int
        """

        if node == self.root and len(node.keys) == 0:
            self.root = node.children[0] if node.children else None
            return


        parent, idx = self._find_parent(self.root, node)

        # Ensure we only attempt to borrow from left sibling if it exists and has enough keys
        if idx > 0 and len(parent.children[idx - 1].keys) > 1:
            self._borrow_from_sibling(parent, idx, borrow_from_left=True)
        # Ensure we only attempt to borrow from right sibling if it exists and has enough keys
        elif idx < len(parent.children) - 1 and len(parent.children[idx + 1].keys) > 1:
            self._borrow_from_sibling(parent, idx, borrow_from_left=False)
        else:
            self._merge_with_siblings(parent, idx)

    
    def _find_parent(self, node, child):
        """
        Recursively finds a node's parent
      
        Parameters
        ----------
        node : Node234 instance
        child : Node234 instance

        Returns
        -------
        A tuple containing the parent node (None if not found) and and the index of the child that is in the parent's keys. 
        """

        if not node or node == child:
            return None, -1

        for i, c in enumerate(node.children):
            if c == child:
                return node, i

        for c in node.children:
            parent, idx = self._find_parent(c, child)
            if parent:
                return parent, idx
        return None, -1

 
    def _move_key(self, source, target, key):
        """
        ?????????????????
        ?????????????????
        """        
        if key in target.keys:
            return
        if key in source.keys:
            source.keys.remove(key)
        target.keys.append(key)
        target.keys.sort()

    def _borrow_from_sibling(self, parent, idx, borrow_from_left):
        """
        ?????????????????
        ?????????????????
        """  
        node = parent.children[idx]
        if borrow_from_left:
            left = parent.children[idx - 1]
            key_from_parent = parent.keys[idx - 1]

            borrowed_key = left.keys.pop()
            parent.keys[idx - 1] = borrowed_key
            self._move_key(left, node, key_from_parent)

            if left.children:
                node.children.insert(0, left.children.pop())
        else:
            right = parent.children[idx + 1]
            key_from_parent = parent.keys[idx]

            borrowed_key = right.keys.pop(0)
            parent.keys[idx] = borrowed_key
            self._move_key(right, node, key_from_parent)

            if right.children:
                node.children.append(right.children.pop(0))


    def _merge_with_siblings(self, parent, idx):
        """
        Handles an underflow by merging a node with its sibling and pulling down a key from the parent node. If a node and its siblind nodes
        does not have enough keys, a merge is performed with either the right or left sibling and a key from the parent is placed in the middle.
        Since a merge might lead to underflow, this process is done recursively

        Parameters
        ----------
        parent : Node234 instance
        idx : int
        """
        
        node = parent.children[idx]

        if idx > 0:
            # Safe to merge with left sibling
            left_sibling = parent.children[idx - 1]
            if idx - 1 >= len(parent.keys):
                raise IndexError("Parent keys and children misaligned during left merge")

            merge_key = parent.keys.pop(idx - 1)
            parent.children.pop(idx)

            # Remove duplicate
            if merge_key in node.keys:
                node.keys.remove(merge_key)
            if merge_key in left_sibling.keys:
                left_sibling.keys.remove(merge_key)

            left_sibling.keys.append(merge_key)
            left_sibling.keys.extend(node.keys)
            left_sibling.children.extend(node.children)

            if parent == self.root and not parent.keys:
                self.root = left_sibling
                return

        elif idx < len(parent.children) - 1:
            # Safe to merge with right sibling
            right_sibling = parent.children[idx + 1]
            if idx >= len(parent.keys):
                raise IndexError("Parent keys and children misaligned during right merge")

            merge_key = parent.keys.pop(idx)
            parent.children.pop(idx + 1)

            # Remove duplicates
            if merge_key in node.keys:
                node.keys.remove(merge_key)
            if merge_key in right_sibling.keys:
                right_sibling.keys.remove(merge_key)

            node.keys.append(merge_key)
            node.keys.extend(right_sibling.keys)
            node.children.extend(right_sibling.children)

            if parent == self.root and not parent.keys:
                self.root = node
                return
        else:
            raise IndexError("Cannot merge: both siblings missing or inconsistent")

        # Recursive underflow fix
        if not parent.keys and parent != self.root:
            grandparent, parent_idx = self._find_parent(self.root, parent)
            if grandparent:
                self._handle_underflow(parent, None)


    def visualize(self):
        """
        Produces a string visualization of the 2-3-4 Tree in level order

        Returns
        -------
        list : a string representation of the hierarchy of the 2-3-4 Tree. <empty tree> is returned if the tree is empty.
        """

        if not self.root:
            return "<empty tree>"

        lines = []
        q = deque([(self.root, 0)]) # Queue stores tuples of (node, level)
        max_level = 0

        # Perform a level-order traversal to get nodes at each level
        nodes_at_level = {}
        while q:
            current_node, level = q.popleft()
            if level not in nodes_at_level:
                nodes_at_level[level] = []
            nodes_at_level[level].append(current_node)
            max_level = max(max_level, level)

            for child in current_node.children:
                if child:
                    q.append((child, level + 1))
                # To handle empty children slots and maintain structure,
                # we might need placeholders, but for this visualization,
                # we only add non-None children. This will affect spacing
                # if some children are None. A more complex visualization
                # would need to account for potential None children to
                # maintain consistent spacing.

        # Calculate spacing and format lines
        # This is a simplified approach. Precise centering and spacing
        # for a 2-3-4 tree can be complex due to variable node sizes.
        # We will use a fixed width for each potential node position
        # at the widest level (assuming max 4 children per node and max depth).

        # Estimate a maximum width needed based on max nodes at deepest level
        # This is a heuristic and might not be perfect for all tree shapes.
        max_nodes_at_level = max((len(nodes) for nodes in nodes_at_level.values()), default=1)
        # Assume each node label is roughly 10 characters wide for spacing calculation
        node_width_estimate = 15 # Adjust as needed

        for level in range(max_level + 1):
            level_nodes = nodes_at_level.get(level, [])
            line = ""
            # Calculate approximate total width needed for this level if all positions were filled
            expected_nodes_this_level = 4**level if level > 0 else 1 # Max possible nodes at this level
            total_level_width_estimate = expected_nodes_this_level * node_width_estimate

            # Add spacing before the first node on the line
            # This part is tricky for perfect centering without knowing the full subtree widths.
            # We'll use a simple approach based on the number of nodes expected vs present.
            # A more advanced visualization would need to account for potential None children to
            # maintain consistent spacing.

            # Simple centering attempt: calculate total width and add padding
            line_content = " ".join([str(node.keys) for node in level_nodes])
            # Estimate how much space this line content will take
            content_width_estimate = sum([len(str(node.keys)) for node in level_nodes]) + (len(level_nodes) - 1) * 1 # spaces between nodes

            # Calculate total width needed for the widest level
            # This is a simplified assumption. Actual width depends on keys and structure.
            widest_level_nodes_count = max((len(nodes) for nodes in nodes_at_level.values()), default=1)
            # Assuming max node string representation length is around 10-15
            max_node_str_len = 15 # Estimate
            total_estimated_width = widest_level_nodes_count * max_node_str_len + (widest_level_nodes_count -1) * 2 # Add space for children connections etc.


            # Calculate padding needed for centering
            # Center the current line content within the total estimated width
            current_line_content = "  ".join([str(node.keys) for node in level_nodes])
            padding_needed = max(0, (total_estimated_width - len(current_line_content)) // 2)
            line = " " * padding_needed + current_line_content


            lines.append(line)

        return "\n".join(lines)


if __name__ == "__main__":
    tree = Tree234()
    values = random.sample(range(1, 101), 10)
    for v in values:
        tree.insert(v)
        print(f"Inserted {v}")
        print(tree.visualize())
        print()


    print("In-Order Traversal:")
    print(tree.inOrderTraversal())

    visualize_tree(tree.root)

    for v in values:
        print(f"Searching for {v}: {'Found' if tree.contains(v) else 'Not Found'}")
        print()

    random_key = random.sample(range(1, 101), 1)

    for v in random_key:
        print(f"Searching for a random value {v}: {'Found' if tree.contains(v) else 'Not Found'}")
        print()

    for v in values:
        tree.remove(v)
        print(f"Removed {v}")
        print(tree.visualize())
        visualize_tree(tree.root)
        print()


    print("In-Order Traversal:")
    print(tree.inOrderTraversal())

    visualize_tree(tree.root)
