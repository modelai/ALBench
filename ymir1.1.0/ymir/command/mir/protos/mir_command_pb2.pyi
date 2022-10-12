"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class TvtType(_TvtType, metaclass=_TvtTypeEnumTypeWrapper):
    """/ assertion type: training, validation or test"""
    pass
class _TvtType:
    V = typing.NewType('V', builtins.int)
class _TvtTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_TvtType.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    TvtTypeUnknown = TvtType.V(0)
    TvtTypeTraining = TvtType.V(1)
    TvtTypeValidation = TvtType.V(2)
    TvtTypeTest = TvtType.V(3)

TvtTypeUnknown = TvtType.V(0)
TvtTypeTraining = TvtType.V(1)
TvtTypeValidation = TvtType.V(2)
TvtTypeTest = TvtType.V(3)
global___TvtType = TvtType


class AssetType(_AssetType, metaclass=_AssetTypeEnumTypeWrapper):
    pass
class _AssetType:
    V = typing.NewType('V', builtins.int)
class _AssetTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_AssetType.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    AssetTypeUnknown = AssetType.V(0)
    AssetTypeImageJpeg = AssetType.V(1)
    AssetTypeImagePng = AssetType.V(2)
    AssetTypeImagePixelMat = AssetType.V(3)
    AssetTypeImageYuv420p = AssetType.V(4)
    AssetTypeImageYuv420sp = AssetType.V(5)
    AssetTypeImageYuv422p = AssetType.V(6)
    AssetTypeImageYuv422sp = AssetType.V(7)
    AssetTypeImageBmp = AssetType.V(8)
    AssetTypeVideoMp4 = AssetType.V(101)

AssetTypeUnknown = AssetType.V(0)
AssetTypeImageJpeg = AssetType.V(1)
AssetTypeImagePng = AssetType.V(2)
AssetTypeImagePixelMat = AssetType.V(3)
AssetTypeImageYuv420p = AssetType.V(4)
AssetTypeImageYuv420sp = AssetType.V(5)
AssetTypeImageYuv422p = AssetType.V(6)
AssetTypeImageYuv422sp = AssetType.V(7)
AssetTypeImageBmp = AssetType.V(8)
AssetTypeVideoMp4 = AssetType.V(101)
global___AssetType = AssetType


class TaskType(_TaskType, metaclass=_TaskTypeEnumTypeWrapper):
    """/ task type"""
    pass
class _TaskType:
    V = typing.NewType('V', builtins.int)
class _TaskTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_TaskType.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    TaskTypeUnknown = TaskType.V(0)
    TaskTypeTraining = TaskType.V(1)
    TaskTypeMining = TaskType.V(2)
    TaskTypeLabel = TaskType.V(3)
    TaskTypeFilter = TaskType.V(4)
    TaskTypeImportData = TaskType.V(5)
    TaskTypeExportData = TaskType.V(6)
    TaskTypeCopyData = TaskType.V(7)
    TaskTypeMerge = TaskType.V(8)
    TaskTypeInfer = TaskType.V(9)
    TaskTypeSampling = TaskType.V(10)
    TaskTypeFusion = TaskType.V(11)
    """/ used by ymir_controller"""

    TaskTypeInit = TaskType.V(12)
    TaskTypeImportModel = TaskType.V(13)
    TaskTypeEvaluate = TaskType.V(16)

TaskTypeUnknown = TaskType.V(0)
TaskTypeTraining = TaskType.V(1)
TaskTypeMining = TaskType.V(2)
TaskTypeLabel = TaskType.V(3)
TaskTypeFilter = TaskType.V(4)
TaskTypeImportData = TaskType.V(5)
TaskTypeExportData = TaskType.V(6)
TaskTypeCopyData = TaskType.V(7)
TaskTypeMerge = TaskType.V(8)
TaskTypeInfer = TaskType.V(9)
TaskTypeSampling = TaskType.V(10)
TaskTypeFusion = TaskType.V(11)
"""/ used by ymir_controller"""

