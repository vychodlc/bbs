### 开发日志

#### 2021年8月21日

+ 创建数据库
+ 分别新建 user, post, topic, followship, comment, message 库
+ 分别确认字段名以及字段数据格式、默认值、主键

#### 2021年8月22日

+ 创建 flask 项目，安装 flask pymysql 等库
+ 测试数据库连接
+ 新建 user API ，包括注册、登录

#### 2021年8月23日

+ 新建 post API，包括新增和获取

#### 2021年8月24日

+ app navbar 设计完毕

#### 2021年8月25日

+ 设计首页

### 开发笔记

#### 数据库设计

+ 用户：
	+ 基本信息：ID、昵称、邮箱、密码、头像、个人简介、性别、权限级别、收藏帖子ID数组、收藏话题ID数组
+ 帖子：
	+ 基本信息：ID、内容、所属话题、时间、发布者ID、点赞数、评论数、转发数、阅读数、是否为转发、原帖ID、是否加精、热度
+ 话题：
	+ 基本信息：ID、话题名称、话题帖子数、管理员ID
+ 评论：
	+ 基本信息：ID、内容、发布者ID、所属帖子ID、是否二级评论、原评论ID、点赞数
+ 关注表：
	+ 基本信息：ID、关注人ID、被关注人ID、是否互关
+ 聊天消息：
	+ 基本信息：ID、发送方ID、接收人ID、消息内容、发送时间、是否已读

#### 业务设计（NavBar 部分）

+ 主页：
	+ 热度计算公式：H=[log(length)+ln(1+read)+1.0*comment+1.75*like+3.2*star]*exp[-γ*(t-tlast)/86400]
	+ 十大 + 朋友圈(仅展示所关注用户的发帖状态)——Tab页显示
+ 话题：使用多Tab页显示不同话题的帖子，按照帖子热度排序，用户收藏的话题会靠前摆放
+ 发帖：类似于微博的发帖界面——包含文字表情配图以及话题选择，不选择的话默认为朋友圈，
+ 消息：展示相关评论、赞、私信
+ 我：展示用户信息以及应用设置、展示用户收藏信息、账号登录&切换&退出、用户的关注以及粉丝

#### 使用技术栈

+ 前端：Vue + scss + TypeScript + ElementUI + ElementManage
+ 后端：Flask + MySQL
+ 工具：VSCode + Navicat

#### Vue 文件树

+ login
	+ index
+ home
	+ index
+ index
	+ index
+ topic
	+ index
+ message
	+ index
	+ message_detail
+ user
	+ index
	+ info_change
	+ favor_page
	+ follow_page
+ common
	+ post_detail

#### api 设计

+ user:
	+ login
	+ register
	+ change_info
	+ get_follow
	+ get_followed
	+ add_follow
	+ del_follow
+ post:
	+ add_post
	+ del_post
	+ edit_post
	+ add_star: 可取消
	+ add_collect: 可取消
	+ add_comment: 可删除
	+ get_post_detail
	+ get_hot
	+ get
+ topic:
+ 