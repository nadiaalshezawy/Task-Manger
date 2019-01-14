#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import TaskItem, Base, Task, User

engine = create_engine('sqlite:///taskitem.db')


# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Sulaiman Ibrahim", email="sall1912@hotmail.com")
session.add(User1)
session.commit()

# Items for Important Urgent Task
task1 = Task(name="Important Urgent")

session.add(task1)
session.commit()

TaskItem1 = TaskItem(
                user_id=1,  description="start with projects"
               , task_category=task1)

session.add(TaskItem1 )
session.commit()


TaskItem2 = TaskItem(
                user_id=1,  description="Look for interior"
               , task_category=task1)

session.add(TaskItem2)
session.commit()

TaskItem3 = TaskItem(
                user_id=1,  description="Finish kids homework"
               , task_category=task1)

session.add(TaskItem3)
session.commit()

# Items for Important Not Urgent Task
task2 = Task(name="Important Not Urgent")

session.add(task2)
session.commit()

TaskItem1 = TaskItem(
                user_id=1,  description="Bring Abaya"
               , task_category=task2)

session.add(TaskItem1 )
session.commit()


TaskItem2 = TaskItem(
                user_id=1,  description="Wrap gifts"
               , task_category=task2)

session.add(TaskItem2)
session.commit()

# Items for Not Important Urgent Task
task3 = Task(name="Not Important Urgent")

session.add(task3)
session.commit()

TaskItem1 = TaskItem(
                user_id=1,  description="Buy makeup"
               , task_category=task3)

session.add(TaskItem1 )
session.commit()


TaskItem2 = TaskItem(
                user_id=1,  description="Call Kcal"
               , task_category=task3)

session.add(TaskItem2)
session.commit()

TaskItem3 = TaskItem(
                user_id=1,  description="Buy unicorn stuff"
               , task_category=task3)

session.add(TaskItem3)
session.commit()

# Items for Not Important Not Urgent Task
task4 = Task(name="Not Important Not Urgent")

session.add(task4)
session.commit()

TaskItem1 = TaskItem(
                user_id=1,  description="Buy yellow shirt"
               , task_category=task4)

session.add(TaskItem1 )
session.commit()


TaskItem2 = TaskItem(
                user_id=1,  description="print photo"
               , task_category=task4)

session.add(TaskItem2)
session.commit()

TaskItem3 = TaskItem(
                user_id=1,  description="wash house"
               , task_category=task4)

session.add(TaskItem3)
session.commit()

print ("added menu items!")
