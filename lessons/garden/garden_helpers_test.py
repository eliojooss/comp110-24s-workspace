"""Test my garden functions."""


__author__ = "730484781"

from lessons.garden.garden_helper import add_by_date

from lessons.garden.garden_helper import lookup_by_kind_and_date

from lessons.garden.garden_helper import add_by_kind


def test_add_by_kind_standard() -> None:
    """Test that when tulip is added as a flower kind, it updates to the string!"""
    test_dict: dict[str, list[str]] = {'flower': ['rose']}
    add_by_kind(test_dict, 'flower', 'tulip')
    assert test_dict == {'flower': ['rose', 'tulip']}


def test_lookup_by_kind_and_date_standard() -> None: 
    """Test that lookup_by_kind_and_date works with standard functionality!"""
    by_kind: dict[str, list[str]] = {"flower": ['tulip', 'rose']}
    by_date: dict[str, list[str]] = {"April": ['tulip'], "June": ["rose"]}
    assert lookup_by_kind_and_date(by_kind, by_date, "flower", "April") == "flowers to plant in April: ['tulip']"


def test_add_by_date_standard() -> None:
    """Test add_by_date with standard functionality!"""
    test_dict: dict[str, list[str]] = {'January': ['rose']}
    add_by_date(test_dict, 'January', 'tulip')
    assert test_dict == {'January': ['rose', 'tulip']}


def test_add_by_kind_edge() -> None:
    """Test add_by_kind in a edge circumstance (adding a plant to an empty dictionary)!"""
    test_dict: dict[str, list[str]] = {}
    add_by_kind(test_dict, 'flower', 'tulip')
    assert test_dict == {'flower': ['tulip']}


def test_add_by_date_edge() -> None:
    """Test add_by_date in a edge circumstance (adding a plant to an empty dictionary)!"""
    test_dict: dict[str, list[str]] = {}
    add_by_date(test_dict, 'January', 'tulip')
    assert test_dict == {'January': ['tulip']}


def test_lookup_by_kind_and_date_edge() -> None:
    """Test that output is correct when there are no plants that meet the criteria!"""
    test_kind: dict[str, list[str]] = {'flower': ['rose']}
    test_date: dict[str, list[str]] = {'January': ['tulip']}
    lookup_by_kind_and_date(test_kind, test_date, 'flower', 'January') == "No flowers to plant in June"