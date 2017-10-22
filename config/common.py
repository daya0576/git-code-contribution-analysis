# -*- coding: utf-8 -*-
from env import ORDER_BY as _ORDER_BY

COL_INSERTION   = '    Insertion'
COL_DELETION    = '    Deletion'
COL_COMMITS     = '    Commits'
COL_TOTAL       = '    % of changes'


order_d = dict(
    commits=COL_COMMITS,
    insertion=COL_INSERTION,
    deletion=COL_DELETION,
    total=COL_TOTAL
)
ORDER_BY = order_d.get(_ORDER_BY, COL_COMMITS)

COMMIT_FLAG = '%%'
