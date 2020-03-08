from django.urls import path

from start.apps.blog import views

urlpatterns=[
    path('blog/', views.index, name=index),
    path('blog/add/', views.add, name=add),
    path('blog/edit/<int:entry_id>/', views.edit, name=edit),
]