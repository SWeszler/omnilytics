from unittest import TestCase
from utils import generate_sequence

class TestGenerateString(TestCase):

    def test_integer_20percent(self):
        sequence, report = generate_sequence()
        integers = 0
        total = 0
        for s in sequence.split(','):
            total += 1
            try:
                int(s)
                integers += 1
            except:
                pass

        self.assertEqual("{:.2f}".format(integers/total), "0.20")


    def test_integer_20percent_report(self):
        sequence, report = generate_sequence()
        total = sum(report.values())

        self.assertEqual("{:.2f}".format(report['integer']/total), "0.20")