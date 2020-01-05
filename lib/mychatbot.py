from . import utils, rules

DEFAULT_ANIMATION = 'confused'
DEFAULT_MSG = '''Sorry, not sure what to say. I'm not that smart: please try to rephrase. Please note that I speak only English at the moment'''

SWEAR_ANIMATION = 'heartbroke'
SWEAR_MESSAGE = 'This is not an appropriate language, please watch your tongue!'

rules = rules.set_rules()
swears = utils.get_swears()

def process_user_message(message):

    user_message = message.lower()

    response = utils.set_response(DEFAULT_ANIMATION, DEFAULT_MSG)
    print('current_time')

    for swear in swears:
        if swear in user_message:
            utils.set_response(SWEAR_ANIMATION, SWEAR_MESSAGE, response)
            return response

    for rule in sorted(rules, key=utils.get_accuracy_level):
        if 'keywords' not in rule or 'msg' not in rule:
            continue
        for keyword in rule['keywords']:
            all_keywords_in_user_message = all(
                word in user_message for word in keyword)
            if (
                type(keyword) is tuple and all_keywords_in_user_message
                or
                type(keyword) is str and keyword in user_message
            ):
                animation = rule['animation']
                msg = rule['msg']() if type(
                    rule['msg']()) is 'function' else rule['msg']()
                utils.set_response(animation, msg, response)
                return response

    return response
