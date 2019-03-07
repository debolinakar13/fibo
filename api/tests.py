import unittest
import os
import requests

from django.test import TestCase

print HttpRequest.get_host()

url = "http://127.0.0.1:8000/api/"

class FunctionTest(unittest.TestCase):
    def test_get_first_element(self):
        """Get first element of fibonacci Array"""
        myurl = url + "?number=1"
        req = requests.get(myurl)
        print "response content is %s, return code is %s" % (req.content, req.status_code)
        self.assertEqual(req.status_code, 200)

    def test_get_tenth_number(self):
        """Get tenth element of fibonacci Array"""
        myurl = url + "?number=10"
        req = requests.get(myurl)
        print "response content is %s, return code is %s" % (req.content, req.status_code)
        self.assertEqual(req.status_code, 200)

class NegativeTest(unittest.TestCase):
    
    def test_zero(self):
        """test the zero integer"""
        myurl = url + "?number=0"
        req = requests.get(myurl)
        print "response content is %s, return code is %s" % (req.content, req.status_code)
        self.assertTrue("zero is not allowed" in req.content)

    def test_negative(self):
        """test the negative integer"""
        myurl = url + "?number=-1"
        req = requests.get(myurl)
        print "response content is %s, return code is %s" % (req.content, req.status_code)
        self.assertTrue("negative integer is not allowed" in req.content)

    def test_string(self):
        """test the negative string"""
        myurl = url + "?number=string"
        req = requests.get(myurl)
        print "response content is %s, return code is %s" % (req.content, req.status_code)
        self.assertTrue("provide a valid number" in req.content)

    def test_float(self):
        """test the float"""
        myurl = url + "?number=0.9"
        req = requests.get(myurl)
        print "response content is %s, return code is %s" % (req.content, req.status_code)
        self.assertTrue("provide a valid number" in req.content)

if __name__ == '__main__':
    unittest.main()
        


