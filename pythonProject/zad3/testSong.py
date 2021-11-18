import unittest
from song import sing


class testSinging(unittest.TestCase):
    def test_sing_all(self):
        self.assertEqual(sing(0),
                         "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.\n\n"
                         "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                         "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                         "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                         "On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                         "On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                         "On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                         "On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                         "On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                         "On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                         "On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                         "On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n")

    def test_sing_one(self):
        self.assertEqual(sing(1),
                         "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.\n\n")

    def test_sing_five(self):
        self.assertEqual(sing(5),
                         "On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n")

    def test_sing_one_three(self):
        self.assertEqual(sing(1, 3),
                         "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.\n\n"
                         "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                         "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n")

    def test_sing_three_seven(self):
        self.assertEqual(sing(3, 7),
                         "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                         "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                         "On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                         "On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                         "On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                         )

    def test_sing_one_out(self):
        self.assertRaises(ValueError, sing, 1, 100)

    def test_sing_negative(self):
        self.assertRaises(ValueError, sing, -1)

    def test_sing_toobig(self):
        self.assertRaises(ValueError, sing, 100)

    def test_sing_pos_neg(self):
        self.assertRaises(ValueError, sing, 5, -1)

    def test_sing_neg_pos(self):
        self.assertRaises(ValueError, sing, -1, 7)

    def test_sing_str(self):
        self.assertRaises(TypeError, sing, 'wwww')

    def test_sing_str_int(self):
        self.assertRaises(TypeError, sing, 'www', 3)

    def test_sing_arr(self):
        self.assertRaises(TypeError, sing, [])

    def test_sing_none(self):
        self.assertRaises(TypeError, sing, None)

    def test_sing_str_str(self):
        self.assertRaises(TypeError, sing, 'www', 'abcc')

    def test_sing_true_str(self):
        self.assertRaises(TypeError, sing, True, 'aaa')

    def test_sing_true_true(self):
        self.assertRaises(TypeError, sing, True, True)
