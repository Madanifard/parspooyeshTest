import os
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views import View
from .forms import searchForm
from .utilise import fined_register_user, report_register_people_pandas

class SearchReport(View):

    def get(self, request):
        ''''
        METHOD: GET
        show the form for search in Data
        '''
        form = searchForm()
        return render(request, 'export/index.html', {
            'form': form
        })
    
    def post(self, request):
        '''
        METHOD: POST
        get Data 
        1) check the validate dates that end_date not greater than start_date
        2) search in Data with pymongo
        3) convert Data find to DataFrame Pandas and export to csv file
        '''
        form = searchForm(request.POST)
        if form.is_valid():
            result_find = fined_register_user(start_date=request.POST['start_date'], end_date=request.POST['end_date'])
            if result_find['error']:
                return render(request, 'export/index.html', {
                'form': form,
                'error': result_find['error'],
                'message': result_find['message'],
                })
            else:
                result = report_register_people_pandas(items=result_find['data'])
                return render(request, 'export/index.html', {
                    'form': form,
                    'error': result['error'],
                    'message': result['message'],
                })
        else:
            return render(request, 'export/index.html', {
                'form': form,
            })

def download(request):
    '''
    create link download report file
    '''
    file_path = os.path.join('reports/output_report.csv')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404