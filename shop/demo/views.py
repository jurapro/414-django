from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import RegisterUserForm
from .models import Order, Product, Cart


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


@login_required
def to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    item_in_cart = Cart.objects.filter(user=request.user, product=product).first()
    if item_in_cart:
        if item_in_cart.count + 1 > product.count:
            return JsonResponse({
                'error': 'Не могу добавить'
            })
        item_in_cart.count += 1
        item_in_cart.save()
        return JsonResponse({
            'count': item_in_cart.count
        })
    item_in_cart = Cart(user=request.user, product=product, count=1)
    item_in_cart.save()
    return JsonResponse({
        'count': item_in_cart.count
    })
