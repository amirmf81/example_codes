from django.http import JsonResponse

from myapp.models.company_model import Company


def delete_company_func(request):
    company_id = request.POST.get("id")
    Company.delete_comp(comp_id=company_id)
    return JsonResponse({
        "ok": True,
    })
