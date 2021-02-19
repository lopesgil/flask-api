from quotr import app,db
from quotr.models import User, Country

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Country': Country}
