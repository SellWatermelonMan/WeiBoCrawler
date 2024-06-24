## 介绍

该项目用来爬取 微博平台 数据

## 环境

- python>=3.8
- pandas>=2.0.3
- parsel>=1.9.1
- Requests>=2.32.3
- rich>=13.7.1

## 功能

### 获取主题内容

```python
q = "#姜萍中考621分却上中专的原因#"  # 话题
kind = "综合"  # 综合，实时，热门，高级
cookie = "" # 输入cookie
wbparser = WBParser(cookie)
wbparser.get_main_body(q, kind)
```

### 获取一级评论

```python
q = "#姜萍中考621分却上中专的原因#"  # 话题
kind = "综合"  # 综合，实时，热门，高级
cookie = "" # 输入cookie
wbparser = WBParser(cookie)
wbparser.get_comments_level_one()
```

### 获取二级评论

```python
q = "#姜萍中考621分却上中专的原因#"  # 话题
kind = "综合"  # 综合，实时，热门，高级
cookie = "" # 输入cookie
wbparser = WBParser(cookie)
wbparser.get_comments_level_two()
```

## 使用

### 安装依赖

```python
pip install -r requirements.txt
```

### 设置

#### 话题

话题需要用两个 `##` 间隔，例子如下

\#姜萍中考621分却上中专的原因\#

#### 类型

类型有 综合，实时，热门，高级 四种方式，对应微博的四种检索方式

#### cookie

cookie 的 获取方式如下

![获取cookie](./Pic/1.png#pic_center)


### 运行

```python
python main.py
```


