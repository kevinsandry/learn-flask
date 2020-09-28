from flaskblog import app

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
    app.run(debug=True, port=3003)