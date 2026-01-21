# core/views.py

from django.views.generic import TemplateView   # ← Add this line

from meta.views import Meta  

from django.shortcuts import render


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meta'] = Meta(
            title="TechSolutions – Android, Web, Data Science & Engineering Experts",
            description="Professional development services in Android apps, scalable web applications, data science, analysis, and data engineering. Build fast, scale to millions.",
            keywords=["android development", "web app development", "data science", "data analysis", "data engineering"],
            og_title="Build & Scale Your Projects with TechSolutions",
            og_description="Expert solutions in mobile, web, and data services.",
            # og_image="https://yourdomain.com/static/images/og-image.jpg",
            twitter_card="summary_large_image",
        )
        return context

