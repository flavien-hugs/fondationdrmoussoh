"""fondation URL Configuration """
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500

from django.conf import settings
from django.conf.urls.static import static
from fondation import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about-us/', views.about_us, name='about_us'),
    path('dr-moussoh/', views.about_ceo, name='about_ceo'),
    path('gallerie/', views.gallerie, name='gallerie'),
    path('l-equipe/', views.team, name='team'),
    path('nos-formations/', views.formation, name='formation'),
    path('bibliotheque/', views.bibliotheque, name='bibliotheque'),

    path('erreur/', views.error404, name='erreur'),

    path('', include('drmoussoh.urls', namespace='drmoussoh')),
    path('admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'fondation.views.error404'
handler404 = 'fondation.views.error500'

