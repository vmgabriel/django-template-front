"""Created Views of Accounts Application"""

# Libraries
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings

# Forms
from .forms import UserForm, RegisterForm

# Models
from .models import User

# Filters
from .filters import ProfileFilter

# Core
from core.views import FilteredListView


class SignUpView(LoginRequiredMixin, generic.CreateView):
    """Create View Sign Up of account"""
    form_class = RegisterForm
    success_url = reverse_lazy("accounts:users")
    template_name = "signup.html"


class UpdateProfileView(LoginRequiredMixin, generic.edit.UpdateView):
    """Update profile view."""
    template_name = "profiles/edit.html"
    success_url = reverse_lazy('accounts:profile-user')
    form_class = UserForm
    model = User

    def get_object(self):
        """Return user"""
        return self.request.user


class ListProfileView(LoginRequiredMixin, FilteredListView):
    template_name = "profiles/list.html"
    filterset_class = ProfileFilter
    model = User
    paginate_by = settings.DEFAULT_COUNT_PAGINATE


@login_required
def show_profile(request):
    template = "profiles/show.html"
    return render(
        request,
        template,
        context={"user_data": request.user, "me": True}
    )


@login_required
def block_user(request, username: str):
    user = get_object_or_404(User, username=username)
    user.blocked_at = datetime.now()
    user.save()
    return redirect("accounts:users")


@login_required
def unlock_user(request, username: str):
    user = get_object_or_404(User, username=username)
    user.blocked_at = None
    user.save()
    return redirect("accounts:users")


@login_required
def delete_user(request, username: str):
    user = get_object_or_404(User, username=username)
    user.inactive_at = datetime.now()
    user.save()
    return redirect("accounts:users")


class ShowProfileView(LoginRequiredMixin, generic.DetailView):
    template_name = "profiles/show.html"
    context_object_name  = "user_data"
    slug_field = "username"
    slug_url_kwarg = "username"

    model = User

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
