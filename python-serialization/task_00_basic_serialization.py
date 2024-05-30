#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):

    """Serialize dictionary to a JSON file"""

    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):

    """Load and deserialize JSON data from a file"""

    with open(filename, 'r') as f:
        data = json.load(f)
    return data
