from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashbord.permissions import HasCustomerAccessPermission


class CustomerDashbordHomeView(LoginRequiredMixin, HasCustomerAccessPermission, TemplateView):
    template_name = "dashbord/customer/home.html"
