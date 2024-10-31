import data2
import hw2
import unittest
# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1

    def test_create_rectangle(self):
        PointA = data2.Point(5, 5)
        PointB = data2.Point(8, 8)
        result = hw2.create_rectangle(PointA, PointB)
        expected = data2.Rectangle(data2.Point(5, 8), data2.Point(8, 5))
        self.assertEqual(expected, result)

    # Part 2

    def test_shorter_duration_than(self):
        D1 = data2.Duration(3, 30)
        D2 = data2.Duration(2, 15)
        result = hw2.shorter_duration_than(D1, D2)
        expected = False
        self.assertEqual(expected, result)
    # Part 3

    def test_song_shorter_than(self):
        Songs = [data2.Song("The Beatles", "Yesterday", data2.Duration(2, 5)), data2.Song("Eagles", "Hotel California",
                                                                                          data2.Duration(6, 30))]
        uppbound = data2.Duration(3, 30)
        result = hw2.song_shorter_than(Songs, uppbound)
        expected = [data2.Song('The Beatles', 'Yesterday', data2.Duration(2, 5))]
        self.assertEqual(expected, result)

    # Part 4
    def test_running_time(self):
        TheSongs = [data2.Song("Bee Gees", "Stayin Alive", data2.Duration(4, 45)), data2.Song("John Lennon", "Imagine",
                                data2.Duration(3, 7)), data2.Song("The Beatles", "Let It Be", data2.Duration(4, 3))]
        playlist = [2, 1, 0, 1]
        result = hw2.running_time(TheSongs, playlist)
        expected = [15, 2]
        self.assertEqual(expected, result)
    # Part 5
    def test_validate_route(self):
        citylinks = [['santa barbara', 'san luis obispo'], ['santa barbara', 'los angeles'],
                     ['los angeles', 'san diego']]
        cityname = ['san luis obispo', 'santa barbara', 'los angeles', 'san diego']
        result = hw2.validate_route(citylinks, cityname)
        expected = True
        self.assertEqual(expected, result)

    # Part 6
    def test_longest_repetition(self):
        list1 = [2, 2, 3, 3, 3, 4, 4, 4, 4]
        result = hw2.longest_repetition(list1)
        expected = 5
        self.assertEqual(expected, result)




if __name__ == '__main__':
    unittest.main()
