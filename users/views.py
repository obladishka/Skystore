from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserForm
from users.models import User


class RegisterView(CreateView):

    model = User
    form_class = UserForm
    template_name = "registration/login.html"
    success_url = reverse_lazy("catalog:product_list")
