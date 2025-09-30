from django.contrib.auth.decorators import user_passes_test

def _in_support(user):
    return user.is_authenticated and (user.is_superuser or user.groups.filter(name="Suporte").exists())

support_required = user_passes_test(_in_support, login_url="login")
