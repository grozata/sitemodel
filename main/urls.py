from django.urls import path

from .views import other_page
from .views import index
from .views import SiteModelLoginView
from .views import profile
from .views import SiteModelLogoutView
from .views import ChangeUserInfoView

app_name = 'main'
urlpatterns = [ 
	path('<str:page>/', other_page, name='other'),
	path('', index, name='index'),
	path('accounts/login/', SiteModelLoginView.as_view(), name='login'),
	path('accounts/profile/', profile, name='profile'),
	path('accounts/logout/', SiteModelLogoutView.as_view(), name='logout'),
	path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
]