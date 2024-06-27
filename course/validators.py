import re

from rest_framework.serializers import ValidationError


class UrlValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, url):
        tmp_url = dict(url).get(self.field)
        if tmp_url is not None and 'youtube.com' not in tmp_url:
            raise ValidationError('The link cannot be used')


class PayValidator:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        pay_value1 = dict(value).get(self.field1)
        pay_value2 = dict(value).get(self.field2)

        if (pay_value1 is None and pay_value2 is None) or (pay_value1 is not None and pay_value2 is not None):
            raise ValidationError('Pay for the course or lesson')