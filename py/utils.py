# convert bundled datset to json style dictionary to be used as an input for chatGPT. 
def genRef(data):
    result = dict()
    for i, bundle in enumerate(data):
        value = []
        key = f'bundle {i+1}'
        for id, _, _, _, page_title, _, _, _, _ in bundle:
            item = dict()
            item["attraction number"] = id
            item["attraction name"] = page_title
            value.append(item)
        result[key] = value
    return result