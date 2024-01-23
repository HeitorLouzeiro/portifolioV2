from django.shortcuts import render

from .models import PersonalData

# Create your views here.


def index(request):
    template_name = 'core/pages/index.html'

    personaldatas = PersonalData.objects.all()[:1]

    context = {
        'personaldatas': personaldatas
    }
    return render(request, template_name, context)
