import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Steps
from ..serializers import StepsSerializer
import datetime
import pytz

# Initialize APIClient Application
client = Client()

class GetAllStepsTest(TestCase):
    """ Test module for GET all steps API """

    def setUp(self):
        self.user1 = User.objects.create(username='testuser', password='password')
        client.force_login(User.objects.get_or_create(username='testuser')[0])
        Steps.objects.create(
            steps=579,
            owner=self.user1,
            date_start=datetime.datetime(2017, 10, 1, 11, tzinfo=pytz.UTC),
            date_end=datetime.datetime(2017, 10, 1, 12, tzinfo=pytz.UTC),
        )
        Steps.objects.create(
            steps=1204,
            owner=self.user1,
            date_start=datetime.datetime(2017, 10, 1, 13, tzinfo=pytz.UTC),
            date_end=datetime.datetime(2017, 10, 1, 14, tzinfo=pytz.UTC),
        )

        self.user2 = User.objects.create(username='user2', email='user2@users.com')
        Steps.objects.create(
            steps=42,
            owner=self.user2,
            date_start=datetime.datetime(2017, 9, 12, 11, tzinfo=pytz.UTC),
            date_end=datetime.datetime(2017, 9, 12, 12, tzinfo=pytz.UTC),
        )

    def test_get_all_steps(self):
        # get API response
        response = client.get(reverse('get_post_steps'))
        # get data from db
        steps = Steps.objects.filter(owner=self.user1)
        serializer = StepsSerializer(steps, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(len(serializer.data), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
