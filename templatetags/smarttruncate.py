__author__ = 'pedroserrudo'
from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()

@register.filter
@stringfilter
def smartcut(value:str, arg) -> str:
    """
	
    usage: description|smartcut:"20:30"

    'This is a string text that will become smart truncated'|smartcut:'20:30'  will become to
    'This is a string text that...'

    normal truncate with 20 chars will cut the word in half
    'This is a string tex...'
    """

    els = map(int, arg.split(':'))
    start = els[0]
    end = els[1]
    if len(value) <= end:
        return value

    occurrence = value[start:end].find(" ")

    if occurrence:
        for pos in range(start, len(value)):
            if value[pos] == " " and pos < end:
                occurrence = pos

        value = value[0:occurrence] + "..."

    return value




