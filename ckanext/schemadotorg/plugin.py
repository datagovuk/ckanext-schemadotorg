# -*- coding: utf-8 -*-
"""
The schema.org plugin
"""
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class SDOPlugin(plugins.SingletonPlugin):
    """
    A plugin for integrating schema.org schema into the rendering
    of the templates.
    """
    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.ITemplateHelpers, inherit=True)

    def update_config(self, config):
        """
        Adds more information to the CKAN configuration, this is also
        the place to do one-off initialisation during startup if
        necessary.
        """
        toolkit.add_template_directory(config, 'templates')

    def get_helpers(self):
        """
        A dictionary of extra helpers that will be available to provide
        helpers to the templates.  All functions in helpers.py will be
        loaded and made available unless their name begins with _.
        """
        from ckanext.schemadotorg import helpers
        from inspect import getmembers, isfunction

        helper_dict = {
            'sdo_installed': lambda: True,
        }

        functions_list = [o for o in getmembers(helpers, isfunction)]
        for name, fn in functions_list:
            if name[0] != '_':
                helper_dict[name] = fn

        return helper_dict
