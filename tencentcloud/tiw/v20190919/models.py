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


class ApplicationItem(AbstractModel):
    """Whiteboard application.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _AppName: Application name.
        :type AppName: str
        :param _CreateTime: Creation time.
        :type CreateTime: str
        :param _TagList: Tag list.
        :type TagList: list of Tag
        """
        self._SdkAppId = None
        self._AppName = None
        self._CreateTime = None
        self._TagList = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def TagList(self):
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._AppName = params.get("AppName")
        self._CreateTime = params.get("CreateTime")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self._TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyTiwTrialRequest(AbstractModel):
    """ApplyTiwTrial request structure.

    """


class ApplyTiwTrialResponse(AbstractModel):
    """ApplyTiwTrial response structure.

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


class AuthParam(AbstractModel):
    """Authentication parameters.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _UserId: User ID.
        :type UserId: str
        :param _UserSig: Signature corresponding to the user ID.
        :type UserSig: str
        """
        self._SdkAppId = None
        self._UserId = None
        self._UserSig = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._UserId = params.get("UserId")
        self._UserSig = params.get("UserSig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Canvas(AbstractModel):
    """Mixed stream canvas parameter

    """

    def __init__(self):
        r"""
        :param _LayoutParams: Width and height of the mixed stream canvas
        :type LayoutParams: :class:`tencentcloud.tiw.v20190919.models.LayoutParams`
        :param _BackgroundColor: Background color, which is black by default. Its format is RGB. for example, "#FF0000" for the red color.
        :type BackgroundColor: str
        """
        self._LayoutParams = None
        self._BackgroundColor = None

    @property
    def LayoutParams(self):
        return self._LayoutParams

    @LayoutParams.setter
    def LayoutParams(self, LayoutParams):
        self._LayoutParams = LayoutParams

    @property
    def BackgroundColor(self):
        return self._BackgroundColor

    @BackgroundColor.setter
    def BackgroundColor(self, BackgroundColor):
        self._BackgroundColor = BackgroundColor


    def _deserialize(self, params):
        if params.get("LayoutParams") is not None:
            self._LayoutParams = LayoutParams()
            self._LayoutParams._deserialize(params.get("LayoutParams"))
        self._BackgroundColor = params.get("BackgroundColor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Concat(AbstractModel):
    """Real-time recording video splicing parameter

    """

    def __init__(self):
        r"""
        :param _Enabled: Whether to enable the video splicing feature
If the video splicing feature is enabled, the real-time recording service will splice multiple video clips resulting from the pause into one video.
        :type Enabled: bool
        :param _Image: Download address of the padding image used during video splicing. If it is not specified, a pure black image is used by default.
        :type Image: str
        """
        self._Enabled = None
        self._Image = None

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._Image = params.get("Image")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationRequest(AbstractModel):
    """CreateApplication request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _AppName: Application name.
        :type AppName: str
        :param _SKey: SKey required for creating an IM application.
        :type SKey: str
        :param _TinyId: TinyId required for creating an IM application.
        :type TinyId: str
        :param _TagList: List of tags to be bound.
        :type TagList: list of Tag
        """
        self._SdkAppId = None
        self._AppName = None
        self._SKey = None
        self._TinyId = None
        self._TagList = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def SKey(self):
        return self._SKey

    @SKey.setter
    def SKey(self, SKey):
        self._SKey = SKey

    @property
    def TinyId(self):
        return self._TinyId

    @TinyId.setter
    def TinyId(self, TinyId):
        self._TinyId = TinyId

    @property
    def TagList(self):
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._AppName = params.get("AppName")
        self._SKey = params.get("SKey")
        self._TinyId = params.get("TinyId")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self._TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationResponse(AbstractModel):
    """CreateApplication response structure.

    """

    def __init__(self):
        r"""
        :param _AppId: AppId of the customer.
        :type AppId: int
        :param _AppName: Application name.
        :type AppName: str
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AppId = None
        self._AppName = None
        self._SdkAppId = None
        self._RequestId = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._AppName = params.get("AppName")
        self._SdkAppId = params.get("SdkAppId")
        self._RequestId = params.get("RequestId")


