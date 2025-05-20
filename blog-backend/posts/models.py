from django.db import models

class Post(models.Model):
    LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
        ('typescript', 'TypeScript'),
        ('java', 'Java'),
        ('ruby', 'Ruby'),
        ('php', 'PHP'),
        ('go', 'Go'),
        ('rust', 'Rust'),
        ('csharp', 'C#'),
        ('cpp', 'C++'),
        ('swift', 'Swift'),
        ('kotlin', 'Kotlin'),
        ('other', 'その他'),
    ]
    #タイトル
    title = models.CharField(max_length=200)
    #トップページの見出し用
    content = models.TextField()
    body = models.TextField(verbose_name="本文", null=True, blank=True)
    #作成日時
    created_at = models.DateTimeField(auto_now_add=True)
    #開発言語
    develop_lang = models.CharField(
        max_length=20,
        choices=LANGUAGE_CHOICES,
        default='python',
        verbose_name='開発言語'
    )

    class Meta:
        db_table = "article"

    def __str__(self):
        return self.title