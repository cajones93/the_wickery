from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .forms import EnquiryForm
from profiles.models import UserProfile # Make sure this import is correct and UserProfile is defined

def enquiry(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            message = form.save()
            messages.success(request, 'Your message has been sent successfully!\n'
                                      'We will get back to you shortly.')
            return redirect(reverse('enquiry'))
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = EnquiryForm()

        # If user is logged in, autofill name and email
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                form = EnquiryForm(initial={
                    'name': profile.user.get_full_name(),
                    'email': profile.user.email,
                })
            except UserProfile.DoesNotExist:
                form = EnquiryForm()

    context = {
        'form': form,
        'on_enquiry_page': True
    }
    return render(request, 'enquiries/enquiry.html', context)