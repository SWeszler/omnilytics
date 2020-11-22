import json
import os
import settings

REPORT = {
    'alphabetical': 0,
    'real_number': 0,
    'integer': 0,
    'alphanumeric': 0
}

def init_storage():
    report_path = os.path.join(settings.DATA_DIR, 'report.json')

    if not os.path.exists(report_path):
        with open(report_path, mode="w") as file:
            file.write(json.dumps(REPORT))

    output_path = os.path.join(settings.DATA_DIR, 'output.txt')

    if not os.path.exists(output_path):
        with open(output_path, mode="w") as file:
            file.write()


def generate_sequence():
    import random
    import string
    import copy
    
    sequence = ''
    types = ['a', 'r', 'i', 'an']
    report = copy.deepcopy(REPORT)

    while len(sequence.encode('utf-8')) < 2*10**6:
        word = ''
        length = random.choice(range(30))
        word_type = random.choice(types)

        if word_type == 'a':
            word_type = string.ascii_lowercase
            report['alphabetical'] += 1
        elif word_type == 'r':
            word_type = string.digits
            report['real_number'] += 1
        elif word_type == 'i':
            word_type = string.digits
            report['integer'] += 1
        else:
            word_type = string.ascii_lowercase + string.digits
            report['alphanumeric'] += 1

        for i in range(length):
            word += random.choice(word_type)
        sequence += word + ','

    return sequence.strip(','), report


def save_sequence(sequence):
    with open(os.path.join(settings.DATA_DIR, 'output.txt'), mode='w') as file:
        file.write(sequence)


def save_report(report):
    with open(os.path.join(settings.DATA_DIR, 'report.json'), mode='w') as file:
        file.write(json.dumps(report))


def get_report():
    result = None
    with open(os.path.join(settings.DATA_DIR, 'report.json'), 'r') as file:
        result = json.loads(file.read())

    return result