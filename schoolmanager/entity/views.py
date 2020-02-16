from django.shortcuts import render
from django.views import View
from .models import (
    Teacher,
    Student,
    ClassRoom,
    Subject,
    Relative,
    Chapter,
    Class,
    )
from .forms import SearchTeacher

def get_class_info(request):
    classes = Class.objects.order_by("id")
    context = {"classes": classes}
    return render(request, "entity/classroom_details.html", context)


class SearchTeacherFormView(View):
    form_class = SearchTeacher
    template_name = 'entity/search_teacher.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        context = {}
        form = self.form_class(request.POST)
        context.update({'form': form})
        if form.is_valid():
            query = form.cleaned_data.get("teacher")
            classes = form.save(query=query)
            context.update({"class":classes})
        return render(request, self.template_name, context)
