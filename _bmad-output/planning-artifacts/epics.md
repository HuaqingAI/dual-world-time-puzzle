---
stepsCompleted: [1, 2, 3, 4]
inputDocuments:
  - "D:/ProgramData/git/repository/github/huaqingai/dual-world-time-puzzle/_bmad-output/planning-artifacts/gdds/gdd-dual-world-time-puzzle-2026-05-19/gdd.md"
  - "D:/ProgramData/git/repository/github/huaqingai/dual-world-time-puzzle/_bmad-output/planning-artifacts/game-architecture.md"
  - "D:/ProgramData/git/repository/github/huaqingai/dual-world-time-puzzle/_bmad-output/planning-artifacts/ux-design-specification.md"
---

# dual-world-time-puzzle - Epic Breakdown

## Overview

This document provides the complete epic and story breakdown for dual-world-time-puzzle, decomposing the requirements from the GDD, UX Design if it exists, and Architecture requirements into implementable stories.

## Requirements Inventory

### Functional Requirements

FR1: 玩家必须能够以俯视角控制小精灵在花园房间中移动，移动支持细微调整，并能用键盘和手柄完成标准小房间主通路穿越。

FR2: 垂直切片必须提供一个中心花园小块、一个完整花园房间、一个简短开始状态和一个结束状态，支持外部试玩。

FR3: 玩家进入房间后，应能在入口附近看到发光种子、出口花、关键对象或明确目标方向。

FR4: 玩家必须能够用单按钮在“枯萎 / Withered”和“盛放 / Bloom”世界状态之间切换；切换过程必须进入短暂转场并锁定重复输入。

FR5: 世界切换必须改变可通行路径或关键对象状态，而不只是视觉滤镜；玩家应能通过观察比较两个状态来规划路线。

FR6: 每次世界切换后，当前谜题相关的 1-2 个关键对象必须获得短暂视觉或音频强调，帮助玩家发现变化。

FR7: 藤蔓桥必须支持“枯萎不可通行 / 盛放展开并可通行”的状态规则，并提供展开动画、发光或音频反馈。

FR8: 花门必须支持睡眠、唤醒和开启状态，用于阻挡路线、打开路线或作为出口反馈。

FR9: 发光种子必须作为房间目标出现；玩家可以触碰或互动收集种子，收集后种子不进入背包格，而是以微光对象跟随玩家。

FR10: 出口花或种植点必须在玩家携带种子后响应，允许玩家种下种子或离开房间。

FR11: 种植必须触发 2-4 秒的恢复反馈，包括视觉恢复、植物舒展、音频层增强或其他可感知的空间变化。

FR12: 每颗主线种子必须带来中心花园的一处永久恢复变化，并能提示下一颗种子方向、下一房间入口或后续章节路径。

FR13: 房间成功条件必须是收集当前房间发光种子，并把它带到出口花或种植点完成种植反馈。

FR14: 整体进度必须由“种下发光种子”驱动，支持房间内进展、房间完成、中心花园进展、区域进展和整体进展。

FR15: 房间重置必须恢复当前房间谜题对象和玩家位置，但不能清除已完成的中心花园永久恢复或已种下的种子记录。

FR16: 玩家辅助必须包含被动提示、观察提示、闲置轻推、手动提示和重置能力；提示必须先引导观察方向，再提示操作顺序。

FR17: 暂停与设置能力必须覆盖继续、提示、重置房间、设置、退出、音量、显示和提示相关选项。

FR18: 输入必须支持移动、世界切换、互动 / 确认、重置房间、暂停 / 设置；主线体验只依赖移动、世界切换和互动三个核心动作。

FR19: 垂直切片首房间必须包含小精灵移动、世界切换、藤蔓桥、花门、发光种子、出口花和种植反馈的完整闭环。

FR20: 首房间推荐流程必须覆盖入口目标展示、世界切换教学、藤蔓桥路线理解、花门反馈、种子收集、返回出口和种植仪式。

FR21: 关卡类型必须支持中心花园、教学房间、主题机制房间、组合房间、恢复房间和可选房间的规划模型。

FR22: 难度进展必须从教学、核心概念、强化、组合到可选挑战递进，每个阶段控制规则负载和目标解谜时长。

FR23: 资产最低集合必须覆盖小精灵、房间地块双状态、藤蔓桥、花门、发光种子、出口花、中心花园小块、世界切换涟漪、花瓣路标、微光轨迹、种植粒子和关键音频。

FR24: 音频必须区分枯萎 / 盛放环境层，并为世界切换、藤蔓桥、花门、种子收集和种植完成提供确认反馈。

FR25: V1 规划目标应支持 4 个区域、16-24 个主线房间和 4 个区域恢复节点，但该范围不属于当前垂直切片承诺。

FR26: V1 和主线范围必须明确排除传统经济系统、完美步数挑战、每日谜题、程序生成主线关卡、排行榜和强制速通评价，除非后续经过正式范围变更。

FR27: 可选重玩价值应来自回访已修复房间、查看前后环境变化、收集低压力明信片或种子图鉴片段，以及在中心花园回看永久变化。

### NonFunctional Requirements

NFR1: 主线体验不得使用敌人、死亡、硬倒计时、战斗、追逐或惩罚性失败作为压力来源。

NFR2: 错误尝试必须可逆；玩家可以继续尝试、观察提示、手动重置房间或离开房间。

NFR3: 关键状态不得只靠颜色表达，必须至少同时改变形状、轮廓、动画、发光、声音、碰撞或通行状态。

NFR4: 关键对象变化必须在世界切换后的 1 秒内被玩家注意到；玩家首次主动切换后应在 10 秒内观察到至少一个有意义变化。

NFR5: 世界切换必须在 0.45-0.75 秒内完成，无加载屏、无明显卡顿，转场期间不接受重复切换输入。

NFR6: 藤蔓桥展开反馈目标为 0.6-0.9 秒；种子收集闪光目标为 0.3-0.5 秒；种植仪式目标为 2-4 秒。

NFR7: PC / Steam 垂直切片必须在 1080p 下稳定 60 FPS，并在 10 分钟核心循环试玩中无明显掉帧。

NFR8: Web demo 应在主流桌面浏览器稳定 60 FPS，弱设备可接受 30 FPS 下限。

NFR9: Web demo 首次可交互目标为普通宽带环境下 30 秒内。

NFR10: 移动和世界切换输入响应目标低于 100ms。

NFR11: 键盘和手柄都必须能够完成完整房间闭环。

NFR12: 教学房间目标是 80% 以上目标玩家在 5 分钟内完成。

NFR13: 70% 以上试玩玩家应能用自己的话说明“切换世界会改变路径或对象状态”。

NFR14: 70% 以上试玩玩家应能在种下第一颗种子后表达明确的修复回报感。

NFR15: 因看不懂藤蔓桥、花门、出口花或种子用途而卡住的玩家比例目标应低于 20%。

NFR16: 前 3 个主线房间不应要求玩家记忆屏幕外对象状态；主线房间必要操作链应控制在 3-6 个关键步骤。

NFR17: 关键目标应在入口 3 秒内可见，或通过花瓣路标明确暗示。

NFR18: 画面密度必须服务可读性，装饰植物不得掩盖路线和交互对象。

NFR19: 正式资产必须统一调色、轮廓、动画节奏和导入规范，避免 AI 或占位素材造成拼贴感。

NFR20: 试玩反馈必须能明确指向下一阶段优先级，包括视觉可读性、谜题结构、音频反馈、移动手感或恢复回报。

### Additional Requirements

