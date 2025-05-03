"""
Module for loading data from various sources
"""

import json


def load_data(file_path):
  """Loads a JSON file"""
  with open(file_path, "r") as handle:
    return json.load(handle)