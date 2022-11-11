import unittest
import test_bot
suite = unittest.TestLoader().loadTestsFromModule(test_bot)
unittest.TextTestRunner().run(suite)