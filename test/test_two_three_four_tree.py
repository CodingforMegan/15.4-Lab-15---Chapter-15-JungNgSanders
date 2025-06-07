"""
Unit tests for the two_three_four_tree.py module.
"""

import pytest

from two_three_four_tree import Tree234, Node234

@pytest.fixture
def empty_node():
    return Node234()

@pytest.fixture
def single_key_node():
    return Node234(keys=[5])

@pytest.fixture
def simple_tree():
    tree = Tree234()
    integers = [10, 20, 5, 6, 12, 30, 25]
    for i in integers:
        tree.insert(i)
    return tree

def test_initialization_defaults(empty_node, single_key_node):
    """Tests that initialized nodes (empty and with a single key) contain the expected class attributes."""
    assert empty_node.keys == []
    assert empty_node.children == []

    assert single_key_node.keys == [5]
    assert single_key_node.children == []

def test_node_is_leaf(empty_node, single_key_node):
    """Tests that the node.is_leaf() method appropriately identifies a leaf node."""
    assert empty_node.is_leaf() is True
    assert single_key_node.is_leaf() is True

    node = Node234(keys=[5], children=[Node234(keys=[1])])
    assert node.is_leaf() is False

def test_node_is_full():
    """Tests that a node is marked as full (True) when it has three keys."""
    node = Node234(keys=[1,2,3])
    assert node.is_full() is True
    node2 = Node234(keys=[1,2])
    assert node2.is_full() is False

def test_node_insert_sorted_order():
    """Tests that inserted keys are stored in sorted order."""
    node = Node234()
    node.insert(10)
    node.insert(5)
    node.insert(15)
    assert node.keys == [5,10,15]

def test_node_insert_duplicate():
    """Tests that a duplicate node is not stored, as expected."""
    node = Node234(keys=[10])
    node.insert(10)
    assert node.keys == [10]

def test_tree_insert():
    tree = Tree234()
    vals = [10, 20, 5, 6, 12, 30, 25]
    for v in vals:
        tree.insert(v)
    assert tree.inOrderTraversal() == sorted(vals)
    for v in vals:
        assert tree.contains(v)

def test_tree_removal():
    """Test that remove() method functions as expected."""
    tree = Tree234()
    vals = [10, 20, 5, 6, 12, 30, 25]
    for v in vals:
        tree.insert(v)
    tree.remove(20)
    tree.remove(5)
    assert tree.contains(20) is False
    assert tree.contains(5) is False
    for v in [6, 10, 12, 25, 30]:
        assert tree.contains(v)
    empty_tree = Tree234()
    with pytest.raises(ValueError):
        empty_tree.remove(99)

def test_tree_balance_invariants(simple_tree):
    """Test that after insertions, all leaves are at the same level (balanced property) using a get_leaf_depths() helper function."""
    def get_leaf_depths(node, depth=0, leaf_depths=None):
        if leaf_depths is None:
            leaf_depths = set()
        if node.is_leaf():
            leaf_depths.add(depth)
        else:
            for child in node.children:
                get_leaf_depths(child, depth+1, leaf_depths)
        return leaf_depths
    leaf_depths = get_leaf_depths(simple_tree.root)
    assert len(leaf_depths) == 1

def test_node_split_error():
    """Test that a ValueError is raised when trying to insert into a full node."""
    node = Node234(keys=[5,10,15])
    with pytest.raises(ValueError):
        node.insert(12)

def test_inorder_traversal_empty_tree():
    """Test that inOrderTraversal() returns an empty list when called with an empty tree."""
    tree = Tree234()
    assert tree.inOrderTraversal() == []

def test_visualize_output(simple_tree):
    """Tests that the tree.visualize() method returns a string (with some brackets)."""
    result = simple_tree.visualize()
    assert isinstance(result, str)
    assert "[" in result