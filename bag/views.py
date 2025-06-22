from django.shortcuts import render, redirect


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    scent = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    if 'product_scent' in request.POST:
        scent = request.POST['product_scent']

    bag = request.session.get('bag', {})

    # List for size and scents 
    options = []
    if size:
        options.append(f'size_{size}')
    if scent:
        options.append(f'scent_{scent}')

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

    request.session['bag'] = bag
    return redirect(redirect_url)
