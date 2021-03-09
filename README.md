# 赞助商排在最顶上！！！！！！！！！

## 蓝星灯塔科技

![./imgs/logo_tr_title.png](./imgs/logo_tr_title.png)

## CACode 开发团队

![./imgs/icon_dev.png](./imgs/icon_dev.png)

# 适用于 flask 的 ORM 框架

## pip命令：pip install CACodeFramework

## 先放几个运行图保命🤡

#### 单线程跑 1000 条数据,没开线程所以慢,各位使用的时候跑跑 threading

### insert:

![./imgs/insert.gif](./imgs/insert.gif)

### delete:

![./imgs/delete.gif](./imgs/delete.gif)

### update:

![./imgs/update.gif](./imgs/update.gif)

### select:

![./imgs/select.gif](./imgs/select.gif)

# 我先说点废话:😜

- 你们就当我在放屁
    - 这是第一个版本，所以效率嘛~~~，😜
        - 15 秒 1000 条插入
        - 0.02 秒 1000 条查询
        - 0.03 秒 1000 条更新
        - 0.03 秒 1000 条删除
    - bug 的话我这边暂时没找到，如果你在哪找到了尽快告诉我，我给你寄礼物😜
        - 这是真送礼物，有手办，键盘。鼠标之类的
        - 如果你愿意的话，我可以给你我的亲笔签名哈哈哈哈哈
    - 别骂我，第一次写 python 的框架😜
        - 嫌弃我写的不好你就别用，要用你自己写去
        - 骂我我会伤心，但是过两天我就当你死了
        - 我家里有一本民法典
        - 我有朋友做律师和法官
    - 接受捐献但希望捐献是因为觉得这个框架好用而不是因为我的帅气😜
        - 我不缺钱
        - 你们的钱不够我塞牙缝

# 使用指北:

#### 先去看 test,里面有一个 【test.py】 文件,请先粗略浏览一遍该文件再继续查看教程

    🐶 狗头保命,import全局

    from CACodeFramework.MainWork import CACodeRepository, CACodePojo
    from CACodeFramework.MainWork.Annotations import Table
    from CACodeFramework.util import Config

#### 第一步，你需要一个全局的 config 类，并让其继承【Config.config】

    class ConF(Config.config):
        def __init__(self, host='localhost', port=3306, database='demo', user='root', password='123456', charset='utf8'):
            super(ConF, self).__init__(host, port, database, user, password, charset)

##### 当然你也可以加以改造

    class ConF(Config.config):
    def __init__(self, host='localhost', port=3306, database='demo', user='root', password='123456', charset='utf8'):
        configs = {
            "IMG_SUFFIX": 'bmp jpg png tif gif pcx tga exif fpx svg psd cdr pcd dxf ufo eps ai raw WMF webp avif',
            "SAVE_PATH": os.sep + 'tickets' + os.sep + 'img'
        }
        super(ConF, self).__init__(host, port, database, user, password, charset, conf=configs)

##### 像这样加上你的自定义配置，然后放到你喜欢的 package 下面就可以当全局变量使用了。我放了好几个方法在那里，源码在这，感觉还能再改：

    from CACodeFramework.util import JsonUtil
    
    
    class config(object):
        """
        配置类:
            默认必须携带操作数据库所需的参数:
                - host:数据库地址
                - port:端口
                - database:数据库名
                - user:用户名
                - password:密码
                - charset:编码默认utf8
                - conf:其他配置
        """
    
        def __init__(self, host, port, database, user, password, charset='utf8', conf=None):
            """
            必须要有的参数
            :param host:数据库地址
            :param port:端口
            :param database:数据库名
            :param user:用户名
            :param password:密码
            :param charset:编码默认utf8
            :param conf:其他配置
            """
            if conf is None:
                conf = {}
            self.conf = conf
            self.host = host
            self.port = port
            self.database = database
            self.user = user
            self.password = password
            self.charset = charset
    
        def get(self):
            """
            获取当前配置类
            :return:
            """
            return self
    
        def set_field(self, key, value):
            """
            设置字段
            :param key:键
            :param value:值
            :return:
            """
            self.conf[key] = value
            return config
    
        def get_field(self, name):
            """
            获取字段
            :param name:
            :return:
            """
            _this = self.get_dict()
            return _this[name]
    
        def get_dict(self):
            """
            将配置类转转字典
            :return:
            """
            return self.__dict__
    
        def get_json(self):
            """
            将配置类转json
            :return:
            """
            return JsonUtil.parse(self.get_dict())

#### 第二步，你需要一个 POJO 类，并让其继承 【CACodePojo.POJO】

        class Demo(CACodePojo.POJO):
            def __init__(self):
                #这里必须在这设置表的字段名，全部赋值为 None 就行了
                self.index = None
                self.title = None
                self.selects = None
                self.success = None

#### 第三步，好你已经成功一大半了👏👏，接下来就是要设置一个Repository，并通过这个资源库操作数据库

    # 加入这个注解，name是表示你所操作的表名，msg是你要告诉后人这个表是什么玩意，不然别人接手你的坑就看不懂了😎
    @Table(name="demo_table", msg="demo message")
    # 这里继承了【CACodeRepository.Repository】类来操作数据库
    class TestClass(CACodeRepository.Repository):
        def __init__(self):
            # 使用父类初始化这个资源库，并将之前设置好的全局配置导入进来放进去
            # 记得一定要加括号(),因为我要的是你的对象🤷‍♂️🤷‍♂️
            # participants是要参考解析的对象，也就是咱们之前创建的POJO类
            # 这里一样要加括号()
            super(TestClass, self).__init__(config_obj=ConF(), participants=Demo())

##### 最后一小步了！！！！！✌了解各个方法的使用

###### 首先是 find_all(),这个应该不用说了吧，看名识作用👏

###### 然后就是 find_by_field(*args):

    这个方法是按照字段来查询，比如说你可能不需要其他多余的数据，比如账号密码啥的你就可以不要了，多豪气看他不爽就给他踢掉
    attributes：我生来肯定是有作用的，比如拖一下程序的运行
    我：希望人出事🙏🙏
    他返回的数据长这样：

![./imgs/find_by_field.jpg](./imgs/find_by_field.jpg)

    其他字段你不想要就可以不要，这里我选查的index和title两个字段
    数据返回的是list[POJO]类型，也就是你初始化Repository那会设置participants的类型，如果不是继承自【CACodePojo.POJO】就不能进行操作哦

###### 到了动手的时候了 find_many(sql):💪💪

    手动输入sql语句查询

![./imgs/find_many.jpg](./imgs/find_many.jpg)

    注意！！！查找非当前POJO存在的字段时，尽量使用 as 改个名字
    因为我着急用，所以上线的比较匆忙😆

![./imgs/find_many_2.png](./imgs/find_many_2.png)

###### 插入一条 insert_one(sql):

    可以处理insert操作,将现成已有数据的POJO插入到数据库
    返回受影响行数

###### 插入多条 insert_many(sql):

    调用insert_one(sql)插入多条

###### 更新操作 updates(sql):

    由于删除也是更新操作，所以这里就没有多写一个delete(sql)了

## 好了，教程到这就结束了，我也懒得写了

## 再来一波赞助商的大LOGO

my wechat: cacode

## 蓝星灯塔科技

![./imgs/logo_tr_title.png](./imgs/logo_tr_title.png)

## CACode 开发团队

![./imgs/icon_dev.png](./imgs/icon_dev.png)