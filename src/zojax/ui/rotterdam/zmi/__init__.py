# This file is necessary to make this directory a package.

from zope import interface
from zope.app.rotterdam import Rotterdam
from zojax.theme.default.interfaces import ISkin


class IRotterdam(ISkin, Rotterdam):
    """ Rotterdam Layer """
