from . import utils, rules

default_animation = 'confused'
default_msg = '''Sorry, not sure what to say. I'm not that smart: please try to rephrase. Please note that I speak only English at the moment'''

swear_animation = 'heartbroke'
swear_message = 'This is not an appropriate language, please watch your tongue!'

rules = rules.set_rules()
swears = utils.get_swears()    

def process_user_message(message):

    user_message = message.lower()

    response = utils.set_response(default_animation, default_msg)

    for swear in swears:
        if swear in user_message:
            utils.set_response(swear_animation, swear_message, response)
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
                msg = rule['msg']() if callable(rule['msg']) else rule['msg']
                utils.set_response(animation, msg, response)
                return response

    return response
