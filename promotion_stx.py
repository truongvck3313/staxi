import logging
import var_stx
import time
from selenium.webdriver.common.by import By
import module_other_stx
import login_stx
import minitor_stx
import vehicle_driver_stx
from retry import retry
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import openpyxl
from selenium.webdriver.common.keys import Keys
wait = WebDriverWait(var_stx.driver, 10)
#18/12


def get_info_web():
    var_stx.driver.implicitly_wait(0.05)
    row = 119
    n = 0
    while (n < 50):
        n += 1
        n = str(n)
        row += 1
        path_column = "//*[@class='table table-hover table-bordered cf']/thead/tr/th[" + n + "]"
        path_data = "//*[@class='table table-hover table-bordered cf']/tbody/tr[1]/td[" + n + "]"
        print(n)
        try:
            name_colum = var_stx.driver.find_element(By.XPATH, path_column).text
            name_data = var_stx.driver.find_element(By.XPATH, path_data).text
            print("ten cot web:" .format(name_colum))
            print("data cot web:" .format(name_data))
            var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", row, 1, name_colum)
            var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", row, 2, name_data)
        except:
            pass
        n = int(n)


def get_info_web1():
    var_stx.driver.implicitly_wait(0.05)
    row = 119
    n = 0
    while (n < 50):
        n += 1
        n = str(n)
        row += 1
        path_column = "//*[@class='table table-hover table-bordered  cf']/thead/tr/th[" + n + "]"
        path_data = "//*[@class='table table-hover table-bordered  cf']/tbody/tr[1]/td[" + n + "]"
        print(n)
        try:
            name_colum = var_stx.driver.find_element(By.XPATH, path_column).text
            name_data = var_stx.driver.find_element(By.XPATH, path_data).text
            print("ten cot web:" .format(name_colum))
            print("data cot web:" .format(name_data))
            var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", row, 1, name_colum)
            var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", row, 2, name_data)
        except:
            pass
        n = int(n)