TaskTypeInit = TaskType.V(12)
TaskTypeImportModel = TaskType.V(13)
TaskTypeEvaluate = TaskType.V(16)
global___TaskType = TaskType


class TaskState(_TaskState, metaclass=_TaskStateEnumTypeWrapper):
    pass
class _TaskState:
    V = typing.NewType('V', builtins.int)
class _TaskStateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_TaskState.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    TaskStateUnknown = TaskState.V(0)
    TaskStatePending = TaskState.V(1)
    TaskStateRunning = TaskState.V(2)
    TaskStateDone = TaskState.V(3)
    TaskStateError = TaskState.V(4)
    TaskStateMiss = TaskState.V(5)

TaskStateUnknown = TaskState.V(0)
TaskStatePending = TaskState.V(1)
TaskStateRunning = TaskState.V(2)
TaskStateDone = TaskState.V(3)
TaskStateError = TaskState.V(4)
TaskStateMiss = TaskState.V(5)
global___TaskState = TaskState


class Sha1Type(_Sha1Type, metaclass=_Sha1TypeEnumTypeWrapper):
    pass
class _Sha1Type:
    V = typing.NewType('V', builtins.int)
class _Sha1TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Sha1Type.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    SHA1_TYPE_UNKNOWN = Sha1Type.V(0)
    SHA1_TYPE_ASSET = Sha1Type.V(1)
    SHA1_TYPE_COMMIT = Sha1Type.V(2)

SHA1_TYPE_UNKNOWN = Sha1Type.V(0)
SHA1_TYPE_ASSET = Sha1Type.V(1)
SHA1_TYPE_COMMIT = Sha1Type.V(2)
global___Sha1Type = Sha1Type


class MirStorage(_MirStorage, metaclass=_MirStorageEnumTypeWrapper):
    pass
class _MirStorage:
    V = typing.NewType('V', builtins.int)
class _MirStorageEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_MirStorage.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    MIR_METADATAS = MirStorage.V(0)
    MIR_ANNOTATIONS = MirStorage.V(1)
    MIR_KEYWORDS = MirStorage.V(2)
    MIR_TASKS = MirStorage.V(3)
    MIR_CONTEXT = MirStorage.V(4)

MIR_METADATAS = MirStorage.V(0)
MIR_ANNOTATIONS = MirStorage.V(1)
MIR_KEYWORDS = MirStorage.V(2)
MIR_TASKS = MirStorage.V(3)
MIR_CONTEXT = MirStorage.V(4)
global___MirStorage = MirStorage


class LabelFormat(_LabelFormat, metaclass=_LabelFormatEnumTypeWrapper):
    pass
class _LabelFormat:
    V = typing.NewType('V', builtins.int)
class _LabelFormatEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_LabelFormat.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    NO_ANNOTATION = LabelFormat.V(0)
    PASCAL_VOC = LabelFormat.V(1)
    IF_ARK = LabelFormat.V(2)

NO_ANNOTATION = LabelFormat.V(0)
PASCAL_VOC = LabelFormat.V(1)
IF_ARK = LabelFormat.V(2)
global___LabelFormat = LabelFormat


