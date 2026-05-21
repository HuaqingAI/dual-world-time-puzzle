# 微光花园 / Seedlight Garden - Development Epics

**Author:** Sue  
**Created:** 2026-05-19  
**Updated:** 2026-05-19  
**Source GDD:** `gdd.md`

---

## Epic Summary

| Epic | Name | Outcome | Priority |
| --- | --- | --- | --- |
| E1 | Player Movement and Room Shell | 小精灵能在一个清晰房间内移动、暂停、重置 | P0 |
| E2 | Dual-World Transformation | 玩家能切换枯萎 / 盛放并读懂状态变化 | P0 |
| E3 | First Puzzle Object Set | 藤蔓桥、花门、出口花构成首个可解房间 | P0 |
| E4 | Seed Collection and Garden Restoration | 玩家能收集种子、带回并触发中心花园修复 | P0 |
| E5 | Feedback, Art, and Audio Slice Polish | 核心动作有足够音画反馈支撑试玩 | P0 |
| E6 | Player Assistance and Playtest Readiness | 玩家卡住时有温和提示，团队能收集试玩判断 | P1 |
| E7 | V1 Content Expansion Planning | 垂直切片验证后有可扩展的区域和关卡计划 | P2 |

---

## Detailed Epics

### E1 - Player Movement and Room Shell

**Goal:** 玩家能控制小精灵进入一个小花园房间，并完成基础移动、暂停和重置。

**GDD Trace:** Game Mechanics / Controls and Input；Level Design Framework / Vertical Slice Room。

#### High-Level Stories

| Story | Player-Facing Outcome | Acceptance Criteria |
| --- | --- | --- |
| E1-S1 Basic Spirit Movement | 玩家能用键盘和手柄移动小精灵 | 小精灵可在房间主通路内移动；边界清楚；玩家能在 8 秒内穿过标准主通路 |
| E1-S2 Room Boundaries and Readability | 玩家能看懂哪些区域可走、哪些区域被挡住 | 可通行 / 不可通行区域有形状和视觉差异；不会只靠颜色区分 |
| E1-S3 Pause and Reset | 玩家能暂停、退出或重置当前房间 | 重置只恢复当前房间谜题，不清除已完成中心花园进度 |
| E1-S4 First Playable Flow Shell | 玩家能从开始状态进入房间并到达结束状态 | 有开始、房间、出口、结束四个可试玩状态 |

**Definition of Done:**

- 键盘和手柄均可完成移动、暂停和重置。
- 房间边界不依赖文字解释。
- 没有死亡、倒计时或惩罚性失败。

---

### E2 - Dual-World Transformation

**Goal:** 玩家能在枯萎 / 盛放之间切换，并在 1 秒内看出当前房间的关键变化。

**GDD Trace:** Core Gameplay / 清晰可读的双世界变化；Game Mechanics / 世界切换；Puzzle Game Specific Design / Core Puzzle Mechanics。

#### High-Level Stories

| Story | Player-Facing Outcome | Acceptance Criteria |
| --- | --- | --- |
| E2-S1 World Switch Action | 玩家按一个按钮切换世界状态 | 切换转场 0.45-0.75 秒；切换期间不会重复触发；玩家始终知道当前状态 |
| E2-S2 Withered and Bloom Visual Language | 玩家能区分枯萎和盛放 | 两个状态在颜色、形状、动画和声音上有明确差异 |
| E2-S3 Key Object Highlight | 玩家切换后能注意到相关对象变化 | 当前谜题相关的 1-2 个对象在切换后短暂高亮或动起来 |
| E2-S4 No-Load Continuity | 玩家感觉世界切换发生在同一空间内 | 切换没有加载屏；角色位置和房间关系保持连续 |

**Definition of Done:**

- 试玩者能描述“切换会改变路径或对象状态”。
- 关键变化不只靠颜色传达。
- 切换动作有视觉和音频确认。

---

### E3 - First Puzzle Object Set

**Goal:** 藤蔓桥、花门、发光种子和出口花组成第一间可解谜房间。

**GDD Trace:** Puzzle Game Specific Design / Puzzle Elements；Level Design Framework / Level Progression。

#### High-Level Stories

| Story | Player-Facing Outcome | Acceptance Criteria |
| --- | --- | --- |
| E3-S1 Vine Bridge Rule | 玩家通过切换世界让藤蔓桥展开 | 枯萎状态不可通行；盛放状态可通行；展开反馈 0.6-0.9 秒 |
| E3-S2 Flower Door Rule | 玩家理解花门会阻挡或放行路线 | 花门睡眠、唤醒、开启状态可读；开启后路线明确 |
| E3-S3 Exit Flower Rule | 玩家带种子后知道返回出口花 | 出口花在持有种子时变亮或打开；没有种子时状态不同 |
| E3-S4 First Room Composition | 玩家能完成一个完整房间谜题 | 入口看到目标或目标方向；必要操作链 3-6 步；完成时间目标 3-5 分钟 |

**Definition of Done:**

- 第一房间能独立试玩。
- 玩家能识别藤蔓桥、花门、种子、出口花的作用。
- 卡住时主要问题可归因为规则理解或视觉提示，而不是缺少内容。

---

### E4 - Seed Collection and Garden Restoration

**Goal:** 发光种子成为情感对象，玩家收集、带回、种下后看到中心花园恢复。