class list_promotion:


    def list_promotion(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.list_promotion).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.list_promotion).click()
        time.sleep(2)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.title_page)))
            time.sleep(2)
        except:
            pass
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.1 Danh sách khuyến mại",
                                                  var_stx.title_page, "6.1 Danh sách khuyến mại", "_DanhSachKhuyenmai.png")


    def list_promotion_g7_test(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx_g7test(self, var_stx.data['login']['tk_admin_test'],  var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.list_promotion).click()
        time.sleep(2.5)


    def list_promotion_x(self):
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
            var_stx.driver.find_element(By.XPATH, var_stx.name).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.3)
        except:
            pass


    def list_promotion_from_to_day(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_promotion)
        except:
            list_promotion.list_promotion(self, "", "", "")

        list_promotion.list_promotion_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)


        var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(var_stx.data['promotion']['from_day'])
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(var_stx.data['promotion']['to_day'])
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if_cut2(code, eventname, result, "VÍ LÁI XE - 3.5 Lịch sử ví tiền",
                                              var_stx.table_1_7, "21/8/2024", "_DanhSachKhuyenmai_TuNgayDenNgay.png", 0, 9)


    def list_promotion_search(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_promotion)
        except:
            list_promotion.list_promotion(self, "", "", "")

        list_promotion.list_promotion_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(7)

        try:
            wait = WebDriverWait(var_stx.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.col_id_name3)))
        except:
            pass

        name = var_stx.driver.find_element(By.XPATH, var_stx.col_id_name3).text
        var_stx.driver.find_element(By.XPATH, var_stx.name).send_keys(name)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "VÍ LÁI XE - 3.5 Lịch sử ví tiền",
                                              var_stx.col_id_name2, name, "_DanhSachKhuyenmai_Ten.png")


    def list_promotion_add_new(self, code, eventname, result, type_promotion, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_promotion)
        except:
            list_promotion.list_promotion(self, "", "", "")


        vehicle_driver_stx.increase()
        number = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 7, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_file_other).click()#icon thêm mới
        time.sleep(1)
        wait = WebDriverWait(var_stx.driver, 12)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.PromoteTypeID)))
        time.sleep(2)


        try:
            var_stx.driver.find_element(By.XPATH, var_stx.PromoteTypeID).click()
        except:
            var_stx.driver.refresh()
            time.sleep(5)
            var_stx.driver.find_element(By.XPATH, var_stx.PromoteTypeID).click()

        time.sleep(1.5)
        if type_promotion == "Khuyến mại chung":
            var_stx.driver.find_element(By.XPATH, var_stx.type_promotion0).click()
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.promotion_continue).click()
            time.sleep(2.5)
            var_stx.driver.find_element(By.XPATH, var_stx.promotion_add_new_name).send_keys("Auto_KM_Chung"+number)
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 14, "Auto_KM_Chung"+number)
            var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 23, 2, "Auto_KM_Chung" + number)

        if type_promotion == "Khuyến mại riêng":
            var_stx.driver.find_element(By.XPATH, var_stx.type_promotion1).click()
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.promotion_continue).click()
            time.sleep(2.5)
            var_stx.driver.find_element(By.XPATH, var_stx.promotion_add_new_name).send_keys("Auto_KM_Rieng"+number)
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 14, "Auto_KM_Rieng"+number)
        var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 23, 3, "Auto_KM_Rieng"+number)


        time.sleep(0.5)
        iframe = var_stx.driver.find_element(By.XPATH, var_stx.promotion_add_new_conten)
        var_stx.driver.switch_to.frame(iframe)
        content_area = var_stx.driver.find_element(By.XPATH, var_stx.promotion_add_new_conten_body)
        content_area.send_keys(var_stx.data['promotion']['conten'])
        var_stx.driver.switch_to.default_content()
        time.sleep(1)

        var_stx.driver.find_element(By.XPATH, var_stx.promotion_add_new_notification).send_keys(var_stx.data['promotion']['notification'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.promotion_add_new_explanation).send_keys(var_stx.data['promotion']['explanation'])    #giải trình
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.promotion_add_new_image).send_keys(var_stx.data['promotion']['image1'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.promotion_add_new_banner).send_keys(var_stx.data['promotion']['image2'])
        time.sleep(0.5)

        #Kiểu hiển thị
        if type_promotion == "Khuyến mại chung":
            var_stx.driver.find_element(By.XPATH, var_stx.type_display0).click()    #mặc định
        if type_promotion == "Khuyến mại riêng":
            var_stx.driver.find_element(By.XPATH, var_stx.type_display1).click()    #Khuyến mại nổi bật
        time.sleep(1.5)


        #Thời gian
        if type_promotion == "Khuyến mại chung":
            var_stx.driver.find_element(By.XPATH, var_stx.reportrange).click()  #Từ ngày đến ngày
            time.sleep(1.5)
            var_stx.driver.find_element(By.XPATH, var_stx.daterangepicker_start).send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.daterangepicker_start).send_keys(var_stx.data['promotion']['time_start'])
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.daterangepicker_end).send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.daterangepicker_end).send_keys(var_stx.data['promotion']['time_end'])
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.apply).click()
            time.sleep(1.5)
            var_stx.driver.find_element(By.XPATH, var_stx.promotion_add_new_image).click()

        if type_promotion == "Khuyến mại riêng":
            #Giờ trong ngày
            var_stx.driver.find_element(By.XPATH, var_stx.HourOfDay_chosen).click()
            time.sleep(1.5)
            var_stx.driver.find_element(By.XPATH, var_stx.chosen_results_8).click()
            time.sleep(1.5)

            var_stx.driver.find_element(By.XPATH, var_stx.DayOfWeek_chosen).click()    #Thứ trong tuần
            time.sleep(1.5)
            var_stx.driver.find_element(By.XPATH, var_stx.chosen_results_monday).click()
            time.sleep(1)


        element = var_stx.driver.find_element(By.XPATH, var_stx.company_promotion)
        var_stx.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.route_select).click()
        time.sleep(1)

        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle).click()
        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_4cho).click()
        time.sleep(1)

        var_stx.driver.find_element(By.XPATH, var_stx.promotion_area).click()
        time.sleep(1.5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.promotion_area_mb).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.promotion_area1).click()
        time.sleep(1)

        var_stx.driver.find_element(By.XPATH, var_stx.promotion_area_mb_dk4).click()
        time.sleep(1)

        var_stx.driver.find_element(By.XPATH, var_stx.company_promotion).click()
        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.company_promotion_g7hn).click()
        time.sleep(1)

        var_stx.driver.find_element(By.XPATH, var_stx.rank_ticket).click()
        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.rank_ticket_silver).click()
        time.sleep(1)
        element = var_stx.driver.find_element(By.XPATH, "//*[text()='Hiển thị mã khuyến mại']")
        var_stx.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        #CẤU HÌNH CHUNG
        if type_promotion == "Khuyến mại chung":
            var_stx.driver.find_element(By.XPATH, var_stx.display_promotion).click() #Hiển thị mã khuyến mại
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.promotion_trian).click() #Khuyến mại tri ân
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.code_promotion).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.code_promotion).send_keys(var_stx.data['promotion']['code_promotion']+number)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.count_sd).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.count_sd).send_keys(var_stx.data['promotion']['count_sd'])
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.count_max).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.count_max).send_keys(var_stx.data['promotion']['count_max'])

        if type_promotion == "Khuyến mại riêng":
            var_stx.driver.find_element(By.XPATH, var_stx.promotion_trian).click() #Khuyến mại tri ân
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.sl_code).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.sl_code).send_keys(var_stx.data['promotion']['sl_code'])
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.characters_start).send_keys(var_stx.data['promotion']['characters_start'])
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.length_code).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.length_code).send_keys(var_stx.data['promotion']['length_code'])
            time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.group_customer).click()
        time.sleep(1)


        #CẤU HÌNH THEO SỐ CHUYẾN ĐI
        var_stx.driver.find_element(By.XPATH, var_stx.promotion_customer).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.source_cuoc).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.time_start_dk).send_keys(var_stx.data['promotion']['time_start'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.sl_customer).send_keys(var_stx.data['promotion']['sl_customer'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.summary_cuoc).send_keys(var_stx.data['promotion']['summary_cuoc'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.time_end_dk).send_keys(var_stx.data['promotion']['time_end'])
        time.sleep(0.5)
        if type_promotion == "Khuyến mại chung":
            var_stx.driver.find_element(By.XPATH, var_stx.money_promotion).click()  #Cố định
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.value_money).send_keys(var_stx.data['promotion']['value_money'])

        if type_promotion == "Khuyến mại riêng":
            var_stx.driver.find_element(By.XPATH, var_stx.money_promotion2).click() #Theo cuốc
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.persent).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.persent).send_keys(var_stx.data['promotion']['persent'])
        time.sleep(1)
        element = var_stx.driver.find_element(By.XPATH, "//*[text()='Tiền khuyến mại tối thiểu']")
        var_stx.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.promotion_max).click()
        time.sleep(1)


        #CẤU HÌNH THEO CUỐC CÓ ĐIỂM TRẢ
        var_stx.driver.find_element(By.XPATH, var_stx.cuoc_have_location).click()  #Cuốc có điểm trả
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.payment_method1).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.payment_method).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.type_cuoc).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.type_cuoc1).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.km_min).send_keys(var_stx.data['promotion']['km_min'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.money_min).send_keys(var_stx.data['promotion']['money_min'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.promotion_min).send_keys(var_stx.data['promotion']['promotion_min'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.promotion_max).send_keys(var_stx.data['promotion']['promotion_max'])
        time.sleep(1.5)

        var_stx.driver.find_element(By.XPATH, var_stx.save).click()
        time.sleep(1)
        WebDriverWait(var_stx.driver, 15).until(EC.presence_of_element_located((By.XPATH, var_stx.promotion_update_success)))
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.1 Danh sách khuyến mại",
                                                  var_stx.promotion_update_success, "Khuyến mại đã được cập nhật thành công", name_image)
        time.sleep(2)
        button = var_stx.driver.find_element(By.XPATH, var_stx.come_back)
        var_stx.driver.execute_script("arguments[0].click();", button)
        time.sleep(4)


    def list_promotion_check_info(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_promotion)
        except:
            # list_promotion.list_promotion_add_new(self, "", "", "", "Khuyến mại riêng", "")
            list_promotion.list_promotion(self, "", "", "")


        time.sleep(1)
        code_promotion = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 23, 3))
        var_stx.driver.find_element(By.XPATH, "//*[text()='"+code_promotion+"']").click()
        time.sleep(4)
        var_stx.driver.switch_to.window(var_stx.driver.window_handles[1])
        time.sleep(3)

        try:
            wait = WebDriverWait(var_stx.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.save)))
        except:
            pass


        var_stx.driver.execute_script("window.scrollBy(0,1400)", "")
        time.sleep(1)
        element = var_stx.driver.find_element(By.XPATH, var_stx.save)
        var_stx.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(5)


        name_promotion = var_stx.driver.find_element(By.XPATH, var_stx.name_promotion).get_attribute('value')     #Tên khuyến mại

        iframe = var_stx.driver.find_element(By.XPATH, var_stx.promotion_add_new_conten)
        var_stx.driver.switch_to.frame(iframe)
        conten_promotion = var_stx.driver.find_element(By.XPATH, var_stx.conten_promotion).text     #Nội dung khuyến mại
        var_stx.driver.switch_to.default_content()
        time.sleep(0.5)

        noti1_promotion = var_stx.driver.find_element(By.XPATH, var_stx.noti1_promotion).text       #Thông báo khách hàng
        noti2_promotion = var_stx.driver.find_element(By.XPATH, var_stx.noti2_promotion).text       #Giải trình khuyến mại
        image_promotion = var_stx.driver.find_element(By.XPATH, var_stx.image_promotion).get_attribute('value')       #Ảnh khuyến mại
        banner_promotion = var_stx.driver.find_element(By.XPATH, var_stx.banner_promotion).get_attribute('value')       #Ảnh banner
        var_stx.driver.find_element(By.XPATH, var_stx.DisplayType)      #Kiểu hiển thị
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.TimeType)     #Loại khuyến mại
        except:
            TimeType = "mất trường loại khuyến mại"

        hour_promotion = var_stx.driver.find_element(By.XPATH, var_stx.hour_promotion).text       #Gio trong tuần
        day_promotion = var_stx.driver.find_element(By.XPATH, var_stx.day_promotion).text       #Ngày trong tuần
        var_stx.driver.find_element(By.XPATH, var_stx.route_promotion)      #Tuyến
        type_vehicle_promotion = var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_promotion).text       #Loại xe
        area1_promotion = var_stx.driver.find_element(By.XPATH, var_stx.area1_promotion).text       #Vùng Khuyến mại
        company_promotion1 = var_stx.driver.find_element(By.XPATH, var_stx.company_promotion1).text       #Công ty khuyến mại
        rank_promotion = var_stx.driver.find_element(By.XPATH, var_stx.rank_promotion).text       #Công ty khuyến mại
        IsGratitudePromotion_promotion = var_stx.driver.find_element(By.XPATH, var_stx.IsGratitudePromotion_promotion).get_attribute('value')       #Khuyến mãi tri ân
        sl_code_promotion = var_stx.driver.find_element(By.XPATH, var_stx.sl_code_promotion).get_attribute('value')      #Số lượng mã
        var_stx.driver.find_element(By.XPATH, var_stx.group_customer1)     #Nhóm khách hàng
        character_promotion = var_stx.driver.find_element(By.XPATH, var_stx.character_promotion).get_attribute('value')      #Ký tự bắt đầu
        length_code_promotion = var_stx.driver.find_element(By.XPATH, var_stx.length_code_promotion).get_attribute('value')      #Độ dài mã
        customer_promotion = var_stx.driver.find_element(By.XPATH, var_stx.customer_promotion).get_attribute('value')      #Khuyến mại theo khách hàng
        var_stx.driver.find_element(By.XPATH, var_stx.source)     #Nguồn cuốc
        time_star_dk_promotion = var_stx.driver.find_element(By.XPATH, var_stx.time_star_dk_promotion).get_attribute('value')      #Thời gian bắt đầu điều kiện
        var_stx.driver.find_element(By.XPATH, var_stx.PromoteMoneyType)     #Nguồn cuốc
        customer_count_promotion = var_stx.driver.find_element(By.XPATH, var_stx.customer_count_promotion).get_attribute('value')      #Số lượng khách hàng
        trip_number_promotion = var_stx.driver.find_element(By.XPATH, var_stx.trip_number_promotion).get_attribute('value')      #Tổng cuốc đã đi
        time_end_dk_promotion = var_stx.driver.find_element(By.XPATH, var_stx.time_end_dk_promotion).get_attribute('value')      #Thời gian kết thúc điều kiện
        persent_promotion = var_stx.driver.find_element(By.XPATH, var_stx.persent_promotion).get_attribute('value')      #% tiền cuốc
        DestinationRequire = var_stx.driver.find_element(By.XPATH, var_stx.DestinationRequire).get_attribute('value')     #Cuốc có điểm trả
        pttt_promotion = var_stx.driver.find_element(By.XPATH, var_stx.pttt_promotion).text       #Phương thức thanh toán
        BookTripType_chosen = var_stx.driver.find_element(By.XPATH, var_stx.BookTripType_chosen).text       #Loại cuốc áp dụng
        min_km_promotion = var_stx.driver.find_element(By.XPATH, var_stx.min_km_promotion).get_attribute('value')      #Số KM tối thiểu
        min_money_promotion = var_stx.driver.find_element(By.XPATH, var_stx.min_money_promotion).get_attribute('value')      #Số tiền cước tối thiểu
        min_moneykm_promotion = var_stx.driver.find_element(By.XPATH, var_stx.min_moneykm_promotion).get_attribute('value')      #Tiền khuyến mại tối thiểu
        max_moneykm_promotion = var_stx.driver.find_element(By.XPATH, var_stx.max_moneykm_promotion).get_attribute('value')      #Tiền khuyến mại tối đa

        print("Tên khuyến mại:" + name_promotion)
        print("Nội dung khuyến mại:" + conten_promotion)
        print("Thông báo khách hàng:" + noti1_promotion)
        print("Giải trình khuyến mại:" + noti2_promotion)
        print("Ảnh khuyến mại:" + image_promotion)
        print("Ảnh banner:" + banner_promotion)
        print("Gio trong ngay:" + hour_promotion)
        print("Ngày trong tuần:" + day_promotion)
        print("Loại xe:" + type_vehicle_promotion)
        print("Vùng Khuyến mại:" + area1_promotion)
        print("Công ty khuyến mại:" + company_promotion1)
        print("Hạng thẻ áp dụng:" + rank_promotion)
        print("Khuyến mãi tri ân:" + IsGratitudePromotion_promotion)
        print("Số lượng mã:" + sl_code_promotion)
        print("Ký tự bắt đầu:" + character_promotion)
        print("Độ dài mã:" + length_code_promotion)
        print("Khuyến mại theo khách hàng:" + customer_promotion)
        print("Thời gian bắt đầu điều kiện:" + time_star_dk_promotion)
        print("Số lượng khách hàng:" + customer_count_promotion)
        print("Tổng cuốc đã đi:" + trip_number_promotion)
        print("Thời gian kết thúc điều kiện:" + time_end_dk_promotion)
        print("% tiền cuốc:" + persent_promotion)
        print("Cuốc có điểm trả:" + DestinationRequire)
        print("Phương thức thanh toán:" + pttt_promotion)
        print("Loại cuốc áp dụng:" + BookTripType_chosen)
        print("Số KM tối thiểu:" + min_km_promotion)
        print("Số tiền cước tối thiểu:" + min_money_promotion)
        print("Tiền khuyến mại tối thiểu:" + min_moneykm_promotion)
        print("Tiền khuyến mại tối đa:" + max_moneykm_promotion)

        logging.info("-------------------------")
        logging.info("KHUYẾN MẠI - 6.1 Danh sách khuyến mại")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        list_promotion.check_km(self, code, "Tên khuyến mại", code_promotion, name_promotion)
        list_promotion.check_km(self, code, "Nội dung khuyến mại", var_stx.data['promotion']['conten'], conten_promotion)
        list_promotion.check_km(self, code, "Thông báo khách hàng", var_stx.data['promotion']['notification'], noti1_promotion)
        list_promotion.check_km(self, code, "Giải trình khuyến mại", var_stx.data['promotion']['explanation'], noti2_promotion)
        list_promotion.check_km(self, code, "Ảnh khuyến mại", var_stx.data['promotion']['image1'], image_promotion)
        list_promotion.check_km(self, code, "Ảnh banner", var_stx.data['promotion']['image2'], banner_promotion)
        list_promotion.check_km(self, code, "Giờ trong ngày", "8", hour_promotion)
        list_promotion.check_km(self, code, "Ngày trong tuần", "Thứ 2", day_promotion)
        list_promotion.check_km(self, code, "Loại xe", "4 Chỗ", type_vehicle_promotion)
        list_promotion.check_km_or(self, code, "Vùng Khuyến mại", "SÂN BAY NỘI BÀI", "G7", area1_promotion)
        list_promotion.check_km(self, code, "Công ty khuyến mại", "G7 Taxi Hà Nội", company_promotion1)
        list_promotion.check_km(self, code, "Hạng thẻ áp dụng", "Hạng bạc", rank_promotion)
        list_promotion.check_km(self, code, "Khuyến mãi tri ân", "true", IsGratitudePromotion_promotion)
        list_promotion.check_km(self, code, "Số lượng mã", var_stx.data['promotion']['sl_code'], sl_code_promotion)
        list_promotion.check_km(self, code, "Ký tự bắt đầu", var_stx.data['promotion']['characters_start'], character_promotion)
        list_promotion.check_km(self, code, "Độ dài mã", var_stx.data['promotion']['length_code'], length_code_promotion)
        list_promotion.check_km(self, code, "Khuyến mại theo khách hàng", "true", customer_promotion)
        list_promotion.check_km(self, code, "Thời gian bắt đầu điều kiện", var_stx.data['promotion']['time_start'], time_star_dk_promotion)
        list_promotion.check_km(self, code, "Thời gian kết thúc điều kiện", var_stx.data['promotion']['time_end'], time_end_dk_promotion)
        list_promotion.check_km(self, code, "Số lượng khách hàng", var_stx.data['promotion']['sl_customer'], customer_count_promotion)
        list_promotion.check_km(self, code, "Tổng cuốc đã đi", var_stx.data['promotion']['summary_cuoc'], trip_number_promotion)
        list_promotion.check_km(self, code, "% tiền cuốc", var_stx.data['promotion']['persent'], persent_promotion)
        list_promotion.check_km(self, code, "Cuốc có điểm trả", "true", DestinationRequire)
        list_promotion.check_km(self, code, "Phương thức thanh toán", "Tiền mặt", pttt_promotion)
        list_promotion.check_km(self, code, "Loại cuốc áp dụng", "Taxi thông thường", BookTripType_chosen)
        list_promotion.check_km(self, code, "Số KM tối thiểu", var_stx.data['promotion']['km_min'], min_km_promotion)
        list_promotion.check_km(self, code, "Số tiền cước tối thiểu", var_stx.data['promotion']['money_min'], min_money_promotion)
        list_promotion.check_km(self, code, "Tiền khuyến mại tối thiểu", var_stx.data['promotion']['promotion_min'], min_moneykm_promotion)
        list_promotion.check_km(self, code, "Tiền khuyến mại tối đa", var_stx.data['promotion']['promotion_max'], max_moneykm_promotion)

        wordbook = openpyxl.load_workbook(var_stx.checklistpath)
        sheet = wordbook.get_sheet_by_name("Checklist")
        rownum = 9
        while (rownum < 1000):
            rownum += 1
            rownum = str(rownum)
            if sheet["A" + rownum].value == code and sheet["F" + rownum].value != None:
                ma = sheet["A" + rownum].value
                result1 = sheet["F" + rownum].value
                print(ma)
                print(result1)
                print(sheet["F" + rownum].value)
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
            rownum = int(rownum)

        time.sleep(1)
        # button = var_stx.driver.find_element(By.XPATH, var_stx.come_back)
        # var_stx.driver.execute_script("arguments[0].click();", button)
        # time.sleep(4)
        var_stx.driver.find_element(By.XPATH, var_stx.come_back)
        module_other_stx.close_tab()
        var_stx.driver.switch_to.window(var_stx.driver.window_handles[0])
        time.sleep(1)



    def check_km(self, code, name, data_before, data_affter):
        logging.info(name + " nhập:" + data_before)
        logging.info(name + " lưu :" + data_affter)

        if data_before == data_affter:
            logging.info("True")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, name + ": \nnhập: {}\n lưu: {}".format(data_before, data_affter))
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
            try:
                element = var_stx.driver.find_element(By.XPATH, "//*[text()='"+name+"']")
                var_stx.driver.execute_script("arguments[0].scrollIntoView();", element)
                time.sleep(1)
            except:
                pass
            var_stx.driver.save_screenshot(var_stx.imagepath + code + "_DanhSachKhuyenmai_Checkthongtin.png")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_DanhSachKhuyenmai_Checkthongtin.png")



    def check_km_or(self, code, name, data_before, data_affter, data_affter1):
        logging.info(name + " nhập:" + data_before)
        logging.info(name + " lưu :" + data_affter)
        logging.info(name + " web :" + data_affter1)

        if (data_before == data_affter1) or (data_affter == data_affter1):
            logging.info("True")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, name + ": \nnhập: {}\n lưu: {}".format(data_before, data_affter))
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
            try:
                element = var_stx.driver.find_element(By.XPATH, "//*[text()='"+name+"']")
                var_stx.driver.execute_script("arguments[0].scrollIntoView();", element)
                time.sleep(1)
            except:
                pass
            var_stx.driver.save_screenshot(var_stx.imagepath + code + "_DanhSachKhuyenmai_Checkthongtin.png")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_DanhSachKhuyenmai_Checkthongtin.png")




    def list_promotion_update(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.update_promotion)
            button = var_stx.driver.find_element(By.XPATH, var_stx.come_back)
            var_stx.driver.execute_script("arguments[0].click();", button)
            time.sleep(4)
        except:
            pass

        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_promotion)
        except:
            list_promotion.list_promotion_add_new(self, "", "", "", "Khuyến mại riêng", "")


        time.sleep(1)
        code_promotion = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 23, 3))
        var_stx.driver.find_element(By.XPATH, "//*[text()='"+code_promotion+"']").click()
        time.sleep(4)

        var_stx.driver.switch_to.window(var_stx.driver.window_handles[1])
        time.sleep(1)

        element = var_stx.driver.find_element(By.XPATH, var_stx.save)
        var_stx.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        # var_stx.driver.find_element(By.XPATH, var_stx.NotificationMessage).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        # var_stx.driver.find_element(By.XPATH, var_stx.NotificationMessage).send_keys("Trường test thông báo khách hàng đã sửa")
        # time.sleep(1)

        var_stx.driver.find_element(By.XPATH, var_stx.persent).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        var_stx.driver.find_element(By.XPATH, var_stx.persent).send_keys(var_stx.data['promotion']['persent_edit'])
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.save).click()
        time.sleep(7)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.1 Danh sách khuyến mại",
                                                  var_stx.promotion_update_success, "Khuyến mại đã được cập nhật thành công",
                                                  "_DanhSachKhuyenmai_CapNhat.png")
        module_other_stx.close_tab()
        var_stx.driver.switch_to.window(var_stx.driver.window_handles[0])
        time.sleep(1)



    def list_promotion_create_code(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.update_promotion)
        except:
            list_promotion.list_promotion_update(self, "", "", "")


        time.sleep(1)
        code_promotion = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 23, 3))
        var_stx.driver.find_element(By.XPATH, "//*[text()='"+code_promotion+"']").click()
        time.sleep(4)

        var_stx.driver.switch_to.window(var_stx.driver.window_handles[1])
        time.sleep(1)

        element = var_stx.driver.find_element(By.XPATH, var_stx.save)
        var_stx.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.create_list_km).click()
        time.sleep(4.5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.fill_code).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.fill_code1).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.save_list_code).click()
        time.sleep(3)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.1 Danh sách khuyến mại",
                                                  var_stx.text_success, "Sinh mã khuyến mại thành công.", "_DanhSachKhuyenmai_TaoMa.png")


        module_other_stx.close_tab()
        var_stx.driver.switch_to.window(var_stx.driver.window_handles[0])
        time.sleep(1)

        # var_stx.driver.back()
        # time.sleep(4)
        # try:
        #     button = var_stx.driver.find_element(By.XPATH, var_stx.come_back)
        #     var_stx.driver.execute_script("arguments[0].click();", button)
        # except:
        #     var_stx.driver.refresh()
        #     time.sleep(5)
        #     button = var_stx.driver.find_element(By.XPATH, var_stx.come_back)
        #     var_stx.driver.execute_script("arguments[0].click();", button)
        # time.sleep(4)


    def list_promotion_active(self, code, eventname, result, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_promotion)
        except:
            list_promotion.list_promotion(self, "", "", "")

        list_promotion.list_promotion_x(self)
        code_promotion = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 23, 3))

        var_stx.driver.find_element(By.XPATH, var_stx.name).send_keys(code_promotion)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        var_stx.driver.find_element(By.XPATH, var_stx.col_id_2_button).click()
        time.sleep(5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
        except:
            pass

        try:
            wait = WebDriverWait(var_stx.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.toast_message)))
        except:
            pass

        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.1 Danh sách khuyến mại",
                                                  var_stx.toast_message, "Cập nhật thành công.", name_image)

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.close).click()
            time.sleep(4)
        except:
            pass


    def list_promotion_icon(self, code, eventname, result, path_icon, path_check, desire, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_promotion)
        except:
            list_promotion.list_promotion(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, path_icon).click()
        time.sleep(4)
        wait = WebDriverWait(var_stx.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, path_check)))
        time.sleep(1)

        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.1 Danh sách khuyến mại",
                                                  path_check, desire, name_image)

        if name_image == "_DanhSachKhuyenmai_BaoCao.png" or name_image == "_DanhSachKhuyenmai_SaoChep.png":
            var_stx.driver.back()
            time.sleep(5)


    def wallet_history_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_promotion1)
        except:
            list_promotion.list_promotion_icon(self, "", "", "", var_stx.icon_see, "", "", "")

        time.sleep(2.5)
        var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        time.sleep(7)
        get_info_web()
        try:
            minitor_stx.get_info_excel(5, "Sheet 1")
        except:
            var_stx.driver.refresh()
            time.sleep(7)
            var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
            time.sleep(7)
            get_info_web()
            minitor_stx.get_info_excel(5, "Sheet 1")
        minitor_stx.check_info_web_excel(code, eventname, result, "KHUYẾN MẠI - 6.1 Danh sách khuyến mại")

        var_stx.driver.back()
        time.sleep(5)


    def list_promotion_delete(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_promotion)
        except:
            list_promotion.list_promotion(self, "", "", "")

        list_promotion.list_promotion_add_new(self, "", "", "", "Khuyến mại riêng","")

        list_promotion.list_promotion_x(self)
        code_promotion = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 23, 3))
        try:
            wait = WebDriverWait(var_stx.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.name)))
        except:
            list_promotion.list_promotion(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.name).send_keys(code_promotion)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        name_promotion = var_stx.driver.find_element(By.XPATH, var_stx.col_id_name2).text
        if name_promotion == code_promotion:
            var_stx.driver.find_element(By.XPATH, var_stx.row_index0_icon_dele).click()
            time.sleep(7)
            try:
                var_stx.driver.find_element(By.XPATH, var_stx.delete1).click()
            except:
                pass

            try:
                wait = WebDriverWait(var_stx.driver, 5)
                element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.delete_promotion_success)))#
            except:
                pass
            module_other_stx.write_result_text_try_if_in(code, eventname, result, "KHUYẾN MẠI - 6.1 Danh sách khuyến mại",
                                                      var_stx.delete_promotion_success, "Xóa khuyến mại thành công", "_DanhSachKhuyenmai_Xoa.png")

            try:
                var_stx.driver.find_element(By.XPATH, var_stx.close).click()
                time.sleep(4.5)
            except:
                pass







