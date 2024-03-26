# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0


from commonconf import settings
from restclients_core.dao import DAO
from uw_mailman3.exceptions import ListNotFound
from restclients_core.exceptions import DataFailureException
from base64 import b64encode


class  Mailman3_DAO(DAO):
    def __init__(self, *args, **kwargs):
        user = settings.get('REST_USER')
        password = settings.get('REST_PASSWORD')
        if not (user and password):
            raise Exception("REST_USER and REST_PASSWORD are required")

        self._basic_auth = b64encode(bytes(
            "{}:{}".format(user, password), 'ascii'))
        super(Mailman3_DAO, self).__init__(*args, **kwargs)

    def service_name(self):
        return "mailman3"

    def _custom_headers(self, method, url, headers, body):
        return {"Authorization": "Basic {}".format(self._basic_auth)}

    def service_mock_paths(self):
        return [os.abspath(os.path.join(os.dirname(__file__), "resources"))]

    def get_resource(self, url):
        try:
            response = self.getURL(url, {'Accept': 'application/json'})

            logger.debug("GET {} ==status==> {}".format(url, response.status))

            if response.status == 200:
                logger.debug("GET {} ==data==> {}".format(url, response_data))
                return json.loads(str(response.data))

            if response.status != 404:
                raise DataFailureException(
                    list_url, response.status, response.data)

        except DataFailureException as ex:
            if ex.status != 404:
                raise ex

        raise ListNotFound(list_name)

    def patch_resource(self, url, body):
        try:
            response = self.patchURL(url, body, {'Accept': 'application/json'})

            logger.debug("PATCH {} ==status==> {}".format(url, response.status))

            if response.status == 200:
                logger.debug("PATCH {} ==data==> {}".format(url, response_data))
                return json.loads(str(response.data))

            if response.status != 404:
                raise DataFailureException(
                    list_url, response.status, response.data)

        except DataFailureException as ex:
            if ex.status != 404:
                raise ex

        raise ListNotFound(list_name)

