#!/usr/bin/python3
"""Module for XML serialization and deserialization
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize dictionary to XML and save to file.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserialize XML data from file into dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    return dictionary