class introduce_list_account:


    def introduce_list_account(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.introduce_list_account).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.introduce_list_account).click()
        time.sleep(2)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.title_page)))
            time.sleep(2)
        except:
            pass
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.2 Danh sách tài khoản giới thiệu",
                                                  var_stx.title_page, "6.2 Danh sách tài khoản giới thiệu", "_DanhSachTaiKhoanGioiThieu.png")


    def introduce_list_account_g7_test(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx_g7test(self, var_stx.data['login']['tk_admin_test'],  var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.introduce_list_account).click()
        time.sleep(2.5)


    def introduce_list_account_x(self):
        var_stx.driver.implicitly_wait(0.2)
        try:
            tu_ngay = var_stx.driver.find_element(By.XPATH, var_stx.from_day)
            var_stx.driver.execute_script("arguments[0].value = '';", tu_ngay)
            time.sleep(0.2)
        except:
            pass
        try:
            den_ngay = var_stx.driver.find_element(By.XPATH, var_stx.to_day)
            var_stx.driver.execute_script("arguments[0].value = '';", den_ngay)
            time.sleep(0.2)
        except:
            pass

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
            var_stx.driver.find_element(By.XPATH, var_stx.account).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.my_introduce_code).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.person_code_introduce).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.3)
        except:
            pass

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.type_account_introduce).click()
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.group_account).click()
            time.sleep(0.3)
        except:
            pass

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.account).click()
        except:
            pass

        var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(var_stx.data['promotion']['from_day1'])
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(var_stx.data['promotion']['to_day1'])
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.person_code_introduce).send_keys("tr09")
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.person_code_introduce).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(4)


    def introduce_list_account_x1(self):
        var_stx.driver.implicitly_wait(0.2)
        # try:
        #     tu_ngay = var_stx.driver.find_element(By.XPATH, var_stx.from_day)
        #     var_stx.driver.execute_script("arguments[0].value = '';", tu_ngay)
        #     time.sleep(0.2)
        # except:
        #     pass
        # try:
        #     den_ngay = var_stx.driver.find_element(By.XPATH, var_stx.to_day)
        #     var_stx.driver.execute_script("arguments[0].value = '';", den_ngay)
        #     time.sleep(0.2)
        # except:
        #     pass

        # try:
        #     var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        #     time.sleep(0.3)
        # except:
        #     pass
        #
        # try:
        #     var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        #     time.sleep(0.3)
        # except:
        #     pass

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.account).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.my_introduce_code).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.person_code_introduce).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.3)
        except:
            pass

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.type_account_introduce).click()
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.group_account).click()
            time.sleep(0.3)
        except:
            pass

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.account).click()
        except:
            pass


    def introduce_list_account_from_to_day(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_introduce_list_account)
        except:
            introduce_list_account.introduce_list_account(self, "", "", "")

        introduce_list_account.introduce_list_account_x1(self)


        var_stx.driver.find_element(By.XPATH, var_stx.reportrange).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.week_before).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.person_code_introduce).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.table_1_2)
        except:
            introduce_list_account.introduce_list_account_x1(self)
            var_stx.driver.find_element(By.XPATH, var_stx.search)
            time.sleep(5)

        module_other_stx.write_result_text_try_if_other(code, eventname, result, "KHUYẾN MẠI - 6.2 Danh sách tài khoản giới thiệu",
                                              var_stx.table_1_2, "", "_DanhSachTaiKhoanGioiThieu_TuNgayDenNgay.png")


    def introduce_list_account_search(self, code, eventname, result, path_input, path_data, path_check, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_introduce_list_account)
        except:
            introduce_list_account.introduce_list_account(self, "", "", "")

        introduce_list_account.introduce_list_account_x1(self)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)

        try:
            data = var_stx.driver.find_element(By.XPATH, path_data).text
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.reportrange).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.week_before).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(5)

        data = var_stx.driver.find_element(By.XPATH, path_data).text
        var_stx.driver.find_element(By.XPATH, path_input).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.account).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(4)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.2 Danh sách tài khoản giới thiệu",
                                              path_check, data, name_image)


    def introduce_list_account_combobox(self, code, eventname, result, path_combobox, path_select, path_check, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_introduce_list_account)
        except:
            introduce_list_account.introduce_list_account(self, "", "", "")

        introduce_list_account.introduce_list_account_x1(self)

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.reportrange).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.week_before).click()
            time.sleep(2)
        except:
            pass

        var_stx.driver.find_element(By.XPATH, path_combobox).click()
        time.sleep(1.5)
        name_combobox = var_stx.driver.find_element(By.XPATH, path_select).text
        var_stx.driver.find_element(By.XPATH, path_select).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(4)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.2 Danh sách tài khoản giới thiệu",
                                              path_check, name_combobox, name_image)


    def introduce_list_account_addnew(self, code, eventname, result, type):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_introduce_list_account)
        except:
            introduce_list_account.introduce_list_account(self, "", "", "")


        vehicle_driver_stx.increase()
        number = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 7, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.add_new1).click()
        time.sleep(2.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_accoun_account).send_keys("210000"+number)

        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_accoun_my_code_introduce).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_accoun_my_code_introduce).send_keys("210000"+number)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_accoun_code_persion_introduce)

        # var_stx.driver.find_element(By.XPATH, var_stx.add_new_accoun_code_persion_introduce).send_keys("KD01")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_accoun_code_type_account).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_accoun_code_group_account).click()
        time.sleep(0.5)

        # if type == "Đã kích hoạt":
        #     var_stx.driver.find_element(By.XPATH, var_stx.add_new_accoun_active_account).click()
        #     time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
        time.sleep(3.5)

        module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 14, "210000"+number)
        var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 24, 2, "210000"+number)

        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.2 Danh sách tài khoản giới thiệu",
                                                  var_stx.message, "Lưu tài khoản giới thiệu thành công.", "_DanhSachTaiKhoanGioiThieu_ThemMoi.png")

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.close).click()
            time.sleep(3)
        except:
            pass


    def introduce_list_account_update(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_introduce_list_account)
        except:
            introduce_list_account.introduce_list_account_addnew(self, "", "", "", "Chưa kích hoạt")

        introduce_list_account.introduce_list_account_x1(self)
        vehicle_driver_stx.increase()
        number = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 7, 2))
        account = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 24, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.account).send_keys(account)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3)
        var_stx.driver.find_element(By.XPATH, var_stx.table_1_2_button).click()
        time.sleep(2.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_accoun_my_code_introduce).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_accoun_my_code_introduce).send_keys("210000"+number)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
        time.sleep(3)
        try:
            var_stx.driver.implicitly_wait(0.3)
            var_stx.driver.find_element(By.XPATH, var_stx.confirm).click()
            time.sleep(3)
            var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
            time.sleep(3)
        except:
            pass

        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.2 Danh sách tài khoản giới thiệu",
                                                  var_stx.message, "Lưu tài khoản giới thiệu thành công.", "_DanhSachTaiKhoanGioiThieu_CapNhat.png")

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.close).click()
            time.sleep(3)
        except:
            pass


    def introduce_list_account_delete(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_introduce_list_account)
        except:
            introduce_list_account.introduce_list_account_addnew(self, "", "", "", "Chưa kích hoạt")

        introduce_list_account.introduce_list_account_x1(self)
        account = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 24, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.account).send_keys(account)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(4)
        check_name = var_stx.driver.find_element(By.XPATH, var_stx.table_1_2).text
        if check_name == account:
            var_stx.driver.find_element(By.XPATH, var_stx.introduce_list_account_delete).click()
            time.sleep(2.5)
            var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
            time.sleep(3)
            module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.2 Danh sách tài khoản giới thiệu",
                                                      var_stx.message, "Xóa tài khoản giới thiệu thành công.", "_DanhSachTaiKhoanGioiThieu_Xoa.png")

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.close).click()
            time.sleep(3)
        except:
            pass







