from flask import render_template, flash, redirect
from application1 import app
from application1.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Mike'}

	posts = [
		{
			'author': {'username': 'John'},
			'body': 'Beautiful day here!'
		},
		{
			'author': {'username': 'Susan'},
			'body': "It was a cool movie!"
		}
	]

	return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}' .format(
			form.username.data, form.remember_me.data))
		return redirect({{ url_for('index') }})
	return render_template('login.html', title='Sign In', form=form)