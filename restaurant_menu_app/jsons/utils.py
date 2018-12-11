def prep_menu(menu):
    items = []
    for item in menu:
        items.append({'name': item.name,
                      'course': item.course,
                      'price': item.price,
                      'description': item.description,
                      'id': item.id})
    return items


def prep_restaurants(restaurants):
    data = []
    for restaurant in restaurants:
        data.append({'name': restaurant.name,
                     'id': restaurant.id})
    return data


def prep_restaurant(restaurant):
    data = {'name': restaurant.name,
            'id': restaurant.id}
    return data


def prep_item(item):
    data = {'name': item.name,
            'course': item.course,
            'price': item.price,
            'description': item.description,
            'id': item.id}
    return data
