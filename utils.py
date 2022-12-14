import os.path

file_name = 'data/1apache_logs.txt'


def check_file(file_name):
    return os.path.exists(file_name)


def read_file(filename):
    with open(filename) as f:
        for row in f:
            yield row


def filter_query(act, data):
    return filter(lambda v: act in v, data)


def map_query(act, data):
    column = int(act)
    return map(lambda v: v.split(' ')[column], data)


def unique_query(data, *args, **kwargs):
    return set(data)


def sort_query(act, data):
    if act == 'asc':
        srt = False
    srt = True
    return sorted(data, reverse=srt)


def limit_query(act, data):
    n = int(act)
    return list(data[:n])


dict_function = {
    'filter': filter_query,
    'map': map_query,
    'unique': unique_query,
    'sort': sort_query,
    'limit': limit_query}


def query_action(cmd, value, data):
    if data is None:
        gen = read_file(file_name)
    else:
        gen = data
    res = dict_function[cmd](act=value, data=gen)
    return list(res)
