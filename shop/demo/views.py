from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import RegisterUserForm
from .models import Order, Product


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
    products = Product.objects.filter(count__gte=1)
    return render(request, 'demo/catalog.html',
                  context={
                      'products': products
                  })


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


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = 'demo/orders.html'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-date')
