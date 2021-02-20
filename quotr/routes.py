from quotr import app, manager, db
from quotr.models import Country, User, FavoriteQuote
from flask_restless import ProcessingException
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv
import os
import requests

load_dotenv()
CLIENT_KEY = os.getenv('CLIENT_KEY') or ''
headers = {
    'Authorization': 'Token token=' + CLIENT_KEY
}

@app.route('/')
@app.route('/index')
def index():
    return "Bem-vinde à API do trabalho final do PSI de Tech Lead!"

def pre_create_user(data=None, **kw):
    data['password'] = generate_password_hash(data['password'])

def post_create_user(result=None, **kw):
    user_id = result['id']
    r = requests.get('https://favqs.com/api/quotes/', headers=headers)
    if r.status_code != 200:
        user = User.query.filter_by(id=user_id).first()
        db.session.delete(user)
        db.session.commit()
        raise ProcessingException(description='Not Authorized',
                                  code='401')
    q = r.json()['quotes'][0]

    quote = FavoriteQuote(user_id=user_id, body=q['body'], author=q['author'])
    db.session.add(quote)
    db.session.commit()

manager.create_api(Country, methods=['GET', 'POST', 'PUT', 'DELETE'])

manager.create_api(User,
                   methods=['GET', 'POST', 'PUT', 'DELETE'],
                   preprocessors={
                       'POST': [pre_create_user]
                   },
                   postprocessors={
                       'POST': [post_create_user]
                   })

manager.create_api(FavoriteQuote, methods=['GET', 'POST', 'PUT', 'DELETE'])
