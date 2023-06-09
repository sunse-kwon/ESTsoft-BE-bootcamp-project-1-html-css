def genRef(data):
    result = dict()
    for i, bundle in enumerate(data):
        value = []
        key = f'bundle {i+1}'
        for id, lat, lng, time_spent, page_title, overview, image_path, address, opening_hour in bundle:
            item = dict()
            item["attraction number"] = id
            item["attraction name"] = page_title
            value.append(item)
        result[key] = value
    return result