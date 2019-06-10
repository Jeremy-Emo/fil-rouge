import datetime

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@stringfilter
def parse_date(date_string):
    try:
        splits = date_string.split("-")
        return splits[2] + "-" + splits[1] + "-" + splits[0]
    except ValueError:
        return None

register.filter(parse_date)

@stringfilter
def parse_time(time_string):
    try:
        minutes = int(time_string) % 60
        hours = int(int(time_string) / 60)
        if len(str(minutes)) < 2:
            minutes = "0" + str(minutes)
        return str(hours) + "h " + str(minutes) + "min"
    except ValueError:
        return None

register.filter(parse_time)
