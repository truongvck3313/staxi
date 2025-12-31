import logging
import var_stx
import time
from selenium.webdriver.common.by import By
import module_other_stx
import login_stx
import minitor_stx
import report_stx
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import openpyxl
from retry import retry
from seleniumwire.utils import decode as sw_decode
from selenium.webdriver.common.keys import Keys
wait = WebDriverWait(var_stx.driver, 10)

#19/12
class list_wallet_driver:

    def list_wallet_driver_x(self):
        var_stx.driver.implicitly_wait(0.3)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.name_driver).clear()
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.account).clear()
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.number).clear()
            time.sleep(0.3)
        except:
            pass


    def list_wallet_driver(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.driver_wallet).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.list_wallet_driver).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.driver_wallet).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.list_wallet_driver).click()
        time.sleep(2)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.title_page)))
            time.sleep(2)
        except:
            pass
        module_other_stx.write_result_text_try_if(code, eventname, result, "VÍ LÁI XE - 3.1 Danh sách ví lái xe",
                                                  var_stx.title_page, "3.1 Danh sách ví lái xe", "_DanhSachViLaiXe.png")


    def list_wallet_driver_7g_test(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx_g7test(self, var_stx.data['login']['tk_admin_test'],  var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.driver_wallet).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.list_wallet_driver).click()
        time.sleep(2.5)


    def list_wallet_driver_toolbar(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_wallet_driver)
        except:
            list_wallet_driver.list_wallet_driver(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.account).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.account).send_keys("batonnt1")
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search1).click()
        time.sleep(7)
        logging.info("-------------------------")
        logging.info("VÍ LÁI XE - 3.1 Danh sách ví lái xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            summary_wallet = var_stx.driver.find_element(By.XPATH, var_stx.summary_wallet).text
            balance_wallet1 = var_stx.driver.find_element(By.XPATH, var_stx.balance_wallet1).text
            balance_wallet2 = var_stx.driver.find_element(By.XPATH, var_stx.balance_wallet2).text
            logging.info(summary_wallet)
            logging.info(balance_wallet1)
            logging.info(balance_wallet2)
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "Tổng số ví:: {}\nSố dư ví tài khoản: {}\nSố dư ví tiền mặt: {}"
                                       .format(summary_wallet, balance_wallet1, balance_wallet2))

            if (summary_wallet != "") and (balance_wallet1 != "") and (balance_wallet2 != ""):
                logging.info("True")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_stx.driver.save_screenshot(var_stx.imagepath + code + "_DanhSachViLaiXe_ThanhTongQuan.png")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_DanhSachViLaiXe_ThanhTongQuan.png")
        except:
            logging.info("False")
            var_stx.driver.save_screenshot(var_stx.imagepath + code + "_DanhSachViLaiXe_ThanhTongQuan.png")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_DanhSachViLaiXe_ThanhTongQuan.png")


    def list_wallet_driver_search(self, code, eventname, result, path_input, path_data, path_check, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_wallet_driver)
        except:
            list_wallet_driver.list_wallet_driver(self, "", "", "")

        list_wallet_driver.list_wallet_driver_x(self)

        var_stx.driver.find_element(By.XPATH, var_stx.number).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.number).send_keys("1")
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search1).click()
        time.sleep(7)
        try:
            var_stx.driver.implicitly_wait(0.3)
            var_stx.driver.find_element(By.XPATH, var_stx.col_id_FullName0)
        except:

            var_stx.driver.find_element(By.XPATH, var_stx.account).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.name_drive).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.number).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.search1).click()
            time.sleep(7)

        data = var_stx.driver.find_element(By.XPATH, path_data).text
        var_stx.driver.find_element(By.XPATH, path_input).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, path_input).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search1).click()
        time.sleep(7)
        if name_image == "_DanhSachViLaiXe_SoHieu.png":
            logging.info("-------------------------")
            logging.info("VÍ LÁI XE - 3.1 Danh sách ví lái xe")
            logging.info("Mã - " + code)
            logging.info("Tên sự kiện - " + eventname)
            logging.info("Kết quả - " + result)

            if data == "-":
                try:
                    var_stx.driver.find_element(By.XPATH, path_check)
                    logging.info("False")
                    var_stx.driver.save_screenshot(var_stx.imagepath + code + name_image)
                    module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                    module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + name_image)
                except:
                    logging.info("True")
                    module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
            else:
                check_text = var_stx.driver.find_element(By.XPATH, path_check).text
                logging.info(check_text)
                logging.info(data)
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, check_text)
                if check_text == data:
                    logging.info("True")
                    module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    logging.info("False")
                    var_stx.driver.save_screenshot(var_stx.imagepath + code + name_image)
                    module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                    module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + name_image)
        else:
            module_other_stx.write_result_text_try_if(code, eventname, result, "VÍ LÁI XE - 3.1 Danh sách ví lái xe",
                                                      path_check, data, name_image)

        var_stx.driver.find_element(By.XPATH, path_input).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)




    def list_wallet_driver_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")

        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_wallet_driver)
        except:
            list_wallet_driver.list_wallet_driver(self, "", "", "")

        list_wallet_driver.list_wallet_driver_x(self)

        var_stx.driver.find_element(By.XPATH, var_stx.number).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.number).send_keys("1")
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search1).click()
        time.sleep(7)
        var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        time.sleep(6)
        var_stx.driver.find_element(By.XPATH, var_stx.number).clear()
        time.sleep(0.5)
        try:
            var_stx.driver.implicitly_wait(0.3)
            var_stx.driver.find_element(By.XPATH, var_stx.not_role)
            var_stx.driver.back()
            time.sleep(5)
        except:
            print("n0")

        try:
            var_stx.driver.implicitly_wait(0.3)
            var_stx.driver.find_element(By.XPATH, var_stx.not_role)
            var_stx.driver.back()
            time.sleep(5)
        except:
            print("n0.1")

        module_other_stx.write_result_dowload_file(code, eventname, result, "VÍ LÁI XE - 3.1 Danh sách ví lái xe",
                                                        "_DanhSachViLaiXe.xlsx", "_DanhSachViLaiXe.png")




    def list_wallet_driver_recharge(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_wallet_driver)
        except:
            list_wallet_driver.list_wallet_driver(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.account).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.account).send_keys(var_stx.data['wallet']['search'])
        var_stx.driver.find_element(By.XPATH, var_stx.search1).click()
        time.sleep(7)
        var_stx.driver.find_element(By.XPATH, var_stx.icon_recharge).click()
        time.sleep(3.5)
        var_stx.driver.find_element(By.XPATH, var_stx.recharge_money).send_keys(var_stx.data['wallet']['recharge_monney'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.recharge_conten).send_keys(var_stx.data['wallet']['recharge_conten'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.recharge_money_source).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.recharge).click()
        time.sleep(3)
        var_stx.driver.find_element(By.XPATH, var_stx.confirm1).click()
        time.sleep(2.5)
        logging.info("-------------------------")
        logging.info("VÍ LÁI XE - 3.1 Danh sách ví lái xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            recharge_message = var_stx.driver.find_element(By.XPATH, var_stx.recharge_message).text
            print(recharge_message)

            recharge_monney = var_stx.driver.find_element(By.XPATH, var_stx.recharge_monney).text
            print(recharge_monney)

            recharge_name_wallet = var_stx.driver.find_element(By.XPATH, var_stx.recharge_name_wallet).text
            print(recharge_name_wallet)

            recharge_service = var_stx.driver.find_element(By.XPATH, var_stx.recharge_service).text
            print(recharge_service)

            recharge_monney2 = var_stx.driver.find_element(By.XPATH, var_stx.recharge_monney2).text
            print(recharge_monney2)

            recharge_source_monney = var_stx.driver.find_element(By.XPATH, var_stx.recharge_source_monney).text
            print(recharge_source_monney)

            recharge_time = var_stx.driver.find_element(By.XPATH, var_stx.recharge_time).text
            print(recharge_time)

            recharge_code_gd = var_stx.driver.find_element(By.XPATH, var_stx.recharge_code_gd).text
            print(recharge_code_gd)

            recharge_conten = var_stx.driver.find_element(By.XPATH, var_stx.recharge_conten1).text
            print(recharge_conten)

            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "Message: {}\nSố tiền: {}\nTên ví: {}\nDịch vụ: {}\nSố tiền: {}"
                                                                                    "\nNguồn tiền: {}\nThời gian: {}\nMã giao dịch: {}\nNội dung: {}"
                                       .format(recharge_message, recharge_monney, recharge_name_wallet, recharge_service, recharge_monney2,
                                               recharge_source_monney, recharge_time, recharge_code_gd, recharge_conten))

            if (recharge_message == "Đã lưu lại giao dịch, Chờ xác nhận.") and (recharge_monney == "1.000.000 VNĐ") and (recharge_name_wallet != "") \
                    and (recharge_service == "Nạp tiền vào Ví Tài Khoản") and (recharge_monney2 == "1.000.000₫") and (recharge_source_monney == "Quầy thu tại hãng") \
                    and (recharge_time != "") and (recharge_code_gd != "") and (recharge_conten == "Trường test nạp tiền"):
                logging.info("True")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_stx.driver.save_screenshot(var_stx.imagepath + code + "_DanhSachViLaiXe_NapTien.png")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_DanhSachViLaiXe_NapTien.png")
        except:
            logging.info("False")
            var_stx.driver.save_screenshot(var_stx.imagepath + code + "_DanhSachViLaiXe_NapTien.png")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_DanhSachViLaiXe_NapTien.png")


        try:
            var_stx.driver.implicitly_wait(1)
            var_stx.driver.find_element(By.XPATH, var_stx.close).click()
            time.sleep(4)
        except:
            pass


    def list_wallet_driver_withdraw(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_wallet_driver)
        except:
            list_wallet_driver.list_wallet_driver(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.account).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.account).send_keys(var_stx.data['wallet']['search'])
        var_stx.driver.find_element(By.XPATH, var_stx.search1).click()
        time.sleep(7)
        var_stx.driver.find_element(By.XPATH, var_stx.icon_withdraw).click()
        time.sleep(3.5)


        var_stx.driver.find_element(By.XPATH, var_stx.recharge_money).send_keys(var_stx.data['wallet']['withdraw_money'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.recharge_conten).send_keys(var_stx.data['wallet']['withdraw_conten'])
        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.withdraw).click()
        time.sleep(3)
        var_stx.driver.find_element(By.XPATH, var_stx.confirm1).click()
        time.sleep(2.5)
        logging.info("-------------------------")
        logging.info("VÍ LÁI XE - 3.1 Danh sách ví lái xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            withdraw_message = var_stx.driver.find_element(By.XPATH, var_stx.recharge_message).text
            print(withdraw_message)

            withdraw_monney = var_stx.driver.find_element(By.XPATH, var_stx.recharge_monney).text
            print(withdraw_monney)

            withdraw_service = var_stx.driver.find_element(By.XPATH, var_stx.withdraw_service).text
            print(withdraw_service)

            withdraw_source = var_stx.driver.find_element(By.XPATH, var_stx.withdraw_source).text
            print(withdraw_source)

            withdraw_time = var_stx.driver.find_element(By.XPATH, var_stx.withdraw_time).text
            print(withdraw_time)

            withdraw_code = var_stx.driver.find_element(By.XPATH, var_stx.withdraw_code).text
            print(withdraw_code)

            withdraw_conten = var_stx.driver.find_element(By.XPATH, var_stx.withdraw_conten).text
            print(withdraw_conten)

            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "Message: {}\nSố tiền: {}\nDịch vụ: {}\nNguồn : {}"
                                                                                    "\nThời gian: {}\nMã giao dịch: {}\nNội dung: {}"
                                       .format(withdraw_message, withdraw_monney, withdraw_service, withdraw_source, withdraw_time, withdraw_code,
                                               withdraw_conten))

            if (withdraw_message == "Đã lưu lại giao dịch, Chờ xác nhận.") and (withdraw_monney == "100 VNĐ") and (withdraw_service == "Rút tiền Ví Tiền Mặt") \
                    and (withdraw_source == "Rút tại quầy") and (withdraw_time != "") and (withdraw_code != "") and (withdraw_conten == var_stx.data['wallet']['withdraw_conten']):
                logging.info("True")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_stx.driver.save_screenshot(var_stx.imagepath + code + "_DanhSachViLaiXe_RutTien.png")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_DanhSachViLaiXe_RutTien.png")
        except:
            logging.info("False")
            var_stx.driver.save_screenshot(var_stx.imagepath + code + "_DanhSachViLaiXe_RutTien.png")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_DanhSachViLaiXe_RutTien.png")


        try:
            var_stx.driver.implicitly_wait(1)
            var_stx.driver.find_element(By.XPATH, var_stx.close).click()
            time.sleep(4)
        except:
            pass


    def list_wallet_driver_hisory(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_wallet_driver)
        except:
            list_wallet_driver.list_wallet_driver(self, "", "", "")

        list_wallet_driver.list_wallet_driver_x(self)

        var_stx.driver.find_element(By.XPATH, var_stx.account).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.account).send_keys(var_stx.data['wallet']['search'])
        var_stx.driver.find_element(By.XPATH, var_stx.search1).click()
        time.sleep(7)
        var_stx.driver.find_element(By.XPATH, var_stx.icon_history).click()
        time.sleep(10)
        var_stx.driver.switch_to.window(var_stx.driver.window_handles[1])
        time.sleep(5)
        try:
            wait = WebDriverWait(var_stx.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.search)))
        except:
            pass

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        except:
            time.sleep(3)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        logging.info("-------------------------")
        logging.info("VÍ LÁI XE - 3.1 Danh sách ví lái xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            page = var_stx.driver.find_element(By.XPATH, var_stx.title_page).text
            print(page)
            name_driver = var_stx.driver.find_element(By.XPATH, var_stx.ag1_9).text
            print(name_driver)
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "Chuyển tới trang: {}\nTên lái xe: {}"
                                       .format(page, name_driver))
            if (page == "3.5 Lịch sử ví tiền") and (name_driver == var_stx.data['wallet']['search']):
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_stx.driver.save_screenshot(var_stx.imagepath + code + "_DanhSachViLaiXe_LichSu.png")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_DanhSachViLaiXe_LichSu.png")
        except:
            logging.info("False")
            var_stx.driver.save_screenshot(var_stx.imagepath + code + "_DanhSachViLaiXe_LichSu.png")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_DanhSachViLaiXe_LichSu.png")

        module_other_stx.close_tab()
        var_stx.driver.switch_to.window(var_stx.driver.window_handles[0])
        time.sleep(1)







