from django.shortcuts import render

from django.views import View
from .forms import DummyForm

class FormDummyView(View):

    # def get(self, request):
    #     # from pdb import set_trace; set_trace()  # в консоли request.GET, pp request.__dict__
    #     hello = request.GET.get('hello')  # отобразить полученную информацию (запрос в строке hello=world)
    #     return render(request, 'form.html', {'hello': hello})

    def get(self, request):
        form = DummyForm()
        return render(request, 'form.html', {'form': form})

    # def post(self, request):
    #     text = request.POST.get('text')
    #     grade = request.POST.get('grade')
    #     image = request.FILES.get('image')
    #     content = image.read()
    #     context = {
    #        'text': text,
    #        'grade': grade,
    #        'content': content,
    #     }
    #     return render(request, 'form.html', context)

    def post(self, request):
        form = DummyForm(request.POST)
        if form.is_valid():
            context = form.cleaned_data
            return render(request, 'form.html', context)
        else:
            return render(request, 'error.html', {'error': form.errors})
