'''
request的参数传递： cookies tooken
cookies 只有web中有
从上一个参数 提取cookie   --提取之后放到公共参数中--也就是外部类中
提取cookies
要知道cookie的位置  -- r.respond.cookies
然后存储到外部类 变量中 setattr(Argument ,"cookies",self.respond.cookies)

添加cookies
cookies的参数  传递给request
self.d = {"cookies": self.__argument["cookies"]}  --self.d是请求数据

第二个接口运行 时，r.run() 中的请求数据 需要拿到 cookies值  self.d 用update

'''