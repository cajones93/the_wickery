from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .forms import EnquiryForm
from .models import Enquiry
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
        initial_data = {}

        # Check for message type and order number in URL
        if 'message_type' in request.GET and request.GET['message_type'] in [choice[0] for choice in Enquiry.MESSAGE_TYPES]:
            initial_data['message_type'] = request.GET['message_type']

        if 'order_number' in request.GET:
            initial_data['order_number'] = request.GET['order_number']

        # If user is logged in, autofill name and email
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                initial_data['name'] = profile.user.get_full_name()
                initial_data['email'] = profile.user.email
            except UserProfile.DoesNotExist:
                pass

        form = EnquiryForm(initial=initial_data)

    context = {
        'form': form,
        'on_enquiry_page': True
    }
    return render(request, 'enquiries/enquiry.html', context)
