from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author':'Kevin Sandryan',
        'title': 'Blog Post 1',
        'content': 'first post content',
        'date_posted': 'September 1, 2020'
    },
     {
        'author':'John Doe',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted': 'September 2, 2020'
    },
     {
        'author':'Stephen Jordan',
        'title': 'Blog Post 3',
        'content': 'third post content',
        'date_posted': 'September 3, 2020'
    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True, port=3003)
