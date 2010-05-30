"""
Copyright 2006 ThoughtWorks, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from selenium import selenium
import unittest
import time

class TestGoogle(unittest.TestCase):
    def setUp(self):
        self.selenium = selenium("localhost", \
            4444, "*firefox", "http://www.w3.org")
        self.selenium.start()

    def test_google(self):
        sel = self.selenium
        #sel.open("http://www.w3.org/Graphics/SVG/Test/20030813/htmlframe/full-interact-cursor-01-f.html")
        sel.open("http://www.w3.org/Graphics/SVG/Test/20030813/htmlframe/full-interact-dom-01-b.html")
        sel.click_at("svg-root", "0,0")
        print "1"
        time.sleep(2)
        sel.click_at("svg-root", "10,40")
        print "2"
        time.sleep(2)
        sel.click_at("svg-root", "10,80")
        sel.click_at("svg-root", "80,80")
        sel.click_at("svg-root", "160,80")
        print "3"
        print "sleeping"
        time.sleep(10)
    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
