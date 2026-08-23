# TSM 简体中文：适配 TSM v0.50.0 的完整变更记录

基准文件：`Chinese for PC.json`（Dexicty 0.50.0）。本记录中的行号均指向正式安装文件 `zh-cn.json`。

## 校验结果

- 新版英文固定界面键：2529 项，中文覆盖：100%
- 从旧版中文补回：133 项
- 依据新版英文新译：101 项
- 已讨论后修改：54 项
- 英中占位符不一致：0 项
- 服务器/游戏运行时任务描述及资源名称：完整保留，共 2433 项
- 格式规范化：重新序列化为有效 JSON；原文件重复的空键和 `Continue with the save file...` 各保留最后一个有效值。

## 本轮新增修改

| 最终行 | 英文键 | v4 翻译 | 当前翻译 |
| ---: | --- | --- | --- |
| 3 | _meta.name | angel v4 | Chinese (Simplified) |
| 4 | _meta.code | zh | zh-CN |
| 918 | in {} | 在 {} 中 | 还有 {} |

- `_meta.name` 改为纯英文 `Chinese (Simplified)`，确保中文字体加载前语言选项仍可辨认。
- `_meta.code` 改为 `zh-CN`，用于明确标识简体中文，并为未来繁体语言包留出区分空间。
- `_meta.font` 继续使用 `Default.ttf`，不捆绑额外字体。
- 近期事件倒计时 `in {}` 从“在 {} 中”改为“还有 {}”。
- v4 已确认的 `Automation`→“跑图辅助”、独立键 `Wax`→“自动跑图(慎)”、`Home`→“回家”与 `Actions`→“动作”全部保留。
- `{fps}`、`{ping}` 等 Discord 状态变量继续保留社区译者加入的原始扩展翻译，本版不删除。

## 已讨论后修改

