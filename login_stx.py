import logging
import var_stx
import time
from selenium.webdriver.common.by import By
from retry import retry
import module_other_stx
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException













class login:

    # def login_stx(self, user, password):
    #     var_stx.driver.implicitly_wait(5)
    #     var_stx.driver.maximize_window()
    #     var_stx.driver.delete_all_cookies()
    #     try:
    #         var_stx.driver.implicitly_wait(1)
    #         login.logout_stx(self)
    #         time.sleep(1)
    #     except:
    #         pass
    #     var_stx.driver.set_page_load_timeout(10)
    #     var_stx.driver.get(var_stx.linktest)
    #     time.sleep(5)
    #     try:
    #         var_stx.driver.implicitly_wait(1)
    #         login.logout_stx(self)
    #         time.sleep(1)
    #     except:
    #         pass
    #     var_stx.driver.find_element(By.XPATH, var_stx.login_user).clear()
    #     time.sleep(0.5)
    #     var_stx.driver.find_element(By.XPATH, var_stx.login_user).send_keys(user)
    #     var_stx.driver.find_element(By.XPATH, var_stx.login_password).clear()
    #     time.sleep(0.5)
    #     var_stx.driver.find_element(By.XPATH, var_stx.login_password).send_keys(password)
    #     var_stx.driver.find_element(By.XPATH, var_stx.dangnhap).click()
    #     time.sleep(10)
    #     try:
    #         wait = WebDriverWait(var_stx.driver, 35)
    #         element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.minitor)))
    #         time.sleep(2)
    #     except:
    #         pass

    def login_stx(self, user, password):
        try:
            var_stx.driver.implicitly_wait(5)
            var_stx.driver.maximize_window()
            var_stx.driver.delete_all_cookies()

            try:
                login.logout_stx(self)
            except NoSuchElementException:
                pass

            var_stx.driver.set_page_load_timeout(10)
            var_stx.driver.get(var_stx.linktest)
            time.sleep(5)
            try:
                login.logout_stx(self)
            except NoSuchElementException:
                pass

            WebDriverWait(var_stx.driver, 10).until(EC.presence_of_element_located((By.XPATH, var_stx.login_user)))
            time.sleep(2)

            username_field = var_stx.driver.find_element(By.XPATH, var_stx.login_user)
            password_field = var_stx.driver.find_element(By.XPATH, var_stx.login_password)

            username_field.clear()
            time.sleep(0.5)
            username_field.send_keys(user)
            time.sleep(0.5)
            password_field.clear()
            time.sleep(0.5)
            password_field.send_keys(password)
            time.sleep(0.5)

            login_button = var_stx.driver.find_element(By.XPATH, var_stx.dangnhap)
            login_button.click()

            WebDriverWait(var_stx.driver, 35).until(EC.element_to_be_clickable((By.XPATH, var_stx.minitor)))
            time.sleep(2)
        except TimeoutException as e:
            print(f"Lỗi: Quá thời gian chờ cho một phần tử - {e}")
        except Exception as e:
            print(f"Lỗi không mong đợi: {e}")




    def login_stx2(self, user, password):
        var_stx.driver.implicitly_wait(5)
        var_stx.driver.maximize_window()
        var_stx.driver.delete_all_cookies()
        try:
            login.logout_stx(self)
            time.sleep(1)
        except:
            pass
        var_stx.driver.set_page_load_timeout(10)
        var_stx.driver.get(var_stx.data['login']['g7'])
        time.sleep(5)
        try:
            login.logout_stx(self)
            time.sleep(1)
        except:
            pass
        var_stx.driver.find_element(By.XPATH, var_stx.login_user).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.login_user).send_keys(user)
        var_stx.driver.find_element(By.XPATH, var_stx.login_password).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.login_password).send_keys(password)
        var_stx.driver.find_element(By.XPATH, var_stx.dangnhap).click()
        time.sleep(10)
        wait = WebDriverWait(var_stx.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.minitor)))
        time.sleep(2)



    def login_stx_g7test(self, user, password):
        var_stx.driver.implicitly_wait(5)
        var_stx.driver.maximize_window()
        var_stx.driver.delete_all_cookies()
        try:
            login.logout_stx(self)
            time.sleep(1)
        except:
            pass
        var_stx.driver.set_page_load_timeout(10)
        var_stx.driver.get(var_stx.data['login']['g7_test'])
        time.sleep(5)
        try:
            login.logout_stx(self)
            time.sleep(1)
        except:
            pass

        var_stx.driver.find_element(By.XPATH, var_stx.login_user).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.login_user).send_keys(user)
        var_stx.driver.find_element(By.XPATH, var_stx.login_password).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.login_password).send_keys(password)
        var_stx.driver.find_element(By.XPATH, var_stx.dangnhap).click()
        time.sleep(2)
        wait = WebDriverWait(var_stx.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.STAXI)))
        time.sleep(2)



    @retry(tries=2, delay=2, backoff=1, jitter=5)
    def login_stx_taxi123(self, user, password):
        var_stx.driver.implicitly_wait(5)
        var_stx.driver.maximize_window()
        var_stx.driver.delete_all_cookies()
        try:
            login.logout_stx(self)
            time.sleep(1)
        except:
            pass

        var_stx.driver.set_page_load_timeout(10)
        var_stx.driver.get(var_stx.data['login']['taxi123'])
        time.sleep(5)
        try:
            login.logout_stx(self)
            time.sleep(1)
        except:
            pass
        var_stx.driver.find_element(By.XPATH, var_stx.login_user).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.login_user).send_keys(user)
        var_stx.driver.find_element(By.XPATH, var_stx.login_password).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.login_password).send_keys(password)
        var_stx.driver.find_element(By.XPATH, var_stx.dangnhap).click()
        time.sleep(2)
        wait = WebDriverWait(var_stx.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.STAXI)))
        time.sleep(2)



    def login_stx_company(self, user, password):
        var_stx.driver.implicitly_wait(5)
        var_stx.driver.maximize_window()
        var_stx.driver.delete_all_cookies()
        try:
            login.logout_stx(self)
            time.sleep(1)
        except:
            pass

        var_stx.driver.set_page_load_timeout(10)
        var_stx.driver.get(var_stx.data['login']['company'])
        time.sleep(5)
        try:
            login.logout_stx(self)
            time.sleep(1)
        except:
            pass

        var_stx.driver.find_element(By.XPATH, var_stx.login_user).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.login_user).send_keys(user)
        var_stx.driver.find_element(By.XPATH, var_stx.login_password).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.login_password).send_keys(password)
        var_stx.driver.find_element(By.XPATH, var_stx.dangnhap).click()
        time.sleep(10)



    def logout_stx(self):
        var_stx.driver.implicitly_wait(1)
        var_stx.driver.find_element(By.XPATH, var_stx.profile).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.icon_logout).click()
        time.sleep(2)



    def login_stx1(self, code, eventname, result, link, path_check, desire, path_image, user, password):
        var_stx.driver.implicitly_wait(5)
        var_stx.driver.maximize_window()
        var_stx.driver.delete_all_cookies()
        try:
            var_stx.driver.implicitly_wait(1)
            login.logout_stx(self)
        except:
            pass

        var_stx.driver.set_page_load_timeout(10)
        var_stx.driver.get(link)
        time.sleep(5)
        try:
            var_stx.driver.implicitly_wait(1)
            login.logout_stx(self)
        except:
            pass

        var_stx.driver.find_element(By.XPATH, var_stx.login_user).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.login_user).send_keys(user)
        var_stx.driver.find_element(By.XPATH, var_stx.login_password).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.login_password).send_keys(password)
        var_stx.driver.find_element(By.XPATH, var_stx.dangnhap).click()
        time.sleep(4)
        module_other_stx.write_result_text_try_if(code, eventname, result, "Login",
                                              path_check, desire, path_image)





class link:



    def affiliate(self, code, event, result, link, path_check, desire, name_image, type):
        var_stx.driver.implicitly_wait(5)
        var_stx.driver.get(var_stx.linktest)
        time.sleep(3)
        # var_v3.driver.find_element(By.XPATH, link).click()
        button = var_stx.driver.find_element(By.XPATH, link)
        var_stx.driver.execute_script("arguments[0].click();", button)
        time.sleep(3)
        print("n1")
        if type == "0":
            print("n2")
            try:
                wait = WebDriverWait(var_stx.driver, 7)
                element = wait.until(EC.element_to_be_clickable((By.XPATH, path_check)))
            except:
                pass
            print("n3")
            module_other_stx.write_result_text_try_if(code, event, result, "Đăng nhập - Liên kết",
                                                  path_check, desire, name_image)
            print("n4")

        if type == "1":
            print("n5")
            time.sleep(1)
            module_other_stx.write_result_text_try_if_title(code, event, result, "Đăng nhập - Liên kết",
                                                     desire, name_image)
            print("n6")

        # var_stx.driver.get(var_stx.linktest)
        # time.sleep(3)










































