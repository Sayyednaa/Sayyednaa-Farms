def cart_count(request):
    """
    Context processor to provide the total number of items in the cart to all templates.
    """
    count = 0
    if 'cart' in request.session:
        cart = request.session.get('cart', {})
        for qty in cart.values():
            count += qty
    return {'cart_count': count}
