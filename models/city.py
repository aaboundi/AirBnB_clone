#!/usr/bin/python3
# city.py
"""Module for City class."""

from models.base_model import BaseModel


class City(BaseModel):
    """Class representing a City."""
    state_id = ""
    name = ""
