import os

from model.database import DATABASE_NAME, Session
import create_database as db_creator
from model.lesson import Lesson, association_table
from model.group import Group
from model.student import Student

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session = Session()

    print(session.query(Lesson).all())
    print('*' * 60)

    for it in session.query(Lesson):
        print(it)

    print('*' * 60)
    print(session.query(Lesson).count())
    print('*' * 60)
    print(session.query(Lesson).first())
    print('*' * 60)