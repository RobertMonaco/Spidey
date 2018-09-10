from django.shortcuts import render, redirect
from spidey.forms import ImageForm
from spidey.spidey import analyze, Spider
from google.cloud import storage
from django.core.files.storage import default_storage


MY_BUCKET = 'cs4263spidey'


def spidey(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            filename = 'uploads/' + request.FILES['pic'].name.replace(" ", "_").replace("(", "").replace(")", "")

            print(filename)
            spider = analyze('static/' + filename)

            return render(request, 'spidey/spidey.html', {
                'form': form,
                'image': filename,
                'spider': spider,
            })
    else:
        form = ImageForm()
    return render(request, 'spidey/spidey.html', {
        'form': form,
        'image': '',
        'spider': None,
    })
