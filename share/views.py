from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import UpdateView, CreateView
from django.urls import reverse_lazy
from .forms import ShareForm, ShareFormEx
from .models import Code, PersonalCode
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User


def show_code(request):
    # Shows list of all exercises 'share.html'

    search_query = request.GET.get('search', '')
    if search_query:
        all_codes_previous = Code.objects.filter(title__icontains=search_query)
    else:
        all_codes_previous = Code.objects.all().order_by('-date')
    page = request.GET.get('page', 1)
    paginator = Paginator(all_codes_previous, 4)
    try:
        all_codes = paginator.page(page)
    except PageNotAnInteger:
        all_codes = paginator.page(1)
    except EmptyPage:
        all_codes = paginator.page(paginator.num_pages)
    num_of_visits = request.session.get('num_of_visits', 0)
    request.session['num_of_visits'] = num_of_visits + 1
    context = {'all_codes': all_codes, 'num_of_visits': num_of_visits}
    return render(request, 'share/share.html', context) #share.html



class AddExercise(CreateView):
    # Add new problem to list of problems 'add_code.html'
    form_class = ShareFormEx
    template_name = 'share/add_code.html'

    def get_success_url(self):
        return reverse('share:code_details', kwargs={'pk': self.object.pk})


@staff_member_required()
def delete_problem(request, code_id):
    # Delete selected problem from list
    Code.objects.filter(pk=code_id).delete()
    return redirect('share:show_code')


def code_details(request, pk=None):
    # List of users sent solutions, ADD SOLUTION 'share_details.html'
    ex = get_object_or_404(Code, pk=pk)
    codes = PersonalCode.objects.filter(code_id=pk).order_by('-date')
    return render(request, 'share/share_details.html', {"codes": codes, 'ex': ex})


def personal_code(request, some=None, code_id=None):
    # Shows source of each user 'personal_code.html'
    to_edit = get_object_or_404(Code, pk=some)
    code = get_object_or_404(PersonalCode, pk=code_id)
    return render(request, 'share/personal_code.html', {"code": code, 'to_edit': to_edit})


class UpdateCode(UpdateView):
    @method_decorator(login_required(redirect_field_name='accounts:login'))
    def dispatch(self, *args, **kwargs):
        return super(UpdateCode, self).dispatch(*args, **kwargs)

    def get_object(self, queryset=None):
        # To pass pk to class based view
        cid = self.kwargs.get('code_id')
        return PersonalCode.objects.get(pk=cid)

    model = PersonalCode
    fields = ['author_code']
    template_name = 'share/add_code.html'
    success_url = reverse_lazy('share:show_code')


def delete_code(request, code_id=None):
    # Find another way if doesnt work
    PersonalCode.objects.filter(pk=code_id).delete()
    return redirect('share:show_code')


@login_required(login_url='/accounts/login')
def add_new_solution(request, ex_id=None):
    # Adds new solution
    # Fix redirect
    parent_ex = Code.objects.get(pk=ex_id)
    current_user = request.user
    if request.method == "POST":
        form = ShareForm(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = current_user.username
            form.code_id = parent_ex
            form.save()
            return redirect('share:code_details', pk=ex_id)
    else:
        form = ShareForm()
    return render(request, 'share/add_solution.html', {'form': form})


@staff_member_required(login_url='/accounts/login/')
def show_users_list(request):
    users_list = User.objects.all()
    return render(request, 'share/admin_show_users.html', {'users_list': users_list})

