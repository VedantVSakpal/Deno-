import unittest

from chatbot import DenoBot


class DenoBotTests(unittest.TestCase):
    def setUp(self):
        self.bot = DenoBot()

    def test_greeting_response(self):
        response = self.bot.respond("Hello")
        self.assertIn("college assistant", response)

    def test_fee_response(self):
        response = self.bot.respond("What are the fees?")
        self.assertIn("fee structures", response)

    def test_course_response(self):
        response = self.bot.respond("Tell me about courses")
        self.assertIn("engineering", response)

    def test_default_response(self):
        response = self.bot.respond("How is the campus?")
        self.assertIn("campus", response.lower())

    def test_college_name_response(self):
        response = self.bot.respond("What is the name of college?")
        self.assertIn("Parul University", response)

    def test_location_response(self):
        response = self.bot.respond("Where is the college located?")
        self.assertIn("Vadodara", response)

    def test_parul_university_description_response(self):
        response = self.bot.respond("What is Parul University?")
        self.assertIn("Parul University", response)
        self.assertIn("Vadodara", response)


if __name__ == "__main__":
    unittest.main()
