from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import Class3Form
from .models import class4Model
from django.urls import reverse_lazy
class Home(TemplateView):
    template_name = 'home.html'

class Thankyou(TemplateView):
    template_name = 'thankyou.html'

class Class1(TemplateView):
    template_name = 'class1.html'

class Class2(TemplateView):
    template_name = 'class2.html'

class Class3(FormView):
    #In form view form_valid function check accepts the data from the template and do the task specified inside the function.
    form_class = Class3Form
    template_name = 'class3.html'
    success_url = reverse_lazy('app1:class4') #using reverse_lazy, need to specify as same as in html templates with format(app_name : url name='')
    def form_valid(self, form):  
        print(form.cleaned_data)
        return super().form_valid(form)
    
class Class4(CreateView):
    #default template name is model.html
    model = class4Model
    fields = "__all__"
    success_url = '/Thankyou/' #if we directly give value without reverse_lazy we need to give the url directly.

class Class5(ListView):
    #default template name is model_list.html
    model = class4Model
    queryset=class4Model.objects.order_by('name')
    context_object_name = 'class5'

class Class6(DetailView):
    #default template name is model_detail.html
    model = class4Model

class Class7(UpdateView):
    #default template name is same as Createview, ie, model_form.html
    #need to specify primary key in urls.py.
    model = class4Model
    fields = "__all__"
    success_url = reverse_lazy('app1:Thankyou')

class Class8(DeleteView):
    #default template name = model_confirm_delete.html
    #need to specify primary key in urls.py.
    model = class4Model
    success_url = '/Thankyou/'