# -*- coding: utf-8 -*-

from itertools import imap, izip
from operator import attrgetter

from flask.ext.restless import helpers


def sort_tasks(tasks):
    sorted_tasks_dict = []
    remaining = 0
    if len(tasks):

        ids = set(imap(attrgetter('id'), tasks))
        next_ids = set(imap(attrgetter('next_id'), tasks))
        head_set = (ids - next_ids)
        if len(head_set) != 1:
            # somehow we lost the head of the linked list
            # just return whatever we can
            sorted_tasks_dict = map(helpers.to_dict, tasks)
        else:
            # we found the head - start rebuilding the linked list
            head = head_set.pop()
            lookup = dict(izip(imap(attrgetter('id'), tasks), tasks))

            safety = len(tasks)
            sorted_tasks = []
            i = head
            while lookup[i].next_id is not None:
                sorted_tasks.append(lookup[i])
                i = lookup[i].next_id

                if safety < 0:
                    # the linked list is shuffled
                    # exit the loop and sacrifice the order
                    sorted_tasks = tasks
                    break
                safety -= 1

            if safety >= 0:
                sorted_tasks.append(lookup[i])

            sorted_tasks_dict = map(helpers.to_dict, sorted_tasks)

    return sorted_tasks_dict