- Starter Template: 架构明确要求从空 Godot 项目开始，而不是使用通用 starter template；初始化命令为 `godot --editor --path .`。
- 项目必须使用 Godot 4.6.2 stable 和 GDScript；GDScript 是 Web demo 支持的关键选择。
- 使用共享房间地图和状态驱动对象变化，而不是加载两套独立世界。
- 实现 `WorldStateManager` Autoload，提供 `Withered`、`Bloom`、`Switching` 显式状态机、切换守卫和状态信号。
- 所有受双世界影响的对象必须通过 `WorldStateResponder` 契约或等价组件响应世界状态变化。
- 双世界对象必须统一更新视觉、碰撞、互动可用性、动画和音频，避免视觉与碰撞状态不同步。
- 使用 Godot 2D renderer；Web-first 可靠性优先时使用 Compatibility renderer，除非效果需求需要 Forward+ 验证。
- 使用 `CharacterBody2D`、`StaticBody2D`、`Area2D` 和 collision layers 实现玩家移动、房间边界、桥通行、触发器和互动。
- 使用 `AnimationPlayer`、`AnimationTree` 或 tweens 实现世界切换、对象状态变化、种子跟随和种植仪式时序。
- 使用 Godot Audio Bus 架构，至少包含 `Master`、`Music`、`Ambience`、`SFX`、`UI`。
- 枯萎 / 盛放环境音应通过 AudioManager 或等价系统交叉淡入淡出，关键对象反馈由本地 SFX 或事件触发。
- 使用 Godot InputMap 定义移动、世界切换、互动、重置和暂停。
- 使用 Godot Control 节点与 CanvasLayer 实现暂停、设置、提示和调试 UI。
- 实现 `EventBus` Autoload，仅用于跨系统事件；本地父子或兄弟通信优先使用直接调用、父级中介或信号。
- 全局事件至少覆盖 `world_state_changed`、`seed_collected`、`seed_planted`、`room_completed`、`restoration_applied`。
- 实现 `SaveManager` Autoload，以带 schema version 的本地 JSON 保存已种下种子、中心花园恢复标记、已完成房间、设置和迁移版本。
- 垂直切片优先预加载资产；V1 内容增长后再按房间场景加载并定义轻量过渡。
- 使用 Godot `.tres` Resource 存储可编辑游戏定义，例如切换时长、提示延迟、种子跟随距离、互动半径、房间、种子和恢复数据。
- 配置必须区分固定常量、可调玩法资源、玩家设置和平台导出参数。
- 实现 `Log` Autoload，提供结构化日志等级 `ERROR`、`WARN`、`INFO`、`DEBUG`、`TRACE`。
- 可恢复错误必须记录警告并使用安全 fallback；关键存档、进度或状态错误必须停止风险操作并记录足够上下文；不得向玩家显示原始技术错误。
- 实现开发调试覆盖层，显示 FPS、当前房间、world_state、is_switching、carried_seed_id、planted_seed_ids 和 restoration_flags。
- 调试工具应支持开发构建中的世界状态热键、房间重置 / 回入口命令、种子 / 进度标记检查和可选碰撞可视化。
- 调试工具必须由 `debug_enabled` 控制，发布构建默认隐藏且不成为 gameplay 依赖。
- 项目结构必须按 `assets/`、`data/`、`scenes/`、`scripts/`、`tests/`、`docs/` 分层，并在脚本内按 world_state、puzzle_objects、seeds、restoration、hints、interaction、player、ui、debug 等领域组织。
- 文件、文件夹、场景、脚本、资源和动画命名必须遵循架构命名约定，例如 `snake_case` 文件、`PascalCase` 类、`snake_case` 函数、过去式 `snake_case` 信号。
- Puzzle object 可以读取世界状态和发事件，但不得直接修改存档或中心花园恢复；恢复系统必须消费事件并通过 `RestorationManager` 更新永久状态。
- UI 必须通过 manager 或 EventBus 请求 gameplay 改变，不得直接编辑 puzzle object 内部状态。
- Godot PC 和 Web export preset 应从垂直切片开始维护。
- 可选 AI 开发支持可以配置 GoPeak Godot MCP 和 Context7 MCP，但核心实现不得依赖它们运行。

### UX Design Requirements

UX-DR1: 建立轻量定制游戏 UI 设计系统，使用 Godot `Control`、`CanvasLayer`、Theme Resource 和可复用 UI 场景，而不是外部应用组件库。

UX-DR2: UI 系统必须定义设计 tokens，包括字体层级、语义颜色、世界状态辅助色、间距与尺寸、动效节奏和可访问性规则。

UX-DR3: UI 视觉必须保持柔和、低噪声、清晰、不过度装饰，且看起来属于 2D 手绘花园而不是桌面应用。

UX-DR4: 色彩系统必须覆盖“安静枯萎 + 温柔盛放 + 微光种子”三层；建议语义色包括 Seedlight `#F7D66A`、Bloom Green `#64B96A`、Petal Coral `#E9867A`、Clear Blue `#78B7D6`、Withered Green Gray `#7C8A77`、Deep Text `#24302A`、Soft Panel `#F4F1E8`。

UX-DR5: 微光种子暖金白必须作为最高注意力色，只用于种子、种植点、关键奖励和极少量引导。

UX-DR6: 文字系统必须优先清晰可读；中文主字体建议思源黑体 / Noto Sans SC，英文建议 Noto Sans / Inter；标题可少量使用圆润或手写感字体但不得影响可读性。

UX-DR7: 字体层级建议为 Menu Title 28-32px、Section Title 22-24px、Body / Menu Item 16-18px、Hint Text 15-16px、Debug Text 12-13px。

UX-DR8: UI 文案必须短、具体、温和，避免长段教程、命令式、批评式或系统化错误口吻。

UX-DR9: 布局必须使用 8px 基础间距；HUD 默认最小化，不遮挡房间、种子、玩家或关键对象。

UX-DR10: 互动提示应靠近玩家或目标对象，并使用固定安全边距，避免覆盖角色或关键反馈。

UX-DR11: 暂停、设置和提示面板可以居中或侧栏展示，但必须避免遮挡当前关键场景反馈。

UX-DR12: 基础 UI 组件必须覆盖 Text Label、Button / Focus Button、Panel、Toggle / Checkbox、Slider、Segmented Control、Focus Container 和 Debug Text Row。

UX-DR13: Interaction Prompt 组件必须用于种子、花门、出口花、种植点和提示点，支持 hidden、available、unavailable、pressed、disabled 状态。

UX-DR14: Interaction Prompt 必须提供输入图标或按键名、短动词、可选对象名；支持键盘和手柄提示文本，不能只显示图标。

UX-DR15: Interaction Prompt 必须在进入范围时淡入、离开范围时淡出；不可用时使用温和摇动、低亮或等价反馈。

UX-DR16: World State Indicator 必须轻量确认当前“枯萎 / 盛放 / 切换 / 锁定”状态，但不得替代场景变化或成为常驻大 HUD。

UX-DR17: World State Indicator 必须用文本或形状差异辅助表达状态，不能只靠颜色；切换开始进入 switching，切换完成后短暂显示目标状态并淡出或缩小。

UX-DR18: Seed Companion Indicator 必须显示种子已被收集并正在跟随，支持 no_seed、collecting、following、ready_to_plant、planted 状态。

UX-DR19: Seed Companion Indicator 必须以场景内跟随光点和微光轨迹为主，可在可读性不足时补充极简 HUD；不得使用“物品栏 1/1”等背包化表达。

UX-DR20: Gentle Hint Panel 必须在玩家主动请求或长时间卡住后提供提示，支持 hidden、passive_nudge、manual_hint_level_1、manual_hint_level_2 状态。

UX-DR21: Gentle Hint Panel 必须先提示观察对象，再提示操作顺序，不直接写完整答案；文本可读且支持键盘 / 手柄关闭。

