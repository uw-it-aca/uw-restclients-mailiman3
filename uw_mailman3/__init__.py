# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0


from commonconf import settings
from uw_mailman3.dao import Mailman3_DAO
from uw_mailman3.exceptions import ListNotFound
from restclients_core.exceptions import DataFailureException
from uw_list_manager.models import List, ListConfig
from base64 import b64encode


class Mailman3:
    def __init__(self):
        self._url_base = settings.get('BASE_VERSION', '3.1')
        self._dao = Mailman3_DAO()

    def _list_full_name(self, list_name):
        return f"{list_name}@{settings.get('DOMAIN_NAME')}"

    def _list_url(self, list_name):
        return f"{self._url_base}/lists/{self._list_full_name(list_name)}"

    def list_admin_url(self, list_id):
        # list_id like: mikes-mm3-test.test.lists.uw.edu
        return (f"https://{settings.get('CLUSTER_NAME')}"
                f"/postorius/lists/{list_id}")

    def _fetch_lists(self, page=1, page_size=500):
        url = f"{self._url_base}/lists"
        return self._dao.get_resource(
            url, {"page": page, "page_size": page_size})

    def get_all_lists(self):
        current_page = 0
        while current_page <= 0:
            lists = self._fetch_lists(page=current_page)
            if not lists:
                break

            for l in lists:
                yield List(data=l)

            current_page += 1

    def get_list_by_name(list_name):
        """
        Query mailman3 server for list_id
        """
        url = self._list_url(list_name)
        return List(data=self._dao.get_resource(url))

    def get_list_config_sub_resource(self, list_name, resource_name):
        url = f"{self._list_url(list_name)}/config/{resource_name}"
        return self._dao.get_resource(url)

    def get_list_config_sub_resource(self, list_name, resource_name, value):
        url = f"{self._list_url(list_name)}/config/{resource_name}"
        data = {resource_name: value}
        return self._dao.patch_resource(url, data)
