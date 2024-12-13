import unittest
import test_12_1
import test_12_2

check = unittest.TestSuite()
check.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_1.RunnerTest))
check.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_2.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(check)