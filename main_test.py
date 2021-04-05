import unittest

loader = unittest.TestLoader()
start_dir = 'test'
suite = loader.discover(start_dir, pattern='test_*')

runner = unittest.TextTestRunner()
runner.run(suite)
