from django.urls import path
from .views import *
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/invoice',permanent=False), name="index"),
    path('invoice/', get_data, name="invoice"),
    path('update/<int:id>/', update, name="update"),
    path('remove/<int:id>/', remove, name="remove"),
]
