#!/usr/bin/python3
"""Script defnes DataBAse storage class"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import class_mapper
from os import environ
from models.base_model import Base, BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """database storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes instance varibles/attributes"""
        user = environ['HBNB_MYSQL_USER']
        pwrd = environ['HBNB_MYSQL_PWD']
        host = environ['HBNB_MYSQL_HOST']
        db = environ['HBNB_MYSQL_DB']
        is_test = environ['HBNB_ENV']
        _url = 'mysql+mysqldb://{}:{}@{}/{}'.format(user, pwrd, host, db)
        self.__engine = create_engine(_url, pool_pre_ping=True)

        if is_test == 'test':
            metadata = MetaData()
            metadata.reflect(bind=self.__engine)
            metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        '''
            Query current database session
        '''
        db_dict = {}
        classes = {"User": User, "BaseModel": BaseModel,
                    "Place": Place, "State": State,
                    "City": City, "Amenity": Amenity,
                    "Review": Review}

        if cls:
            objs = self.__session.query(classes[cls]).all()
            for obj in objs:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                db_dict[key] = obj
            return db_dict
        else:
            for k, v in classes.items():
                if k not in ["BaseModel", "Amenity"]:
                    objs = self.__session.query(v).all()

                    if len(objs) > 0:
                        for obj in objs:
                            key = "{}.{}".format(obj.__class__.__name__,
                                                 obj.id)
                            db_dict[key] = obj
            return db_dict

    def new(self, obj):
        """adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables in the database"""
        from sqlalchemy.orm import sessionmaker, scoped_session

        self.__session = Base.metadata.create_all(self.__engine)
        ssmaker = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ssmaker)
        self.__session = Session()

    def close(self):
        """Close private session attribute"""
        self.__session.close()