**GDD Trace:** Core Gameplay Loop；Game Mechanics / 发光种子、出口花 / 种植；Progression and Balance / Player Progression。

#### High-Level Stories

| Story | Player-Facing Outcome | Acceptance Criteria |
| --- | --- | --- |
| E4-S1 Visible Seed Goal | 玩家进入房间后知道要找种子 | 种子或目标方向在入口 3 秒内可见或被明确提示 |
| E4-S2 Seed Collection Feedback | 玩家收集种子时感到它是特殊对象 | 收集有 0.3-0.5 秒闪光和音效；种子随后以微光轨迹跟随 |
| E4-S3 Return With Seed | 玩家知道把种子带回哪里 | 出口花或种植点在持有种子时有明确反馈 |
| E4-S4 Planting Ritual | 玩家种下种子并看到恢复 | 种植仪式持续 2-4 秒；中心花园产生永久视觉或音频变化 |
| E4-S5 Progress Persistence | 玩家回到中心花园能看到已恢复内容 | 已种下的第一颗种子不会因房间重置消失 |

**Definition of Done:**

- 玩家能完整体验“找种子 -> 带回 -> 种下 -> 花园恢复”。
- 种子不表现为普通钥匙或背包物品。
- 试玩后玩家能描述修复回报。

---

### E5 - Feedback, Art, and Audio Slice Polish

**Goal:** 垂直切片拥有足够音画反馈，让玩家靠表现理解状态、交互和奖励。

**GDD Trace:** Core Gameplay / 表现反馈服务玩法；Art and Audio Direction。

#### High-Level Stories

| Story | Player-Facing Outcome | Acceptance Criteria |
| --- | --- | --- |
| E5-S1 Withered/Bloom Art Pass | 玩家第一眼能区分两个世界 | 两套状态在色彩、轮廓、运动和密度上不同；不阴森、不混乱 |
| E5-S2 Core Object Animation Pass | 玩家看得懂桥、门、种子、出口花变化 | 每个核心对象有至少 2 个状态和对应动画 |
| E5-S3 World Switch Audio Layer | 玩家听得见世界变化 | 枯萎 / 盛放环境层不同；切换时有过渡音 |
| E5-S4 Planting Reward Polish | 玩家种下种子后获得明确回报 | 恢复反馈包含画面、声音、运动和中心花园变化 |
| E5-S5 Accessibility Readability Pass | 玩家不依赖颜色也能理解关键对象 | 关键对象同时使用形状、轮廓、动画或发光状态 |

**Definition of Done:**

- 世界切换、藤蔓桥、花门、种子、种植这五个瞬间都可被短视频或 GIF 清楚展示。
- 音频不是后期占位，至少能承担状态提示和完成确认。
- 视觉噪声不遮挡路线和交互对象。

---

### E6 - Player Assistance and Playtest Readiness

**Goal:** 垂直切片可以交给外部玩家试玩，并收集核心体验是否成立的证据。

**GDD Trace:** Puzzle Game Specific Design / Player Assistance；Success Metrics。

#### High-Level Stories

| Story | Player-Facing Outcome | Acceptance Criteria |
| --- | --- | --- |
| E6-S1 Passive Cues | 玩家不用读教程也能注意目标 | 种子、出口花、关键对象有低干扰提示 |
| E6-S2 Idle Nudge | 玩家长时间无进展时得到温和方向提示 | 45-60 秒无有效进展后出现花瓣、微光或视线提示 |
| E6-S3 Manual Hint | 玩家主动请求时获得分层提示 | 提示先指观察方向，再指操作顺序，不直接抢走发现感 |
| E6-S4 Playtest Build | 外部玩家能独立完成试玩流程 | 有开始、完整房间、结束反馈；无需开发者旁白 |
| E6-S5 Playtest Questions | 团队能判断下一步优先级 | 收集理解度、完成时间、卡点、修复回报和视觉 hook 反馈 |

**Definition of Done:**

- 至少 5 名目标玩家完成试玩或暴露明确卡点。
- 有记录完成时间、提示使用、卡点位置和主观回报感的方法。
- 试玩问题直接对应 GDD 成功指标。

---

### E7 - V1 Content Expansion Planning

**Goal:** 垂直切片验证后，扩展到 v1 内容时仍保持“一房间一个小魔法”和低压力解谜边界。

**GDD Trace:** Progression and Balance；Level Design Framework；Out of Scope。

#### High-Level Stories

| Story | Player-Facing Outcome | Acceptance Criteria |
| --- | --- | --- |
| E7-S1 Area Motif Plan | 玩家在每个区域遇到一个新主题规则 | 4 个候选区域各有主题、主机制和恢复回报 |
| E7-S2 Level Difficulty Map | 玩家体验到平滑难度曲线 | 教学、强化、组合、可选挑战分层明确 |
| E7-S3 Content Budget | 团队知道 v1 内容上限 | 16-24 个主线房间作为规划上限，不在切片阶段承诺 |
| E7-S4 Scope Guardrails | 团队避免把游戏扩成管理或冒险大作 | Out of Scope 在生产计划中可执行 |

**Definition of Done:**

- 扩展计划不改变核心循环。
- 每个新增机制都能追溯到支柱、循环和玩家回报。
- 未经垂直切片验证，不进入大规模内容生产。
