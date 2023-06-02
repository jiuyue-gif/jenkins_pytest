import allure,pytest



class TestSayHi(object):
    @pytest.mark.xfail(False, reason="")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.feature("成功打印文字模板")
    def test_success(self):
        print("hi, success!!!")
        assert 1

    @pytest.mark.xfail(True, reason="")
    @allure.feature("chagpt给的模板")
    def test_fail(self):
        with allure.step("Step 1"):
            assert 1 + 1 == 2
        with allure.step("Step 2"):
            assert 2 * 2 == 4


# if __name__ == "__main__":
#     pytest.main(["-s", "login.py"])

