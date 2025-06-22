from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():

        product = get_object_or_404(Product, pk=item_id)

        # Ensure item_data is always a dictionary with 'items_by_options'
        # This handles legacy bag structures or ensures consistency
        if isinstance(item_data, int):
            # Convert old format (simple quantity) to new format (no options)
            item_data = {'items_by_options': {'no_options': item_data}}
        elif 'items_by_size' in item_data:  # Handle old 'items_by_size' format
            new_items_by_options = {}
            for size, qty in item_data['items_by_size'].items():
                new_items_by_options[f'size_{size}'] = qty
            item_data = {'items_by_options': new_items_by_options}
        elif 'items_by_options' not in item_data:
            # If it's a dictionary but doesn't have the expected key,
            # this might be an error or another old format.
            # For now, let's assume it should have 'no_options' if no other options are present.
            # You might want to log this or raise an error in a real application.
            item_data['items_by_options'] = {'no_options': 0}  # Or handle based on context

        for option_key, quantity in item_data['items_by_options'].items():
            if quantity > 0: # Only process if quantity is positive
                total += quantity * product.price
                product_count += quantity

                # Parse the option_key to extract size and scent
                size = None
                scent = None
                if option_key != 'no_options':
                    parts = option_key.split('_')
                    for i in range(len(parts)):
                        if parts[i] == 'size' and i + 1 < len(parts):
                            size = parts[i+1]
                        elif parts[i] == 'scent' and i + 1 < len(parts):
                            scent = parts[i+1]

                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                    'scent': scent,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
