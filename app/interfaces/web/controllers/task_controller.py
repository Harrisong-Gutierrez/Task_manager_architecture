# app/interfaces/web/controllers/task_controller.py
from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.core.services import TaskService
from app.infrastructure.database import TaskRepository
from app.core.models import Priority
from datetime import datetime
from app import db

bp = Blueprint('tasks', __name__, url_prefix='/tasks')

@bp.route('/', methods=['GET', 'POST'])
def manage_tasks():
    # Inicializa servicio
    repo = TaskRepository(db.session)
    service = TaskService(repo)

    # POST: Crear nueva tarea
    if request.method == 'POST':
        try:
            title = request.form['title']
            description = request.form['description']
            priority = Priority(int(request.form['priority']))
            due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d') if request.form.get('due_date') else None
            
            service.create_task(
                title=title,
                description=description,
                priority=priority,
                due_date=due_date
            )
            flash('Tarea creada exitosamente', 'success')
        except ValueError as e:
            flash(str(e), 'danger')
        except Exception:
            flash('Error al crear la tarea', 'danger')

        return redirect(url_for('tasks.manage_tasks'))

    # GET: Mostrar tareas
    show_completed = request.args.get('show_completed', 'all')
    sort_by = request.args.get('sort_by', 'priority')

    tasks = service.list_tasks(
        completed=None if show_completed == 'all' else show_completed == 'completed',
        sort_by=sort_by
    )

    return render_template(
        'tasks.html',
        tasks=tasks,
        Priority=Priority,
        show_completed=show_completed,
        sort_by=sort_by
    )

@bp.route('/complete/<task_id>')
def complete_task(task_id):
    repo = TaskRepository(db.session)
    service = TaskService(repo)
    
    if service.complete_task(task_id):
        flash('Tarea completada', 'success')
    else:
        flash('Tarea no encontrada', 'danger')
    
    return redirect(url_for('tasks.manage_tasks'))

@bp.route('/delete/<task_id>')
def delete_task(task_id):
    repo = TaskRepository(db.session)
    service = TaskService(repo)
    
    if service.delete_task(task_id):
        flash('Tarea eliminada', 'success')
    else:
        flash('Error al eliminar tarea', 'danger')
    
    return redirect(url_for('tasks.manage_tasks'))