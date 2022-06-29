from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg, Count


class Post(models.Model):
    """Post model"""

    title = models.CharField(
        max_length=100, default='My Title', help_text="Title of the post")
    content = models.CharField(
        max_length=255, blank=True, help_text='Content of the post')

    class Meta:
        ordering = ['id']

    def rating_average(self):
        """Returns the average rating"""
        return self.rate_set.aggregate(Avg('rate'))['rate__avg']

    def rating_count(self):
        """Returns the count of the rating"""
        return self.rate_set.aggregate(count=Count('rate'))['count']

    def __str__(self) -> str:
        """Returns a string representation of the post"""
        return f'Post title: {self.title} with average rating of {self.rating_average()}'


class Rate(models.Model):
    """Rate Model"""
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    rate = models.IntegerField(choices=RATING_CHOICES, default=5)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Can enable this to force each user send one rate per post without overwriting.
    # class Meta:
    #     unique_together = ('User', 'post',)

    def __str__(self):
        """Returns a string representation of the rate"""
        return f'User {self.user.username} Rated {self.rate} to post {self.post.title}'
