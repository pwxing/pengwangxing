import unittest


def all_case():
    case_dir = "D:\\selenium\\apy_framework\\testsuites"

    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir, pattern="test*.py", top_level_dir=None)

    # print discover
    for test_suite in discover:
        # print test_suite
        for test_case in test_suite:
            testcase.addTests(test_case)
    print testcase
    return testcase

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(all_case())