from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .forms import CodeSearchForm, ExpiringFileForm
from .models import UploadedFile

def upload_file(request):
    if request.method == 'POST':
        form = ExpiringFileForm(request.POST, request.FILES)
        if form.is_valid():
            expiring_file = form.save(commit=False)
            expiring_file.expiration_date = timezone.now() + timezone.timedelta(days=7)  # Set expiration date
            expiring_file.save()
            return redirect('success')  # Update this to your success page or render a success template
    else:
        form = ExpiringFileForm()
    return render(request, 'main/upload.html', {'form': form})

def access_file(request, code):
    uploaded_file = get_object_or_404(UploadedFile, code=code)
    response = HttpResponse(uploaded_file.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def home(request):
    return render(request, 'main/home.html')

def search_code(request):
    if request.method == 'POST':
        form = CodeSearchForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            return redirect('access_file', code=code)
    else:
        form = CodeSearchForm()
    return render(request, 'main/search.html', {'form': form})

def success(request):
    return render(request, 'main/success.html')

