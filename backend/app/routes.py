from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import TodoItem

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required  # Ensure the user is logged in before viewing the to-do list
def index():
    todos = TodoItem.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', todos=todos)

@main_bp.route('/add', methods=['POST'])
@login_required
def add_todo():
    task = request.form.get('task')
    if task:
        new_todo = TodoItem(task=task, user_id=current_user.id)
        db.session.add(new_todo)
        db.session.commit()
    return redirect(url_for('main.index'))

@main_bp.route('/delete/<int:id>')
@login_required
def delete_todo(id):
    todo = TodoItem.query.get(id)
    if todo and todo.user_id == current_user.id:
        db.session.delete(todo)
        db.session.commit()
    return redirect(url_for('main.index'))

@main_bp.route('/toggle/<int:id>')
@login_required
def toggle_todo(id):
    todo = TodoItem.query.get(id)
    if todo and todo.user_id == current_user.id:
        todo.done = not todo.done
        db.session.commit()
    return redirect(url_for('main.index'))

