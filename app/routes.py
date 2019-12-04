from app import app, controller
from flask import render_template, request

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kiki'}
    return render_template('index.html', title='Home', user=user)

@app.route('/search', methods=['POST'])
def handle_data():
    searchKey = request.form['searchKey']
    out = '''
<html>
    <head>
        <title>Search Page - Sparkuy</title>
        '''+controller.style+'''
    </head>
    <body>
        ''' + controller.searchLocal(searchKey) + '''
    </body>
</html>'''
    return out

@app.route('/detail', methods=['POST'])
def handle_detail():
    Id = request.form['id']
    return controller.getAttrById(Id)