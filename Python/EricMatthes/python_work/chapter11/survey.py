class AnonymousSurvey():
	"""Сбор ананонимных ответов на опросы."""

	def __init__(self, question):
		"""Сохраняет ответы и готовится к сохранению ответа"""
		self.question = question
		self.responses = []

	def show_question(self):
		"""Выводит вопрос"""
		print(self.question)

	def store_response(self,new_response):
		"""Сохраняет один ответ на вопрос"""
		self.responses.append(new_response)

	def show_result(self):
		"""Выводит все полученные ответы"""
		print("Servey result: ")
		for responses in self.responses:
			print(f"- 	{responses}")