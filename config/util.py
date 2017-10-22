# -*- coding: utf-8 -*-
import subprocess
import sys
PY3 = sys.version_info[0] >= 3

if PY3:
    unicode = str
else:
    unicode = unicode

__author__ = "daya0576"
__date__ = "2017-10-20 16:20"

defenc = sys.getdefaultencoding()


def safe_decode(s):
    """Safely decodes a binary string to unicode"""
    if isinstance(s, unicode):
        return s
    elif isinstance(s, bytes):
        return s.decode(defenc, 'surrogateescape')
    elif s is not None:
        raise TypeError('Expected bytes or text, but got %r' % (s,))


def execute(command, repo):
    if repo.path:
        command = ['git', '-C', repo.path] + command[1:]
    ls_output = subprocess.check_output(command)
    return ls_output