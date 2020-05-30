# -*- coding: utf-8 -*-

__all__ = ['KnowledgeTracing']

import random
import matplotlib.pyplot as plt


class Student(object):

    def __init__(self, name):

        self.name = name
        self.time_index = 0
        self.skill_history = {}

    def setup_skill(self, skill):

        if skill.name not in self.skill_history:
            self.skill_history[skill.name] = []

        self.skill_history[skill.name].append(skill)


class Skill(object):
    def __init__(self, name, value=.5, guess=.3, slip=.3, transition=.4):

        self.name = name
        self.value = value
        self.guess = guess
        self.slip = slip
        self.transition = transition


class KnowledgeTracing(object):

    def __init__(self, student):

        self.student = student

    def correct_answer(self, knowledge_value, slip_value, guess_value):

        dividend = knowledge_value * (1 - slip_value)
        divisor = (knowledge_value * (1 - slip_value)) + \
                  ((1 - knowledge_value) * guess_value)

        return dividend / divisor

    def wrong_answer(self, knowledge_value, slip_value, guess_value):
        dividend = knowledge_value * slip_value
        divisor = (knowledge_value * slip_value) + \
                  ((1 - knowledge_value) * (1 - guess_value))

        return dividend / divisor

    def update_skill(self, skill_name, status):

        if status is True:

            new_value = self.correct_answer()

        else:

            new_value = self.wrong_answer()

        return new_value + (1 - new_value) * transition_value


def correct_answer(knowledge_value, slip_value, guess_value):

    dividend = knowledge_value * (1 - slip_value)
    divisor = (knowledge_value * (1 - slip_value)) + \
              ((1 - knowledge_value) * guess_value)

    return dividend / divisor


def wrong_answer( knowledge_value, slip_value, guess_value):
    dividend = knowledge_value * slip_value
    divisor = (knowledge_value * slip_value) + \
              ((1 - knowledge_value) * (1 - guess_value))

    return dividend / divisor


def update_skill(knowledge_value, slip_value, guess_value, transition_value, status):

    if status is True:

        new_value = correct_answer(knowledge_value, slip_value, guess_value)

    else:

        new_value = wrong_answer(knowledge_value, slip_value, guess_value)

    return new_value + (1 - new_value) * transition_value


if __name__ == '__main__':

    value = .4
    values = [value]

    for i in range(50):

        index_status = random.choice([True, False])

        value = update_skill(
            knowledge_value=value,
            slip_value=.3,
            guess_value=.3,
            transition_value=.08,
            status=index_status
        )

        print(i, index_status, value)
        values.append(value)

    plt.plot(values)
    plt.show()
