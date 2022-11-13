'''
输出测试报告
main.py [options] [file_or_dir] [file_or_dir] [...]

编写测试用例
执行测试用例
生成测试报告
生成测试总结
'''
import pytest

pytest.main(["--html=report/report.html","--self-contained-html",])