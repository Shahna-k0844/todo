from django.urls import include, path

from . import views

urlpatterns = [
    path('',views.homefunction,name='home'),
    path('show',views.showfunction,name='show'),
    path('remove<int:id>',views.removefunction,name='remove'),
    path('edit<int:id>',views.editfunction,name='edit'),
    # path('edit<int:id>',views.editfunction2,name='editted'),
    path('signup',views.signfunction,name='sign'),
    path('login',views.loginfunction,name='login'),
]
