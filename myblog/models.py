from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# 文章分类
class Category(models.Model):
    name = models.CharField('文章分类', max_length=100)
    index = models.IntegerField(default=999, verbose_name='分类排序')

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章标签
class Tag(models.Model):
    name = models.CharField('文章标签', max_length=100)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 推荐位
class Recommend(models.Model):
    name = models.CharField('推荐位', max_length=100)

    class Meta:
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章
class Article(models.Model):
    # 文章标题
    title = models.CharField('标题', max_length=100)
    # 文章摘要
    excerpt = models.TextField('摘要', max_length=300, blank=True)
    # 文章分类，多对一的关系，一篇文章对应一个分类，一个分类对应多篇文章
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='分类', blank=True)
    # 多对多的关系，一篇文章可以有多个标签，一个标签下有多篇文章
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    # 封面
    img = models.ImageField(upload_to='article_img/%Y/%m/%d', verbose_name='文章封面', blank=True, null=True)
    # 文章内容
    body = models.TextField()
    # 作者
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    # 阅读量
    views = models.PositiveIntegerField('阅读量', default=0)
    # 文章属于哪个推荐位
    recommend = models.ForeignKey(Recommend, on_delete=models.DO_NOTHING, verbose_name='推荐位', blank=True, null=True)
    # 发布时间
    create_time = models.DateTimeField('发布时间', auto_now_add=True)
    # 修改时间
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
            verbose_name = '文章'
            verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# Banner
class Banner(models.Model):
    # banner标题
    text_info = models.CharField('标题', max_length=50, default='')
    # 图片
    img = models.ImageField('轮播图', upload_to='banner/')
    # 链接
    link_url = models.URLField('图片链接', max_length=100, default='')
    # 是否激活显示
    is_active = models.BooleanField('是否显示', default=False)

    def __str__(self):
        return self.text_info

    class Meta:
        verbose_name = '轮播banner'
        verbose_name_plural = verbose_name


# 友情链接
class Link(models.Model):
    # 链接名称
    name = models.CharField('链接名称', max_length=20)
    link_url = models.URLField('网址', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
