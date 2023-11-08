"""Generating the difference between two files."""


from hexlet_code.tools.parse_file import get_dict_from_file
from hexlet_code.tools.diff import diff
from hexlet_code.formatters.format_diff import format_diff


def generate_diff(path_file1, path_file2, format_name='stylish'):
    """Create a difference between two files in a selected format.
    Return string."""
    dict1 = get_dict_from_file(path_file1)
    dict2 = get_dict_from_file(path_file2)
    list_diff = diff(dict1, dict2)
    return format_diff(list_diff, format_name)