import json
from urlparse import urljoin
from collections import OrderedDict
import logging
import time

import requests
from memoize import Memoizer

from cloudfoundry.apps import CloudFoundryApp
from cloudfoundry.organizations import CloudFoundryOrg
from cloudfoundry.spaces import CloudFoundrySpace
from cloudfoundry.routes import CloudFoundryRoute
from cloudfoundry.domains import CloudFoundryDomain
from cloudfoundry.utils import create_bits_zip


cache_store = {}
memo = Memoizer(cache_store)
max_cache_time = 10


class CloudFoundryException(Exception):
    pass


class CloudFoundryAuthenticationException(CloudFoundryException):
    pass


class CloudFoundryInterface(object):

    def __init__(self, target, username=None, password=None, debug=False):
        self._apps = None
        self._orgs = None
        self._spaces = None
        self._routes = None
        self._domains = None
        self._expires_at = None

        self._target = target
        self._username = username
        self._password = password
        self._token = None
        self._auth_endpoint = None

        self._debug = debug




    def login(self):
        logging.info("Logging in to CF API {}".format(self._target))

        auth_endpoint = requests.get("{}/{}".format(self._target,"v2/info"), verify=True).json()['authorization_endpoint']

        login_data={
                "grant_type": "password",
                "password": self._password,
                "scope": "",
                "username": self._username
        }
        headers =  {"Authorization": "Basic Y2Y6", "Accept": "application/json"}
        response = requests.post("{}/{}".format(auth_endpoint,"oauth/token"), data=login_data, headers=headers, verify=True).json()
        self._token = response['access_token']
        self._expires_at = int(response['expires_in']) + time.time()

        self._session = requests.Session()
        self._session.headers.update(self._auth_args())


        return self._token

    def _auth_args(self):
        headers = {'Accept':'application/json'}
        headers.update({'Authorization': 'bearer {}'.format(self._token)})
        logging.debug("Returning Final Headers: {}".format(headers))
        return headers

    def _request(self, url, request_type=requests.get, data=None, verify=True, raw_data = False, files=None):

        if not self.live:
            raise CloudFoundryException("Auth Required and Not Logged In")


        if data and not raw_data:
            data = json.dumps(data)
        full_url = urljoin(self._target, url)

        response = self._session.request(request_type.__name__, full_url, verify=verify, data=data, files=files)

        if response.status_code in range(200,299):
            return response
        elif response.status_code == 404:
            raise CloudFoundryException("HTTP {} - {}".format(response.status_code, response.text))
        else:
            raise CloudFoundryException("HTTP {} - {}".format(response.status_code, response.text))

    def _get_or_exception(self, url, json=True, **kwargs):

        if json:
            final_dict = {}
            response = self._request(url, **kwargs)
            final_dict.update(response.json())
            while 'next_url' in response.json() and response.json()['next_url'] is not None:
                response = self._request(response.json()['next_url'], **kwargs)
                final_dict.update(response.json())

            return final_dict
        else:
            return self._request(url, **kwargs).text

    def _post_or_exception(self, url, json=True, **kwargs):
        if json:
            return self._request(url, request_type=requests.post, **kwargs).json()
        return self._request(url, request_type=requests.post, **kwargs).text

    def _delete_or_exception(self, url, json=True, **kwargs):
        if json:
            return self._request(url, request_type=requests.delete, **kwargs).json()
        return self._request(url, request_type=requests.delete, **kwargs).text

    def _put_or_exception(self, url, json=True, files=None, data=None, **kwargs):
        if json:
            return self._request(url, request_type=requests.put, files=files, data=data, **kwargs).json()
        return self._request(url, request_type=requests.put, files=files, data=data, **kwargs).text


    @property
    def live(self):
        current_time = time.time()
        if current_time > self._expires_at:
            return False
        return True



    @property
    def apps(self):
        self._update_apps()
        return self._apps


    @property
    def orgs(self):
        self._update_orgs()
        return self._orgs


    @property
    def spaces(self):
        self._update_spaces()
        return self._spaces

    @property
    def routes(self):
        self._update_routes()
        return self._routes


    @property
    def domains(self):
        self._update_domains()
        return self._domains


    @memo(max_age=max_cache_time)
    def _update_orgs(self):
        logging.info("Updating all orgs as user {}".format(self.username))
        raw = self._get_or_exception("v2/organizations")['resources']
        orgs = {}
        for org in raw:
            org_data = org['entity']
            metadata = org['metadata']
            current_org = CloudFoundryOrg.from_dict(metadata,org_data)
            orgs[current_org.guid] = current_org
        self._orgs = orgs


    @memo(max_age=max_cache_time)
    def _update_spaces(self):
        logging.info("Updating all spaces as user {}".format(self._username))
        raw = self._get_or_exception("v2/spaces")['resources']
        spaces = {}
        for space in raw:
            space_data = space['entity']
            metadata = space['metadata']
            current_org = CloudFoundrySpace.from_dict(metadata,space_data)
            spaces[current_org.guid] = current_org
        self._spaces = spaces


    @memo(max_age=max_cache_time)
    def _update_domains(self):
        logging.info("Updating all domains as user {}".format(self._username))
        domains = {}
        shared_raw = self._get_or_exception("v2/shared_domains")['resources']
        for domain in shared_raw:
            domain_data = domain['entity']
            metadata = domain['metadata']
            current_domain = CloudFoundryDomain.from_dict(metadata,domain_data)
            domains[current_domain.guid] = current_domain

        private_raw = self._get_or_exception("v2/private_domains")['resources']
        for domain in private_raw:
            domain_data = domain['entity']
            metadata = domain['metadata']
            current_domain = CloudFoundryDomain.from_dict(metadata,domain_data)
            domains[current_domain.guid] = current_domain

        self._domains = domains


    @memo(max_age=max_cache_time)
    def _update_apps(self):
        logging.info("Updating all app as user {}".format(self._username))
        raw = self._get_or_exception("v2/apps")['resources']
        apps = {}
        for app in raw:
            app_data = app['entity']
            metadata = app['metadata']
            current_app = CloudFoundryApp.from_dict(metadata,app_data)
            apps[current_app.guid] = current_app
        self._apps = apps

    @memo(max_age=max_cache_time)
    def _update_routes(self):
        logging.info("Updating all routes as user {}".format(self._username))
        raw = self._get_or_exception("v2/routes")['resources']
        routes = {}
        for route in raw:
            route_data = route['entity']
            metadata = route['metadata']
            current_route = CloudFoundryRoute.from_dict(metadata,route_data)
            routes[current_route.guid] = current_route
        self._routes = routes


    def get_app(self,guid):

        self._update_apps()
        if guid in self.apps.keys():
            return self.apps[guid]
        logging.warn("{} not found, returning None".format(guid))
        return None


    def get_app_by_name(self,name):
        self._update_apps()
        for app in self.apps.values():
            if app.name == name:
                return app
        logging.warn("{} not found, returning None".format(name))
        return None


    def get_space_by_name(self,name):
        self._update_spaces()
        for space in self.spaces.values():
            if space.name == name:
                return space
        logging.warn("{} not found, returning None".format(name))
        return None

    def get_domain_by_name(self,name):
        self._update_domains()
        for domain in self.domains.values():
            if domain.name == name:
                return domain
        logging.warn("{} not found, returning None".format(name))
        return None

    def get_route_by_name(self,name):
        self._update_routes()
        for route in self.routes.values():
            if route.host == name:
                return route
        logging.warn("{} not found, returning None".format(name))
        return None

    def create_app(self,name, space):
        """
        Creates an application

        :param name: Name of the application
        :type name: str
        :param space: space in which to create the app
        :type space: CloudFoundrySpace
        :return: The CloudFoundryApp object corresponding to the new app
        :rtype: CloudFoundryApp
        """
        assert isinstance(space,CloudFoundrySpace)
        logging.warn("Creating new app in space {}".format(space.guid))

        if self.get_app_by_name(name) is not None:
            return self.get_app_by_name(name)

        response = self._post_or_exception("v2/apps",data={'name':name, 'space_guid':space.guid})
        metadata = response['metadata']
        app_data = response['entity']
        app = CloudFoundryApp.from_dict(metadata,app_data)
        self._apps[app.guid] = app

        return app

    def delete_app(self,app):
        assert isinstance(app,CloudFoundryApp)
        logging.critical("Deleting App with GUID: {}".format(app.guid))

        self._delete_or_exception("v2/apps/{}".format(app.guid),json=False)
        self._apps.pop(guid,None)


    def upload_bits(self,app,path):
        """
        Uploads the bits for an application, given the local path.  Creates the required zip file

        :param app: The application to which we should upload the bits
        :type app: CloudFoundryApp
        :param path: The local path containing the bits
        :type path: str
        """
        logging.info("Compressing bits in {} for upload to app {}".format(path,app.name))
        assert isinstance(path,(unicode,str,basestring))
        assert isinstance(app, CloudFoundryApp)
        zipdata = create_bits_zip(path)
        files_data = OrderedDict()
        files_data['resources'] = (None,'[]')
        files_data['application'] = zipdata.getvalue()

        #logging.debug(dict(files_data))

        self._put_or_exception("v2/apps/{}/bits".format(app.guid),
                               files=files_data,
                               raw_data = True
                               )

    def start_app(self,app):
        """
        Convinience function to start an app
        :param app: the application to start
        :type app: CloudFoundryApp
        """
        self.update_app(app,{'state':'STARTED'})


    def scale_app(self,app,instances):
        """
        Scale an application.
        :param app: the application to scale
        :param instances: number of instances we want.
        """
        self.update_app(app,{'instances':instances})

    def update_app(self,app,changes):
        """
        Update any specific attribute of an app.
        :param app: The app to update
        :type app: CloudFoundryApp
        :param changes: the changes to make
        :type changes: dict
        """

        logging.info("Updating app {}".format(app.name))
        logging.debug("App changes: {}".format(changes))
        assert isinstance(app, CloudFoundryApp)
        assert isinstance(changes,dict)

        self._put_or_exception("/v2/apps/{}".format(app.guid),data=changes)
        self._update_apps()

    def create_route(self,host,domain,space):
        """
        Create a brand new route
        :param host: The hostname to add
        :type host: str
        :param domain: The domain for the hostname (e.g. cfapps.io)
        :type domain: CloudFoundryDomain
        :param space: The space to which the host should belong
        :type space: CloudFoundrySpace

        """

        logging.info("Adding new route {} to {} in space {}".format(host,domain.name,space.name))
        assert isinstance(host,(str,unicode,basestring))
        assert isinstance(domain,CloudFoundryDomain)
        assert isinstance(space,CloudFoundrySpace)


        new_route_raw = self._post_or_exception("v2/routes",
                               data={
                                    'domain_guid': domain.guid,
                                    'host': host,
                                    'space_guid': space.guid
                               }
                            )

        self._update_routes.delete() #Delete the caches for this function
        return self.get_route_by_name(host)



    def add_route_to_app(self,app,route):
        self._update_apps()
        self._update_routes.delete()
        self._update_routes()
        assert isinstance(app, CloudFoundryApp)
        assert isinstance(route, CloudFoundryRoute)
        logging.info("Adding route {} to app {}".format(route.host,app.name))
        response = self._put_or_exception("v2/apps/{}/routes/{}".format(app.guid,route.guid))
        self._apps[app.guid] = CloudFoundryApp.from_dict(response['metadata'],response['entity'])
        self._update_routes.delete()


    def delete_route_from_app(self,app,route):

        assert isinstance(app,CloudFoundryApp)
        assert isinstance(route,CloudFoundryRoute)
        logging.info("Removing route {} to app {}".format(route.host, app.name))
        response = self._delete_or_exception("v2/apps/{}/routes/{}".format(app.guid,route.guid))
        self._apps[app.guid] = CloudFoundryApp.from_dict(response['metadata'],response['entity'])
        self._update_routes()