from django.shortcuts import render

def custom_404(request,exception):
    return render(request,'notfound.html',status=404)