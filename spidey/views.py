from django.shortcuts import render, redirect
from spidey.forms import ImageForm
from spidey.spidey import analyze


def spidey(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            file = request.FILES['pic']
            file_path = "static/uploads/" + file.name.replace(" ", "_")

            # labels = analyze(file_path)
            labels = ['cool', 'fun', 'spidery']

            return render(request, 'spidey/spidey.html', {
                'form': form,
                'image': file_path,
                'labels': labels
            })
    else:
        form = ImageForm()
    return render(request, 'spidey/spidey.html', {
        'form': form,
        'image': '',
        'labels': []
    })
