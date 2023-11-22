#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref='state', cascade='all, delete, delete-orphan')

    else:
        name = ''

        @property
        def cities(self):
            """Getter attribute that returns the list of City instances"""
            from models import storage
            from models.city import City
            city_inst = storage.all(City)
            return [city for city in city_inst.values() if city.state_id == self.id]