from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse, Http404
from django.template import loader

from fakenews_api.models import Report


# Create your views here.
def index(request):
    latest_reports_list = Report.objects.order_by('-pub_date')[:5]
    report_count = Report.objects.count()
    template = loader.get_template('fakenews_api/index.html')
    context = {
        'latest_reports_list': latest_reports_list,
        'report_count' : report_count
    }
    return HttpResponse(template.render(context, request))

def training(request):
    training_reports_list = Report.objects.filter(is_train = True).order_by('-pub_date')[:100]
    report_count = Report.objects.filter(is_train = True).count()
    template = loader.get_template('fakenews_api/training.html')
    context = {
        'training_reports_list': training_reports_list,
        'report_count' : report_count
    }
    return HttpResponse(template.render(context, request))

def detail(request, report_id):
    r = get_object_or_404(Report, pk=report_id)
    return render(request, 'fakenews_api/detail.html', {'report': r})


# api web views
def report_list(request):
    MAX_OBJECTS = 20
    reports = Report.objects.all()[:MAX_OBJECTS]
    data = {
        "results" : list(reports.values("title", "author", "content", "pub_date"))
    }
    return JsonResponse(data)

def report_detail(request, pk):
    report = get_object_or_404(Report, pk = pk)
    data = {
        "results" : {
            "title" : report.title,
            "author" : report.author,
            "content" : report.content,
            "pub_date" : report.pub_date
        }
    }
    return JsonResponse(data)
