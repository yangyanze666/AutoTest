##项目介绍
目前搭建的自动化框架，是基于Python语言，对python的request库进行了二次封装，使用pytest作为测试用例管理，pytest-html作为测试报告的框架结构。
能够支持简单的单元测试和复杂的功能测试，支持数据驱动，执行测试过程中可以将某些测试跳过，或者对某些预期失败的case标记成失败，支持重复执行失败的case，
具有很多第三方插件，并且可以自定义扩展，方便进行持续集成。 目前已经实现yaml和excel的数据驱动，后续会在Jenkins进行部署实现持续集成。同时对测试报告也实现了汉化和自定义，在原有的基础上添加了测试用例名称，进一步优化了展示效果。



## 项目部署

首先，下载项目源码后，在根目录下找到 ```requirements.txt``` 文件，然后通过 pip 工具安装 requirements.txt 依赖，执行命令：

```
pip install -i http://mirrors.paic.com.cn/pypi/web/simple   --trusted-host   mirrors.paic.com.cn -r requirements.txt
```



## 项目结构



- config ====>> 配置文件
- data ====>> 测试数据文件管理
- lib ====>> 框架的核心代码 
  api ====>> 接口封装层，如封装HTTP接口为Python接口 
  common ====>> 各种工具类 
  core ====>> requests请求方法封装、关键字返回结果类 
  operation ====>> 关键字封装层，如把多个Python接口封装为关键字
- log ====>> 打印用例执行过程
- report ====>> 测试报告
- testcases ====>> 测试用例
- pytest.ini ====>> pytest配置文件
- requirements.txt ====>> 相关依赖包文件
- runner ====>> 组织维护测试用例的套件