class recharge:

    def pay_money_into_the_driver_wallet(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.driver_wallet).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.pay_money_into_the_driver_wallet).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.driver_wallet).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.pay_money_into_the_driver_wallet).click()
        time.sleep(2)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.title_page)))
            time.sleep(2)
        except:
            pass
        module_other_stx.write_result_text_try_if(code, eventname, result, "VÍ LÁI XE - 3.2 Đóng tiền vào ví lái xe",
                                                  var_stx.title_page, "3.2 Đóng tiền vào ví lái xe", "_DongTienVaoViXe.png")


    def pay_money_into_the_driver_wallet_fill(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_pay_money_into_the_driver_wallet)
        except:
            recharge.pay_money_into_the_driver_wallet(self, "", "", "")


        var_stx.driver.find_element(By.XPATH, var_stx.recharge_type_fee).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.recharge_account).click()
        time.sleep(3)


        var_stx.driver.find_element(By.XPATH, var_stx.recharge_account_input).send_keys(var_stx.data['wallet']['search'])
        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.recharge_account1).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.recharge_money1).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.recharge_money1_input).send_keys(var_stx.data['wallet']['recharge_monney1'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.recharge_note).send_keys(var_stx.data['wallet']['note1'])
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.save).click()
        time.sleep(2.5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "VÍ LÁI XE - 3.2 Đóng tiền vào ví lái xe",
                                                  var_stx.text_success, "Tạo giao dịch đóng tiền thành công.", "_DongTienVaoViXe_Luu.png")






