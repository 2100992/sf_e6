from apps.app import app
from flask import render_template
from flask import request
import functools

# @functools.lru_cache(maxsize=1280, typed=False)
# def fibo_steroids(n):
#     if n in [0, 1]:
#         return n
#     else:
#         return fibo_steroids(n-1) + fibo_steroids(n-2)


# @functools.lru_cache(maxsize=1280, typed=False)
def new_fibo(n):

    fib1 = fib2 = 1

    if n in [0,1]:
        return n

    for _ in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2

    return fib2



@app.route('/')
def index():
    k = request.args.get('k', 0)
    try:
        k = int(k)
    except:
        k = 0
    fibo = new_fibo(k)
    return render_template('index.html', n=fibo)


# @app.route('/<number>')
# def fibo(number):
#     fibo = fibo_steroids(int(number))
#     return render_template('index.html', n=str(fibo))

# @app.route('/new/<number>')
# def fibo_for(number):
#     fibo = new_fibo(int(number))
#     return render_template('index.html', n=str(fibo))