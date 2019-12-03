import unittest
import os
import main
import re

class MyTestCase(unittest.TestCase):
    def test_something(self):
        for _, _, arquivo in os.walk('input'):
            for dir in arquivo:
                input_file = open('input/' + dir, 'r')
                output_file = open('output/' + dir, 'r')
                response = re.sub('[+\\n&]', '', output_file.read())
                n, r = input_file.readline().split(' ')
                inteiros = list(map(int, input_file.readline().split()))
                print(main.buscar(int(n), int(r), inteiros), response)
                self.assertEqual(main.buscar(int(n), int(r), inteiros), response)
                input_file.close()
                output_file.close()


if __name__ == '__main__':
    unittest.main()
