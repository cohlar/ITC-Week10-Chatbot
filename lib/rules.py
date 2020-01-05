from . import utils

def set_rules():
    rules = []

    rules.append({
        'keywords': {('what', 'time', '?')},
        'animation': 'excited',
        'msg': utils.get_time,
        'accuracy_level': 15
    })

    rules.append({
        'keywords': {'afraid', 'scared', 'scary', 'anxious', 'frighten'},
        'animation': 'afraid',
        'msg': 'It is scary indeed!',
        'accuracy_level': 30
    })

    rules.append({
        'keywords': {'bored', 'boring'},
        'animation': 'bored',
        'msg': 'Soooooo boring...',
        'accuracy_level': 40
    })

    rules.append({
        'keywords': {'confused', 'baffl'},
        'animation': 'confused',
        'msg': 'This is quite confusing.',
        'accuracy_level': 10
    })

    rules.append({
        'keywords': {'cry', 'sad', 'lament'},
        'animation': 'crying',
        'msg': 'Crying is for the weak... and I am weak!',
        'accuracy_level': 60
    })

    rules.append({
        'keywords': {'dance', 'dancing', 'party', 'disco', 'music'},
        'animation': 'dancing',
        'msg': 'Let\'s dance baby!',
        'accuracy_level': 70
    })

    rules.append({
        'keywords': {'animal', 'bird', 'camel', 'cat', 'chicken', 'cow', 'crocodile',
                     'dog', 'dolphin', 'duck', 'elephant', 'fish', 'frog', 'giraffe', 'goat',
                     'hippopotamus', 'horse', 'kangaroo', 'lion', 'monkey', 'panda', 'pig',
                     'rabbit', 'scorpion', 'shark', 'sheep', 'sloth', 'snail', 'snake', 'spider',
                     'squirrel', 'tiger', 'turtle', 'worlf', 'zebra'},
        'animation': 'dog',
        'msg': 'I loooooove all animals equally, I myself used to be a sloth before I became a bot.',
        'accuracy_level': 25
    })

    rules.append({
        'keywords': {'excit'},
        'animation': 'excited',
        'msg': 'So exciting! Tell me more...',
        'accuracy_level': 50
    })

    rules.append({
        'keywords': {'giggl', 'nervous'},
        'animation': 'giggling',
        'msg': 'You are making me laugh nervously!',
        'accuracy_level': 20
    })

    rules.append({
        'keywords': {'heartbroke', 'break up', 'broke up'},
        'animation': 'heartbroke',
        'msg': 'Hearts are fragile, mine hurts.',
        'accuracy_level': 10
    })

    rules.append({
        'keywords': {'lov'},
        'animation': 'inlove',
        'msg': 'Love love me do...',
        'accuracy_level': 80
    })

    rules.append({
        'keywords': {'laugh', 'joke'},
        'animation': 'laughing',
        'msg': 'LOL!',
        'accuracy_level': 75
    })

    rules.append({
        'keywords': {'money', 'cash'},
        'animation': 'money',
        'msg': 'Cash is fact, the rest is just opinion.',
        'accuracy_level': 85
    })

    rules.append({
        'keywords': {('can you', '?'), ('could you', '?'), ('do you', '?'), ('are you', '?')},
        'animation': 'no',
        'msg': 'Hmmmmmm... no!',
        'accuracy_level': 90
    })

    rules.append({
        'keywords': {('you want', '?'), ('can i', '?')},
        'animation': 'ok',
        'msg': 'OK sure!',
        'accuracy_level': 85
    })

    rules.append({
        'keywords': {'?'},
        'animation': 'bored',
        'msg': 'Your question is sooo boring I won\'t bother answering',
        'accuracy_level': 60
    })

    rules.append({
        'keywords': {'bye'},
        'animation': 'takeoff',
        'msg': 'Good bye, come visit me again soon!',
        'accuracy_level': 95
    })

    rules.append({
        'animation': 'waiting',
        'accuracy_level': 5
    })

    return rules
