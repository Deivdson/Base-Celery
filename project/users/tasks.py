from celery import shared_task


@shared_task(max_retries=3)
def divide():
    import time
    time.sleep(5)
    return 2 / 4