UX-DR22: Pause and Settings Menu 必须提供继续、重置、设置、退出和提示入口，支持 closed、pause_root、settings、confirm_reset、confirm_exit 状态。

UX-DR23: Pause and Settings Menu 必须拥有明确焦点、循环导航和一致返回键；暂停时冻结 gameplay 输入，返回后恢复上一状态。

UX-DR24: Restoration Completion Feedback 必须在种下种子后确认修复成功，包含场景恢复动画、极简文本确认和可选下一步提示。

UX-DR25: Restoration Completion Feedback 必须支持 planting、restoring、completed、next_available 状态；首次种植展示完整 2-4 秒仪式，后续可缩短但不得消失。

UX-DR26: Debug Overlay 必须用于开发和 playtest 验证，支持 hidden、compact、expanded 状态，并显示 FPS、world_state、is_switching、room_id、carried_seed_id、restoration_flags。

UX-DR27: Debug Overlay 必须通过开发热键切换，不影响玩家 UI，发布构建默认隐藏。

UX-DR28: UI 组件实现必须使用可复用场景与脚本，包括 `scenes/ui/interaction_prompt.tscn`、`world_state_indicator.tscn`、`gentle_hint_panel.tscn`、`pause_menu.tscn`、`settings_menu.tscn`、`restoration_feedback.tscn` 和 `scenes/debug/debug_overlay.tscn`。

UX-DR29: UI 组件必须共享主题资源和设计 tokens，避免每个 UI 场景单独设置颜色、字体和间距；交互状态必须由明确 enum 或 state 字段驱动。

UX-DR30: Primary action 每个界面最多一个，支持 Enter / A 确认并拥有清楚焦点；secondary action 支持键盘、鼠标、手柄一致导航。

UX-DR31: 重置房间、退出试玩和恢复默认设置等风险操作必须二次确认，默认焦点不得落在危险行动上，且不使用刺眼红色表达风险。

UX-DR32: 成功反馈优先级必须为场景动画 > 声音 > 粒子 / 微光 > 极简 UI，并回答“我做对了吗”和“发生了什么”。

UX-DR33: 不可用反馈必须使用轻微摇动、低亮、花瓣闭合、短暂停顿或柔和短音，不使用错误警报或羞辱式文案。

UX-DR34: 提示反馈必须分为 Passive Cue、Idle Nudge 和 Manual Hint 三层，Idle Nudge 在 45-60 秒无进展后短暂强调关键对象。

UX-DR35: 设置行必须用于音量、显示、提示强度、减少闪烁、语言等选项，整行可聚焦，设置即时生效，失败时恢复上一个有效值。

UX-DR36: 确认对话必须用于重置房间、退出试玩、恢复默认设置，结构包含一句说明、安全行动、取消和危险确认。

UX-DR37: Gameplay 默认不显示地图和任务列表；玩家应通过场景构图、光点、花瓣、声音和中心花园空间理解方向。

UX-DR38: 暂停菜单必须为垂直结构，键盘支持方向键 / WASD、Enter、Esc，手柄支持 D-pad / 左摇杆、A、B，鼠标 hover 不得破坏当前手柄焦点状态。

UX-DR39: 修复完成后必须先展示场景变化，再出现轻量下一步提示；玩家应能选择继续探索、返回中心花园或暂停，而不是被立即传送。

UX-DR40: 暂停、设置、手动提示和确认对话可以使用 overlay；overlay 必须暂停 gameplay 输入并保留清楚返回方式；普通教学不得做成 modal。

UX-DR41: 垂直切片应尽量避免房间内加载屏；必要加载使用微光聚拢、短淡入淡出和不超过一行的状态文字。

UX-DR42: 中心花园未恢复区域不得显示“空”，应表现为沉睡、低亮、未盛放的可恢复空间。

UX-DR43: PC / Steam 默认以 16:9、1080p、键盘和手柄体验为基准，额外屏幕空间用于提升场景可读性和环境呼吸感，而不是增加常驻 UI。

UX-DR44: Web demo 必须适应常见桌面浏览器窗口，最低支持 1280x720 以上可玩，推荐 1920x1080；小窗口下 UI 文本和提示不得溢出，菜单优先保持单列结构。

UX-DR45: Web demo 不得因窗口尺寸变化暴露调试 UI 或破坏焦点顺序；首房间窗口化状态下仍需看清目标、关键对象和互动提示。

UX-DR46: 当前垂直切片不承诺移动端，但核心交互不得天然排斥未来触控；世界切换保持单按钮逻辑，互动范围不能过小，UI 不依赖 hover。

UX-DR47: UI 缩放必须至少支持 100%、125%、150%；菜单、提示和焦点环随 UI scale 放大。

UX-DR48: 响应式测试必须覆盖 1280x720、1600x900、1920x1080、2560x1440；后续 4K 需要验证 UI scale。

UX-DR49: UI 可读性应采用 WCAG AA 精神，普通 UI 文本对比度目标参考 4.5:1。

UX-DR50: 按钮和菜单项必须有清楚焦点状态，并支持键盘和手柄完整操作。

UX-DR51: Gameplay 中可交互目标不得要求像素级站位。

UX-DR52: 闪光、粒子和屏幕涟漪必须柔和，避免高频闪烁，并提供减少闪烁设置。

UX-DR53: 基础音频设置必须包含主音量、音乐和音效；可访问性设置必须包含减少闪烁、提示强度和可能的 UI 缩放。

UX-DR54: UX 测试必须覆盖键盘完整通关首房间、手柄完整通关首房间、混合输入后焦点不丢失、暂停 / 确认 / 设置可返回与取消。

UX-DR55: 可访问性测试必须覆盖色弱模拟、关闭音乐或降低音效后的关键反馈理解、减少闪烁开启后的世界切换和种植反馈清晰度。

UX-DR56: 至少 5 名目标玩家应完成试玩，用于记录是否看懂世界切换、是否知道种子跟随、是否感到修复回报。

UX-DR57: 首房间 UX 流程必须让玩家看到远处种子和断开路径，在路径不可达时发现藤蔓桥或花门，并通过环境微光或轻提示暗示切换。

UX-DR58: 首次切换后必须在 0.45-0.75 秒过渡后让关键对象高亮或展开；若玩家未注意到变化，45-60 秒后触发轻推提示。

UX-DR59: 种子收集流程必须在接近时增强微光并出现短互动提示，收集时提供短闪光和柔和音效，收集后变为跟随玩家的微光对象。

UX-DR60: 玩家携带种子后，出口花或种植点必须主动变得更可读；未携带种子互动时，使用温和不可用反馈并引导回种子方向。

UX-DR61: 种植流程必须让种植点发光并出现短提示，玩家确认后触发 2-4 秒仪式、颜色恢复、植物舒展、声音层增加和中心花园永久恢复。

UX-DR62: 完成确认必须配合场景，不应变成大 UI 弹窗抢走修复瞬间；中心花园应承担进度、情绪回报和下一步方向。

### FR Coverage Map

FR1: Epic 1 - 小精灵俯视角移动与键盘 / 手柄基础移动。

FR2: Epic 1 - 垂直切片基础结构。

FR3: Epic 1 - 入口目标和方向可读性。

FR4: Epic 2 - 枯萎 / 盛放单按钮切换。

FR5: Epic 2 - 双世界改变路径或对象状态。

FR6: Epic 2 - 切换后关键对象强调。

FR7: Epic 2 - 藤蔓桥状态规则。

FR8: Epic 2 - 花门状态规则。

FR9: Epic 3 - 发光种子收集与跟随。

FR10: Epic 3 - 出口花 / 种植点响应。

FR11: Epic 4 - 2-4 秒种植恢复反馈。

FR12: Epic 4 - 中心花园永久恢复变化。

FR13: Epic 3 - 房间成功条件。

