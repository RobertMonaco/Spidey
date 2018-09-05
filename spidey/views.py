from django.shortcuts import render, redirect
from spidey.forms import ImageForm
from spidey.spidey import analyze


def spidey(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            labels = analyze()

            return redirect('/')
    else:
        form = DocumentForm()
    return render(request, 'spidey/spidey.html', {
        'form': form
    })