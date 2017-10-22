# -*- coding: utf-8 -*-
import functools

__author__ = "daya0576"
__date__ = "2017-10-20 14:39"

from line_profiler import LineProfiler

class Line_Profiler(object):
    def __init__(self, follow=None):
        self.follow = follow or []

    def __call__(self, func):
        def profiled_func(*args, **kwargs):
            line_profiler = LineProfiler()
            line_profiler.add_function(func)
            map(lambda x: line_profiler.add_function(x), self.follow)
            line_profiler.enable_by_count()
            result = func(*args, **kwargs)
            line_profiler.disable_by_count()
            line_profiler.print_stats(stripzeros=True)
            return result

        return functools.wraps(func)(profiled_func)


profile = Line_Profiler()

