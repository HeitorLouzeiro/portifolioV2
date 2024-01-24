from django.shortcuts import render

from .models import About, PersonalData

# Create your views here.


def index(request):
    template_name = 'core/pages/index.html'

    personaldatas = PersonalData.objects.all()[:1]
    abouts = About.objects.all()[:1]

    context = {
        'personaldatas': personaldatas,
        'abouts': abouts,
    }
    return render(request, template_name, context)
