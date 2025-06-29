from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product, CandleSize, WaxType, Scent
from bag.contexts import bag_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    
                    if isinstance(item_data, dict) and 'items_by_options' in item_data:    
                        for options_key, quantity in item_data['items_by_options'].items():
                            
                            selected_size_obj = None
                            selected_scent_obj = None
                            selected_wax_type_obj = None
                            wax_multiplier = None
                            size_multiplier = None

                            
                            if options_key != 'no_options':
                                parts = options_key.split('_')
                                
                                for i in range(len(parts)):
                                    if parts[i] == 'size' and i + 1 < len(parts):
                                        size_pk = parts[i+1]
                                        selected_size_obj = get_object_or_404(CandleSize, pk=size_pk)
                                        size_multiplier = selected_size_obj.price_modifier or 1.00
                                    elif parts[i] == 'scent' and i + 1 < len(parts):
                                        scent_pk = parts[i+1]
                                        selected_scent_obj = get_object_or_404(Scent, pk=scent_pk)
                                    elif parts[i] == 'wax' and i + 1 < len(parts):
                                        wax_pk = parts[i+1]
                                        selected_wax_type_obj = get_object_or_404(WaxType, pk=wax_pk)
                                        wax_multiplier = selected_wax_type_obj.price_modifier or 1.00
                                                                    
                            lineitem_subtotal = product.price * size_multiplier * wax_multiplier
                            
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                selected_size=selected_size_obj,
                                selected_scent=selected_scent_obj,
                                selected_wax_type=selected_wax_type_obj,
                                lineitem_subtotal=lineitem_subtotal,
                                
                            )
                            
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))
        
        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        
        order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')

        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)



def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')
    
    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)