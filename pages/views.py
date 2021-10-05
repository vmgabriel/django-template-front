"""Views of Page"""

# Libraries
from django.shortcuts import render

# Models
from accounts.models import User


def home_page(request):
    anonymous_template = "index.html"
    logged_template = "content.html"

    if not request.user.is_authenticated:
        return render(request, anonymous_template)

    users = User.objects.all()
    user_active = users.filter(inactive_at__isnull=True)
    user_blocked = users.filter(blocked_at__isnull=False)
    user_staff = user_active.filter(is_staff=True)

    print(user_blocked.count())

    ctx = {
        "users_all": users.count(),
        "users_active": user_active.count(),
        "users_blocked": user_blocked.count(),
        "users_staff": user_staff.count(),
        "users_normal": user_active.count() - (
            user_staff.count() + user_blocked.count()
        )
    }

    return render(request, logged_template, context=ctx)
