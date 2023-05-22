# ORM - SQLAlchemy

# pip install sqlalchemy

import os
from database import DATABASE_NAME, Session
import create_database as db_creator

from student import Student
from group import Group

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()
