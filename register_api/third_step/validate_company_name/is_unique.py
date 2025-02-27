from myapp.models.company_model import Company


def is_unique_func(name):
    try:
        Company.objects.get(name=name)
        return False

    except:
        return True
