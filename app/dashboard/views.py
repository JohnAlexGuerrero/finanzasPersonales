from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from Transaction.models import Expense

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/index.html"
    context_data_name = "transactions"
    
    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user).order_by('-created')
    