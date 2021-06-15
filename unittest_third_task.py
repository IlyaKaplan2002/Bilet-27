import unittest
from third_task import read_file


class TestReadFile(unittest.TestCase):
    def test_read_file_1(self):
        self.assertEqual(read_file(), "1u 0v 4w")

    def test_read_file_2(self):
        self.assertEqual(read_file("data/new_data.txt"), "29u 3v 0w")


if __name__ == '__main__':
    unittest.main()
