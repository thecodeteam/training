__author__ = 'mcowger'

import logging
from pprint import pformat, pprint

class CloudFoundryOrg(object):

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
        name,
        guid=None,
        url=None,
        billing_enabled=False,
        quota_definition_guid=None,
        status="active",
        quota_definition_url=None,
        spaces_url=None,
        domains_url=None,
        private_domains_url=None,
        users_url=None,
        managers_url=None,
        billing_managers_url=None,
        auditors_url=None,
        app_events_url=None,
        space_quota_definitions_url=None,
        metadata=None
    ):
        self._name = name
        self.billing_enabled=billing_enabled
        self.quota_definition_guid=quota_definition_guid
        self.status=status
        self.quota_definition_url=quota_definition_url
        self.spaces_url=spaces_url
        self.domains_url=domains_url
        self.private_domains_url=private_domains_url
        self.users_url=users_url
        self.managers_url=managers_url
        self.billing_managers_url=billing_managers_url
        self.auditors_url=auditors_url
        self.app_events_url=app_events_url
        self.space_quota_definitions_url=space_quota_definitions_url
        self.guid = metadata['guid']
        self.url = metadata['url']



    @property
    def name(self):
        return self._name

    @staticmethod
    def from_dict(metadata, dict):
        return CloudFoundryOrg(metadata=metadata, **dict)

