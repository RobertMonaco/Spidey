from django.shortcuts import render, redirect
from spidey.forms import ImageForm
from spidey.spidey import analyze
from google.cloud import storage
from django.core.files.storage import default_storage


MY_BUCKET = 'cs4263spidey'

def spidey(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            filename = 'uploads/' + request.FILES['pic'].name.replace(" ", "_").replace("(", "").replace(")", "")

            labels = analyze('static/' + filename)
            #labels = ['cool', 'fun', 'spidery']

            return render(request, 'spidey/spidey.html', {
                'form': form,
                'image': filename,
                'labels': labels
            })
    else:
        form = ImageForm()
    return render(request, 'spidey/spidey.html', {
        'form': form,
        'image': '',
        'labels': []
    })
