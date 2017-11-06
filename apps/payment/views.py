from django.shortcuts import render, redirect, reverse
from django.views.generic import CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import PersonalForm, FinancialForm
from .models import UserPersonalModel


class PersonalView(LoginRequiredMixin, CreateView):
    form_class = PersonalForm
    template_name = "payment/personal.html"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(PersonalView, self).form_valid(form)

    def get_success_url(self):
        return reverse('payment:financial')


class FinancialView(LoginRequiredMixin, CreateView):
    form_class = FinancialForm
    template_name = "payment/financial.html"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(FinancialView, self).form_valid(form)

    def get_success_url(self):
        user_personal = UserPersonalModel.objects.filter(user=self.request.user)
        if user_personal.exists():
            return reverse('landing')
        else:
            return reverse('payment:personal')