FR14: Epic 4 - 种子驱动整体进度。

FR15: Epic 5 - 房间重置不清除永久进度。

FR16: Epic 5 - 分层提示系统。

FR17: Epic 5 - 暂停与设置能力。

FR18: Epic 1 - 核心输入动作集合。

FR19: Epic 3 - 首房间完整闭环内容。

FR20: Epic 3 - 首房间推荐流程。

FR21: Epic 6 - 关卡类型规划模型。

FR22: Epic 6 - 难度进展模型。

FR23: Epic 6 - 垂直切片最低资产集合。

FR24: Epic 6 - 双世界与关键交互音频反馈。

FR25: Epic 6 - V1 区域和房间扩展规划。

FR26: Epic 6 - V1 范围守卫。

FR27: Epic 6 - 可选重玩价值规划。

## Epic Summary

| Epic | Focus | FRs Covered |
| --- | --- | --- |
| Epic 1 | 玩家能进入垂直切片房间，控制小精灵移动，看见目标方向，并具备最小共享实现基础。 | FR1, FR2, FR3, FR18 |
| Epic 2 | 玩家能切换枯萎 / 盛放状态，并通过藤蔓桥、花门和关键对象反馈理解路线变化。 | FR4, FR5, FR6, FR7, FR8 |
| Epic 3 | 玩家能收集发光种子、看到种子跟随、带回出口花 / 种植点，并完成首房间目标。 | FR9, FR10, FR13, FR19, FR20 |
| Epic 4 | 玩家种下种子后，中心花园产生永久恢复变化，并理解后续方向或区域进展。 | FR11, FR12, FR14 |
| Epic 5 | 玩家卡住时能获得低压力提示，能重置当前房间，能通过暂停 / 设置管理体验。 | FR15, FR16, FR17 |
| Epic 6 | 垂直切片具备最低资产、Web demo 准备、关卡框架、V1 扩展边界和试玩验证。 | FR21, FR22, FR23, FR24, FR25, FR26, FR27 |

## Epic 1: 可进入的首个花园房间

玩家能进入垂直切片房间，控制小精灵移动，看见目标方向，并具备最小共享实现基础。

### Story 1.1: 启动到首个花园房间

As a 玩家,
I want 启动游戏后进入一个清晰的首个花园房间,
So that 我能立即理解自己在哪里、控制谁、以及房间里存在一个可探索目标。

**Acceptance Criteria:**

**Given** 玩家启动垂直切片构建
**When** 主场景加载完成
**Then** 游戏显示首个花园房间 shell，包含玩家起始点、房间边界、可读地面层和至少一个远处目标占位
**And** 不显示调试 UI 或复杂菜单遮挡场景

**Given** 首房间加载完成
**When** 玩家停留在入口附近
**Then** 摄像机 / 视口构图能同时显示玩家、主要通路方向和目标占位
**And** 在 16:9、1080p 基准下不需要滚动 UI 或额外说明才能理解房间方向

**Given** 开发者查看项目结构
**When** 检查 Godot 项目文件
**Then** 项目使用 Godot 4.6.2 + GDScript 的空项目基础
**And** 初始目录遵循架构约定，至少包含 `assets/`、`data/`、`scenes/`、`scripts/`、`docs/`

**Given** 首房间 shell 已加载
**When** 后续 stories 增加玩家移动、世界切换、种子和 UI
**Then** 当前场景结构能容纳 `Player`、`Objects`、`UI` 和后续 puzzle object 节点
**And** Story 1.1 不要求任何未来 story 才能成功启动和显示房间

### Story 1.2: 最小共享实现基础

As a 玩家,
I want 游戏的状态、反馈、提示和错误处理从一开始就采用一致基础,
So that 后续玩法不会因为临时 UI、音频、事件或日志方案而产生矛盾和返工。

**Acceptance Criteria:**

**Given** 开发者查看 Godot Autoload 配置
**When** 首房间 shell 项目初始化完成
**Then** 存在最小 `EventBus` 或等价全局事件入口，以及 `Log` 或等价结构化日志入口
**And** 事件入口至少预留 `world_state_changed`、`seed_collected`、`seed_planted`、`room_completed`、`restoration_applied`

**Given** 开发者查看 Godot 音频配置
**When** 首房间 shell 项目初始化完成
**Then** 至少存在 `Master`、`Music`、`Ambience`、`SFX` 和 `UI` audio buses
**And** `AudioManager` 或等价入口可被后续世界切换、对象反馈和设置菜单复用

**Given** 开发者查看 UI 基础资源
**When** 首房间 shell 项目初始化完成
**Then** 存在最小 Theme Resource、基础字体 / 颜色 / 间距 tokens 和可复用 UI 场景目录
**And** `Interaction Prompt`、`World State Indicator`、`Seed Companion Indicator`、`Gentle Hint Panel`、`Pause Menu`、`Settings Menu`、`Restoration Feedback` 至少有组件契约或占位场景路径

**Given** 后续 story 需要事件、日志、音频或 UI 组件
**When** 开发者实现该 story
**Then** 必须复用本 story 建立的共享入口和组件契约
**And** 不允许为单个 story 创建互不兼容的一次性 UI、音频、事件或日志方案

### Story 1.3: 小精灵基础移动与房间碰撞

As a 玩家,
I want 用键盘或手柄稳定移动小精灵,
So that 我能轻松探索首个花园房间而不被操作精度卡住。

**Acceptance Criteria:**

**Given** 首房间已经加载
**When** 玩家使用 WASD、方向键、左摇杆或十字键输入方向
**Then** 小精灵按输入方向以俯视角移动
**And** 移动支持慢速细微调整，不要求精准平台跳跃或像素级站位

**Given** 小精灵接近房间边界或不可通行边界
**When** 玩家继续向边界移动
**Then** 小精灵被轻柔阻挡且不会穿出房间
**And** 阻挡反馈不表现为惩罚、伤害或失败

**Given** 玩家从入口沿主通路移动
**When** 玩家保持移动输入
**Then** 小精灵能在 8 秒内穿过标准小房间主通路的基础距离
**And** 移动响应目标低于 100ms

**Given** 玩家使用键盘完成一轮移动测试
**When** 切换到手柄继续移动
**Then** 控制方式切换不会造成角色停止响应或焦点丢失
**And** 键盘和手柄均可独立完成房间探索基础动作

### Story 1.4: 核心输入动作映射

As a 玩家,
I want 游戏识别移动、切换、互动、重置和暂停这些核心动作,
So that 后续机制可以建立在一致、可预期的输入基础上。

**Acceptance Criteria:**

**Given** 开发者打开 Godot InputMap
**When** 查看输入动作配置
**Then** 存在移动、世界切换、互动 / 确认、重置房间、暂停 / 设置动作
**And** 每个动作至少包含键盘绑定，核心动作包含手柄绑定

**Given** 玩家按下尚未实现完整机制的世界切换、互动或重置输入
**When** 对应 gameplay 功能还未由后续 story 接管
**Then** 游戏使用安全占位响应或无害日志记录
**And** 不会崩溃、卡死、切换到无效状态或展示技术错误

**Given** 玩家使用暂停输入
**When** 暂停菜单尚未由 Epic 5 实现
**Then** 游戏保留该输入动作供后续 story 接管
**And** 当前 story 不依赖未来暂停 UI 才能完成

**Given** 主线体验只依赖移动、世界切换和互动三个动作
**When** 开发者新增输入动作
**Then** 新动作必须有明确用途说明
**And** 不得引入与当前核心循环无关的复杂操作要求

### Story 1.5: 首房间入口目标引导

As a 玩家,
I want 进入房间时看到目标方向和可探索线索,
So that 我知道下一步应该尝试靠近哪里。

**Acceptance Criteria:**

