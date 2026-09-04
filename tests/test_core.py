import unittest
from termlens import visible_length
class Tests(unittest.TestCase):
 def test_ansi(self): self.assertEqual(visible_length('\x1b[31mred\x1b[0m'),3)
if __name__=='__main__': unittest.main()
