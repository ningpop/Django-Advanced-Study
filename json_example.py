import json

diary = {
    'id': 3,
    'title': 'I\'m starving..',
    'body': 'On nana On na On nanana deal car',
}

print(diary)
print(type(diary))

diary_s = json.dumps(diary)     # dumps : dictionary --> json

print(diary_s)
print(type(diary_s))

diary_back = json.loads(diary_s)    # loads : json --> dictionary

print(diary_back)
print(type(diary_back))