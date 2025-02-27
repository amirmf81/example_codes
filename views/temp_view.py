from django.http import JsonResponse
from myapp.models.user_model import User


def temp_func(request):
    user_id = request.POST.get("user_id")
    user = User.objects.get(id=user_id)
    print(user.username)
    user.phone_number = ''
    user.register_state = 1
    user.save()
    return JsonResponse({
        "ok": True,
    })
