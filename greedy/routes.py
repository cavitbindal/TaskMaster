from flask import render_template, request, redirect, url_for
from greedy.db import Todo

def configure_routes(app, db_instance):
    @app.route('/')
    def index():
        todo_list = Todo.query.all()
        print(todo_list)
        return render_template('base.html',todo_list=todo_list)

    @app.route("/add",methods=["POST"])
    def add():
        title = request.form.get("title")

        db_instance.add_todo(title)

        return redirect(url_for("index"))

    @app.route("/update/<int:todo_id>")
    def update(todo_id):
        db_instance.update(todo_id)
        return redirect(url_for("index"))    

    @app.route("/delete/<int:todo_id>")
    def delete(todo_id):
        db_instance.delete(todo_id)
        return redirect(url_for("index"))
