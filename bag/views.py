from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product, WaxType, Scent, CandleSize

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    
    size = None
    if 'product_size' in request.POST:
        size = get_object_or_404(CandleSize, pk=request.POST['product_size'])

    scent = None
    if 'product_scent' in request.POST:
        scent = get_object_or_404(Scent, pk=request.POST['product_scent'])
        
    wax = None
    if 'product_wax' in request.POST:
        wax = get_object_or_404(WaxType, pk=request.POST['product_wax'])

    bag = request.session.get('bag', {})

    message_parts = [f'{product.name}']
    
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

    scent = None
    if 'product_scent' in request.POST:
        scent = get_object_or_404(Scent, pk=request.POST['product_scent'])

    wax = None
    if 'product_wax' in request.POST:
        wax = get_object_or_404(WaxType, pk=request.POST['product_wax'])

    bag = request.session.get('bag', {})

    message_parts = [f'{product.name}']

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

    print(f'options_key: {options_key}')
    if item_id in bag and isinstance(bag[item_id], dict) and 'items_by_options' in bag[item_id]:
        if options_key in bag[item_id]['items_by_options']:
            if quantity > 0:
                bag[item_id]['items_by_options'][options_key] = quantity
                messages.success(request, f'Updated "{message_string}" quantity to {quantity}')
            else:
                # Remove from the bag if quantity is 0 or less
                del bag[item_id]['items_by_options'][options_key]
                messages.success(request, f'Removed "{message_string}" from your bag')

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

        scent = None
        if 'product_scent' in request.POST:
            scent = get_object_or_404(Scent, pk=request.POST['product_scent'])
            
        wax = None
        if 'product_wax' in request.POST:
            wax = get_object_or_404(WaxType, pk=request.POST['product_wax'])

        bag = request.session.get('bag', {})

        message_parts = [f'{product.name}']

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
