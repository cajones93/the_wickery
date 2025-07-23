from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def privacy_policy_view(request):
    """
    A simple view to render the privacy policy page.
    """
    return render(request, 'home/privacy_policy.html')