class install_new_app:


    def install_new_app(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.config_cckm).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.config_cckm).click()
            time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.install_new_app).click()
        time.sleep(2)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.title_page1)))
            time.sleep(2)
        except:
            pass
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.3.1 Cài app mới",
                                              var_stx.title_page1, "6.3.1 Cài app mới", "_CaiAppMoi.png")


    def install_new_app_g7_test(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx_g7test(self, var_stx.data['login']['tk_admin_test'],  var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.config_cckm).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.install_new_app).click()
        time.sleep(3.5)


    def install_new_app_search(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_install_new_app)
        except:
            install_new_app.install_new_app(self, "", "", "")

        name = var_stx.driver.find_element(By.XPATH, var_stx.table_2_2).text

        var_stx.driver.find_element(By.XPATH, var_stx.name).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        var_stx.driver.find_element(By.XPATH, var_stx.name).send_keys(name)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.table_1_2)))
        except:
            pass
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.3.1 Cài app mới",
                                              var_stx.table_1_2, name, "_CaiAppMoi_TimKiem.png")


    # @retry(tries=2, delay=2, backoff=1, jitter=5)
    def install_new_app_addnew(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_install_new_app)
        except:
            install_new_app.install_new_app(self, "", "", "")

        number_old = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 25, 2))
        var_stx.driver.find_element(By.XPATH, var_stx.name).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        var_stx.driver.find_element(By.XPATH, var_stx.name).send_keys(number_old)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(4)
        try:
            color_active = var_stx.driver.find_element(By.XPATH, var_stx.table_1_6_button).value_of_css_property("color")
            text_active = var_stx.driver.find_element(By.XPATH, var_stx.table_1_6_button).text
            print("color:"+ color_active)
            print("text:"+ text_active)
            if color_active == "rgba(51, 122, 183, 1)" and text_active == "Kích hoạt":
                var_stx.driver.find_element(By.XPATH, var_stx.active).click()
                time.sleep(2.5)
                var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
                time.sleep(2)
                try:
                    var_stx.driver.find_element(By.XPATH, var_stx.close).click()
                    time.sleep(4)
                except:
                    pass
                var_stx.driver.find_element(By.XPATH, var_stx.name).send_keys(Keys.CONTROL, "a", Keys.DELETE)
                var_stx.driver.find_element(By.XPATH, var_stx.name).send_keys(number_old)
                time.sleep(1)
                var_stx.driver.find_element(By.XPATH, var_stx.search).click()
                time.sleep(4)
                var_stx.driver.find_element(By.XPATH, var_stx.stop_active).click()
                time.sleep(2.5)
                var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
                time.sleep(2)
                try:
                    var_stx.driver.find_element(By.XPATH, var_stx.close).click()
                    time.sleep(4)
                except:
                    pass

            if color_active == "rgba(51, 122, 183, 1)" and text_active == "Ngừng kích hoạt":
                var_stx.driver.find_element(By.XPATH, var_stx.active).click()
                time.sleep(2.5)
                var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
                time.sleep(2)
                try:
                    var_stx.driver.find_element(By.XPATH, var_stx.close).click()
                    time.sleep(4)
                except:
                    pass
        except:
            var_stx.driver.refresh()
            time.sleep(7)


        vehicle_driver_stx.increase()
        number = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 7, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.add_new1).click()
        time.sleep(2)
        wait = WebDriverWait(var_stx.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.promotion_add_new_name)))
        time.sleep(2)

        var_stx.driver.find_element(By.XPATH, var_stx.promotion_add_new_name).send_keys("Auto_CaiAppMoi"+number)
        module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 14, "Auto_CaiAppMoi"+number)
        var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 25, 2, "Auto_CaiAppMoi" + number)

        time.sleep(0.5)
        iframe = var_stx.driver.find_element(By.XPATH, var_stx.promotion_add_new_conten)
        var_stx.driver.switch_to.frame(iframe)
        content_area = var_stx.driver.find_element(By.XPATH, var_stx.promotion_add_new_conten_body)
        content_area.send_keys(var_stx.data['promotion']['conten1'])
        var_stx.driver.switch_to.default_content()
        time.sleep(1)

        var_stx.driver.find_element(By.XPATH, var_stx.promotion_add_new_notification).send_keys(var_stx.data['promotion']['notification1'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.promotion_add_new_explanation).send_keys(var_stx.data['promotion']['explanation1'])    #giải trình
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.promotion_add_new_image).send_keys(var_stx.data['promotion']['image1'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.promotion_add_new_banner).send_keys(var_stx.data['promotion']['image2'])
        time.sleep(0.5)
        element = var_stx.driver.find_element(By.XPATH, "//*[text()='Tặng tiền khi giới thiệu']")
        var_stx.driver.execute_script("arguments[0].scrollIntoView();", element)


        #Kiểu hiển thị
        var_stx.driver.find_element(By.XPATH, var_stx.type_display0).click()    #mặc định
        time.sleep(1)

        #Thời gian
        var_stx.driver.find_element(By.XPATH, var_stx.time_start).send_keys(var_stx.data['promotion']['time_start'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.time_end).send_keys(var_stx.data['promotion']['time_end'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.promotion_add_new_image).click()


        #Cấu hình người cài App mới
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.donate_money_default).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.promotional_money).send_keys(var_stx.data['promotion']['promotional_money'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.max_promotion).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.max_promotion).send_keys(var_stx.data['promotion']['max_promotion'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.money_promotional).send_keys(var_stx.data['promotion']['money_promotional'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.count_sd).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.count_sd).send_keys(var_stx.data['promotion']['count_sd'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.group1).click()
        # var_stx.driver.find_element(By.XPATH, var_stx.group0).click()
        time.sleep(1)


        #Cấu hình người giới thiệu
        var_stx.driver.find_element(By.XPATH, var_stx.donate_money1).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.number_money).send_keys(var_stx.data['promotion']['number_money'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.dk_donate_money1).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.maximum_limit).send_keys(var_stx.data['promotion']['maximum_limit'])
        time.sleep(0.5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.number_of_apps_introduced).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.number_of_apps_introduced).send_keys(var_stx.data['promotion']['number_of_apps_introduced'])
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.number_of_successful_picks).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.number_of_successful_picks).send_keys(var_stx.data['promotion']['number_of_successful_picks'])
        time.sleep(0.5)
        element = var_stx.driver.find_element(By.XPATH, "//*[text()='(Giới hạn số tiền tối đa mà KH được khuyến mại. Áp dụng cho CTKM theo %)']")
        var_stx.driver.execute_script("arguments[0].scrollIntoView();", element)

        #Điều kiện khuyến mại
        var_stx.driver.find_element(By.XPATH, var_stx.hoe_has_pay_points).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.minimum_km).send_keys(var_stx.data['promotion']['minimum_km'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.minimum_fare_amount).send_keys(var_stx.data['promotion']['minimum_fare_amount'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.minimum_promotional_amount).send_keys(var_stx.data['promotion']['minimum_promotional_amount'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.maxium_promotional_amount).send_keys(var_stx.data['promotion']['maxium_promotional_amount'])
        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.save).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.save).click()
            time.sleep(2)
        except:
            pass
        wait = WebDriverWait(var_stx.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.check_promotion)))
        time.sleep(1)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.3.1 Cài app mới",
                                                  var_stx.check_promotion, "Khuyến mại đã được tạo thành công", "_CaiAppMoi_ThemMoi.png")

        button = var_stx.driver.find_element(By.XPATH, var_stx.come_back)
        var_stx.driver.execute_script("arguments[0].click();", button)
        time.sleep(7)


    def install_new_app_update(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_install_new_app)
        except:
            # install_new_app.install_new_app_addnew(self, "", "", "")
            install_new_app.install_new_app(self, "", "", "")


        time.sleep(1)
        code_promotion = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 25, 2))
        var_stx.driver.find_element(By.XPATH, "//*[text()='"+code_promotion+"']").click()
        time.sleep(4)
        element = var_stx.driver.find_element(By.XPATH, var_stx.save)
        var_stx.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.maxium_promotional_amount).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        var_stx.driver.find_element(By.XPATH, var_stx.maxium_promotional_amount).send_keys(var_stx.data['promotion']['maxium_promotional_amount_edit'])
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.save).click()
        time.sleep(8)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.3.1 Cài app mới",
                                                  var_stx.promotion_update_success1, "Khuyến mại đã được cập nhật thành công",
                                                  "_CaiAppMoi_CapNhat.png")

        button = var_stx.driver.find_element(By.XPATH, var_stx.come_back)
        var_stx.driver.execute_script("arguments[0].click();", button)
        time.sleep(5)


    def install_new_app_active(self, code, eventname, result, button, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_install_new_app)
        except:
            install_new_app.install_new_app_addnew(self, "", "", "")
            # install_new_app.install_new_app_addnew(self, "", "", "")


        time.sleep(1)
        code_promotion = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 25, 2))
        var_stx.driver.find_element(By.XPATH, var_stx.name).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        var_stx.driver.find_element(By.XPATH, var_stx.name).send_keys(code_promotion)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(4)
        var_stx.driver.find_element(By.XPATH, button).click()
        time.sleep(2.5)
        var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
        time.sleep(2)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.3.1 Cài app mới",
                                                  var_stx.update_success1, "Cập nhật thành công.", name_image)

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.close).click()
            time.sleep(4)
        except:
            pass






