from django.shortcuts import render

# using class
from django.views.generic.base import TemplateView


# Inheritance dari TemplateResponseMixin
# ContextMixin
# View
class IndexPageView(TemplateView):
    pass


class ContextPageView(TemplateView):
    template_name = "class3.html"
    
    def get_context_data(self):
        context = {
            "title": "Class3PageView",
            "creator": "Theis",
        }
        return context
    

class ParameterPageView(TemplateView):
    template_name = "class4.html"

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(**kwargs)

        context['creator'] = "Theis"
        context['title'] = "ParameterPageView"
        
        return context