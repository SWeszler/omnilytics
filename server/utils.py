import json
import os
import settings
import time


def generate_sequence():
    import random
    import string
    import time
    
    max_length = 2*10**6
    sequence = ''
    types = ['a', 'r', 'i', 'an']
    total_count = 0
    report = {
        'alphabetical': 0,
        'real_number': 0,
        'integer': 0,
        'alphanumeric': 0
    }

    while len(sequence) <= max_length:
        word_type = random.choice(types)
        length = random.choice(range(2, 30))
        total_count += 1

        if length > max_length - len(sequence):
            length = max_length - len(sequence)

        if word_type == 'a':
            word_type = string.ascii_lowercase
            report['alphabetical'] += 1
        elif word_type == 'r':
            sequence += str(random.uniform(1, length))[:length] + ','
            report['real_number'] += 1
            continue
        elif word_type == 'i' and (report['integer'] / total_count) <= 0.2:
            sequence += str(random.randint(1, length))[:length] + ','
            report['integer'] += 1
            continue
        else:
            word_type = string.ascii_lowercase + string.digits
            report['alphanumeric'] += 1

        sequence += ''.join([random.choice(word_type) for i in range(length)]) + ','

    return sequence[:-1], report


def save_sequence(sequence, timestamp):
    with open(os.path.join(settings.DATA_DIR, 'output_{}.txt'.format(timestamp)), mode='w') as file:
        file.write(sequence)


def save_report(report, timestamp):
    with open(os.path.join(settings.DATA_DIR, 'report_{}.json'.format(timestamp)), mode='w') as file:
        file.write(json.dumps(report))


def get_report(timestamp):
    result = None
    with open(os.path.join(settings.DATA_DIR, 'report_{}.json'.format(timestamp)), 'r') as file:
        result = json.loads(file.read())

    return result


def get_output(timestamp):
    return os.path.join(settings.DATA_DIR, 'output_{}.txt'.format(timestamp))