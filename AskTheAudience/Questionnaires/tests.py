from django.test import TestCase
from django.urls import reverse

from Questionnaires.models import *

class QuestionModelTests(TestCase):
    def test_question_model(self):

        tested_text = "Some text"
        tested_answer = "Some answer"
        question = Question(text=tested_text)
        question.save()
        question.answer_set.create(text=tested_answer)
        question.save()

        self.assertEqual(question.__str__(), tested_text)
        self.assertEqual(question.answer_set.get(id=1).__str__(), tested_answer)

class ViewTests(TestCase):
    def test_index_view(self):
        url = reverse("questionnaires:index")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_vote_view(self):

        question = Question(text="Some text")
        question.save()
        question.answer_set.create(text='Answer one', votes_number=0)
        question.answer_set.create(text='Answer two', votes_number=10)
        question.save()

        url = reverse("questionnaires:vote")
        data = {'question_id' : question.id}
        resp = self.client.get(url, data)

        self.assertEqual(resp.status_code, 200)

    def test_results_view(self):

        question = Question(text="Some text")
        question.save()
        question.answer_set.create(text='Answer one', votes_number=0)
        question.answer_set.create(text='Answer two', votes_number=10)
        question.save()

        url = reverse("questionnaires:results")
        data = {'radio_choice' : 1, 'question_id' : question.id}
        resp = self.client.post(url, data)

        self.assertEqual(resp.status_code, 200)
