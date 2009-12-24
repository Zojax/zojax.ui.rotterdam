##############################################################################
#
# Copyright (c) 2007 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
from zope.component import getMultiAdapter
from zope.traversing.browser import absoluteURL


class ContextActions(object):

    actions = ()

    def __call__(self):
        context = self.context
        request = self.request
        
        actions = getMultiAdapter(
            (context, request), name='view_get_menu')['zmi_actions']

        if actions:
            url = absoluteURL(context, request)

            for action in actions:
                action_url = action['action']
                if action_url and not action_url.startswith('http'):
                    action['action'] = '%s/%s'%(url, action_url)

            self.actions = actions

        return self.index()
