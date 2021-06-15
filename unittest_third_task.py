import unittest
from third_task import read_file

class TestReadFile(unittest.TestCase):
    def test_read_file(self):
        self.assertEqual(read_file(), "1u 0v 4w") 

if __name__ == '__main__':
    unittest.main()
