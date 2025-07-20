from django.urls import path
from .views import MemberApplicationView, HomePageView, AdminDashboardView, toggle_approval
from django.views.generic import TemplateView
from .views import CustomLoginView, MemberDashboardView

urlpatterns = [
path('', HomePageView.as_view(), name='home'),
    path('apply/', MemberApplicationView.as_view(), name='apply'),
    path('apply/success/', TemplateView.as_view(
        template_name="core/application_success.html"
    ), name='application_success'),
]


urlpatterns += [
    path('admin-dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('dashboard/approve/<int:user_id>/', toggle_approval, name='toggle_approval'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('member-dashboard/', MemberDashboardView.as_view(), name='member_dashboard'),
]

