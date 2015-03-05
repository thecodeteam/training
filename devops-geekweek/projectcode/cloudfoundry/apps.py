import logging
from pprint import pformat, pprint


class CloudFoundryApp(object):

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
        buildpack=None,
        command=None,
        console=True,
        debug=None,
        detected_buildpack="",
        detected_start_command="",
        disk_quota=0,
        docker_image=None,
        environment_json=None,
        events_url="",
        health_check_timeout=None,
        instances=0,
        memory=0,
        name='',
        package_state='',
        package_updated_at=None,
        production=False,
        routes_url='',
        service_bindings_url='',
        space_guid='',
        space_url='',
        stack_guid='',
        stack_url='',
        staging_failed_reason=None,
        staging_task_id='',
        state='STOPPED',
        version='',
        health_check_type=None,
        diego=False,
        metadata=None

    ):
        self.buildpack=buildpack
        self.command=command
        self.console=console
        self.debug=debug
        self.detected_buildpack=detected_buildpack
        self.detected_start_command=detected_start_command
        self.disk_quota=disk_quota
        self.docker_image=docker_image
        self.environment_json=environment_json
        self.events_url=events_url
        self.health_check_timeout=health_check_timeout
        self.instances=instances
        self.memory=memory
        self._name=name
        self.package_state=package_state
        self.package_updated_at=package_updated_at
        self.production=production
        self.routes_url=routes_url
        self.service_bindings_url=service_bindings_url
        self.space_guid=space_guid
        self.space_url=space_url
        self.stack_guid=stack_guid
        self.stack_url=stack_url
        self.staging_failed_reason=staging_failed_reason
        self.staging_task_id=staging_task_id
        self.state=state
        self.health_check_type=health_check_type
        self.version=version
        self.diego=diego
        self.guid = metadata['guid']
        self.url = metadata['url']




    @property
    def name(self):
        return self._name

    @staticmethod
    def from_dict(metadata, dict):
        return CloudFoundryApp(metadata=metadata, **dict)


