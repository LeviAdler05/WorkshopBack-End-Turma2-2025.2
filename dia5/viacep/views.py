from django.views.generic import FormView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Endereco
from .forms import EnderecoForm

class EnderecoCreateView(FormView):
    template_name = 'viacep/endereco_form.html'
    form_class = EnderecoForm
    success_url = reverse_lazy('viacep:list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class EnderecoListView(ListView):
    model = Endereco
    template_name = 'viacep/endereco_list.html'
    context_object_name = 'enderecos'

class EnderecoDetailView(DetailView):
    model = Endereco
    template_name = 'viacep/endereco_detail.html'

class EnderecoDeleteView(DeleteView):
    model = Endereco
    template_name = 'viacep/endereco_confirm_delete.html'
    success_url = reverse_lazy('viacep:list')