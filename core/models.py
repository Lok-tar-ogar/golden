from django.db import models

class picture(models.Model):
    title = models.CharField('标题', max_length=20)
    caption = models.CharField('内容', max_length=34, blank=True, null=True)
    filepath = models.CharField('文件地址', max_length=200, blank=True, null=True)  # 头像路径
    language = models.CharField('语言 zh | en', max_length=34, default='zh')
    dimDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "图片"
        verbose_name_plural = "图片库"
        ordering = ['id']

    def __str__(self):
        return self.title

class syspara(models.Model):
    """
    网站标识 等系统参数;
    """
    key = models.CharField('键', max_length=20)
    value = models.CharField('值', max_length=3400, blank=True, null=True)
    language = models.CharField('语言 zh | en', max_length=34, default='zh')
    dimDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "系统参数"
        verbose_name_plural = "系统参数们"
        ordering = ['id']

    def __str__(self):
        return self.key


# Create your models here.
class carousel(models.Model):

    """
    轮播.
    """
    title = models.CharField('标题', max_length=50)
    imgs = models.ManyToManyField(picture)
    link = models.CharField('链接地址（可为空）', max_length=50, blank=True)
    caption = models.CharField('子标题', max_length=500, blank=True, null=True)
    language = models.CharField('语言 zh | en', max_length=34, default='zh')
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '轮播管理'
        ordering = ['-dimDate'] # sorted news by dimdate
class productclass(models.Model):
    '''
    产品
    '''
    name = models.CharField('产品分类名称', max_length=50)
    language = models.CharField('语言 zh | en', max_length=34, default='zh')
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '产品分类'
        ordering = ['-dimDate'] # sorted news by dimdate
class product(models.Model):
    '''
    产品
    '''
    name = models.CharField('产品名称', max_length=50)
    imgs = models.ForeignKey(picture, to_field='id', null=True)
    content = models.TextField('介绍详情')
    viewedTimes = models.IntegerField('浏览次数',default=0)
    type = models.ForeignKey(productclass)
    language = models.CharField('语言 zh | en', max_length=34, default='zh')
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '产品'
        ordering = ['-dimDate'] # sorted news by dimdate
class facilityclass(models.Model):
    '''
    产品
    '''
    name = models.CharField('设备分类名称', max_length=50)
    language = models.CharField('语言 zh | en', max_length=34, default='zh')
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '设备分类'
        ordering = ['-dimDate'] # sorted news by dimdate
class facility(models.Model):
    '''
    设备
    '''
    name = models.CharField('设备名称', max_length=50)
    imgs = models.ForeignKey(picture, to_field='id', null=True)
    content = models.TextField('介绍详情')
    viewedTimes = models.IntegerField('浏览次数',default=0)
    type = models.ForeignKey(productclass)
    language = models.CharField('语言 zh | en', max_length=34, default='zh')
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '设备'
        ordering = ['-dimDate'] # sorted news by dimdate

class certificateclass(models.Model):
    '''
    产品
    '''
    name = models.CharField('证书分类名称', max_length=50)
    language = models.CharField('语言 zh | en', max_length=34, default='zh')
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '证书分类'
        ordering = ['-dimDate'] # sorted news by dimdate
class certificate(models.Model):
    '''
    设备
    '''
    name = models.CharField('资质名称', max_length=50)
    imgs = models.ForeignKey(picture, to_field='id', null=True)
    content = models.TextField('介绍详情')
    viewedTimes = models.IntegerField('浏览次数',default=0)
    type = models.ForeignKey(certificateclass)
    language = models.CharField('语言 zh | en', max_length=34, default='zh')
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '设备'
        ordering = ['-dimDate'] # sorted news by dimdate

class case(models.Model):
    '''
    设备
    '''
    name = models.CharField('案例名称', max_length=50)
    imgs = models.ForeignKey(picture, to_field='id', null=True)
    content = models.TextField('介绍详情')
    viewedTimes = models.IntegerField('浏览次数',default=0)
    href = models.CharField('友情链接', max_length=50)
    language = models.CharField('语言 zh | en', max_length=34, default='zh')
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '案例'
        ordering = ['-dimDate'] # sorted news by dimdate

class friendlink(models.Model):
    '''
    设备
    '''
    name = models.CharField('友情链接名称', max_length=50)
    href = models.CharField('友情链接', max_length=50)
    language = models.CharField('语言 zh | en', max_length=34, default='zh')
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '友情链接'
        ordering = ['-dimDate'] # sorted news by dimdate

class job(models.Model):
    '''
    设备
    '''
    name = models.CharField('职位名称', max_length=50)
    content = models.TextField('介绍详情')
    viewedTimes = models.IntegerField('浏览次数',default=0)
    href = models.CharField('友情链接', max_length=50,null=True)
    language = models.CharField('语言 zh | en', max_length=34, default='zh')
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '案例'
        ordering = ['-dimDate'] # sorted news by dimdate

class video(models.Model):
    title = models.CharField('标题', max_length=20)
    caption = models.CharField('内容', max_length=34, blank=True, null=True)
    filepath = models.CharField('文件地址', max_length=200, blank=True, null=True)
    language = models.CharField('语言 zh | en', max_length=34, default='zh')
    dimDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = "视频库"
        ordering = ['id']

    def __str__(self):
        return self.title
class articleclass(models.Model):
    '''
    产品
    '''
    name = models.CharField('文章分类名称', max_length=50)
    language = models.CharField('语言 zh | en', max_length=34, default='zh')
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '文章分类'
        ordering = ['-dimDate'] # sorted news by dimdate

class article(models.Model):
    '''
    文章
    '''
    title = models.CharField('文章标题', max_length=50)
    imgs = models.ForeignKey(picture, to_field='id', null=True)
    content = models.TextField('文章详情')
    viewedTimes = models.IntegerField('浏览次数')
    type = models.ForeignKey(certificateclass)
    language = models.CharField('语言 zh | en', max_length=34, default='zh')
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '文章'
        ordering = ['-dimDate'] # sorted news by dimdate


class user(models.Model):
    username = models.CharField('登录名', max_length=20, blank=True, null=False,unique=True)  # 登录名、昵称，唯一校验
    pwd = models.CharField('密码', max_length=34, blank=True, null=True)
    avt = models.ForeignKey(picture,to_field='id',null=True)
    salt=models.CharField('密码盐值',max_length=32,blank=True,null=True)
    type = models.CharField('用户类型', max_length=32, blank=True, null=True)
    dimDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "用户资料表"
        verbose_name_plural = "users"
        ordering = ['id']

    def __str__(self):
        return self.username

# class flowgroup(models.Model):
#     name=models.CharField('名字',max_length=20)
#     user = models.ManyToManyField(user)
#     dimDate = models.DateTimeField(auto_now_add=True)
#     class Meta:
#         verbose_name = "流程组表"
#         verbose_name_plural = "流程组们"
#         ordering = ['id']
#
#     def __str__(self):
#         return self.name
#
# class flow(models.Model):
#     name=models.CharField('名字',max_length=20)
#     groupName=models.ForeignKey(flowgroup)
#     orderId=models.CharField('下一个流程id号',max_length=20)
#     user = models.ManyToManyField(user)
#     dimDate = models.DateTimeField(auto_now_add=True)
#     class Meta:
#         verbose_name = "流程表"
#         verbose_name_plural = "流程们"
#         ordering = ['id']
#
#     def __str__(self):
#         return self.name



