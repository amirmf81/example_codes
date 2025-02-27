"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp.views.admin_views.get_user_id_view import get_user_id_view_func
from myapp.views.check_city_view import check_city_view_func
from myapp.views.company_view.delete_company import delete_company_func
from myapp.views.get_location_view import get_location_view_func
from myapp.views.get_reports_view.daily_report_view import daily_report_view_func
from myapp.views.get_reports_view.monthly_report_view import monthly_report_view_func
from myapp.views.get_reports_view.report_view import report_view_func
from myapp.views.get_reports_view.weekly_report_view import weekly_report_view_func
from myapp.views.get_scale_view import get_scale_view_func
from myapp.views.user_view.get_state_view import get_state_view_func
from myapp.views.register_view.first_view import first_view_func
from myapp.views.login_view import login_view_func
from myapp.views.temp_view import temp_func
from myapp.views.user_view.update_user_view import update_view
from myapp.views.register_view.complete_register_view import complete_register_view_func
from myapp.views.user_view.del_user_view import del_user_view_func
from myapp.views.register_view.validate_otp_view import validate_otp_func


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view_func),
    path('register/', first_view_func),
    path('change_password/', update_view),
    path('complete_register/', complete_register_view_func),
    path('del_user/', del_user_view_func),
    path('get_state', get_state_view_func),
    path('validate_otp', validate_otp_func),
    path('temp', temp_func),
    path('delete_company', delete_company_func),
    path('get_location', get_location_view_func),
    path('get_scale', get_scale_view_func),
    path('get_report', report_view_func),
    path('check_city', check_city_view_func),
    path('get_daily_report', daily_report_view_func),
    path('get_monthly_report', monthly_report_view_func),
    path('get_weekly_report', weekly_report_view_func),


]
