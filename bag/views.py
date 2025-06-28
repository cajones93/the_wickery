from django.shortcuts import render, redirect, reverse, HttpResponse


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    scent = None
    if 'product_scent' in request.POST:
        scent = request.POST['product_scent']
        
    wax = None
    if 'product_wax' in request.POST:
        wax = request.POST['product_wax']

    bag = request.session.get('bag', {})

    # List for size and scents 
    options = []
    if size:
        options.append(f'size_{size}')

    if scent:
        options.append(f'scent_{scent}')
        
    if wax and wax != "None":
        options.append(f'wax_{wax}')

    # If no size or scent
    if not options:
        options_key = 'no_options'
    else:
        # create string to track options
        options_key = '_'.join(options)

    if item_id not in bag or not isinstance(bag[item_id], dict) or 'items_by_options' not in bag[item_id]:
        bag[item_id] = {'items_by_options': {}}

    # Now, add or update the quantity for the specific option_key
    if options_key in bag[item_id]['items_by_options']:
        bag[item_id]['items_by_options'][options_key] += quantity
    else:
        bag[item_id]['items_by_options'][options_key] = quantity

    print(f'Options added: {options_key}')
    request.session['bag'] = bag
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """
    Adjust the quantity of the specified product (and its options) to the new amount.
    """
    quantity = int(request.POST.get('quantity'))

    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    scent = None
    if 'product_scent' in request.POST:
        scent = request.POST['product_scent']
        
    wax = None
    if 'product_wax' in request.POST:
        wax = request.POST['product_wax']

    bag = request.session.get('bag', {})

    # Construct the unique option key based on size and scent
    options = []
    if size and size != "None":
        options.append(f'size_{size}')
    if scent and scent != "None":
        options.append(f'scent_{scent}')
    if wax and wax != "None":
        options.append(f'wax_{wax}')

    if not options:
        options_key = 'no_options'
    else:
        options_key = '_'.join(options)

    if item_id in bag and isinstance(bag[item_id], dict) and 'items_by_options' in bag[item_id]:
        if options_key in bag[item_id]['items_by_options']:
            if quantity > 0:
                bag[item_id]['items_by_options'][options_key] = quantity
            else:
                # Remove from the bag if quantity is 0 or less
                del bag[item_id]['items_by_options'][options_key]
                # If no more options for this item_id, remove the item_id itself
                if not bag[item_id]['items_by_options']:
                    bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
    Remove the specified product (and its options) from the bag.
    """
    
    size = request.POST.get('size')
    scent = request.POST.get('scent')
    wax = request.POST.get('wax')

    bag = request.session.get('bag', {})

    options = []
    if size and size != "None":
        options.append(f'size_{size}')
    if scent and scent != "None":
        options.append(f'scent_{scent}')
    if wax:
        options.append(f'wax_{wax}')

    if not options:
        options_key = 'no_options'
    else:
        options_key = '_'.join(options)

    if options_key == 'no_options':
        bag.pop(item_id)
    else:
        del bag[item_id]['items_by_options'][options_key]

    request.session['bag'] = bag
    return HttpResponse(status=200)