**Given** 玩家进入首房间入口区域
**When** 房间初始视角出现
**Then** 玩家能看到远处种子、断开的路径、出口花或关键对象方向中的至少一种目标线索
**And** 不需要常驻任务列表、地图或大段教学文字才能理解目标方向

**Given** 首房间使用 16:9、1080p 基准视口
**When** 玩家站在入口附近
**Then** 场景构图优先展示玩家、目标方向、关键通路和可探索区域
**And** HUD 默认最小化，不遮挡目标占位或玩家位置

**Given** Web demo 以 1280x720 窗口运行
**When** 玩家进入首房间
**Then** 目标线索仍然可见，UI 文本或提示不溢出屏幕
**And** 不因为窗口化而暴露调试 UI

**Given** 首房间后续会加入世界切换、种子和提示
**When** 当前 story 完成
**Then** 房间入口已经为这些机制预留可读构图位置
**And** 当前目标引导不依赖未来机制才能被玩家理解

## Epic 2: 可读的双世界路线变化

玩家能切换枯萎 / 盛放状态，并通过藤蔓桥、花门和关键对象反馈理解路线变化。

### Story 2.1: 受控的双世界状态机

As a 玩家,
I want 用单按钮在枯萎和盛放之间切换,
So that 我能通过世界状态变化理解新的路线可能性。

**Acceptance Criteria:**

**Given** 游戏处于首房间并已配置世界切换输入
**When** 玩家按下世界切换按钮
**Then** `WorldStateManager` 从 `WITHERED` 或 `BLOOM` 进入 `SWITCHING`
**And** 在 0.45-0.75 秒转场完成后提交到目标状态

**Given** 世界状态处于 `SWITCHING`
**When** 玩家重复按下世界切换按钮
**Then** 重复输入被锁定且不会排队触发额外切换
**And** 游戏不会进入无效状态或造成玩家失败

**Given** 世界状态发生变化
**When** 状态机开始、提交和结束切换
**Then** 系统发出类型清晰的状态信号供对象、音频、UI 和调试系统订阅
**And** gameplay 对象不直接拥有或覆盖全局世界状态

**Given** 开发者启用日志
**When** 世界切换开始和结束
**Then** 日志记录 from / to 状态与是否处于 switching
**And** 不向玩家显示原始技术日志

### Story 2.2: 统一的世界状态响应契约

As a 玩家,
I want 所有双世界对象用一致方式响应状态变化,
So that 我看到的画面、碰撞和互动结果不会互相矛盾。

**Acceptance Criteria:**

**Given** 开发者创建受世界状态影响的对象
**When** 对象需要响应枯萎 / 盛放
**Then** 对象实现 `WorldStateResponder` 或等价契约
**And** 该契约支持接收切换开始、状态提交和切换结束事件

**Given** 一个 responder 收到新世界状态
**When** 它应用状态
**Then** 它能统一更新视觉、碰撞、互动可用性、动画和可选音频反馈
**And** 不允许只改贴图而忽略碰撞或互动状态

**Given** responder 缺少可选动画、音频或视觉节点
**When** 它应用状态
**Then** 系统记录可恢复警告并使用安全 fallback
**And** 不破坏首房间主流程

**Given** 后续新增藤蔓桥、花门、出口花或提示对象
**When** 它们接入世界状态
**Then** 它们复用同一响应模式
**And** 避免每个对象实现互不兼容的一次性切换逻辑

### Story 2.3: 藤蔓桥双状态通行

As a 玩家,
I want 看见藤蔓桥在盛放时展开并可通行,
So that 我理解切换世界可以改变路线。

**Acceptance Criteria:**

**Given** 玩家处于枯萎状态并靠近藤蔓桥
**When** 玩家尝试通过藤蔓桥
**Then** 藤蔓桥呈现卷起、断裂或不可通行状态
**And** 碰撞阻挡玩家且不造成伤害、死亡或失败

**Given** 玩家切换到盛放状态
**When** 藤蔓桥收到状态变化
**Then** 藤蔓桥在 0.6-0.9 秒内展开并变为可通行
**And** 展开过程包含形状、轮廓、动画、发光或声音中的至少两种状态表达

**Given** 藤蔓桥完成盛放状态
**When** 玩家移动到桥上
**Then** 玩家可以稳定通过桥到达另一侧
**And** 视觉可通行状态与碰撞状态一致

**Given** 玩家在切换后 1 秒内观察场景
**When** 藤蔓桥是当前谜题关键对象
**Then** 藤蔓桥获得短暂强调
**And** 强调不会被全屏噪声变化淹没

### Story 2.4: 花门睡眠、唤醒与开启状态

As a 玩家,
I want 理解花门何时阻挡、何时苏醒、何时打开,
So that 我能判断路线是否已经被解锁。

**Acceptance Criteria:**

**Given** 花门处于睡眠状态
**When** 玩家靠近或尝试通过
**Then** 花门阻挡路线并显示沉睡或闭合表现
**And** 不使用错误警报或惩罚反馈

**Given** 花门收到正确世界状态或后续种子携带条件
**When** 花门被唤醒
**Then** 花瓣呼吸、门心亮起或开启音等反馈确认状态变化
**And** 状态差异不只依赖颜色

**Given** 花门进入开启状态
**When** 玩家移动通过花门位置
**Then** 碰撞和互动状态允许通行
**And** 视觉打开状态与实际通行结果一致

**Given** 花门暂时不可用
**When** 玩家互动
**Then** 花门提供温和不可用反馈
**And** 玩家能理解“现在还不行”而不是“失败了”

### Story 2.5: 世界切换可读反馈与轻量状态指示

As a 玩家,
I want 切换世界后立刻看懂当前状态和关键变化,
So that 我能用观察而不是试错推进谜题。

**Acceptance Criteria:**

**Given** 玩家首次在首房间触发世界切换
**When** 0.45-0.75 秒切换过渡完成
**Then** 与当前谜题相关的 1-2 个关键对象短暂高亮、动起来或发出确认音
**And** 玩家在 1 秒内能注意到至少一个有意义变化

**Given** 世界状态正在切换
**When** 状态指示器显示反馈
**Then** `World State Indicator` 进入 `switching` 状态
**And** 切换完成后短暂显示 `withered` 或 `bloom` 再淡出或缩小

**Given** 玩家依赖状态指示器确认世界状态
**When** 指示器显示枯萎或盛放
**Then** 指示器包含文本或形状差异
**And** 不只靠颜色表达状态

**Given** 玩家没有注意到切换结果
**When** 玩家继续观察当前房间
**Then** 当前关键对象仍保持可重新观察的可读状态
**And** Epic 2 不要求未来提示系统才能让世界切换功能成立

## Epic 3: 种子收集与首房间完成闭环

玩家能收集发光种子、看到种子跟随、带回出口花 / 种植点，并完成首房间目标。

### Story 3.1: 发光种子的接近与收集

As a 玩家,
I want 看到并收集发光种子,
So that 我理解它是当前房间的目标和修复对象。

**Acceptance Criteria:**

**Given** 玩家进入首房间并看到远处种子
**When** 玩家接近种子
**Then** 种子微光增强并显示短互动提示
**And** 提示文案短、具体，例如“收集”，不使用长段教程

**Given** 玩家使用触碰或互动输入收集种子
**When** 收集成功
**Then** 种子播放 0.3-0.5 秒短闪光和柔和音效
**And** 发出 `seed_collected(seed_id, room_id)` 事件或等价信号

**Given** 玩家靠近种子但当前不能收集
**When** 玩家尝试互动
**Then** 系统提供温和不可用反馈
**And** 不显示批评式或技术错误文案

**Given** `Interaction Prompt` 组件显示种子互动
**When** 玩家使用键盘或手柄
**Then** 提示包含按键名或输入图标和文本
**And** 不能只显示图标