class CreateSnapshotTaskRequest(AbstractModel):
    """CreateSnapshotTask request structure.

    """

    def __init__(self):
        r"""
        :param _Whiteboard: Whiteboard parameters.
        :type Whiteboard: :class:`tencentcloud.tiw.v20190919.models.SnapshotWhiteboard`
        :param _SdkAppId: `SdkAppId` of the whiteboard application.
        :type SdkAppId: int
        :param _RoomId: Whiteboard room ID.
        :type RoomId: int
        :param _CallbackURL: Callback URL to which the whiteboard snapshot result is to be sent.
        :type CallbackURL: str
        :param _COS: `COS` bucket in which the generated whiteboard snapshot file is to be stored. If you leave this parameter empty, the generated file will be stored in the public bucket and retained for only three days.
        :type COS: :class:`tencentcloud.tiw.v20190919.models.SnapshotCOS`
        :param _SnapshotMode: Whiteboard snapshot mode. Default value: `AllMarks`. Valid values:

`AllMarks`: Full mode. In this mode, a snapshot image is generated based on each whiteboard snapshot mark that is added by calling the `addSnapshotMark` API on the client.

`LatestMarksOnly`: Single-page deduplication mode. In this mode, a snapshot image is generated based only on the latest whiteboard snapshot mark that is added by calling the `addSnapshotMark` API on the client if the API is called multiple times for the same whiteboard snapshot.

**Note: The `LatestMarksOnly` mode takes effect only when the `addSnapshotMark` API is called by using Tencent Interactive Whiteboard SDK v2.6.8 or later. Otherwise, even if this parameter is set to `LatestMarksOnly`, the default `AllMarks` mode is used.**
        :type SnapshotMode: str
        """
        self._Whiteboard = None
        self._SdkAppId = None
        self._RoomId = None
        self._CallbackURL = None
        self._COS = None
        self._SnapshotMode = None

    @property
    def Whiteboard(self):
        return self._Whiteboard

    @Whiteboard.setter
    def Whiteboard(self, Whiteboard):
        self._Whiteboard = Whiteboard

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def CallbackURL(self):
        return self._CallbackURL

    @CallbackURL.setter
    def CallbackURL(self, CallbackURL):
        self._CallbackURL = CallbackURL

    @property
    def COS(self):
        return self._COS

    @COS.setter
    def COS(self, COS):
        self._COS = COS

    @property
    def SnapshotMode(self):
        return self._SnapshotMode

    @SnapshotMode.setter
    def SnapshotMode(self, SnapshotMode):
        self._SnapshotMode = SnapshotMode


    def _deserialize(self, params):
        if params.get("Whiteboard") is not None:
            self._Whiteboard = SnapshotWhiteboard()
            self._Whiteboard._deserialize(params.get("Whiteboard"))
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._CallbackURL = params.get("CallbackURL")
        if params.get("COS") is not None:
            self._COS = SnapshotCOS()
            self._COS._deserialize(params.get("COS"))
        self._SnapshotMode = params.get("SnapshotMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSnapshotTaskResponse(AbstractModel):
    """CreateSnapshotTask response structure.

    """

    def __init__(self):
        r"""
        :param _TaskID: ID of the whiteboard snapshot task. This parameter is returned only if a task is created successfully.
        :type TaskID: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskID = None
        self._RequestId = None

    @property
    def TaskID(self):
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskID = params.get("TaskID")
        self._RequestId = params.get("RequestId")


class CreateTranscodeRequest(AbstractModel):
    """CreateTranscode request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the customer
        :type SdkAppId: int
        :param _Url: URL of the transcoded document after URL encoding. URL encoding converts characters into a format that can be transmitted over the Internet. For example, URL encoding can convert the document URL http://example.com/Test.pdf into http://example.com/%E6%B5%8B%E8%AF%95.pdf. To improve the success rate of URL parsing, use URL encoding.
        :type Url: str
        :param _IsStaticPPT: Whether the PowerPoint file is static. The default value is False.
If IsStaticPPT is False, documents with the .ppt or .pptx extension will be dynamically transcoded to HTML5 pages, and documents with other extensions will be statically transcoded to images. If IsStaticPPT is True, documents with any extensions will be statically transcoded to images.
        :type IsStaticPPT: bool
        :param _MinResolution: Note: This parameter is disused. Use the MinScaleResolution parameter to pass in a resolution. For more information, see [CreateTranscode](https://intl.cloud.tencent.com/document/api/1137/40060?from_cn_redirect=1#SDK).

Minimum resolution of the transcoded document. If no value or null is specified for it or the resolution format is invalid, the original document resolution is used.

Example: 1280x720. Note that the character between the numbers is the letter x.
        :type MinResolution: str
        :param _ThumbnailResolution: Resolution of the thumbnail generated for the dynamically transcoded PowerPoint file. If no value or null is specified for it or the resolution format is invalid, no thumbnail will be generated. The resolution format is the same as that of MinResolution.

For static transcoding, this parameter does not work.
        :type ThumbnailResolution: str
        :param _CompressFileType: Compression format of the transcoded file. If no value or null is specified for it or the specified format is invalid, no compression file will be generated. Currently, the following compression formats are supported:

`zip`: generates a .zip compression package.
`tar.gz: generates a .tar.gz compression package.
        :type CompressFileType: str
        :param _ExtraData: Internal parameter.
        :type ExtraData: str
        :param _Priority: Document transcoding priority. This parameter takes effect only for PowerPoint dynamic transcoding. Valid values:<br/>
- low: Low transcoding priority. The task can transcode at most 500 MB of data or a 2000-page document, with a download timeout no longer than 10 minutes. Due to resource limits, these tasks may have to queue for a long period of time. Consider this before you use this feature.
- null: Normal transcoding priority. The task can transcode at most 200 MB of data or a 500-page document, with a download timeout no longer than 2 minutes.
<br/>
Note: For static transcoding such as PDF transcoding, each task can transcode at most 200 MB of data regardless of the transcoding priority.
        :type Priority: str
        :param _MinScaleResolution: Minimum resolution of the transcoded document. If no value or null is specified for it or the resolution format is invalid, the original document resolution is used.
Higher resolution brings clearer visual effect, but also means larger size of the transcoded image resources and longer loading time of the transcoded file. Set this parameter appropriately based on your actual scenario.

Example: 1280x720. Note that the character between the numbers is the letter x.
        :type MinScaleResolution: str
        :param _AutoHandleUnsupportedElement: Specifies whether to enable auto handling of unsupported elements. By default, this feature is disabled.

If auto handling is enabled, the following processes are performed:
1. Inkblots: Remove unsupported inkblots, such as those drawn by using WPS.
2. Auto page flip: Clear the auto page clip settings in the PowerPoint file and set the page flip mode to mouse click.
3. Corrupted audio/videos: Remove the references to corrupted audio/videos in the PowerPoint file.
        :type AutoHandleUnsupportedElement: bool
        """
        self._SdkAppId = None
        self._Url = None
        self._IsStaticPPT = None
        self._MinResolution = None
        self._ThumbnailResolution = None
        self._CompressFileType = None
        self._ExtraData = None
        self._Priority = None
        self._MinScaleResolution = None
        self._AutoHandleUnsupportedElement = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def IsStaticPPT(self):
        return self._IsStaticPPT

    @IsStaticPPT.setter
    def IsStaticPPT(self, IsStaticPPT):
        self._IsStaticPPT = IsStaticPPT

    @property
    def MinResolution(self):
        return self._MinResolution

    @MinResolution.setter
    def MinResolution(self, MinResolution):
        self._MinResolution = MinResolution

    @property
    def ThumbnailResolution(self):
        return self._ThumbnailResolution

    @ThumbnailResolution.setter
    def ThumbnailResolution(self, ThumbnailResolution):
        self._ThumbnailResolution = ThumbnailResolution

    @property
    def CompressFileType(self):
        return self._CompressFileType

    @CompressFileType.setter
    def CompressFileType(self, CompressFileType):
        self._CompressFileType = CompressFileType

    @property
    def ExtraData(self):
        return self._ExtraData

    @ExtraData.setter
    def ExtraData(self, ExtraData):
        self._ExtraData = ExtraData

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def MinScaleResolution(self):
        return self._MinScaleResolution

    @MinScaleResolution.setter
    def MinScaleResolution(self, MinScaleResolution):
        self._MinScaleResolution = MinScaleResolution

    @property
    def AutoHandleUnsupportedElement(self):
        return self._AutoHandleUnsupportedElement

    @AutoHandleUnsupportedElement.setter
    def AutoHandleUnsupportedElement(self, AutoHandleUnsupportedElement):
        self._AutoHandleUnsupportedElement = AutoHandleUnsupportedElement


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Url = params.get("Url")
        self._IsStaticPPT = params.get("IsStaticPPT")
        self._MinResolution = params.get("MinResolution")
        self._ThumbnailResolution = params.get("ThumbnailResolution")
        self._CompressFileType = params.get("CompressFileType")
        self._ExtraData = params.get("ExtraData")
        self._Priority = params.get("Priority")
        self._MinScaleResolution = params.get("MinScaleResolution")
        self._AutoHandleUnsupportedElement = params.get("AutoHandleUnsupportedElement")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTranscodeResponse(AbstractModel):
    """CreateTranscode response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Unique ID of the document transcoding task, which is used to query the task progress and transcoding result
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateVideoGenerationTaskRequest(AbstractModel):
    """CreateVideoGenerationTask request structure.

    """

    def __init__(self):
        r"""
        :param _OnlineRecordTaskId: ID of the recording task.
        :type OnlineRecordTaskId: str
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _Whiteboard: Whiteboard parameters of the recording video generation task, such as the width and height of the whiteboard.

This parameter conflicts with the Whiteboard parameter in the API for starting a recording task. If the two Whiteboard parameters are both specified, the Whiteboard parameter in this API takes priority for recording video generation. If the Whiteboard parameter in this API is not specified, the Whiteboard parameter specified in the API for starting a recording task is used for recording video generation.
        :type Whiteboard: :class:`tencentcloud.tiw.v20190919.models.Whiteboard`
        :param _Concat: Video splicing parameters.

This parameter conflicts with the Concat parameter in the API for starting a recording task. If the two Concat parameters are both specified, the Concat parameter in this API takes priority for video splicing. If the Concat parameter in this API is not specified, the Concat parameter specified in the API for starting a recording task is used for video splicing.
        :type Concat: :class:`tencentcloud.tiw.v20190919.models.Concat`
        :param _MixStream: Video stream mixing parameters.

This parameter conflicts with the MixStream parameter in the API for starting a recording task. If the two MixStream parameters are both specified, the MixStream parameter in this API takes priority for video stream mixing. If the MixStream parameter in this API is not specified, the MixStream parameter specified in the API for starting a recording task is used for video stream mixing.
        :type MixStream: :class:`tencentcloud.tiw.v20190919.models.MixStream`
        :param _RecordControl: A group of video generation parameters. It specifies the streams to be generated, whether to disable audio recording for a stream, and whether to record only low-resolution videos, etc.

This parameter conflicts with the RecordControl parameter in the API for starting a recording task. If the two RecordControl parameters are both specified, the RecordControl parameter in this API takes priority for video generation control. If the RecordControl parameter in this API is not specified, the RecordControl parameter specified in the API for starting a recording task is used for video generation control.
        :type RecordControl: :class:`tencentcloud.tiw.v20190919.models.RecordControl`
        :param _ExtraData: Internal parameter.
        :type ExtraData: str
        """
        self._OnlineRecordTaskId = None
        self._SdkAppId = None
        self._Whiteboard = None
        self._Concat = None
        self._MixStream = None
        self._RecordControl = None
        self._ExtraData = None

    @property
    def OnlineRecordTaskId(self):
        return self._OnlineRecordTaskId

    @OnlineRecordTaskId.setter
    def OnlineRecordTaskId(self, OnlineRecordTaskId):
        self._OnlineRecordTaskId = OnlineRecordTaskId

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Whiteboard(self):
        return self._Whiteboard

    @Whiteboard.setter
    def Whiteboard(self, Whiteboard):
        self._Whiteboard = Whiteboard

    @property
    def Concat(self):
        return self._Concat

    @Concat.setter
    def Concat(self, Concat):
        self._Concat = Concat

    @property
    def MixStream(self):
        return self._MixStream

    @MixStream.setter
    def MixStream(self, MixStream):
        self._MixStream = MixStream

    @property
    def RecordControl(self):
        return self._RecordControl

    @RecordControl.setter
    def RecordControl(self, RecordControl):
        self._RecordControl = RecordControl

    @property
    def ExtraData(self):
        return self._ExtraData

    @ExtraData.setter
    def ExtraData(self, ExtraData):
        self._ExtraData = ExtraData


    def _deserialize(self, params):
        self._OnlineRecordTaskId = params.get("OnlineRecordTaskId")
        self._SdkAppId = params.get("SdkAppId")
        if params.get("Whiteboard") is not None:
            self._Whiteboard = Whiteboard()
            self._Whiteboard._deserialize(params.get("Whiteboard"))
        if params.get("Concat") is not None:
            self._Concat = Concat()
            self._Concat._deserialize(params.get("Concat"))
        if params.get("MixStream") is not None:
            self._MixStream = MixStream()
            self._MixStream._deserialize(params.get("MixStream"))
        if params.get("RecordControl") is not None:
            self._RecordControl = RecordControl()
            self._RecordControl._deserialize(params.get("RecordControl"))
        self._ExtraData = params.get("ExtraData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVideoGenerationTaskResponse(AbstractModel):
    """CreateVideoGenerationTask response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: ID of the video generation task.
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CustomLayout(AbstractModel):
    """Custom mixed stream layout parameter

    """

    def __init__(self):
        r"""
        :param _Canvas: Mixed stream canvas parameter
        :type Canvas: :class:`tencentcloud.tiw.v20190919.models.Canvas`
        :param _InputStreamList: Stream layout. The layout of each stream cannot exceed the canvas area.
        :type InputStreamList: list of StreamLayout
        """
        self._Canvas = None
        self._InputStreamList = None

    @property
    def Canvas(self):
        return self._Canvas

    @Canvas.setter
    def Canvas(self, Canvas):
        self._Canvas = Canvas

    @property
    def InputStreamList(self):
        return self._InputStreamList

    @InputStreamList.setter
    def InputStreamList(self, InputStreamList):
        self._InputStreamList = InputStreamList


    def _deserialize(self, params):
        if params.get("Canvas") is not None:
            self._Canvas = Canvas()
            self._Canvas._deserialize(params.get("Canvas"))
        if params.get("InputStreamList") is not None:
            self._InputStreamList = []
            for item in params.get("InputStreamList"):
                obj = StreamLayout()
                obj._deserialize(item)
                self._InputStreamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataItem(AbstractModel):
    """Chart data, including the time, values, and details.

    """

    def __init__(self):
        r"""
        :param _Time: Time. The following formats are supported:
yyyy-mm
yyyy-mm-dd
yyyy-mm-dd HH:MM:SS
        :type Time: str
        :param _Value: Values required for drawing charts.
        :type Value: int
        :param _Details: Details of the values.
        :type Details: list of Detail
        """
        self._Time = None
        self._Value = None
        self._Details = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Value = params.get("Value")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = Detail()
                obj._deserialize(item)
                self._Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAPIServiceRequest(AbstractModel):
    """DescribeAPIService request structure.

    """

    def __init__(self):
        r"""
        :param _Service: Supported services are cos:GetService and cdn:DescribeDomainsConfig.
        :type Service: str
        :param _Data: Request parameters in JSON format.
        :type Data: str
        """
        self._Service = None
        self._Data = None

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Service = params.get("Service")
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAPIServiceResponse(AbstractModel):
    """DescribeAPIService response structure.

    """

    def __init__(self):
        r"""
        :param _ResponseData: Response data in JSON format.
        :type ResponseData: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ResponseData = None
        self._RequestId = None

    @property
    def ResponseData(self):
        return self._ResponseData

    @ResponseData.setter
    def ResponseData(self, ResponseData):
        self._ResponseData = ResponseData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResponseData = params.get("ResponseData")
        self._RequestId = params.get("RequestId")


class DescribeApplicationInfosRequest(AbstractModel):
    """DescribeApplicationInfos request structure.

    """


class DescribeApplicationInfosResponse(AbstractModel):
    """DescribeApplicationInfos response structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationInfos: Application list.
        :type ApplicationInfos: list of ApplicationItem
        :param _AllOption: Specifies whether all applications are included. The value 0 indicates no and 1 indicates yes.
        :type AllOption: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ApplicationInfos = None
        self._AllOption = None
        self._RequestId = None

    @property
    def ApplicationInfos(self):
        return self._ApplicationInfos

    @ApplicationInfos.setter
    def ApplicationInfos(self, ApplicationInfos):
        self._ApplicationInfos = ApplicationInfos

    @property
    def AllOption(self):
        return self._AllOption

    @AllOption.setter
    def AllOption(self, AllOption):
        self._AllOption = AllOption

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ApplicationInfos") is not None:
            self._ApplicationInfos = []
            for item in params.get("ApplicationInfos"):
                obj = ApplicationItem()
                obj._deserialize(item)
                self._ApplicationInfos.append(obj)
        self._AllOption = params.get("AllOption")
        self._RequestId = params.get("RequestId")


class DescribeApplicationUsageRequest(AbstractModel):
    """DescribeApplicationUsage request structure.

    """

    def __init__(self):
        r"""
        :param _BeginTime: Start time of the query period. The start time point is included in the query period.
        :type BeginTime: str
        :param _EndTime: End time of the query period. The end time point is not included in the query period.
        :type EndTime: str
        :param _SubProduct: Subproduct name.
        :type SubProduct: str
        :param _TimeLevel: Unit of time increment.
- MONTHLY: month
- DAILY: day
- MINUTELY: minute
        :type TimeLevel: str
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _IsWeighted: true: Returns the weighted sum of raw usage data.
false: Returns the raw usage data.
        :type IsWeighted: bool
        """
        self._BeginTime = None
        self._EndTime = None
        self._SubProduct = None
        self._TimeLevel = None
        self._SdkAppId = None
        self._IsWeighted = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SubProduct(self):
        return self._SubProduct

    @SubProduct.setter
    def SubProduct(self, SubProduct):
        self._SubProduct = SubProduct

    @property
    def TimeLevel(self):
        return self._TimeLevel

    @TimeLevel.setter
    def TimeLevel(self, TimeLevel):
        self._TimeLevel = TimeLevel

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def IsWeighted(self):
        return self._IsWeighted

    @IsWeighted.setter
    def IsWeighted(self, IsWeighted):
        self._IsWeighted = IsWeighted


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._SubProduct = params.get("SubProduct")
        self._TimeLevel = params.get("TimeLevel")
        self._SdkAppId = params.get("SdkAppId")
        self._IsWeighted = params.get("IsWeighted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationUsageResponse(AbstractModel):
    """DescribeApplicationUsage response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Usage data required for drawing charts.
        :type Data: list of DataItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DataItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBoardSDKLogRequest(AbstractModel):
    """DescribeBoardSDKLog request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _RoomId: Room ID to be used to query logs.
        :type RoomId: str
        :param _UserId: User ID to be used to query logs.
        :type UserId: str
        :param _TimeRange: Query period, which consists of two Unix timestamps in milliseconds. The first indicates the start time and the second the end time.
        :type TimeRange: list of int
        :param _AggregationInterval: Interval for aggregating log number queries. Example values: `5m`, `1h`, `4h`
        :type AggregationInterval: str
        :param _Query: Extra query conditions.
        :type Query: str
        :param _Ascending: Specifies whether to sort results in ascending order of time.
        :type Ascending: bool
        :param _Context: Context key used for recursive extraction. Obtain this parameter in the response to the last request.
        :type Context: str
        """
        self._SdkAppId = None
        self._RoomId = None
        self._UserId = None
        self._TimeRange = None
        self._AggregationInterval = None
        self._Query = None
        self._Ascending = None
        self._Context = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def TimeRange(self):
        return self._TimeRange

    @TimeRange.setter
    def TimeRange(self, TimeRange):
        self._TimeRange = TimeRange

    @property
    def AggregationInterval(self):
        return self._AggregationInterval

    @AggregationInterval.setter
    def AggregationInterval(self, AggregationInterval):
        self._AggregationInterval = AggregationInterval

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Ascending(self):
        return self._Ascending

    @Ascending.setter
    def Ascending(self, Ascending):
        self._Ascending = Ascending

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._UserId = params.get("UserId")
        self._TimeRange = params.get("TimeRange")
        self._AggregationInterval = params.get("AggregationInterval")
        self._Query = params.get("Query")
        self._Ascending = params.get("Ascending")
        self._Context = params.get("Context")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBoardSDKLogResponse(AbstractModel):
    """DescribeBoardSDKLog response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Number of logs queried.
        :type Total: int
        :param _Sources: Log details.
        :type Sources: list of str
        :param _Buckets: Number of logs queried within each time range after aggregation based on the time range.
        :type Buckets: list of str
        :param _Context: Context key used for recursive extraction. This parameter can be used in the next request.
        :type Context: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Sources = None
        self._Buckets = None
        self._Context = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Sources(self):
        return self._Sources

    @Sources.setter
    def Sources(self, Sources):
        self._Sources = Sources

    @property
    def Buckets(self):
        return self._Buckets

    @Buckets.setter
    def Buckets(self, Buckets):
        self._Buckets = Buckets

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._Sources = params.get("Sources")
        self._Buckets = params.get("Buckets")
        self._Context = params.get("Context")
        self._RequestId = params.get("RequestId")


class DescribeIMApplicationsRequest(AbstractModel):
    """DescribeIMApplications request structure.

    """


class DescribeIMApplicationsResponse(AbstractModel):
    """DescribeIMApplications response structure.

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


class DescribeOnlineRecordCallbackRequest(AbstractModel):
    """DescribeOnlineRecordCallback request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the application
        :type SdkAppId: int
        """
        self._SdkAppId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOnlineRecordCallbackResponse(AbstractModel):
    """DescribeOnlineRecordCallback response structure.

    """

    def __init__(self):
        r"""
        :param _Callback: Callback address of the real-time recording event. If no callback address is set, this field is null.
        :type Callback: str
        :param _CallbackKey: Authentication key of the real-time recording callback
        :type CallbackKey: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Callback = None
        self._CallbackKey = None
        self._RequestId = None

    @property
    def Callback(self):
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Callback = params.get("Callback")
        self._CallbackKey = params.get("CallbackKey")
        self._RequestId = params.get("RequestId")


class DescribeOnlineRecordRequest(AbstractModel):
    """DescribeOnlineRecord request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the customer
        :type SdkAppId: int
        :param _TaskId: ID of the real-time recording task
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOnlineRecordResponse(AbstractModel):
    """DescribeOnlineRecord response structure.

    """

    def __init__(self):
        r"""
        :param _FinishReason: Recording stop reason
- AUTO: Recording automatically stops because no upstream audio/video or whiteboard operation occurs in the room for a long time.
- USER_CALL: The API for stopping recording is called.
- EXCEPTION: An exception occurred.
- FORCE_STOP: Recording is forcibly stopped, which is usually because the recording has been paused for more than 90 minutes or has lasted for more than 24 hours.
        :type FinishReason: str
        :param _TaskId: ID of the recording task to be queried.
        :type TaskId: str
        :param _Status: Recording task status
- PREPARED: preparing
- RECORDING: recording
- PAUSED: recording is paused.
- STOPPED: recording is stopped, and the recorded video is being processed and uploaded.
- FINISHED: the recorded video has been processed and uploaded, and the recording result is generated.
        :type Status: str
        :param _RoomId: Room ID
        :type RoomId: int
        :param _GroupId: Group ID of the whiteboard
        :type GroupId: str
        :param _RecordUserId: ID of the recording user
        :type RecordUserId: str
        :param _RecordStartTime: Actual recording start time, which is a UNIX timestamp in seconds
        :type RecordStartTime: int
        :param _RecordStopTime: Actual recording stop time, which is a UNIX timestamp in seconds
        :type RecordStopTime: int
        :param _TotalTime: Total video playback duration, in milliseconds
        :type TotalTime: int
        :param _ExceptionCnt: Number of exceptions during recording
        :type ExceptionCnt: int
        :param _OmittedDurations: Duration to be deleted in the spliced video. This parameter is valid only when the video splicing feature is enabled.
        :type OmittedDurations: list of OmittedDuration
        :param _VideoInfos: List of recorded videos
        :type VideoInfos: list of VideoInfo
        :param _ReplayUrl: 
        :type ReplayUrl: str
        :param _Interrupts: Number of video stream interruptions during recording.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Interrupts: list of Interrupt
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FinishReason = None
        self._TaskId = None
        self._Status = None
        self._RoomId = None
        self._GroupId = None
        self._RecordUserId = None
        self._RecordStartTime = None
        self._RecordStopTime = None
        self._TotalTime = None
        self._ExceptionCnt = None
        self._OmittedDurations = None
        self._VideoInfos = None
        self._ReplayUrl = None
        self._Interrupts = None
        self._RequestId = None

    @property
    def FinishReason(self):
        return self._FinishReason

    @FinishReason.setter
    def FinishReason(self, FinishReason):
        self._FinishReason = FinishReason

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RecordUserId(self):
        return self._RecordUserId

    @RecordUserId.setter
    def RecordUserId(self, RecordUserId):
        self._RecordUserId = RecordUserId

    @property
    def RecordStartTime(self):
        return self._RecordStartTime

    @RecordStartTime.setter
    def RecordStartTime(self, RecordStartTime):
        self._RecordStartTime = RecordStartTime

    @property
    def RecordStopTime(self):
        return self._RecordStopTime

    @RecordStopTime.setter
    def RecordStopTime(self, RecordStopTime):
        self._RecordStopTime = RecordStopTime

    @property
    def TotalTime(self):
        return self._TotalTime

    @TotalTime.setter
    def TotalTime(self, TotalTime):
        self._TotalTime = TotalTime

    @property
    def ExceptionCnt(self):
        return self._ExceptionCnt

    @ExceptionCnt.setter
    def ExceptionCnt(self, ExceptionCnt):
        self._ExceptionCnt = ExceptionCnt

    @property
    def OmittedDurations(self):
        return self._OmittedDurations

    @OmittedDurations.setter
    def OmittedDurations(self, OmittedDurations):
        self._OmittedDurations = OmittedDurations

    @property
    def VideoInfos(self):
        return self._VideoInfos

    @VideoInfos.setter
    def VideoInfos(self, VideoInfos):
        self._VideoInfos = VideoInfos

    @property
    def ReplayUrl(self):
        return self._ReplayUrl

    @ReplayUrl.setter
    def ReplayUrl(self, ReplayUrl):
        self._ReplayUrl = ReplayUrl

    @property
    def Interrupts(self):
        return self._Interrupts

    @Interrupts.setter
    def Interrupts(self, Interrupts):
        self._Interrupts = Interrupts

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FinishReason = params.get("FinishReason")
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._RoomId = params.get("RoomId")
        self._GroupId = params.get("GroupId")
        self._RecordUserId = params.get("RecordUserId")
        self._RecordStartTime = params.get("RecordStartTime")
        self._RecordStopTime = params.get("RecordStopTime")
        self._TotalTime = params.get("TotalTime")
        self._ExceptionCnt = params.get("ExceptionCnt")
        if params.get("OmittedDurations") is not None:
            self._OmittedDurations = []
            for item in params.get("OmittedDurations"):
                obj = OmittedDuration()
                obj._deserialize(item)
                self._OmittedDurations.append(obj)
        if params.get("VideoInfos") is not None:
            self._VideoInfos = []
            for item in params.get("VideoInfos"):
                obj = VideoInfo()
                obj._deserialize(item)
                self._VideoInfos.append(obj)
        self._ReplayUrl = params.get("ReplayUrl")
        if params.get("Interrupts") is not None:
            self._Interrupts = []
            for item in params.get("Interrupts"):
                obj = Interrupt()
                obj._deserialize(item)
                self._Interrupts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePostpaidUsageRequest(AbstractModel):
    """DescribePostpaidUsage request structure.

    """

    def __init__(self):
        r"""
        :param _BeginTime: Start time of the query period.
        :type BeginTime: str
        :param _EndTime: End time of the query period.
        :type EndTime: str
        """
        self._BeginTime = None
        self._EndTime = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePostpaidUsageResponse(AbstractModel):
    """DescribePostpaidUsage response structure.

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


class DescribeQualityMetricsRequest(AbstractModel):
    """DescribeQualityMetrics request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _StartTime: Start time, which is a Unix timestamp in seconds. The time length cannot exceed seven days.
        :type StartTime: int
        :param _EndTime: End time, which is a Unix timestamp in seconds. The time length cannot exceed seven days.
        :type EndTime: int
        :param _Metric: Metrics to be queried. Valid values:
  - image_load_total_count: The number of image loads.
  - image_load_fail_count: The number of image load failures.
  - image_load_success_rate: The success rate of image loading, in percentage.
  - ppt_load_total_count: The number of PowerPoint file loads.
  - ppt_load_fail_count: The number of PowerPoint file load failures.
  - ppt_load_success_rate: The success rate of PowerPoint file loading, in percentage.
  - verify_sdk_total_count: The number of SDK verifications.
  - verify_sdk_fail_count: The number of SDK verification failures.
  - verify_sdk_success_rate: The success rate of SDK verification, in percentage.
  - verify_sdk_in_one_second_rate: The rate of SDK verification completed within one second, in percentage.
  - verify_sdk_cost_avg: The average time taken by each SDK verification, in milliseconds.
        :type Metric: str
        :param _Interval: Aggregation interval. Valid value: `1h`.
        :type Interval: str
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._Metric = None
        self._Interval = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Metric = params.get("Metric")
        self._Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQualityMetricsResponse(AbstractModel):
    """DescribeQualityMetrics response structure.

    """

    def __init__(self):
        r"""
        :param _Metric: Query metrics.
        :type Metric: str
        :param _Content: Time series.
        :type Content: list of TimeValue
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Metric = None
        self._Content = None
        self._RequestId = None

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Metric = params.get("Metric")
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = TimeValue()
                obj._deserialize(item)
                self._Content.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRecordSearchRequest(AbstractModel):
    """DescribeRecordSearch request structure.

    """


class DescribeRecordSearchResponse(AbstractModel):
    """DescribeRecordSearch response structure.

    """

    def __init__(self):
        r"""
        :param _RecordTaskSet: The set of queried recording tasks.
        :type RecordTaskSet: list of RecordTaskSearchResult
        :param _TotalCount: Number of recording tasks.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RecordTaskSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def RecordTaskSet(self):
        return self._RecordTaskSet

    @RecordTaskSet.setter
    def RecordTaskSet(self, RecordTaskSet):
        self._RecordTaskSet = RecordTaskSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RecordTaskSet") is not None:
            self._RecordTaskSet = []
            for item in params.get("RecordTaskSet"):
                obj = RecordTaskSearchResult()
                obj._deserialize(item)
                self._RecordTaskSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRoomListRequest(AbstractModel):
    """DescribeRoomList request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _TimeRange: Query period, which consists of two Unix timestamps in milliseconds. The first indicates the start time and the second the end time.
        :type TimeRange: list of int
        :param _Query: Extra query conditions.
        :type Query: str
        :param _MaxSize: Maximum number of data entries to be returned. Default value: 1000.
        :type MaxSize: int
        """
        self._SdkAppId = None
        self._TimeRange = None
        self._Query = None
        self._MaxSize = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TimeRange(self):
        return self._TimeRange

    @TimeRange.setter
    def TimeRange(self, TimeRange):
        self._TimeRange = TimeRange

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TimeRange = params.get("TimeRange")
        self._Query = params.get("Query")
        self._MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoomListResponse(AbstractModel):
    """DescribeRoomList response structure.

    """

    def __init__(self):
        r"""
        :param _RoomList: List of rooms of the whiteboard.
        :type RoomList: list of RoomListItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RoomList = None
        self._RequestId = None

    @property
    def RoomList(self):
        return self._RoomList

    @RoomList.setter
    def RoomList(self, RoomList):
        self._RoomList = RoomList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RoomList") is not None:
            self._RoomList = []
            for item in params.get("RoomList"):
                obj = RoomListItem()
                obj._deserialize(item)
                self._RoomList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSnapshotTaskRequest(AbstractModel):
    """DescribeSnapshotTask request structure.

    """

    def __init__(self):
        r"""
        :param _TaskID: ID of the query task.
        :type TaskID: str
        :param _SdkAppId: SdkAppId of the task.
        :type SdkAppId: int
        """
        self._TaskID = None
        self._SdkAppId = None

    @property
    def TaskID(self):
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._TaskID = params.get("TaskID")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotTaskResponse(AbstractModel):
    """DescribeSnapshotTask response structure.

    """

    def __init__(self):
        r"""
        :param _TaskID: Task ID.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type TaskID: str
        :param _Status: Task status.
Running: The task is running.
Finished: The task is finished.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _CreateTime: Creation time of the task. Unit: seconds.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type CreateTime: int
        :param _FinishTime: Completion time of the task. Unit: seconds.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type FinishTime: int
        :param _Result: Task result information.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.tiw.v20190919.models.SnapshotResult`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskID = None
        self._Status = None
        self._CreateTime = None
        self._FinishTime = None
        self._Result = None
        self._RequestId = None

    @property
    def TaskID(self):
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def FinishTime(self):
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskID = params.get("TaskID")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._FinishTime = params.get("FinishTime")
        if params.get("Result") is not None:
            self._Result = SnapshotResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeTIWDailyUsageRequest(AbstractModel):
    """DescribeTIWDailyUsage request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _SubProduct: Subproduct usage to be queried. The following parameters are supported:
- sp_tiw_board: The duration of use of whiteboards, in minutes.
- sp_tiw_dt: The number of pages dynamically transcoded.
- sp_tiw_st: The number of pages statically transcoded.
- sp_tiw_ric: The duration of real-time recording, in minutes.

Note: Dynamic transcoding multiplies the number of pages of a document by eight times. Static transcoding does not change the number of pages of a document.
        :type SubProduct: str
        :param _StartTime: Start date in the format of YYYY-MM-DD. The start date is included in the query period.
        :type StartTime: str
        :param _EndTime: End date in the format of YYYY-MM-DD. The end date is included in the query period. The period queried per request cannot be longer than 31 days.
        :type EndTime: str
        """
        self._SdkAppId = None
        self._SubProduct = None
        self._StartTime = None
        self._EndTime = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SubProduct(self):
        return self._SubProduct

    @SubProduct.setter
    def SubProduct(self, SubProduct):
        self._SubProduct = SubProduct

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._SubProduct = params.get("SubProduct")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTIWDailyUsageResponse(AbstractModel):
    """DescribeTIWDailyUsage response structure.

    """

    def __init__(self):
        r"""
        :param _Usages: Usage summary of a specified product during a specified query period.
        :type Usages: list of UsageDataItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Usages = None
        self._RequestId = None

    @property
    def Usages(self):
        return self._Usages

    @Usages.setter
    def Usages(self, Usages):
        self._Usages = Usages

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Usages") is not None:
            self._Usages = []
            for item in params.get("Usages"):
                obj = UsageDataItem()
                obj._deserialize(item)
                self._Usages.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTIWRoomDailyUsageRequest(AbstractModel):
    """DescribeTIWRoomDailyUsage request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _SubProduct: Subproduct usage to be queried. The following parameters are supported:
- sp_tiw_board: The duration of use of whiteboards, in minutes.
- sp_tiw_ric: The duration of real-time recording, in minutes.
        :type SubProduct: str
        :param _StartTime: Start date in the format of YYYY-MM-DD. The start date is included in the query period.
        :type StartTime: str
        :param _EndTime: End date in the format of YYYY-MM-DD. The end date is included in the query period. The period queried per request cannot be longer than 31 days.
        :type EndTime: str
        :param _RoomIDs: Room IDs to be queried. If you leave this parameter empty, all room IDs are queried.
        :type RoomIDs: list of int non-negative
        :param _Offset: Offset for query. Default value: `0`.
        :type Offset: int
        :param _Limit: Maximum number of entries returned per query. Default value: `20`.
        :type Limit: int
        """
        self._SdkAppId = None
        self._SubProduct = None
        self._StartTime = None
        self._EndTime = None
        self._RoomIDs = None
        self._Offset = None
        self._Limit = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SubProduct(self):
        return self._SubProduct

    @SubProduct.setter
    def SubProduct(self, SubProduct):
        self._SubProduct = SubProduct

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RoomIDs(self):
        return self._RoomIDs

    @RoomIDs.setter
    def RoomIDs(self, RoomIDs):
        self._RoomIDs = RoomIDs

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
        self._SdkAppId = params.get("SdkAppId")
        self._SubProduct = params.get("SubProduct")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RoomIDs = params.get("RoomIDs")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTIWRoomDailyUsageResponse(AbstractModel):
    """DescribeTIWRoomDailyUsage response structure.

    """

    def __init__(self):
        r"""
        :param _Usages: Usage of the specified product per room during the specified query period.
        :type Usages: list of RoomUsageDataItem
        :param _Total: Number of usage data entries.
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Usages = None
        self._Total = None
        self._RequestId = None

    @property
    def Usages(self):
        return self._Usages

    @Usages.setter
    def Usages(self, Usages):
        self._Usages = Usages

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Usages") is not None:
            self._Usages = []
            for item in params.get("Usages"):
                obj = RoomUsageDataItem()
                obj._deserialize(item)
                self._Usages.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeTranscodeCallbackRequest(AbstractModel):
    """DescribeTranscodeCallback request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the application
        :type SdkAppId: int
        """
        self._SdkAppId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTranscodeCallbackResponse(AbstractModel):
    """DescribeTranscodeCallback response structure.

    """

    def __init__(self):
        r"""
        :param _Callback: Document transcoding callback address
        :type Callback: str
        :param _CallbackKey: Authentication key of the document transcoding callback
        :type CallbackKey: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Callback = None
        self._CallbackKey = None
        self._RequestId = None

    @property
    def Callback(self):
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Callback = params.get("Callback")
        self._CallbackKey = params.get("CallbackKey")
        self._RequestId = params.get("RequestId")


class DescribeTranscodeRequest(AbstractModel):
    """DescribeTranscode request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the customer
        :type SdkAppId: int
        :param _TaskId: Unique ID of the document transcoding task
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTranscodeResponse(AbstractModel):
    """DescribeTranscode response structure.

    """

    def __init__(self):
        r"""
        :param _Pages: Total number of document pages
        :type Pages: int
        :param _Progress: Transcoding progress. Value range: 0 to 100
        :type Progress: int
        :param _Resolution: Document resolution
        :type Resolution: str
        :param _ResultUrl: URL of the transcoding result
Dynamic transcoding: link of the HTML5 page transcoded from a PowerPoint file
Static transcoding: URL prefix of the image transcoded for each document page. For example, if the URL prefix is `http://example.com/g0jb42ps49vtebjshilb/`, the image URL of the first page is
`http://example.com/g0jb42ps49vtebjshilb/1.jpg`, and so on.
        :type ResultUrl: str
        :param _Status: Current task state
- QUEUED: queuing for transcoding
- PROCESSING: transcoding is in progress
- FINISHED: transcoded
        :type Status: str
        :param _TaskId: Unique ID of the transcoding task
        :type TaskId: str
        :param _Title: Document name
        :type Title: str
        :param _ThumbnailUrl: URL prefix of the thumbnail. If the URL prefix is `http://example.com/g0jb42ps49vtebjshilb/ `, the thumbnail URL for the first page of the dynamically transcoded PowerPoint file is
`http://example.com/g0jb42ps49vtebjshilb/1.jpg`, and so on.

If the document transcoding request carries the ThumbnailResolution parameter and the transcoding type is dynamic transcoding, this parameter is not null. In other cases, this parameter is null.
        :type ThumbnailUrl: str
        :param _ThumbnailResolution: Resolution of the thumbnail generated for dynamic transcoding
        :type ThumbnailResolution: str
        :param _CompressFileUrl: URL for downloading the transcoded and compressed file. If `CompressFileType` carried in the document transcoding request is null or is not a supported compression format, this parameter is null.
        :type CompressFileUrl: str
        :param _ResourceListUrl: Download URL (for trial) of the resource list.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type ResourceListUrl: str
        :param _Ext: Document generation mode (for trial).
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Ext: str
        :param _CreateTime: Document transcoding task creation time, unit: seconds.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type CreateTime: int
        :param _AssignTime: Document transcoding task assignment time, unit: seconds.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type AssignTime: int
        :param _FinishedTime: Document transcoding task finished time, unit: seconds.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type FinishedTime: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Pages = None
        self._Progress = None
        self._Resolution = None
        self._ResultUrl = None
        self._Status = None
        self._TaskId = None
        self._Title = None
        self._ThumbnailUrl = None
        self._ThumbnailResolution = None
        self._CompressFileUrl = None
        self._ResourceListUrl = None
        self._Ext = None
        self._CreateTime = None
        self._AssignTime = None
        self._FinishedTime = None
        self._RequestId = None

    @property
    def Pages(self):
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        self._Pages = Pages

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def ResultUrl(self):
        return self._ResultUrl

    @ResultUrl.setter
    def ResultUrl(self, ResultUrl):
        self._ResultUrl = ResultUrl

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def ThumbnailUrl(self):
        return self._ThumbnailUrl

    @ThumbnailUrl.setter
    def ThumbnailUrl(self, ThumbnailUrl):
        self._ThumbnailUrl = ThumbnailUrl

    @property
    def ThumbnailResolution(self):
        return self._ThumbnailResolution

    @ThumbnailResolution.setter
    def ThumbnailResolution(self, ThumbnailResolution):
        self._ThumbnailResolution = ThumbnailResolution

    @property
    def CompressFileUrl(self):
        return self._CompressFileUrl

    @CompressFileUrl.setter
    def CompressFileUrl(self, CompressFileUrl):
        self._CompressFileUrl = CompressFileUrl

    @property
    def ResourceListUrl(self):
        return self._ResourceListUrl

    @ResourceListUrl.setter
    def ResourceListUrl(self, ResourceListUrl):
        self._ResourceListUrl = ResourceListUrl

    @property
    def Ext(self):
        return self._Ext

    @Ext.setter
    def Ext(self, Ext):
        self._Ext = Ext

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def AssignTime(self):
        return self._AssignTime

    @AssignTime.setter
    def AssignTime(self, AssignTime):
        self._AssignTime = AssignTime

    @property
    def FinishedTime(self):
        return self._FinishedTime

    @FinishedTime.setter
    def FinishedTime(self, FinishedTime):
        self._FinishedTime = FinishedTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Pages = params.get("Pages")
        self._Progress = params.get("Progress")
        self._Resolution = params.get("Resolution")
        self._ResultUrl = params.get("ResultUrl")
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        self._Title = params.get("Title")
        self._ThumbnailUrl = params.get("ThumbnailUrl")
        self._ThumbnailResolution = params.get("ThumbnailResolution")
        self._CompressFileUrl = params.get("CompressFileUrl")
        self._ResourceListUrl = params.get("ResourceListUrl")
        self._Ext = params.get("Ext")
        self._CreateTime = params.get("CreateTime")
        self._AssignTime = params.get("AssignTime")
        self._FinishedTime = params.get("FinishedTime")
        self._RequestId = params.get("RequestId")


class DescribeTranscodeSearchRequest(AbstractModel):
    """DescribeTranscodeSearch request structure.

    """


class DescribeTranscodeSearchResponse(AbstractModel):
    """DescribeTranscodeSearch response structure.

    """

    def __init__(self):
        r"""
        :param _TranscodeTaskSet: The set of queried transcoding tasks.
        :type TranscodeTaskSet: list of TranscodeTaskSearchResult
        :param _TotalCount: Number of transcoding tasks.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TranscodeTaskSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def TranscodeTaskSet(self):
        return self._TranscodeTaskSet

    @TranscodeTaskSet.setter
    def TranscodeTaskSet(self, TranscodeTaskSet):
        self._TranscodeTaskSet = TranscodeTaskSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TranscodeTaskSet") is not None:
            self._TranscodeTaskSet = []
            for item in params.get("TranscodeTaskSet"):
                obj = TranscodeTaskSearchResult()
                obj._deserialize(item)
                self._TranscodeTaskSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeUsageSummaryRequest(AbstractModel):
    """DescribeUsageSummary request structure.

    """

    def __init__(self):
        r"""
        :param _BeginTime: Start time of the query period.
        :type BeginTime: str
        :param _EndTime: End time of the query period.
        :type EndTime: str
        :param _SubProducts: Subproducts whose usage you want to query.
        :type SubProducts: list of str
        :param _IsWeighted: true: Returns weighted data.
false: Returns raw data.
        :type IsWeighted: bool
        """
        self._BeginTime = None
        self._EndTime = None
        self._SubProducts = None
        self._IsWeighted = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SubProducts(self):
        return self._SubProducts

    @SubProducts.setter
    def SubProducts(self, SubProducts):
        self._SubProducts = SubProducts

    @property
    def IsWeighted(self):
        return self._IsWeighted

    @IsWeighted.setter
    def IsWeighted(self, IsWeighted):
        self._IsWeighted = IsWeighted


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._SubProducts = params.get("SubProducts")
        self._IsWeighted = params.get("IsWeighted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsageSummaryResponse(AbstractModel):
    """DescribeUsageSummary response structure.

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


class DescribeUserListRequest(AbstractModel):
    """DescribeUserList request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _RoomId: Room ID to be used to query users.
        :type RoomId: str
        :param _TimeRange: Query period, which consists of two Unix timestamps in milliseconds. The first indicates the start time and the second the end time.
        :type TimeRange: list of int
        :param _Query: Extra query conditions.
        :type Query: str
        :param _MaxSize: Maximum number of data entries to be returned. Default value: `1000`.
        :type MaxSize: int
        """
        self._SdkAppId = None
        self._RoomId = None
        self._TimeRange = None
        self._Query = None
        self._MaxSize = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def TimeRange(self):
        return self._TimeRange

    @TimeRange.setter
    def TimeRange(self, TimeRange):
        self._TimeRange = TimeRange

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._TimeRange = params.get("TimeRange")
        self._Query = params.get("Query")
        self._MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserListResponse(AbstractModel):
    """DescribeUserList response structure.

    """

    def __init__(self):
        r"""
        :param _UserList: User list of the room.
        :type UserList: list of UserListItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UserList = None
        self._RequestId = None

    @property
    def UserList(self):
        return self._UserList

    @UserList.setter
    def UserList(self, UserList):
        self._UserList = UserList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UserList") is not None:
            self._UserList = []
            for item in params.get("UserList"):
                obj = UserListItem()
                obj._deserialize(item)
                self._UserList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserResourcesRequest(AbstractModel):
    """DescribeUserResources request structure.

    """


class DescribeUserResourcesResponse(AbstractModel):
    """DescribeUserResources response structure.

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


class DescribeUserStatusRequest(AbstractModel):
    """DescribeUserStatus request structure.

    """


class DescribeUserStatusResponse(AbstractModel):
    """DescribeUserStatus response structure.

    """

    def __init__(self):
        r"""
        :param _AppId: AppId of the customer.
        :type AppId: int
        :param _IsTiwUser: Specifies whether the whiteboard service of the trial or official edition is activated before.

0: The whiteboard service is not activated.
1: The whiteboard service is activated.
        :type IsTiwUser: int
        :param _IsSaaSUser: Specifies whether the interactive class feature of the trial or official edition is activated before.
        :type IsSaaSUser: int
        :param _IsTiwOfflineRecordUser: Specifies whether the user uses the offline recording feature of the whiteboard service.
        :type IsTiwOfflineRecordUser: int
        :param _IsAuthenticated: Specifies whether the user is authenticated.
        :type IsAuthenticated: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AppId = None
        self._IsTiwUser = None
        self._IsSaaSUser = None
        self._IsTiwOfflineRecordUser = None
        self._IsAuthenticated = None
        self._RequestId = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def IsTiwUser(self):
        return self._IsTiwUser

    @IsTiwUser.setter
    def IsTiwUser(self, IsTiwUser):
        self._IsTiwUser = IsTiwUser

    @property
    def IsSaaSUser(self):
        return self._IsSaaSUser

    @IsSaaSUser.setter
    def IsSaaSUser(self, IsSaaSUser):
        self._IsSaaSUser = IsSaaSUser

    @property
    def IsTiwOfflineRecordUser(self):
        return self._IsTiwOfflineRecordUser

    @IsTiwOfflineRecordUser.setter
    def IsTiwOfflineRecordUser(self, IsTiwOfflineRecordUser):
        self._IsTiwOfflineRecordUser = IsTiwOfflineRecordUser

    @property
    def IsAuthenticated(self):
        return self._IsAuthenticated

    @IsAuthenticated.setter
    def IsAuthenticated(self, IsAuthenticated):
        self._IsAuthenticated = IsAuthenticated

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._IsTiwUser = params.get("IsTiwUser")
        self._IsSaaSUser = params.get("IsSaaSUser")
        self._IsTiwOfflineRecordUser = params.get("IsTiwOfflineRecordUser")
        self._IsAuthenticated = params.get("IsAuthenticated")
        self._RequestId = params.get("RequestId")


class DescribeVideoGenerationTaskCallbackRequest(AbstractModel):
    """DescribeVideoGenerationTaskCallback request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        """
        self._SdkAppId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoGenerationTaskCallbackResponse(AbstractModel):
    """DescribeVideoGenerationTaskCallback response structure.

    """

    def __init__(self):
        r"""
        :param _Callback: Callback URL for recording video generation.
        :type Callback: str
        :param _CallbackKey: Callback authentication key for recording video generation.
        :type CallbackKey: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Callback = None
        self._CallbackKey = None
        self._RequestId = None

    @property
    def Callback(self):
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Callback = params.get("Callback")
        self._CallbackKey = params.get("CallbackKey")
        self._RequestId = params.get("RequestId")


class DescribeVideoGenerationTaskRequest(AbstractModel):
    """DescribeVideoGenerationTask request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _TaskId: ID of the recording video generation task.
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoGenerationTaskResponse(AbstractModel):
    """DescribeVideoGenerationTask response structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Group ID corresponding to the task.
        :type GroupId: str
        :param _RoomId: Room ID corresponding to the task.
        :type RoomId: int
        :param _TaskId: Task ID.
        :type TaskId: str
        :param _Progress: Disused.
        :type Progress: int
        :param _Status: Status of the recording video generation task. Valid values:
- QUEUED: Queuing.
- PROCESSING: Video generation in progress.
- FINISHED: Video generation finished. (To determine whether the task succeeded or failed, check the error code and message.)
        :type Status: str
        :param _TotalTime: Total video playback duration. Unit: milliseconds.
        :type TotalTime: int
        :param _VideoInfos: Disused. Use the `VideoInfoList` parameter.
        :type VideoInfos: :class:`tencentcloud.tiw.v20190919.models.VideoInfo`
        :param _VideoInfoList: List of videos generated by the recording video generation tasks.
        :type VideoInfoList: list of VideoInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GroupId = None
        self._RoomId = None
        self._TaskId = None
        self._Progress = None
        self._Status = None
        self._TotalTime = None
        self._VideoInfos = None
        self._VideoInfoList = None
        self._RequestId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TotalTime(self):
        return self._TotalTime

    @TotalTime.setter
    def TotalTime(self, TotalTime):
        self._TotalTime = TotalTime

    @property
    def VideoInfos(self):
        return self._VideoInfos

    @VideoInfos.setter
    def VideoInfos(self, VideoInfos):
        self._VideoInfos = VideoInfos

    @property
    def VideoInfoList(self):
        return self._VideoInfoList

    @VideoInfoList.setter
    def VideoInfoList(self, VideoInfoList):
        self._VideoInfoList = VideoInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RoomId = params.get("RoomId")
        self._TaskId = params.get("TaskId")
        self._Progress = params.get("Progress")
        self._Status = params.get("Status")
        self._TotalTime = params.get("TotalTime")
        if params.get("VideoInfos") is not None:
            self._VideoInfos = VideoInfo()
            self._VideoInfos._deserialize(params.get("VideoInfos"))
        if params.get("VideoInfoList") is not None:
            self._VideoInfoList = []
            for item in params.get("VideoInfoList"):
                obj = VideoInfo()
                obj._deserialize(item)
                self._VideoInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWhiteboardApplicationConfigRequest(AbstractModel):
    """DescribeWhiteboardApplicationConfig request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _TaskTypes: Task types to be queried.
recording: Real-time recording.
transcode: Document transcoding.
        :type TaskTypes: list of str
        :param _SdkAppIds: SdkAppIds to be used to query configurations.
        :type SdkAppIds: list of int
        """
        self._SdkAppId = None
        self._TaskTypes = None
        self._SdkAppIds = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskTypes(self):
        return self._TaskTypes

    @TaskTypes.setter
    def TaskTypes(self, TaskTypes):
        self._TaskTypes = TaskTypes

    @property
    def SdkAppIds(self):
        return self._SdkAppIds

    @SdkAppIds.setter
    def SdkAppIds(self, SdkAppIds):
        self._SdkAppIds = SdkAppIds


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskTypes = params.get("TaskTypes")
        self._SdkAppIds = params.get("SdkAppIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteboardApplicationConfigResponse(AbstractModel):
    """DescribeWhiteboardApplicationConfig response structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _Configs: Task-related configurations of the whiteboard application.
        :type Configs: list of WhiteboardApplicationConfig
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SdkAppId = None
        self._Configs = None
        self._RequestId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Configs(self):
        return self._Configs

    @Configs.setter
    def Configs(self, Configs):
        self._Configs = Configs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        if params.get("Configs") is not None:
            self._Configs = []
            for item in params.get("Configs"):
                obj = WhiteboardApplicationConfig()
                obj._deserialize(item)
                self._Configs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWhiteboardBucketConfigRequest(AbstractModel):
    """DescribeWhiteboardBucketConfig request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _TaskType: Task type to be queried.
recording: Real-time recording.
transcode: Document transcoding.
        :type TaskType: str
        """
        self._SdkAppId = None
        self._TaskType = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteboardBucketConfigResponse(AbstractModel):
    """DescribeWhiteboardBucketConfig response structure.

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


class DescribeWhiteboardPushCallbackRequest(AbstractModel):
    """DescribeWhiteboardPushCallback request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        """
        self._SdkAppId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteboardPushCallbackResponse(AbstractModel):
    """DescribeWhiteboardPushCallback response structure.

    """

    def __init__(self):
        r"""
        :param _Callback: Callback URL of the whiteboard push event. If no callback URL is set, this parameter is null.
        :type Callback: str
        :param _CallbackKey: Callback authentication key for whiteboard push.
        :type CallbackKey: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Callback = None
        self._CallbackKey = None
        self._RequestId = None

    @property
    def Callback(self):
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Callback = params.get("Callback")
        self._CallbackKey = params.get("CallbackKey")
        self._RequestId = params.get("RequestId")


class DescribeWhiteboardPushRequest(AbstractModel):
    """DescribeWhiteboardPush request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _TaskId: ID of the whiteboard push task.
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteboardPushResponse(AbstractModel):
    """DescribeWhiteboardPush response structure.

    """

    def __init__(self):
        r"""
        :param _FinishReason: Reason for push stop.
- AUTO: Pushing automatically stops because no upstream audio/video or whiteboard operation occurs in the room for a long time.
- USER_CALL: The API for stopping pushing is called.
- EXCEPTION: An exception occurred.
        :type FinishReason: str
        :param _TaskId: ID of the whiteboard push task.
        :type TaskId: str
        :param _Status: Status of the push task.
- PREPARED: Push in preparation (including entering the room and starting the push service).
- PUSHING: Pushing in progress.
- STOPPED: Pushing stopped.
        :type Status: str
        :param _RoomId: Room ID.
        :type RoomId: int
        :param _GroupId: Group ID of the whiteboard.
        :type GroupId: str
        :param _PushUserId: User ID of the push task.
        :type PushUserId: str
        :param _PushStartTime: Actual push start time, which is a Unix timestamp in seconds.
        :type PushStartTime: int
        :param _PushStopTime: Actual push stop time, which is a Unix timestamp in seconds.
        :type PushStopTime: int
        :param _ExceptionCnt: Number of exceptions during push.
        :type ExceptionCnt: int
        :param _IMSyncTime: IM timestamp corresponding to the first frame of the whiteboard push video. The timestamp is used for time synchronization between IM messages and the whiteboard push video during playback.
        :type IMSyncTime: int
        :param _Backup: Result information of the backup push task.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Backup: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FinishReason = None
        self._TaskId = None
        self._Status = None
        self._RoomId = None
        self._GroupId = None
        self._PushUserId = None
        self._PushStartTime = None
        self._PushStopTime = None
        self._ExceptionCnt = None
        self._IMSyncTime = None
        self._Backup = None
        self._RequestId = None

    @property
    def FinishReason(self):
        return self._FinishReason

    @FinishReason.setter
    def FinishReason(self, FinishReason):
        self._FinishReason = FinishReason

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def PushUserId(self):
        return self._PushUserId

    @PushUserId.setter
    def PushUserId(self, PushUserId):
        self._PushUserId = PushUserId

    @property
    def PushStartTime(self):
        return self._PushStartTime

    @PushStartTime.setter
    def PushStartTime(self, PushStartTime):
        self._PushStartTime = PushStartTime

    @property
    def PushStopTime(self):
        return self._PushStopTime

    @PushStopTime.setter
    def PushStopTime(self, PushStopTime):
        self._PushStopTime = PushStopTime

    @property
    def ExceptionCnt(self):
        return self._ExceptionCnt

    @ExceptionCnt.setter
    def ExceptionCnt(self, ExceptionCnt):
        self._ExceptionCnt = ExceptionCnt

    @property
    def IMSyncTime(self):
        return self._IMSyncTime

    @IMSyncTime.setter
    def IMSyncTime(self, IMSyncTime):
        self._IMSyncTime = IMSyncTime

    @property
    def Backup(self):
        return self._Backup

    @Backup.setter
    def Backup(self, Backup):
        self._Backup = Backup

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FinishReason = params.get("FinishReason")
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._RoomId = params.get("RoomId")
        self._GroupId = params.get("GroupId")
        self._PushUserId = params.get("PushUserId")
        self._PushStartTime = params.get("PushStartTime")
        self._PushStopTime = params.get("PushStopTime")
        self._ExceptionCnt = params.get("ExceptionCnt")
        self._IMSyncTime = params.get("IMSyncTime")
        self._Backup = params.get("Backup")
        self._RequestId = params.get("RequestId")


class DescribeWhiteboardPushSearchRequest(AbstractModel):
    """DescribeWhiteboardPushSearch request structure.

    """


class DescribeWhiteboardPushSearchResponse(AbstractModel):
    """DescribeWhiteboardPushSearch response structure.

    """

    def __init__(self):
        r"""
        :param _WhiteboardPushTaskSet: The set of queried push tasks.
        :type WhiteboardPushTaskSet: list of WhiteboardPushTaskSearchResult
        :param _TotalCount: Number of push tasks.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._WhiteboardPushTaskSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def WhiteboardPushTaskSet(self):
        return self._WhiteboardPushTaskSet

    @WhiteboardPushTaskSet.setter
    def WhiteboardPushTaskSet(self, WhiteboardPushTaskSet):
        self._WhiteboardPushTaskSet = WhiteboardPushTaskSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("WhiteboardPushTaskSet") is not None:
            self._WhiteboardPushTaskSet = []
            for item in params.get("WhiteboardPushTaskSet"):
                obj = WhiteboardPushTaskSearchResult()
                obj._deserialize(item)
                self._WhiteboardPushTaskSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class Detail(AbstractModel):
    """Detailed metric data with different tags in billable usage data.

    """

    def __init__(self):
        r"""
        :param _TagName: Usage metric.
        :type TagName: str
        :param _Weight: Usage weight.
        :type Weight: float
        :param _Value: Usage value.
        :type Value: float
        """
        self._TagName = None
        self._Weight = None
        self._Value = None

    @property
    def TagName(self):
        return self._TagName

    @TagName.setter
    def TagName(self, TagName):
        self._TagName = TagName

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._TagName = params.get("TagName")
        self._Weight = params.get("Weight")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Interrupt(AbstractModel):
    """Number of video stream interruptions during real-time recording.

    """

    def __init__(self):
        r"""
        :param _UserId: User ID.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type UserId: str
        :param _Count: Number of video stream interruptions.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Count: int
        """
        self._UserId = None
        self._Count = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LayoutParams(AbstractModel):
    """Custom mixed stream layout parameter

    """

    def __init__(self):
        r"""
        :param _Width: Stream image width. Value range: [2,3000]
        :type Width: int
        :param _Height: Stream image height. Value range: [2,3000]
        :type Height: int
        :param _X: Offset of the top point in the upper-left corner of the current image to the X axis of the top point in the upper-left corner of the canvas. Default value: 0. Value range: [0,3000].
        :type X: int
        :param _Y: Offset of the top point in the upper-left corner of the current image to the Y axis of the top point in the upper-left corner of the canvas. Default value: 0. Value range: [0,3000].
        :type Y: int
        :param _ZOrder: Z-axis position of the image. The default value is 0.
The Z axis determines the overlap sequence of images. The image with the largest z-axis value is at the top layer.
        :type ZOrder: int
        """
        self._Width = None
        self._Height = None
        self._X = None
        self._Y = None
        self._ZOrder = None

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def X(self):
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def ZOrder(self):
        return self._ZOrder

    @ZOrder.setter
    def ZOrder(self, ZOrder):
        self._ZOrder = ZOrder


    def _deserialize(self, params):
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._ZOrder = params.get("ZOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixStream(AbstractModel):
    """Stream mixing configuration

    """

    def __init__(self):
        r"""
        :param _Enabled: Whether stream mixing is enabled
        :type Enabled: bool
        :param _DisableAudio: Whether audio stream mixing is disabled
        :type DisableAudio: bool
        :param _ModelId: ID of the embedded mixed stream layout template. Valid values: 1 and 2. For more information on the differences of both values, see the sample embedded mixed stream layout template.
If the Custom field is not specified, ModelId is required.
        :type ModelId: int
        :param _TeacherId: ID of a teacher account
This field is valid only when ModelId is specified.
If you specify TeacherID for a user, the user's video stream will be displayed in the first image of the embedded template.
        :type TeacherId: str
        :param _Custom: Custom mixed stream layout parameter
If this parameter is available, the ModelId and TeacherId fields will be ignored.
        :type Custom: :class:`tencentcloud.tiw.v20190919.models.CustomLayout`
        """
        self._Enabled = None
        self._DisableAudio = None
        self._ModelId = None
        self._TeacherId = None
        self._Custom = None

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def DisableAudio(self):
        return self._DisableAudio

    @DisableAudio.setter
    def DisableAudio(self, DisableAudio):
        self._DisableAudio = DisableAudio

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def TeacherId(self):
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def Custom(self):
        return self._Custom

    @Custom.setter
    def Custom(self, Custom):
        self._Custom = Custom


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._DisableAudio = params.get("DisableAudio")
        self._ModelId = params.get("ModelId")
        self._TeacherId = params.get("TeacherId")
        if params.get("Custom") is not None:
            self._Custom = CustomLayout()
            self._Custom._deserialize(params.get("Custom"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationRequest(AbstractModel):
    """ModifyApplication request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _AppName: Application name.
        :type AppName: str
        """
        self._SdkAppId = None
        self._AppName = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationResponse(AbstractModel):
    """ModifyApplication response structure.

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


class ModifyAutoRenewFlagRequest(AbstractModel):
    """ModifyAutoRenewFlag request structure.

    """

    def __init__(self):
        r"""
        :param _SubProduct: Subproduct ID. To obtain this ID, call the `DescribeUserResources` API and find the subproduct ID of the monthly feature package with the level 1. Usually the value is `sp_tiw_package`.
        :type SubProduct: str
        :param _ResourceId: Resource ID. To obtain this ID, call the `DescribeUserResources` API and find the resource ID of the monthly feature package with the level 1.
        :type ResourceId: str
        :param _AutoRenewFlag: Renewal mode. Valid values: `0` (default mode, which is auto-renewal), `1` (auto-renewal), `2` (manual renewal, which is specified by users). If no renewal is required, set it to `0`.
        :type AutoRenewFlag: int
        """
        self._SubProduct = None
        self._ResourceId = None
        self._AutoRenewFlag = None

    @property
    def SubProduct(self):
        return self._SubProduct

    @SubProduct.setter
    def SubProduct(self, SubProduct):
        self._SubProduct = SubProduct

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag


    def _deserialize(self, params):
        self._SubProduct = params.get("SubProduct")
        self._ResourceId = params.get("ResourceId")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoRenewFlagResponse(AbstractModel):
    """ModifyAutoRenewFlag response structure.

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


class ModifyWhiteboardApplicationConfigRequest(AbstractModel):
    """ModifyWhiteboardApplicationConfig request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _Configs: Task-related configurations of the whiteboard application.
        :type Configs: list of WhiteboardApplicationConfig
        """
        self._SdkAppId = None
        self._Configs = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Configs(self):
        return self._Configs

    @Configs.setter
    def Configs(self, Configs):
        self._Configs = Configs


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        if params.get("Configs") is not None:
            self._Configs = []
            for item in params.get("Configs"):
                obj = WhiteboardApplicationConfig()
                obj._deserialize(item)
                self._Configs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWhiteboardApplicationConfigResponse(AbstractModel):
    """ModifyWhiteboardApplicationConfig response structure.

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


class ModifyWhiteboardBucketConfigRequest(AbstractModel):
    """ModifyWhiteboardBucketConfig request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _TaskType: Task type to be queried.
recording: Real-time recording.
transcode: Document transcoding.
        :type TaskType: str
        :param _BucketName: Name of the COS bucket.
        :type BucketName: str
        :param _BucketLocation: Region of the COS bucket.
        :type BucketLocation: str
        :param _BucketPrefix: Resource prefix of the bucket.
        :type BucketPrefix: str
        :param _ResultDomain: Domain name of the URL of the bucket.
        :type ResultDomain: str
        """
        self._SdkAppId = None
        self._TaskType = None
        self._BucketName = None
        self._BucketLocation = None
        self._BucketPrefix = None
        self._ResultDomain = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def BucketName(self):
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def BucketLocation(self):
        return self._BucketLocation

    @BucketLocation.setter
    def BucketLocation(self, BucketLocation):
        self._BucketLocation = BucketLocation

    @property
    def BucketPrefix(self):
        return self._BucketPrefix

    @BucketPrefix.setter
    def BucketPrefix(self, BucketPrefix):
        self._BucketPrefix = BucketPrefix

    @property
    def ResultDomain(self):
        return self._ResultDomain

    @ResultDomain.setter
    def ResultDomain(self, ResultDomain):
        self._ResultDomain = ResultDomain


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskType = params.get("TaskType")
        self._BucketName = params.get("BucketName")
        self._BucketLocation = params.get("BucketLocation")
        self._BucketPrefix = params.get("BucketPrefix")
        self._ResultDomain = params.get("ResultDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWhiteboardBucketConfigResponse(AbstractModel):
    """ModifyWhiteboardBucketConfig response structure.

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


class OmittedDuration(AbstractModel):
    """Duration to be ignored in the spliced video

    """

    def __init__(self):
        r"""
        :param _VideoTime: Offset of the paused time in the spliced video, in milliseconds
        :type VideoTime: int
        :param _PauseTime: Recording pause timestamp, in milliseconds
        :type PauseTime: int
        :param _ResumeTime: Recording resumption timestamp, in milliseconds
        :type ResumeTime: int
        """
        self._VideoTime = None
        self._PauseTime = None
        self._ResumeTime = None

    @property
    def VideoTime(self):
        return self._VideoTime

    @VideoTime.setter
    def VideoTime(self, VideoTime):
        self._VideoTime = VideoTime

    @property
    def PauseTime(self):
        return self._PauseTime

    @PauseTime.setter
    def PauseTime(self, PauseTime):
        self._PauseTime = PauseTime

    @property
    def ResumeTime(self):
        return self._ResumeTime

    @ResumeTime.setter
    def ResumeTime(self, ResumeTime):
        self._ResumeTime = ResumeTime


    def _deserialize(self, params):
        self._VideoTime = params.get("VideoTime")
        self._PauseTime = params.get("PauseTime")
        self._ResumeTime = params.get("ResumeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseOnlineRecordRequest(AbstractModel):
    """PauseOnlineRecord request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the customer
        :type SdkAppId: int
        :param _TaskId: ID of the real-time recording task
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseOnlineRecordResponse(AbstractModel):
    """PauseOnlineRecord response structure.

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


class RecordControl(AbstractModel):
    """It specifies the global recording parameters and the recording parameters over a specific stream. For example, you can specify the streams you want to record and whether to record low-resolution videos only.

    """

    def __init__(self):
        r"""
        :param _Enabled: It specifies whether to enable RecordControl. Valid values: true (yes); false (no).
        :type Enabled: bool
        :param _DisableRecord: A global parameter generally used in conjunction with `StreamControls` that specifies whether to disable recording. Valid values:

true: no stream is recorded.
false: all streams are recorded. Default value: false.

The setting in this parameter is applied to all streams. However, if `StreamControls` is passed in, the parameters in `StreamControls` will take precedence.
        :type DisableRecord: bool
        :param _DisableAudio: A global parameter generally used in conjunction with `StreamControls` that specifies whether to disable audio recording over all streams. Valid values:

true: no audio recording of any streams.
false: audio recording of all streams. Default value: false.

The setting in this parameter is applied to all streams. However, if `StreamControls` is passed in, the parameters in `StreamControls` will take precedence.
        :type DisableAudio: bool
        :param _PullSmallVideo: A global parameter generally used in conjunction with `StreamControls` that specifies whether to record low-resolution videos only. Valid values:

true: only records low-resolution videos for all streams. Please ensure that the up-streaming end pushes the low-resolution videos. Otherwise, the recorded video may be black.
false: high-resolution video recording of all streams. Default value: false.

The setting in this parameter is applied to all streams. However, if `StreamControls` is passed in, the parameters in `StreamControls` will take precedence.
        :type PullSmallVideo: bool
        :param _StreamControls: Parameters over specific streams, which take priority over global configurations. If it’s empty, all streams are recorded according to the global configurations. 
        :type StreamControls: list of StreamControl
        """
        self._Enabled = None
        self._DisableRecord = None
        self._DisableAudio = None
        self._PullSmallVideo = None
        self._StreamControls = None

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def DisableRecord(self):
        return self._DisableRecord

    @DisableRecord.setter
    def DisableRecord(self, DisableRecord):
        self._DisableRecord = DisableRecord

    @property
    def DisableAudio(self):
        return self._DisableAudio

    @DisableAudio.setter
    def DisableAudio(self, DisableAudio):
        self._DisableAudio = DisableAudio

    @property
    def PullSmallVideo(self):
        return self._PullSmallVideo

    @PullSmallVideo.setter
    def PullSmallVideo(self, PullSmallVideo):
        self._PullSmallVideo = PullSmallVideo

    @property
    def StreamControls(self):
        return self._StreamControls

    @StreamControls.setter
    def StreamControls(self, StreamControls):
        self._StreamControls = StreamControls


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._DisableRecord = params.get("DisableRecord")
        self._DisableAudio = params.get("DisableAudio")
        self._PullSmallVideo = params.get("PullSmallVideo")
        if params.get("StreamControls") is not None:
            self._StreamControls = []
            for item in params.get("StreamControls"):
                obj = StreamControl()
                obj._deserialize(item)
                self._StreamControls.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordTaskResult(AbstractModel):
    """Real-time recording result.

    """

    def __init__(self):
        r"""
        :param _FinishReason: `AUTO`: Recording automatically stops. `USER_CALL`: The API for stopping recording is called.
        :type FinishReason: str
        :param _ExceptionCnt: Number of exceptions.
        :type ExceptionCnt: int
        :param _RoomId: Room ID.
        :type RoomId: int
        :param _GroupId: Group ID.
        :type GroupId: str
        :param _RecordStartTime: Actual recording start time.
        :type RecordStartTime: int
        :param _RecordStopTime: Recording end time.
        :type RecordStopTime: int
        :param _TotalTime: Recording duration.
        :type TotalTime: int
        :param _VideoInfos: List of video information.
        :type VideoInfos: list of VideoInfo
        :param _OmittedDurations: Omitted video durations.
        :type OmittedDurations: list of OmittedDuration
        :param _Details: Details.
        :type Details: str
        :param _ErrorCode: Task execution error code.
        :type ErrorCode: int
        :param _ErrorMsg: Error message.
        :type ErrorMsg: str
        """
        self._FinishReason = None
        self._ExceptionCnt = None
        self._RoomId = None
        self._GroupId = None
        self._RecordStartTime = None
        self._RecordStopTime = None
        self._TotalTime = None
        self._VideoInfos = None
        self._OmittedDurations = None
        self._Details = None
        self._ErrorCode = None
        self._ErrorMsg = None

    @property
    def FinishReason(self):
        return self._FinishReason

    @FinishReason.setter
    def FinishReason(self, FinishReason):
        self._FinishReason = FinishReason

    @property
    def ExceptionCnt(self):
        return self._ExceptionCnt

    @ExceptionCnt.setter
    def ExceptionCnt(self, ExceptionCnt):
        self._ExceptionCnt = ExceptionCnt

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RecordStartTime(self):
        return self._RecordStartTime

    @RecordStartTime.setter
    def RecordStartTime(self, RecordStartTime):
        self._RecordStartTime = RecordStartTime

    @property
    def RecordStopTime(self):
        return self._RecordStopTime

    @RecordStopTime.setter
    def RecordStopTime(self, RecordStopTime):
        self._RecordStopTime = RecordStopTime

    @property
    def TotalTime(self):
        return self._TotalTime

    @TotalTime.setter
    def TotalTime(self, TotalTime):
        self._TotalTime = TotalTime

    @property
    def VideoInfos(self):
        return self._VideoInfos

    @VideoInfos.setter
    def VideoInfos(self, VideoInfos):
        self._VideoInfos = VideoInfos

    @property
    def OmittedDurations(self):
        return self._OmittedDurations

    @OmittedDurations.setter
    def OmittedDurations(self, OmittedDurations):
        self._OmittedDurations = OmittedDurations

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg


    def _deserialize(self, params):
        self._FinishReason = params.get("FinishReason")
        self._ExceptionCnt = params.get("ExceptionCnt")
        self._RoomId = params.get("RoomId")
        self._GroupId = params.get("GroupId")
        self._RecordStartTime = params.get("RecordStartTime")
        self._RecordStopTime = params.get("RecordStopTime")
        self._TotalTime = params.get("TotalTime")
        if params.get("VideoInfos") is not None:
            self._VideoInfos = []
            for item in params.get("VideoInfos"):
                obj = VideoInfo()
                obj._deserialize(item)
                self._VideoInfos.append(obj)
        if params.get("OmittedDurations") is not None:
            self._OmittedDurations = []
            for item in params.get("OmittedDurations"):
                obj = OmittedDuration()
                obj._deserialize(item)
                self._OmittedDurations.append(obj)
        self._Details = params.get("Details")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMsg = params.get("ErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordTaskSearchResult(AbstractModel):
    """Real-time recording task query results.

    """

    def __init__(self):
        r"""
        :param _TaskId: Unique task ID.
        :type TaskId: str
        :param _Status: Status of the real-time recording task.
- PAUSED: Recording paused.
- PREPARED: Recording in preparation.
- RECORDING: Recording in progress.
- STOPPED: Recording stopped.
- FINISHED: Recording finished.
        :type Status: str
        :param _RoomId: Room ID of the real-time recording task.
        :type RoomId: int
        :param _CreateTime: Creation time of the task.
        :type CreateTime: str
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _Result: Real-time recording result.
        :type Result: :class:`tencentcloud.tiw.v20190919.models.RecordTaskResult`
        """
        self._TaskId = None
        self._Status = None
        self._RoomId = None
        self._CreateTime = None
        self._SdkAppId = None
        self._Result = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._RoomId = params.get("RoomId")
        self._CreateTime = params.get("CreateTime")
        self._SdkAppId = params.get("SdkAppId")
        if params.get("Result") is not None:
            self._Result = RecordTaskResult()
            self._Result._deserialize(params.get("Result"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeOnlineRecordRequest(AbstractModel):
    """ResumeOnlineRecord request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the customer
        :type SdkAppId: int
        :param _TaskId: ID of the resumed real-time recording task
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeOnlineRecordResponse(AbstractModel):
    """ResumeOnlineRecord response structure.

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


class RoomListItem(AbstractModel):
    """Whiteboard room data returned for log queries.

    """

    def __init__(self):
        r"""
        :param _RoomId: Room ID.
        :type RoomId: str
        :param _StartTime: The first time when the room ID appeared during the queried period, which is a Unix timestamp in milliseconds.
        :type StartTime: int
        :param _EndTime: The last time when the room ID appeared during the queried period, which is a Unix timestamp in milliseconds.
        :type EndTime: int
        :param _UserNumber: Number of users in the room.
        :type UserNumber: int
        """
        self._RoomId = None
        self._StartTime = None
        self._EndTime = None
        self._UserNumber = None

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def UserNumber(self):
        return self._UserNumber

    @UserNumber.setter
    def UserNumber(self, UserNumber):
        self._UserNumber = UserNumber


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._UserNumber = params.get("UserNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoomUsageDataItem(AbstractModel):
    """Usage information of the room.

    """

    def __init__(self):
        r"""
        :param _Time: Start date in the format of YYYY-MM-DD.
        :type Time: str
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _SubProduct: Subproduct usage information, which is consistent with the corresponding request parameters.
- sp_tiw_board: The duration of use of whiteboards.
- sp_tiw_ric: The duration of real-time recording.
        :type SubProduct: str
        :param _Value: Usage values.
- The unit of sp_tiw_board and sp_tiw_ric is minutes.
        :type Value: float
        :param _RoomID: 
        :type RoomID: int
        """
        self._Time = None
        self._SdkAppId = None
        self._SubProduct = None
        self._Value = None
        self._RoomID = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SubProduct(self):
        return self._SubProduct

    @SubProduct.setter
    def SubProduct(self, SubProduct):
        self._SubProduct = SubProduct

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def RoomID(self):
        return self._RoomID

    @RoomID.setter
    def RoomID(self, RoomID):
        self._RoomID = RoomID


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._SdkAppId = params.get("SdkAppId")
        self._SubProduct = params.get("SubProduct")
        self._Value = params.get("Value")
        self._RoomID = params.get("RoomID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetOnlineRecordCallbackKeyRequest(AbstractModel):
    """SetOnlineRecordCallbackKey request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the application
        :type SdkAppId: int
        :param _CallbackKey: Authentication key for the real-time recording callback. It is a string that can have up to 64 characters. If an empty string is passed in, the existing callback authentication key will be deleted. For more information, please [see here](https://www.tencentcloud.com/document/product/1176/55569).
        :type CallbackKey: str
        """
        self._SdkAppId = None
        self._CallbackKey = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetOnlineRecordCallbackKeyResponse(AbstractModel):
    """SetOnlineRecordCallbackKey response structure.

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


class SetOnlineRecordCallbackRequest(AbstractModel):
    """SetOnlineRecordCallback request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the customer
        :type SdkAppId: int
        :param _Callback: Callback address of the real-time recording task result. If an empty string is passed in, the existing callback address will be deleted. The callback address only supports the HTTP or HTTPS protocol, so the callback address must start with `http://` or `https://`. For the callback format, please [see here](https://www.tencentcloud.com/document/product/1176/55569).
        :type Callback: str
        """
        self._SdkAppId = None
        self._Callback = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Callback(self):
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Callback = params.get("Callback")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetOnlineRecordCallbackResponse(AbstractModel):
    """SetOnlineRecordCallback response structure.

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


class SetTranscodeCallbackKeyRequest(AbstractModel):
    """SetTranscodeCallbackKey request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the application
        :type SdkAppId: int
        :param _CallbackKey: Authentication key for the document transcoding callback. It is a string that can have up to 64 characters. If an empty string is passed in, the existing callback authentication key will be deleted. For more information about callback authentication, please [see here](https://www.tencentcloud.com/document/product/1176/55569).
        :type CallbackKey: str
        """
        self._SdkAppId = None
        self._CallbackKey = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetTranscodeCallbackKeyResponse(AbstractModel):
    """SetTranscodeCallbackKey response structure.

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


class SetTranscodeCallbackRequest(AbstractModel):
    """SetTranscodeCallback request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the customer
        :type SdkAppId: int
        :param _Callback: Callback address for the document transcoding progress. If an empty string is passed in, the existing callback address will be deleted. The callback address only supports the HTTP or HTTPS protocol, so the callback address must start with `http://` or `https://`.
For more information about the callback format, please [see here](https://www.tencentcloud.com/document/product/1176/55569).
        :type Callback: str
        """
        self._SdkAppId = None
        self._Callback = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Callback(self):
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Callback = params.get("Callback")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetTranscodeCallbackResponse(AbstractModel):
    """SetTranscodeCallback response structure.

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


class SetVideoGenerationTaskCallbackKeyRequest(AbstractModel):
    """SetVideoGenerationTaskCallbackKey request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _CallbackKey: Callback authentication key for recording video generation. It is a string that can have up to 64 characters. If an empty string is passed in, the existing callback authentication key is deleted.
        :type CallbackKey: str
        """
        self._SdkAppId = None
        self._CallbackKey = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetVideoGenerationTaskCallbackKeyResponse(AbstractModel):
    """SetVideoGenerationTaskCallbackKey response structure.

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


class SetVideoGenerationTaskCallbackRequest(AbstractModel):
    """SetVideoGenerationTaskCallback request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _Callback: Callback URL of the offline recording task result. If it is specified as null, the set callback URL is deleted. The callback URL only supports the HTTP or HTTPS protocol, and therefore the callback URL must start with `http://` or `https://`.
        :type Callback: str
        """
        self._SdkAppId = None
        self._Callback = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Callback(self):
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Callback = params.get("Callback")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetVideoGenerationTaskCallbackResponse(AbstractModel):
    """SetVideoGenerationTaskCallback response structure.

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


class SetWhiteboardPushCallbackKeyRequest(AbstractModel):
    """SetWhiteboardPushCallbackKey request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _CallbackKey: Callback authentication key for whiteboard push. It is a string that can have up to 64 characters. If an empty string is passed in, the existing callback authentication key is deleted. For more information, see [Event Notification](https://www.tencentcloud.com/document/product/1176/55569).
        :type CallbackKey: str
        """
        self._SdkAppId = None
        self._CallbackKey = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetWhiteboardPushCallbackKeyResponse(AbstractModel):
    """SetWhiteboardPushCallbackKey response structure.

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


class SetWhiteboardPushCallbackRequest(AbstractModel):
    """SetWhiteboardPushCallback request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _Callback: Callback URL of the whiteboard push task result. If an empty string is passed in, the existing callback URL is deleted. The callback URL only supports the HTTP or HTTPS protocol, and therefore the callback URL must start with `http://` or `https://`. For the callback format, see [Event Notification](https://www.tencentcloud.com/document/product/1176/55569).
        :type Callback: str
        """
        self._SdkAppId = None
        self._Callback = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Callback(self):
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Callback = params.get("Callback")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetWhiteboardPushCallbackResponse(AbstractModel):
    """SetWhiteboardPushCallback response structure.

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


class SnapshotCOS(AbstractModel):
    """COS bucket parameters for storing whiteboard snapshots.

    """

    def __init__(self):
        r"""
        :param _Uin: UIN of the Tencent Cloud account.
        :type Uin: int
        :param _Region: COS region.
        :type Region: str
        :param _Bucket: COS bucket name.
        :type Bucket: str
        :param _TargetDir: Root directory for storing whiteboard snapshots.
        :type TargetDir: str
        :param _Domain: CDN acceleration domain name.
        :type Domain: str
        """
        self._Uin = None
        self._Region = None
        self._Bucket = None
        self._TargetDir = None
        self._Domain = None

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def TargetDir(self):
        return self._TargetDir

    @TargetDir.setter
    def TargetDir(self, TargetDir):
        self._TargetDir = TargetDir

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._Region = params.get("Region")
        self._Bucket = params.get("Bucket")
        self._TargetDir = params.get("TargetDir")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotResult(AbstractModel):
    """Result of the whiteboard snapshot task.

    """

    def __init__(self):
        r"""
        :param _ErrorCode: Task execution error code.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type ErrorCode: str
        :param _ErrorMessage: Task execution error message.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type ErrorMessage: str
        :param _Total: Number of generated snapshot images.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param _Snapshots: List of URLs of the snapshot images.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Snapshots: list of str
        """
        self._ErrorCode = None
        self._ErrorMessage = None
        self._Total = None
        self._Snapshots = None

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Snapshots(self):
        return self._Snapshots

    @Snapshots.setter
    def Snapshots(self, Snapshots):
        self._Snapshots = Snapshots


    def _deserialize(self, params):
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._Total = params.get("Total")
        self._Snapshots = params.get("Snapshots")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotWhiteboard(AbstractModel):
    """Whiteboard parameters of the whiteboard snapshot task, such as the width and height of the whiteboard.

    """

    def __init__(self):
        r"""
        :param _Width: Whiteboard width. Valid range: [0,2560]. Default value: 1280.
        :type Width: int
        :param _Height: Whiteboard height. Valid range: [0,2560]. Default value: 720.
        :type Height: int
        :param _InitParams: Escaped JSON string of the whiteboard initial parameters, which is passed through to the Tencent Interactive Whiteboard SDK.
        :type InitParams: str
        """
        self._Width = None
        self._Height = None
        self._InitParams = None

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def InitParams(self):
        return self._InitParams

    @InitParams.setter
    def InitParams(self, InitParams):
        self._InitParams = InitParams


    def _deserialize(self, params):
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._InitParams = params.get("InitParams")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartOnlineRecordRequest(AbstractModel):
    """StartOnlineRecord request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the customer
        :type SdkAppId: int
        :param _RoomId: ID of the room for recording. Value range: (1, 4294967295)
        :type RoomId: int
        :param _RecordUserId: User ID used by the recording service for entering a room. The ID cannot exceed 60 bytes in length. Its format is `tic_record_user_${RoomId}_${Random}`, where `${RoomId}` indicates the ID of the room for recording and `${Random}` is a random string.
The ID must be an unused ID in the SDK. The recording service uses the user ID to enter the room for audio, video, and whiteboard recording. If this ID is already used in the SDK, the SDK and recording service will conflict, affecting the recording operation.
        :type RecordUserId: str
        :param _RecordUserSig: Signature corresponding to RecordUserId
        :type RecordUserSig: str
        :param _GroupId: (Disused) IM group ID of the whiteboard. By default, it is the same as the room ID.
        :type GroupId: str
        :param _Concat: Real-time recording video splicing parameter
        :type Concat: :class:`tencentcloud.tiw.v20190919.models.Concat`
        :param _Whiteboard: Real-time recording whiteboard parameter, such as the whiteboard width and height
        :type Whiteboard: :class:`tencentcloud.tiw.v20190919.models.Whiteboard`
        :param _MixStream: Real-time recording stream mixing parameter
Notes:
1. The stream mixing feature needs to be enabled separately. If you need the feature, contact TIW customer service.
2. To use the stream mixing feature, the Extras parameter is required and must contain "MIX_STREAM".
        :type MixStream: :class:`tencentcloud.tiw.v20190919.models.MixStream`
        :param _Extras: List of advanced features used
List of possible values:
MIX_STREAM - Stream mixing feature
        :type Extras: list of str
        :param _AudioFileNeeded: Whether to return the audio-only recording file of different streams in the result callback. The file format is mp3.
        :type AudioFileNeeded: bool
        :param _RecordControl: A group of real-time recording parameters. It specifies the streams to be recorded, whether to disable the audio recording, and whether to record only low-resolution videos, etc.
        :type RecordControl: :class:`tencentcloud.tiw.v20190919.models.RecordControl`
        :param _RecordMode: 
        :type RecordMode: str
        :param _ChatGroupId: 
        :type ChatGroupId: str
        :param _AutoStopTimeout: Recording timeout. Unit: seconds. Valid range: [300,86400]. Default value: 300.

If no upstream audio/video exists or no operation is performed on the whiteboard for the specified period of time, the recording service automatically stops the recording task.
        :type AutoStopTimeout: int
        :param _ExtraData: Internal parameter. You can ignore this parameter.
        :type ExtraData: str
        """
        self._SdkAppId = None
        self._RoomId = None
        self._RecordUserId = None
        self._RecordUserSig = None
        self._GroupId = None
        self._Concat = None
        self._Whiteboard = None
        self._MixStream = None
        self._Extras = None
        self._AudioFileNeeded = None
        self._RecordControl = None
        self._RecordMode = None
        self._ChatGroupId = None
        self._AutoStopTimeout = None
        self._ExtraData = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RecordUserId(self):
        return self._RecordUserId

    @RecordUserId.setter
    def RecordUserId(self, RecordUserId):
        self._RecordUserId = RecordUserId

    @property
    def RecordUserSig(self):
        return self._RecordUserSig

    @RecordUserSig.setter
    def RecordUserSig(self, RecordUserSig):
        self._RecordUserSig = RecordUserSig

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Concat(self):
        return self._Concat

    @Concat.setter
    def Concat(self, Concat):
        self._Concat = Concat

    @property
    def Whiteboard(self):
        return self._Whiteboard

    @Whiteboard.setter
    def Whiteboard(self, Whiteboard):
        self._Whiteboard = Whiteboard

    @property
    def MixStream(self):
        return self._MixStream

    @MixStream.setter
    def MixStream(self, MixStream):
        self._MixStream = MixStream

    @property
    def Extras(self):
        return self._Extras

    @Extras.setter
    def Extras(self, Extras):
        self._Extras = Extras

    @property
    def AudioFileNeeded(self):
        return self._AudioFileNeeded

    @AudioFileNeeded.setter
    def AudioFileNeeded(self, AudioFileNeeded):
        self._AudioFileNeeded = AudioFileNeeded

    @property
    def RecordControl(self):
        return self._RecordControl

    @RecordControl.setter
    def RecordControl(self, RecordControl):
        self._RecordControl = RecordControl

    @property
    def RecordMode(self):
        return self._RecordMode

    @RecordMode.setter
    def RecordMode(self, RecordMode):
        self._RecordMode = RecordMode

    @property
    def ChatGroupId(self):
        return self._ChatGroupId

    @ChatGroupId.setter
    def ChatGroupId(self, ChatGroupId):
        self._ChatGroupId = ChatGroupId

    @property
    def AutoStopTimeout(self):
        return self._AutoStopTimeout

    @AutoStopTimeout.setter
    def AutoStopTimeout(self, AutoStopTimeout):
        self._AutoStopTimeout = AutoStopTimeout

    @property
    def ExtraData(self):
        return self._ExtraData

    @ExtraData.setter
    def ExtraData(self, ExtraData):
        self._ExtraData = ExtraData


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._RecordUserId = params.get("RecordUserId")
        self._RecordUserSig = params.get("RecordUserSig")
        self._GroupId = params.get("GroupId")
        if params.get("Concat") is not None:
            self._Concat = Concat()
            self._Concat._deserialize(params.get("Concat"))
        if params.get("Whiteboard") is not None:
            self._Whiteboard = Whiteboard()
            self._Whiteboard._deserialize(params.get("Whiteboard"))
        if params.get("MixStream") is not None:
            self._MixStream = MixStream()
            self._MixStream._deserialize(params.get("MixStream"))
        self._Extras = params.get("Extras")
        self._AudioFileNeeded = params.get("AudioFileNeeded")
        if params.get("RecordControl") is not None:
            self._RecordControl = RecordControl()
            self._RecordControl._deserialize(params.get("RecordControl"))
        self._RecordMode = params.get("RecordMode")
        self._ChatGroupId = params.get("ChatGroupId")
        self._AutoStopTimeout = params.get("AutoStopTimeout")
        self._ExtraData = params.get("ExtraData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartOnlineRecordResponse(AbstractModel):
    """StartOnlineRecord response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: ID of the real-time recording task
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class StartWhiteboardPushRequest(AbstractModel):
    """StartWhiteboardPush request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _RoomId: Room ID of the whiteboard push task. Valid range: (1,4294967295).

1. By default, the whiteboard push task uses the RoomId string as the GroupID of the IM group. For example, if the RoomId string is 1234, the GroupID of the IM group is also 1234. Message synchronization requires joining a group. Make sure that an IM group is created before the push starts. Otherwise, the push fails.
2. If neither TRTCRoomId nor TRTCRoomIdStr is specified, the value of RoomId is used as the Tencent Real-Time Communication (TRTC) room ID for the whiteboard push task.
        :type RoomId: int
        :param _PushUserId: User ID used by the whiteboard push service for entering the whiteboard room. If `IMAuthParam`and `TRTCAuthParam` are not specified, this user ID is used for operations such as logging in to the IM application, joining an IM group, and entering the room for TRTC whiteboard push.
The ID cannot exceed 60 bytes in length and must be an unused ID. The whiteboard push service uses the user ID to enter the room for whiteboard audio/video push. If this ID is already used in another scenario, the other scenario and whiteboard push service will conflict, affecting the pushing operation.
        :type PushUserId: str
        :param _PushUserSig: User's IM signature corresponding to the PushUserId.
        :type PushUserSig: str
        :param _Whiteboard: Whiteboard parameters, such as the width, height, and background color of the whiteboard.
        :type Whiteboard: :class:`tencentcloud.tiw.v20190919.models.Whiteboard`
        :param _AutoStopTimeout: Whiteboard push timeout. Unit: seconds. Valid range: [300,259200]. Default value: 1800.

If no operation is performed on the whiteboard for the specified period of time, the whiteboard push service automatically stops whiteboard push.
        :type AutoStopTimeout: int
        :param _AutoManageBackup: Specifies whether to synchronize operations on the primary whiteboard push task to the backup task.
        :type AutoManageBackup: bool
        :param _Backup: Parameters of the backup whiteboard push task.

After the backup parameters are specified, the whiteboard push service adds a relayed video stream. That is, there are two video streams on the whiteboard in the same room.
        :type Backup: :class:`tencentcloud.tiw.v20190919.models.WhiteboardPushBackupParam`
        :param _PrivateMapKey: Advanced permission control parameter in TRTC. If the advanced permission control feature is enabled in TRTC, this parameter is required.
        :type PrivateMapKey: str
        :param _VideoFPS: Frame rate of the whiteboard push video. Valid range: [0,30]. Default value: 20. Unit: fps.
        :type VideoFPS: int
        :param _VideoBitrate: Whiteboard push bitrate. Valid range: [0,2000]. Default value: 1200. Unit: kbps.

The bitrate specified here is a reference value. During actual push, a dynamic bitrate is used. The actual bitrate does not remain the specified value but rather fluctuates around it.
        :type VideoBitrate: int
        :param _AutoRecord: Specifies whether to automatically record the whiteboard push when the recording mode in TRTC is set to `SubscribeStreamUserIds`.

Default value: `false`. If you need to enable automatic whiteboard push recording, set this parameter to `true`.

If the recording mode in TRTC is set to `Global Auto Recording`, ignore this parameter.
        :type AutoRecord: bool
        :param _UserDefinedRecordId: ID of the whiteboard push recording. The ID is filled in the `userdefinerecordid` parameter in the callback message after cloud recording is complete in TRTC, helping you identify the recording callback and locate the video file in VOD media resource management.

The value can be up to 64 bytes in length and contain letters (a-z and A-Z), digits (0-9), underscores (_), and hyphens (-).

After this parameter is set, automatic whiteboard push recording is enabled regardless of the value of the `AutoRecord` parameter.

Default RecordId generation rule:
urlencode(SdkAppID_RoomID_PushUserID)

Example:
SdkAppID = 12345678，RoomID = 12345，PushUserID = push_user_1
Therefore: RecordId = 12345678_12345_push_user_1
        :type UserDefinedRecordId: str
        :param _AutoPublish: Specifies whether to enable automatic relay whiteboard push when the relay push mode in TRTC is set to `SubscribeRelayUserIds`.

Default value: `false`. If you need to enable automatic relay whiteboard push, set this parameter to `true`.

If the recording mode in TRTC is set to `Global Auto Relay`, ignore this parameter.
        :type AutoPublish: bool
        :param _UserDefinedStreamId: Stream ID used by TRTC for relay whiteboard push. With this ID, you can stream the user’s audio/video by using the domain name and standard streaming solution (FLV or HLS) in TRTC.

The value can be up to 64 bytes in length and contain letters (a-z and A-Z), digits (0-9), underscores (_), and hyphens (-).

After this parameter is set, automatic relay whiteboard push is enabled regardless of the value of the `AutoPublish` parameter.

Default StreamID generation rule:
urlencode(SdkAppID_RoomID_PushUserID_main)

Example:
SdkAppID = 12345678，RoomID = 12345，PushUserID = push_user_1
Therefore, StreamID = 12345678_12345_push_user_1_main
        :type UserDefinedStreamId: str
        :param _ExtraData: Internal parameter. You can ignore this parameter.
        :type ExtraData: str
        :param _TRTCRoomId: TRTC room ID of the numeric type. Valid range: (1,4294967295).

If RoomId and TRTCRoomId are both specified, the value of TRTCRoomId takes priority as the room ID for TRTC whiteboard push.

If the TRTCRoomIdStr parameter is specified, this parameter is ignored.
        :type TRTCRoomId: int
        :param _TRTCRoomIdStr: TRTC room ID of the string type.

If TRTCRoomIdStr is specified, its value takes priority as the room ID for TRTC whiteboard push.
        :type TRTCRoomIdStr: str
        :param _IMAuthParam: IM authentication parameters.
If the ID of the IM application used by whiteboard messages is different from SdkAppId of the whiteboard application, specify this parameter to provide authentication information of the IM application.

If this parameter is specified, the whiteboard push service preferably uses the SdkAppId value in this parameter as the transmission channel for whiteboard messages. If this parameter is left empty, the SdkAppId value in the common parameters is used.
        :type IMAuthParam: :class:`tencentcloud.tiw.v20190919.models.AuthParam`
        :param _TRTCAuthParam: TRTC authentication parameters, used for room entrance authentication for TRTC push.
If the ID of the TRTC application to which the target TRTC room belongs is different from SdkAppId of the whiteboard application, specify this parameter to provide authentication information of the TRTC application.

If this parameter is specified, the whiteboard push service preferably uses the SdkAppId value in this parameter as the ID of the target TRTC application. If this parameter is left empty, the SdkAppId value in the common parameters is used.
        :type TRTCAuthParam: :class:`tencentcloud.tiw.v20190919.models.AuthParam`
        :param _TRTCEnterRoomMode: This parameter is available only to users in the allowlist for trial.

TRTC room entrance mode for whiteboard push. Default value: `TRTCAppSceneVideoCall`.

`TRTCAppSceneVideoCall`: This scenario is most suitable when there are two or more people on a video call. The internal encoders and network protocols are optimized for video smoothness to reduce call latency and lagging.
`TRTCAppSceneLIVE`: This scenario is most suitable when there is only one person speaking or performing for an online audience, and occasionally multiple people interact with one another through video. The internal encoders and network protocols are optimized for performance and compatibility to deliver better performance and video clarity.
        :type TRTCEnterRoomMode: str
        """
        self._SdkAppId = None
        self._RoomId = None
        self._PushUserId = None
        self._PushUserSig = None
        self._Whiteboard = None
        self._AutoStopTimeout = None
        self._AutoManageBackup = None
        self._Backup = None
        self._PrivateMapKey = None
        self._VideoFPS = None
        self._VideoBitrate = None
        self._AutoRecord = None
        self._UserDefinedRecordId = None
        self._AutoPublish = None
        self._UserDefinedStreamId = None
        self._ExtraData = None
        self._TRTCRoomId = None
        self._TRTCRoomIdStr = None
        self._IMAuthParam = None
        self._TRTCAuthParam = None
        self._TRTCEnterRoomMode = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def PushUserId(self):
        return self._PushUserId

    @PushUserId.setter
    def PushUserId(self, PushUserId):
        self._PushUserId = PushUserId

    @property
    def PushUserSig(self):
        return self._PushUserSig

    @PushUserSig.setter
    def PushUserSig(self, PushUserSig):
        self._PushUserSig = PushUserSig

    @property
    def Whiteboard(self):
        return self._Whiteboard

    @Whiteboard.setter
    def Whiteboard(self, Whiteboard):
        self._Whiteboard = Whiteboard

    @property
    def AutoStopTimeout(self):
        return self._AutoStopTimeout

    @AutoStopTimeout.setter
    def AutoStopTimeout(self, AutoStopTimeout):
        self._AutoStopTimeout = AutoStopTimeout

    @property
    def AutoManageBackup(self):
        return self._AutoManageBackup

    @AutoManageBackup.setter
    def AutoManageBackup(self, AutoManageBackup):
        self._AutoManageBackup = AutoManageBackup

    @property
    def Backup(self):
        return self._Backup

    @Backup.setter
    def Backup(self, Backup):
        self._Backup = Backup

    @property
    def PrivateMapKey(self):
        return self._PrivateMapKey

    @PrivateMapKey.setter
    def PrivateMapKey(self, PrivateMapKey):
        self._PrivateMapKey = PrivateMapKey

    @property
    def VideoFPS(self):
        return self._VideoFPS

    @VideoFPS.setter
    def VideoFPS(self, VideoFPS):
        self._VideoFPS = VideoFPS

    @property
    def VideoBitrate(self):
        return self._VideoBitrate

    @VideoBitrate.setter
    def VideoBitrate(self, VideoBitrate):
        self._VideoBitrate = VideoBitrate

    @property
    def AutoRecord(self):
        return self._AutoRecord

    @AutoRecord.setter
    def AutoRecord(self, AutoRecord):
        self._AutoRecord = AutoRecord

    @property
    def UserDefinedRecordId(self):
        return self._UserDefinedRecordId

    @UserDefinedRecordId.setter
    def UserDefinedRecordId(self, UserDefinedRecordId):
        self._UserDefinedRecordId = UserDefinedRecordId

    @property
    def AutoPublish(self):
        return self._AutoPublish

    @AutoPublish.setter
    def AutoPublish(self, AutoPublish):
        self._AutoPublish = AutoPublish

    @property
    def UserDefinedStreamId(self):
        return self._UserDefinedStreamId

    @UserDefinedStreamId.setter
    def UserDefinedStreamId(self, UserDefinedStreamId):
        self._UserDefinedStreamId = UserDefinedStreamId

    @property
    def ExtraData(self):
        return self._ExtraData

    @ExtraData.setter
    def ExtraData(self, ExtraData):
        self._ExtraData = ExtraData

    @property
    def TRTCRoomId(self):
        return self._TRTCRoomId

    @TRTCRoomId.setter
    def TRTCRoomId(self, TRTCRoomId):
        self._TRTCRoomId = TRTCRoomId

    @property
    def TRTCRoomIdStr(self):
        return self._TRTCRoomIdStr

    @TRTCRoomIdStr.setter
    def TRTCRoomIdStr(self, TRTCRoomIdStr):
        self._TRTCRoomIdStr = TRTCRoomIdStr

    @property
    def IMAuthParam(self):
        return self._IMAuthParam

    @IMAuthParam.setter
    def IMAuthParam(self, IMAuthParam):
        self._IMAuthParam = IMAuthParam

    @property
    def TRTCAuthParam(self):
        return self._TRTCAuthParam

    @TRTCAuthParam.setter
    def TRTCAuthParam(self, TRTCAuthParam):
        self._TRTCAuthParam = TRTCAuthParam

    @property
    def TRTCEnterRoomMode(self):
        return self._TRTCEnterRoomMode

    @TRTCEnterRoomMode.setter
    def TRTCEnterRoomMode(self, TRTCEnterRoomMode):
        self._TRTCEnterRoomMode = TRTCEnterRoomMode


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._PushUserId = params.get("PushUserId")
        self._PushUserSig = params.get("PushUserSig")
        if params.get("Whiteboard") is not None:
            self._Whiteboard = Whiteboard()
            self._Whiteboard._deserialize(params.get("Whiteboard"))
        self._AutoStopTimeout = params.get("AutoStopTimeout")
        self._AutoManageBackup = params.get("AutoManageBackup")
        if params.get("Backup") is not None:
            self._Backup = WhiteboardPushBackupParam()
            self._Backup._deserialize(params.get("Backup"))
        self._PrivateMapKey = params.get("PrivateMapKey")
        self._VideoFPS = params.get("VideoFPS")
        self._VideoBitrate = params.get("VideoBitrate")
        self._AutoRecord = params.get("AutoRecord")
        self._UserDefinedRecordId = params.get("UserDefinedRecordId")
        self._AutoPublish = params.get("AutoPublish")
        self._UserDefinedStreamId = params.get("UserDefinedStreamId")
        self._ExtraData = params.get("ExtraData")
        self._TRTCRoomId = params.get("TRTCRoomId")
        self._TRTCRoomIdStr = params.get("TRTCRoomIdStr")
        if params.get("IMAuthParam") is not None:
            self._IMAuthParam = AuthParam()
            self._IMAuthParam._deserialize(params.get("IMAuthParam"))
        if params.get("TRTCAuthParam") is not None:
            self._TRTCAuthParam = AuthParam()
            self._TRTCAuthParam._deserialize(params.get("TRTCAuthParam"))
        self._TRTCEnterRoomMode = params.get("TRTCEnterRoomMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartWhiteboardPushResponse(AbstractModel):
    """StartWhiteboardPush response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Push task ID.
        :type TaskId: str
        :param _Backup: Result parameters of the backup task.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Backup: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._Backup = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Backup(self):
        return self._Backup

    @Backup.setter
    def Backup(self, Backup):
        self._Backup = Backup

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Backup = params.get("Backup")
        self._RequestId = params.get("RequestId")


class StopOnlineRecordRequest(AbstractModel):
    """StopOnlineRecord request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the customer
        :type SdkAppId: int
        :param _TaskId: ID of the recording task to stop
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopOnlineRecordResponse(AbstractModel):
    """StopOnlineRecord response structure.

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


class StopWhiteboardPushRequest(AbstractModel):
    """StopWhiteboardPush request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _TaskId: ID of the whiteboard push task to be stopped.
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopWhiteboardPushResponse(AbstractModel):
    """StopWhiteboardPush response structure.

    """

    def __init__(self):
        r"""
        :param _Backup: Parameters of the backup task.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Backup: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Backup = None
        self._RequestId = None

    @property
    def Backup(self):
        return self._Backup

    @Backup.setter
    def Backup(self, Backup):
        self._Backup = Backup

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Backup = params.get("Backup")
        self._RequestId = params.get("RequestId")


class StreamControl(AbstractModel):
    """A group of parameters for recording over specified streams. It specifies whether to disable the audio recording and whether to record high-resolution or low-resolution videos.

    """

    def __init__(self):
        r"""
        :param _StreamId: Video stream ID
Description of the possible video stream ID values:
1. `tic_record_user`: the whiteboard video stream
2. `tic_substream`: the auxiliary video stream
3. Specific user ID: the video stream of the specified user

The actual recording uses the prefix match of the video stream ID. The real stream becomes the specified stream once its ID prefix matches with the stream ID.
        :type StreamId: str
        :param _DisableRecord: Whether to disable recording over the stream.

true: does not record this stream. This stream will not be included in the final recording file.
false: records this stream. This stream will be included in the final recording file.

Default value: false
        :type DisableRecord: bool
        :param _DisableAudio: Whether to disable the audio recording of the stream.

true: does not record the audio of the stream. In the final recording file, this stream will be soundless.
false: the stream has both video and audio recording.

Default value: false
        :type DisableAudio: bool
        :param _PullSmallVideo: Whether to only record low-resolution stream videos.

true: records only low-resolution videos. In this case, please make sure that the client pushes low-resolution videos upstream. Otherwise, the recorded video may be black. 
false: records only high-resolution videos.

Default value: false
        :type PullSmallVideo: bool
        """
        self._StreamId = None
        self._DisableRecord = None
        self._DisableAudio = None
        self._PullSmallVideo = None

    @property
    def StreamId(self):
        return self._StreamId

    @StreamId.setter
    def StreamId(self, StreamId):
        self._StreamId = StreamId

    @property
    def DisableRecord(self):
        return self._DisableRecord

    @DisableRecord.setter
    def DisableRecord(self, DisableRecord):
        self._DisableRecord = DisableRecord

    @property
    def DisableAudio(self):
        return self._DisableAudio

    @DisableAudio.setter
    def DisableAudio(self, DisableAudio):
        self._DisableAudio = DisableAudio

    @property
    def PullSmallVideo(self):
        return self._PullSmallVideo

    @PullSmallVideo.setter
    def PullSmallVideo(self, PullSmallVideo):
        self._PullSmallVideo = PullSmallVideo


    def _deserialize(self, params):
        self._StreamId = params.get("StreamId")
        self._DisableRecord = params.get("DisableRecord")
        self._DisableAudio = params.get("DisableAudio")
        self._PullSmallVideo = params.get("PullSmallVideo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamLayout(AbstractModel):
    """Stream layout parameter

    """

    def __init__(self):
        r"""
        :param _LayoutParams: Stream layout configuration
        :type LayoutParams: :class:`tencentcloud.tiw.v20190919.models.LayoutParams`
        :param _InputStreamId: Video stream ID
Description of the possible video stream ID values:
1. tic_record_user: the current picture is used to display the whiteboard video stream.
2. tic_substream: the current picture is used to display the auxiliary video stream.
3. Specific user ID: the current picture is used to display the video stream of a specific user.
4.Left empty: the current picture is vacant for new video stream.
        :type InputStreamId: str
        :param _BackgroundColor: Background color in RGB format, such as "#FF0000" for red. The default color is black. 
        :type BackgroundColor: str
        :param _FillMode: Video filling mode.

0: self-adaption mode. Scales the video proportionally to completely display it in the specified area. In this mode, there may be black bars.
1: full-screen mode. Scales the video to make it fill the entire specified area. In this mode, no black bars will appear, but the video may not be displayed fully.
        :type FillMode: int
        """
        self._LayoutParams = None
        self._InputStreamId = None
        self._BackgroundColor = None
        self._FillMode = None

    @property
    def LayoutParams(self):
        return self._LayoutParams

    @LayoutParams.setter
    def LayoutParams(self, LayoutParams):
        self._LayoutParams = LayoutParams

    @property
    def InputStreamId(self):
        return self._InputStreamId

    @InputStreamId.setter
    def InputStreamId(self, InputStreamId):
        self._InputStreamId = InputStreamId

    @property
    def BackgroundColor(self):
        return self._BackgroundColor

    @BackgroundColor.setter
    def BackgroundColor(self, BackgroundColor):
        self._BackgroundColor = BackgroundColor

    @property
    def FillMode(self):
        return self._FillMode

    @FillMode.setter
    def FillMode(self, FillMode):
        self._FillMode = FillMode


    def _deserialize(self, params):
        if params.get("LayoutParams") is not None:
            self._LayoutParams = LayoutParams()
            self._LayoutParams._deserialize(params.get("LayoutParams"))
        self._InputStreamId = params.get("InputStreamId")
        self._BackgroundColor = params.get("BackgroundColor")
        self._FillMode = params.get("FillMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Tag information.

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
        


class TimeValue(AbstractModel):
    """Time series returned for the queried metric.

    """

    def __init__(self):
        r"""
        :param _Time: Unix timestamp in seconds.
        :type Time: int
        :param _Value: Current value of the queried metric.
        :type Value: float
        """
        self._Time = None
        self._Value = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranscodeTaskResult(AbstractModel):
    """Transcoding task result.

    """

    def __init__(self):
        r"""
        :param _ResultUrl: Transcoding result URL.
        :type ResultUrl: str
        :param _Resolution: Target resolution.
        :type Resolution: str
        :param _Title: Title (usually the document name).
        :type Title: str
        :param _Pages: Number of transcoded pages.
        :type Pages: int
        :param _ThumbnailUrl: URL prefix of the thumbnail. If the URL prefix is `http://example.com/g0jb42ps49vtebjshilb/`, the thumbnail URL for the first page of the dynamically transcoded PowerPoint file is
`http://example.com/g0jb42ps49vtebjshilb/1.jpg`, and so on.

If the document transcoding request carries the ThumbnailResolution parameter and the transcoding type is dynamic transcoding, this parameter is not null. In other cases, this parameter is null.
        :type ThumbnailUrl: str
        :param _ThumbnailResolution: Resolution of the thumbnail generated for dynamic transcoding
        :type ThumbnailResolution: str
        :param _CompressFileUrl: URL for downloading the transcoded and compressed file. If `CompressFileType` carried in the document transcoding request is null or is not a supported compression format, this parameter is null.
        :type CompressFileUrl: str
        :param _ErrorCode: Task execution error code.
        :type ErrorCode: int
        :param _ErrorMsg: Task execution error message.
        :type ErrorMsg: str
        """
        self._ResultUrl = None
        self._Resolution = None
        self._Title = None
        self._Pages = None
        self._ThumbnailUrl = None
        self._ThumbnailResolution = None
        self._CompressFileUrl = None
        self._ErrorCode = None
        self._ErrorMsg = None

    @property
    def ResultUrl(self):
        return self._ResultUrl

    @ResultUrl.setter
    def ResultUrl(self, ResultUrl):
        self._ResultUrl = ResultUrl

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Pages(self):
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        self._Pages = Pages

    @property
    def ThumbnailUrl(self):
        return self._ThumbnailUrl

    @ThumbnailUrl.setter
    def ThumbnailUrl(self, ThumbnailUrl):
        self._ThumbnailUrl = ThumbnailUrl

    @property
    def ThumbnailResolution(self):
        return self._ThumbnailResolution

    @ThumbnailResolution.setter
    def ThumbnailResolution(self, ThumbnailResolution):
        self._ThumbnailResolution = ThumbnailResolution

    @property
    def CompressFileUrl(self):
        return self._CompressFileUrl

    @CompressFileUrl.setter
    def CompressFileUrl(self, CompressFileUrl):
        self._CompressFileUrl = CompressFileUrl

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg


    def _deserialize(self, params):
        self._ResultUrl = params.get("ResultUrl")
        self._Resolution = params.get("Resolution")
        self._Title = params.get("Title")
        self._Pages = params.get("Pages")
        self._ThumbnailUrl = params.get("ThumbnailUrl")
        self._ThumbnailResolution = params.get("ThumbnailResolution")
        self._CompressFileUrl = params.get("CompressFileUrl")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMsg = params.get("ErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranscodeTaskSearchResult(AbstractModel):
    """Transcoding task query results.

    """

    def __init__(self):
        r"""
        :param _CreateTime: Creation time of the task.
        :type CreateTime: str
        :param _TaskId: Unique task ID.
        :type TaskId: str
        :param _Status: Current task status.
- QUEUED: Queuing for transcoding.
- PROCESSING: Transcoding in progress.
- FINISHED: Transcoding finished.
        :type Status: str
        :param _OriginalFilename: Original name of the transcoded document.
        :type OriginalFilename: str
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _Result: Transcoding task result.
        :type Result: :class:`tencentcloud.tiw.v20190919.models.TranscodeTaskResult`
        :param _IsStatic: Specifies whether the transcoding is static.
        :type IsStatic: bool
        """
        self._CreateTime = None
        self._TaskId = None
        self._Status = None
        self._OriginalFilename = None
        self._SdkAppId = None
        self._Result = None
        self._IsStatic = None

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OriginalFilename(self):
        return self._OriginalFilename

    @OriginalFilename.setter
    def OriginalFilename(self, OriginalFilename):
        self._OriginalFilename = OriginalFilename

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def IsStatic(self):
        return self._IsStatic

    @IsStatic.setter
    def IsStatic(self, IsStatic):
        self._IsStatic = IsStatic


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._OriginalFilename = params.get("OriginalFilename")
        self._SdkAppId = params.get("SdkAppId")
        if params.get("Result") is not None:
            self._Result = TranscodeTaskResult()
            self._Result._deserialize(params.get("Result"))
        self._IsStatic = params.get("IsStatic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsageDataItem(AbstractModel):
    """Tencent Interactive Whiteboard usage information.

    """

    def __init__(self):
        r"""
        :param _Time: Start date in the format of YYYY-MM-DD.
        :type Time: str
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _SubProduct: Subproduct usage information, which is consistent with the corresponding request parameters.
- sp_tiw_board: The duration of use of whiteboards.
- sp_tiw_dt: The number of pages dynamically transcoded.
- sp_tiw_st: The number of pages statically transcoded.
- sp_tiw_ric: The duration of real-time recording.
        :type SubProduct: str
        :param _Value: Usage values.
- The unit of sp_tiw_dt and sp_tiw_st is pages.
- The unit of sp_tiw_board and sp_tiw_ric is minutes.
        :type Value: float
        """
        self._Time = None
        self._SdkAppId = None
        self._SubProduct = None
        self._Value = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SubProduct(self):
        return self._SubProduct

    @SubProduct.setter
    def SubProduct(self, SubProduct):
        self._SubProduct = SubProduct

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._SdkAppId = params.get("SdkAppId")
        self._SubProduct = params.get("SubProduct")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserListItem(AbstractModel):
    """Whiteboard user data returned for log queries.

    """

    def __init__(self):
        r"""
        :param _UserId: User ID in the room.
        :type UserId: str
        :param _StartTime: The first time when the user ID appeared during the queried period, which is a Unix timestamp in milliseconds.
        :type StartTime: int
        :param _EndTime: The last time when the user ID appeared during the queried period, which is a Unix timestamp in milliseconds.
        :type EndTime: int
        """
        self._UserId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoInfo(AbstractModel):
    """Video information

    """

    def __init__(self):
        r"""
        :param _VideoPlayTime: Video playback start time, in milliseconds
        :type VideoPlayTime: int
        :param _VideoSize: Video size, in bytes
        :type VideoSize: int
        :param _VideoFormat: Video format
        :type VideoFormat: str
        :param _VideoDuration: Video playback duration, in milliseconds
        :type VideoDuration: int
        :param _VideoUrl: Video file URL
        :type VideoUrl: str
        :param _VideoId: Video file ID
        :type VideoId: str
        :param _VideoType: Video stream type - 0: camera video - 1: screen-sharing video - 2: whiteboard video - 3: mixed stream video - 4: audio-only (mp3)
        :type VideoType: int
        :param _UserId: ID of the user to which the camera video or screen-sharing video belongs (whiteboard video: null, mixed stream video: tic_mixstream_<Room ID>_<Mixed stream layout type>, auxiliary video: tic_substream_user ID)
        :type UserId: str
        :param _Width: Width of the video resolution.
        :type Width: int
        :param _Height: Height of the video resolution.
        :type Height: int
        """
        self._VideoPlayTime = None
        self._VideoSize = None
        self._VideoFormat = None
        self._VideoDuration = None
        self._VideoUrl = None
        self._VideoId = None
        self._VideoType = None
        self._UserId = None
        self._Width = None
        self._Height = None

    @property
    def VideoPlayTime(self):
        return self._VideoPlayTime

    @VideoPlayTime.setter
    def VideoPlayTime(self, VideoPlayTime):
        self._VideoPlayTime = VideoPlayTime

    @property
    def VideoSize(self):
        return self._VideoSize

    @VideoSize.setter
    def VideoSize(self, VideoSize):
        self._VideoSize = VideoSize

    @property
    def VideoFormat(self):
        return self._VideoFormat

    @VideoFormat.setter
    def VideoFormat(self, VideoFormat):
        self._VideoFormat = VideoFormat

    @property
    def VideoDuration(self):
        return self._VideoDuration

    @VideoDuration.setter
    def VideoDuration(self, VideoDuration):
        self._VideoDuration = VideoDuration

    @property
    def VideoUrl(self):
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl

    @property
    def VideoId(self):
        return self._VideoId

    @VideoId.setter
    def VideoId(self, VideoId):
        self._VideoId = VideoId

    @property
    def VideoType(self):
        return self._VideoType

    @VideoType.setter
    def VideoType(self, VideoType):
        self._VideoType = VideoType

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._VideoPlayTime = params.get("VideoPlayTime")
        self._VideoSize = params.get("VideoSize")
        self._VideoFormat = params.get("VideoFormat")
        self._VideoDuration = params.get("VideoDuration")
        self._VideoUrl = params.get("VideoUrl")
        self._VideoId = params.get("VideoId")
        self._VideoType = params.get("VideoType")
        self._UserId = params.get("UserId")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Whiteboard(AbstractModel):
    """Real-time recording whiteboard parameter, such as the whiteboard width and height

    """

    def __init__(self):
        r"""
        :param _Width: Whiteboard video width in the real-time recording result. The value must be equal to or greater than 2. Default value: 1280.
        :type Width: int
        :param _Height: Whiteboard video height in the real-time recording result. The value must be equal to or greater than 2. Default value: 960.
        :type Height: int
        :param _InitParam: Whiteboard initialization parameter, which is passed through to the whiteboard SDK
        :type InitParam: str
        """
        self._Width = None
        self._Height = None
        self._InitParam = None

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def InitParam(self):
        return self._InitParam

    @InitParam.setter
    def InitParam(self, InitParam):
        self._InitParam = InitParam


    def _deserialize(self, params):
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._InitParam = params.get("InitParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhiteboardApplicationConfig(AbstractModel):
    """Whiteboard application configuration, including the resource bucket, domain name, callback URL, and callback key.

    """

    def __init__(self):
        r"""
        :param _TaskType: Task type.

recording: Real-time recording.
transcode: Document transcoding.
        :type TaskType: str
        :param _BucketName: Bucket name.
        :type BucketName: str
        :param _BucketLocation: Region of the bucket.
        :type BucketLocation: str
        :param _BucketPrefix: Resource prefix of the bucket.
        :type BucketPrefix: str
        :param _ResultDomain: Destination CDN domain name.
        :type ResultDomain: str
        :param _Callback: Callback URL.
        :type Callback: str
        :param _CallbackKey: Callback authentication key.
        :type CallbackKey: str
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _AdminUserId: IM admin user ID.
        :type AdminUserId: str
        :param _AdminUserSig: IM admin user signature.
        :type AdminUserSig: str
        """
        self._TaskType = None
        self._BucketName = None
        self._BucketLocation = None
        self._BucketPrefix = None
        self._ResultDomain = None
        self._Callback = None
        self._CallbackKey = None
        self._SdkAppId = None
        self._AdminUserId = None
        self._AdminUserSig = None

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def BucketName(self):
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def BucketLocation(self):
        return self._BucketLocation

    @BucketLocation.setter
    def BucketLocation(self, BucketLocation):
        self._BucketLocation = BucketLocation

    @property
    def BucketPrefix(self):
        return self._BucketPrefix

    @BucketPrefix.setter
    def BucketPrefix(self, BucketPrefix):
        self._BucketPrefix = BucketPrefix

    @property
    def ResultDomain(self):
        return self._ResultDomain

    @ResultDomain.setter
    def ResultDomain(self, ResultDomain):
        self._ResultDomain = ResultDomain

    @property
    def Callback(self):
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def AdminUserId(self):
        return self._AdminUserId

    @AdminUserId.setter
    def AdminUserId(self, AdminUserId):
        self._AdminUserId = AdminUserId

    @property
    def AdminUserSig(self):
        return self._AdminUserSig

    @AdminUserSig.setter
    def AdminUserSig(self, AdminUserSig):
        self._AdminUserSig = AdminUserSig


    def _deserialize(self, params):
        self._TaskType = params.get("TaskType")
        self._BucketName = params.get("BucketName")
        self._BucketLocation = params.get("BucketLocation")
        self._BucketPrefix = params.get("BucketPrefix")
        self._ResultDomain = params.get("ResultDomain")
        self._Callback = params.get("Callback")
        self._CallbackKey = params.get("CallbackKey")
        self._SdkAppId = params.get("SdkAppId")
        self._AdminUserId = params.get("AdminUserId")
        self._AdminUserSig = params.get("AdminUserSig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhiteboardPushBackupParam(AbstractModel):
    """Backup-related request parameters of the whiteboard push task.

    """

    def __init__(self):
        r"""
        :param _PushUserId: User ID used by the whiteboard push service for entering a room,
The ID must be an unused ID in the SDK. The whiteboard push service uses the user ID to enter the room for whiteboard push. If this ID is already used in the SDK, the SDK and recording service will conflict, affecting the pushing operation.
        :type PushUserId: str
        :param _PushUserSig: Signature corresponding to the PushUserId ID.
        :type PushUserSig: str
        """
        self._PushUserId = None
        self._PushUserSig = None

    @property
    def PushUserId(self):
        return self._PushUserId

    @PushUserId.setter
    def PushUserId(self, PushUserId):
        self._PushUserId = PushUserId

    @property
    def PushUserSig(self):
        return self._PushUserSig

    @PushUserSig.setter
    def PushUserSig(self, PushUserSig):
        self._PushUserSig = PushUserSig


    def _deserialize(self, params):
        self._PushUserId = params.get("PushUserId")
        self._PushUserSig = params.get("PushUserSig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhiteboardPushResult(AbstractModel):
    """Whiteboard push task result.

    """

    def __init__(self):
        r"""
        :param _FinishReason: `AUTO`: Pushing automatically stops. `USER_CALL`: The API for stopping pushing is called.
        :type FinishReason: str
        :param _ExceptionCnt: Number of exceptions.
        :type ExceptionCnt: int
        :param _RoomId: Room ID.
        :type RoomId: int
        :param _GroupId: IM group ID.
        :type GroupId: str
        :param _PushStartTime: Actual push start time.
        :type PushStartTime: int
        :param _PushStopTime: Push end time.
        :type PushStopTime: int
        :param _IMSyncTime: IM timestamp corresponding to the first frame of the whiteboard push video. The timestamp is used for time synchronization between IM messages and the whiteboard push video during playback.
        :type IMSyncTime: int
        :param _ErrorCode: Task execution error code.
        :type ErrorCode: int
        :param _ErrorMsg: Error message.
        :type ErrorMsg: str
        """
        self._FinishReason = None
        self._ExceptionCnt = None
        self._RoomId = None
        self._GroupId = None
        self._PushStartTime = None
        self._PushStopTime = None
        self._IMSyncTime = None
        self._ErrorCode = None
        self._ErrorMsg = None

    @property
    def FinishReason(self):
        return self._FinishReason

    @FinishReason.setter
    def FinishReason(self, FinishReason):
        self._FinishReason = FinishReason

    @property
    def ExceptionCnt(self):
        return self._ExceptionCnt

    @ExceptionCnt.setter
    def ExceptionCnt(self, ExceptionCnt):
        self._ExceptionCnt = ExceptionCnt

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def PushStartTime(self):
        return self._PushStartTime

    @PushStartTime.setter
    def PushStartTime(self, PushStartTime):
        self._PushStartTime = PushStartTime

    @property
    def PushStopTime(self):
        return self._PushStopTime

    @PushStopTime.setter
    def PushStopTime(self, PushStopTime):
        self._PushStopTime = PushStopTime

    @property
    def IMSyncTime(self):
        return self._IMSyncTime

    @IMSyncTime.setter
    def IMSyncTime(self, IMSyncTime):
        self._IMSyncTime = IMSyncTime

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg


    def _deserialize(self, params):
        self._FinishReason = params.get("FinishReason")
        self._ExceptionCnt = params.get("ExceptionCnt")
        self._RoomId = params.get("RoomId")
        self._GroupId = params.get("GroupId")
        self._PushStartTime = params.get("PushStartTime")
        self._PushStopTime = params.get("PushStopTime")
        self._IMSyncTime = params.get("IMSyncTime")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMsg = params.get("ErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhiteboardPushTaskSearchResult(AbstractModel):
    """Real-time recording task query results.

    """

    def __init__(self):
        r"""
        :param _TaskId: Unique task ID.
        :type TaskId: str
        :param _Status: Status of the whiteboard push task.
- PREPARED: Push in preparation.
- PUSHING: Pushing in progress.
- STOPPED: Pushing stopped.
        :type Status: str
        :param _RoomId: Room ID of the whiteboard push task.
        :type RoomId: int
        :param _CreateTime: Creation time of the task.
        :type CreateTime: str
        :param _SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param _Result: Whiteboard push result.
        :type Result: :class:`tencentcloud.tiw.v20190919.models.WhiteboardPushResult`
        :param _PushUserId: User ID of the whiteboard push task.
        :type PushUserId: str
        """
        self._TaskId = None
        self._Status = None
        self._RoomId = None
        self._CreateTime = None
        self._SdkAppId = None
        self._Result = None
        self._PushUserId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def PushUserId(self):
        return self._PushUserId

    @PushUserId.setter
    def PushUserId(self, PushUserId):
        self._PushUserId = PushUserId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._RoomId = params.get("RoomId")
        self._CreateTime = params.get("CreateTime")
        self._SdkAppId = params.get("SdkAppId")
        if params.get("Result") is not None:
            self._Result = WhiteboardPushResult()
            self._Result._deserialize(params.get("Result"))
        self._PushUserId = params.get("PushUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        