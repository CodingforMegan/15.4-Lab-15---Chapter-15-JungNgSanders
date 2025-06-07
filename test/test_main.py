"""
Unit tests for the main.py module.
"""
import pytest

import main

def test_visualize_tree_empty(capsys) -> None:
    """Test that visualize_tree(None) returns None and prints an 'Empty tree...' message."""
    result = main.visualize_tree(None)
    assert result is None

    captured = capsys.readouterr()
    assert "Empty tree cannot be displayed" in captured.out