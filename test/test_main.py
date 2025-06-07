"""
Unit tests for the main.py module.
"""
import pytest
from unittest.mock import patch, MagicMock
import main

def test_visualize_tree_empty(capsys) -> None:
    """Test that visualize_tree(None) returns None and prints an 'Empty tree...' message."""
    result = main.visualize_tree(None)
    assert result is None

    captured = capsys.readouterr()
    assert "Empty tree cannot be displayed" in captured.out

def test_visualize_tree_single_node():
    """Test that expected plotting methods are called using MagicMock."""
    from two_three_four_tree import Node234
    root = Node234()
    root.keys = [42]
    root.children = []

    fake_fig = MagicMock()
    fake_draw = MagicMock()
    fake_title = MagicMock()
    fake_show = MagicMock()

    with patch.object(main.plt, 'figure', fake_fig), \
         patch.object(main.nx,  'draw',   fake_draw), \
         patch.object(main.plt, 'title',  fake_title), \
         patch.object(main.plt, 'show',   fake_show):

        result = main.visualize_tree(root)
        assert result is None

    fake_fig.assert_called_once()
    fake_draw.assert_called_once()
    fake_title.assert_called_once()
    fake_show.assert_called_once()
