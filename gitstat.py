# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

import getopt
import re
import pandas as pd
import sys

from config.common import COL_TOTAL, COL_DELETION, COL_INSERTION, COL_COMMITS, ORDER_BY, COMMIT_FLAG
from config.util import safe_decode, execute
from env import AUTHOR_NAME_MAPPING, REPO

__author__ = "daya0576"
__date__ = "2017-10-20 11:25"

branch = 'develop'


class Repo(object):
    def __init__(self, path=''):
        self.path = path


def get_authors(repo):
    """ fetch all authors"""
    command = ['git', 'log', '--format=%aN']
    result = execute(command, repo)
    authors = set(result.splitlines())
    authors = [safe_decode(x) for x in authors]

    return authors


def get_stat_by(author, repo):
    """ sum of insertion/deletion/commits of author """
    author_filter = '--committer=^{} '.format(author)

    command = ['git', 'log', author_filter, '--oneline', '--shortstat', '--pretty=%{}'.format(COMMIT_FLAG)]
    # print(' '.join(command))
    # command = 'git log --oneline --shortstat --pretty='.split()
    result = execute(command, repo=repo)
    result = safe_decode(result)
    insertion = re.findall(r'(\d+) insertions', result)
    deletion = re.findall(r'(\d+) deletions', result)

    insertion_sum, deletion_sum = sum([int(x) for x in insertion]), sum([int(x) for x in deletion])

    d = {
        COL_COMMITS: result.count(COMMIT_FLAG),
        COL_INSERTION: insertion_sum,
        COL_DELETION: deletion_sum
    }
    return {author: d}


def get_dataframe(author_d):
    df = pd.DataFrame.from_dict(author_d, orient='index').reset_index()

    if AUTHOR_NAME_MAPPING:
        name_d = {x: k for k, v in AUTHOR_NAME_MAPPING.items() for x in v}
        df = df.replace({"index": name_d})
        df = df.groupby('index', as_index=False).sum()

    return df


def after(df):
    df.sort_values(COL_COMMITS, ascending=0)

    df_total = df.sum(numeric_only=True)
    df_total[COL_TOTAL] = '100%'
    total_changes = df_total[COL_INSERTION] + df_total[COL_DELETION]

    df[COL_TOTAL] = (df[COL_INSERTION] + df[COL_DELETION]) / total_changes
    df[COL_TOTAL] = df[COL_TOTAL].map('{:.2%}'.format)

    # Sort
    df = df.sort_values(ORDER_BY, ascending=0)

    # df = df.set_index('index')

    return df, df_total


def pretty_print(df, df_total):
    # TODO: pretty print && export to other format
    # Add the row of total to the end
    df = df.append(df_total, ignore_index=True)
    df['index'].fillna('TOTAL', inplace=True)

    df.set_index('index', inplace=True)
    df.index.name = None

    print('\n\n{}'.format(df))


def main():
    repo_path = sys.argv[-1] if len(sys.argv) > 2 else REPO
    if not repo_path:
        print('pytho3 main.py <REPO PATH>')
    repo = Repo(path=repo_path)
    author_d = {}
    # print('Analyzing ')
    for author in get_authors(repo):
        # print(author, end=' ')
        author_d.update(get_stat_by(author, repo))

    df = get_dataframe(author_d)
    df, df_total = after(df)

    pretty_print(df, df_total)