class withdraw:

    def withdraw_money_from_driver_wallet(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.driver_wallet).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.Withdraw_money_from_driver_wallet).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.driver_wallet).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.Withdraw_money_from_driver_wallet).click()
        time.sleep(2)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.title_page)))
            time.sleep(2)
        except:
            pass
        module_other_stx.write_result_text_try_if(code, eventname, result, "VÍ LÁI XE - 3.3 Rút tiền từ ví lái xe",
                                                  var_stx.title_page, "3.3 Rút tiền từ ví lái xe", "_RutTienTuViXe.png")


    def withdraw_money_from_driver_wallet_fill(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_withdraw_money_from_driver_wallet)
        except:
            withdraw.withdraw_money_from_driver_wallet(self, "", "", "")


        var_stx.driver.find_element(By.XPATH, var_stx.recharge_type_fee).click()
        time.sleep(1)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.DriverCode).send_keys(var_stx.data['wallet']['search'])
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.DriverCodeList).send_keys(var_stx.data['wallet']['search'])
        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.recharge_batont1).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.Amount).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.Amount).send_keys(var_stx.data['wallet']['withdraw_monney2'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.Comment).send_keys(var_stx.data['wallet']['note2'])
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.save).click()
        time.sleep(2.5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "VÍ LÁI XE - 3.2 Đóng tiền vào ví lái xe",
                                                  var_stx.text_success, "Tạo giao dịch rút tiền thành công.", "_RutTienTuViXe_Luu.png")






