from django.urls import path
from django.utils.translation import gettext_lazy as _
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path(_('about/'), views.about, name='about'),
    path(_('services/'), views.services, name='services'),
    path(_('results/'), views.results, name='results'),
    path(_('blog/'), views.blog_list, name='blog_list'),
    path(_('blog/') + '<slug:slug>/', views.blog_detail, name='blog_detail'),
    path(_('contact/'), views.contact, name='contact'),
    path(_('contact/') + 'submit/', views.contact_submit, name='contact_submit'),
    path(_('legal/privacy/'), views.legal_privacy, name='legal_privacy'),
    path(_('legal/terms/'), views.legal_terms, name='legal_terms'),
    path(_('legal/cookies/'), views.legal_cookies, name='legal_cookies'),
]
