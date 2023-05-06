from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from orderfood.forms import PartialForm, RegisterUserForm, LoginUserForm
from orderfood.models import Dish, Order, Employee, DishOrder


def index(request):
    if request.user.is_authenticated:
        return redirect('order')
    return redirect('sign')


def order(request):
    if not request.user.is_authenticated:
        return redirect('auth')
    print(request.POST)
    if request.POST:
        form = PartialForm(request.POST)
        if form.is_valid():
            order = Order(date=request.POST['date'], employee=form.cleaned_data.get('employee'), user=request.user)
            order.save()
            for i in range(1, len(request.POST)):
                if ('selectedDish_' + str(i)) in dict(request.POST):
                    dish = Dish.objects.get(pk=request.POST['selectedDish_' + str(i)])
                    print(dish)
                    dishOrder = DishOrder(dish=dish, order=order)
                    dishOrder.save()

    form = PartialForm()
    dishes = Dish.objects.all()
    order_history = {}
    users_orders = Order.objects.filter(user=request.user).order_by('-pk')
    for order in users_orders:
        order_history[order] = []
        for dish_order in DishOrder.objects.filter(order=order):
            order_history[order].append(dish_order.dish)

    context = {
        'form': form,
        'dishes': dishes,
        'order_history': order_history
    }
    return render(request, 'orderfood/index.html', context=context)


def report(request):
    dishes = {}
    report_data = {}
    total_sum = 0
    if request.POST:
        orders = Order.objects.filter(date__startswith=request.POST['date'])

        for order in orders:
            dish_orders = DishOrder.objects.filter(order=order)
            for dish_order in dish_orders:
                dish = Dish.objects.get(pk=dish_order.dish.pk)
                if str(dish.pk) in dishes:
                    dishes[str(dish.pk)] += 1
                else:
                    dishes[str(dish.pk)] = 1

        for key in dishes.keys():
            dish = Dish.objects.get(pk=key)
            report_data[key] = [dish.title, dishes[key], dish.price, dish.price * dishes[key]]
            print(report_data)
            total_sum += dish.price * dishes[key]

    print(dishes)
    context = {'report_data': report_data,
               'total_sum': total_sum}
    return render(request, 'orderfood/report.html', context=context)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'orderfood/register.html'
    success_url = reverse_lazy('auth')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'orderfood/auth.html'

    def get_success_url(self):
        return reverse_lazy('order')


def logout_user(request):
    logout(request)
    return redirect('auth')