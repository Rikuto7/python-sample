import tasks


def main():
    result = tasks.task.delay()
    print(result)
    status = True
    while status:
        if result.ready():
            print(result.get())
            status = False
        else:
            pass