| 最终行 | 英文键 | 原译 | 测试版 | 说明 |
| ---: | --- | --- | --- | --- |
| 3 | _meta.name | 中文 \| Dexicty「0.50.0」 | Chinese (Simplified) | 正式发布语言名称 |
| 4 | _meta.code | zh | zh-CN | 区分简体与未来繁体语言包 |
| 5 | _meta.font | ZiYueYingYinSong-2.ttf | Default.ttf | 使用模组默认字体，不附带额外字体 |
| 49 | A pulsing ring behind each mark, for reading the overlay against bright sky. | 每个标记后的脉动光环，便于在明亮天空下阅读叠加层。 | 每个标记后的脉动光环，便于在明亮天空背景下辨认悬浮显示。 | 已讨论确认 |
| 68 | Actions | 操作 | 动作 | 已讨论确认 |
| 79 | Adds all known map shrine unlock keys. | 添加所有已知的地图神坛解锁钥匙。 | 向服务器发送解锁数据，以解锁所有已知的地图神坛。 | 已讨论确认 |
| 80 | Adds all known music sheet unlock keys. | 添加所有已知的乐谱解锁钥匙。 | 向服务器发送解锁数据，以解锁所有已知的乐谱。 | 已讨论确认 |
| 154 | Aurora | 极光 | AURORA | 已讨论确认 |
| 171 | Automation | 自动化 | 跑图辅助 | 已讨论确认 |
| 175 | Aviary Village | 飞鸟村 | 云巢 | 已讨论确认 |
| 176 | Aviary Village or Village of Dreams | 飞鸟村或梦想村 | 云巢或圆梦村 | 已讨论确认 |
| 201 | Bird Nest | 鸟巢 | 云顶浮石（右图） | 已讨论确认 |
| 255 | Butterfly Fields | 蝴蝶田 | 蝴蝶平原 | 已讨论确认 |
| 292 | Carry | 背负 | 肩背 | 已讨论确认 |
| 498 | Developer overlays | 开发者菜单 | 开发者调试显示 | 已讨论确认 |
| 525 | Discord Rich Presence | Discord 富活动状态 | Discord 游戏活动状态 | 已讨论确认 |
| 674 | Fast Meditate | 快速传送 | 快速冥想(含回家) | 已讨论确认 |
| 819 | Grow | 生长 | 变大 | 已讨论确认 |
| 847 | Hidden Forest | 雨林（森林） | 雨林 | 已讨论确认 |
| 863 | Home | 遇境 | 回家 | 已讨论确认 |
| 869 | How big the overlay draws, as a percentage. Separate from the menu's scale - the size that reads well over the world is not the size that reads well on a settings page. Scale By Distance still overrides it per marker. | 覆盖层以百分比形式绘制的大小。该设置独立于菜单缩放——在游戏世界里看起来清晰的大小，在设置页面上不一定合适。“按距离缩放”仍会针对每个标记覆盖此设置。 | 悬浮显示的绘制大小，以百分比表示。此设置独立于菜单缩放——适合显示在游戏世界中的大小，不一定适合设置页面。“按距离缩放”仍会针对每个标记覆盖此设置。 | 已讨论确认 |
| 918 | in {} | 在 {} 中 | 还有 {} | 已讨论确认 |
| 1310 | Overlay Scale | 覆盖层比例 | 悬浮显示缩放 | 已讨论确认 |
| 1311 | Overlays | 叠加层 | 悬浮显示 | 已讨论确认 |
| 1344 | Picking a track on the Music tab sets it as the background music for every player in the area, not just you. Only tracks whose audio bank is already loaded on their machine will play - in practice the Aurora set travels and most level tracks do not. | 在“音乐”选项卡中选择一首曲目，会将其设为该区域所有玩家的背景音乐，而不仅仅是你自己。只有那些音频库已在他们本机加载的曲目才会播放——实际上，Aurora 曲目集会随玩家走（即随处可播），而大多数关卡曲目则不会。 | 在“音乐”选项卡中选择一首曲目，会将其设为该区域所有玩家的背景音乐，而不仅仅是你自己。只有那些音频库已在他们本机加载的曲目才会播放——实际上，AURORA 曲目集会随玩家走（即随处可播），而大多数关卡曲目则不会。 | 已讨论确认 |
| 1408 | Prairie Cave | 草原洞穴 | 幽光山洞 | 已讨论确认 |
| 1409 | Prairie Heights | 草原高地 | 云峰 | 已讨论确认 |
| 1410 | Prairie Village | 草原村庄 | 云中仙乡（三塔图） | 已讨论确认 |
| 1605 | Report the mod overlay's frame rate. | 报告模组叠加层的帧率。 | 显示模组悬浮显示的帧率。 | 已讨论确认 |
| 1799 | Shrink | 缩小 | 变小 | 已讨论确认 |
| 1894 | Steps | 步数 | 步骤 | 已讨论确认 |
| 1969 | Temple of the Prairie | 草原神庙 | 云野神殿 | 已讨论确认 |
| 2008 | The Citadel | 城堡 | 霞光城 | 已讨论确认 |
| 2017 | The default palette is chosen so a dye reads as violet and a candle as ember at fifty metres - which is what makes the overlay legible without reading a single label. | 默认调色板选择使染料在五十米处呈现紫色，蜡烛呈现余烬色——这使得无需阅读标签即可辨认叠加层。 | 默认调色板经过专门选择，使染料在五十米外显示为紫罗兰色、蜡烛显示为余烬色——因此无需读取文字标签，也能辨认悬浮显示。 | 已讨论确认 |
| 2209 | Travel | 旅行 | 传送 | 已讨论确认 |
| 2210 | Travel timed out - the level did not come up. | 旅行超时——关卡未出现。 | 传送超时——未能进入目标场景。 | 已讨论确认 |
| 2211 | Travelling to the objective... | 正在前往目标点... | 正在传送至目标点... | 已讨论确认 |
| 2291 | Village of Dreams | 梦想村 | 圆梦村 | 已讨论确认 |
| 2328 | Wax | 烛火 | 自动跑图(慎) | 已讨论确认 |
| 2412 | World Overlay | 世界叠加层 | 游戏内悬浮显示 | 已讨论确认 |
| 2413 | World overlay | 世界覆盖层 | 游戏内悬浮显示 | 已讨论确认 |
| 2570 | ====World overlay==== | 世界叠加层 | 游戏内悬浮显示 | 已讨论确认 |
| 2700 | Aurora Apple Music URL | 极光 Apple Music URL | AURORA Apple Music 链接 | 已讨论确认 |
| 2809 | Prairie_NestAndKeeper | 云顶浮石 | 云顶浮石（右图） | 已讨论确认 |
| 2811 | Prairie_Village | 云中仙乡 | 云中仙乡（三塔图） | 已讨论确认 |
| 3130 | Aurora Concert | 极光演唱会 | AURORA演唱会 | 已讨论确认 |
| 3596 | Help Bumbling Boatswain or Slumbering Shipwright find treasure in Prairie Village | 帮助笨拙水手或沉睡造船师在云野三塔图寻找宝藏 | 帮助笨拙水手或沉睡造船师在云中仙乡寻找宝藏 | 已讨论确认 |
| 3597 | Help Cackling Cannoneer or Slumbering Shipwright find treasure in Prairie Village | 帮助大笑炮手或沉睡造船师在云野三塔图寻找宝藏 | 帮助大笑炮手或沉睡造船师在云中仙乡寻找宝藏 | 已讨论确认 |
| 3653 | Catch the wandering lights around the Bird Nest | 收集鸟巢周围散落的光芒 | 收集云顶浮石周围散落的光芒 | 已讨论确认 |
| 3654 | Catch the wandering lights in Prairie Village | 收集云野三塔图散落的光芒 | 收集云中仙乡散落的光芒 | 已讨论确认 |
| 3683 | Meditate by the Bird Nest | 在鸟巢旁冥想 | 在云顶浮石旁冥想 | 已讨论确认 |
| 3684 | Meditate in Prairie Village | 在云野三塔图冥想 | 在云中仙乡冥想 | 已讨论确认 |
| 3777 | Go on a floating boat ride around the Bird Nest with Lively Navigator | 与活泼领航员一起乘坐漂浮船环游鸟巢 | 与活泼领航员一起乘坐漂浮船环游云顶浮石 | 已讨论确认 |
| 4252 | Geyser | 圣岛喷泉 | 间歇泉 | 已讨论确认 |

