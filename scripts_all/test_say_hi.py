import allure,pytest


class TestSayHi(object):
    @pytest.mark.xfail(False, reason="")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step(title="成功打印文字")
    def test_success(self):
        print("hi, success!!!")
        assert 1

    @pytest.mark.xfail(True, reason="")
    @allure.step(title="断言失败--打印文字")
    def test_fail(self):
        print("hi, fail!!!")
        assert 0


# if __name__ == "__main__":
#     pytest.main(["-s", "login.py"])

