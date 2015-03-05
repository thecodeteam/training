__author__ = 'mcowger'

import logging
from pprint import pformat, pprint

class CloudFoundrySpace(object):

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
        organization_guid=None,
        space_quota_definition_guid=None,
        organization_url=None,
        developers_url=None,
        managers_url=None,
        auditors_url=None,
        apps_url=None,
        routes_url=None,
        domains_url=None,
        service_instances_url=None,
        app_events_url=None,
        events_url=None,
        security_groups_url=None,
        metadata=None
    ):
        self._name = name
        self.organization_guid=organization_guid
        self.space_quota_definition_guid=space_quota_definition_guid
        self.organization_url=organization_url
        self.developers_url=developers_url
        self.managers_url=managers_url
        self.auditors_url=auditors_url
        self.apps_url=apps_url
        self.routes_url=routes_url
        self.domains_url=domains_url
        self.service_instances_url=service_instances_url
        self.app_events_url=app_events_url
        self.events_url=events_url
        self.security_groups_url=security_groups_url
        self.guid = metadata['guid']
        self.url = metadata['url']



    @property
    def name(self):
        return self._name

    @staticmethod
    def from_dict(metadata, dict):
        return CloudFoundrySpace(metadata=metadata, **dict)

