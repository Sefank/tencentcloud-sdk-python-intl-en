# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AddResourceTagRequest(AbstractModel):
    """AddResourceTag request structure.

    """

    def __init__(self):
        r"""
        :param _TagKey: The tag key that needs to be bound. For the requirements, refer to: https://intl.cloud.tencent.com/document/product/651/13354?from_cn_redirect=1
        :type TagKey: str
        :param _TagValue: The tag value that needs to be bound. For the requirements, refer to: https://intl.cloud.tencent.com/document/product/651/13354?from_cn_redirect=1
        :type TagValue: str
        :param _Resource: Resource to be associated, represented in the standard six-segment resource format. For the correct format, see https://intl.cloud.tencent.com/document/product/651/89122?from_cn_redirect=1
        :type Resource: str
        """
        self._TagKey = None
        self._TagValue = None
        self._Resource = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        self._Resource = params.get("Resource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddResourceTagResponse(AbstractModel):
    """AddResourceTag response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AttachResourcesTagRequest(AbstractModel):
    """AttachResourcesTag request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceType: Service short name, which is the third segment of the six-segment resource format. For more information on the format, see https://intl.cloud.tencent.com/document/product/651/89122?from_cn_redirect=1
        :type ServiceType: str
        :param _ResourceIds: Resource ID array, which can contain up to 50 resources
        :type ResourceIds: list of str
        :param _TagKey: The tag key that needs to be bound. For the requirements, refer to: https://intl.cloud.tencent.com/document/product/651/13354?from_cn_redirect=1
        :type TagKey: str
        :param _TagValue: The tag value that needs to be bound. For the requirements, refer to: https://intl.cloud.tencent.com/document/product/651/13354?from_cn_redirect=1
        :type TagValue: str
        :param _ResourceRegion: Region of the resource. This parameter can be left blank if region is not involved. The region must correspond to resources specified by ResourceIds.N. Once the region is specified, all resources specified by ResourceIds.N must locate in this region. Example: ap-beijing.
        :type ResourceRegion: str
        :param _ResourcePrefix: Resource prefix (the part before "/" in the last segment in the six-segment resource description), which is optional for COS buckets but required for other Tencent Cloud resources.
        :type ResourcePrefix: str
        """
        self._ServiceType = None
        self._ResourceIds = None
        self._TagKey = None
        self._TagValue = None
        self._ResourceRegion = None
        self._ResourcePrefix = None

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def ResourceRegion(self):
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourcePrefix(self):
        return self._ResourcePrefix

    @ResourcePrefix.setter
    def ResourcePrefix(self, ResourcePrefix):
        self._ResourcePrefix = ResourcePrefix


    def _deserialize(self, params):
        self._ServiceType = params.get("ServiceType")
        self._ResourceIds = params.get("ResourceIds")
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ResourcePrefix = params.get("ResourcePrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachResourcesTagResponse(AbstractModel):
    """AttachResourcesTag response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateTagRequest(AbstractModel):
    """CreateTag request structure.

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key.
        :type TagKey: str
        :param _TagValue: Tag value.
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTagResponse(AbstractModel):
    """CreateTag response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateTagsRequest(AbstractModel):
    """CreateTags request structure.

    """

    def __init__(self):
        r"""
        :param _Tags: Tag list.
Value range of N: 0–9
        :type Tags: list of Tag
        """
        self._Tags = None

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTagsResponse(AbstractModel):
    """CreateTags response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteResourceTagRequest(AbstractModel):
    """DeleteResourceTag request structure.

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key.
        :type TagKey: str
        :param _Resource: [Six-segment resource description](https://intl.cloud.tencent.com/document/product/598/10606?from_cn_redirect=1)
        :type Resource: str
        """
        self._TagKey = None
        self._Resource = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._Resource = params.get("Resource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteResourceTagResponse(AbstractModel):
    """DeleteResourceTag response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteTagRequest(AbstractModel):
    """DeleteTag request structure.

    """

    def __init__(self):
        r"""
        :param _TagKey: The tag key to be deleted.
        :type TagKey: str
        :param _TagValue: The tag value to be deleted.
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTagResponse(AbstractModel):
    """DeleteTag response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteTagsRequest(AbstractModel):
    """DeleteTags request structure.

    """

    def __init__(self):
        r"""
        :param _Tags: Tag list.
Value range of N: 0–9
        :type Tags: list of Tag
        """
        self._Tags = None

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTagsResponse(AbstractModel):
    """DeleteTags response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeProjectsRequest(AbstractModel):
    """DescribeProjects request structure.

    """

    def __init__(self):
        r"""
        :param _AllList: If this parameter is 1, all projects (including hidden ones) will be queried. If it is 0, only non-hidden projects will be queried.
        :type AllList: int
        :param _Limit: Number of entries per page. Fixed value: 1,000.
        :type Limit: int
        :param _Offset: Pagination offset.
        :type Offset: int
        """
        self._AllList = None
        self._Limit = None
        self._Offset = None

    @property
    def AllList(self):
        return self._AllList

    @AllList.setter
    def AllList(self, AllList):
        self._AllList = AllList

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._AllList = params.get("AllList")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectsResponse(AbstractModel):
    """DescribeProjects response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of data entries.
        :type Total: int
        :param _Projects: Project list.
        :type Projects: list of Project
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Projects = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Projects(self):
        return self._Projects

    @Projects.setter
    def Projects(self, Projects):
        self._Projects = Projects

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Projects") is not None:
            self._Projects = []
            for item in params.get("Projects"):
                obj = Project()
                obj._deserialize(item)
                self._Projects.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourceTagsByResourceIdsRequest(AbstractModel):
    """DescribeResourceTagsByResourceIds request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceType: Service type.
        :type ServiceType: str
        :param _ResourcePrefix: Resource prefix.
        :type ResourcePrefix: str
        :param _ResourceIds: Array of resource IDs (up to 50)
        :type ResourceIds: list of str
        :param _ResourceRegion: The resource's region.
        :type ResourceRegion: str
        :param _Offset: Data offset. The default value is 0. Must be an integral multiple of the `Limit` parameter.
        :type Offset: int
        :param _Limit: Page size. The default value is 0.
        :type Limit: int
        :param _Category: Tag type. Valid values: Custom: custom tag; System: system tag; All: all tags. Default value: All.
        :type Category: str
        """
        self._ServiceType = None
        self._ResourcePrefix = None
        self._ResourceIds = None
        self._ResourceRegion = None
        self._Offset = None
        self._Limit = None
        self._Category = None

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ResourcePrefix(self):
        return self._ResourcePrefix

    @ResourcePrefix.setter
    def ResourcePrefix(self, ResourcePrefix):
        self._ResourcePrefix = ResourcePrefix

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def ResourceRegion(self):
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category


    def _deserialize(self, params):
        self._ServiceType = params.get("ServiceType")
        self._ResourcePrefix = params.get("ResourcePrefix")
        self._ResourceIds = params.get("ResourceIds")
        self._ResourceRegion = params.get("ResourceRegion")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Category = params.get("Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceTagsByResourceIdsResponse(AbstractModel):
    """DescribeResourceTagsByResourceIds response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of results.
        :type TotalCount: int
        :param _Offset: Data offset.
        :type Offset: int
        :param _Limit: Page size.
        :type Limit: int
        :param _Tags: Tag list.
        :type Tags: list of TagResource
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Offset = None
        self._Limit = None
        self._Tags = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagResource()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourceTagsByResourceIdsSeqRequest(AbstractModel):
    """DescribeResourceTagsByResourceIdsSeq request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceType: Service type
        :type ServiceType: str
        :param _ResourcePrefix: Resource prefix
        :type ResourcePrefix: str
        :param _ResourceIds: Unique resource ID
        :type ResourceIds: list of str
        :param _ResourceRegion: Resource region
        :type ResourceRegion: str
        :param _Offset: Data offset. Default value: 0. It must be an integer multiple of the `Limit` parameter
        :type Offset: int
        :param _Limit: Number of entries per page. Default value: 15
        :type Limit: int
        """
        self._ServiceType = None
        self._ResourcePrefix = None
        self._ResourceIds = None
        self._ResourceRegion = None
        self._Offset = None
        self._Limit = None

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ResourcePrefix(self):
        return self._ResourcePrefix

    @ResourcePrefix.setter
    def ResourcePrefix(self, ResourcePrefix):
        self._ResourcePrefix = ResourcePrefix

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def ResourceRegion(self):
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ServiceType = params.get("ServiceType")
        self._ResourcePrefix = params.get("ResourcePrefix")
        self._ResourceIds = params.get("ResourceIds")
        self._ResourceRegion = params.get("ResourceRegion")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceTagsByResourceIdsSeqResponse(AbstractModel):
    """DescribeResourceTagsByResourceIdsSeq response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of results
        :type TotalCount: int
        :param _Offset: Data offset
        :type Offset: int
        :param _Limit: Number of entries per page
        :type Limit: int
        :param _Tags: Tag list
        :type Tags: list of TagResource
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Offset = None
        self._Limit = None
        self._Tags = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagResource()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourceTagsByTagKeysRequest(AbstractModel):
    """DescribeResourceTagsByTagKeys request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceType: Service type
        :type ServiceType: str
        :param _ResourcePrefix: Resource prefix
        :type ResourcePrefix: str
        :param _ResourceRegion: Resource region
        :type ResourceRegion: str
        :param _ResourceIds: List of unique resource IDs, which can contain no more than 20 IDs.
        :type ResourceIds: list of str
        :param _TagKeys: List of resource tag keys, which can contain no more than 20 keys.
        :type TagKeys: list of str
        :param _Limit: Number of entries per page. Default value: 400
        :type Limit: int
        :param _Offset: Data offset. Default value: 0. It must be an integer multiple of the `Limit` parameter
        :type Offset: int
        """
        self._ServiceType = None
        self._ResourcePrefix = None
        self._ResourceRegion = None
        self._ResourceIds = None
        self._TagKeys = None
        self._Limit = None
        self._Offset = None

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ResourcePrefix(self):
        return self._ResourcePrefix

    @ResourcePrefix.setter
    def ResourcePrefix(self, ResourcePrefix):
        self._ResourcePrefix = ResourcePrefix

    @property
    def ResourceRegion(self):
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ServiceType = params.get("ServiceType")
        self._ResourcePrefix = params.get("ResourcePrefix")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ResourceIds = params.get("ResourceIds")
        self._TagKeys = params.get("TagKeys")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceTagsByTagKeysResponse(AbstractModel):
    """DescribeResourceTagsByTagKeys response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of results
        :type TotalCount: int
        :param _Offset: Data offset
        :type Offset: int
        :param _Limit: Number of entries per page
        :type Limit: int
        :param _Rows: Resource tag
        :type Rows: list of ResourceIdTag
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Offset = None
        self._Limit = None
        self._Rows = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Rows(self):
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = ResourceIdTag()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourceTagsRequest(AbstractModel):
    """DescribeResourceTags request structure.

    """

    def __init__(self):
        r"""
        :param _CreateUin: Creator `uin`
        :type CreateUin: int
        :param _ResourceRegion: Resource region.
        :type ResourceRegion: str
        :param _ServiceType: Service type.
        :type ServiceType: str
        :param _ResourcePrefix: Resource prefix
        :type ResourcePrefix: str
        :param _ResourceId: Unique resource ID. Queries with `ResourceId` only may be slow or fail to return results. We recommend you also enter `ServiceType`, `ResourcePrefix`, and `ResourceRegion` (which can be ignored for resources that don't have the region attribute) when entering `ResourceId`.
        :type ResourceId: str
        :param _Offset: Data offset. Default value: 0. It must be an integer multiple of the `Limit` parameter
        :type Offset: int
        :param _Limit: Number of entries per page. Default value: 15
        :type Limit: int
        :param _CosResourceId: Whether it is a COS resource (0 or 1). This parameter is required when the entered `ResourceId` is a COS resource.
        :type CosResourceId: int
        """
        self._CreateUin = None
        self._ResourceRegion = None
        self._ServiceType = None
        self._ResourcePrefix = None
        self._ResourceId = None
        self._Offset = None
        self._Limit = None
        self._CosResourceId = None

    @property
    def CreateUin(self):
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def ResourceRegion(self):
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ResourcePrefix(self):
        return self._ResourcePrefix

    @ResourcePrefix.setter
    def ResourcePrefix(self, ResourcePrefix):
        self._ResourcePrefix = ResourcePrefix

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def CosResourceId(self):
        return self._CosResourceId

    @CosResourceId.setter
    def CosResourceId(self, CosResourceId):
        self._CosResourceId = CosResourceId


    def _deserialize(self, params):
        self._CreateUin = params.get("CreateUin")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ServiceType = params.get("ServiceType")
        self._ResourcePrefix = params.get("ResourcePrefix")
        self._ResourceId = params.get("ResourceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._CosResourceId = params.get("CosResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceTagsResponse(AbstractModel):
    """DescribeResourceTags response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of results
        :type TotalCount: int
        :param _Offset: Data offset.
        :type Offset: int
        :param _Limit: Number of entries per page.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Limit: int
        :param _Rows: Resource tag
        :type Rows: list of TagResource
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Offset = None
        self._Limit = None
        self._Rows = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Rows(self):
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = TagResource()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourcesByTagsRequest(AbstractModel):
    """DescribeResourcesByTags request structure.

    """

    def __init__(self):
        r"""
        :param _TagFilters: Tag filtering arrays.
        :type TagFilters: list of TagFilter
        :param _CreateUin: Tag creator uin.
        :type CreateUin: int
        :param _Offset: Data offset. The default value is 0. Must be an integral multiple of the `Limit` parameter.
        :type Offset: int
        :param _Limit: Page size. The default value is 15.
        :type Limit: int
        :param _ResourcePrefix: Resource prefix.
        :type ResourcePrefix: str
        :param _ResourceId: Unique resource ID.
        :type ResourceId: str
        :param _ResourceRegion: The resource's region.
        :type ResourceRegion: str
        :param _ServiceType: Service type.
        :type ServiceType: str
        """
        self._TagFilters = None
        self._CreateUin = None
        self._Offset = None
        self._Limit = None
        self._ResourcePrefix = None
        self._ResourceId = None
        self._ResourceRegion = None
        self._ServiceType = None

    @property
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

    @property
    def CreateUin(self):
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ResourcePrefix(self):
        return self._ResourcePrefix

    @ResourcePrefix.setter
    def ResourcePrefix(self, ResourcePrefix):
        self._ResourcePrefix = ResourcePrefix

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceRegion(self):
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType


    def _deserialize(self, params):
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        self._CreateUin = params.get("CreateUin")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ResourcePrefix = params.get("ResourcePrefix")
        self._ResourceId = params.get("ResourceId")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ServiceType = params.get("ServiceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcesByTagsResponse(AbstractModel):
    """DescribeResourcesByTags response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of results.
        :type TotalCount: int
        :param _Offset: Data offset.
        :type Offset: int
        :param _Limit: Number of entries per page.
Note: This field may return null, indicating that no valid value is found.
        :type Limit: int
        :param _Rows: Resource tag.
        :type Rows: list of ResourceTag
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Offset = None
        self._Limit = None
        self._Rows = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Rows(self):
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourcesByTagsUnionRequest(AbstractModel):
    """DescribeResourcesByTagsUnion request structure.

    """

    def __init__(self):
        r"""
        :param _TagFilters: Tag filtering arrays.
        :type TagFilters: list of TagFilter
        :param _CreateUin: Tag creator uin.
        :type CreateUin: int
        :param _Offset: Data offset. The default value is 0. Must be an integral multiple of the `Limit` parameter.
        :type Offset: int
        :param _Limit: Page size. The default value is 15.
        :type Limit: int
        :param _ResourcePrefix: Resource prefix.
        :type ResourcePrefix: str
        :param _ResourceId: Unique resource ID.
        :type ResourceId: str
        :param _ResourceRegion: The resource’s region.
        :type ResourceRegion: str
        :param _ServiceType: Service type
        :type ServiceType: str
        """
        self._TagFilters = None
        self._CreateUin = None
        self._Offset = None
        self._Limit = None
        self._ResourcePrefix = None
        self._ResourceId = None
        self._ResourceRegion = None
        self._ServiceType = None

    @property
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

    @property
    def CreateUin(self):
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ResourcePrefix(self):
        return self._ResourcePrefix

    @ResourcePrefix.setter
    def ResourcePrefix(self, ResourcePrefix):
        self._ResourcePrefix = ResourcePrefix

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceRegion(self):
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType


    def _deserialize(self, params):
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        self._CreateUin = params.get("CreateUin")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ResourcePrefix = params.get("ResourcePrefix")
        self._ResourceId = params.get("ResourceId")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ServiceType = params.get("ServiceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcesByTagsUnionResponse(AbstractModel):
    """DescribeResourcesByTagsUnion response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of results.
        :type TotalCount: int
        :param _Offset: Data offset.
        :type Offset: int
        :param _Limit: The size of each page.
        :type Limit: int
        :param _Rows: Resource tag.
        :type Rows: list of ResourceTag
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Offset = None
        self._Limit = None
        self._Rows = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Rows(self):
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTagKeysRequest(AbstractModel):
    """DescribeTagKeys request structure.

    """

    def __init__(self):
        r"""
        :param _CreateUin: Creator `Uin`. If not specified, `Uin` is only used as the query condition.
        :type CreateUin: int
        :param _Offset: Data offset. The default value is 0. Must be an integral multiple of the `Limit` parameter.
        :type Offset: int
        :param _Limit: Number of entries per page. Default: 15; maximum: 1,000.
        :type Limit: int
        :param _ShowProject: Whether to show project
        :type ShowProject: int
        :param _Category: Tag type. Valid values: Custom: custom tag; System: system tag; All: all tags. Default value: All.
        :type Category: str
        """
        self._CreateUin = None
        self._Offset = None
        self._Limit = None
        self._ShowProject = None
        self._Category = None

    @property
    def CreateUin(self):
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ShowProject(self):
        return self._ShowProject

    @ShowProject.setter
    def ShowProject(self, ShowProject):
        self._ShowProject = ShowProject

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category


    def _deserialize(self, params):
        self._CreateUin = params.get("CreateUin")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ShowProject = params.get("ShowProject")
        self._Category = params.get("Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagKeysResponse(AbstractModel):
    """DescribeTagKeys response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of results.
        :type TotalCount: int
        :param _Offset: Data offset.
        :type Offset: int
        :param _Limit: Page size.
        :type Limit: int
        :param _Tags: Tag list.
        :type Tags: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Offset = None
        self._Limit = None
        self._Tags = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Tags = params.get("Tags")
        self._RequestId = params.get("RequestId")


class DescribeTagValuesRequest(AbstractModel):
    """DescribeTagValues request structure.

    """

    def __init__(self):
        r"""
        :param _TagKeys: Tag key list.
        :type TagKeys: list of str
        :param _CreateUin: Creator `Uin`. If not specified, `Uin` is only used as the query condition.
        :type CreateUin: int
        :param _Offset: Data offset. The default value is 0. Must be an integral multiple of the `Limit` parameter.
        :type Offset: int
        :param _Limit: Page size. The default value is 0.
        :type Limit: int
        :param _Category: Tag type. Valid values: Custom: custom tag; System: system tag; All: all tags. Default value: All.
        :type Category: str
        """
        self._TagKeys = None
        self._CreateUin = None
        self._Offset = None
        self._Limit = None
        self._Category = None

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def CreateUin(self):
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category


    def _deserialize(self, params):
        self._TagKeys = params.get("TagKeys")
        self._CreateUin = params.get("CreateUin")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Category = params.get("Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagValuesResponse(AbstractModel):
    """DescribeTagValues response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of results.
        :type TotalCount: int
        :param _Offset: Data offset.
        :type Offset: int
        :param _Limit: Page size.
        :type Limit: int
        :param _Tags: Tag list.
        :type Tags: list of Tag
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Offset = None
        self._Limit = None
        self._Tags = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTagValuesSeqRequest(AbstractModel):
    """DescribeTagValuesSeq request structure.

    """

    def __init__(self):
        r"""
        :param _TagKeys: Tag key list
        :type TagKeys: list of str
        :param _CreateUin: Creator `Uin`. If this parameter is blank or left empty, only `Uin` will be used as a condition for query
        :type CreateUin: int
        :param _Offset: Data offset. Default value: 0. It must be an integer multiple of the `Limit` parameter
        :type Offset: int
        :param _Limit: Number of entries per page. Default value: 15
        :type Limit: int
        """
        self._TagKeys = None
        self._CreateUin = None
        self._Offset = None
        self._Limit = None

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def CreateUin(self):
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._TagKeys = params.get("TagKeys")
        self._CreateUin = params.get("CreateUin")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagValuesSeqResponse(AbstractModel):
    """DescribeTagValuesSeq response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of results
        :type TotalCount: int
        :param _Offset: Data offset
        :type Offset: int
        :param _Limit: Number of entries per page
        :type Limit: int
        :param _Tags: Tag list
        :type Tags: list of Tag
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Offset = None
        self._Limit = None
        self._Tags = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTagsRequest(AbstractModel):
    """DescribeTags request structure.

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key. Either exists or does not exist alongside the tag value. If it does not exist, all of the user's tags will be queried.
        :type TagKey: str
        :param _TagValue: Tag value. Either exists or does not exist alongside the tag key. If it does not exist, all of the user's tags will be queried.
        :type TagValue: str
        :param _Offset: Data offset. The default value is 0. Must be an integral multiple of the `Limit` parameter.
        :type Offset: int
        :param _Limit: Page size. The default value is 0.
        :type Limit: int
        :param _CreateUin: Creator `Uin`. If not specified, `Uin` is only used as the query condition.
        :type CreateUin: int
        :param _TagKeys: Tag key array, which either exists or does not exist with the tag value. If it does not exist, all tags of the user will be queried. If it is passed in together with `TagKey`, it will be used and the `TagKey` will be ignored.
        :type TagKeys: list of str
        :param _ShowProject: Whether to show project tag
        :type ShowProject: int
        """
        self._TagKey = None
        self._TagValue = None
        self._Offset = None
        self._Limit = None
        self._CreateUin = None
        self._TagKeys = None
        self._ShowProject = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def CreateUin(self):
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def ShowProject(self):
        return self._ShowProject

    @ShowProject.setter
    def ShowProject(self, ShowProject):
        self._ShowProject = ShowProject


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._CreateUin = params.get("CreateUin")
        self._TagKeys = params.get("TagKeys")
        self._ShowProject = params.get("ShowProject")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagsResponse(AbstractModel):
    """DescribeTags response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of results.
        :type TotalCount: int
        :param _Offset: Data offset.
        :type Offset: int
        :param _Limit: Page size.
        :type Limit: int
        :param _Tags: Tag list.
        :type Tags: list of TagWithDelete
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Offset = None
        self._Limit = None
        self._Tags = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagWithDelete()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTagsSeqRequest(AbstractModel):
    """DescribeTagsSeq request structure.

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key, which either exists or does not exist with the tag value. If it does not exist, all tags of the user will be queried
        :type TagKey: str
        :param _TagValue: Tag value, which either exists or does not exist with the tag key. If it does not exist, all tags of the user will be queried
        :type TagValue: str
        :param _Offset: Data offset. Default value: 0. It must be an integer multiple of the `Limit` parameter
        :type Offset: int
        :param _Limit: Number of entries per page. Default value: 15
        :type Limit: int
        :param _CreateUin: Creator `Uin`. If this parameter is blank or left empty, only `Uin` will be used as a condition for query
        :type CreateUin: int
        :param _TagKeys: Tag key array, which either exists or does not exist with the tag value. If it does not exist, all tags of the user will be queried. If it is passed in together with `TagKey`, it will be used and the `TagKey` will be ignored.
        :type TagKeys: list of str
        :param _ShowProject: Whether to show project tag
        :type ShowProject: int
        """
        self._TagKey = None
        self._TagValue = None
        self._Offset = None
        self._Limit = None
        self._CreateUin = None
        self._TagKeys = None
        self._ShowProject = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def CreateUin(self):
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def ShowProject(self):
        return self._ShowProject

    @ShowProject.setter
    def ShowProject(self, ShowProject):
        self._ShowProject = ShowProject


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._CreateUin = params.get("CreateUin")
        self._TagKeys = params.get("TagKeys")
        self._ShowProject = params.get("ShowProject")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagsSeqResponse(AbstractModel):
    """DescribeTagsSeq response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of results
        :type TotalCount: int
        :param _Offset: Data offset
        :type Offset: int
        :param _Limit: Number of entries per page
        :type Limit: int
        :param _Tags: Tag list
        :type Tags: list of TagWithDelete
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Offset = None
        self._Limit = None
        self._Tags = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagWithDelete()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DetachResourcesTagRequest(AbstractModel):
    """DetachResourcesTag request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceType: Resource service name (the third segment in the six-segment resource description)
        :type ServiceType: str
        :param _ResourceIds: Resource ID array, which can contain up to 50 resources
        :type ResourceIds: list of str
        :param _TagKey: Tag key to be unbound
        :type TagKey: str
        :param _ResourceRegion: Resource region. If resources have the region attribute, this field is required; otherwise, it is optional.
        :type ResourceRegion: str
        :param _ResourcePrefix: Resource prefix (the part before "/" in the last segment in the six-segment resource description), which is optional for COS buckets but required for other Tencent Cloud resources.
        :type ResourcePrefix: str
        """
        self._ServiceType = None
        self._ResourceIds = None
        self._TagKey = None
        self._ResourceRegion = None
        self._ResourcePrefix = None

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def ResourceRegion(self):
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourcePrefix(self):
        return self._ResourcePrefix

    @ResourcePrefix.setter
    def ResourcePrefix(self, ResourcePrefix):
        self._ResourcePrefix = ResourcePrefix


    def _deserialize(self, params):
        self._ServiceType = params.get("ServiceType")
        self._ResourceIds = params.get("ResourceIds")
        self._TagKey = params.get("TagKey")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ResourcePrefix = params.get("ResourcePrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachResourcesTagResponse(AbstractModel):
    """DetachResourcesTag response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class FailedResource(AbstractModel):
    """Information of failed resources.
    This is returned when resource tag binding or unbinding fails.

    """

    def __init__(self):
        r"""
        :param _Resource: Six-segment descriptions of failed resources
        :type Resource: str
        :param _Code: Error code
        :type Code: str
        :param _Message: Error message
        :type Message: str
        """
        self._Resource = None
        self._Code = None
        self._Message = None

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetResourcesRequest(AbstractModel):
    """GetResources request structure.

    """

    def __init__(self):
        r"""
        :param _ResourceList: Six-segment resource description list. Tencent Cloud uses a six-segment value to describe a resource.
For example, ResourceList.1 = qcs::${ServiceType}:${Region}:${Account}:${ResourcePreifx}/${ResourceId}.
If this parameter is passed in, the list of all matching resources will be returned, and the specified `MaxResults` will become invalid.
Value range of N: 0–9
        :type ResourceList: list of str
        :param _TagFilters: Tag key and value.
If multiple tags are specified, resources bound to all such tags will be queried.
Value range of N: 0–5
There can be up to 10 `TagValues` in each `TagFilters`.
        :type TagFilters: list of TagFilter
        :param _PaginationToken: The token value of the next page obtained from the response of the previous page.
Leave it empty for the first request.
        :type PaginationToken: str
        :param _MaxResults: Number of data entries to return per page (up to 200).
Default value: 50.
        :type MaxResults: int
        """
        self._ResourceList = None
        self._TagFilters = None
        self._PaginationToken = None
        self._MaxResults = None

    @property
    def ResourceList(self):
        return self._ResourceList

    @ResourceList.setter
    def ResourceList(self, ResourceList):
        self._ResourceList = ResourceList

    @property
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

    @property
    def PaginationToken(self):
        return self._PaginationToken

    @PaginationToken.setter
    def PaginationToken(self, PaginationToken):
        self._PaginationToken = PaginationToken

    @property
    def MaxResults(self):
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults


    def _deserialize(self, params):
        self._ResourceList = params.get("ResourceList")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        self._PaginationToken = params.get("PaginationToken")
        self._MaxResults = params.get("MaxResults")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetResourcesResponse(AbstractModel):
    """GetResources response structure.

    """

    def __init__(self):
        r"""
        :param _PaginationToken: Token value obtained for the next page
        :type PaginationToken: str
        :param _ResourceTagMappingList: List of resources and their associated tags (key-value pairs)
        :type ResourceTagMappingList: list of ResourceTagMapping
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PaginationToken = None
        self._ResourceTagMappingList = None
        self._RequestId = None

    @property
    def PaginationToken(self):
        return self._PaginationToken

    @PaginationToken.setter
    def PaginationToken(self, PaginationToken):
        self._PaginationToken = PaginationToken

    @property
    def ResourceTagMappingList(self):
        return self._ResourceTagMappingList

    @ResourceTagMappingList.setter
    def ResourceTagMappingList(self, ResourceTagMappingList):
        self._ResourceTagMappingList = ResourceTagMappingList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PaginationToken = params.get("PaginationToken")
        if params.get("ResourceTagMappingList") is not None:
            self._ResourceTagMappingList = []
            for item in params.get("ResourceTagMappingList"):
                obj = ResourceTagMapping()
                obj._deserialize(item)
                self._ResourceTagMappingList.append(obj)
        self._RequestId = params.get("RequestId")


class GetTagKeysRequest(AbstractModel):
    """GetTagKeys request structure.

    """

    def __init__(self):
        r"""
        :param _PaginationToken: The token value of the next page obtained from the response of the previous page.
Leave it empty for the first request.
        :type PaginationToken: str
        :param _MaxResults: Number of data entries to return per page (up to 1,000).
Default value: 50.
        :type MaxResults: int
        :param _Category: Tag type. Valid values: Custom: custom tag; System: system tag; All: all tags. Default value: All.
        :type Category: str
        """
        self._PaginationToken = None
        self._MaxResults = None
        self._Category = None

    @property
    def PaginationToken(self):
        return self._PaginationToken

    @PaginationToken.setter
    def PaginationToken(self, PaginationToken):
        self._PaginationToken = PaginationToken

    @property
    def MaxResults(self):
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category


    def _deserialize(self, params):
        self._PaginationToken = params.get("PaginationToken")
        self._MaxResults = params.get("MaxResults")
        self._Category = params.get("Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTagKeysResponse(AbstractModel):
    """GetTagKeys response structure.

    """

    def __init__(self):
        r"""
        :param _PaginationToken: Token value obtained for the next page
        :type PaginationToken: str
        :param _TagKeys: Tag key information.
        :type TagKeys: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PaginationToken = None
        self._TagKeys = None
        self._RequestId = None

    @property
    def PaginationToken(self):
        return self._PaginationToken

    @PaginationToken.setter
    def PaginationToken(self, PaginationToken):
        self._PaginationToken = PaginationToken

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PaginationToken = params.get("PaginationToken")
        self._TagKeys = params.get("TagKeys")
        self._RequestId = params.get("RequestId")


class GetTagValuesRequest(AbstractModel):
    """GetTagValues request structure.

    """

    def __init__(self):
        r"""
        :param _TagKeys: Tag key.
All tag values corresponding to the list of tag keys.
Maximum length: 20
        :type TagKeys: list of str
        :param _PaginationToken: The token value of the next page obtained from the response of the previous page.
Leave it empty for the first request.
        :type PaginationToken: str
        :param _MaxResults: Number of data entries to return per page (up to 1,000).
Default value: 50.
        :type MaxResults: int
        :param _Category: Tag type. Valid values: Custom: custom tag; System: system tag; All: all tags. Default value: All.
        :type Category: str
        """
        self._TagKeys = None
        self._PaginationToken = None
        self._MaxResults = None
        self._Category = None

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def PaginationToken(self):
        return self._PaginationToken

    @PaginationToken.setter
    def PaginationToken(self, PaginationToken):
        self._PaginationToken = PaginationToken

    @property
    def MaxResults(self):
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category


    def _deserialize(self, params):
        self._TagKeys = params.get("TagKeys")
        self._PaginationToken = params.get("PaginationToken")
        self._MaxResults = params.get("MaxResults")
        self._Category = params.get("Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTagValuesResponse(AbstractModel):
    """GetTagValues response structure.

    """

    def __init__(self):
        r"""
        :param _PaginationToken: Token value obtained for the next page
        :type PaginationToken: str
        :param _Tags: Tag list.
        :type Tags: list of Tag
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PaginationToken = None
        self._Tags = None
        self._RequestId = None

    @property
    def PaginationToken(self):
        return self._PaginationToken

    @PaginationToken.setter
    def PaginationToken(self, PaginationToken):
        self._PaginationToken = PaginationToken

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PaginationToken = params.get("PaginationToken")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class GetTagsRequest(AbstractModel):
    """GetTags request structure.

    """

    def __init__(self):
        r"""
        :param _PaginationToken: The token value of the next page obtained from the response of the previous page.
Leave it empty for the first request.
        :type PaginationToken: str
        :param _MaxResults: Number of data entries to return per page (up to 1,000).
Default value: 50.
        :type MaxResults: int
        :param _TagKeys: Tag key.
All tags corresponding to the list of tag keys.
Maximum length: 20
        :type TagKeys: list of str
        :param _Category: Tag type. Valid values: Custom: custom tag; System: system tag; All: all tags. Default value: All.
        :type Category: str
        """
        self._PaginationToken = None
        self._MaxResults = None
        self._TagKeys = None
        self._Category = None

    @property
    def PaginationToken(self):
        return self._PaginationToken

    @PaginationToken.setter
    def PaginationToken(self, PaginationToken):
        self._PaginationToken = PaginationToken

    @property
    def MaxResults(self):
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category


    def _deserialize(self, params):
        self._PaginationToken = params.get("PaginationToken")
        self._MaxResults = params.get("MaxResults")
        self._TagKeys = params.get("TagKeys")
        self._Category = params.get("Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTagsResponse(AbstractModel):
    """GetTags response structure.

    """

    def __init__(self):
        r"""
        :param _PaginationToken: Token value obtained for the next page
        :type PaginationToken: str
        :param _Tags: Tag list.
        :type Tags: list of Tag
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PaginationToken = None
        self._Tags = None
        self._RequestId = None

    @property
    def PaginationToken(self):
        return self._PaginationToken

    @PaginationToken.setter
    def PaginationToken(self, PaginationToken):
        self._PaginationToken = PaginationToken

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PaginationToken = params.get("PaginationToken")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyResourceTagsRequest(AbstractModel):
    """ModifyResourceTags request structure.

    """

    def __init__(self):
        r"""
        :param _Resource: [Six-segment resource description](https://intl.cloud.tencent.com/document/product/598/10606?from_cn_redirect=1)
        :type Resource: str
        :param _ReplaceTags: The tags to be added or modified. If the resource described by `Resource` is not associated with the input tag keys, an association will be added. If the tag keys are already associated, the values corresponding to the associated tag keys will be modified to the input values. This API must contain either `ReplaceTags` or `DeleteTag`, and these two parameters cannot include the same tag keys. This parameter can be omitted, but it cannot be an empty array.
        :type ReplaceTags: list of Tag
        :param _DeleteTags: The tags to be disassociated. This API must contain either `ReplaceTags` or `DeleteTag`, and these two parameters cannot include the same tag keys. This parameter can be omitted, but it cannot be an empty array.
        :type DeleteTags: list of TagKeyObject
        """
        self._Resource = None
        self._ReplaceTags = None
        self._DeleteTags = None

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def ReplaceTags(self):
        return self._ReplaceTags

    @ReplaceTags.setter
    def ReplaceTags(self, ReplaceTags):
        self._ReplaceTags = ReplaceTags

    @property
    def DeleteTags(self):
        return self._DeleteTags

    @DeleteTags.setter
    def DeleteTags(self, DeleteTags):
        self._DeleteTags = DeleteTags


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        if params.get("ReplaceTags") is not None:
            self._ReplaceTags = []
            for item in params.get("ReplaceTags"):
                obj = Tag()
                obj._deserialize(item)
                self._ReplaceTags.append(obj)
        if params.get("DeleteTags") is not None:
            self._DeleteTags = []
            for item in params.get("DeleteTags"):
                obj = TagKeyObject()
                obj._deserialize(item)
                self._DeleteTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourceTagsResponse(AbstractModel):
    """ModifyResourceTags response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyResourcesTagValueRequest(AbstractModel):
    """ModifyResourcesTagValue request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceType: Resource service name (the third segment in the six-segment resource description)
        :type ServiceType: str
        :param _ResourceIds: Resource ID array, which can contain up to 50 resources
        :type ResourceIds: list of str
        :param _TagKey: Tag key
        :type TagKey: str
        :param _TagValue: Tag value
        :type TagValue: str
        :param _ResourceRegion: Resource region. If resources have the region attribute, this field is required; otherwise, it is optional.
        :type ResourceRegion: str
        :param _ResourcePrefix: Resource prefix (the part before "/" in the last segment in the six-segment resource description), which is optional for COS buckets but required for other Tencent Cloud resources.
        :type ResourcePrefix: str
        """
        self._ServiceType = None
        self._ResourceIds = None
        self._TagKey = None
        self._TagValue = None
        self._ResourceRegion = None
        self._ResourcePrefix = None

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def ResourceRegion(self):
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourcePrefix(self):
        return self._ResourcePrefix

    @ResourcePrefix.setter
    def ResourcePrefix(self, ResourcePrefix):
        self._ResourcePrefix = ResourcePrefix


    def _deserialize(self, params):
        self._ServiceType = params.get("ServiceType")
        self._ResourceIds = params.get("ResourceIds")
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ResourcePrefix = params.get("ResourcePrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourcesTagValueResponse(AbstractModel):
    """ModifyResourcesTagValue response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Project(AbstractModel):
    """Project information.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: int
        :param _ProjectName: Project name.
        :type ProjectName: str
        :param _CreatorUin: Creator UIN.
        :type CreatorUin: int
        :param _ProjectInfo: Project description.
        :type ProjectInfo: str
        :param _CreateTime: Creation time.
        :type CreateTime: str
        """
        self._ProjectId = None
        self._ProjectName = None
        self._CreatorUin = None
        self._ProjectInfo = None
        self._CreateTime = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def CreatorUin(self):
        return self._CreatorUin

    @CreatorUin.setter
    def CreatorUin(self, CreatorUin):
        self._CreatorUin = CreatorUin

    @property
    def ProjectInfo(self):
        return self._ProjectInfo

    @ProjectInfo.setter
    def ProjectInfo(self, ProjectInfo):
        self._ProjectInfo = ProjectInfo

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._CreatorUin = params.get("CreatorUin")
        self._ProjectInfo = params.get("ProjectInfo")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceIdTag(AbstractModel):
    """Resource tag key value

    """

    def __init__(self):
        r"""
        :param _ResourceId: Unique resource ID
Note: this field may return null, indicating that no valid values can be obtained
        :type ResourceId: str
        :param _TagKeyValues: Tag key-value pair
Note: this field may return null, indicating that no valid values can be obtained
        :type TagKeyValues: list of Tag
        """
        self._ResourceId = None
        self._TagKeyValues = None

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def TagKeyValues(self):
        return self._TagKeyValues

    @TagKeyValues.setter
    def TagKeyValues(self, TagKeyValues):
        self._TagKeyValues = TagKeyValues


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        if params.get("TagKeyValues") is not None:
            self._TagKeyValues = []
            for item in params.get("TagKeyValues"):
                obj = Tag()
                obj._deserialize(item)
                self._TagKeyValues.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceTag(AbstractModel):
    """Resource tag.

    """

    def __init__(self):
        r"""
        :param _ResourceRegion: The resource's region.
Note: This field may return null, indicating that no valid value is found.
        :type ResourceRegion: str
        :param _ServiceType: Service type.
Note: This field may return null, indicating that no valid value is found.
        :type ServiceType: str
        :param _ResourcePrefix: Resource prefix.
Note: This field may return null, indicating that no valid value is found.
        :type ResourcePrefix: str
        :param _ResourceId: Unique resource ID.
Note: This field may return null, indicating that no valid value is found.
        :type ResourceId: str
        :param _Tags: Resource tag.
Note: This field may return null, indicating that no valid value is found.
        :type Tags: list of Tag
        """
        self._ResourceRegion = None
        self._ServiceType = None
        self._ResourcePrefix = None
        self._ResourceId = None
        self._Tags = None

    @property
    def ResourceRegion(self):
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ResourcePrefix(self):
        return self._ResourcePrefix

    @ResourcePrefix.setter
    def ResourcePrefix(self, ResourcePrefix):
        self._ResourcePrefix = ResourcePrefix

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ResourceRegion = params.get("ResourceRegion")
        self._ServiceType = params.get("ServiceType")
        self._ResourcePrefix = params.get("ResourcePrefix")
        self._ResourceId = params.get("ResourceId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceTagMapping(AbstractModel):
    """Resources and their associated tags (key-value pairs).

    """

    def __init__(self):
        r"""
        :param _Resource: Six-segment resource description. Tencent Cloud uses a six-segment value to describe a resource.
For example, ResourceList.1 = qcs::${ServiceType}:${Region}:${Account}:${ResourcePreifx}/${ResourceId}.
        :type Resource: str
        :param _Tags: List of tags associated with the resource
        :type Tags: list of Tag
        """
        self._Resource = None
        self._Tags = None

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """A tag key-value pair.

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key.
        :type TagKey: str
        :param _TagValue: Tag value.
        :type TagValue: str
        :param _Category: Tag type. Valid values: Custom: custom tag; System: system tag; All: all tags. Default value: All.Note: This field may return null, indicating that no value is obtained.
        :type Category: str
        """
        self._TagKey = None
        self._TagValue = None
        self._Category = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        self._Category = params.get("Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagFilter(AbstractModel):
    """Tag filtering array. '**AND**' relation if multiple arrays.

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key.
        :type TagKey: str
        :param _TagValue: Tag value array. '**OR**' relation if multiple values.
        :type TagValue: list of str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagKeyObject(AbstractModel):
    """Tag key object.

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key.
        :type TagKey: str
        """
        self._TagKey = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagResource(AbstractModel):
    """Tag key-value pair and resource ID.

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key.
        :type TagKey: str
        :param _TagValue: Tag value.
        :type TagValue: str
        :param _ResourceId: Resource ID.
        :type ResourceId: str
        :param _TagKeyMd5: Tag key MD5 value.
        :type TagKeyMd5: str
        :param _TagValueMd5: Tag value MD5 value.
        :type TagValueMd5: str
        :param _ServiceType: Resource type
Note: this field may return null, indicating that no valid values found.
        :type ServiceType: str
        :param _Category: Tag type. Valid values: Custom: custom tag; System: system tag.Note: This field may return null, indicating that no value is obtained.
        :type Category: str
        """
        self._TagKey = None
        self._TagValue = None
        self._ResourceId = None
        self._TagKeyMd5 = None
        self._TagValueMd5 = None
        self._ServiceType = None
        self._Category = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def TagKeyMd5(self):
        return self._TagKeyMd5

    @TagKeyMd5.setter
    def TagKeyMd5(self, TagKeyMd5):
        self._TagKeyMd5 = TagKeyMd5

    @property
    def TagValueMd5(self):
        return self._TagValueMd5

    @TagValueMd5.setter
    def TagValueMd5(self, TagValueMd5):
        self._TagValueMd5 = TagValueMd5

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        self._ResourceId = params.get("ResourceId")
        self._TagKeyMd5 = params.get("TagKeyMd5")
        self._TagValueMd5 = params.get("TagValueMd5")
        self._ServiceType = params.get("ServiceType")
        self._Category = params.get("Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagResourcesRequest(AbstractModel):
    """TagResources request structure.

    """

    def __init__(self):
        r"""
        :param _ResourceList: Cloud resource to be bound, represented in the standard six-segment resource format. For the correct format, see [Resource Description Method](https://intl.cloud.tencent.com/document/product/598/10606?from_cn_redirect=1).
Value range of N: 0-9.
        :type ResourceList: list of str
        :param _Tags: Tag key and value.
If multiple tags are specified, all such tags will be created and bound to the specified resources.
For each resource, each tag key can have only one value. If you try to add an existing tag key, the corresponding tag value will be updated to the new value.
Non-existent tags will be automatically created.
Value range of N: 0-9
        :type Tags: list of Tag
        """
        self._ResourceList = None
        self._Tags = None

    @property
    def ResourceList(self):
        return self._ResourceList

    @ResourceList.setter
    def ResourceList(self, ResourceList):
        self._ResourceList = ResourceList

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ResourceList = params.get("ResourceList")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagResourcesResponse(AbstractModel):
    """TagResources response structure.

    """

    def __init__(self):
        r"""
        :param _FailedResources: Information of failed resources.
When tag creating and binding succeeds, the returned `FailedResources` will be empty.
When tag creating and binding partially or completely fails, the returned `FailedResources` will display the details of failed resources.
        :type FailedResources: list of FailedResource
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FailedResources = None
        self._RequestId = None

    @property
    def FailedResources(self):
        return self._FailedResources

    @FailedResources.setter
    def FailedResources(self, FailedResources):
        self._FailedResources = FailedResources

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FailedResources") is not None:
            self._FailedResources = []
            for item in params.get("FailedResources"):
                obj = FailedResource()
                obj._deserialize(item)
                self._FailedResources.append(obj)
        self._RequestId = params.get("RequestId")


class TagWithDelete(AbstractModel):
    """A tag key-value pair and if deletion is allowed.

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key.
        :type TagKey: str
        :param _TagValue: Tag value.
        :type TagValue: str
        :param _CanDelete: If deletion is allowed.
        :type CanDelete: int
        :param _Category: Tag type. Valid values: Custom: custom tag; System: system tag; All: all tags. Default value: All.Note: This field may return null, indicating that no value is obtained.
        :type Category: str
        """
        self._TagKey = None
        self._TagValue = None
        self._CanDelete = None
        self._Category = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def CanDelete(self):
        return self._CanDelete

    @CanDelete.setter
    def CanDelete(self, CanDelete):
        self._CanDelete = CanDelete

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        self._CanDelete = params.get("CanDelete")
        self._Category = params.get("Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnTagResourcesRequest(AbstractModel):
    """UnTagResources request structure.

    """

    def __init__(self):
        r"""
        :param _ResourceList: Six-segment resource description list. Tencent Cloud uses a six-segment value to describe a resource. For more information, see [CAM](https://intl.cloud.tencent.com/document/product/598/67350?from_cn_redirect=1) > Overview > API List > Six-Segment Resource Information.
For example: ResourceList.1 = qcs::${ServiceType}:${Region}:uin/${Account}:${ResourcePrefix}/${ResourceId}.
Value range of N: 0–9
        :type ResourceList: list of str
        :param _TagKeys: Tag key.
Value range: 0–9
        :type TagKeys: list of str
        """
        self._ResourceList = None
        self._TagKeys = None

    @property
    def ResourceList(self):
        return self._ResourceList

    @ResourceList.setter
    def ResourceList(self, ResourceList):
        self._ResourceList = ResourceList

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys


    def _deserialize(self, params):
        self._ResourceList = params.get("ResourceList")
        self._TagKeys = params.get("TagKeys")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnTagResourcesResponse(AbstractModel):
    """UnTagResources response structure.

    """

    def __init__(self):
        r"""
        :param _FailedResources: Information of failed resources.
When tag unbinding succeeds, the returned `FailedResources` will be empty.
When tag unbinding partially or completely fails, the returned `FailedResources` will display the details of failed resources.
        :type FailedResources: list of FailedResource
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FailedResources = None
        self._RequestId = None

    @property
    def FailedResources(self):
        return self._FailedResources

    @FailedResources.setter
    def FailedResources(self, FailedResources):
        self._FailedResources = FailedResources

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FailedResources") is not None:
            self._FailedResources = []
            for item in params.get("FailedResources"):
                obj = FailedResource()
                obj._deserialize(item)
                self._FailedResources.append(obj)
        self._RequestId = params.get("RequestId")


class UpdateResourceTagValueRequest(AbstractModel):
    """UpdateResourceTagValue request structure.

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key associated with the resource.
        :type TagKey: str
        :param _TagValue: Modified tag value.
        :type TagValue: str
        :param _Resource: [Six-segment resource description](https://intl.cloud.tencent.com/document/product/598/10606?from_cn_redirect=1)
        :type Resource: str
        """
        self._TagKey = None
        self._TagValue = None
        self._Resource = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        self._Resource = params.get("Resource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateResourceTagValueResponse(AbstractModel):
    """UpdateResourceTagValue response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")