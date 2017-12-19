# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
# from django.http import HttpResponseRedirect, HttpResponse


from app.forms import LenderForm


class LenderView(TemplateView):
    template_name = "lender.html"
    form_class = LenderForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        # if form.is_valid():
        #     form.save()
        return render(request, self.template_name, {'form': form})
