import time
import django.dispatch
from django.dispatch import receiver
import threading
from django.db import transaction
from app.models import MyModel

# custom signal
task_done = django.dispatch.Signal()

#another custom signal
another_task_done = django.dispatch.Signal()

# Receiver function connected to the signal
@receiver(task_done)
def task_receiver(sender, **kwargs):
    print("Signal received. Starting a task.")
    print(f"Task signal handler running in thread: {threading.get_ident()}")

    with transaction.atomic():  # Ensures the operation is part of the transaction
        MyModel.objects.create(name='Task Done Entry')
        print("Database change made by task_receiver.")

    time.sleep(20)  # Simulate a task
    print("Task completed after 20 seconds.")
    print(f"Task signal handler completed in thread: {threading.get_ident()}")

@receiver(another_task_done)
def another_task_receiver(sender, **kwargs):
    print("Signal received. Starting a task.")
    print(f"Another task signal handler running in thread: {threading.get_ident()}")

    with transaction.atomic():  # Ensures the operation is part of the transaction
        MyModel.objects.create(name='Another Task Done Entry')
        print("Database change made by another_task_receiver.")

    time.sleep(25)  # Simulate a task
    print("Task completed after 25 seconds.")
    print(f"Another task signal handler completed in thread: {threading.get_ident()}")