### Story 3.2: 种子跟随与陪伴反馈

As a 玩家,
I want 收集后的种子以微光跟随我,
So that 我知道它还在身边并需要被带回去种下。

**Acceptance Criteria:**

**Given** 玩家成功收集种子
**When** 种子从房间目标转为携带状态
**Then** 种子不进入背包格或物品栏
**And** 它以跟随光点、微光轨迹和柔和运动表现为短暂同行对象

**Given** 玩家移动穿过房间
**When** 种子处于 following 状态
**Then** 种子持续跟随玩家且不会阻挡移动
**And** 玩家能通过位置、轨迹、声音或必要文字确认“种子还在”

**Given** 玩家靠近出口花或种植点
**When** 携带种子进入响应范围
**Then** `Seed Companion Indicator` 进入 `ready_to_plant` 或等价状态
**And** 种子反馈增强但不遮挡玩家或关键对象

**Given** 玩家已经携带一颗种子
**When** 玩家尝试再次收集同房间种子
**Then** 系统安全拒绝重复携带
**And** 记录可恢复日志或给出温和反馈，不破坏房间流程

### Story 3.3: 出口花与种植点携种响应

As a 玩家,
I want 携带种子时看到出口花或种植点响应,
So that 我知道应该把种子带到哪里。

**Acceptance Criteria:**

**Given** 玩家未携带种子并靠近出口花或种植点
**When** 玩家尝试互动
**Then** 出口花或种植点保持关闭、低亮或不可用状态
**And** 反馈应温和暗示还缺少种子

**Given** 玩家携带种子并靠近出口花或种植点
**When** 进入互动范围
**Then** 出口花或种植点主动变得更可读，例如点亮、呼吸或出现短提示
**And** 提示不会遮挡修复对象

**Given** 玩家携带种子并触发互动
**When** 出口花或种植点接受种子
**Then** 系统进入种植 / 修复流程
**And** 发出 `seed_planted(seed_id, garden_slot_id)` 或等价事件

**Given** 玩家不知道携带种子后去哪里
**When** 玩家在房间内停留或偏离路线
**Then** 花瓣路标、出口花低亮或光点方向可轻微指引目标方向
**And** 不显示完整解答式路线说明

### Story 3.4: 首房间完整完成闭环

As a 玩家,
I want 完成首房间从进入、观察、收集到带回种子的完整流程,
So that 我能体验到垂直切片的核心玩法承诺。

**Acceptance Criteria:**

**Given** 玩家从首房间入口开始
**When** 玩家观察目标、切换世界、通过关键路径、接近并收集种子
**Then** 玩家能带着跟随种子返回出口花或种植点
**And** 流程不需要敌人、死亡、硬倒计时、战斗或追逐压力

**Given** 玩家把当前房间种子带到出口花或种植点
**When** 种植或交付完成
**Then** 房间成功条件被满足
**And** 系统记录 `room_completed(room_id)` 或等价事件

**Given** 玩家在首房间中进行错误尝试
**When** 走错路、切错状态或与不可用对象互动
**Then** 玩家可以继续尝试或等待提示
**And** 进度不会被惩罚性清除

**Given** 首房间流程完成一次
**When** 开发者检查流程覆盖
**Then** 首房间包含小精灵移动、世界切换、藤蔓桥、花门、发光种子、出口花和种植反馈入口
**And** 后续中心花园恢复可以在 Epic 4 独立接管

## Epic 4: 中心花园修复与永久进度

玩家种下种子后，中心花园产生永久恢复变化，并理解后续方向或区域进展。

### Story 4.1: 种植仪式与修复反馈

As a 玩家,
I want 种下种子后看到明确的修复仪式,
So that 我感到自己真的让花园变好了。

**Acceptance Criteria:**

**Given** 玩家带着种子到达种植点
**When** 种植点接受种子并开始仪式
**Then** 种植点发光并播放 2-4 秒修复反馈
**And** 反馈包含颜色恢复、植物舒展、声音层增加或其他可感知变化

**Given** 种植仪式正在播放
**When** UI 显示完成确认
**Then** 确认文案极简，例如“这里重新发光了”
**And** 不使用大弹窗遮挡场景修复瞬间

**Given** 玩家开启减少闪烁设置
**When** 种植仪式播放
**Then** 粒子强度、屏幕波纹或高亮变化被降低到柔和水平
**And** 修复结果仍然清楚可见

**Given** 种植仪式完成
**When** 系统进入 completed 状态
**Then** 种子跟随表现结束并转为已种下状态
**And** 玩家能看见变化前后的空间差异

### Story 4.2: 中心花园永久恢复状态

As a 玩家,
I want 已种下的种子永久改变中心花园,
So that 我的进展不会因为重置房间而丢失。

**Acceptance Criteria:**

**Given** 种植成功并产生恢复事件
**When** `RestorationManager` 接收恢复 ID
**Then** 中心花园对应区域从沉睡、低亮或未盛放状态变为恢复状态
**And** 未恢复区域仍表现为可恢复空间，而不是“空内容”

**Given** 恢复标记已经应用
**When** 玩家重置当前房间或返回中心花园
**Then** 已恢复区域保持恢复状态
**And** 不因房间重置被清除

**Given** 恢复标记已经存在
**When** 同一恢复事件再次触发
**Then** 系统不会重复应用或破坏状态
**And** 可安全记录重复事件

**Given** 中心花园展示恢复状态
**When** 玩家观察恢复区域
**Then** 进度通过颜色、形状、植物状态、声音或路径变化表达
**And** 不只通过数值进度条表达恢复度

### Story 4.3: 种子驱动的进度与下一步方向

As a 玩家,
I want 种下种子后理解下一步可以去哪里,
So that 我愿意继续寻找下一颗种子或进入下一片区域。

**Acceptance Criteria:**

**Given** 玩家完成一次种植
**When** 中心花园恢复变化结束
**Then** 场景轻量暗示下一颗种子方向、下一房间入口或后续区域路径
**And** 暗示优先来自环境、光点、花瓣、声音或空间构图

**Given** 玩家停留在中心花园
**When** 已恢复节点可见
**Then** 玩家能区分房间内进展、房间完成和中心花园进展
**And** 不需要复杂任务列表理解已完成状态

**Given** 后续区域尚未实现
**When** 中心花园展示未来方向
**Then** 方向提示保持轻量和可扩展
**And** 不承诺当前垂直切片之外的多房间流程

**Given** 玩家完成垂直切片
**When** 游戏进入结束或回到中心花园
**Then** 玩家可以继续观察恢复结果、暂停或结束试玩
**And** 不被立即强制传送而错过修复反馈

### Story 4.4: 本地保存与恢复进度读取

As a 玩家,
I want 关闭并重新进入后保留已种下种子和花园恢复,
So that 我的修复进展是可信的。

**Acceptance Criteria:**

**Given** 玩家种下种子并产生恢复标记
**When** `SaveManager` 保存进度
**Then** 本地 JSON 存档包含 schema version、planted seed IDs、restoration flags、completed rooms 和 settings
**And** 只有 save/progression manager 直接读写存档文件

**Given** 玩家重新启动游戏
**When** 存档存在且版本有效
**Then** 游戏恢复已种下种子、中心花园恢复标记和已完成房间状态
**And** 不要求玩家重复完成已保存的恢复

**Given** 存档缺失或可恢复损坏
**When** 游戏加载进度
**Then** 系统记录警告并使用安全默认状态
**And** 不向玩家显示原始技术错误

**Given** 未来存档 schema 变化
**When** 游戏读取旧版本
**Then** SaveManager 能识别版本并保留迁移入口
**And** 当前垂直切片不需要实现 Steam Cloud 或复杂存档 UI

