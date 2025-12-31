import logging

import customer_stx
import var_stx
import time
from selenium.webdriver.common.by import By
import module_other_stx
import login_stx
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
wait = WebDriverWait(var_stx.driver, 10)
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains


# chiều 31/12/2025


class accounting_14_1:


    def accounting_14_1_display_data(self, type):
        wait = WebDriverWait(var_stx.driver, 6)

        if type == "refresh":
            var_stx.driver.refresh()
            time.sleep(5)

        # try:
        #     var_stx.driver.find_element(By.XPATH, var_stx.reportrange).click()
        #     time.sleep(2)
        #     try:
        #         var_stx.driver.find_element(By.XPATH, var_stx.today).click()
        #     except:
        #         var_stx.driver.find_element(By.XPATH, var_stx.today1).click()
        #     time.sleep(2)
        #     var_stx.driver.find_element(By.XPATH, var_stx.Status1).click()
        #     time.sleep(1)
        #     var_stx.driver.find_element(By.XPATH, var_stx.search3).click()
        #     element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.ag3_2)))
        #     time.sleep(1.5)
        #     print("đã tìm hôm nay")
        # except:
        #     try:
        #         var_stx.driver.find_element(By.XPATH, var_stx.reportrange).click()
        #         time.sleep(2)
        #         try:
        #             var_stx.driver.find_element(By.XPATH, var_stx.yesterday).click()
        #         except:
        #             var_stx.driver.find_element(By.XPATH, var_stx.yesterday1).click()
        #         time.sleep(2)
        #         var_stx.driver.find_element(By.XPATH, var_stx.Status1).click()
        #         time.sleep(1)
        #         var_stx.driver.find_element(By.XPATH, var_stx.search3).click()
        #         element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.ag2_2)))
        #         time.sleep(1.5)
        #         print("đã tìm hôm qua")
        #     except:
        #         print("Không có bản ghi 14.1")

        if var_stx.linktest[0:23] == "https://g7test.staxi.vn":
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.reportrange)))
            element.click()
            time.sleep(2)

            try:
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
                time.sleep(0.5)
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day).send_keys("16/09/2025 00:00")
            except:
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day1).send_keys(Keys.CONTROL, "a", Keys.DELETE)
                time.sleep(0.5)
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day1).send_keys("16/09/2025 00:10")
            time.sleep(0.5)

            try:
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
                time.sleep(0.5)
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day).send_keys("16/09/2025 00:00")
            except:
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day1).send_keys(Keys.CONTROL, "a", Keys.DELETE)
                time.sleep(0.5)
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day1).send_keys("16/09/2025 00:10")
            time.sleep(0.5)
            try:
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_apply).click()
            except:
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_apply1).click()
            time.sleep(2)

            var_stx.driver.find_element(By.XPATH, var_stx.Status_notyetprocessed).click()
            time.sleep(1.5)
            var_stx.driver.find_element(By.XPATH, var_stx.search3).click()
            time.sleep(7)

        else:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.reportrange)))
            element.click()
            time.sleep(2)
            try:
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
                time.sleep(0.5)
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day).send_keys("12/06/2025 00:00")
            except:
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day1).send_keys(Keys.CONTROL, "a", Keys.DELETE)
                time.sleep(0.5)
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day1).send_keys("12/06/2025 00:00")
            time.sleep(0.5)

            try:
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
                time.sleep(0.5)
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day).send_keys("13/06/2025 23:00")
            except:
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day1).send_keys(Keys.CONTROL, "a", Keys.DELETE)
                time.sleep(0.5)
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day1).send_keys("13/06/2025 23:00")
            time.sleep(0.5)
            try:
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_apply).click()
            except:
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_apply1).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.Status_notyetprocessed).click()
            time.sleep(1.5)
            var_stx.driver.find_element(By.XPATH, var_stx.search3).click()
            time.sleep(7)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.accounting_1_DisplayPublicBookId)))
        except:
            pass





    def accounting_14_1(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.accounting).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.accounting_14_1).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.accounting).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.accounting_14_1).click()
        time.sleep(5)
        try:
            wait = WebDriverWait(var_stx.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.title_page)))
        except:
            pass
        module_other_stx.write_result_text_try_if(code, eventname, result, "KẾ TOÁN - 14.1 Quản lý xuất hoá đơn",
                                                  var_stx.title_page, "14.1 Quản lý xuất hoá đơn", "_QuanLyXuatHoaDon.png")

        accounting_14_1.accounting_14_1_display_data(self, "not refresh")



    def accounting_14_1_fromday_today(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.export_send)
        except:
            accounting_14_1.accounting_14_1(self, "", "", "")

        from_day = var_stx.driver.find_element(By.XPATH, var_stx.accounting_fromday2).text
        from_day_cv = datetime.strptime(from_day, "%H:%M %d/%m/%Y")
        from_day_cv = from_day_cv.strftime("%d/%m/%Y %H:%M")

        to_day = var_stx.driver.find_element(By.XPATH, var_stx.accounting_today2).text
        to_day_cv = datetime.strptime(to_day, "%H:%M %d/%m/%Y")
        to_day_cv = to_day_cv.strftime("%d/%m/%Y %H:%M")

        var_stx.driver.find_element(By.XPATH, var_stx.reportrange).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day).send_keys(from_day_cv)
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day).send_keys(from_day_cv)

        # var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        # time.sleep(0.5)
        # var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day).send_keys(to_day_cv)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.reportrange_apply).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.search3).click()
        time.sleep(2.5)

        module_other_stx.write_result_text_try_if(code, eventname, result, "KẾ TOÁN - 14.1 Quản lý xuất hoá đơn",
                                                  var_stx.accounting_fromday1, from_day, "_QuanLyXuatHoaDon_TuNgayDenNgay.png")

        # accounting_14_1.accounting_14_1_display_data(self, "refresh")



    def accounting_14_1_combobox(self, code, eventname, result, path_data, path_combobox, path_check, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.export_send)
        except:
            accounting_14_1.accounting_14_1(self, "", "", "")

        data = var_stx.driver.find_element(By.XPATH, path_data).text
        print(data)

        path_full_combobox = path_combobox + "//*[text()='"+data+"']"
        print(path_full_combobox)

        var_stx.driver.find_element(By.XPATH, path_full_combobox).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.search3).click()
        time.sleep(2.5)

        module_other_stx.write_result_text_try_if(code, eventname, result, "KẾ TOÁN - 14.1 Quản lý xuất hoá đơn",
                                                  path_check, data, name_image)
        accounting_14_1.accounting_14_1_display_data(self, "refresh")



    def accounting_14_1_input(self, code, eventname, result, path_data, path_input, path_check, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.export_send)
        except:
            accounting_14_1.accounting_14_1(self, "", "", "")

        if var_stx.linktest[0:17] == "https://g7staging":
            var_stx.driver.find_element(By.XPATH, var_stx.reportrange).click()
            time.sleep(2)
            try:
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
                time.sleep(0.5)
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day).send_keys("20/06/2025 00:00")
            except:
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day1).send_keys(Keys.CONTROL, "a", Keys.DELETE)
                time.sleep(0.5)
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day1).send_keys("20/06/2025 00:00")
            time.sleep(0.5)

            try:
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
                time.sleep(0.5)
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day).send_keys("21/06/2025 23:59")
            except:
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day1).send_keys(Keys.CONTROL, "a", Keys.DELETE)
                time.sleep(0.5)
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day1).send_keys("21/06/2025 23:59")
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.reportrange_apply).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.Status_0).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.search3).click()
            time.sleep(2.5)


        try:
            wait = WebDriverWait(var_stx.driver, 25)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, path_data)))
        except:
            pass
        data = var_stx.driver.find_element(By.XPATH, path_data).text
        print(data)
        var_stx.driver.find_element(By.XPATH, path_input).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search3).click()
        time.sleep(2.5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KẾ TOÁN - 14.1 Quản lý xuất hoá đơn",
                                                  path_check, data, name_image)

        accounting_14_1.accounting_14_1_display_data(self, "refresh")



    def accounting_14_1_other_input(self, code, eventname, result, id_data, path_input, path_check, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.export_send)
        except:
            accounting_14_1.accounting_14_1(self, "", "", "")

        n = 0
        while (n < 25):
            n += 1
            n = str(n)

            path_full_data = f"//div[@row-index='{n}']//div[@role='gridcell' and @col-id='{id_data}']"
            try:
                data = var_stx.driver.find_element(By.XPATH, path_full_data).text
                print(data)
                if data != "":
                    var_stx.driver.find_element(By.XPATH, path_input).send_keys(data)
                    time.sleep(1)
                    var_stx.driver.find_element(By.XPATH, var_stx.search3).click()
                    time.sleep(2.5)
                    module_other_stx.write_result_text_try_if(code, eventname, result, "KẾ TOÁN - 14.1 Quản lý xuất hoá đơn",
                                                              path_check, data, name_image)
                    accounting_14_1.accounting_14_1_display_data(self, "refresh")
                    break
            except:
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "Không có dữ liệu")
            n = int(n)



    def accounting_14_1_combobox_other(self, code, eventname, result, data, path_combobox, path_check, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.export_send)
        except:
            accounting_14_1.accounting_14_1(self, "", "", "")


        n = 0
        while (n < 25):
            n += 1
            n = str(n)
            path_full_combobox = path_combobox + "//*[text()='" + data + "']"
            print(path_full_combobox)
            try:
                var_stx.driver.find_element(By.XPATH, path_full_combobox).click()
                time.sleep(1)
                var_stx.driver.find_element(By.XPATH, var_stx.search3).click()
                time.sleep(2.5)

                logging.info("-------------------------")
                logging.info("KẾ TOÁN - 14.1 Quản lý xuất hoá đơn")
                logging.info("Mã - " + code)
                logging.info("Tên sự kiện - " + eventname)
                logging.info("Kết quả - " + result)
                print(path_check)
                try:
                    try:
                        check_text = var_stx.driver.find_element(By.XPATH, path_check).text
                    except:
                        scroll_bar = var_stx.driver.find_element(By.XPATH, "//*[@class='ag-body-horizontal-scroll-viewport']")
                        ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(800, 0).release().perform()
                        time.sleep(2)
                        check_text = var_stx.driver.find_element(By.XPATH, path_check).text
                    logging.info(check_text)
                    logging.info(data)
                    module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, check_text)

                    if check_text == data:
                        logging.info("True")
                        module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
                    else:
                        module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "Không có dữ liệu")
                        var_stx.driver.save_screenshot(var_stx.imagepath + code + name_image)
                        module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + name_image)
                except:
                    module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "Không có dữ liệu")
                    var_stx.driver.save_screenshot(var_stx.imagepath + code + name_image)
                    module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + name_image)

                break
            except:
                pass
            n = int(n)
        accounting_14_1.accounting_14_1_display_data(self, "refresh")



    def accounting_14_1_other_combobox(self, code, eventname, result, id_data, path_combobox, path_check, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.export_send)
        except:
            accounting_14_1.accounting_14_1(self, "", "", "")

        n = 0
        while (n < 25):
            n += 1
            n = str(n)

            path_full_data = f"//div[@row-index='{n}']//div[@role='gridcell' and @col-id='{id_data}']"
            print(path_full_data)
            try:
                data = var_stx.driver.find_element(By.XPATH, path_full_data).text
                print(data)
                if data != "":
                    path_full_combobox = path_combobox + "//*[text()='" + data + "']"
                    print(path_full_combobox)
                    var_stx.driver.find_element(By.XPATH, path_full_combobox).click()
                    time.sleep(1)
                    var_stx.driver.find_element(By.XPATH, var_stx.search3).click()
                    time.sleep(2.5)
                    try:
                        var_stx.driver.find_element(By.XPATH, path_check)
                    except:
                        scroll_bar = var_stx.driver.find_element(By.XPATH, "//*[@class='ag-body-horizontal-scroll-viewport']")
                        ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(800, 0).release().perform()
                        time.sleep(2)

                    module_other_stx.write_result_text_try_if(code, eventname, result, "KẾ TOÁN - 14.1 Quản lý xuất hoá đơn",
                                                              path_check, data, name_image)
                    accounting_14_1.accounting_14_1_display_data(self, "refresh")
                    break
            except:
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "Không có dữ liệu")
                scroll_bar = var_stx.driver.find_element(By.XPATH, "//*[@class='ag-body-horizontal-scroll-viewport']")
                ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(400, 0).release().perform()
                time.sleep(2)
            n = int(n)



    def accounting_14_1_search_advance(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.export_send)
        except:
            accounting_14_1.accounting_14_1(self, "", "", "")


        var_stx.driver.find_element(By.XPATH, var_stx.search_advanced).click()
        time.sleep(2.5)

        var_stx.driver.find_element(By.XPATH, var_stx.search_advanced_BookCodeSearch).send_keys("00007BB2")#Tìm nhiều mã cuốc khách
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search_advanced_address_from).send_keys("Lê Hồng Phong, P. Đằng Lâm, Q. Hải An, TP. Hải Phòng") #Điểm đón
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search_advanced_address_to).send_keys("44/3 Lê Thái Tổ, Hàng Trống") #Điểm trả
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search_advanced_StringSourceType).click()#Loại cuốc
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search_advanced_promotion).send_keys("AUTO12AV") #Mã khuyến mại
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search_advanced_name_driver).send_keys("Trần Quang trường") #Tên lái xe
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search_advanced_number).send_keys("1922") #Số hiệu
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search_advanced_phone1).send_keys("0928264397") #Số điện thoại
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search_advanced_liscense_plate).send_keys("29k103465") #Biển số xe
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search_advanced_customer).send_keys("Vương Phú Qúy") #Khách hàng
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search_advanced_phone2).send_keys("0928264009") #Số điện thoại
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search_advanced_serial).send_keys("9999920985636338") #Serial
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search_advanced_hd).send_keys("HOPDONGMACDINH") #Hợp đồng
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search_advanced_type_hd).click()#Loại hợp đồng
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search_advanced_from_to_day).click()#Thời gian dùng thẻ
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search_advanced_delete)
        var_stx.driver.find_element(By.XPATH, var_stx.search_advanced_search)

        module_other_stx.write_result_text_try_if(code, eventname, result, "KẾ TOÁN - 14.1 Quản lý xuất hoá đơn",
                                                  var_stx.search_advanced_tite, "Bộ lọc nâng cao", "_QuanLyXuatHoaDon_TimKiemNangCao.png")

        var_stx.driver.find_element(By.XPATH, var_stx.search_advanced_x).click()
        time.sleep(2)



    def accounting_14_1_search_advance_delete(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.export_send)
        except:
            accounting_14_1.accounting_14_1(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.BookCodeSearch).send_keys("00007BB2")
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search3).click()
        time.sleep(2.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search_advance_delete).click()
        time.sleep(2)
        module_other_stx.write_result_text_try_if_value(code, eventname, result, "KẾ TOÁN - 14.1 Quản lý xuất hoá đơn",
                                                  var_stx.BookCodeSearch, "", "_QuanLyXuatHoaDon_XoaBoLoc.png")

        accounting_14_1.accounting_14_1_display_data(self, "refresh")



    def accounting_14_1_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.export_send)
            var_stx.driver.find_element(By.XPATH, var_stx.accounting_2_Source)
        except:
            accounting_14_1.accounting_14_1(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        time.sleep(7)

        module_other_stx.write_result_dowload_file(code, eventname, result, "KẾ TOÁN - 14.1 Quản lý xuất hoá đơn",
                                                        "_QuanLyXuatHoaDon_Excel.xlsx", "_QuanLyXuatHoaDon_XuatExcel.png")



    def accounting_14_1_button(self, code, eventname, result, type, button, path_check, desire1, desire2, name_image):
        var_stx.driver.implicitly_wait(0.5)
        wait = WebDriverWait(var_stx.driver, 25)

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.export_send)
            var_stx.driver.refresh()
            time.sleep(5)
        except:
            accounting_14_1.accounting_14_1(self, "", "", "")

        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.reportrange)))
            element.click()
        except:
            var_stx.driver.refresh()
            time.sleep(6)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.reportrange)))
            element.click()
        time.sleep(2)
        print(var_stx.linktest[0:23])

        if var_stx.linktest[0:23] == "https://g7test.staxi.vn":

            try:
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
                time.sleep(0.5)
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day).send_keys("27/07/2025 00:00")
            except:
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day1).send_keys(Keys.CONTROL, "a", Keys.DELETE)
                time.sleep(0.5)
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day1).send_keys("27/07/2025 00:00")
            time.sleep(0.5)

            try:
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
                time.sleep(0.5)
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day).send_keys("28/07/2025 23:59")
            except:
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day1).send_keys(Keys.CONTROL, "a", Keys.DELETE)
                time.sleep(0.5)
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day1).send_keys("28/07/2025 23:59")
            time.sleep(0.5)
            try:
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_apply).click()
            except:
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_apply1).click()
            time.sleep(2)

            var_stx.driver.find_element(By.XPATH, var_stx.Status_notyetprocessed).click()
            time.sleep(1.5)
            # var_stx.driver.find_element(By.XPATH, var_stx.BookCodeSearch).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            # time.sleep(0.5)
            # var_stx.driver.find_element(By.XPATH, var_stx.BookCodeSearch).send_keys("00001456")
            # time.sleep(0.5)

        else:
            try:
                logging.info("n0")
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
                time.sleep(0.5)
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day).send_keys("04/08/2025 00:00")
                logging.info("n1")
            except:
                logging.info("n2")
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day1).send_keys(Keys.CONTROL, "a", Keys.DELETE)
                time.sleep(0.5)
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day1).send_keys("04/08/2025 00:00")
                logging.info("n3")
            time.sleep(0.5)

            try:
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
                time.sleep(0.5)
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day).send_keys("05/08/2025 23:59")
                logging.info("n4")
            except:
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day1).send_keys(Keys.CONTROL, "a", Keys.DELETE)
                time.sleep(0.5)
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day1).send_keys("05/08/2025 23:59")
                logging.info("n5")
            time.sleep(0.5)
            try:
                logging.info("n6")
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_apply).click()
            except:
                var_stx.driver.find_element(By.XPATH, var_stx.reportrange_apply1).click()
                logging.info("n7")
            time.sleep(2)
            logging.info("n8")
            var_stx.driver.find_element(By.XPATH, var_stx.Status_notyetprocessed).click()
            time.sleep(1.5)

        if type == "3":
            var_stx.driver.find_element(By.XPATH, var_stx.InvoiceType_customer).click()
            time.sleep(1.5)

        var_stx.driver.find_element(By.XPATH, var_stx.search3).click()
        logging.info("n11")
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.accounting_1_DisplayPublicBookId)))
        time.sleep(1)
        logging.info("n12")
        var_stx.driver.implicitly_wait(5)
        n = 0
        while (n < 21):
            n = n + 1
            n = str(n)
            path_checkbox = "//*[@name='left']/div[" + n + "]//*[@type='checkbox']"

            try:
                logging.info("n13")
                var_stx.driver.find_element(By.XPATH, path_checkbox).click()
                time.sleep(1)
                var_stx.driver.find_element(By.XPATH, button).click()
                logging.info("n14")
                time.sleep(2.5)
                if type == "1":
                    module_other_stx.write_result_text_try_if_or(code, eventname, result, "KẾ TOÁN - 14.1 Quản lý xuất hoá đơn",
                                                                    path_check, desire1, desire2, name_image)
                if type == "2":
                    module_other_stx.write_result_text_try_if(code, eventname, result, "KẾ TOÁN - 14.1 Quản lý xuất hoá đơn",
                                                                    path_check, desire1, name_image)
                    var_stx.driver.find_element(By.XPATH, var_stx.note).send_keys("Ghi chú chọn button Không xuất hóa đơn")


                if (name_image == "_QuanLyXuatHoaDon_XuatHoaDonKhachLe.png") or (name_image == "_QuanLyXuatHoaDon_KhongXuatHoa.png"):
                    var_stx.driver.refresh()
                    time.sleep(5)
                    logging.info("n15")
                break

            except:
                pass
            n = int(n)






    def accounting_14_1_export_invoice_fillinfo(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        # try:
        #     var_stx.driver.find_element(By.XPATH, var_stx.check_export_invoice)
        # except:

        accounting_14_1.accounting_14_1_button(self, "", "", "", "3", var_stx.export_invoice,
                                               "", "",  "", "")

        #khách hàng doanh nghiệp
        var_stx.driver.find_element(By.XPATH, var_stx.individual_kh_company_checkbox).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_email).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_email).send_keys("truongvck22@gmail.com")
        time.sleep(0.5)
        # var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_VAT)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_tax_code).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_tax_code).send_keys("8338123381")
        time.sleep(0.5)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_name_business).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_name_business).send_keys("Công ty TNHH Kinh Tập")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_address).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_address).send_keys("910 Đ. Kim Giang, Thanh Liệt, Thanh Trì, Hà Nội, Việt Nam")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_fullname).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_fullname).send_keys("Vương Phú Quý")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_phone).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_phone).send_keys("0826473154")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_serial).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_serial).send_keys("9999920987715201")
        time.sleep(0.5)
        if var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_pay_sec).is_selected() == False:
            var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_pay_sec).click()

        # var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_pay_sec).click()
        time.sleep(1.5)

        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_hd).click()
        time.sleep(1.5)
        # var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_hd1).click()
        # time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_serial_sec).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_serial_sec).send_keys("020200004314")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_not_export_invoice)
        # var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_export_customer) 0ECDC593-A101-4396-9763-3D2EFEC305B7      21/10
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_send_info)




        #KH cá nhân (không có MST)
        var_stx.driver.find_element(By.XPATH, var_stx.individual_customers_checkbox).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_email).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_email).send_keys("truongvck111@gmail.com")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_fullname).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_fullname).send_keys("Lã Thanh")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_cccd).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_cccd).send_keys("020200009822")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_address).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_address).send_keys("980 Đ. Kim Giang, Thanh Liệt, Thanh Trì, Hà Nội, Việt Nam")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_phone).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_phone).send_keys("0826473155")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_serial).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_serial).send_keys("9999920987715202")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.save4).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.confirm).click()
        except:
            pass
        try:
            var_stx.driver.implicitly_wait(0.3)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.invoice_save)))
            logging.info(element)
            module_other_stx.write_result_text_try_if(code, eventname, result, "KẾ TOÁN - 14.1 Quản lý xuất hoá đơn",
                                                      var_stx.invoice_save, "Lưu thông tin thành công!", "_QuanLyXuatHoaDon_Luu.png")
        except:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.toast_message)))
            logging.info(element)
            module_other_stx.write_result_text_try_if(code, eventname, result, "KẾ TOÁN - 14.1 Quản lý xuất hoá đơn",
                                                      var_stx.toast_message, "Lưu thông tin thành công!", "_QuanLyXuatHoaDon_Luu.png")


        try:
            var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_cancel).click()
        except:
            pass
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_x).click()
        except:
            pass
        time.sleep(2)



    def select_icon(self, fromday, today, col_id):
        try:
            var_stx.driver.find_element(By.XPATH, "//*[@name='left']/div[1]//*[@type='checkbox']")
        except:
            accounting_14_1.accounting_14_1(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.reportrange).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day).send_keys(fromday)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day1).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day1).send_keys(fromday)
        time.sleep(0.5)

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day).send_keys(today)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day1).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day1).send_keys(today)
        time.sleep(0.5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.reportrange_apply).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.reportrange_apply1).click()
        time.sleep(2)

        var_stx.driver.find_element(By.XPATH, var_stx.Status_notyetprocessed).click()
        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search3).click()
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.accounting_2_DisplayPublicBookId)))
        time.sleep(1)


        n = -1
        while (n < 30):
            n = n + 1
            n = str(n)
            path_icon = f"//div[@row-index='{n}']//div[@role='gridcell' and @col-id='{col_id}']/span/a/img"
            try:
                var_stx.driver.find_element(By.XPATH, path_icon).click()
                time.sleep(2.5)
                break
            except:
                pass
            n = int(n)



    def accounting_14_1_icon(self, code, eventname, result, src, path_check, desire, name_image):
        var_stx.driver.implicitly_wait(5)
        accounting_14_1.select_icon(self, "26/05/2025 00:00", "27/05/2025 10:59", src)

        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.info_invoice_actual_revenue)))
        except:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.info_invoice_actual_revenue1)))
        element.send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)

        var_stx.driver.execute_script("arguments[0].value = '60000'; arguments[0].dispatchEvent(new Event('input'));", element)

        # element.send_keys("60000")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_address_from).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_address_from).send_keys("1 Đ. Đại Cồ Việt, Bách Khoa, Hai Bà Trưng, Hà Nội, Việt Nam")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_address_to).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_address_to).send_keys("120 P. Nguyễn Văn Viên, Vĩnh Phú, Hai Bà Trưng, Hà Nội, Việt Nam")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_note).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_note).send_keys("Test ghi chú xuất hóa đơn")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_confirm).click()
        time.sleep(2.5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KẾ TOÁN - 14.1 Quản lý xuất hoá đơn",
                                                  path_check, desire, name_image)

        # module_other_stx.write_result_text_try_if(code, eventname, result, "KẾ TOÁN - 14.1 Quản lý xuất hoá đơn",
        #                                           var_stx.swal2_title, "Thay đổi thông tin xuất hóa đơn", "_QuanLyXuatHoaDon_GuiThongTin.png")
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_x1).click()
            time.sleep(2.5)
        except:
            pass



    def select_electronic_invoice(self, name):
        n = -1
        while (n < 30):
            n = n + 1
            n = str(n)
            path_icon = f"//div[@row-index='{n}']//div[@role='gridcell' and @col-id='InvoiceLink']/span/a"
            try:
                status_button = var_stx.driver.find_element(By.XPATH, path_icon).text
                print(status_button)
                if status_button == name:
                    var_stx.driver.find_element(By.XPATH, path_icon).click()
                    time.sleep(5)
                    break
            except:
                pass
            n = int(n)



    def accounting_14_1_electronic_invoice(self, code, eventname, result, name):
        var_stx.driver.implicitly_wait(0.5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.export_send)
            accounting_14_1.accounting_14_1_display_data(self, "not refresh")
        except:
            accounting_14_1.accounting_14_1(self, "", "", "")

        accounting_14_1.select_electronic_invoice(self, name)
        if name == "Xem HĐ ":
            try:
                var_stx.driver.switch_to.window(var_stx.driver.window_handles[1])
                time.sleep(2)
                module_other_stx.write_result_not_displayed_try(code, eventname, result, "KẾ TOÁN - 14.1 Quản lý xuất hoá đơn",
                                                          var_stx.export_send, "_QuanLyXuatHoaDon_XemHD.png")
                var_stx.driver.switch_to.window(var_stx.driver.window_handles[0])
                time.sleep(2)
                curr = var_stx.driver.current_window_handle
                for handle in var_stx.driver.window_handles:
                    if handle != curr:
                        var_stx.driver.switch_to.window(handle)
                        var_stx.driver.close()
                        time.sleep(1)
                var_stx.driver.switch_to.window(curr)
                time.sleep(1)
            except:
                var_stx.driver.switch_to.window(var_stx.driver.window_handles[0])
                time.sleep(2)
                logging.info("False")
                var_stx.driver.save_screenshot(var_stx.imagepath + code + "_QuanLyXuatHoaDon_XemHD.png")
                # module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_QuanLyXuatHoaDon_XemHD.png")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "Không có dữ liệu")



        if name == "Xuất lại ":
            try:
                var_stx.driver.find_element(By.XPATH, var_stx.check_export_invoice)
                module_other_stx.write_result_text_try_if_or(code, eventname, result, "KẾ TOÁN - 14.1 Quản lý xuất hoá đơn",
                                                          var_stx.check_export_invoice, "Cuốc khách không đủ điều kiện xuất hóa đơn",
                                                             "Thông tin xuất hóa đơn", "_QuanLyXuatHoaDon_XuatLai.png")
                try:
                    var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_x).click()
                except:
                    var_stx.driver.find_element(By.XPATH, var_stx.i_understand).click()
                    time.sleep(2.5)
            except:
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "Không có dữ liệu")

        if name == "Xem " or name == "Xuất ":
            try:
                var_stx.driver.find_element(By.XPATH, var_stx.check_export_invoice)
                module_other_stx.write_result_text_try_if_or(code, eventname, result, "KẾ TOÁN - 14.1 Quản lý xuất hoá đơn",
                                                          var_stx.check_export_invoice, "Cuốc khách không đủ điều kiện xuất hóa đơn",
                                                             "Thông tin xuất hóa đơn", "_QuanLyXuatHoaDon_XuatLai.png")
                var_stx.driver.find_element(By.XPATH, var_stx.info_invoice_x).click()
                time.sleep(2.5)
            except:
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "Không có dữ liệu")



    def accounting_14_1_link_icon(self, code, eventname, result, path_icon, path_check, desire, name_image):
        var_stx.driver.implicitly_wait(0.5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.accounting_1_Source)
        except:
            accounting_14_1.accounting_14_1(self, "", "", "")


        var_stx.driver.find_element(By.XPATH, var_stx.view_more1).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, path_icon).click()
        time.sleep(2)
        var_stx.driver.switch_to.window(var_stx.driver.window_handles[1])
        time.sleep(2)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, path_check)))
            time.sleep(1.5)
        except:
            pass

        if name_image == "_QuanLyXuatHoaDon_LotrinhGPS.png":
            module_other_stx.write_result_not_displayed_try(code, eventname, result, "KẾ TOÁN - 14.1 Quản lý xuất hoá đơn",
                                                      path_check, name_image)

        else:
            module_other_stx.write_result_text_try_if_in(code, eventname, result, "KẾ TOÁN - 14.1 Quản lý xuất hoá đơn",
                                                            path_check, desire, name_image)

        var_stx.driver.switch_to.window(var_stx.driver.window_handles[0])
        time.sleep(2)
        curr = var_stx.driver.current_window_handle
        for handle in var_stx.driver.window_handles:
            if handle != curr:
                var_stx.driver.switch_to.window(handle)
                var_stx.driver.close()
                time.sleep(1)
        var_stx.driver.switch_to.window(curr)
        time.sleep(1)











    def accounting_14_1_info_order(self, code, eventname, result):
        var_stx.driver.implicitly_wait(0.5)
        accounting_14_1.accounting_14_1(self, "", "", "")
        #abc
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.reportrange)))
        element.click()
        time.sleep(2)

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day).send_keys(Keys.CONTROL, "a",Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day).send_keys("05/10/2025 00:00")
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day1).send_keys(Keys.CONTROL, "a",Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.reportrange_from_day1).send_keys("05/10/2025 00:00")
        time.sleep(0.5)

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day).send_keys("06/10/2025 23:59")
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day1).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.reportrange_to_day1).send_keys("06/10/2025 23:59")
        time.sleep(0.5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.reportrange_apply).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.reportrange_apply1).click()
        time.sleep(2)

        # var_stx.driver.find_element(By.XPATH, var_stx.Source_dieuhanh).click()
        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search3).click()
        time.sleep(7)
        var_stx.driver.find_element(By.XPATH, var_stx.accounting_1_DisplayPublicBookId).click()
        time.sleep(2.5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KẾ TOÁN - 14.1 Quản lý xuất hoá đơn - Thông tin cuốc",
                                                  var_stx.info_order, "Thông tin cuốc", "_QuanLyXuatHoaDon_ThongTinCuoc.png")


    def check_accounting_14_1_info_order(self, code, eventname, result, type, type_value,  path_name, path_data, desire_name, name_image):
        var_stx.driver.implicitly_wait(0.5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.info_order)
        except:
            accounting_14_1.accounting_14_1_info_order(self, "", "", "")

        logging.info("-------------------------")
        logging.info("KẾ TOÁN - 14.1 Quản lý xuất hoá đơn - Thông tin cuốc")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)

        if type == "0":
            try:
                name = var_stx.driver.find_element(By.XPATH, path_name).text
                if type_value == "text":
                    data = var_stx.driver.find_element(By.XPATH, path_data).text
                else:
                    data = var_stx.driver.find_element(By.XPATH, path_data).get_attribute("value")
                logging.info(name)
                logging.info(data)
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, f"name: {name}\ndata: {data}")

                if name == desire_name:
                    logging.info("True")
                    module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    logging.info("False")
                    var_stx.driver.save_screenshot(var_stx.imagepath + code + name_image)
                    module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                    module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + name_image)
            except:
                logging.info("False")
                var_stx.driver.save_screenshot(var_stx.imagepath + code + name_image)
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + name_image)


        if type == "1":
            try:
                name = var_stx.driver.find_element(By.XPATH, path_name).text
                if type_value == "text":
                    data = var_stx.driver.find_element(By.XPATH, path_data).text
                else:
                    data = var_stx.driver.find_element(By.XPATH, path_data).get_attribute("value")
                logging.info(name)
                logging.info(data)
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, f"name: {name}\ndata: {data}")

                if (name == desire_name) and (data != ""):
                    logging.info("True")
                    module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    logging.info("False")
                    var_stx.driver.save_screenshot(var_stx.imagepath + code + name_image)
                    module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                    module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + name_image)
            except:
                logging.info("False")
                var_stx.driver.save_screenshot(var_stx.imagepath + code + name_image)
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + name_image)


        if type == "2":
            try:
                name = var_stx.driver.find_element(By.XPATH, path_name).text
                if type_value == "text":
                    data = var_stx.driver.find_element(By.XPATH, path_data).text
                else:
                    data = var_stx.driver.find_element(By.XPATH, path_data).get_attribute("value")
                logging.info(name)
                logging.info(data)
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, f"name: {name}\ndata: {data}")

                if (name == desire_name) and (data != ""):
                    logging.info("True")
                    module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
            except:
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "Không có dữ liệu")


        if type == "3":
            try:
                name = var_stx.driver.find_element(By.XPATH, path_name).text
                try:
                    data = var_stx.driver.find_element(By.XPATH, path_data).text
                    module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, f"name: {name}\ndata: {data}")
                    if (name == desire_name) and (data != ""):
                        logging.info("True")
                        module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
                except:
                    logging.info(name)
                    module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, f"name: {name}\ndata:")
                    if (name == desire_name):
                        logging.info("True")
                        module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
            except:
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "Không có dữ liệu")



    def check_accounting_14_1_info_order_history(self, code, eventname, result):
        var_stx.driver.implicitly_wait(0.5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.info_order)
        except:
            accounting_14_1.accounting_14_1_info_order(self, "", "", "")


        var_stx.driver.find_element(By.XPATH, var_stx.history).click()
        time.sleep(2)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KẾ TOÁN - 14.1 Quản lý xuất hoá đơn - Thông tin cuốc(Lịch sử)",
                                                  var_stx.Agent, "Tác nhân", "_QuanLyXuatHoaDon_ThongTinCuoc_LichSuCuoc.png")

        var_stx.driver.find_element(By.XPATH, var_stx.close3).click()
        time.sleep(2.5)






