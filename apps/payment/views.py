from django.shortcuts import render, redirect, reverse
from django.views.generic import CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import PersonalForm, FinancialForm
from .models import UserPersonalModel, UserFinancialModel, UserOrder
from apps.cart.models import CartProduct


class PersonalView(LoginRequiredMixin, CreateView):
    form_class = PersonalForm
    template_name = "payment/personal.html"

    def form_valid(self, form):
        old_info_qs = UserPersonalModel.objects.filter(user=self.request.user)
        if old_info_qs.exists():
            old_info_qs.delete()
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(PersonalView, self).form_valid(form)

    def get_success_url(self):
        return reverse('payment:financial')


class FinancialView(LoginRequiredMixin, CreateView):
    form_class = FinancialForm
    template_name = "payment/financial.html"

    def form_valid(self, form):
        old_info_qs = UserFinancialModel.objects.filter(user=self.request.user)
        if old_info_qs.exists():
            old_info_qs.delete()
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(FinancialView, self).form_valid(form)

    def get_success_url(self):
        user_personal = UserPersonalModel.objects.filter(user=self.request.user)
        if user_personal.exists():
            return reverse('payment:confirmation')
        else:
            return reverse('payment:personal')


class ConfirmationView(LoginRequiredMixin, View):

    def get(self, request):
        template_name = "payment/confirmation.html"
        context = {}
        return render(request, template_name, context)


class CompletePaymentView(LoginRequiredMixin, View):

    def get(self, request):
        template_name = "payment/completed.html"
        context = {}
        personal_qs = UserPersonalModel.objects.filter(user=request.user)
        financial_qs = UserFinancialModel.objects.filter(user=request.user)
        if not personal_qs.exists():
            return reverse("payment:personal")
        if not financial_qs.exists():
            return reverse("payment:financial")
        cart_products = CartProduct.objects.filter(user=request.user)
        payment = 0
        for i in cart_products:
            payment += i.product.price
        order = UserOrder.objects.create(user=request.user, total_payment=payment)
        for i in cart_products:
            order.products.add(i.product)
        order.save()

        cart_products.delete()
        return render(request, template_name, context)
