"""EX05 Dictionaries and Functions!"""

__author__ = "730484781"


from exercises.ex05.dictionary import invert

from exercises.ex05.dictionary import favorite_color

from exercises.ex05.dictionary import count

from exercises.ex05.dictionary import alphabetizer

from exercises.ex05.dictionary import update_attendance


def test_invert_edge() -> None:
    """Test a edge case of inverting an empty dict!"""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_invert_standard() -> None:
    """Test a standard use of the invert function with two values!"""
    test_dict: dict[str, str] = {'test': 'a', 'standard': 'b'}
    assert invert(test_dict) == {'a': 'test', 'b': 'standard'}


def test_invert_standard_again() -> None:
    """Test another standard use of the invert function!"""
    test_dict: dict[str, str] = {'test': 'a', 'again': 'b', 'but': 'c', 'longer': 'd', }
    assert invert(test_dict) == {'a': 'test', 'b': 'again', 'c': 'but', 'd': 'longer'}


def test_favorite_color_edge_case() -> None:
    """Test favorite_color to ensure a tie will output the first color seen!"""
    test_dict: dict[str, str] = {'Ryan': 'blue', 'Caleb': 'yellow', 'John': 'pink', 'Sarah': 'blue', 'James': 'yellow'}
    assert favorite_color(test_dict) == 'blue'


def test_favorite_color_standard_case() -> None:
    """Test favorite_color to ensure standard functionality!"""
    test_dict: dict[str, str] = {'Ryan': 'red', 'Caleb': 'red', 'John': 'pink', 'Sarah': 'blue', 'James': 'red'}
    assert favorite_color(test_dict) == 'red'


def test_favorite_color_standard_again() -> None:
    """Test favorite_color in a standard setting with a longer data set!"""
    test_dict: dict[str, str] = {'Ryan': 'magenta', 'Caleb': 'red', 'John': 'pink', 'Sarah': 'magenta', 'James': 'red', 'Joe': 'pink', 'Jamie': 'magenta', 'Elio': 'magenta'}
    assert favorite_color(test_dict) == 'magenta'


def test_count_edge() -> None:
    """Test that counting an empty string returns an empty dict!"""
    test_list: list[str] = []
    assert count(test_list) == {}


def test_count_standard() -> None:
    """Test the count function in a standard setting!"""
    test_list: list[str] = ['vanilla', 'chocolate', 'strawberry', 'vanilla']
    assert count(test_list) == {'vanilla': 2, 'chocolate': 1, 'strawberry': 1}


def test_count_standard_repeating_value() -> None:
    """Test the count function in a standard setting!"""
    test_list: list[str] = ['vanilla', 'vanilla', 'vanilla', 'vanilla']
    assert count(test_list) == {'vanilla': 4}


def test_alphabetizer_edge() -> None:
    """Test an edge case of alphabetizer (empty str should return empty dict)!"""
    test_list: list[str] = []
    assert alphabetizer(test_list) == {}


def test_alphabetizer_standard() -> None:
    """Test a standard case of alphabetizer!"""
    test_list: list[str] = ['bat', 'banana', 'dog', 'pecan']
    assert alphabetizer(test_list) == {'b': ['bat', 'banana'], 'd': ['dog'], 'p': ['pecan']}


def test_alphabetizer_changing_capitals() -> None:
    """Test a standard case of alphabetizer with different capital letters!"""
    test_list: list[str] = ['Boat', 'Banana', 'door', 'Tree', 'Trunk']
    assert alphabetizer(test_list) == {'b': ['Boat', 'Banana'], 'd': ['door'], 't': ['Tree', 'Trunk']}


def test_update_attendance_edge() -> None:
    """Test update_attendance but append a list of names to the current attendance!"""
    attendance_log: dict = {"Monday": ["Caleb", "John"], "Tuesday": ["Tim"]}
    update_attendance(attendance_log, "Tuesday", ["James", "John"])
    assert attendance_log == {"Monday": ["Caleb", "John"], "Tuesday": ["Tim", ["James", "John"]]}


def test_update_attendance_standard_add_day() -> None:
    """Test update_attendance when adding a day!"""
    attendance_log: dict = {"Monday": ["Caleb", "John"], "Tuesday": ["James"]}
    update_attendance(attendance_log, "Wednesday", "Johnathan")
    assert attendance_log == {"Monday": ["Caleb", "John"], "Tuesday": ["James"], "Wednesday": ["Johnathan"]}


def test_update_attendance_standard() -> None:
    """Test update_attendance standardly!"""
    attendance_log: dict = {"Monday": ["Joe"], "Tuesday": ["Sarah"]}
    update_attendance(attendance_log, "Monday", "Tim")
    assert attendance_log == {"Monday": ["Joe", "Tim"], "Tuesday": ["Sarah"]}