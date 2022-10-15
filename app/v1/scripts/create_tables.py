from app.v1.schema.user_schema import User
from app.v1.schema.todo_schema import Todo

from app.v1.utils.db import db

def create_tables():
    with db:
        db.create_tables([User, Todo])