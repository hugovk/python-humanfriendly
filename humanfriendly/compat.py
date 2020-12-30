# Human friendly input/output in Python.
#
# Author: Peter Odding <peter@peterodding.com>
# Last Change: December 10, 2020
# URL: https://humanfriendly.readthedocs.io

"""
Compatibility helpers.
"""

__all__ = (
    'on_macos',
    'on_windows',
)

# Standard library modules.
import sys


def on_macos():
    """
    Check if we're running on Apple MacOS.

    :returns: :data:`True` if running MacOS, :data:`False` otherwise.
    """
    return sys.platform.startswith('darwin')


def on_windows():
    """
    Check if we're running on the Microsoft Windows OS.

    :returns: :data:`True` if running Windows, :data:`False` otherwise.
    """
    return sys.platform.startswith('win')
