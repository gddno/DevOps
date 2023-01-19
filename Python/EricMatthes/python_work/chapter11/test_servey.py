import unittest
from survey import AnonymousSurvey

class TestAnonymouseSurvey(unittest.TestCase):
	"""Тесты для класса AnonymouseServey"""
		
	def setUp(self):
		"""Создание опроса и набора ответов для всех тестовых методов"""
		question = "What language did you first learn to speak"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['English', 'Arabic', 'Portugal']

	def test_store_single_response(self):
		"""Проверяет, что один ответ сохранен правильно"""
		self.my_survey.store_response(self.responses[0])
		self.assertIn('English', self.my_survey.responses)

	"""Проверяет, что три ответа сохраняются правильно"""
	def test_store_three_responses(self):
		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
	unittest.main()