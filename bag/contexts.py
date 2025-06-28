from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, WaxType, Scent, CandleSize


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():

        product = get_object_or_404(Product, pk=item_id)


        for options_key, quantity in item_data['items_by_options'].items():
            if quantity > 0:

                # Get the size, scent, and wax from the options_key
                size = None
                scent = None
                wax = None
                size_multiplier = Decimal('1.00') 
                wax_multiplier = Decimal('1.00')
                
                if options_key != 'no_options':
                    parts = options_key.split('_')
                    for i in range(len(parts)):
                        if parts[i] == 'size' and i + 1 < len(parts):
                            size_pk = parts[i+1]
                            size_obj = get_object_or_404(CandleSize, pk=size_pk)
                            size_multiplier = size_obj.price_modifier or 1.0
                        elif parts[i] == 'wax' and i + 1 < len(parts):
                            wax_pk = parts[i+1]
                            wax_obj = get_object_or_404(WaxType, pk=wax_pk)
                            wax_multiplier = wax_obj.price_modifier or 1.0
                
                line_subtotal = product.price * size_multiplier * wax_multiplier
                    
                total += quantity * line_subtotal
                product_count += quantity
                
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                    'scent': scent,
                    'wax': wax,
                    'line_subtotal': line_subtotal,
                    'lineitem_total': line_subtotal * quantity,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
