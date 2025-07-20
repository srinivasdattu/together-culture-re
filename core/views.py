from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import MemberApplicationForm
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import User
from .utils import generate_password_reset_link
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect


class MemberApplicationView(CreateView):
    model = User
    form_class = MemberApplicationForm
    template_name = "core/apply.html"
    success_url = reverse_lazy("application_success")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.username = user.email
        user.set_unusable_password()
        user.is_active = True
        user.save()
        form.save_m2m()
        return super().form_valid(form)


class HomePageView(TemplateView):
    template_name = "core/home.html"


class AdminDashboardView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = User
    template_name = "core/admin_dashboard.html"
    context_object_name = "members"

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

    def get_queryset(self):
        queryset = User.objects.exclude(is_superuser=True)
        q = self.request.GET.get("q")
        status = self.request.GET.get("status")

        if q:
            queryset = queryset.filter(email__icontains=q)

        if status == "approved":
            queryset = queryset.filter(is_approved=True)
        elif status == "pending":
            queryset = queryset.filter(is_approved=False)

        return queryset.order_by("-date_joined")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["member_json"] = [
            {
                "id": member.id,
                "first_name": member.first_name,
                "last_name": member.last_name,
                "email": member.email,
                "phone": member.phone,
                "location": member.location,
                "interests": [i.name for i in member.interests.all()],
                "professional_background": member.professional_background,
                "why_join": member.why_join,
                "how_contribute": member.how_contribute,
                "is_approved": member.is_approved,
                "date_joined": member.date_joined.strftime("%Y-%m-%d %H:%M:%S"),
            }
            for member in context["members"]
        ]
        return context


User = get_user_model()

@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def toggle_approval(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_approved = not user.is_approved
    user.save()
    return redirect('admin_dashboard')


@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def toggle_approval(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_approved = not user.is_approved
    user.save()

    if user.is_approved:
        reset_link = generate_password_reset_link(user, request)
        print(f"[EMAIL SIMULATION] Send this link to user {user.email} to set password:\n{reset_link}")

    return redirect('admin_dashboard')


class CustomLoginView(LoginView):
    def get_success_url(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return '/admin-dashboard/'
        elif user.is_approved:
            return '/member-dashboard/'
        else:
            # Optionally: log out the unapproved user immediately
            from django.contrib.auth import logout
            logout(self.request)
            return '/accounts/login/?unapproved=1'


class MemberDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'core/member_dashboard.html'


