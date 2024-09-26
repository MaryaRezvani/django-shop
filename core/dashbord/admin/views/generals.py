from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashbord.permissions import HasAdminAccessPermission


class AdminDashbordHomeView(LoginRequiredMixin, HasAdminAccessPermission, TemplateView):
    template_name = "dashbord/admin/home.html"