class report:


    def summary_report_on_promotions_by_company(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.report).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.report).click()
            time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.summary_report_on_promotions_by_company).click()
        time.sleep(2)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.title_page1)))
            time.sleep(2)
        except:
            pass
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.4 Báo cáo - 6.4.1 BC tổng hợp KM theo công ty",
                                                  var_stx.title_page1, "6.4.1 BC tổng hợp KM theo công ty", "_BCTongHopKmTheoCongTy.png")


    def summary_report_on_promotions_by_company_search(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_summary_report_on_promotions_by_company)
        except:
            report.summary_report_on_promotions_by_company(self, "", "", "")

        #
        var_stx.driver.find_element(By.XPATH, var_stx.reportrange).click()
        time.sleep(2.5)

        var_stx.driver.find_element(By.XPATH, var_stx.daterangepicker_start).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.daterangepicker_start).send_keys("23/10/2025 00:00")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.daterangepicker_end).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.daterangepicker_end).send_keys("29/10/2025 08:56")
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.apply).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(10)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.list_data2_2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.reportrange).click()
            time.sleep(2.5)
            var_stx.driver.find_element(By.XPATH, var_stx.daterangepicker_start).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.daterangepicker_start).send_keys("23/10/2024 00:00")
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.daterangepicker_end).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.daterangepicker_end).send_keys("29/10/2025 08:56")
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.apply).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(10)


        module_other_stx.write_result_text_try_if_other(code, eventname, result, "KHUYẾN MẠI - 6.4 Báo cáo - 6.4.1 BC tổng hợp KM theo công ty",
                                              var_stx.list_data2_2, "", "_BCTongHopKmTheoCongTy_TimKiem.png")


    def summary_report_on_promotions_by_company_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_summary_report_on_promotions_by_company)
            var_stx.driver.find_element(By.XPATH, var_stx.list_data2_2)
        except:
            report.summary_report_on_promotions_by_company_search(self, "", "", "")

        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        time.sleep(7)
        minitor_stx.get_info_web()
        try:
            minitor_stx.get_info_excel(5, "Sheet 1")
        except:
            var_stx.driver.refresh()
            time.sleep(7)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(8)
            var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
            time.sleep(7)
            minitor_stx.get_info_web()
            minitor_stx.get_info_excel(5, "Sheet 1")
        minitor_stx.check_info_web_excel(code, eventname, result, "KHUYẾN MẠI - 6.4 Báo cáo - 6.4.1 BC tổng hợp KM theo công ty")







    def detailed_km_reports_by_company(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.report).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.report).click()
            time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.detailed_km_reports_by_company).click()
        time.sleep(2)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.title_page1)))
            time.sleep(2)
        except:
            pass
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.4 Báo cáo - 6.4.2 BC chi tiết KM theo công ty",
                                                  var_stx.title_page1, "6.4.2 BC chi tiết KM theo công ty", "_BCChiTietKmTheoCongTy.png")


    def detailed_km_reports_by_company_search(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_detailed_km_reports_by_company)
        except:
            report.detailed_km_reports_by_company(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys("26/08/2025 00:00")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys("04/09/2025 23:59")
        time.sleep(1)

        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.list_data2_2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys("28/04/2025 00:00")
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys("02/06/2025 23:59")
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(5)
        module_other_stx.write_result_text_try_if_other(code, eventname, result, "KHUYẾN MẠI - 6.4 Báo cáo - 6.4.2 BC chi tiết KM theo công ty",
                                              var_stx.list_data2_2, "", "_BCChiTietKmTheoCongTy_TimKiem.png")


    def detailed_km_reports_by_company_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_detailed_km_reports_by_company)
            var_stx.driver.find_element(By.XPATH, var_stx.list_data2_2)
        except:
            report.detailed_km_reports_by_company_search(self, "", "", "")

        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        time.sleep(7)
        minitor_stx.get_info_web()
        try:
            minitor_stx.get_info_excel(5, "Sheet 1")
        except:
            var_stx.driver.refresh()
            time.sleep(7)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(8)
            var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
            time.sleep(7)
            minitor_stx.get_info_web()
            minitor_stx.get_info_excel(5, "Sheet 1")
        minitor_stx.check_info_web_excel(code, eventname, result, "KHUYẾN MẠI - 6.4 Báo cáo - 6.4.2 BC chi tiết KM theo công ty")







    def reports_km_by_day(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.report).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.report).click()
            time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.reports_km_by_day).click()
        time.sleep(2)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.title_page1)))
            time.sleep(2)
        except:
            pass
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.4 Báo cáo - 6.4.3 BC KM theo ngày",
                                                  var_stx.title_page1, "6.4.3 BC KM theo ngày", "_BCKMTheoNgay.png")


    def reports_km_by_day_search(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_reports_km_by_day)
        except:
            report.reports_km_by_day(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys("08/08/2025 00:00")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys("09/09/2025 23:59")
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.table_1_2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys("11/07/2025 00:00")
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys("02/06/2026 00:00")
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(10)

        module_other_stx.write_result_text_try_if_other(code, eventname, result, "KHUYẾN MẠI - 6.4 Báo cáo - 6.4.3 BC KM theo ngày",
                                              var_stx.table_1_2, "", "_BCKMTheoNgay_TimKiem.png")


    def reports_km_by_day_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_reports_km_by_day)
            var_stx.driver.find_element(By.XPATH, var_stx.table_1_2)
        except:
            report.reports_km_by_day_search(self, "", "", "")

        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        time.sleep(9)
        get_info_web1()
        try:
            minitor_stx.get_info_excel(5, "Sheet 1")
        except:
            var_stx.driver.refresh()
            time.sleep(7)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(8)
            var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
            time.sleep(9)
            get_info_web1()
            minitor_stx.get_info_excel(5, "Sheet 1")
        minitor_stx.check_info_web_excel(code, eventname, result, "KHUYẾN MẠI - 6.4 Báo cáo - 6.4.3 BC KM theo ngày")








    def reports_km_by_month(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.report).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.report).click()
            time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.reports_km_by_month).click()
        time.sleep(2)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.title_page1)))
            time.sleep(2)
        except:
            pass
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.4 Báo cáo - 6.4.4 BC KM theo tháng",
                                                  var_stx.title_page1, "6.4.4 BC KM theo tháng", "_BCKMTheoThang.png")


    def reports_km_by_month_search(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_reports_km_by_month)
        except:
            report.reports_km_by_month(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys("12/2024")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys("12/2024")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(7)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.table_1_2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys("12/2024")
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys("05/2026")
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(7)

        try:
            wait = WebDriverWait(var_stx.driver, 15)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.table_1_2)))
        except:
            pass
        module_other_stx.write_result_text_try_if_other(code, eventname, result, "KHUYẾN MẠI - 6.4 Báo cáo - 6.4.4 BC KM theo tháng",
                                              var_stx.table_1_2, "", "_BCKMTheoThang_TimKiem.png")


    def reports_km_by_month_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_reports_km_by_month)
            var_stx.driver.find_element(By.XPATH, var_stx.table_1_2)
        except:
            report.reports_km_by_month_search(self, "", "", "")

        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        time.sleep(5)
        get_info_web1()
        try:
            minitor_stx.get_info_excel(5, "Sheet 1")
        except:
            var_stx.driver.refresh()
            time.sleep(7)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(5)
            var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
            time.sleep(5)
            get_info_web1()
            minitor_stx.get_info_excel(5, "Sheet 1")
        minitor_stx.check_info_web_excel(code, eventname, result, "KHUYẾN MẠI - 6.4 Báo cáo - 6.4.4 BC KM theo tháng")









    def reports_km_by_kh(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.report).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.report).click()
            time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.reports_km_by_kh).click()
        time.sleep(2)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.title_page1)))
            time.sleep(2)
        except:
            pass
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.4 Báo cáo - 6.4.5 BC KM theo KH",
                                              var_stx.title_page1, "6.4.5 BC KM theo KH", "_BCKMTheoKH.png")


    def reports_km_by_kh_search(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_reports_km_by_kh)
        except:
            report.reports_km_by_kh(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys("10/09/2025 00:00")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys("12/09/2025 02:59")
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.table_1_2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys("01/05/2025 00:00")
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys("02/06/2026 23:59")
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(5)

        module_other_stx.write_result_text_try_if_other(code, eventname, result, "KHUYẾN MẠI - 6.4 Báo cáo - 6.4.5 BC KM theo KH",
                                              var_stx.table_1_2, "", "_BCKMTheoKH_TimKiem.png")


    def reports_km_by_kh_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_reports_km_by_kh)
            var_stx.driver.find_element(By.XPATH, var_stx.table_1_2)
        except:
            report.reports_km_by_kh_search(self, "", "", "")

        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        time.sleep(5)
        get_info_web1()
        try:
            minitor_stx.get_info_excel(5, "Sheet 1")
        except:
            var_stx.driver.refresh()
            time.sleep(7)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(5)
            var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
            time.sleep(5)
            get_info_web1()
            minitor_stx.get_info_excel(5, "Sheet 1")
        minitor_stx.check_info_web_excel(code, eventname, result, "KHUYẾN MẠI - 6.4 Báo cáo - 6.4.5 BC KM theo KH")









    def reports_km_by_lx(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.report).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.report).click()
            time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.reports_km_by_lx).click()
        time.sleep(2)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.title_page1)))
            time.sleep(2)
        except:
            pass
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.4 Báo cáo - 6.4.6 BC KM theo LX",
                                                  var_stx.title_page1, "6.4.6 BC KM theo LX", "_BCKMTheoLX.png")


    def reports_km_by_lx_search(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_reports_km_by_lx)
        except:
            report.reports_km_by_lx(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys("10/09/2025 00:00")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys("17/09/2025 23:59")
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.table_1_2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys("02/07/2025 23:59")
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys("02/06/2026 23:59")
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(5)

        module_other_stx.write_result_text_try_if_other(code, eventname, result, "KHUYẾN MẠI - 6.4 Báo cáo - 6.4.6 BC KM theo LX",
                                              var_stx.table_1_2, "", "_BCKMTheoLX_TimKiem.png")


    def reports_km_by_lx_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_reports_km_by_lx)
            var_stx.driver.find_element(By.XPATH, var_stx.table_1_2)
        except:
            report.reports_km_by_lx_search(self, "", "", "")

        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        time.sleep(5)
        get_info_web1()
        try:
            minitor_stx.get_info_excel(5, "Sheet 1")
        except:
            var_stx.driver.refresh()
            time.sleep(7)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(5)
            var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
            time.sleep(5)
            get_info_web1()
            minitor_stx.get_info_excel(5, "Sheet 1")
        minitor_stx.check_info_web_excel(code, eventname, result, "KHUYẾN MẠI - 6.4 Báo cáo - 6.4.6 BC KM theo LX")









    def reports_km_by_customer(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.report).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.report).click()
            time.sleep(2)

        var_stx.driver.find_element(By.XPATH, var_stx.reports_km_by_customer).click()
        time.sleep(2)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.title_page1)))
            time.sleep(2)
        except:
            pass

        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.4 Báo cáo - 6.4.7 BC KM theo cuốc khách",
                                                  var_stx.title_page1, "6.4.7 BC KM theo cuốc khách", "_BCKMTheoCuocKhach.png")


    def reports_km_by_customer_search(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_reports_km_by_customer)
        except:
            report.reports_km_by_customer(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys("01/05/2025 00:00")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys("02/06/2025 23:59")
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.list_data2_2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys("02/07/2025 23:59")
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys("02/06/2026 23:59")
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(5)

        module_other_stx.write_result_text_try_if_other(code, eventname, result, "KHUYẾN MẠI - 6.4 Báo cáo - 6.4.7 BC KM theo cuốc khách",
                                              var_stx.list_data2_2, "", "_BCKMTheoCuocKhach_TimKiem.png")


    def reports_km_by_customer_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_reports_km_by_customer)
            var_stx.driver.find_element(By.XPATH, var_stx.list_data2_2)
        except:
            report.reports_km_by_customer_search(self, "", "", "")

        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        time.sleep(5)
        minitor_stx.get_info_web()
        try:
            minitor_stx.get_info_excel(5, "Sheet 1")
        except:
            var_stx.driver.refresh()
            time.sleep(7)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(5)
            var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
            time.sleep(5)
            minitor_stx.get_info_web()
            minitor_stx.get_info_excel(5, "Sheet 1")
        minitor_stx.check_info_web_excel(code, eventname, result, "KHUYẾN MẠI - 6.4 Báo cáo - 6.4.7 BC KM theo cuốc khách")









    def reports_km_not_use(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.report).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.report).click()
            time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.reports_km_not_use).click()
        time.sleep(2)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.title_page1)))
            time.sleep(2)
        except:
            pass
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.4 Báo cáo - 6.4.8 BC mã KM chưa sử dụng",
                                                  var_stx.title_page1, "6.4.8 BC mã KM chưa sử dụng", "_BCKMChuaSuDung.png")


    def reports_km_not_use_search(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_reports_km_not_use)
        except:
            report.reports_km_not_use(self, "", "", "")


        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(7)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.table_1_2)
        except:
            var_stx.driver.refresh()
            time.sleep(5)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(5)

        module_other_stx.write_result_text_try_if_other(code, eventname, result, "KHUYẾN MẠI - 6.4 Báo cáo - 6.4.8 BC mã KM chưa sử dụng",
                                              var_stx.table_1_2, "", "_BCKMChuaSuDung_TimKiem.png")


    def reports_km_not_use_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_reports_km_not_use)
            var_stx.driver.find_element(By.XPATH, var_stx.table_1_2)
        except:
            report.reports_km_not_use_search(self, "", "", "")

        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        time.sleep(7)
        get_info_web1()
        try:
            minitor_stx.get_info_excel(5, "Sheet 1")
        except:
            var_stx.driver.refresh()
            time.sleep(7)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(7)
            var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
            time.sleep(7)
            get_info_web1()
            minitor_stx.get_info_excel(5, "Sheet 1")
        minitor_stx.check_info_web_excel(code, eventname, result, "KHUYẾN MẠI - 6.4 Báo cáo - 6.4.8 BC mã KM chưa sử dụng")







    def referral_account_summary_report(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.report).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.report).click()
            time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.referral_account_summary_report).click()
        time.sleep(2)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.title_page1)))
            time.sleep(2)
        except:
            pass
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.4 Báo cáo - 6.4.9 BC tổng hợp tài khoản giới thiệu",
                                                  var_stx.title_page1, "6.4.9 BC tổng hợp tài khoản giới thiệu", "_BCTongHopTaiKhoanGioithieu.png")


    def referral_account_summary_report_search(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_referral_account_summary_report)
        except:
            report.referral_account_summary_report(self, "", "", "")


        var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys("3/5/2025 00:00")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys("2/6/2025 8:51")
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.table_1_2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys("2/6=4/2025 8:51")
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(Keys.CONTROL, "a", Keys.DELETE)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys("2/6/2025 8:51")
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(5)

        module_other_stx.write_result_text_try_if_other(code, eventname, result, "KHUYẾN MẠI - 6.4 Báo cáo - 6.4.9 BC tổng hợp tài khoản giới thiệu",
                                              var_stx.table_1_2, "", "_BCTongHopTaiKhoanGioithieu_TimKiem.png")


    def referral_account_summary_report_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_referral_account_summary_report)
            var_stx.driver.find_element(By.XPATH, var_stx.table_1_2)
        except:
            report.referral_account_summary_report_search(self, "", "", "")

        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        time.sleep(7)
        get_info_web1()
        try:
            minitor_stx.get_info_excel(5, "Sheet 1")
        except:
            var_stx.driver.refresh()
            time.sleep(7)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(5)
            var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
            time.sleep(7)
            get_info_web1()
            minitor_stx.get_info_excel(5, "Sheet 1")
        minitor_stx.check_info_web_excel(code, eventname, result, "KHUYẾN MẠI - 6.4 Báo cáo - 6.4.9 BC tổng hợp tài khoản giới thiệu")






