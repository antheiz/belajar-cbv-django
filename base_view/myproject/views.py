# fbv
from urllib import request
from django.shortcuts import render

# cbv
from django.views import View


def index(request):
    context = {
        'heading': 'Selamat Datang',
        'by': 'FBV',
    }

    if request.method == 'POST':
        context['heading'] = 'Function Based View - POST'

    return render(request, 'index.html', context)


class IndexPageView(View):

    template_name = ''
    context = {
        'by': 'CBV'
    }

    def get(self, request):
        self.context['heading'] = 'Selamat Datang'
        return render(request, self.template_name, self.context)

    def post(self, request):
        self.context['heading'] = 'Class Based View - POST'
        return render(request, self.template_name, self.context)

    
