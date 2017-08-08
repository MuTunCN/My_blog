#自定义模板标签
from ..models import Post
from django import template
register = template.Library()


@register.simple_tag
def get_newest_post(num=1):
    return Post.objects.all().order_by('-created_time')[:num]