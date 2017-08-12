from django.shortcuts import render
# from blog.models import AcUser
import time
import markdown
from django.http import HttpResponse
from blog.models import Post
from django.shortcuts import render, get_object_or_404


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    return render(request, 'detail.html', context={'post': post})


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def index(request):
    post_list = Post.objects.all().order_by('-created_time')    #创建时间倒叙
    content = {
        'post_list': post_list
    }
    return render(request, "index.html", content)


def ac_data_ana(request):
    lvl_data = get_lvl_data()
    gender_data = get_gender_data()
    au_data = get_au_data()
    re_data = get_re_data()
    content = {
        "lvl_data": lvl_data,
        "gender_data": gender_data,
        "au_data": au_data,
        "re_data":re_data
    }
    return render(request, "acDataAna.html", content)


def get_re_data():
    """分析注册时间分布"""
    # data_index = set()
    # for item in AcUser._get_collection().find():
    #     d_time = item["regTime"].split(".")[0]
    #     t = time.strptime(d_time, "%Y-%m-%d %H:%M:%S")
    #     data_index.add(t[0])
    # data_index = list(data_index)
    # data_index.sort()
    #
    # def get_year_num(year):
    #     num = 0
    #     for item in AcUser._get_collection().find():
    #         d_time = item["regTime"].split(".")[0]
    #         t = time.strptime(d_time, "%Y-%m-%d %H:%M:%S")
    #         if t[0] == year:
    #             num += 1
    #     return num
    #
    # return list(map(get_year_num, [i for i in data_index])), data_index
    # return  [251, 15920, 41765, 35883, 173833, 333], [2007, 2008, 2013, 2014, 2015, 2016]
    return [['2007', 251], ['2008', 15920], ['2013', 41765], ['2014', 35883], ['2015', 173833], ['2016', 333]]

def get_au_data():
    """分析活跃用户 活跃用户指最后一次登陆在2017年3月后"""
    # time.struct_time(tm_year=2017, tm_mon=7, tm_mday=14, tm_hour=8, tm_min=25, tm_sec=16, tm_wday=4, tm_yday=195, tm_isdst=-1)
    # au = 0
    # iu = 0
    # for item in AcUser._get_collection().find():
    #     d_time = item["lastLoginDate"].split(".")[0]
    #     t = time.strptime(d_time, "%Y-%m-%d %H:%M:%S")
    #     if t[0] == 2017 and t[1] >= 3:
    #         au += 1
    #     else:
    #         iu += 1
    # return [["活跃用户", au], ["非活跃用户", iu]]
    return [['活跃用户', 75208], ['非活跃用户', 192777]]

def get_gender_data():
    """性别分布"""
    # gender_data = []
    # for i in range(2):
    #     pipeline = [
    #         {"$match": {"gender": i}},
    #         {"$group": {"_id": "null", "count": {"$sum": 1}}}
    #     ]
    #     gender = AcUser._get_collection().aggregate(pipeline)
    #     gender_data.append(["男性" if i == 1 else "女性", [item["count"] for item in gender][0]])
    # return gender_data
    return [['女性', 146875], ['男性', 109252]]


def get_lvl_data():
    """分析等级分布"""
    # lvl_data = []
    # for i in range(4):
    #     pipeline = [
    #         {"$match": {"level": {"$gte": 0 + i * 10, "$lt": 9 + i * 10}}},
    #         {"$group": {"_id": "null", "count": {"$sum": 1}}}
    #     ]
    #     lvl_num = AcUser._get_collection().aggregate(pipeline)
    #     lvl_name = str(0 + i * 10) + "-" + str(9 + i * 10)
    #     lvl_data.append([lvl_name, [item["count"] for item in lvl_num][0]])
    # return lvl_data
    return [['0-9', 167631], ['10-19', 21625], ['20-29', 12950], ['30-39', 13532]]