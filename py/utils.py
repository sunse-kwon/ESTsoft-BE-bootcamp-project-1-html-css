# ChatGPT의 input으로 넣기 위해 번들화 된 리스트형태의 데이터셋을 딕셔너리 형태로 바꿔주는 함수 
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