# This file is necessary to make this directory a package.

from zope import interface
from zope.app.rotterdam import Rotterdam
from zojax.layoutform.interfaces import ILayoutFormLayer


class IRotterdam(Rotterdam, ILayoutFormLayer):
    """ Rotterdam Layer """