class transaction_confirmation:


    def transaction_confirmation_x(self):
        var_stx.driver.implicitly_wait(0.2)
        time.sleep(1)
        try:
            # var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            # var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(Keys.CONTROL + "a")
            # var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(Keys.BACKSPACE)
            tu_ngay = var_stx.driver.find_element(By.XPATH, var_stx.from_day)
            var_stx.driver.execute_script("arguments[0].value = '';", tu_ngay)
            time.sleep(0.2)
        except:
            pass

        time.sleep(1.5)
        try:
            # var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            # var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(Keys.CONTROL + "a")
            # var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(Keys.BACKSPACE)
            den_ngay = var_stx.driver.find_element(By.XPATH, var_stx.to_day)
            var_stx.driver.execute_script("arguments[0].value = '';", den_ngay)
            time.sleep(0.2)
        except:
            pass

        time.sleep(1)

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.transaction_confirmation_x3).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.2)
        except:
            pass



    def transaction_confirmation(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.driver_wallet).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.transaction_confirmation).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.driver_wallet).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.transaction_confirmation).click()
        time.sleep(2)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.title_page)))
            time.sleep(2)
        except:
            pass
        module_other_stx.write_result_text_try_if(code, eventname, result, "VÍ LÁI XE - 3.4 Xác nhận giao dịch",
                                                  var_stx.title_page, "3.4 Xác nhận giao dịch", "_XacNhanGiaoDich.png")



    def transaction_confirmation_from_to_day(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_transaction_confirmation)
        except:
            transaction_confirmation.transaction_confirmation(self, "", "", "")

        transaction_confirmation.transaction_confirmation_x(self)
        date = var_stx.driver.find_element(By.XPATH, var_stx.ag1_10).text
        date1 = date.split(" ")[0]
        # date1 = date[-10::]
        print(date1)
        date2 = date1 + " 00:00"
        date3 = date1 + " 23 :00"
        print(date)
        var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(date2)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(date3)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        var_stx.driver.implicitly_wait(1)
        logging.info("-------------------------")
        logging.info("VÍ LÁI XE - 3.4 Xác nhận giao dịch")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            check_text = var_stx.driver.find_element(By.XPATH, var_stx.ag1_10).text
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, check_text)

            check_text = check_text.split(" ")[0]
            logging.info(check_text)
            logging.info(date1)
            if check_text == date1:
                logging.info("True")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_stx.driver.save_screenshot(var_stx.imagepath + code + "_XacNhanGiaoDich_TuNgayDenNgay.png")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_XacNhanGiaoDich_TuNgayDenNgay.png")
        except:
            logging.info("False")
            var_stx.driver.save_screenshot(var_stx.imagepath + code + "_XacNhanGiaoDich_TuNgayDenNgay.png")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_XacNhanGiaoDich_TuNgayDenNgay.png")



    def transaction_confirmation_search(self, code, eventname, result, path_data, type_check, path_check, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_transaction_confirmation)
        except:
            transaction_confirmation.transaction_confirmation(self, "", "", "")

        transaction_confirmation.transaction_confirmation_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        if type_check == "0":
            data = var_stx.driver.find_element(By.XPATH, path_data).text
            var_stx.driver.find_element(By.XPATH, var_stx.transaction_confirmation_x3).send_keys(data)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(5)
            module_other_stx.write_result_text_try_if(code, eventname, result, "VÍ LÁI XE - 3.4 Xác nhận giao dịch",
                                                      path_check, data, name_image)

        if type_check == "1":
            var_stx.driver.find_element(By.XPATH, var_stx.transaction_confirmation_x3).send_keys(var_stx.data['wallet']['sdt'])
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(5)
            module_other_stx.write_result_text_try_if(code, eventname, result, "VÍ LÁI XE - 3.4 Xác nhận giao dịch",
                                                      path_check, var_stx.data['wallet']['search'], name_image)



    def transaction_confirmation_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_transaction_confirmation)
        except:
            transaction_confirmation.transaction_confirmation(self, "", "", "")

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.ag1_2)
        except:
            transaction_confirmation.transaction_confirmation_x(self)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(5)
        var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        time.sleep(5)
        # minitor_stx.get_info_web()
        # try:
        #     minitor_stx.get_info_excel(5, "Sheet 1")
        # except:
        #     var_stx.driver.refresh()
        #     time.sleep(7)
        #     var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        #     time.sleep(30)
        #     minitor_stx.get_info_web()
        #     minitor_stx.get_info_excel(5, "Sheet 1")
        #
        # minitor_stx.check_info_web_excel(code, eventname, result, "VÍ LÁI XE - 3.1 Danh sách ví lái xe")

        module_other_stx.write_result_dowload_file(code, eventname, result, "VÍ LÁI XE - 3.4 Xác nhận giao dịch",
                                                   "_xacnhangiaodich.xls", "_XacNhanGiaoDich_XuatExcel.png")

        try:
            var_stx.driver.implicitly_wait(1)
            check_route_excel = var_stx.driver.find_element(By.XPATH, var_stx.check_route_excel).text
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, check_route_excel)
            var_stx.driver.back()
            time.sleep(3)
        except:
            pass



    def transaction_confirmation_pay(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_transaction_confirmation)
        except:
            transaction_confirmation.transaction_confirmation(self, "", "", "")
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.transaction_confirmation_pay).click()
        time.sleep(2.5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "VÍ LÁI XE - 3.4 Xác nhận giao dịch",
                                                  var_stx.check_transaction_confirmation_pay, "VÍ LÁI XE", "_XacNhanGiaoDich_ThanhToan.png")

        try:
            var_stx.driver.implicitly_wait(1)
            var_stx.driver.find_element(By.XPATH, var_stx.exit).click()
            time.sleep(1)
        except:
            pass



    def transaction_confirmation_history_pay(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_transaction_confirmation)
        except:
            transaction_confirmation.transaction_confirmation(self, "", "", "")
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.transaction_confirmation_history_pay).click()
        time.sleep(5)
        var_stx.driver.switch_to.window(var_stx.driver.window_handles[1])
        time.sleep(2)
        logging.info("-------------------------")
        logging.info("VÍ LÁI XE - 3.4 Xác nhận giao dịch")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            wait = WebDriverWait(var_stx.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.title_page)))
            time.sleep(1)
            page = var_stx.driver.find_element(By.XPATH, var_stx.title_page).text
            print(page)
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "Chuyển tới trang: {}".format(page))
            if page == "3.11 Lịch sử thanh toán":
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_stx.driver.save_screenshot(var_stx.imagepath + code + "_XacNhanGiaoDich_LichSuThanhToan.png")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_XacNhanGiaoDich_LichSuThanhToan.png")
        except:
            logging.info("False")
            var_stx.driver.save_screenshot(var_stx.imagepath + code + "_XacNhanGiaoDich_LichSuThanhToan.png")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_XacNhanGiaoDich_LichSuThanhToan.png")

        module_other_stx.close_tab()
        var_stx.driver.switch_to.window(var_stx.driver.window_handles[0])
        time.sleep(1)



    def transaction_confirmation_igree(self, code, eventname, result, button, desire, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_transaction_confirmation)
            var_stx.driver.find_element(By.XPATH, var_stx.STAXI)
        except:
            transaction_confirmation.transaction_confirmation(self, "", "", "")
        time.sleep(2)

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.ag1_2)
        except:
            transaction_confirmation.transaction_confirmation_x(self)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(5)

        var_stx.driver.find_element(By.XPATH, var_stx.transaction_confirmation_igree).click()
        time.sleep(3)
        var_stx.driver.find_element(By.XPATH, button).click()
        time.sleep(3)
        module_other_stx.write_result_text_try_if(code, eventname, result, "VÍ LÁI XE - 3.4 Xác nhận giao dịch",
                                                  var_stx.message, desire, name_image)
        try:
            var_stx.driver.implicitly_wait(1)
            var_stx.driver.find_element(By.XPATH, var_stx.close1).click()
            time.sleep(1.5)
        except:
            pass






