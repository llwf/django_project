import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Question
# Create your tests here.

class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        在将来发布的问卷应该返回False
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        在超过一天发布的问卷应该返回False
        """
        time = timezone.now() - datetime.timedelta(days=30, seconds=1)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_recently_question(self):
        """
        最近一天内发布的问卷，返回True
        """
        time = timezone.now() - datetime.timedelta(hours=22, seconds=12)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), True)
