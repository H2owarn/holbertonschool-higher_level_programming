#!/usr/bin/python3
"""This module converting CSV to JSON format"""


import csv
import json


def convert_csv_to_json(csv_file, json_file="data.json"):
    """Convert CSV data to JSON format"""
    try:
        with open(csv_file, 'r', encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)

            data = [row for row in csv_reader]

        with open(json_file, "w", encoding="utf-8") as file:
            json.dump(data, file)

    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
