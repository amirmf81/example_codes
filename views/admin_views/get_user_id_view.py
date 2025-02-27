from django.http import JsonResponse, HttpResponse

from myapp.models.user_model import User


def get_user_id_view_func(request):
    #user_id = request.GET.get("user_id")
    #user = User.objects.get(id=user_id).username
    #print(user)
    return HttpResponse({
        "Hi"
    })
