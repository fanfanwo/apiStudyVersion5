'''
cookies 鉴权
cookies 需要先从登录接口返回值中 提取 --self.respond.cookies  --将cookies变量设置在外部类参数中  setattr(Argument,"cookies",self.respond.cookies)
提取完cookies后 将cookies更新到 请求数据中  --self.d = {"cookies": self.__argument["cookies"]}
然后发送请求
'''