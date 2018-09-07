from django.shortcuts import render, redirect
from spidey.forms import ImageForm
from spidey.spidey import analyze
from google.cloud import storage


MY_BUCKET = 'cs4263spidey'

def spidey(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            filename = request.FILES['pic'].name.replace(" ", "_").replace("(", "").replace(")", "")

            # Upload file to gcloud storage
            #storage_client = storage.Client()
            #bucket = storage_client.get_bucket(MY_BUCKET)
            #blob = bucket.blob(filename)

            #blob.upload_from_filename('/tmp/uploads/' + filename)

            # labels = analyze(file_path)
            labels = ['cool', 'fun', 'spidery']

            return render(request, 'spidey/spidey.html', {
                'form': form,
                'image': 'uploads/' + filename,
                'labels': labels
            })
    else:
        form = ImageForm()
    return render(request, 'spidey/spidey.html', {
        'form': form,
        'image': '',
        'labels': []
    })
