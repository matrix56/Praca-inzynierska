from django.shortcuts import render

def glowna(request):
    return render(request, 'Strona_glowna/glowna.html', {})