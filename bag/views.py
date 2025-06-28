from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product, WaxType, Scent, CandleSize


def view_bag(request):
    """
    A view that renders the bag contents page.
    It processes the session bag to retrieve full product and option details.
    """
    bag = request.session.get('bag', {})
    bag_items = []
    total = 0
    product_count = 0

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)

        if 'items_by_options' in item_data and isinstance(item_data['items_by_options'], dict):
            for options_key, quantity in item_data['items_by_options'].items():
                
                size = None
                scent = None
                wax = None
                wax_modifier = 0
                size_modifier = 0

                # Parse options_key to get the chosen options' PKs
                option_parts = options_key.split('_')
                
                # Loop through parts, expecting format like 'size_1', 'scent_2', 'wax_3'
                for i in range(len(option_parts)):
                    if option_parts[i] == 'size' and i + 1 < len(option_parts):
                        # Get pk from options
                        size_pk = option_parts[i+1] # This is now the PK
                        size = CandleSize.objects.get(pk=size_pk)
                        size_modifier = size.price_modifier or 0
                    elif option_parts[i] == 'scent' and i + 1 < len(option_parts):
                        scent_pk = option_parts[i+1] # This is now the PK
                        scent = Scent.objects.get(pk=scent_pk)
                    elif option_parts[i] == 'wax' and i + 1 < len(option_parts):
                        wax_pk = option_parts[i+1] # This is now the PK
                        wax = WaxType.objects.get(pk=wax_pk)
                        wax_modifier = wax.price_modifier or 0

                # Calculate line item total with modifiers
                lineitem_total = (product.price + wax_modifier + size_modifier) * quantity
                total += lineitem_total
                product_count += quantity

                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                    'scent': scent,
                    'wax': wax,
                    'options_key': options_key,
                    'lineitem_total': lineitem_total,
                })

    # Prepare context for template
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
    }

    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    
    size = None
    if 'product_size' in request.POST:
        size = get_object_or_404(CandleSize, pk=request.POST['product_size'])
        size_pk = size.pk

    scent = None
    if 'product_scent' in request.POST:
        scent = get_object_or_404(Scent, pk=request.POST['product_scent'])
        scent_pk = scent.pk
        
    wax = None
    if 'product_wax' in request.POST:
        wax = get_object_or_404(WaxType, pk=request.POST['product_wax'])
        wax_pk = wax.pk

    bag = request.session.get('bag', {})

    message_parts = [f'"{product.name}"']
    
    # List for size and scents 
    options = []
    if size:
        options.append(f'size_{size_pk}')
        message_parts.append(f'Size: {size.friendly_name}')

    if scent:
        options.append(f'scent_{scent_pk}')
        message_parts.append(f'Scent: {scent.friendly_name}')
        
    if wax and wax != "None":
        options.append(f'wax_{wax_pk}')
        message_parts.append(f'Wax: {wax.friendly_name}')

    message_string = " | ".join(message_parts)
    
    # If no size or scent
    if not options:
        options_key = 'no_options'
    else:
        # create string to track options
        options_key = '_'.join(options)

    # Add new item to bag and initialise to dictionary
    if item_id not in bag:
        bag[item_id] = {'items_by_options': {}}

    # Add or update the quantity for the specific option_key
    if options_key in bag[item_id]['items_by_options']:
        bag[item_id]['items_by_options'][options_key] += quantity
        messages.success(request, f'Added "{message_string}" to your bag')
    else:
        bag[item_id]['items_by_options'][options_key] = quantity
        messages.success(request, f'Added "{message_string}" to your bag')

    print(options_key)
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Adjust the quantity of the specified product (and its options) to the new amount.
    """
    
    product = get_object_or_404(Product, pk=item_id)
    
    quantity = int(request.POST.get('quantity'))

    size = None
    if 'product_size' in request.POST:
        size = get_object_or_404(CandleSize, pk=request.POST['product_size'])
        size_pk = size.pk

    scent = None
    if 'product_scent' in request.POST:
        scent = get_object_or_404(Scent, pk=request.POST['product_scent'])
        scent_pk = scent.pk
        
    wax = None
    if 'product_wax' in request.POST:
        wax = get_object_or_404(WaxType, pk=request.POST['product_wax'])
        wax_pk = wax.pk

    bag = request.session.get('bag', {})

    message_parts = [f'"{product.name}"']
    
    # List for size and scents 
    options = []
    if size:
        options.append(f'size_{size.pk}')
        message_parts.append(f'Size: {size.friendly_name}')

    if scent:
        options.append(f'scent_{scent.pk}')
        message_parts.append(f'Scent: {scent.friendly_name}')
        
    if wax and wax != "None":
        options.append(f'wax_{wax.pk}')
        message_parts.append(f'Wax: {wax.friendly_name}')

    message_string = " | ".join(message_parts)

    if not options:
        options_key = 'no_options'
    else:
        options_key = '_'.join(options)

    if item_id in bag and isinstance(bag[item_id], dict) and 'items_by_options' in bag[item_id]:
        if options_key in bag[item_id]['items_by_options']:
            if quantity > 0:
                bag[item_id]['items_by_options'][options_key] = quantity
                messages.success(request, f'Updated "{message_string}" quantity to {quantity}')
            else:
                # Remove from the bag if quantity is 0 or less
                del bag[item_id]['items_by_options'][options_key]
                messages.success(request, f'Removed "{message_string}" from your bag')

                # ----------------------------------------------
                # If no more options for this item_id, remove the item_id itself ----- DONT THINK NECESSARY
                # if not bag[item_id]['items_by_options']:
                #     bag.pop(item_id)
                #     if size and size != "None":
                #         messages.success(request, f'Updated size {size.upper()} {product.name} made from {wax} with scent: {scent} to your bag')
                #     else:
                #         messages.success(request, f'Updated {product.name} made from {wax} with scent: {scent} to your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
    Remove the specified product (and its options) from the bag.
    """

    product = get_object_or_404(Product, pk=item_id)

    try:
        size = None
        if 'product_size' in request.POST:
            size = get_object_or_404(CandleSize, pk=request.POST['product_size'])
            size_pk = size.pk

        scent = None
        if 'product_scent' in request.POST:
            scent = get_object_or_404(Scent, pk=request.POST['product_scent'])
            scent_pk = scent.pk
            
        wax = None
        if 'product_wax' in request.POST:
            wax = get_object_or_404(WaxType, pk=request.POST['product_wax'])
            wax_pk = wax.pk

        bag = request.session.get('bag', {})

        message_parts = [f'"{product.name}"']

        # List for size and scents 
        options = []
        if size and size != "None":
            options.append(f'size_{size.pk}')
            message_parts.append(f'Size: {size.friendly_name}')

        if scent:
            options.append(f'scent_{scent.pk}')
            message_parts.append(f'Scent: {scent.friendly_name}')

        if wax and wax != "None":
            options.append(f'wax_{wax.pk}')
            message_parts.append(f'Wax: {wax.friendly_name}')

        message_string = " | ".join(message_parts)

        if not options:
            options_key = 'no_options'
        else:
            options_key = '_'.join(options)
        
        print(f'Delete options: {options_key}')

        if options_key == 'no_options':
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')
        else:
            del bag[item_id]['items_by_options'][options_key]
            messages.success(request, f'Removed "{message_string}" from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:

        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
