from django.shortcuts import render

from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import AdvUser
from .forms import ChangeUserInfoForm

class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
	model = AdvUser
	template_name = 'main/change_user_info.html'
	form_class = ChangeUserInfoForm
	success_url = reverse_lazy('main:profile')
	success_message = 'You info changed'

	def dispatch(self, request, *args, **kwargs):
		self.user_id = request.user.pk 
		return super().dispatch(request, *args, **kwargs)

	def get_object(self, queryset = None):
		if not queryset:
			queryset = self.get_queryset()
		return get_object_or_404(queryset, pk=self.user_id)


class SiteModelLogoutView(LoginRequiredMixin, LogoutView):
	template_name = 'main/logout.html'


@login_required
def profile(request):
	return render(request, 'main/profile.html')

class SiteModelLoginView(LoginView):
	template_name = 'main/login.html'


def other_page(request, page):
	try:
		template = get_template('main/' + page + '.html')
	except TemplateDoesNotExist:
		raise Http404
	return HttpResponse(template.render(request=request))

def index(request):
	return render(request, 'main/index.html')
