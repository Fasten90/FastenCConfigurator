import unittest
import os


class TestSystem(unittest.TestCase):

    def test_upper(self):
        import FastenCConfigurator
        FastenCConfigurator.main()
        # Expected files:
        expected_existing_files = [ 'config_NAME_OF_SET.md', 'config_new_debug_set.md' ]
        for item in expected_existing_files:
            self.assertTrue(os.path.exists(item))
        self.assertFalse(os.path.exists('RandomFilesName.md'))


if __name__ == '__main__':
    unittest.main()

