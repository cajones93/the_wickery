from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .forms import EnquiryForm


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

    context = {
        'form': form,
        'on_enquiry_page': True
    }
    return render(request, 'enquiries/enquiry.html', context)
