from flask import Flask, g, render_template
import os, sqlite3

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = os.urandom(24).hex()
app.config['DEBUG'] = True

# database initialization
def db_conn():
    sql = sqlite3.connect(r'C:\Users\Khoshkar\PycharmProjects\Calories\application\database\database.db')
    sql.row_factory = sqlite3.Row
    return sql

def db_get():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = db_conn()
    return g.sqlite_db

@app.teardown_appcontext
def db_close(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', title = 'Page not found'), 404

from application.routes import food
from application.routes import date
from application.routes import view
from application.routes import home