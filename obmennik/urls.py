from django.contrib import admin
from django.urls import include, path
from orders.views import send_order
from app.views import index
urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('success', send_order, name='send_order')
]
