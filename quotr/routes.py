from quotr import app, manager
from quotr.models import Country, User

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

manager.create_api(Country, methods=['GET', 'POST', 'PUT', 'DELETE'])
manager.create_api(User, methods=['GET', 'POST', 'PUT', 'DELETE'])
