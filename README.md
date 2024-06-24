## 介绍

该项目用来爬取 微博平台 数据

## 环境

- python>=3.8
- pandas>=2.0.3
- parsel>=1.9.1
- Requests>=2.32.3
- rich>=13.7.1


## 使用

### 安装依赖

```python
pip install -r requirements.txt
```

### 设置 话题，类型，cookie

cookie 的 获取方式如下



```python
q = "#姜萍中考621分却上中专的原因#"  # 话题
kind = "综合"  # 综合，实时，热门，高级
cookie = "" 
```


### 运行

```python
python main.py
```
### 效果

![效果](./Pic/1.png#pic_center)
