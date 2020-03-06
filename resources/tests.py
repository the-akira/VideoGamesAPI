from django.test import TestCase
from .models import Game, Director, Genre, Platform, Screenshot
import json

class TestEndpoints(TestCase):

	fixtures = [
		'games.json',
		'genres.json',
		'platforms.json',
		'directors.json',
		'screenshots.json'
	]

	def get_query(self, url):
		return self.client.get(url)

	def test_api_root(self):
		self.assertEqual(self.get_query("/api/").status_code, 200)

	def test_schema_root(self):
		self.assertEqual(self.get_query("/schema").status_code, 200)

	def test_games_root(self):
		self.assertEqual(self.get_query("/api/games/").status_code, 200)

	def test_games_search(self):
		response = self.get_query('/api/games/?search=castlevania')
		json_data = json.loads(response.content)
		game = Game.objects.all().first()
		self.assertEqual(response.status_code, 200)

		list_response = self.get_query('/api/games/')
		list_data = json.loads(list_response.content)
		self.assertLess(json_data["count"],list_data["count"])
		self.assertEqual(game.title, json_data['results'][0]['title'])

	def test_games_detail(self):
		response = self.get_query('/api/games/3/')
		json_data = json.loads(response.content)
		game = Game.objects.all().first()
		self.assertEqual(response.status_code, 200)
		self.assertEqual(game.title, json_data['title'])

	def test_genres_root(self):
		self.assertEqual(self.get_query("/api/genres/").status_code, 200)

	def test_platforms_root(self):
		self.assertEqual(self.get_query("/api/platforms/").status_code, 200)

	def test_platforms_search(self):
		response = self.get_query('/api/platforms/?search=SNES')
		json_data = json.loads(response.content)
		platform = Platform.objects.all().first()
		self.assertEqual(response.status_code, 200)

		list_response = self.get_query('/api/platforms/')
		list_data = json.loads(list_response.content)
		self.assertLess(json_data["count"],list_data["count"])
		self.assertEqual(platform.name, json_data['results'][0]['name'])

	def test_platforms_detail(self):
		response = self.get_query('/api/platforms/2/')
		json_data = json.loads(response.content)
		platform = Platform.objects.all().first()
		self.assertEqual(response.status_code, 200)
		self.assertEqual(platform.name, json_data['name'])