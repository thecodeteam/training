__author__ = 'mcowger'

import logging
from pprint import pformat, pprint

class CloudFoundryRoute(object):

    @classmethod
    def get_class_name(cls):
        return cls.__name__

    def __str__(self):
        # to show include all variables in sorted order
        return "<{}>@0x{}:\n".format(self.get_class_name(),id(self)) + "\n".join(["  %s: %s" % (key.rjust(16), self.__dict__[key]) for key in sorted(set(self.__dict__))])

    def __repr__(self):
        return self.__str__()

    def __init__(
        self,
        host=None,
        guid=None,
        url=None,
        domain_guid=None,
        space_guid=None,
        domain_url=None,
        space_url=None,
        apps_url=None,
        metadata=None
    ):
        self.host=host
        self.domain_guid=domain_guid
        self.space_guid=space_guid
        self.domain_url=domain_url
        self.space_url=space_url
        self.apps_url=apps_url
        self.guid = metadata['guid']
        self.url = metadata['url']



    @property
    def name(self):
        return self.host

    @staticmethod
    def from_dict(metadata, dict):
        return CloudFoundryRoute(metadata=metadata, **dict)
