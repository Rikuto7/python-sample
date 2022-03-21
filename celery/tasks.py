import time

import celery


app = celery.Celery(
    'tasks',
    broker='',
    backend=''
)

@app.task
def task():
    time.sleep(5)
    print('dome')

@app.task
def group_task():
    group = celery.group(
        task.s() for _ in range(10)
    )
    return group()

@app.task
def call_back(result):
    print(result)

@app.task
def chord_task():
    chord = celery.chord(
        (task.s() for _ in range(10)),
        call_back.s()
    )
    return chord()

# celery -A tasks woeker --logvel=info
