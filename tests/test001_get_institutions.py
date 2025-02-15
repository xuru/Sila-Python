import unittest, silasdk

from tests.test_config import *

class Test001GetInstitutionsTest(unittest.TestCase):
    def test_get_institutions(self):
        payload = {
            "institution_name": "1st advantage bank"
        }
        response = silasdk.User.get_institutions(app, payload)
        self.assertTrue(response["success"])


if __name__ == "__main__":
    unittest.main()