class MirMetadatas(google.protobuf.message.Message):
    """/ ========== metadatas.mir =========="""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class AttributesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___MetadataAttributes: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[global___MetadataAttributes] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    ATTRIBUTES_FIELD_NUMBER: builtins.int
    @property
    def attributes(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___MetadataAttributes]:
        """/ key: asset hash, value: attributes"""
        pass
    def __init__(self,
        *,
        attributes : typing.Optional[typing.Mapping[typing.Text, global___MetadataAttributes]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["attributes",b"attributes"]) -> None: ...
global___MirMetadatas = MirMetadatas

class MetadataAttributes(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATASET_NAME_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    TVT_TYPE_FIELD_NUMBER: builtins.int
    ASSET_TYPE_FIELD_NUMBER: builtins.int
    WIDTH_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    IMAGE_CHANNELS_FIELD_NUMBER: builtins.int
    dataset_name: typing.Text = ...
    @property
    def timestamp(self) -> global___Timestamp: ...
    tvt_type: global___TvtType.V = ...
    asset_type: global___AssetType.V = ...
    width: builtins.int = ...
    """/ column number"""

    height: builtins.int = ...
    """/ row number"""

    image_channels: builtins.int = ...
    """/ (for images) channel count"""

    def __init__(self,
        *,
        dataset_name : typing.Text = ...,
        timestamp : typing.Optional[global___Timestamp] = ...,
        tvt_type : global___TvtType.V = ...,
        asset_type : global___AssetType.V = ...,
        width : builtins.int = ...,
        height : builtins.int = ...,
        image_channels : builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["timestamp",b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["asset_type",b"asset_type","dataset_name",b"dataset_name","height",b"height","image_channels",b"image_channels","timestamp",b"timestamp","tvt_type",b"tvt_type","width",b"width"]) -> None: ...
global___MetadataAttributes = MetadataAttributes

class Timestamp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    START_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    start: builtins.int = ...
    """/ start time stamp"""

    duration: builtins.float = ...
    """/ duration (in seconds), for images, it's always 0"""

    def __init__(self,
        *,
        start : builtins.int = ...,
        duration : builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["duration",b"duration","start",b"start"]) -> None: ...
global___Timestamp = Timestamp

class MirAnnotations(google.protobuf.message.Message):
    """/ ========== annotations.mir =========="""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class TaskAnnotationsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___SingleTaskAnnotations: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[global___SingleTaskAnnotations] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    TASK_ANNOTATIONS_FIELD_NUMBER: builtins.int
    HEAD_TASK_ID_FIELD_NUMBER: builtins.int
    @property
    def task_annotations(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___SingleTaskAnnotations]:
        """/ key: task id, value: annotations of that single task"""
        pass
    head_task_id: typing.Text = ...
    def __init__(self,
        *,
        task_annotations : typing.Optional[typing.Mapping[typing.Text, global___SingleTaskAnnotations]] = ...,
        head_task_id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["head_task_id",b"head_task_id","task_annotations",b"task_annotations"]) -> None: ...
global___MirAnnotations = MirAnnotations

class SingleTaskAnnotations(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class ImageAnnotationsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___SingleImageAnnotations: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[global___SingleImageAnnotations] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    IMAGE_ANNOTATIONS_FIELD_NUMBER: builtins.int
    @property
    def image_annotations(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___SingleImageAnnotations]:
        """/ key: image id, value: annotations of that single image"""
        pass
    def __init__(self,
        *,
        image_annotations : typing.Optional[typing.Mapping[typing.Text, global___SingleImageAnnotations]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["image_annotations",b"image_annotations"]) -> None: ...
global___SingleTaskAnnotations = SingleTaskAnnotations

class SingleImageAnnotations(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ANNOTATIONS_FIELD_NUMBER: builtins.int
    @property
    def annotations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Annotation]: ...
    def __init__(self,
        *,
        annotations : typing.Optional[typing.Iterable[global___Annotation]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["annotations",b"annotations"]) -> None: ...
global___SingleImageAnnotations = SingleImageAnnotations

class Annotation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    INDEX_FIELD_NUMBER: builtins.int
    BOX_FIELD_NUMBER: builtins.int
    CLASS_ID_FIELD_NUMBER: builtins.int
    SCORE_FIELD_NUMBER: builtins.int
    index: builtins.int = ...
    """Index of this annotation in current single image, may be different from the index in repeated field."""

    @property
    def box(self) -> global___Rect: ...
    class_id: builtins.int = ...
    score: builtins.float = ...
    def __init__(self,
        *,
        index : builtins.int = ...,
        box : typing.Optional[global___Rect] = ...,
        class_id : builtins.int = ...,
        score : builtins.float = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["box",b"box"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["box",b"box","class_id",b"class_id","index",b"index","score",b"score"]) -> None: ...
global___Annotation = Annotation

class Rect(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    W_FIELD_NUMBER: builtins.int
    H_FIELD_NUMBER: builtins.int
    x: builtins.int = ...
    y: builtins.int = ...
    w: builtins.int = ...
    h: builtins.int = ...
    def __init__(self,
        *,
        x : builtins.int = ...,
        y : builtins.int = ...,
        w : builtins.int = ...,
        h : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["h",b"h","w",b"w","x",b"x","y",b"y"]) -> None: ...
global___Rect = Rect

class MirKeywords(google.protobuf.message.Message):
    """/ ========== keywords.mir =========="""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class KeywordsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___Keywords: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[global___Keywords] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    class IndexPredifinedKeyidsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int = ...
        @property
        def value(self) -> global___Assets: ...
        def __init__(self,
            *,
            key : builtins.int = ...,
            value : typing.Optional[global___Assets] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    KEYWORDS_FIELD_NUMBER: builtins.int
    INDEX_PREDIFINED_KEYIDS_FIELD_NUMBER: builtins.int
    @property
    def keywords(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___Keywords]:
        """key: asset hash, value: keywords list
        cnt: count of keywords
        """
        pass
    @property
    def index_predifined_keyids(self) -> google.protobuf.internal.containers.MessageMap[builtins.int, global___Assets]:
        """key: class id, value: assert ids"""
        pass
    def __init__(self,
        *,
        keywords : typing.Optional[typing.Mapping[typing.Text, global___Keywords]] = ...,
        index_predifined_keyids : typing.Optional[typing.Mapping[builtins.int, global___Assets]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["index_predifined_keyids",b"index_predifined_keyids","keywords",b"keywords"]) -> None: ...
global___MirKeywords = MirKeywords

class Assets(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ASSET_IDS_FIELD_NUMBER: builtins.int
    @property
    def asset_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        asset_ids : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["asset_ids",b"asset_ids"]) -> None: ...
global___Assets = Assets

class Keywords(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PREDIFINED_KEYIDS_FIELD_NUMBER: builtins.int
    CUSTOMIZED_KEYWORDS_FIELD_NUMBER: builtins.int
    @property
    def predifined_keyids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """predefined: managed id-keyword map"""
        pass
    @property
    def customized_keywords(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """customized: arbitrary user defined keywords"""
        pass
    def __init__(self,
        *,
        predifined_keyids : typing.Optional[typing.Iterable[builtins.int]] = ...,
        customized_keywords : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["customized_keywords",b"customized_keywords","predifined_keyids",b"predifined_keyids"]) -> None: ...
global___Keywords = Keywords

class MirTasks(google.protobuf.message.Message):
    """/ ========== tasks.mir =========="""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class TasksEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___Task: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[global___Task] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    TASKS_FIELD_NUMBER: builtins.int
    HEAD_TASK_ID_FIELD_NUMBER: builtins.int
    @property
    def tasks(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___Task]: ...
    head_task_id: typing.Text = ...
    def __init__(self,
        *,
        tasks : typing.Optional[typing.Mapping[typing.Text, global___Task]] = ...,
        head_task_id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["head_task_id",b"head_task_id","tasks",b"tasks"]) -> None: ...
global___MirTasks = MirTasks

class Task(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class UnknownTypesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: builtins.int = ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : builtins.int = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    TYPE_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    TASK_ID_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    MODEL_FIELD_NUMBER: builtins.int
    UNKNOWN_TYPES_FIELD_NUMBER: builtins.int
    RETURN_CODE_FIELD_NUMBER: builtins.int
    RETURN_MSG_FIELD_NUMBER: builtins.int
    EVALUATION_FIELD_NUMBER: builtins.int
    SERIALIZED_TASK_PARAMETERS_FIELD_NUMBER: builtins.int
    SERIALIZED_EXECUTOR_CONFIG_FIELD_NUMBER: builtins.int
    SRC_REVS_FIELD_NUMBER: builtins.int
    DST_REV_FIELD_NUMBER: builtins.int
    EXECUTOR_FIELD_NUMBER: builtins.int
    type: global___TaskType.V = ...
    name: typing.Text = ...
    """/ user defined task name"""

    task_id: typing.Text = ...
    """/ auto generated unique id"""

    timestamp: builtins.int = ...
    """/ execution time of this task
    RFC 3339 date strings
    """

    @property
    def model(self) -> global___ModelMeta:
        """/ (special for training task): result model for cmd train"""
        pass
    @property
    def unknown_types(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, builtins.int]:
        """/ (special for import task): unknown types for cmd import"""
        pass
    return_code: builtins.int = ...
    return_msg: typing.Text = ...
    @property
    def evaluation(self) -> global___Evaluation: ...
    serialized_task_parameters: typing.Text = ...
    serialized_executor_config: typing.Text = ...
    src_revs: typing.Text = ...
    dst_rev: typing.Text = ...
    executor: typing.Text = ...
    def __init__(self,
        *,
        type : global___TaskType.V = ...,
        name : typing.Text = ...,
        task_id : typing.Text = ...,
        timestamp : builtins.int = ...,
        model : typing.Optional[global___ModelMeta] = ...,
        unknown_types : typing.Optional[typing.Mapping[typing.Text, builtins.int]] = ...,
        return_code : builtins.int = ...,
        return_msg : typing.Text = ...,
        evaluation : typing.Optional[global___Evaluation] = ...,
        serialized_task_parameters : typing.Text = ...,
        serialized_executor_config : typing.Text = ...,
        src_revs : typing.Text = ...,
        dst_rev : typing.Text = ...,
        executor : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["evaluation",b"evaluation","model",b"model"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dst_rev",b"dst_rev","evaluation",b"evaluation","executor",b"executor","model",b"model","name",b"name","return_code",b"return_code","return_msg",b"return_msg","serialized_executor_config",b"serialized_executor_config","serialized_task_parameters",b"serialized_task_parameters","src_revs",b"src_revs","task_id",b"task_id","timestamp",b"timestamp","type",b"type","unknown_types",b"unknown_types"]) -> None: ...
global___Task = Task

class ModelMeta(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MODEL_HASH_FIELD_NUMBER: builtins.int
    MEAN_AVERAGE_PRECISION_FIELD_NUMBER: builtins.int
    CONTEXT_FIELD_NUMBER: builtins.int
    model_hash: typing.Text = ...
    """/ hash for models.tar.gz"""

    mean_average_precision: builtins.float = ...
    """/ model mAP"""

    context: typing.Text = ...
    """/ context generated by train command"""

    def __init__(self,
        *,
        model_hash : typing.Text = ...,
        mean_average_precision : builtins.float = ...,
        context : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["context",b"context","mean_average_precision",b"mean_average_precision","model_hash",b"model_hash"]) -> None: ...
global___ModelMeta = ModelMeta

class Evaluation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class DatasetEvaluationsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___SingleDatasetEvaluation: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[global___SingleDatasetEvaluation] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    CONFIG_FIELD_NUMBER: builtins.int
    DATASET_EVALUATIONS_FIELD_NUMBER: builtins.int
    @property
    def config(self) -> global___EvaluateConfig: ...
    @property
    def dataset_evaluations(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___SingleDatasetEvaluation]:
        """key: prediction dataset id, value: evaluation result for ground truth and prediction dataset"""
        pass
    def __init__(self,
        *,
        config : typing.Optional[global___EvaluateConfig] = ...,
        dataset_evaluations : typing.Optional[typing.Mapping[typing.Text, global___SingleDatasetEvaluation]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["config",b"config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["config",b"config","dataset_evaluations",b"dataset_evaluations"]) -> None: ...
global___Evaluation = Evaluation

class EvaluateConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    GT_DATASET_ID_FIELD_NUMBER: builtins.int
    PRED_DATASET_IDS_FIELD_NUMBER: builtins.int
    CONF_THR_FIELD_NUMBER: builtins.int
    IOU_THRS_INTERVAL_FIELD_NUMBER: builtins.int
    NEED_PR_CURVE_FIELD_NUMBER: builtins.int
    gt_dataset_id: typing.Text = ...
    @property
    def pred_dataset_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    conf_thr: builtins.float = ...
    iou_thrs_interval: typing.Text = ...
    need_pr_curve: builtins.bool = ...
    def __init__(self,
        *,
        gt_dataset_id : typing.Text = ...,
        pred_dataset_ids : typing.Optional[typing.Iterable[typing.Text]] = ...,
        conf_thr : builtins.float = ...,
        iou_thrs_interval : typing.Text = ...,
        need_pr_curve : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["conf_thr",b"conf_thr","gt_dataset_id",b"gt_dataset_id","iou_thrs_interval",b"iou_thrs_interval","need_pr_curve",b"need_pr_curve","pred_dataset_ids",b"pred_dataset_ids"]) -> None: ...
global___EvaluateConfig = EvaluateConfig

class SingleDatasetEvaluation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class IouEvaluationsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___SingleIouEvaluation: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[global___SingleIouEvaluation] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    CONF_THR_FIELD_NUMBER: builtins.int
    GT_DATASET_ID_FIELD_NUMBER: builtins.int
    PRED_DATASET_ID_FIELD_NUMBER: builtins.int
    IOU_EVALUATIONS_FIELD_NUMBER: builtins.int
    IOU_AVERAGED_EVALUATION_FIELD_NUMBER: builtins.int
    conf_thr: builtins.float = ...
    gt_dataset_id: typing.Text = ...
    pred_dataset_id: typing.Text = ...
    @property
    def iou_evaluations(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___SingleIouEvaluation]:
        """key: string of iou threshold"""
        pass
    @property
    def iou_averaged_evaluation(self) -> global___SingleIouEvaluation:
        """average for all ious"""
        pass
    def __init__(self,
        *,
        conf_thr : builtins.float = ...,
        gt_dataset_id : typing.Text = ...,
        pred_dataset_id : typing.Text = ...,
        iou_evaluations : typing.Optional[typing.Mapping[typing.Text, global___SingleIouEvaluation]] = ...,
        iou_averaged_evaluation : typing.Optional[global___SingleIouEvaluation] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["iou_averaged_evaluation",b"iou_averaged_evaluation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["conf_thr",b"conf_thr","gt_dataset_id",b"gt_dataset_id","iou_averaged_evaluation",b"iou_averaged_evaluation","iou_evaluations",b"iou_evaluations","pred_dataset_id",b"pred_dataset_id"]) -> None: ...
global___SingleDatasetEvaluation = SingleDatasetEvaluation

class SingleIouEvaluation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class CiEvaluationsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int = ...
        @property
        def value(self) -> global___SingleTopicEvaluation: ...
        def __init__(self,
            *,
            key : builtins.int = ...,
            value : typing.Optional[global___SingleTopicEvaluation] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    class TopicEvaluationsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___SingleTopicEvaluation: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[global___SingleTopicEvaluation] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    CI_EVALUATIONS_FIELD_NUMBER: builtins.int
    CI_AVERAGED_EVALUATION_FIELD_NUMBER: builtins.int
    TOPIC_EVALUATIONS_FIELD_NUMBER: builtins.int
    @property
    def ci_evaluations(self) -> google.protobuf.internal.containers.MessageMap[builtins.int, global___SingleTopicEvaluation]:
        """key: class ids"""
        pass
    @property
    def ci_averaged_evaluation(self) -> global___SingleTopicEvaluation:
        """evaluations averaged by class ids"""
        pass
    @property
    def topic_evaluations(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___SingleTopicEvaluation]:
        """key: topic names"""
        pass
    def __init__(self,
        *,
        ci_evaluations : typing.Optional[typing.Mapping[builtins.int, global___SingleTopicEvaluation]] = ...,
        ci_averaged_evaluation : typing.Optional[global___SingleTopicEvaluation] = ...,
        topic_evaluations : typing.Optional[typing.Mapping[typing.Text, global___SingleTopicEvaluation]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["ci_averaged_evaluation",b"ci_averaged_evaluation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["ci_averaged_evaluation",b"ci_averaged_evaluation","ci_evaluations",b"ci_evaluations","topic_evaluations",b"topic_evaluations"]) -> None: ...
global___SingleIouEvaluation = SingleIouEvaluation

class SingleTopicEvaluation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    AP_FIELD_NUMBER: builtins.int
    AR_FIELD_NUMBER: builtins.int
    TP_FIELD_NUMBER: builtins.int
    FP_FIELD_NUMBER: builtins.int
    FN_FIELD_NUMBER: builtins.int
    PR_CURVE_FIELD_NUMBER: builtins.int
    ap: builtins.float = ...
    ar: builtins.float = ...
    tp: builtins.int = ...
    fp: builtins.int = ...
    fn: builtins.int = ...
    @property
    def pr_curve(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FloatPoint]: ...
    def __init__(self,
        *,
        ap : builtins.float = ...,
        ar : builtins.float = ...,
        tp : builtins.int = ...,
        fp : builtins.int = ...,
        fn : builtins.int = ...,
        pr_curve : typing.Optional[typing.Iterable[global___FloatPoint]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ap",b"ap","ar",b"ar","fn",b"fn","fp",b"fp","pr_curve",b"pr_curve","tp",b"tp"]) -> None: ...
global___SingleTopicEvaluation = SingleTopicEvaluation

class FloatPoint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    x: builtins.float = ...
    y: builtins.float = ...
    def __init__(self,
        *,
        x : builtins.float = ...,
        y : builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["x",b"x","y",b"y"]) -> None: ...
global___FloatPoint = FloatPoint

class MirContext(google.protobuf.message.Message):
    """/ ========== context.mir =========="""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class PredefinedKeyidsCntEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int = ...
        value: builtins.int = ...
        def __init__(self,
            *,
            key : builtins.int = ...,
            value : builtins.int = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    class ProjectPredefinedKeyidsCntEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int = ...
        value: builtins.int = ...
        def __init__(self,
            *,
            key : builtins.int = ...,
            value : builtins.int = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    class CustomizedKeywordsCntEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: builtins.int = ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : builtins.int = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    IMAGES_CNT_FIELD_NUMBER: builtins.int
    NEGATIVE_IMAGES_CNT_FIELD_NUMBER: builtins.int
    PROJECT_NEGATIVE_IMAGES_CNT_FIELD_NUMBER: builtins.int
    PREDEFINED_KEYIDS_CNT_FIELD_NUMBER: builtins.int
    PROJECT_PREDEFINED_KEYIDS_CNT_FIELD_NUMBER: builtins.int
    CUSTOMIZED_KEYWORDS_CNT_FIELD_NUMBER: builtins.int
    images_cnt: builtins.int = ...
    """/ total images count"""

    negative_images_cnt: builtins.int = ...
    """/ total negative images count (images without any annotations)"""

    project_negative_images_cnt: builtins.int = ...
    """/ total negative images count (images without any project class names)"""

    @property
    def predefined_keyids_cnt(self) -> google.protobuf.internal.containers.ScalarMap[builtins.int, builtins.int]:
        """/ key: class id, value: images count"""
        pass
    @property
    def project_predefined_keyids_cnt(self) -> google.protobuf.internal.containers.ScalarMap[builtins.int, builtins.int]:
        """/ key: class id (only in this project), value: images count"""
        pass
    @property
    def customized_keywords_cnt(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, builtins.int]:
        """/ key: customized keywords, value: images count"""
        pass
    def __init__(self,
        *,
        images_cnt : builtins.int = ...,
        negative_images_cnt : builtins.int = ...,
        project_negative_images_cnt : builtins.int = ...,
        predefined_keyids_cnt : typing.Optional[typing.Mapping[builtins.int, builtins.int]] = ...,
        project_predefined_keyids_cnt : typing.Optional[typing.Mapping[builtins.int, builtins.int]] = ...,
        customized_keywords_cnt : typing.Optional[typing.Mapping[typing.Text, builtins.int]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["customized_keywords_cnt",b"customized_keywords_cnt","images_cnt",b"images_cnt","negative_images_cnt",b"negative_images_cnt","predefined_keyids_cnt",b"predefined_keyids_cnt","project_negative_images_cnt",b"project_negative_images_cnt","project_predefined_keyids_cnt",b"project_predefined_keyids_cnt"]) -> None: ...
global___MirContext = MirContext