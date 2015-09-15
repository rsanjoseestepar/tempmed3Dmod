from __future__ import absolute_import

from med3Dmodel.celery import app
import time

@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)

@app.task
def funtest(id):
    time.sleep(6)
    print id
    return