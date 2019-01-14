#!/usr/bin/env python3
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


class Task(Base):
    __tablename__ = 'task_category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    #user_id = Column(Integer, ForeignKey('user.id'))
    #user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            #'user_id': self.user_id,
            }


class TaskItem(Base):
    __tablename__ = 'task_item'

    #name = Column(String(80), nullable=False, unique=True)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    task_id = Column(Integer, ForeignKey('task_category.id'))
    task_category = relationship(Task)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            #'name': self.name,
            'description': self.description,
            'id': self.id,
            'task_id': self.task_id,
            'user_id': self.user_id,
        }


engine = create_engine('sqlite:///taskitem.db')
Base.metadata.create_all(engine)
