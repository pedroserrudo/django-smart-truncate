__author__ = 'pedroserrudo'
from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()

@register.filter
@stringfilter
def smartcut(value, arg):
    """
	
    usage: description|smartcut:"20:30"

    'this is a string text that will become smart truncated'|smartcut:'20:30'  will become to
    'this is a string text that...'

    normal truncate with 20 chars will cut the word in half
    'this is a string tex...'
    """

    els = map(int, arg.split(':'))
    start = els[0]
    end = els[1]
    if len(value) <= end:
        return value

    ocurrence = value[start:end].find(" ")

    if ocurrence:
        for pos in range(start, len(value)):
            if value[pos] == " " and pos < end:
                ocurrence = pos

        value = value[0:ocurrence] + "..."

    return value




