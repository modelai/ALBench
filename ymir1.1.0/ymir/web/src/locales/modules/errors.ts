const errors = {
  'error.timeout': { cn: '请求超时', en: 'Request Timeout', },
  'error110101': { cn: '接口错误', en: 'API_ERROR: API Error', },
  'error110102': { cn: '参数校验失败', en: 'Parammeters Validation Failed', },
  'error110103': { cn: '未知错误', en: 'UNKNOWN_ERROR: Unkown Error', },
  'error110104': { cn: 'token失效，请重新登录', en: 'INVALID_TOKEN: Invalid Token, Please try again', },
  'error110105': { cn: '必填字段缺失', en: 'REQUIRED_FIELD_MISSING: ', },
  'error110106': { cn: '服务器错误', en: 'CONTROLLER_ERROR: ', },
  'error110107': { cn: '用户名或密码错误，请重试', en: 'Unmatch email or password, Please try again', },
  'error110108': { cn: '下载失败', en: 'FAILED_TO_DOWNLOAD: failed to download file', },
  'error110109': { cn: '配置不可用', en: 'INVALID_CONFIGURATION', },
  'error110110': { cn: '用户权限不匹配', en: 'INVALID_SCOPE', },
  'error110111': {
    cn: '无法隐藏受保护的资源，如当前迭代的产出、项目中的训练集、测试集、挖掘集或者正在进行的数据集/模型',
    en: 'Can not hide protected resource, such as result of current iteration, training, testing, and mining dataset related to project, or in-progress dataset/model',
  },
  'error110201': { cn: '找不到该用户，请重试', en: 'USER_NOT_FOUND: User Not Found, retry or contact admin.', },
  'error110202': { cn: '名称已重复，请选择新的名称注册', en: 'USER_DUPLICATED_NAME: Duplicated Username, try another name', },
  'error110203': { cn: '用户未授权访问', en: 'USER_NOT_ACCESSIBLE: User is Unaccessable', },
  'error110204': { cn: '用户未登录，请登录', en: 'USER_NOT_LOGGED_IN: User is not logged in, please log in', },
  'error110205': { cn: '该操作需要管理员权限，用户不是管理员', en: 'USER_NOT_ADMIN: User is not admin but action need admin privelige', },
  'error110206': { cn: '用户未被激活', en: 'USER_NOT_ACTIVE: User is not active', },
  'error110207': { cn: '用户角色权限不匹配', en: 'Invalid role for user', },
  'error110301': { cn: '找不到该用户的工作空间', en: 'WORKSPACE_NOT_FOUND: User\'s workspace not found', },
  'error110302': { cn: '重复的工作空间名称', en: 'WORKSPACE_DUPLICATED_NAME', },
  'error110304': { cn: '工作空间创建失败', en: 'WORKSPACE_FAILED_TO_CREATE', },
  'error110401': { cn: '找不到数据集', en: 'Dataset is not found', },
  'error110402': { cn: '重复的数据集名称', en: 'Duplicated dataset name', },
  'error110403': { cn: '数据集未授权访问', en: 'Dataset inaccessable', },
  'error110404': { cn: '数据集创建失败', en: 'DATASET_FAILED_TO_CREATE: failed to create dataset', },
  'error110405': { cn: '数据集被系统保护不可删除', en: 'DATASET_FAILED_TO_DELETE: failed to delete dataset', },
  'error110501': { cn: '找不到该数据', en: 'Asset is not found', },
  'error110601': { cn: '找不到该模型', en: 'Model is not found', },
  'error110602': { cn: '重复的模型名称', en: 'Duplicated model name', },
  'error110603': { cn: '模型未授权访问', en: 'Model inaccessable', },
  'error110604': { cn: '模型创建不成功', en: 'MODEL_FAILED_TO_CREATE: failed to create model', },
  'error110605': { cn: '模型尚未准备好', en: 'MODEL_NOT_READY: model is not ready', },
  'error110701': { cn: '找不到该任务', en: 'Task is not found', },
  'error110702': { cn: '重复的任务名称', en: 'Duplicated task name', },
  'error110703': { cn: '任务未授权访问', en: 'Task inaccessable', },
  'error110704': { cn: '任务创建失败', en: 'TASK_FAILED_TO_CREATE: failed to create task', },
  'error110705': { cn: '任务状态过时', en: 'TASK_STATUS_OBSOLETE', },
  'error110706': { cn: '更新任务状态失败', en: 'FAILED_TO_UPDATE_TASK_STATUS: failed to update task status', },
  'error110801': { cn: '找不到对应的历史树', en: 'HISTORY NOT FOUND', },
  'error111001': { cn: '重复的标签名称或别名', en: 'KEYWORD_DUPLICATED: duplicated keyword or aliases', },
  'error110901': { cn: '调用推理失败', en: 'INFERENCE_FAILED_TO_CALL: failed to call inference', },
  'error110902': { cn: '推理镜像配置错误', en: 'INFERENCE_CONFIG_ERROR: inference image configure error', },
  'error111101': { cn: '镜像名称重复', en: 'Duplicated docker image name', },
  'error111102': { cn: '找不到镜像', en: 'Docker image is not found', },
  'error111103': { cn: '共享镜像失败', en: 'Share docker image failed', },
  'error111104': { cn: '此镜像关联其他镜像，请清除关联后再处理', en: 'Clean relationships of docker images before deleting it', },
  'error111105': { cn: '分享镜像失败', en: 'FAILED_TO_GET_SHARED_DOCKER_IMAGES', },
  'error111106': { cn: '分享镜像配置获取失败', en: 'SHARED_IMAGE_CONFIG_ERROR', },
  'error111201': { cn: '无法获取GPU个数信息', en: 'Can not get server\'s GPU count', },
  'error111301': { cn: 'ClickHouse连接失败，无法获取统计数据', en: 'ClickHouse connect error, then get statstics data failed', },
  'error111401': { cn: '找不到项目', en: 'Project Not Found', },
  'error111402': { cn: '项目名称重复', en: 'Duplicated project name', },
  'error111502': { cn: '数据集名称重复', en: 'Duplicated dataset name', },
  'error111901': { cn: '隐藏和取消隐藏不能同时处理', en: 'Hide and Unhide cannot handle in same request', },
  'error111904': { cn: '操作的数量为空', en: 'Operations is missing', },
  'error110406': { cn: '不在同一个数据集的版本不能进行比对', en: 'Versions must be in the same datasets', },
  'error111902': { cn: '调用CMD进行数据集比对失败', en: 'Evaluate error from CMD', },
  'error111903': { cn: '完成数据集比对，但找不到相应的结果', en: 'Evaluate done, but can not find result', },
  'error130604': {
    cn: '内部网络错误, 请检查应用程序系统配置',
    en: 'HTTP_ERROR: internal network error, please check system configuration.',
  },
  'error140400': { cn: 'viz 一般错误', en: 'viz: general_error', },
  'error140401': { cn: 'viz 分支不存在', en: 'viz: branch_not_exists', },
  'error140500': { cn: 'viz 内部错误', en: 'viz: internal_error', },
  'error150400': { cn: 'controller 一般错误', en: 'controller: general_error', },
  'error150401': { cn: 'controller 重复的任务id', en: 'controller: duplicate_task_id', },
  'error150402': { cn: 'controller 任务进度日志错误', en: 'controller: percent_log_error', },
  'error150404': {
    cn: '进度日志文件格式转换错误，请确认镜像写入日志格式',
    en: 'Percent log parsed error, please check input from docker image.',
  },
  'error150500': { cn: 'controller 内部错误', en: 'controller: internal_error', },
  'error160001': { cn: 'CMD: 参数不可用', en: 'RC_CMD_INVALID_ARGS: invalid args', },
  'error160002': { cn: 'CMD: 训练集为空', en: 'RC_CMD_EMPTY_TRAIN_SET: empty train set', },
  'error160003': { cn: 'CMD: 测试集为空', en: 'RC_CMD_EMPTY_VAL_SET: empty test set', },
  'error160004': { cn: 'CMD: 容器错误', en: 'RC_CMD_CONTAINER_ERROR: image container error', },
  'error160005': { cn: 'CMD: 未知类型', en: 'RC_CMD_UNKNOWN_TYPES: unkown type', },
  'error160006': { cn: 'CMD: 分支或标签不可用', en: 'RC_CMD_INVALID_BRANCH_OR_TAG: invalid branch or tag', },
  'error160007': { cn: 'CMD: 脏Repo，需要清理', en: 'RC_CMD_DIRTY_REPO: dirty repo.', },
  'error160008': {
    cn: '合并错误，例如训练集和测试集有重合图片',
    en: 'Merge error, such as training dataset have the same assets in testing dataset.',
  },
  'error160009': { cn: 'CMD: mir repo不可用', en: 'RC_CMD_INVALID_MIR_REPO: invalid mir repo.', },
  'error160010': { cn: 'CMD: 文件不可用', en: 'RC_CMD_INVALID_FILE: invalid file', },
  'error160011': { cn: 'CMD: 无结果生成', en: 'RC_CMD_NO_RESULT: no result', },
  'error169999': { cn: 'CMD: 未知错误', en: 'RC_CMD_ERROR_UNKNOWN: unkown error', },
}

export default errors