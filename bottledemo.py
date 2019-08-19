from bottle import run, route, template, get, post, request, Bottle, static_file, response

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='/Users/ankitkumar/Desktop/Screenshots')

#@route('/hello/<name>')
@route('/', method='GET')
def index(name='ankit'):
    #return '<h1> hello world </h>'
    return '''
           <form action="/login" method="post">
               Username: <input name="username" type="text" />
               Password: <input name="password" type="password" />
               <input value="Login" type="submit" />
           </form>
       '''
    return template('Hello {{name}}, how are you?', name=name)


@route('/hello')
def hello_again():
    if request.get_cookie("visited"):
        return "Welcome back! Nice to see you again"
    else:
        response.set_cookie("visited", "yes")
        return "Hello there! Nice to meet you"

@route('/', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

@route('/forum')
def display_forum():
    forum_id = request.query.id
    page = request.query.page or '1'
    return template('Forum ID: {{id}} (page {{page}})', id=forum_id, page=page)


run()
