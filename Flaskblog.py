from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '1d75f0b0cdb877293206b6b6edfeae0b'

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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'kevinsandry' and form.password.data == 'password':
            flash(f'Hello {form.username.data}!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Wrong username or password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
    app.run(debug=True, port=3003)
