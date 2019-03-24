import unittest
from app import app


class TestApp(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.status_code, 200)

    def test_ping(self):
        tester = app.test_client(self)
        response = tester.get("/ping")
        self.assertEqual(response.status_code, 200)

    def test_system(self):
        tester = app.test_client(self)
        response = tester.get("/system")
        self.assertEqual(response.status_code, 200)

    def test_media(self):
        tester = app.test_client(self)
        input = "11497188"
        response = tester.get("/mediainfo/" + input)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
