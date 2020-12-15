from sample import celery


@celery.task()
def add_together(a: float, b: float) -> float:
    return a + b