## 新增的固定界面翻译

| 最终行 | 英文键 | 测试版中文 | 来源 |
| ---: | --- | --- | --- |
| 17 | (not in this level) | (不在当前场景) | 旧版中文继承 |
| 18 | (not named yet) | (尚未命名) | 旧版中文继承 |
| 35 | A friendship has gone stale | 一段好友关系已失效 | 依据新版英文新译 |
| 40 | A message was translated | 一条消息已翻译 | 依据新版英文新译 |
| 41 | A moderation action was applied to your account | 你的账号已受到管理措施 | 依据新版英文新译 |
| 44 | a number | 数字 | 旧版中文继承 |
| 50 | A server request completed | 服务器请求已完成 | 依据新版英文新译 |
| 54 | a switch | 开关 | 旧版中文继承 |
| 55 | A whole number at +0x{:X}. The engine stores every scalar as a 32-bit word, so a switch is 1 or 0. | 内存偏移+0x{:X}处为整数，游戏使用32位数值存储，开关状态1代表开启、0代表关闭 | 旧版中文继承 |
| 75 | Add key | 添加解锁标识 | 旧版中文继承 |
| 105 | Alt+Mouse | Alt+鼠标 | 旧版中文继承 |
| 106 | An event queue is waiting for you | 有事件队列等待你处理 | 依据新版英文新译 |
| 109 | Ancestor Transform | 先祖变身 | 依据新版英文新译 |
| 150 | At +0x{:X} in the block, as {}.<br><br>{} | 模块偏移+0x{:X}，数值为{}<br><br>{} | 旧版中文继承 |
| 180 | Back | 返回 | 旧版中文继承 |
| 210 | Block them? | 是否屏蔽该玩家？ | 旧版中文继承 |
| 243 | Broadcast Sound | 广播声音 | 依据新版英文新译 |
| 275 | Byte (u8) | 字节（无符号8位） | 旧版中文继承 |
| 276 | Bytes (hex) | 字节（十六进制） | 旧版中文继承 |
| 279 | Called {}. | 已执行{} | 旧版中文继承 |
| 288 | Candle | 白蜡烛 | 旧版中文继承 |
| 333 | Clear the objects you have placed, on your own screen and everyone else's. Only ever touches ones they already attribute to you. | 清除你放置的物件，并同步到你和其他所有人的画面。只会处理游戏已认定属于你的物件。 | 依据新版英文新译 |
| 334 | Clear the search to see every kind of notification. | 清空搜索以查看所有类型的通知。 | 依据新版英文新译 |
| 336 | Clear the search to see everything that has arrived. | 清空筛选，显示所有加载项 | 旧版中文继承 |
| 337 | Clear the search to see everything the game can send. | 清空筛选，显示游戏所有可加载内容 | 旧版中文继承 |
| 349 | Click to flip it. | 点击切换开关状态 | 旧版中文继承 |
| 360 | Cold Wind | 寒风 | 旧版中文继承 |
| 373 | Colour | 颜色 | 依据新版英文新译 |
| 374 | colour | 色彩 | 旧版中文继承 |
| 381 | Community | 社区 | 旧版中文继承 |
| 446 | Cross the full-AFK line as well, which sleeps the avatar instead of sitting it. | 同时达到完全挂机的判定，让角色进入睡眠而不是坐下。 | 依据新版英文新译 |
| 458 | Cycle speed | 循环速度 | 依据新版英文新译 |
| 459 | Cycles the hue instead of holding one colour. | 让色相循环变化，而不是保持单一颜色。 | 依据新版英文新译 |
| 466 | Day | 白昼 | 旧版中文继承 |
| 471 | Declared by: {} | 定义来源：{} | 旧版中文继承 |
| 473 | Default: {} | 默认值：{} | 旧版中文继承 |
| 475 | Del | 删除 | 旧版中文继承 |
| 492 | Deposit | 献祭 | 旧版中文继承 |
| 499 | Dig | 挖掘 | 旧版中文继承 |
| 500 | Dig with a shovel for everyone else in the area. You will not see it yourself. | 向区域内其他所有人显示你用铲子挖掘；你自己看不到该效果。 | 依据新版英文新译 |
| 537 | Double | 双倍 | 旧版中文继承 |
| 552 | Drop it on the ground | 放置在地面 | 旧版中文继承 |
| 578 | Each of these is sent once per person - {} right now. | 以下每项会对每名玩家发送一次——当前共 {} 名。 | 依据新版英文新译 |
| 588 | Emitters | 发射器 | 依据新版英文新译 |
| 608 | End | 结束 | 旧版中文继承 |
| 609 | Engine state | 游戏引擎状态 | 旧版中文继承 |
| 648 | Everything is refused | 全部拦截 | 旧版中文继承 |
| 658 | Expects: {} | 所需参数：{} | 旧版中文继承 |
| 667 | F | F键 | 旧版中文继承 |
| 671 | Fake AFK | 伪装挂机 | 依据新版英文新译 |
| 699 | Filter properties | 属性筛选 | 旧版中文继承 |
| 710 | Firework Show | 烟花表演 | 依据新版英文新译 |
| 719 | Flies any of the game's emitters as a firework, for everyone in the area. | 将游戏中的任意发射器作为烟花发射，并向区域内所有人显示。 | 依据新版英文新译 |
| 722 | Float | 浮点数 | 旧版中文校正后继承 |
| 728 | Fly | 飞行 | 旧版中文继承 |
| 745 | Follow it with the camera | 镜头跟随该物体 | 旧版中文继承 |
| 755 | Forest | 雨林 | 旧版中文继承 |
| 768 | Friend Post sent | 好友动态已发送 | 依据新版英文新译 |
| 777 | Full trips around the colour wheel per second. | 每秒绕完整色相环的圈数。 | 依据新版英文新译 |
| 818 | Group: {} | 分组：{} | 旧版中文继承 |
| 820 | Guard | 防护 | 旧版中文继承 |
| 828 | Handles | 操控柄 | 旧版中文校正后继承 |
| 829 | Hands Out | 摊手 | 旧版中文继承 |
| 836 | HDR Brightness | 高动态亮度 | 旧版中文继承 |
| 848 | Hide anything further away than this, in metres. The overlay draws the sphere while you are changing it. | 隐藏距离超过此数值的物件，单位为米。调整时悬浮显示会绘出范围球。 | 依据新版英文新译 |
| 849 | Hide it | 隐藏 | 旧版中文继承 |
| 870 | How bright the overlay's white is, now that the game is presenting in HDR. Nothing reports what the game drew its own menus at - turn this until the two match. | HDR 模式下悬浮显示中白色的亮度。游戏不会报告其自身菜单的绘制亮度——请调整到两者一致。 | 旧版中文校正后继承 |
| 871 | How close somebody has to be to get a card, in metres. | 其他玩家需要靠近到多远才能收到信息卡，单位为米。 | 依据新版英文新译 |
| 877 | How far out around you the rockets set off from. At zero they all leave from the one point under you. Where each one curves to after that is the game's own randomiser, not ours. | 火箭从你周围多远处升空。设为 0 时，全部从你正下方同一点发射；之后的弯曲方向由游戏随机决定，并非模组控制。 | 依据新版英文新译 |
| 892 | How many go up per volley. | 每轮发射的数量。 | 依据新版英文新译 |
| 893 | How many volleys one Launch fires. | 每次“发射”包含的轮数。 | 依据新版英文新译 |
| 933 | Info Card Distance | 信息卡距离 | 依据新版英文新译 |
| 935 | Injured | 受伤状态 | 旧版中文继承 |
| 941 | Int16 | 16位整数 | 旧版中文继承 |
| 942 | Int32 | 32位整数 | 旧版中文继承 |
| 943 | Int64 | 64位整数 | 旧版中文继承 |
| 976 | Key | 按键/解锁标识 | 旧版中文继承 |
| 991 | Last sent | 上次发送 | 依据新版英文新译 |
| 995 | Layout not read from the game | 界面布局未读取游戏原生配置 | 旧版中文继承 |
| 996 | Lazy | 简易低速模式 | 旧版中文继承 |
| 1009 | Level, speed, and how long each emote loops for. | 动作等级、播放速度、单次循环时长 | 旧版中文继承 |
| 1010 | Level-up cinematic | 升级动画 | 依据新版英文新译 |
| 1013 | Lie Down | 躺下 | 依据新版英文新译 |
| 1018 | Light Horn | 发光号角 | 旧版中文继承 |
| 1027 | Load into a level, then reopen this. | 进入场景后重新打开工具面板 | 旧版中文继承 |
| 1055 | Make them pout | 让对方噘嘴 | 依据新版英文新译 |
| 1056 | Make yourself glow for everyone else in the area. You will not see it yourself. | 让区域内其他所有人看到你发光；你自己看不到该效果。 | 依据新版英文新译 |
| 1057 | Makes every server A/B experiment report disabled. Wins over Force All On. | 禁用所有服务器测试分支，优先级高于强制开启 | 旧版中文继承 |
| 1058 | Makes every server A/B experiment report enabled - the unreleased and bucketed behaviour the account was not selected for. | 解锁全部测试分支，体验账号未分配的未实装内容 | 旧版中文继承 |
| 1065 | Manatee II | 海牛 II | 旧版中文继承 |
| 1085 | Memory | 内存 | 旧版中文校正后继承 |
| 1112 | Move handles | 位移操控手柄 | 旧版中文继承 |
| 1146 | Nerdy | 专业调试模式 | 旧版中文继承 |
| 1149 | Network Filter | 网络拦截过滤器 | 旧版中文继承 |
| 1152 | Neutral | 中性色 | 旧版中文继承 |
| 1181 | No property matches that. | 无匹配属性 | 旧版中文继承 |
| 1190 | Nobody to act on | 没有可作用的玩家 | 依据新版英文新译 |
| 1196 | not editable | 不可编辑 | 旧版中文继承 |
| 1205 | Notes: {} | 备注：{} | 旧版中文继承 |
| 1251 | NPC | NPC | 旧版中文校正后继承 |
| 1256 | Object | 物件 | 旧版中文继承 |
| 1270 | Only methods the engine records as taking nothing can be called. The rest are listed so you can see what the class can do. | 仅无参引擎函数可直接调用，其余仅展示接口不可执行 | 旧版中文继承 |
| 1275 | Open a shop by key | 通过ID打开先祖商店 | 旧版中文继承 |
| 1314 | Override staged. It answers every read of that key. | 修改已缓存，游戏读取该ID均返回解锁状态 | 旧版中文继承 |
| 1347 | Pink | 粉色 | 依据新版英文新译 |
| 1351 | Place the chosen object at yourself, for everyone in the area including you. | 在自己所在位置放置所选物件，并向区域内包括你在内的所有人显示。 | 依据新版英文新译 |
| 1354 | Placeable Spawner | 可放置物生成器 | 依据新版英文新译 |
| 1359 | Plant | 植被 | 旧版中文继承 |
| 1365 | Play at everyone | 对所有人播放 | 依据新版英文新译 |
| 1366 | Play at them | 对对方播放 | 依据新版英文新译 |
| 1392 | Plays any of the game's sounds for everyone in the area. | 向区域内所有人播放游戏中的任意声音。 | 依据新版英文新译 |
| 1393 | Plays it from where each person is standing, for everyone in the area. | 从每名玩家所在位置播放，并让区域内所有人听到。 | 依据新版英文新译 |
| 1394 | Plays it from where they are standing, for everyone in the area. | 从对方所在位置播放，并让区域内所有人听到。 | 依据新版英文新译 |
| 1395 | Plays the hide-and-seek pout on their character, for everyone in the area. | 让对方角色播放捉迷藏噘嘴效果，并向区域内所有人显示。 | 依据新版英文新译 |
| 1396 | Plays the hide-and-seek win banner and its sound on their screen. Only they see it. | 在对方画面播放捉迷藏胜利横幅和音效；只有对方能看到。 | 依据新版英文新译 |
| 1397 | Plays the level-up burst where they are standing, for everyone in the area. This one may also move their camera. | 在对方所在位置播放升级爆发效果，并向区域内所有人显示；该效果也可能移动对方镜头。 | 依据新版英文新译 |
| 1399 | Pops the "relationship restored" message on their screen. Only they see it. | 在对方画面弹出“关系已恢复”消息；只有对方能看到。 | 依据新版英文新译 |
| 1407 | Prairie | 云野 | 旧版中文继承 |
| 1443 | Proud | 自豪动作 | 旧版中文继承 |
| 1445 | Pull light from them | 从对方身上吸取光 | 依据新版英文新译 |
| 1447 | Purple | 紫色 | 依据新版英文新译 |
| 1457 | Puts the tag-game ancestor glow on their character, for everyone in the area. | 给对方角色附加追逐游戏中的先祖光效，并向区域内所有人显示。 | 依据新版英文新译 |
| 1473 | Radiance Tint | 光辉染色 | 依据新版英文新译 |
| 1488 | Range: {} | 生效范围：{} | 旧版中文继承 |
| 1497 | Re-read the personality your avatar currently has. | 重新读取角色个性动作 | 旧版中文继承 |
| 1509 | read-only | 只读 | 旧版中文继承 |
| 1516 | Reading the level... | 加载场景资源中... | 旧版中文继承 |
| 1517 | Reading the registry | 读取内存注册表 | 旧版中文继承 |
| 1528 | Reads as away to everyone else while you keep playing. | 你可以继续游玩，但其他所有人会看到你处于离开状态。 | 依据新版英文新译 |
| 1536 | Recolours your avatar's glow for everyone in the area. | 改变你的角色光芒颜色，并向区域内所有人显示。 | 依据新版英文新译 |
| 1547 | Referenced by | 引用自 | 旧版中文继承 |
| 1548 | References | 引用列表 | 旧版中文继承 |
| 1550 | Reflection registry: {} classes, {} members, {} methods. | 反射注册表：{}个类，{}个成员，{}个函数 | 旧版中文继承 |
| 1578 | Remove this friend? | 确定删除该好友？ | 旧版中文继承 |
| 1589 | Removes the hold delay at every meditation circle. | 跳过所有冥想点的长按等待，包括回家。 | 依据新版英文新译 |
| 1615 | Reset rotation | 重置旋转角度 | 旧版中文继承 |
| 1645 | Rotate handles | 旋转操控手柄 | 旧版中文继承 |
| 1646 | Rules | 拦截规则 | 旧版中文继承 |
| 1649 | Run Eden now? | 立即自动跑伊甸？ | 旧版中文继承 |
| 1654 | Running | 运行中 | 旧版中文继承 |
| 1656 | Sad | 难过 | 旧版中文继承 |
| 1658 | Sassy | 俏皮 | 旧版中文继承 |
| 1677 | SByte (i8) | 有符号字节(i8) | 旧版中文继承 |
| 1681 | Scale handles | 缩放操控手柄 | 旧版中文继承 |
| 1705 | Seconds between re-sends. There is no duration on the wire - the receiver stamps its own clock - so the tint is held by sending it again before it fades. Under the fade it looks continuous; over it, the colour pulses. | 重复发送的间隔秒数。消息本身不带持续时间，接收端会按自己的时钟计时，因此需在颜色消退前再次发送来维持染色。间隔短于消退时间时看起来连续，长于消退时间时颜色会脉冲闪烁。 | 依据新版英文新译 |
| 1706 | Seconds between volleys. | 每轮之间的间隔秒数。 | 依据新版英文新译 |
| 1715 | Section | 分区 | 旧版中文校正后继承 |
| 1716 | Select | 选中 | 旧版中文继承 |
| 1729 | Send them a friend toast | 向对方发送好友提示 | 依据新版英文新译 |
| 1738 | Server: {} | 服务器：{} | 依据新版英文新译 |
| 1756 | Shared Creation updated | 共享创作已更新 | 依据新版英文新译 |
| 1769 | Shout | 呼唤 | 旧版中文继承 |
| 1771 | Shovel Dig | 铲子挖掘 | 依据新版英文新译 |
| 1781 | Show it | 显示该项目 | 旧版中文继承 |
| 1791 | Show them a game over | 向对方显示游戏结束 | 依据新版英文新译 |
| 1792 | Show them a win banner | 向对方显示胜利横幅 | 依据新版英文新译 |
| 1837 | Sneaky | 潜行模式 | 旧版中文继承 |
| 1842 | Solemn | 庄重 | 旧版中文继承 |
| 1844 | Someone | 某位玩家 | 依据新版英文新译 |
| 1846 | Something else is driving this object's position. | 其他功能正在控制该物件坐标 | 旧版中文继承 |
| 1865 | Spawns one of the game's own objects, attached to you, for everyone else in the area. | 生成一个附着在你身上的游戏原生物件，并向区域内其他所有人显示。 | 依据新版英文新译 |
| 1869 | Spawns winged light where they are standing. It streams to YOU, not to them - the drop always belongs to whoever sent it - and everyone in the area sees it happen. | 在对方所在位置生成光翼。光翼会飞向你而非对方——掉落物始终属于发送者——区域内所有人都能看到该过程。 | 依据新版英文新译 |
| 1901 | Stop following it | 停止跟随 | 旧版中文继承 |
| 1905 | Stopped | 已停止 | 旧版中文继承 |
| 1957 | takes arguments | 支持参数输入 | 旧版中文继承 |
| 1977 | text | 文本 | 旧版中文继承 |
| 1978 | Text at +0x{:X}. Up to 15 characters - longer strings live on the heap and cannot be written in place. | 内存+0x{:X}文本，最多15字符，长字符串无法直接修改 | 旧版中文继承 |
| 1983 | That friendship has reached its cap for now | 该好友关系目前已达到上限 | 依据新版英文新译 |
| 2020 | The effects every player around you sees. | 你周围每名玩家都能看到的效果。 | 依据新版英文新译 |
| 2042 | The game keeps no field for this key, so the override answers reads of it rather than being written into the block. | 游戏无该数据存储字段，强制解锁仅读取时生效，不写入服务器配置 | 旧版中文继承 |
| 2043 | The game keeps no field for this key, so the value answers every read of it rather than being written anywhere. Up to {} characters. | 游戏无该存储项，自定义文本每次读取都会返回，最多{}字符 | 旧版中文继承 |
| 2059 | The hook address did not resolve on this game build. | 无法在当前游戏版本中解析钩子地址。 | 依据新版英文新译 |
| 2073 | The list of everything the game can send is being read. This takes a moment the first time. | 正在读取全部游戏交互事件，首次加载耗时片刻 | 旧版中文继承 |
| 2077 | The network filter could not install its hook. | 网络拦截钩子挂载失败 | 旧版中文继承 |
| 2095 | The same, with the game-over banner and sound instead of the win one. | 效果相同，但会改为播放游戏结束横幅和音效，而非胜利横幅。 | 依据新版英文新译 |
| 2103 | The server is moving you | 服务器正在传送你 | 依据新版英文新译 |
| 2105 | The server sent this key but the game keeps no field for it, so there is nothing to write. An override answers every read of it instead, including the reads at the next sign-in. | 服务器下发该ID，但游戏无存储字段；强制解锁永久生效，下次登录仍识别 | 旧版中文继承 |
| 2107 | The server wants to move you | 服务器请求传送你 | 依据新版英文新译 |
| 2112 | The sound name travels with the message, so everyone in the level hears exactly what you picked - and unlike a firework, the volume and the range travel with it too. | 声音名称会随消息发送，因此场景内所有人都会听到你所选的声音；与烟花不同，音量和传播范围也会一并发送。 | 依据新版英文新译 |
| 2132 | There is no ground under it to drop onto. | 下方无地面，无法落地 | 旧版中文继承 |
| 2135 | There is nothing left to refuse. | 无可拦截事件 | 旧版中文继承 |
| 2139 | These act on every other player in the instance, so they fill in once somebody else is here. | 这些功能会作用于当前实例中的其他所有玩家；有人加入后此处才会出现选项。 | 依据新版英文新译 |
| 2149 | This class exposes no reflected methods. | 该类无可调用反射函数 | 旧版中文继承 |
| 2166 | This object neither references anything nor is referenced by anything else in the level. | 该物件与场景其他物件无关联 | 旧版中文继承 |
| 2167 | This object runs rather than shows. Stop halts it; it does not undo what running it already did. | 该功能为持续执行，停止不会撤销已生效操作 | 旧版中文继承 |
| 2168 | This object type cannot be moved. | 该类型物件禁止移动 | 旧版中文继承 |
| 2169 | This one needs membership, so it was never built. | 此功能需要会员资格，因此尚未实现。 | 依据新版英文新译 |
| 2177 | Ticket | 活动门票 | 旧版中文继承 |
| 2187 | Timid | 腼腆动作 | 旧版中文继承 |
| 2202 | Tough | 坚毅动作 | 旧版中文继承 |
| 2221 | Try a shorter word - {} to search. | 搜索词过长，缩短后搜索{} | 旧版中文继承 |
| 2228 | Turn Off | 关闭 | 依据新版英文新译 |
| 2229 | Turn off {}? | 要关闭 {} 吗？ | 依据新版英文新译 |
| 2231 | Turn them into an ancestor | 把对方变成先祖 | 依据新版英文新译 |
| 2243 | Type: {} | 类型：{} | 旧版中文继承 |
| 2244 | Unavailable | 不可用 | 依据新版英文新译 |
| 2252 | Ungrouped | 未分组 | 旧版中文继承 |
| 2275 | Valley | 霞谷 | 旧版中文继承 |
| 2280 | Vault | 禁阁 | 旧版中文继承 |
| 2324 | Wasteland | 暮土 | 旧版中文继承 |
| 2351 | What your glow turns for everyone else. Ignored while Rainbow is on. | 其他人看到的你的光芒颜色。开启彩虹模式时此项无效。 | 依据新版英文新译 |
| 2365 | Whether this kind of notification is shown as a toast. | 是否将此类通知显示为弹窗提示。 | 依据新版英文新译 |
| 2377 | Which of the server's events you have refused. | 已拦截服务器事件 | 旧版中文继承 |
| 2406 | Wise | 沉稳动作 | 旧版中文继承 |
| 2440 | You have new mail | 你有新邮件 | 依据新版英文新译 |
| 2441 | You have new mail with an attachment | 你有一封带附件的新邮件 | 依据新版英文新译 |
| 2446 | Your friend list changed | 你的好友列表已更新 | 依据新版英文新译 |
| 2448 | Your friendship gains for this group are capped for now | 你在该组中的好友关系增益目前已达上限 | 依据新版英文新译 |
| 2451 | Your linkable star tags were updated | 你的可关联星标已更新 | 依据新版英文新译 |
| 2452 | Your message may violate the Community Guidelines and was blocked | 你的消息可能违反《社区准则》，已被拦截 | 依据新版英文新译 |
| 2457 | Your purchases were updated | 你的购买项目已更新 | 依据新版英文新译 |
| 2467 | {}  ({} of {}) | {}  （{} / {}） | 依据新版英文新译 |
| 2469 | {} accepted your invite | {} 接受了你的邀请 | 依据新版英文新译 |
| 2473 | {} came online | {} 已上线 | 依据新版英文新译 |
| 2476 | {} commented on your creation | {} 评论了你的创作 | 依据新版英文新译 |
| 2477 | {} could not be called. | {}调用失败 | 旧版中文继承 |
| 2484 | {} from {} | {}，来自 {} | 依据新版英文新译 |
| 2485 | {} has no effect while {} is on. Turning it on switches {} off. | 开启 {} 时，{} 不会生效。启用此项会关闭 {}。 | 依据新版英文新译 |
| 2486 | {} has reborn | {} 已重生 | 依据新版英文新译 |
| 2492 | {} is in this level {} times - showing {}. Travel again for the next one. | {} 在该场景中出现了 {} 次——当前显示第 {} 个。再次传送可前往下一个。 | 依据新版英文新译 |
| 2495 | {} is not on this object. | 该物件无{}属性 | 旧版中文继承 |
| 2507 | {} objects here, none of them placed scenery. | 此处{}物件，无场景装饰 | 旧版中文继承 |
| 2509 | {} of {} can be clicked in the world. | {} / {} 可交互物件 | 旧版中文继承 |
| 2511 | {} of {} refused | 拦截{} / {}项 | 旧版中文继承 |
| 2513 | {} placed objects here, none of them writable. | {}放置道具，无可编辑项 | 旧版中文继承 |
| 2515 | {} reacted to your shared creation | {} 对你的共享创作作出了回应 | 依据新版英文新译 |
| 2517 | {} sent a chat message | {} 发来一条聊天消息 | 依据新版英文新译 |
| 2518 | {} sent you a friend invite | {} 向你发送了好友邀请 | 依据新版英文新译 |
| 2519 | {} sent you a Friend Post | {} 向你发送了一条好友动态 | 依据新版英文新译 |
| 2520 | {} sent you a gift | {} 向你赠送了礼物 | 依据新版英文新译 |
| 2521 | {} strengthened your friendship | {} 加深了与你的好友关系 | 依据新版英文新译 |
| 2524 | {} wants to see more of your Shared Creations | {} 想查看更多你的共享创作 | 依据新版英文新译 |
| 2528 | {} went offline | {} 已下线 | 依据新版英文新译 |
| 2529 | {} with no position or bounds. | {}无坐标边界 | 旧版中文继承 |

## 本轮明确保留

- `Spirit` 相关用语继续使用“先祖”。
- `Winged Light` 相关用语继续使用“光翼”。
- `Princess Carry` / `Princess Carry II` 继续使用“公主抱”/“公主抱 II”。
- 新版中新增的每日任务整句翻译全部保留，不按固定英文界面文件裁掉。
