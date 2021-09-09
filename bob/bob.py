"""Bob"""

def response(hey_bob):
    """
    :param hey_bob: string
    :return: string - Bob's response
    """
    hey_bob = hey_bob.strip()
    if hey_bob.isupper() and hey_bob.endswith('?'):
        response = 'Calm down, I know what I\'m doing!'
    elif hey_bob.isupper():
        response = 'Whoa, chill out!'
    elif hey_bob.endswith('?'):
        response = 'Sure.'
    elif hey_bob.isspace() or not hey_bob:
        response = 'Fine. Be that way!'
    else:
        response = 'Whatever.'

    return response
