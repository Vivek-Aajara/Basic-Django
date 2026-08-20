from django.shortcuts import render, redirect
from django.utils.functional import empty

from .forms import Person2Form

# Create your views here.
def formdemo(request):
    if request.method == 'POST':
        form = Person2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formdemo')
    else:
        form = Person2Form()

    return render(request, 'FormDemo.html', {'form': form})