class list_account_introduce:


    def list_account_introduce(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.list_account_introduce).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.list_account_introduce).click()
        time.sleep(2)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.title_page)))
            time.sleep(2)
        except:
            pass
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.11 Danh sách loại tài khoản giới thiệu",
                                                  var_stx.title_page, "6.11 Danh sách loại tài khoản giới thiệu", "_DanhSachLoaiTaiKhoanGioithieu.png")


    def list_account_introduce_g7_test(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx_g7test(self, var_stx.data['login']['tk_admin_test'],  var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.list_account_introduce).click()
        time.sleep(3.5)


    def list_account_introduce_search(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_account_introduce)
        except:
            list_account_introduce.list_account_introduce(self, "", "", "")


        data = var_stx.driver.find_element(By.XPATH, var_stx.table_2_2).text
        var_stx.driver.find_element(By.XPATH, var_stx.name).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.table_1_2)
        except:
            var_stx.driver.refresh()
            time.sleep(5)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(5)

        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.11 Danh sách loại tài khoản giới thiệu",
                                              var_stx.table_1_2, data, "_DanhSachLoaiTaiKhoanGioithieu_TimKiem.png")


    def list_account_introduce_addnew(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_account_introduce)
        except:
            list_account_introduce.list_account_introduce(self, "", "", "")

        account_introduce = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 26, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.name).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        var_stx.driver.find_element(By.XPATH, var_stx.name).send_keys(account_introduce)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3)
        try:
            name_account = var_stx.driver.find_element(By.XPATH, var_stx.table_1_2).text
            if name_account == account_introduce:
                var_stx.driver.find_element(By.XPATH, var_stx.list_promotion_delete).click()
                time.sleep(3)
                try:
                    var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
                except:
                    pass
                time.sleep(2)
                try:
                    var_stx.driver.find_element(By.XPATH, var_stx.close).click()
                    time.sleep(2.5)
                except:
                    pass
            else:
                var_stx.driver.find_element(By.XPATH, var_stx.name).send_keys(Keys.CONTROL, "a", Keys.DELETE)
                time.sleep(1)
                var_stx.driver.find_element(By.XPATH, var_stx.search).click()
                time.sleep(3)
        except:
            pass

        vehicle_driver_stx.increase()
        number = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 7, 2))
        var_stx.driver.find_element(By.XPATH, var_stx.add_new1).click()
        time.sleep(2.5)
        var_stx.driver.find_element(By.XPATH, var_stx.list_account_introduce_addnew_input).send_keys("Auto_account_"+number)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new2).click()
        time.sleep(2.5)

        var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 26, 2, "Auto_account_"+number)
        module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 14, "Auto_account_"+number)


        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.11 Danh sách loại tài khoản giới thiệu",
                                              var_stx.message, "Lưu loại tài khoản giới thiệu thành công.", "_DanhSachLoaiTaiKhoanGioithieu_ThemMoi.png")
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.close).click()
            time.sleep(4)
        except:
            pass


    def list_account_introduce_delete(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_account_introduce)
        except:
            list_account_introduce.list_account_introduce_addnew(self, "", "", "")



        account_introduce = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 26, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.name).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        var_stx.driver.find_element(By.XPATH, var_stx.name).send_keys(account_introduce)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3)
        name_account = var_stx.driver.find_element(By.XPATH, var_stx.table_1_2).text
        if name_account == account_introduce:
            var_stx.driver.find_element(By.XPATH, var_stx.list_promotion_delete).click()
            time.sleep(3)
            try:
                var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
            except:
                pass
            time.sleep(2)
            module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.11 Danh sách loại tài khoản giới thiệu",
                                                      var_stx.message, "Xóa loại tài khoản giới thiệu thành công.", "_DanhSachLoaiTaiKhoanGioithieu_Xoa.png")

            try:
                var_stx.driver.find_element(By.XPATH, var_stx.close).click()
                time.sleep(2.5)
            except:
                pass








