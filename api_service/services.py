from django.template.defaultfilters import lower


def checking_the_string(message):
    if 'абракадабра' in lower(message):
        return True
    else:
        return False