class wallet_history:


    def wallet_history(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.driver_wallet).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.wallet_history).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.driver_wallet).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.wallet_history).click()
        time.sleep(2)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.title_page)))
            time.sleep(2)
        except:
            pass
        module_other_stx.write_result_text_try_if(code, eventname, result, "VÍ LÁI XE - 3.5 Lịch sử ví tiền",
                                                 var_stx.title_page, "3.5 Lịch sử ví tiền", "_LichSuViTien.png")


    def wallet_history_x(self):
        var_stx.driver.implicitly_wait(0.2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.driver_sdt).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.PrivateCode_input).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.code_gd).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.type_wallet1).click()
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.type_wallet2).click()
            time.sleep(0.3)
        except:
            pass


    def wallet_history_from_to_day(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_wallet_history)
        except:
            wallet_history.wallet_history(self, "", "", "")


        date = var_stx.driver.find_element(By.XPATH, var_stx.from_day1).get_attribute("value")
        print(date)
        date1 = date.split(" ")[0]

        day = date1.split("/")[0]
        day = int(day)
        day = str(day)
        month = date1.split("/")[1]
        month = int(month)
        month = str(month)
        year = date1.split("/")[2]

        date1 = day + "/" + month + "/" + year
        print(date1)

        print(date1)
        date2 = date1 + " 00:00"
        date3 = date1 + " 23 :00"



        wallet_history.wallet_history_x(self)

        var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(date2)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(date3)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(7)
        logging.info("-------------------------")
        logging.info("VÍ LÁI XE - 3.5 Lịch sử ví tiền")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            check_text = var_stx.driver.find_element(By.XPATH, var_stx.list_data2_14).text
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, check_text)

            check_text = check_text.split(" ")[1]
            logging.info(check_text)
            logging.info(date1)
            if check_text == date1:
                logging.info("True")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_stx.driver.save_screenshot(var_stx.imagepath + code + "_LichSuViTien_TuNgayDenNgay.png")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_LichSuViTien_TuNgayDenNgay.png")
        except:
            logging.info("False")
            var_stx.driver.save_screenshot(var_stx.imagepath + code + "_XacNhanGiaoDich_TuNgayDenNgay.png")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_LichSuViTien_TuNgayDenNgay.png")

        #
        #
        #
        # module_other_stx.write_result_text_try_if_cut2(code, eventname, result, "VÍ LÁI XE - 3.5 Lịch sử ví tiền",
        #                                       var_stx.list_data2_13, date1, "_LichSuViTien_TuNgayDenNgay.png", 9, 19)


    def wallet_history_search(self, code, eventname, result, path_data, path_input, path_check, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_wallet_history)
        except:
            wallet_history.wallet_history(self, "", "", "")


        wallet_history.wallet_history_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        data = var_stx.driver.find_element(By.XPATH, path_data).text
        var_stx.driver.find_element(By.XPATH, path_input).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "VÍ LÁI XE - 3.5 Lịch sử ví tiền",
                                                  path_check, data, name_image)




    def wallet_history_search_scroll(self, code, eventname, result, path_data, path_input, path_check, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_wallet_history)
        except:
            wallet_history.wallet_history(self, "", "", "")


        wallet_history.wallet_history_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3.5)
        scroll_bar = var_stx.driver.find_element(By.XPATH, "//*[@class='ag-body-horizontal-scroll-viewport']")
        ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(800, 0).release().perform()
        time.sleep(1.5)
        data = var_stx.driver.find_element(By.XPATH, path_data).text
        print(data)
        var_stx.driver.find_element(By.XPATH, path_input).send_keys(data)
        time.sleep(1)
        ag1_2 = var_stx.driver.find_element(By.XPATH, var_stx.ag1_10).text
        print("ag1_10: {}".format(ag1_2))
        ag1_3 = var_stx.driver.find_element(By.XPATH, var_stx.ag1_11).text
        print("ag1_11: {}".format(ag1_3))
        ag1_4 = var_stx.driver.find_element(By.XPATH, var_stx.ag1_12).text
        print("ag1_12: {}".format(ag1_4))
        ag1_5 = var_stx.driver.find_element(By.XPATH, var_stx.ag1_13).text
        print("ag1_13: {}".format(ag1_5))
        # ag1_6 = var_stx.driver.find_element(By.XPATH, var_stx.ag1_14).text
        # print("ag1_10: {}".format(ag1_6))
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        print("đã bấm tìm kiếm")
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "VÍ LÁI XE - 3.5 Lịch sử ví tiền",
                                                  path_check, data, name_image)
        ag1_2 = var_stx.driver.find_element(By.XPATH, var_stx.ag1_10).text
        print("ag1_10: {}".format(ag1_2))
        ag1_3 = var_stx.driver.find_element(By.XPATH, var_stx.ag1_11).text
        print("ag1_11: {}".format(ag1_3))
        ag1_4 = var_stx.driver.find_element(By.XPATH, var_stx.ag1_12).text
        print("ag1_12: {}".format(ag1_4))
        ag1_5 = var_stx.driver.find_element(By.XPATH, var_stx.ag1_13).text
        print("ag1_13: {}".format(ag1_5))

        var_stx.driver.refresh()
        time.sleep(5)


    def wallet_history_bombobox(self, code, eventname, result, button, path_check, desire, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_wallet_history)
        except:
            wallet_history.wallet_history(self, "", "", "")

        wallet_history.wallet_history_x(self)

        var_stx.driver.find_element(By.XPATH, var_stx.reportrange).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.reportrange_30day).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, button).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        a = var_stx.driver.find_element(By.XPATH, path_check).text
        print(a)
        module_other_stx.write_result_text_try_if(code, eventname, result, "VÍ LÁI XE - 3.5 Lịch sử ví tiền",
                                                  path_check, desire, name_image)


    def wallet_history_detail(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_wallet_history)
        except:
            wallet_history.wallet_history(self, "", "", "")

        wallet_history.wallet_history_x(self)

        var_stx.driver.find_element(By.XPATH, var_stx.reportrange).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.reportrange_30day).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        try:
            var_stx.driver.find_element(By.XPATH, "//*[@class='ag-center-cols-viewport']/div/div[1]")
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.reportrange).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.in_month).click()
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(5)

        scroll_bar = var_stx.driver.find_element(By.XPATH, "//*[@class='ag-body-horizontal-scroll-viewport']")
        try:
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(800, 0).release().perform()
            time.sleep(1)
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(800, 0).release().perform()
        except:
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(400, 0).release().perform()
            time.sleep(1)
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(400, 0).release().perform()

        time.sleep(2)
        n = 0
        while (n < 7):
            n = n + 1
            n = str(n)
            path_icon = "//*[@class='ag-center-cols-viewport']/div/div[" + n + "]//*[@class='fa fa-angle-double-right']"
            try:
                var_stx.driver.find_element(By.XPATH, path_icon)
                break
            except:
                try:
                    var_stx.driver.find_element(By.XPATH, "//*[@class='ag-icon ag-icon-next']").click()
                    time.sleep(2)
                    ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(400, 0).release().perform()
                    time.sleep(1)
                except:
                    pass
            n = int(n)


        n = 0
        while (n < 25):
            n = n + 1
            n = str(n)
            path_icon = "//*[@class='ag-center-cols-viewport']/div/div[" + n + "]//*[@class='fa fa-angle-double-right']"
            try:
                button = var_stx.driver.find_element(By.XPATH, path_icon)
                var_stx.driver.execute_script("arguments[0].click();", button)
                # var_stx.driver.find_element(By.XPATH, path_icon).click()
                time.sleep(5)
                var_stx.driver.switch_to.window(var_stx.driver.window_handles[1])
                time.sleep(3)
                wait = WebDriverWait(var_stx.driver, 20)
                element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.ag1_2)))
                break
            except:
                pass
            n = int(n)


        # var_stx.driver.find_element(By.XPATH, var_stx.ag1_button).click()
        # time.sleep(5)

        logging.info("-------------------------")
        logging.info("VÍ LÁI XE - 3.5 Lịch sử ví tiền")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            page = var_stx.driver.find_element(By.XPATH, var_stx.title_page).text
            print(page)
            try:
                code_customer = var_stx.driver.find_element(By.XPATH, var_stx.col_id_2_a).text
            except:
                code_customer = var_stx.driver.find_element(By.XPATH, var_stx.table_1_1).text

            print(code_customer)
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "Chuyển tới trang: {}\nMã quốc khách: {}"
                                       .format(page, code_customer))
            if (page == "8.4 Báo cáo doanh thu") and (code_customer != ""):
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_stx.driver.save_screenshot(var_stx.imagepath + code + "_LichSuViTien_ChiTiet.png")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_LichSuViTien_ChiTiet.png")
        except:
            logging.info("False")
            var_stx.driver.save_screenshot(var_stx.imagepath + code + "_LichSuViTien_ChiTiet.png")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_LichSuViTien_ChiTiet.png")

        module_other_stx.close_tab()
        var_stx.driver.switch_to.window(var_stx.driver.window_handles[0])
        time.sleep(1)


    def wallet_history_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_wallet_history)
        except:
            wallet_history.wallet_history(self, "", "", "")


        wallet_history.wallet_history_x(self)

        var_stx.driver.find_element(By.XPATH, var_stx.WalletOperationType_naptien).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.PrivateCode1)
        except:
            wallet_history.wallet_history_x(self)
            var_stx.driver.find_element(By.XPATH, var_stx.search)
            time.sleep(5)

        report_stx.get_info_web4()

        var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        time.sleep(1)
        try:
            wait = WebDriverWait(var_stx.driver, 20)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.messsage_export)))

            report_stx.dowload_excel(self, "3.5 Lịch sử ví tiền")
            minitor_stx.get_info_excel1(3, "Data")
        except:
            report_stx.get_info_web4()
            minitor_stx.get_info_excel1(5, "Sheet 1")



        minitor_stx.check_info_web_excel(code, eventname, result, "VÍ LÁI XE - 3.5 Lịch sử ví tiền")


    def wallet_history_print(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_wallet_history)
        except:
            wallet_history.wallet_history(self, "", "", "")

        # wallet_history.wallet_history_x(self)
        # var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        # time.sleep(5)
        var_stx.driver.find_element(By.XPATH, var_stx.print_data).click()
        time.sleep(3)
        logging.info("False")
        var_stx.driver.save_screenshot(var_stx.imagepath + code + "_LichSuViTien_InDuLieu.png")
        module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
        module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_LichSuViTien_InDuLieu.png")







