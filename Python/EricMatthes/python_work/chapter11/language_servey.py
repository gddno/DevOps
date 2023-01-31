from survey import AnonymousSurvey

# Определение вопроса с соданием экземпляра AnonymouseSurvey.
quation = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(quation)

#Вывод вопроса и сохранение ответа
my_survey.show_question()
print("Print 'q' at any time to quit.\n")

while True:
	response = input("Language: ")
	if response == 'q':
		break
	my_survey.store_response(response)

#Вывод результатов опроса.
print("\nThank you very to everyone who participated in the survey!")
my_survey.show_result()