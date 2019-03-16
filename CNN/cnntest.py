import unittest
from predict_image import result


class Tests(unittest.TestCase):

    def test_1(self):
        """Check that cat1 is cat"""
        self.assertEqual(result('cat1.jpg'),'Cat')

    def test_2(self):
        """check that dog3 is dog"""
        self.assertEqual(result('dog2.jpg'), 'Dog') 

    

if __name__ == "__main__":
    unittest.main()
            