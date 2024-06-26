from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

class DB:
    def __init__(self, app=None):
        self.db = db

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.db.init_app(app)
    
    def add_todo(self, title):
        new_todo=Todo(title=title,complete=False)
        self.db.session.add(new_todo)
        self.db.session.commit()
        
    def update(self, todo_id):
        todo=Todo.query.filter_by(id=todo_id).first()
        todo.complete = not todo.complete
        self.db.session.commit()
        
    def delete(self,todo_id):
        todo=Todo.query.filter_by(id=todo_id).first()
        self.db.session.delete(todo)
        self.db.session.commit()
