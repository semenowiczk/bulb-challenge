#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import json

def get_readings(readings_file):
    """Load readings from local filesysystem.
    There's no need to refactor this function.
    The json library reads until EOF and then loads into memory.
    Returns a dictionary."""
    with open(readings_file, 'r') as f:
        readings = json.load(f)
    return readings
