from flask import Flask, render_template

app = Flask(__name__)


@app.route('/profiling')
def profiling():
    return render_template('profiling.html')


if __name__ == '__main__':
    app.run()
