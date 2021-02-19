from quotr import app, manager
from quotr.models import Country, User
from werkzeug.security import generate_password_hash

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

def pre_create_user(data=None, **kw):
    data['password'] = generate_password_hash(data['password'])

manager.create_api(Country, methods=['GET', 'POST', 'PUT', 'DELETE'])
manager.create_api(User,
                   methods=['GET', 'POST', 'PUT', 'DELETE'],
                   preprocessors={
                       'POST': [pre_create_user]
                   })
