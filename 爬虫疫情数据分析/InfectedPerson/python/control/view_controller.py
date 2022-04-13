from web import app
from flask import render_template


@app.route('/')
def user_index():
    return render_template('index.html')


@app.route('/seach_data')
def seach_data():
    return  render_template('seach_data.html')

@app.route('/news')
def news():
    return  render_template('news.html')

