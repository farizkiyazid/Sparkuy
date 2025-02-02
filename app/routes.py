from app import app, controller
from flask import render_template, request

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

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
        <ul>
            <li><a class="active" href="/">Sparkuy</a></li>
        </ul>
        <br>
        ''' + controller.searchLocal(searchKey) + '''
    </body>
</html>'''
    return out

@app.route('/detail', methods=['POST'])
def handle_detail():
    Id = request.form['id']
    return controller.getAttrById(Id)