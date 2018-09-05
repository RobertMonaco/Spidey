from django.shortcuts import render, redirect
from spidey.forms import ImageForm
from spidey.spidey import analyze


def spidey(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            file = request.FILES['pic']

            analyze("spidey/SpiderPics/" + file.name)

            return redirect('/')
    else:
        form = ImageForm()
    return render(request, 'spidey/spidey.html', {
        'form': form
    })
