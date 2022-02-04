import imp
from django.contrib import admin
from django.urls import path

from django.views.generic.base import TemplateView

from .views import IndexPageView, ContextPageView, ParameterPageView

urlpatterns = [
    path('parameter/<int:parameter>/', ParameterPageView.as_view()),
    path('class3/', ContextPageView.as_view()),
    path('class2/', TemplateView.as_view(template_name="class2.html")),
    path('class1/', IndexPageView.as_view(template_name="index.html")),
    path('admin/', admin.site.urls),
]


"""

1. Membuat class view di views.py tapi menggunakan templatenya di urls
2. Jika halaman kita itu statis, tidak ada perubahan apapun,
   maka kita lakukan templateview langsung pada urls.py
3. Membuat views dengan context saja,kita menggunakan class 
   TemplateView di views.py
4. Kita memasukan parameter ke dalam template, di atur pada urls.py 
   dengan menggunakan path

"""