from flask import Flask, url_for, session, render_template_string
from flask import render_template, redirect
from authlib.integrations.flask_client import OAuth
import os


GOOGLE_CLIENT_ID = ''
GOOGLE_CLIENT_SECRET = ''

app = Flask(__name__)
app.secret_key = '!secret'
app.config['GOOGLE_CLIENT_ID']=GOOGLE_CLIENT_ID
app.config['GOOGLE_CLIENT_SECRET']=GOOGLE_CLIENT_SECRET


print(app.config)

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
oauth = OAuth(app)
oauth.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid email profile'
    }
)


@app.route('/')
def homepage():
    user = session.get('user')
    # return render_template('index.html', user=user)
    # HTML template string
    template = """
    {% if user %}
    <pre>
    {{ user|tojson }}
    </pre>
    <a href="{{ url_for('logout') }}">logout</a>
    {% else %}
    <a href="{{ url_for('login') }}">login</a>
    {% endif %}
    """
    
    return render_template_string(template, user=user)


@app.route('/login')
def login():
    redirect_uri = url_for('auth', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


@app.route('/auth')
def auth():
    token = oauth.google.authorize_access_token()
    session['user'] = token['userinfo']
    return redirect('/')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


if __name__ == '__main__':
    # app.run()
    app.run(debug=True, host="0.0.0.0")
    # app.run(ssl_context=('cert.pem', 'key.pem'))