class list_group_account_introduce:


    def list_group_account_introduce(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.list_group_account_introduce).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.list_group_account_introduce).click()
        time.sleep(2)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.title_page)))
            time.sleep(2)
        except:
            pass
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.12 Danh sách nhóm tài khoản giới thiệu",
                                                  var_stx.title_page, "6.12 Danh sách nhóm tài khoản giới thiệu", "_DanhSachNhomTaiKhoanGioithieu.png")


    def list_group_account_introduce_g7_test(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx_g7test(self, var_stx.data['login']['tk_admin_test'],  var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.promotion).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.list_group_account_introduce).click()
        time.sleep(3.5)


    def list_group_account_introduce_search(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_group_account_introduce)
        except:
            list_group_account_introduce.list_group_account_introduce(self, "", "", "")

        data = var_stx.driver.find_element(By.XPATH, var_stx.table_2_2).text
        var_stx.driver.find_element(By.XPATH, var_stx.name).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.table_1_2)
        except:
            var_stx.driver.refresh()
            time.sleep(5)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(5)

        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.12 Danh sách nhóm tài khoản giới thiệu",
                                              var_stx.table_1_2, data, "_DanhSachNhomTaiKhoanGioithieu_TimKiem.png")


    def list_group_account_introduce_addnew(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_group_account_introduce)
        except:
            list_group_account_introduce.list_group_account_introduce(self, "", "", "")


        group_introduce = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 27, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.name).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        var_stx.driver.find_element(By.XPATH, var_stx.name).send_keys(group_introduce)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3)
        try:
            name_account = var_stx.driver.find_element(By.XPATH, var_stx.table_1_2).text
            if name_account == group_introduce:
                var_stx.driver.find_element(By.XPATH, var_stx.list_promotion_delete).click()
                time.sleep(3)
                try:
                    var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
                except:
                    pass
                time.sleep(2)
                try:
                    var_stx.driver.find_element(By.XPATH, var_stx.close).click()
                    time.sleep(2.5)
                except:
                    pass
            else:
                var_stx.driver.find_element(By.XPATH, var_stx.name).send_keys(Keys.CONTROL, "a", Keys.DELETE)
                time.sleep(1)
                var_stx.driver.find_element(By.XPATH, var_stx.search).click()
                time.sleep(3)
        except:
            pass

        vehicle_driver_stx.increase()
        number = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 7, 2))
        var_stx.driver.find_element(By.XPATH, var_stx.add_new1).click()
        time.sleep(2.5)
        var_stx.driver.find_element(By.XPATH, var_stx.list_account_introduce_addnew_input).send_keys("Auto_group_"+number)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.list_group_account_introduce_addnew_type1).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new2).click()
        time.sleep(2.5)

        var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 27, 2, "Auto_group_"+number)
        module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 14, "Auto_group_"+number)


        module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.12 Danh sách nhóm tài khoản giới thiệu",
                                              var_stx.message, "Lưu loại tài khoản giới thiệu thành công.", "_DanhSachNhomTaiKhoanGioithieu_ThemMoi.png")
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.close).click()
            time.sleep(4)
        except:
            pass


    def list_group_account_introduce_delete(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_group_account_introduce)
        except:
            list_group_account_introduce.list_group_account_introduce_addnew(self, "", "", "")

        group_introduce = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 27, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.name).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        var_stx.driver.find_element(By.XPATH, var_stx.name).send_keys(group_introduce)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3)
        name_account = var_stx.driver.find_element(By.XPATH, var_stx.table_1_2).text
        if name_account == group_introduce:
            var_stx.driver.find_element(By.XPATH, var_stx.list_promotion_delete).click()
            time.sleep(3)
            try:
                var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
            except:
                pass
            time.sleep(2)
            module_other_stx.write_result_text_try_if(code, eventname, result, "KHUYẾN MẠI - 6.12 Danh sách nhóm tài khoản giới thiệu",
                                                      var_stx.message, "Xóa loại tài khoản giới thiệu thành công.", "_DanhSachNhomTaiKhoanGioithieu_Xoa.png")

            try:
                var_stx.driver.find_element(By.XPATH, var_stx.close).click()
                time.sleep(2.5)
            except:
                pass






