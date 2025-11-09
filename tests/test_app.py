import os
import sys
import unittest

# Make sure project root is on the path (needed in Jenkins)
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from app import greet


class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(
            greet("World"),
            "Hello, World from FirstName LastName!",
        )


if __name__ == "__main__":
    unittest.main()
