#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer(), default=0, nullable=False)
        number_bathrooms = Column(Integer(), default=0, nullable=False)
        max_guest = Column(Integer(), default=0, nullable=False)
        price_by_night = Column(Integer(), default=0, nullable=False)
        latitude = Column(Float(), nullable=True)
        longitude = Column(Float(), nullable=True)
        reviews = relationship("Review", backref='place', cascade='all, delete, delete-orphan')
    else:
        amenity_ids = []
        @property
        def reviews(self):
            """Getter attribute that returns the list of City instances"""
            from models import storage
            from models.review import Review
            review_inst = storage.all(Review)
            return [review for review in review_inst.values() if review.place_id == self.id]
