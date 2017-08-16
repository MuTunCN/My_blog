from blog.models import Post, DayView, Category
from django.utils import timezone
from django.db.models.aggregates import Sum


oDv = DayView.objects.all().order_by('-running_time')
rt = oDv[0].running_time
cates = Category.objects.all()
dv = DayView(date=timezone.now())

for cate in cates:
    if cate.name == 'article':
        a_views = Post.objects.filter(category=cate).aggregate(sum=Sum('views'))['sum']
        dv.o_aViews = a_views
    elif cate.name == 'project':
        p_views = Post.objects.filter(category=cate).aggregate(sum=Sum('views'))['sum']
        dv.o_pViews = p_views

dv.running_time = rt+1
dv.arti_views = a_views - oDv[0].o_aViews
dv.proj_views = p_views - oDv[0].o_pViews
dv.save()
