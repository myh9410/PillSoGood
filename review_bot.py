import requests
import json
import random
from time import sleep

keys = ['8d17f5ec47b2bc2eeae5a8fb6805c8e741130514',
        'b868ab76af5f6077b41771a4d66cb2fcea6a20d4',
        '80daa51b16cf2ba3a464ea9c0e57817d500c93d7',
        '31cf2b1397b8c7dccd21ab19d5abba923a445ea2',
        'f8ab0970b498b0775e72e284e00255a204d2178e',
        '5e7a76868c85cda66a8a1e5df14f9e696fc412e0',
        '22f3abf6eba07761f8411f14b63721c7ff49dd1c',
        '47e4df12cca7b54dbcae23def68552356a754c7f',
        'f79ee3becf5992e2e1f09518fc03399d667d349d',
        ]

titles = [
    '굿굿',
    '흐음...',
    '좋습니다.',
    '조금 애매...',
    '진짜 좋아요',
]

contents = [
    '이거 먹고 날아다녀요!',
    '그저 그런듯...',
    '직접 약국에 가서 처방받은 것같은 느낌을 받았습니다. 좋아요!!',
    '머리가 너무 빠져서 꾸준히 먹고 있어요^^지금 두달째 되었는데 조금 더 먹어봐야 알겠지만 머리가 조금 굵어지는듯해요!!',
    '딱 두달분먹었고 머리는 아직은 잘 모르겠구요. 손톱은 단단해졌어요.  꾸준히 먹어보려구요',
    '전부 만족합니다~',
    '재구매 해서 먹고 있어요!',
    '항상 먹던거라 주문했어요~~',
    '이거드시고 괜찮아서 세통째구입중입니다~~~'
]
while True:
    key_idx = random.randint(0, 8)
    title_idx = random.randint(0, 4)
    content_idx = random.randint(0, 6)
    rank = random.randint(1, 5)
    item_id = random.randint(1, 29051)
    print(key_idx, title_idx, content_idx, rank)

    header = 'token ' + keys[key_idx]
    headers = {
        'Authorization': header
    }
    data = {
        'title': titles[title_idx],
        'content': contents[content_idx],
        'rank': rank
    }

    url = 'http://j3a506.p.ssafy.io:8000/reviews/' + str(item_id) + '/'

    response = requests.post(url, data=data, headers=headers)
    sleep(1)
