from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.template import loader

from intapp.models import Report, ReportEntry

# Create your views here.
def index(request):
    latest_reports_list = ReportEntry.objects.all()[:5]
    report_count = ReportEntry.objects.count()
    template = loader.get_template('intapp/index.html')
    context = {
        'latest_reports_list': latest_reports_list,
        'report_count': report_count
    }
    return HttpResponse(template.render(context, request))