## Epic 5: 温和辅助、重置与设置体验

玩家卡住时能获得低压力提示，能重置当前房间，能通过暂停 / 设置管理体验。

### Story 5.1: 暂停菜单与安全返回

As a 玩家,
I want 随时暂停游戏并安全返回,
So that 我能以低压力节奏管理游玩。

**Acceptance Criteria:**

**Given** 玩家在首房间游玩
**When** 按下 Esc、Menu / Start 或等价暂停输入
**Then** 游戏显示暂停菜单
**And** gameplay 输入被冻结但当前世界状态和玩家位置被保留

**Given** 暂停菜单打开
**When** 玩家使用键盘、鼠标或手柄导航
**Then** 菜单以垂直结构展示继续、提示、重置房间、设置和退出
**And** 焦点状态清楚，鼠标 hover 不破坏当前手柄焦点

**Given** 玩家选择继续
**When** 暂停菜单关闭
**Then** gameplay 输入恢复
**And** 玩家回到暂停前的房间状态

**Given** 暂停菜单或 overlay 打开
**When** 玩家按返回键
**Then** UI 返回上一级或关闭到 gameplay
**And** 返回方式在键盘和手柄上保持一致

### Story 5.2: 房间重置与风险确认

As a 玩家,
I want 卡住时重置当前房间而不丢失永久进度,
So that 我可以安全地重新尝试。

**Acceptance Criteria:**

**Given** 玩家从暂停菜单选择重置房间
**When** 确认对话出现
**Then** 对话用一句话说明后果，例如“当前房间会回到入口，已种下的种子不会丢失。”
**And** 默认焦点落在取消或安全行动上

**Given** 玩家确认重置房间
**When** 重置执行
**Then** 当前房间谜题对象和玩家位置恢复初始状态
**And** 已种下的种子、中心花园恢复和已完成房间记录不被清除

**Given** 玩家取消重置
**When** 对话关闭
**Then** 游戏返回暂停菜单或 gameplay 前一状态
**And** 不改变房间或进度

**Given** 重置过程中发生可恢复错误
**When** 系统无法恢复某个非关键对象
**Then** 记录警告并使用安全 fallback
**And** 玩家不会看到原始技术错误或进入坏状态

### Story 5.3: 分层提示与温和轻推

As a 玩家,
I want 在看不懂时获得温和提示,
So that 我能恢复方向而不是被直接告知答案。

**Acceptance Criteria:**

**Given** 玩家进入房间
**When** 目标种子、出口花或关键对象存在
**Then** 系统可提供被动提示，例如微光、轻微动作、花瓣路标或声音方向
**And** 不显示大段教程文字

**Given** 玩家触发世界切换
**When** 当前谜题相关对象变化
**Then** 系统提供观察提示，短暂强调 1-2 个关键对象
**And** 提示不被全屏装饰性变化淹没

**Given** 玩家 45-60 秒无有效进展
**When** idle nudge 触发
**Then** 花瓣、种子微光或小精灵视线指向关键区域
**And** 先提示观察对象，不直接给操作答案

**Given** 玩家主动请求手动提示
**When** `Gentle Hint Panel` 显示
**Then** 面板显示一句观察方向和可选按键提示
**And** 文本可读，支持键盘 / 手柄关闭

### Story 5.4: 设置菜单与基础可访问性

As a 玩家,
I want 调整音量、显示和可访问性选项,
So that 我能以适合自己的方式游玩。

**Acceptance Criteria:**

**Given** 玩家从暂停菜单进入设置
**When** 设置菜单打开
**Then** 菜单包含主音量、音乐、音效、显示模式、提示强度、减少闪烁和 UI 缩放选项
**And** 设置项以标签 + 当前值 / 控件 + 可选说明的行结构呈现

**Given** 玩家调整 slider、toggle 或 segmented option
**When** 设置值有效
**Then** 设置即时生效
**And** 失败时恢复上一个有效值并记录可恢复警告

**Given** 玩家启用 UI 缩放
**When** 选择 100%、125% 或 150%
**Then** 菜单、提示和焦点环随 UI scale 放大
**And** 文本不溢出控件或屏幕安全边距

**Given** 玩家启用减少闪烁
**When** 世界切换、种子收集或种植反馈播放
**Then** 高频闪烁、粒子强度或屏幕波纹被降低
**And** 关键反馈仍能通过视觉或声音理解

### Story 5.5: 菜单焦点、确认对话与内容语气

As a 玩家,
I want 菜单和提示始终清楚、温和、可操作,
So that 我不会在 UI 中迷失或感觉被惩罚。

**Acceptance Criteria:**

**Given** 玩家使用键盘操作菜单
**When** 按方向键 / WASD、Enter 和 Esc
**Then** 焦点移动、确认和返回行为符合菜单导航规则
**And** 所有玩家可操作菜单项都有明确 focus state

**Given** 玩家使用手柄操作菜单
**When** 使用 D-pad / 左摇杆、A 和 B
**Then** 焦点移动、确认和返回行为与键盘一致
**And** 混合鼠标、键盘和手柄后焦点状态不丢失

**Given** 玩家触发退出试玩、重置房间或恢复默认设置
**When** 确认对话出现
**Then** 对话包含说明、安全行动、取消和危险确认
**And** 危险行动不使用刺眼红色，且默认焦点不落在危险行动上

**Given** UI 显示提示、错误或不可用反馈
**When** 玩家阅读文案
**Then** 文案短、具体、温和
**And** 避免命令式、批评式或系统化错误口吻

## Epic 6: 试玩可验证的表现、关卡框架与扩展准备

垂直切片具备最小资产、音频反馈、关卡类型框架、难度进展模型和 V1 扩展边界，支持试玩验证与后续内容生产。

### Story 6.1: 轻量 UI 设计系统验证与主题资源完善

As a 玩家,
I want 游戏 UI 与花园氛围一致且清晰可读,
So that UI 能辅助我行动而不抢走场景反馈。

**Acceptance Criteria:**

**Given** Story 1.2 已建立最小 UI 主题资源和组件契约
**When** 查看主题和 tokens
**Then** 字体层级、语义颜色、世界状态辅助色、8px 间距、尺寸、动效节奏和可访问性规则被补齐到可交付标准
**And** UI 继续使用 Godot `Control`、`CanvasLayer`、Theme Resource 和可复用场景实现

**Given** UI 需要表现种子、盛放、枯萎和普通文本
**When** 使用颜色 tokens
**Then** 包含 Seedlight `#F7D66A`、Bloom Green `#64B96A`、Petal Coral `#E9867A`、Clear Blue `#78B7D6`、Withered Green Gray `#7C8A77`、Deep Text `#24302A`、Soft Panel `#F4F1E8`
**And** 关键状态不只靠颜色表达

**Given** 游戏显示菜单或提示文本
**When** 使用字体层级
**Then** Menu Title、Section Title、Body / Menu Item、Hint Text 和 Debug Text 有明确字号范围
**And** 普通 UI 文本对比度目标参考 4.5:1

**Given** 新增或完善 UI 组件
**When** 开发者实现组件
**Then** 组件复用 Story 1.2 建立的主题资源、组件契约和 enum / state 字段
**And** 避免每个 UI 场景单独硬编码字体、颜色和间距

### Story 6.2: 垂直切片最低资产与导入规范

As a 玩家,
I want 首房间中的角色、对象和反馈有一致的视觉语言,
So that 我能看懂什么可通行、可互动、已完成或待恢复。

**Acceptance Criteria:**

**Given** 垂直切片资产清单
**When** 开发者检查项目资源
**Then** 至少存在小精灵、房间地块双状态、藤蔓桥、花门、发光种子、出口花、中心花园小块、世界切换涟漪、花瓣路标、微光轨迹和种植粒子的占位或正式资产
**And** 每类资产位于架构约定的 `assets/` 子目录中

