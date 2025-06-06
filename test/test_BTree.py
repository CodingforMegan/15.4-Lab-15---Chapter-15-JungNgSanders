"""
Unit tests for the BTree.py module.
"""

import pytest

from BTree import Tree234, Node234

@pytest.fixture
def test_BTree():
  tree = Tree234()
  integers = [10, 20, 5, 6, 12, 30, 25]
  for i in integers:
    tree.insert(i)  
  for i in integers:
    assert tree.contains(i)
