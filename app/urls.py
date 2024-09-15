from django.urls import path
from . import views

urlpatterns = [
    path('emit-signal/', views.emit_signal_view),
    path('emit-signals-thread/', views.emit_signal_view_thread),
]