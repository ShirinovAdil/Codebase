from django.shortcuts import render, redirect
from .forms import NewForm
from django.views.generic import TemplateView


class HomeForm(TemplateView):
    template_name = 'personal/home.html'

    def get(self, request, *args, **kwargs):
        form = NewForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = HomeForm(request.POST)
        if request.method == 'POST':
            form = NewForm(request.POST)

        if form.is_valid():
            return redirect(HomeForm)

# def show_form(request):
#     cooking_place = Course.objects.get(course_name__exact="Cooking")
#     networking_place = Course.objects.get(course_name__exact="Networking")
#     context = {"cooking_place": cooking_place,
#                "networking_place": networking_place
#                }
#
#     return render(request, 'basic/home.html', context)
