from django.test import TestCase
from ..models import Steps
from django.contrib.auth.models import User
import datetime
import pytz

class StepsCase(TestCase):
    """ Test module for Steps model """

    def setUp(self):
        self.user1 = User.objects.create(username='user1', email='user1@users.com')
        Steps.objects.create(
            pk=1,
            steps=579,
            owner=self.user1,
            date_start=datetime.datetime(2017, 10, 1, 11, tzinfo=pytz.UTC),
            date_end=datetime.datetime(2017, 10, 1, 12, tzinfo=pytz.UTC),
        )
        Steps.objects.create(
            pk=2,
            steps=1204,
            owner=self.user1,
            date_start=datetime.datetime(2017, 10, 1, 13, tzinfo=pytz.UTC),
            date_end=datetime.datetime(2017, 10, 1, 14, tzinfo=pytz.UTC),
        )

        self.user2 = User.objects.create(username='user2', email='user2@users.com')
        Steps.objects.create(
            pk=3,
            steps=42,
            owner=self.user2,
            date_start=datetime.datetime(2017, 9, 12, 11, tzinfo=pytz.UTC),
            date_end=datetime.datetime(2017, 9, 12, 12, tzinfo=pytz.UTC),
        )

    def test_get_steps(self):
        user1_steps = Steps.objects.get(pk=1)
        self.assertEqual(
            user1_steps.get_steps(), 579
        )

    def test_steps_owner(self):
        user1_steps1 = Steps.objects.get(pk=1)
        user1_steps2 = Steps.objects.get(pk=2)
        user2_steps1 = Steps.objects.get(pk=3)

        self.assertEqual(
            user1_steps1.owner, user1_steps2.owner
        )
        self.assertNotEqual(
            user1_steps1.owner, user2_steps1.owner
        )
