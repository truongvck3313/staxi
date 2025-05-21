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














class list_wallet_driver:



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
        time.sleep(5)
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

        var_stx.driver.find_element(By.XPATH, var_stx.list_wallet_driver_search_inpuut).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.list_wallet_driver_search_inpuut).send_keys("batonnt1")
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
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


    def list_wallet_driver_search(self, code, eventname, result, path_data, path_check, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_wallet_driver)
        except:
            list_wallet_driver.list_wallet_driver(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.list_wallet_driver_search_inpuut).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.list_wallet_driver_search_inpuut).send_keys("09874")
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(7)
        try:
            var_stx.driver.implicitly_wait(0.3)
            var_stx.driver.find_element(By.XPATH, var_stx.list_data3_4)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.list_wallet_driver_search_inpuut).clear()
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(5)

        data = var_stx.driver.find_element(By.XPATH, path_data).text
        var_stx.driver.find_element(By.XPATH, var_stx.list_wallet_driver_search_inpuut).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.list_wallet_driver_search_inpuut).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(7)

        module_other_stx.write_result_text_try_if(code, eventname, result, "VÍ LÁI XE - 3.1 Danh sách ví lái xe",
                                                  path_check, data, name_image)


    def list_wallet_driver_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")

        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_wallet_driver)
        except:
            list_wallet_driver.list_wallet_driver(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.list_wallet_driver_search_inpuut).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.list_wallet_driver_search_inpuut).send_keys("09874")
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(7)
        var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        time.sleep(6)
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



        minitor_stx.get_info_web()
        try:
            minitor_stx.get_info_excel1(5, "Sheet 1")
        except:
            print("n1")
            var_stx.driver.refresh()
            time.sleep(7)
            var_stx.driver.find_element(By.XPATH, var_stx.list_wallet_driver_search_inpuut).clear()
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.list_wallet_driver_search_inpuut).send_keys("09874")
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(7)
            var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
            time.sleep(7)
            minitor_stx.get_info_web()
            minitor_stx.get_info_excel1(5, "Sheet 1")
            print("n2")
        minitor_stx.check_info_web_excel(code, eventname, result, "VÍ LÁI XE - 3.1 Danh sách ví lái xe")


    def list_wallet_driver_recharge(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_wallet_driver)
        except:
            list_wallet_driver.list_wallet_driver(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.list_wallet_driver_search_inpuut).clear()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.list_wallet_driver_search_inpuut).send_keys(var_stx.data['wallet']['search'])
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
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

        var_stx.driver.find_element(By.XPATH, var_stx.list_wallet_driver_search_inpuut).clear()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.list_wallet_driver_search_inpuut).send_keys(var_stx.data['wallet']['search'])
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
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

        var_stx.driver.find_element(By.XPATH, var_stx.list_wallet_driver_search_inpuut).clear()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.list_wallet_driver_search_inpuut).send_keys(var_stx.data['wallet']['search'])
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
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
        time.sleep(5)
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
        var_stx.driver.find_element(By.XPATH, var_stx.recharge_account).send_keys(var_stx.data['wallet']['search'])
        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.recharge_account1).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.recharge_money1).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.recharge_money1).send_keys(var_stx.data['wallet']['recharge_monney1'])
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
        time.sleep(5)
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
        var_stx.driver.find_element(By.XPATH, var_stx.recharge_account).send_keys(var_stx.data['wallet']['search'])
        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.recharge_account1).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.recharge_money1).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.recharge_money1).send_keys(var_stx.data['wallet']['withdraw_monney2'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.recharge_note).send_keys(var_stx.data['wallet']['note2'])
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
            # var_stx.driver.find_element(By.XPATH, var_stx.from_day).clear()
            # var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(Keys.CONTROL + "a")
            # var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(Keys.BACKSPACE)
            tu_ngay = var_stx.driver.find_element(By.XPATH, var_stx.from_day)
            var_stx.driver.execute_script("arguments[0].value = '';", tu_ngay)
            time.sleep(0.2)
        except:
            pass

        time.sleep(1.5)
        try:
            # var_stx.driver.find_element(By.XPATH, var_stx.to_day).clear()
            # var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(Keys.CONTROL + "a")
            # var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(Keys.BACKSPACE)
            den_ngay = var_stx.driver.find_element(By.XPATH, var_stx.to_day)
            var_stx.driver.execute_script("arguments[0].value = '';", den_ngay)
            time.sleep(0.2)
        except:
            pass

        time.sleep(1)

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.transaction_confirmation_x3).clear()
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
        time.sleep(5)
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
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "VÍ LÁI XE - 3.5 Lịch sử ví tiền",
                                                 var_stx.title_page, "3.5 Lịch sử ví tiền", "_LichSuViTien.png")


    def wallet_history_x(self):
        var_stx.driver.implicitly_wait(0.2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.from_day).clear()
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.to_day).clear()
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.driver_sdt).clear()
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.code_dam).clear()
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.code_gd).clear()
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
        # var_stx.driver.find_element(By.XPATH, var_stx.name_driver_sdt).clear()
        # time.sleep(0.5)
        # var_stx.driver.find_element(By.XPATH, var_stx.name_driver_sdt).send_keys("bathao")
        # time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        scroll_bar = var_stx.driver.find_element(By.XPATH, "//*[@class='ag-body-horizontal-scroll-viewport']")
        try:
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(800, 0).release().perform()
        except:
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(400, 0).release().perform()
            time.sleep(1)
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(400, 0).release().perform()

        time.sleep(2)
        n = 0
        while (n < 5):
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
                except:
                    pass
            n = int(n)


        n = 0
        while (n < 25):
            n = n + 1
            n = str(n)
            path_icon = "//*[@class='ag-center-cols-viewport']/div/div[" + n + "]//*[@class='fa fa-angle-double-right']"
            try:
                var_stx.driver.find_element(By.XPATH, path_icon).click()
                time.sleep(5)
                var_stx.driver.switch_to.window(var_stx.driver.window_handles[1])
                time.sleep(3)
                wait = WebDriverWait(var_stx.driver, 20)
                element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.table_1_1)))
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


        var_stx.driver.find_element(By.XPATH, var_stx.export_excel6).click()
        time.sleep(7)
        report_stx.get_info_web4()
        try:
            minitor_stx.get_info_excel1(5, "Sheet 1")
        except:
            var_stx.driver.refresh()
            time.sleep(7)
            var_stx.driver.find_element(By.XPATH, var_stx.export_excel6).click()
            time.sleep(7)
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








