import unittest
from survey import AnonymousSurvey

class TestAnonymouseSurvey():
	"""Тесты для класса AnonymouseServey"""
	
	def test_store_single_response(self):
		"""Проверяет, что один ответ сохранен правильно"""
		question = "What language did you first learn to speak?"
		my_survey = AnonymouseSurvey(question)
		my_survey.store_response('English')
		self.assertIn('English', my_survey.responses)

	# """Проверяет, что три ответа сохраняются правильно"""
	# def test_store_three_responses(self):
	# 	question = ""
	# 	my_survey = AnonymouseSurvey(question)
	# 	responses = ['English', 'Arabic', 'Portugal']

	# 	for response in responses:
	# 		my_survey.store_response(response)

	# 	for response in responses:
	# 		self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
	unittest.main()