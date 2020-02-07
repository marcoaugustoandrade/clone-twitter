from app import app


@app.route('/index', methods=['GET'])
@app.route('/')
def index():
    return '<h1>Olá mundo!</h1>'

@app.route('/teste')
@app.route('/teste/<string:name>')
def teste(name=None):
    if name:
        return 'Olá, %s!' % name
    else:
        return 'Olá usuário!'
