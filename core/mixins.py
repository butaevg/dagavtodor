from django.contrib.auth.decorators import login_required 
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseRedirect

class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)