__author__ = 'mcowger'

import logging
from pprint import pformat, pprint

class CloudFoundryDomain(object):

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
        name=None,
        metadata=None,
        owning_organization_guid=None,
        owning_organization_url=None
    ):
        self._name=name
        self.owning_organization_guid=owning_organization_guid
        self.owning_organization_url=owning_organization_url
        self.guid = metadata['guid']
        self.url = metadata['url']



    @property
    def name(self):
        return self._name

    @property
    def is_shared(self):
        if self.owning_organization_guid is None:
            return True
        return False

    @staticmethod
    def from_dict(metadata, dict):
        return CloudFoundryDomain(metadata=metadata, **dict)