# BAAH env checker

一个用于检查和修复环境来在各种各样的平台运行 [BAAH](https://github.com/sanmusen214/BAAH) 的辅助程序。

---

实现的内容有

 - 检查系统环境
 - 检查python环境
 - 针对python版本修复requeirements
 - 一行命令配置BAAH源码需要运行的环境

---

## 运行环境

任意python3

需要可以访问github的网络

## 目录详解

```
data\   #存储适配数据
        linux\   #Linux相关
                 linux_id_data.json  #linux发行版适配数据
        requeirements\   #修复使用的依赖列表
        arch.json   #指令集架构适配数据
checker.py    #主程序
```