**Given** 关键对象需要状态差异
**When** 设计枯萎、盛放、可互动、已完成和不可通行状态
**Then** 每个关键对象至少使用颜色以外的一种维度表达状态
**And** 视觉密度不遮挡路线、玩家或互动对象

**Given** 项目使用 AI 占位或概念素材
**When** 素材进入可玩切片
**Then** 素材经过统一调色、轮廓、动画节奏和导入规范检查
**And** 避免拼贴感影响核心可读性

**Given** 开发者新增场景、脚本、资源或动画
**When** 提交文件
**Then** 文件夹、文件、类名、函数、信号、资源和动画名称遵循架构命名约定
**And** 不把 gameplay 逻辑散落到资产目录中

### Story 6.3: 关键交互声音反馈完善

As a 玩家,
I want 听见世界状态和关键互动的差异,
So that 声音帮助我确认发生了什么。

**Acceptance Criteria:**

**Given** Story 1.2 已建立最小音频总线和 `AudioManager` 或等价入口
**When** 开发者查看 Audio Bus
**Then** `Master`、`Music`、`Ambience`、`SFX` 和 `UI` buses 路由完整
**And** 每类关键声音路由到合适 bus

**Given** 玩家在枯萎和盛放之间切换
**When** 世界状态变化
**Then** 枯萎 / 盛放环境音通过 AudioManager 或等价系统交叉淡入淡出
**And** 切换声音确认当前变化而不造成刺耳警报

**Given** 藤蔓桥、花门、种子收集或种植完成触发
**When** 对应事件发生
**Then** 播放对应 SFX 或占位声音
**And** 关闭音乐或降低音效后，关键反馈仍可通过视觉理解

**Given** 玩家调整主音量、音乐或音效设置
**When** 设置变化
**Then** 对应 bus 音量即时更新
**And** 设置值可被保存并在重新启动后恢复

### Story 6.4: 调试覆盖层与事件日志验证

As a 开发者,
I want 在试玩构建中观察关键状态而不影响玩家体验,
So that 我能快速验证世界切换、种子和恢复流程是否正确。

**Acceptance Criteria:**

**Given** 开发或测试构建启用 `debug_enabled`
**When** 开发者按调试热键
**Then** `Debug Overlay` 在 hidden、compact 和 expanded 状态之间切换
**And** 显示 FPS、world_state、is_switching、room_id、carried_seed_id 和 restoration_flags

**Given** 发布构建或默认玩家体验
**When** 游戏启动
**Then** 调试覆盖层默认隐藏
**And** gameplay 不依赖调试 UI 才能运行

**Given** Story 1.2 已建立最小事件和日志入口
**When** 开发者检查事件和日志实现
**Then** `EventBus` 或等价系统发布类型清晰的事件
**And** `Log` 或等价系统使用 `ERROR`、`WARN`、`INFO`、`DEBUG`、`TRACE` 等级

**Given** 跨系统事件发生
**When** 世界状态变化、种子收集、种子种下、房间完成或恢复应用
**Then** `EventBus` 或等价系统发布类型清晰的事件
**And** UI 或恢复系统通过事件 / manager 请求变化，不直接编辑 puzzle object 内部状态

**Given** 可恢复错误、关键错误或调试状态发生
**When** 系统记录日志
**Then** `Log` Autoload 或等价系统使用 `ERROR`、`WARN`、`INFO`、`DEBUG`、`TRACE` 等级
**And** 原始技术错误不直接展示给玩家

### Story 6.5: Web Demo、响应式尺寸与导出准备

As a 试玩玩家,
I want 在 PC 和桌面浏览器中稳定体验垂直切片,
So that 我可以顺畅理解首房间核心玩法。

**Acceptance Criteria:**

**Given** PC / Steam 目标构建
**When** 在 1920x1080 运行首房间
**Then** 游戏目标稳定 60 FPS
**And** 10 分钟核心循环试玩中不出现阻断核心流程的错误

**Given** Web demo 目标构建
**When** 在主流桌面浏览器运行
**Then** 主流设备目标 60 FPS，弱设备可接受 30 FPS 下限
**And** 首次可交互目标为普通宽带环境 30 秒内

**Given** Web demo 在 1280x720、1600x900、1920x1080 和 2560x1440 下测试
**When** 玩家游玩首房间
**Then** 目标、关键对象、互动提示、暂停菜单、设置菜单和修复反馈不溢出且不遮挡关键对象
**And** 窗口尺寸变化不会暴露调试 UI 或破坏焦点顺序

**Given** 项目需要导出 PC 和 Web
**When** 开发者查看导出配置
**Then** Godot export preset 或导出说明从垂直切片阶段开始维护
**And** 可选 GoPeak Godot MCP 和 Context7 MCP 设置仅作为开发支持文档，不成为运行时依赖

### Story 6.6: 关卡类型、难度模型与 V1 扩展边界

As a 开发团队,
I want 明确关卡类型、难度进展和 V1 扩展边界,
So that 垂直切片验证后可以稳定扩展内容。

**Acceptance Criteria:**

**Given** 关卡规划文档或数据资源
**When** 查看关卡类型
**Then** 支持中心花园、教学房间、主题机制房间、组合房间、恢复房间和可选房间的分类
**And** 每类房间有用途和内容规则说明

**Given** 难度进展模型
**When** 查看阶段定义
**Then** 包含教学、核心概念、强化、组合和可选挑战阶段
**And** 每阶段定义规则负载、目标解谜时长和设计目标

**Given** 前 3 个主线房间规划
**When** 检查谜题结构
**Then** 不要求玩家记忆屏幕外对象状态
**And** 主线房间必要操作链控制在 3-6 个关键步骤

**Given** V1 内容扩展规划
**When** 查看范围边界
**Then** 记录 4 个区域、16-24 个主线房间和 4 个区域恢复节点作为规划上限
**And** 明确该范围不是当前垂直切片承诺

**Given** V1 范围守卫
**When** 检查主线规划
**Then** 明确排除传统经济系统、完美步数挑战、每日谜题、程序生成主线关卡、排行榜和强制速通评价
**And** 任何重新引入这些系统的决定都必须经过正式范围变更

**Given** 可选重玩内容规划
**When** 查看扩展方向
**Then** 重玩价值来自回访已修复房间、查看前后环境变化、低压力明信片 / 种子图鉴片段和中心花园永久变化回看
**And** 不把可选重玩设计成阻挡主线或增加惩罚性压力的系统

### Story 6.7: 试玩验证与成功指标

As a 开发团队,
I want 用目标玩家试玩验证核心理解和修复回报,
So that 下一阶段优先级来自真实反馈而不是猜测。

**Acceptance Criteria:**

**Given** 垂直切片达到可试玩状态
**When** 组织试玩
**Then** 至少 5 名目标玩家完成首房间或达到记录点
**And** 记录他们是否看懂世界切换、是否知道种子跟随、是否感到修复回报

**Given** 试玩完成
**When** 汇总结果
**Then** 检查 80% 以上目标玩家是否能在 5 分钟内完成教学房间
**And** 检查 70% 以上玩家是否能描述“切换世界会改变路径或对象状态”

**Given** 玩家完成第一次种植
**When** 采集反馈
**Then** 检查 70% 以上玩家是否表达明确修复回报感
**And** 记录因看不懂关键对象而卡住的玩家比例是否低于 20%

**Given** 试玩反馈已整理
**When** 决定下一阶段工作
**Then** 反馈能明确指向视觉可读性、谜题结构、音频反馈、移动手感或恢复回报等优先级
**And** 不用排行榜、速通评分或惩罚性指标评估 cozy puzzle 主线体验
