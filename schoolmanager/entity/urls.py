from django.urls import path

from . import views

urlpatterns = [
    path("get_class_info", views.get_class_info, name="get_class_info"),
    path("search_teacher", views.SearchTeacherFormView.as_view(), name="search_teacher"),
]