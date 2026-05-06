from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name='Test User', email='test@example.com', team='Marvel')
        self.assertEqual(user.name, 'Test User')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel', description='Superhero team')
        self.assertEqual(team.name, 'Marvel')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(name='Test User', email='test2@example.com', team='DC')
        activity = Activity.objects.create(user=user, activity_type='Running', duration=30, date='2023-01-01')
        self.assertEqual(activity.activity_type, 'Running')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = User.objects.create(name='Test User', email='test3@example.com', team='Marvel')
        leaderboard = Leaderboard.objects.create(user=user, points=100, rank=1)
        self.assertEqual(leaderboard.rank, 1)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Push Ups', description='Upper body exercise', difficulty='Easy')
        self.assertEqual(workout.name, 'Push Ups')
