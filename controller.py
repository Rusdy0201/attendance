from flask import Flask, render_template, url_for

app = Flask(__name__)

value = [
{
    'monthly':'$55,000',
    'Annual':'$300.000'

}
]

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html', value=value, title='Dashboard')


if __name__ == '__main__':
    app.run(debug = True)