class withdraw_money:       #Tool rút tiền
    def move13_1(self):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.g7_taxi_hn_209)
        except:
            login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.driver_wallet_v2).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.move13_1).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.driver_wallet_v2).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.move13_1).click()
        time.sleep(2)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.check_13_1)))
        except:
            url = var_stx.linktest + 'DriverWallet/WithDraw_V2?58887578'
            var_stx.driver.get(url)
            print(f"Đã vào trang: {url}")
            time.sleep(7)

    def move3_5(self):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.g7_taxi_hn_209)
        except:
            login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.driver_wallet).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.move3_5).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.driver_wallet).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.move3_5).click()
        time.sleep(5)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.check_3_5)))
        except:
            url = var_stx.linktest + 'DriverWallet/History?5462810'
            var_stx.driver.get(url)
            print(f"Đã vào trang: {url}")
            time.sleep(7)

    @retry(tries=2, delay=2, backoff=1, jitter=5, )
    def tc1(self, drive_wallet, row):
        row = int(row)
        var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 250, 2, "None")
        var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 251, 2, 0)

        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.title_13_1)
        except:
            withdraw_money.move13_1(self)

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.add_new2).click()
        except:
            try:
                var_stx.driver.implicitly_wait(0.3)
                var_stx.driver.find_element(By.XPATH, var_stx.withdraw_money_cancel).click()
                time.sleep(2)
            except:
                pass

            try:
                var_stx.driver.implicitly_wait(0.3)
                var_stx.driver.find_element(By.XPATH, var_stx.skip).click()
                time.sleep(2)
                var_stx.driver.find_element(By.XPATH, var_stx.withdraw_money_cancel).click()
                time.sleep(2)
            except:
                pass
            try:
                var_stx.driver.find_element(By.XPATH, var_stx.add_new2).click()
            except:
                var_stx.driver.refresh()
                time.sleep(7)
                var_stx.driver.find_element(By.XPATH, var_stx.add_new2).click()

        #Chọn lái xe mặc định
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.drive_withdraw_money_select)))
        time.sleep(1)
        element.click()
        time.sleep(1.5)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.drive_withdraw_money_select1)))
        element.click()
        time.sleep(1)

        #Chọn lái xe danh sách
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.drive_withdraw_money_select)))
        element.click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.drive_withdraw_money_select_input).send_keys(drive_wallet)
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.drive_withdraw_money_select_input).send_keys(Keys.ENTER)
        time.sleep(2)
        check_driver = var_stx.driver.find_element(By.XPATH, var_stx.drive_withdraw_money_select_input).get_attribute("text")
        print(f"text: {check_driver}")
        if check_driver == "\n  -- Chọn lái xe --\n  \n":
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.drive_withdraw_money_select)))
            element.click()
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.drive_withdraw_money_select_input).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.drive_withdraw_money_select_input).send_keys(drive_wallet)
            time.sleep(2)
            try:
                var_stx.driver.find_element(By.XPATH, var_stx.drive_withdraw_money_select1).click()
                time.sleep(1)
            except:
                pass

        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.create).click()
        time.sleep(1.5)
        var_stx.driver.save_screenshot(var_stx.imagepath + "RutTien" + "_Tc01.png")

        try:
            var_stx.driver.implicitly_wait(1.5)
            message = var_stx.driver.find_element(By.XPATH, var_stx.toast_message).text
            var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 250, 2, "Không có dữ liệu")
            var_stx.appendData("./data_wallet.xlsx", "Sheet1", row, 2, "False")
            var_stx.appendData("./data_wallet.xlsx", "Sheet1", row, 3, "Không tìm thấy lái xe")
            var_stx.driver.find_element(By.XPATH, var_stx.withdraw_money_cancel).click()
            time.sleep(2)
        except:
            pass


        try:
            var_stx.driver.implicitly_wait(2.5)
            soduvisaurut = var_stx.driver.find_element(By.XPATH, var_stx.soduvisaurut).get_attribute("value")
            var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 250, 2, "Cho phép tạo")
        except:
            pass

        try:
            var_stx.driver.implicitly_wait(2.5)
            laixedangduocchilo = var_stx.driver.find_element(By.XPATH, var_stx.laixedangduocchilo).text
            var_stx.driver.find_element(By.XPATH, var_stx.skip).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.withdraw_money_cancel).click()
            var_stx.appendData("./data_wallet.xlsx", "Sheet1", row, 2, "True")
            var_stx.appendData("./data_wallet.xlsx", "Sheet1", row, 3, "Chưa kiểm tra do nằm trong lô chi dở")
            var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 250, 2, "Không có dữ liệu")
            time.sleep(2)
        except:
            pass


    @retry(tries=2, delay=2, backoff=1, jitter=5, )
    def tc2(self, drive_wallet, row):
        row = int(row)
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.soduvisaurut)
        except:
            withdraw_money.tc1(self, drive_wallet, row)

        try:
            var_stx.driver.implicitly_wait(0.3)
            var_stx.driver.find_element(By.XPATH, var_stx.select_all).ckick()
            time.sleep(1)
        except:
            pass

        soduvisaurut = var_stx.driver.find_element(By.XPATH, var_stx.soduvisaurut).get_attribute("value")
        soduvisaurut = int(soduvisaurut.replace(".", "").replace("₫", "").strip())
        var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 251, 2, soduvisaurut)
        # var_stx.appendData("./data_wallet.xlsx", "Sheet1", row, 3, f"\nTC2: Số dư ví sau rút: {soduvisaurut}")
        #
        if soduvisaurut == 0:
            var_stx.appendData("./data_wallet.xlsx", "Sheet1", row, 2, "True")
            var_stx.appendData("./data_wallet.xlsx", "Sheet1", row, 3, f"Số dư ví sau rút: {soduvisaurut}")

        # else:
        #     var_stx.appendData("./data_wallet.xlsx", "Sheet1", row, 2, f"\nTC2:  <>  0")


    @retry(tries=2, delay=2, backoff=1, jitter=5, )
    def tc3(self, drive_wallet, row):
        row = int(row)
        var_stx.driver.implicitly_wait(5)
        var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 252, 2, "")
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.back2).click()
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.title_13_1)))
            time.sleep(1.5)
        except:
            pass


        try:
            var_stx.driver.find_element(By.XPATH, var_stx.title_13_1)
        except:
            withdraw_money.move13_1(self)

        var_stx.driver.find_element(By.XPATH, var_stx.withdraw_money_input).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.withdraw_money_input).send_keys(drive_wallet)
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.reportrange).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.yearselect_2023).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.reportrange_left_1).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.yearselect_2027).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.reportrange_right_1).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.yearselect_confirm).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.wait_confirm).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3)
        try:
            code_withdraw_money = var_stx.driver.find_element(By.XPATH, var_stx.ag1_3).get_attribute("value")
            var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 252, 2, "Có dữ liệu")
        except:
            var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 252, 2, "Không dữ liệu")


        var_stx.driver.find_element(By.XPATH, var_stx.wait_confirm1).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3)
        try:
            code_withdraw_money = var_stx.driver.find_element(By.XPATH, var_stx.ag1_3).get_attribute("value")
            var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 252, 2, "Có dữ liệu")
        except:
            pass


    @retry(tries=2, delay=2, backoff=1, jitter=5, )
    def tc4(self, drive_wallet, row):
        row = int(row)
        var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 253, 2, 0)
        var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 254, 2, 0)

        var_stx.driver.implicitly_wait(5)
        withdraw_money.move3_5(self)
        var_stx.driver.find_element(By.XPATH, var_stx.DriverName).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.DriverName).send_keys(drive_wallet)
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.reportrange).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.yearselect_2023).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.reportrange_left_1).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.yearselect_2027).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.reportrange_right_1).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.yearselect_confirm).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.WalletKind).click()
        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3.5)
        var_stx.driver.find_element(By.XPATH, var_stx.page_last).click()
        time.sleep(2.5)

        var_stx.driver.implicitly_wait(0.3)
        n = 21
        while (n > 0):
            n = n - 1
            n = str(n)
            path_soduvi = "//*[@class='ag-center-cols-viewport']/div/div[" + n + "]/div[6]"
            path_sotien = "//*[@class='ag-center-cols-viewport']/div/div[" + n + "]/div[4]"
            print(f"Dòng: {n}")
            try:
                soduvi = var_stx.driver.find_element(By.XPATH, path_soduvi).text
                soduvi = int(soduvi.replace(".", "").replace("₫", "").strip())
                var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 253, 2, soduvi)
                print(f"Số dư ví: {soduvi}")

                sotien = var_stx.driver.find_element(By.XPATH, path_sotien).text
                sotien = int(sotien.replace(".", "").replace("₫", "").replace("+", "").strip())
                var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 254, 2, sotien)
                print(f"Số tiền: {sotien}")
                break
            except:
                pass
            n = int(n)



        soduvisaurut_excel = int(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 251, 2))
        soduvi_excel = int(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 253, 2))
        sotien_excel = int(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 254, 2))
        # sotienchenh = soduvi_excel - sotien_excel
        var_stx.appendData("./data_wallet.xlsx", "Sheet1", row, 4, f"Số dư ví: {soduvi_excel}\n"
                                                                   f"Số tiền : {sotien_excel}\n"
                                                                   f"Số dư ví sau rút: {soduvisaurut_excel}\n"
                                                                   f"Số tiền chênh: {soduvisaurut_excel}")


        if soduvi_excel - sotien_excel == soduvisaurut_excel:
            var_stx.appendData("./data_wallet.xlsx", "Sheet1", row, 2, "False")
            var_stx.appendData("./data_wallet.xlsx", "Sheet1", row, 3, "Thiếu giao dịch đầu từ năm 2024")
        else:
            var_stx.appendData("./data_wallet.xlsx", "Sheet1", row, 2, "False")
            var_stx.appendData("./data_wallet.xlsx", "Sheet1", row, 3, "Lỗi khác.")


    @retry(tries=2, delay=2, backoff=1, jitter=5, )
    def tc5(self, drive_wallet, row):
        row = int(row)
        var_stx.driver.implicitly_wait(5)
        var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 255, 2, 0)
        var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 256, 2, "")


        try:
            var_stx.driver.find_element(By.XPATH, var_stx.title_13_1)
        except:
            withdraw_money.tc3(self, drive_wallet, row)

        #trạng thái chờ xác nhận
        var_stx.driver.find_element(By.XPATH, var_stx.wait_confirm).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3)
        var_stx.driver.implicitly_wait(0.3)
        n = 0
        while (n < 25):
            n = n + 1
            n = str(n)
            money_excel = int(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 255, 2))
            path_withdrawal_code = "//*[@class='ag-center-cols-viewport']/div/div[" + n + "]/div[3]"
            path_money = "//*[@class='ag-center-cols-viewport']/div/div[" + n + "]/div[8]"
            try:
                money = var_stx.driver.find_element(By.XPATH, path_money).text
                withdrawal_code = var_stx.driver.find_element(By.XPATH, path_withdrawal_code).text
                print(money)
                print(withdrawal_code)
                money = int(''.join(re.findall(r'\d+', money)))
                var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 255, 2, money_excel+money)
                var_stx.appendData(var_stx.path_luutamthoi, "Sheet1", 256, 2, f"{withdrawal_code}, ")

            except:
                dau_trang = var_stx.driver.find_element(By.XPATH, var_stx.lbCurrent).text
                cuoi_trang = var_stx.driver.find_element(By.XPATH, var_stx.lbTotal).text
                if dau_trang == cuoi_trang:
                    print("Đã ở trang cuối")
                    break
                else:
                    var_stx.driver.find_element(By.XPATH, var_stx.btNext).click()
                    time.sleep(3)
                    print("Đã chuyển sang trang tiếp theo")
                    n = 0
            n = int(n)


        #trạng thái lần đầu - chờ xác nhận
        var_stx.driver.find_element(By.XPATH, var_stx.wait_confirm1).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3)
        var_stx.driver.implicitly_wait(0.3)
        n = 0
        while (n < 25):
            n = n + 1
            n = str(n)
            money_excel = int(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 255, 2))
            path_withdrawal_code = "//*[@class='ag-center-cols-viewport']/div/div[" + n + "]/div[3]"
            path_money = "//*[@class='ag-center-cols-viewport']/div/div[" + n + "]/div[8]"
            try:
                money = var_stx.driver.find_element(By.XPATH, path_money).text
                withdrawal_code = var_stx.driver.find_element(By.XPATH, path_withdrawal_code).text
                print(money)
                print(withdrawal_code)
                money = int(''.join(re.findall(r'\d+', money)))
                var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 255, 2, money_excel+money)
                var_stx.appendData(var_stx.path_luutamthoi, "Sheet1", 256, 2, f"{withdrawal_code}, ")

            except:
                dau_trang = var_stx.driver.find_element(By.XPATH, var_stx.lbCurrent).text
                cuoi_trang = var_stx.driver.find_element(By.XPATH, var_stx.lbTotal).text
                if dau_trang == cuoi_trang:
                    print("Đã ở trang cuối")
                    break
                else:
                    var_stx.driver.find_element(By.XPATH, var_stx.btNext).click()
                    time.sleep(3)
                    print("Đã chuyển sang trang tiếp theo")
                    n = 0
            n = int(n)



        tongcotsotien = int(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 255, 2))
        soduvisaurut = int(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 251, 2))
        maruttien = var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 256, 2)
        tienchenh = soduvisaurut - tongcotsotien
        var_stx.appendData("./data_wallet.xlsx", "Sheet1", row, 4, f"Số dư ví sau rút: {soduvisaurut}\n"
                                                                   f"Tổng cột số tiền : {tongcotsotien}\n"
                                                                   f"Số tiền chênh lệch: {tienchenh}")

        if tongcotsotien == soduvisaurut:
            var_stx.appendData("./data_wallet.xlsx", "Sheet1", row, 2, "True")
            var_stx.appendData("./data_wallet.xlsx", "Sheet1", row, 3, f"Có lệnh rút tiền chờ xác nhận: {maruttien}")
        else:
            var_stx.appendData("./data_wallet.xlsx", "Sheet1", row, 2, "False")
            var_stx.appendData("./data_wallet.xlsx", "Sheet1", row, 3, "Lỗi khác (có lệnh rút tiền chờ xác nhận).")


    def run_tc(self):
        wordbook = openpyxl.load_workbook('data_wallet.xlsx')
        sheet = wordbook.get_sheet_by_name("Sheet1")
        rownum = 1
        while (rownum < 5000):
            rownum += 1
            rownum = str(rownum)
            drive_wallet = sheet["A" + rownum].value
            print("Đang chạy tới hàng: {}, Ví lái xe: {}".format(int(rownum) - 1, drive_wallet))
            if drive_wallet == None:
                break

            # withdraw_money.tc1(self, drive_wallet, rownum)
            # print("Đã chạy xong tc1")
            #
            # result_tc1 = var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 250, 2)
            # if result_tc1 == "Cho phép tạo":
            #     withdraw_money.tc2(self, drive_wallet, rownum)
            #     print("Đã chạy xong tc2")
            #
            #     result_tc2 = int(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 251, 2))
            #     if result_tc2 != 0:
            #         withdraw_money.tc3(self, drive_wallet, rownum)
            #         print("Đã chạy xong tc3")
            #
            #         result_tc3 = var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 252, 2)
            #         if result_tc3 == "Không dữ liệu":
            #             withdraw_money.tc4(self, drive_wallet, rownum)
            #             print("Đã chạy xong tc4")
            #         if result_tc3 == "Có dữ liệu":
            #             withdraw_money.tc5(self, drive_wallet, rownum)
            #             print("Đã chạy xong tc5")
            try:
                withdraw_money.tc1(self, drive_wallet, rownum)
                print("Đã chạy xong tc1")

                result_tc1 = var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 250, 2)
                if result_tc1 == "Cho phép tạo":
                    withdraw_money.tc2(self, drive_wallet, rownum)
                    print("Đã chạy xong tc2")

                    result_tc2 = int(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 251, 2))
                    if result_tc2 != 0:
                        withdraw_money.tc3(self, drive_wallet, rownum)
                        print("Đã chạy xong tc3")

                        result_tc3 = var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 252, 2)
                        if result_tc3 == "Không dữ liệu":
                            withdraw_money.tc4(self, drive_wallet, rownum)
                            print("Đã chạy xong tc4")
                        if result_tc3 == "Có dữ liệu":
                            withdraw_money.tc5(self, drive_wallet, rownum)
                            print("Đã chạy xong tc5")
            except:
                module_other_stx.swich_tab_0()

            rownum = int(rownum)














