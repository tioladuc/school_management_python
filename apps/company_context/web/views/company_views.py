from django.views.generic import FormView
from django.urls import reverse_lazy
from ..forms.company_form import CompanyForm
from ...application.commands.create_company import CreateCompanyCommand
from ...api.dependencies import services
class CompanyCreateWebView(FormView):
    template_name='company_context/company_form.html';form_class=CompanyForm;success_url=reverse_lazy('company-created')
    def form_valid(self,form): self.result=services()['company'].create(CreateCompanyCommand(**form.cleaned_data));return super().form_valid(form)
