from flask import Flask, render_template
import numpy as np
from numpy import random

app = Flask(__name__)

@app.route('/')
def main():
    a = np.round(random.normal(size=20), 2)
    b = random.randint(1, 1000, size=(100))
    c = np.zeros([3, 2])
    d = np.ones([3, 2])
    e = random.randint(1, 100, size=(5, 5)).astype("i")

    return render_template('main.html', a=a, b=b, c=c, d=d, e=e)

if __name__ == '__main__':
    app.run(debug=True)