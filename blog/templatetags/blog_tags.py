#自定义模板标签
from ..models import Post, Tag
from django import template
register = template.Library()


@register.simple_tag
def get_all_tags():
    return Tag.objects.all()