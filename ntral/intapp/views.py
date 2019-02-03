from django.http import HttpResponse
from django.template import loader

from intapp.models import ReportEntry


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
