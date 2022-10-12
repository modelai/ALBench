# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from src.swagger_models.base_model_ import Model
from src import util


class AssetInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, asset_id: str=None, class_ids: List[int]=None):  # noqa: E501
        """AssetInfo - a model defined in Swagger

        :param asset_id: The asset_id of this AssetInfo.  # noqa: E501
        :type asset_id: str
        :param class_ids: The class_ids of this AssetInfo.  # noqa: E501
        :type class_ids: List[int]
        """
        self.swagger_types = {
            'asset_id': str,
            'class_ids': List[int]
        }

        self.attribute_map = {
            'asset_id': 'asset_id',
            'class_ids': 'class_ids'
        }
        self._asset_id = asset_id
        self._class_ids = class_ids

    @classmethod
    def from_dict(cls, dikt) -> 'AssetInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AssetInfo of this AssetInfo.  # noqa: E501
        :rtype: AssetInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def asset_id(self) -> str:
        """Gets the asset_id of this AssetInfo.


        :return: The asset_id of this AssetInfo.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id: str):
        """Sets the asset_id of this AssetInfo.


        :param asset_id: The asset_id of this AssetInfo.
        :type asset_id: str
        """

        self._asset_id = asset_id

    @property
    def class_ids(self) -> List[int]:
        """Gets the class_ids of this AssetInfo.


        :return: The class_ids of this AssetInfo.
        :rtype: List[int]
        """
        return self._class_ids

    @class_ids.setter
    def class_ids(self, class_ids: List[int]):
        """Sets the class_ids of this AssetInfo.


        :param class_ids: The class_ids of this AssetInfo.
        :type class_ids: List[int]
        """

        self._class_ids = class_ids