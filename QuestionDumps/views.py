from django.shortcuts import render
from .models import *
# Create your views here.
def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = QuizFile(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect('list')
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = QuizFile.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'list.html',
        {'documents': documents, 'form': form}
    )
