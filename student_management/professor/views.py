from django.shortcuts import render
from .models import Professor, Subject


def professor_list(request):
    professors = Professor.objects.all()
    subjects = Subject.objects.select_related("professor").all()
    return render(
        request,
        "professor/professor_list.html",
        {"professors": professors, "subjects": subjects},
    )
