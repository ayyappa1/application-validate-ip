import unittest    
from urllib.request import urlopen
import json

# unit testing - unittest.TestCase is used to create test cases by subclassing it 
class ApplicateionTest(unittest.TestCase):
# Returns True if host ip address matches in respose ip address. 
    def test_ip_addr(self):
        response = json.load(urlopen('http://ipinfo.io/json'))
        print(response)
        try:
            response['ip'] == "60.243.92.23"

        except:
            print("Please check your hostname type")
        self.assertRegex(response['ip'],r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')

# Running the test
if __name__ == '__main__':
    unittest.main()
