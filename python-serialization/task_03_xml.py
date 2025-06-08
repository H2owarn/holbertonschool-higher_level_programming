#!/usr/bin/python3
"""This module define two main functions
Serializing and Deserializing with XML"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Convert a Python dictionary to XML and save it to a file."""
    try:
        root = ET.Element("root")

        # Convert dictionary keys and values into XML elements
        for key, value in dictionary.items():
            element = ET.Element(key)
            element.text = str(value)
            root.append(element)

        # Convert the XML structure into a tree
        tree = ET.ElementTree(root)

        # Write XML data to the specified file
        tree.write(filename, encoding="utf-8", xml_declaration=True)

        return False
    except Exception as e:
        print(f"Error during serialization: {e}")
        return False  # Failure


def deserialize_from_xml(filename):
    """Read XML data from a file and return constructed dictionary"""
    try:
        tree_parse = ET.parse(filename)
        root = tree_parse.getroot()

        # Convert XML elements into dictionary format

        data = {child.tag: child.text for child in root}
        return data

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

    except ET.ParseError:
        print(f"Error: Failed to parse {filename}, invalid XML format.")
        return None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None