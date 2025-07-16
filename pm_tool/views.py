from flask import Blueprint, render_template, request, redirect, url_for
from .models import Task, WBSItem, User
from . import db


bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    tasks = Task.query.all()
    wbs_items = WBSItem.query.filter_by(parent_id=None).all()
    return render_template('index.html', tasks=tasks, wbs_items=wbs_items)


@bp.route('/tasks')
def tasks():
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)


@bp.route('/tasks/add', methods=['POST'])
def add_task():
    title = request.form['title']
    description = request.form.get('description')
    task = Task(title=title, description=description)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('main.tasks'))


@bp.route('/wbs')
def wbs():
    items = WBSItem.query.filter_by(parent_id=None).all()
    return render_template('wbs.html', items=items)


@bp.route('/wbs/add', methods=['POST'])
def add_wbs_item():
    name = request.form['name']
    item = WBSItem(name=name)
    db.session.add(item)
    db.session.commit()
    return redirect(url_for('main.wbs'))
