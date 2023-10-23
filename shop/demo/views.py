from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import RegisterUserForm


# Create your views here.
class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')


def about(request):
    pass


def contact(request):
    pass


def catalog(request):
    pass


def product(request):
    pass


@login_required
def cart(request):
    cart_items = request.user.cart_set.all()
    return render(request, 'demo/cart.html',
                  context={
                      'cart_items': cart_items
                  })


@login_required
def checkout(request):
    pass


@login_required
def orders(request):
    pass
