# Events 爬虫工具

## 快速开始

```bash
# 安装依赖
pip install requests beautifulsoup4

# 运行爬虫
python meetup.py      # 爬取 Meetup 活动
python allevents.py   # 爬取 AllEvents 活动
python eventsbrite.py # 爬取 Eventbrite 活动
```

## 使用方式

### 1. Meetup 爬虫
```python
from meetup import fetch_events, parse_events

# 获取原始数据
raw_data = fetch_events()

# 解析为结构化数据
events = parse_events(raw_data)
print(f"获取到 {len(events)} 个活动")
```

### 2. AllEvents 爬虫
```python
from allevents import fetch_events, parse_events

# 获取并解析活动
raw_data = fetch_events()
events = parse_events(raw_data)
```

### 3. Eventbrite 爬虫
```python
from eventsbrite import fetch_events, parse_events

# 获取并解析活动
raw_data = fetch_events()
events = parse_events(raw_data)
```

## 输出数据格式

每个活动包含以下字段：
- **基本信息**: 活动ID、标题、时间、地点、描述
- **详细信息**: 主办方、类别、标签、票价信息
- **媒体资源**: 图片URL、活动链接
- **参与数据**: 参与人数、评分、关注度

---

## 网站基本信息

| 网站名称 | 简介与规模 | 主要特色 | 典型用户群体 | 适合爬取的数据类型 |
|-----------|-------------|-------------|----------------|--------------------|
| **Eventbrite** | 成立于 2006 年，总部位于旧金山。是全球最大的活动票务与组织平台之一，每年举办超过 450 万场活动，覆盖 180+ 国家。 | - 专注大型活动与商业票务（会议、展览、音乐节）<br>- 官方 API 较完善，活动信息结构化良好<br>- 提供城市、类别、日期等搜索筛选功能 | 活动主办方、企业活动经理、音乐节组织者、普通消费者 | 标题、时间、地点、票价、主办方、活动类别、报名人数、描述 |
| **Meetup** | 创建于 2002 年，被 WeWork 收购后重新独立。全球拥有超过 5,000 万用户，每月活跃组织超 10 万场本地活动。 | - 强调"基于兴趣的线下社群"<br>- 涵盖技术聚会、语言交换、徒步、文化活动等<br>- 活动以社群形式组织，可爬取群组信息 | 技术爱好者、外语学习者、社区组织者、城市新居民 | 群组名、活动名、时间、地点、参与人数、类别、活动描述 |
| **AllEvents.in** | 成立于印度但在美国使用广泛，聚合了全球 60,000+ 城市的活动数据，是一个活动信息聚合平台。 | - 聚合型平台，来源包括本地场馆、社交媒体、Eventbrite 等<br>- 分类丰富（音乐、文化、美食、节庆、学术）<br>- 界面简洁，信息字段较统一 | 城市居民、学生、文化活动参与者、活动推广者 | 活动标题、类别、地点、日期、门票链接、组织者、标签 |