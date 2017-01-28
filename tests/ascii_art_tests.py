# -*- coding: utf-8 -*-
import unittest

from ascii_art import ASCII_Art
from PIL import Image

class AsciiArtTests(unittest.TestCase):
    def setUp(self):
        self.chars =  list('#@%S?+:*,. ')
        self.ascii_art = ASCII_Art(self.chars)
        self.test_image = Image.open('Images/test.jpg')

    def tearDown(self):
        self.test_image.close()
    def test_to_greyscale(self):
        self.assertEqual('L', self.ascii_art.to_greyscale(self.test_image).mode)

    def test_pixel_to_ascii(self):
        self.assertEqual('#', self.ascii_art.pixel_to_ascii(0))
        self.assertEqual(' ', self.ascii_art.pixel_to_ascii(255))
        self.assertEqual('?', self.ascii_art.pixel_to_ascii(int(255/2)))
    def test_calc_avg_pixel(self):
        self.assertEqual(0, self.ascii_art.calc_avg_pixel([]))
        self.assertEqual(0, self.ascii_art.calc_avg_pixel([0,0,0]))
        self.assertEqual(1, self.ascii_art.calc_avg_pixel([1,1,1]))

if __name__ == '__main__':
    unittest.main()

