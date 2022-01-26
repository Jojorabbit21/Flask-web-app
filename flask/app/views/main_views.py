from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hi')
def hello():
  return 'Welcome, Stranger!'

@bp.route('/')
def index():
  return ('INDEX:')