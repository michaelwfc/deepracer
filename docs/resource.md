
# Resource

[racing-tips](https://aws.amazon.com/cn/deepracer/racing-tips/)

## DeepRacer 模型、模型训练和模型分析

- [Scott Pletcher 的 DeepRacer 模型实验（公共档案）](https://github.com/scottpletcher/deepracer) - 此存储库包含有关不同奖励函数策略及其性能的一些有用笔记。新用户的良好起点。
- [Jeremy Pedersen 的 DeepRacer 模型笔记（公共档案）](https://github.com/jeremypedersen/deepracer-notes ) - 我自己关于基本（默认）DeepRacer 奖励函数性能的小修改的笔记。
- [Capstone_AWS_DeepRacer](https://github.com/dgnzlz/Capstone_AWS_DeepRacer)- 学生项目，旨在创建最佳赛车线路和速度设置，附带示例奖励函数

## 视频
[Boltron Racing Team](https://www.youtube.com/watch?v=-4X9cv6Fopw) - 一系列关于训练和优化 DeepRacer 模型的 YouTube 视频
[AWS 中国团队的 DeepRacer 视频](https://space.bilibili.com/418158141/search/video?keyword=deepracer) - Bilibili（中文 YouTube）上的视频

## DeepRacer 机器人操作系统（ROS）示例项目
[DeepRacer 开源入门指南](https://github.com/aws-deepracer/aws-deepracer-launcher) - 引导用户在汽车上设置 ROS 项目并创建一个简单的“Hello World”项目
[DeepRacer 跟随领导者项目](https://github.com/aws-deepracer/aws-deepracer-follow-the-leader-sample-project) - 向用户展示如何修改 DeepRacer ROS 堆栈以使用 OpenCV 在场景中跟随人



## DeepRacer 工作坊
官方 AWS 工作坊和非官方工作坊代码移植


[DeepRacer 200L 工作坊](https://catalog.workshops.aws/deepracer-200l/en-US) - 一个简单的入门工作坊，适合新的 DeepRacer 用户。引导他们完成训练第一个模型的过程。

[DeepRacer 400L（DeepRacer 汽车）工作坊](https://catalog.workshops.aws/deepracer-car-400l/en-US) -  启用通过 SSM、Greengrass 和 CloudWatch 对 DeepRacer 进行日志收集和电池监控。
[DeepRacer 401（GenAI）工作坊](https://catalog.us-east-1.prod.workshops.aws/workshops/d8a88732-5154-49ac-9725-033c0bc74029/en-US/30-lab-1-aws-deepracer-model-evaluator-using-agents) - 创建一个“DeepRacer 专家”聊天机器人，并测试您的 DeepRacer 模型与 AI 生成的 DeepRacer 赛道图像的对比。
[Jeremy Pedersen 的 DeepRacer “GenAI 实验室”（公共档案）](https://github.com/jeremypedersen/deepracer-genai) - 对 DeepRacer 401（GenAI）工作坊 的重写，以支持中文并更改所使用的 LLM（出于法律/合规原因）。
[Jeremy Pedersen 的 DeepRacer “深度黑客”](https://github.com/jeremypedersen/deepracer-deephacks)  - 基于现在已不再使用的 AWS 工作坊，直接在 SageMaker 和 RoboMaker 上运行和评估 DeepRacer 模型的代码。

## DeepRacer 解决方案（AWS 解决方案库）
[使用 SageMaker 训练 DeepRacer 模型](https://aws.amazon.com/cn/solutions/guidance/training-an-aws-deepracer-model-using-amazon-sagemaker/) - 一篇较旧的帖子，展示了用户如何直接使用 SageMaker 训练和评估 DeepRacer 模型
DREM（DeepRacer 事件管理）解决方案设置指南 - 向用户展示如何设置 DREM 来管理 DeepRacer 汽车、排行榜、模型上传和自动计时

## DeepRacer 博客（AWS）
[日志分析（来自 DBS 银行 Ray Goh 的客座文章）](https://aws.amazon.com/cn/blogs/machine-learning/using-log-analysis-to-drive-experiments-and-win-the-aws-deepracer-f1-proam-race/) - 解释如何使用 Jupyter Notebook 执行日志分析
[直接使用 SageMaker 训练 DeepRacer 模型](https://aws.amazon.com/cn/solutions/guidance/aws-deepracer-event-management/) - 包含视频。引导用户在 SageMaker 上训练模型。不幸的是，现在非常过时。

[Introducing AWS DeepRacer Log Analysis ](https://blog.deepracing.io/2020/03/30/introducing-aws-deepracer-log-analysis/)
[deepracer-analysis-tool](https://github.com/aws-deepracer-community/deepracer-analysis/)

## DeepRacer 博客（社区）
官方 DeepRacer 社区网站 - 此页面主要是一个占位符。要与社区成员联系，您应该加入 Discord 渠道。
如何在 15 分钟内训练一个 DeepRacer 模型 - Falk Tandetzky 撰写的一篇博客，讲述他如何训练他的第一个模型。包括一些聪明的方法来思考什么是好的转向角。他还有一篇 后续文章 关于他在 re:Invent 中的表现（2019 年全球前 8 名）以及一些 GitHub 上的示例代码。
在 7 个步骤中创建自己的 DeepRaser 路线 - 引导您使用泡沫瓷砖和胶带创建自己的赛道
如何赢得 DeepRacer - 来自 Axel Springer TechCon
打入 DeepRacer Top 1%，Part 1 和 Part 2 - DS 为 Building Fynd 撰写的博客
构建 DeepRacer 定时器软件 / 硬件 - 一篇关于该过程的早期社区博客。这现在已纳入DREM。

## DeepRacer 模型训练与日志分析
[deepracer-for-cloud](https://aws-deepracer-community.github.io/deepracer-for-cloud/)（在任何地方运行 DeepRacer - DeepRacer 社区自有的离线 DeepRacer 训练和分析解决方案的安装与使用手册。
[Jeremy Pedersen 的 DeepRacer "Deep Stats"](https://github.com/jeremypedersen/deepracer-deepstats)（公开档案 - 我自己的 DeepRacer 日志分析代码，重度借鉴了 DeepRacer 社区的日志分析代码 和一个现已停用的 DeepRacer 400L 研讨会。

## AWS 和社区 DeepRacer GitHub 页面
[官方 AWS DeepRacer GitHub 仓库](https://github.com/aws-deepracer/) - 所有（开源）DeepRacer 软件堆栈代码的集合。大多数代码并不是以立即可用的形式提供。请查看 DeepRacer 社区的 GitHub 代码（见下方链接）。
[DeepRacer 社区的 GitHub 仓库](https://github.com/aws-deepracer-community) - 用于在 *任何地方* 运行 DeepRacer 训练和评估任务的代码，以及来自之前 DeepRacer 联赛官方比赛的数据、日志分析代码等。
特别有用：[所有 DeepRacer 赛道名称的列表](https://github.com/aws-deepracer-community/deepracer-simapp/blob/master/tracks.txt) （用于日志分析等所需的 .npy 文件）

## 学术论文
引用或包含 DeepRacer 的已发布工作。

基于图像的自主微型赛车动作平滑性正则化研究
物理赛道上的 DeepRacer：参数探索与性能评估
利用图像梯度弥合 Sim2Real 差距以实现端到端自主驾驶任务
DeepRacing：用于自主赛车的参数化轨迹
DeepRacer：用于 Sim2Real 强化学习实验的教育性自主赛车平台

