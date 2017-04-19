#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Cedric van Putten
# Copyright (c) 2017 Cedric van Putten
#
# License: MIT
#

"""This module exports the Swaglint plugin class."""

from SublimeLinter.lint import NodeLinter, util


class Swaglint(NodeLinter):
    """Provides an interface to swaglint."""

    npm_name = 'swaglint'
    syntax = ('yaml')
    cmd = ('swaglint', '--reporter', 'compact', '--stdin', '--stdin-filename', '@')
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.1.5'
    regex = (
        r'(?:(?P<error>error)|(?P<warning>warning))\s@\s'
        r'(?P<line>[0-9]+)\:(?P<col>[0-9]+)\s-\s'
        r'(?P<message>.+)'
    )
    multiline = True
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_STDOUT
