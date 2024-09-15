from django.shortcuts import render
import time
from django.http import HttpResponse
from .signals import task_done
from .signals import another_task_done
import threading
from app.models import MyModel


# Create your views here.

def emit_signal_view(request):
    start_time = time.time()

    print(f"View running in thread: {threading.get_ident()}")

    # Emit the signal
    task_done.send(sender=None)

     # Check if changes were made
    count = MyModel.objects.count()

    end_time = time.time()
    elapsed_time = end_time - start_time

    return HttpResponse(f"Signal emitted and task done in {elapsed_time:.2f} seconds and {threading.get_ident()} and database count is {count}")


#demonstrating that the signals are processed synchronously in the same thread.
def emit_signal_view_thread(request):
    start_time = time.time()

    print(f"View running in thread: {threading.get_ident()}")

    # Emit the signals
    task_done.send(sender=None)
    another_task_done.send(sender=None)

    # Check if changes were made
    count = MyModel.objects.count()

    end_time = time.time()
    elapsed_time = end_time - start_time

    return HttpResponse(f"Signals emitted and tasks done in {elapsed_time:.2f} seconds and {threading.get_ident()} database count is and {count}")
