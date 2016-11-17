# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 12:26:15 2016

@author: gergov
"""

import unittest
import tenper, filelines, birthdate

class TestMyExcHandling(unittest.TestCase):
    
    # test tenper.py
    def test_tenper_zero(self):
        self.assertEqual(tenper.tenper(0), 'fail')
            
    # test filelines.py
    def test_filelines_nofile(self):
        self.assertEqual(filelines.filelines('notafile.txt'), 0)
                    
    # test birthdate.py
        
    def test_birthdate_bigger(self):
        self.assertRaises(ValueError, birthdate.Person, 'jozsi', 2018)
        
    def test_birthdate_valid_birthdate(self):
        jozsi = birthdate.Person('Jozsi', 1977)
        self.assertEqual(jozsi.get_birthdate(), 1977)
        
    def test_birthdate_valid_name(self):
        jozsi = birthdate.Person('Jozsi', 1977)
        self.assertEqual(jozsi.get_name(), 'Jozsi')
        
        
if __name__ == '__main__':
    unittest.main()