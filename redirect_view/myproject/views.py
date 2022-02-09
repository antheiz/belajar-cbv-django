from django.views.generic.base import RedirectView, TemplateView


class HomePageView(RedirectView):
    # url = '/'
    pattern_name = 'index' # redirect langsung ke nama url


# For check specific query string
class HomeUserPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        print(kwargs)
        if self.request.GET.__contains__('city') and self.request.GET.__contains__('work'):
            kwargs['city'] = self.request.GET['city']
            kwargs['work'] = self.request.GET['work']
        print(kwargs)
        # return super().get_context_data(**kwargs)
        context = kwargs
        return context

# just inheritance from base view
class HomeRedirectView(RedirectView):
    pattern_name = 'user'
    permanent = False # 302 (tra permanent) if True => 301. lihat di terminal
    query_string = True # untuk query string (https://localhost:8000/home?type=something)

    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        if kwargs['user'] == 'theisandatu':
            print("Merubah data")
            kwargs['user'] = 'theis'
        print(kwargs)
        return super().get_redirect_url(**kwargs)