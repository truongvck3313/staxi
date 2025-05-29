import logging
import var_stx
import time
import json
from selenium.webdriver.common.by import By
import module_other_stx
import login_stx
from seleniumwire.utils import decode as sw_decode
from selenium.webdriver.common.keys import Keys
import os
import shutil
import re
import openpyxl
from xls2xlsx import XLS2XLSX
import minitor_stx
import vehicle_driver_stx
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess
import random



def get_info_web():
    var_stx.driver.implicitly_wait(0.05)
    row = 119
    n = 0
    while (n < 50):
        n += 1
        n = str(n)
        row += 1
        path_column = "//*[@id='DataTables_Table_0']/thead/tr/th[" + n + "]"
        path_data = "//*[@id='DataTables_Table_0']/tbody/tr[1]/td[" + n + "]"
        path_data_a2 = "//*[@id='DataTables_Table_0']/tbody/tr[1]/td[" + n + "]/a"
        print(n)
        try:
            name_colum = var_stx.driver.find_element(By.XPATH, path_column).text
            print("ten cot web:" .format(name_colum))
            var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", row, 1, name_colum)

            name_data_a2 = var_stx.driver.find_element(By.XPATH, path_data_a2).text
            print("data cot web a:" .format(name_data_a2))
            var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", row, 2, name_data_a2)
        except:
            try:
                name_data = var_stx.driver.find_element(By.XPATH, path_data).text
                var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", row, 2, name_data)
                print("data cot web:" .format(name_data))
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
        path_column = "//*[@class='table table-hover table-bordered cf']/thead/tr/th[" + n + "]"
        path_data = "//*[@class='table table-hover table-bordered cf']/tbody/tr[1]/td[" + n + "]"
        print(n)
        try:
            name_colum = var_stx.driver.find_element(By.XPATH, path_column).text
            print("ten cot web:" .format(name_colum))
            var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", row, 1, name_colum)

            name_data = var_stx.driver.find_element(By.XPATH, path_data).text
            var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", row, 2, name_data)
            print("data cot web:" .format(name_data))
        except:
            pass

        n = int(n)







class admin_10_1:


    def admin_10_1_1(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_1).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_1).click()
            time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.admin_10_1_1).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.1 Cấu hình điều xe nâng cao - 10.1.1 Danh sách bộ phương pháp điều xe",
                                                  var_stx.title_page1, "10.1.1 Danh sách bộ phương pháp điều xe", "_DanhSachBoPhuongPhapDieuXe.png")


    def admin_10_1_1_search(self, code, eventname, result, type_check):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_1_1)
        except:
            admin_10_1.admin_10_1_1(self, "", "", "")


        var_stx.driver.find_element(By.XPATH, var_stx.name).clear()
        time.sleep(0.3)
        var_stx.driver.find_element(By.XPATH, var_stx.OperatorId).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)

        if type_check == "0":
            data = var_stx.driver.find_element(By.XPATH, var_stx.table_2_2).text
            var_stx.driver.find_element(By.XPATH, var_stx.name).send_keys(data)
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(3.5)
            module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.1 Cấu hình điều xe nâng cao - 10.1.1 Danh sách bộ phương pháp điều xe",
                                                            var_stx.table_1_2, data, "_DanhSachBoPhuongPhapDieuXe_Ten.png")

        if type_check == "1":
            var_stx.driver.find_element(By.XPATH, var_stx.OperatorId4).click()
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(3.5)
            module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.1 Cấu hình điều xe nâng cao - 10.1.1 Danh sách bộ phương pháp điều xe",
                                                            var_stx.table_1_3, "Điều tuần tự", "_DanhSachBoPhuongPhapDieuXe_PhuongPhapDieu.png")






class admin_10_3:


    def admin_10_3_1(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx_envang(self, var_stx.data['login']['tk_admin'], var_stx.data['login']['mk_admin'])
        var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
        time.sleep(2)
        try:
            var_stx.driver.implicitly_wait(1)
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_3).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_3).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.admin_10_3_1).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.3 Quản trị công ty - 10.3.1 Thông tin công ty ",
                                                  var_stx.title_page1, "10.3.1 Thông tin công ty", "_ThongTinCongTy.png")


    def admin_10_3_1_save(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_3_1)
        except:
            admin_10_3.admin_10_3_1(self, "", "", "")

        vehicle_driver_stx.increase()
        number = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 7, 2))


        var_stx.driver.find_element(By.XPATH, var_stx.info_company_name).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_company_name).send_keys("En Vang HP")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.info_company_name_app).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_company_name_app).send_keys("En vang test")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.info_company_adress).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_company_adress).send_keys("Hải Phòng")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.info_company_phone).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_company_phone).send_keys("02253777999")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.info_company_code_hd).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_company_code_hd).send_keys("Auto_"+number)
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.info_company_stt).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_company_stt).send_keys("2")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.info_company_mail).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_company_mail).send_keys("envanghp@gmail.com")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.info_company_name2).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_company_name2).send_keys("Én Vàng Taxi")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.info_company_path_company).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_company_path_company).send_keys("http://localhost:18445/Media/Uploads/01-49-01-builink-giai-doan-bitcoin-halving.jpg")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.info_company_path_image).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_company_path_image).send_keys("https://envanghpbak.staxi.vn/Media/Uploads/Background-01.png")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.info_company_pin).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_company_pin).send_keys("8634343222")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.info_company_web).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_company_web).send_keys("https://envanghpbak.staxi.vn/Company/Info?4515111")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.info_company_logo).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_company_logo).send_keys("http://localhost:18445/Media/Uploads/01-49-01-builink-giai-doan-bitcoin-halving.jpg")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.info_company_tax).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_company_tax).send_keys("3500247383")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.info_company_person).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_company_person).send_keys("Nguyễn Văn A")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.info_company_describe).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_company_describe).send_keys("Công ty test nhập thông tin công ty")
        time.sleep(0.5)

        iframe = var_stx.driver.find_element(By.XPATH, var_stx.promotion_add_new_conten)
        var_stx.driver.switch_to.frame(iframe)
        content_area = var_stx.driver.find_element(By.XPATH, var_stx.promotion_add_new_conten_body)
        # content_area.clear()
        time.sleep(0.5)
        # content_area.send_keys("Trường test thông tin công ty")
        content_area.click()
        var_stx.driver.switch_to.default_content()

        time.sleep(1)
        element = var_stx.driver.find_element(By.XPATH, "//*[text()='Đồng bộ khách hàng']")
        var_stx.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)


        var_stx.driver.find_element(By.XPATH, var_stx.save3).click()
        time.sleep(2.5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.3 Quản trị công ty - 10.3.1 Thông tin công ty ",
                                                  var_stx.update_success1, "Cập nhật thành công.", "_ThongTinCongTy_Luu.png")


    def admin_10_3_1_sync_driver(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_3_1)
        except:
            admin_10_3.admin_10_3_1(self, "", "", "")

        time.sleep(1)
        element = var_stx.driver.find_element(By.XPATH, "//*[text()='Đồng bộ khách hàng']")
        var_stx.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.sync_driver).click()
        time.sleep(2)

        var_stx.driver.find_element(By.XPATH, var_stx.update_version_CommandVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.update_version_CommandVersion).send_keys("164")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.update_version_VehicleTypeVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.update_version_VehicleTypeVersion).send_keys("214")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.update_version_FloorVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.update_version_FloorVersion).send_keys("151")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.update_version_SurchargeVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.update_version_SurchargeVersion).send_keys("302")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.update_version_CompanyVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.update_version_CompanyVersion).send_keys("352")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.update_version_LandmarkVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.update_version_LandmarkVersion).send_keys("203")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.update_version_ConfigVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.update_version_ConfigVersion).send_keys("612")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.update_version_PriceVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.update_version_PriceVersion).send_keys("295")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.update_version_RegionVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.update_version_RegionVersion).send_keys("353")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.update_version_AcronymVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.update_version_AcronymVersion).send_keys("381")
        time.sleep(1)

        var_stx.driver.find_element(By.XPATH, var_stx.igree3).click()
        time.sleep(1)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.3 Quản trị công ty - 10.3.1 Thông tin công ty ",
                                                  var_stx.check_sync_driver, "Cập nhật phiên bản đồng bộ lái xe thành công.", "_ThongTinCongTy_DongBoLaiXe.png")
        time.sleep(3)


    def admin_10_3_1_sync_customer(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_3_1)
        except:
            admin_10_3.admin_10_3_1(self, "", "", "")

        time.sleep(1)
        element = var_stx.driver.find_element(By.XPATH, "//*[text()='Đồng bộ khách hàng']")
        var_stx.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer).click()
        time.sleep(2)

        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_CompanyVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_CompanyVersion).send_keys("11")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_ConfigPriceListVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_ConfigPriceListVersion).send_keys("12")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_LandmarkRouteVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_LandmarkRouteVersion).send_keys("11")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_AdminFeedbackTypeVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_AdminFeedbackTypeVersion).send_keys("11")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_VehicleTypeVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_VehicleTypeVersion).send_keys("11")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_LandmarkVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_LandmarkVersion).send_keys("11")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_LandmarkRouteVehicleTypeVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_LandmarkRouteVehicleTypeVersion).send_keys("11")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_ConfigCustVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_ConfigCustVersion).send_keys("14")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_HighlightAddressVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_HighlightAddressVersion).send_keys("11")
        time.sleep(1)

        var_stx.driver.find_element(By.XPATH, var_stx.igree3).click()
        time.sleep(1)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.3 Quản trị công ty - 10.3.1 Thông tin công ty ",
                                                  var_stx.check_sync_customer, "Cập nhật phiên bản đồng bộ khách hàng thành công.", "_ThongTinCongTy_DongBoKhachHang.png")
        time.sleep(2.5)


    def admin_10_3_1_back(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_3_1)
        except:
            admin_10_3.admin_10_3_1(self, "", "", "")

        time.sleep(1)

        var_stx.driver.find_element(By.XPATH, var_stx.back).click()
        time.sleep(3)
        module_other_stx.write_result_not_displayed_try(code, eventname, result, "BÁO CÁO - 10.3 Quản trị công ty - 10.3.1 Thông tin công ty ",
                                                  var_stx.check_admin_10_3_1, "_ThongTinCongTy_QuayLai.png")







    def admin_10_3_5(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_3).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_3).click()
            time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.admin_10_3_5).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.3 Quản trị công ty - 10.3.5 Quản trị tên xe",
                                                  var_stx.title_page1, "10.3.5 Quản trị tên xe", "_QuanTriTenXe.png")


    def admin_10_3_5_search(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_3_5)
        except:
            admin_10_3.admin_10_3_5(self, "", "", "")


        data = var_stx.driver.find_element(By.XPATH, var_stx.data_table2_2).text
        var_stx.driver.find_element(By.XPATH, var_stx.name_driver).send_keys(data)
        time.sleep(4)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.3 Quản trị công ty - 10.3.5 Quản trị tên xe",
                                                  var_stx.data_table1_2, data, "_QuanTriTenXe_TimKiem.png")

        var_stx.driver.find_element(By.XPATH, var_stx.name_driver).clear()
        time.sleep(1)


    def admin_10_3_5_add_new(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_3_5)
        except:
            admin_10_3.admin_10_3_5(self, "", "", "")

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.name_driver).clear()
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.name_driver).send_keys(var_stx.data['admin']['manager_vehicle_addnew'])
            time.sleep(3)
            name = var_stx.driver.find_element(By.XPATH, var_stx.data_table1_2).text
            if name == var_stx.data['admin']['manager_vehicle_addnew']:
                var_stx.driver.find_element(By.XPATH, var_stx.data_table1_3_button).click()
                time.sleep(2.5)
                var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
                time.sleep(1.5)
        except:
            pass

        try:
            admin_10_3.admin_10_3_5_delete(self, "", "", "")
        except:
            pass
        var_stx.driver.refresh()
        time.sleep(7)

        var_stx.driver.find_element(By.XPATH, var_stx.add_new1).click()
        time.sleep(2.5)
        var_stx.driver.find_element(By.XPATH, var_stx.id_name).send_keys(var_stx.data['admin']['manager_vehicle_addnew'])
        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new2).click()
        time.sleep(1.5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.3 Quản trị công ty - 10.3.5 Quản trị tên xe",
                                                  var_stx.toast_message, "Lưu tên xe thành công.", "_QuanTriTenXe_ThemMoi.png")
        time.sleep(2)


    def admin_10_3_5_update(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_3_5)
        except:
            admin_10_3.admin_10_3_5(self, "", "", "")
        var_stx.driver.refresh()
        time.sleep(5)
        var_stx.driver.find_element(By.XPATH, var_stx.name_driver).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.name_driver).send_keys(var_stx.data['admin']['manager_vehicle_addnew'])
        time.sleep(3)
        name = var_stx.driver.find_element(By.XPATH, var_stx.data_table1_2).text
        if name == var_stx.data['admin']['manager_vehicle_addnew']:
            var_stx.driver.find_element(By.XPATH, var_stx.data_table1_2).click()
            time.sleep(2.5)
            var_stx.driver.find_element(By.XPATH, var_stx.id_name).clear()
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.id_name).send_keys(var_stx.data['admin']['manager_vehicle_addnew_edit'])
            time.sleep(1.5)
            var_stx.driver.find_element(By.XPATH, var_stx.update).click()
            time.sleep(1.5)
            module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.3 Quản trị công ty - 10.3.5 Quản trị tên xe",
                                                      var_stx.toast_message, "Cập nhật tên xe thành công.", "_QuanTriTenXe_CapNhat.png")
            time.sleep(2)


    def admin_10_3_5_delete(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_3_5)
        except:
            admin_10_3.admin_10_3_5(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.name_driver).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.name_driver).send_keys(var_stx.data['admin']['manager_vehicle_addnew_edit'])
        time.sleep(3)
        name = var_stx.driver.find_element(By.XPATH, var_stx.data_table1_2).text
        if name == var_stx.data['admin']['manager_vehicle_addnew_edit']:
            var_stx.driver.find_element(By.XPATH, var_stx.data_table1_3_button).click()
            time.sleep(2.5)
            var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
            time.sleep(1.5)
            module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.3 Quản trị công ty - 10.3.5 Quản trị tên xe",
                                                      var_stx.toast_message, "Xóa tên xe thành công.", "_QuanTriTenXe_Xoa.png")
            var_stx.driver.find_element(By.XPATH, var_stx.name_driver).clear()
            time.sleep(2)








    def admin_10_3_6(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_3).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_3).click()
            time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.admin_10_3_6).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.3 Quản trị công ty - 10.3.6 Quản trị loại xe",
                                                  var_stx.title_page1, "10.3.6 Quản trị loại xe", "_QuanTriLaiXe.png")


    def admin_10_3_6_combobox(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_3_6)
        except:
            admin_10_3.admin_10_3_6(self, "", "", "")

        # var_stx.driver.find_element(By.XPATH, var_stx.PartnerCarType).click()
        # time.sleep(1.5)
        # data = var_stx.driver.find_element(By.XPATH, var_stx.PartnerCarType).text
        #
        #
        #
        # var_stx.driver.find_element(By.XPATH, var_stx.name_driver).send_keys(data)
        # time.sleep(3)
        # module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.3 Quản trị công ty - 10.3.5 Quản trị tên xe",
        #                                           var_stx.data_table1_2, data, "_QuanTriTenXe_TimKiem.png")


    def admin_10_3_6_sync_driver(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_3_6)
        except:
            admin_10_3.admin_10_3_6(self, "", "", "")


        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.icon_sync_driver).click()
        time.sleep(2.5)
        var_stx.driver.find_element(By.XPATH, var_stx.update_version_CommandVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.update_version_CommandVersion).send_keys("573")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.update_version_VehicleTypeVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.update_version_VehicleTypeVersion).send_keys("588")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.update_version_FloorVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.update_version_FloorVersion).send_keys("6954")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.update_version_SurchargeVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.update_version_SurchargeVersion).send_keys("592")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.update_version_CompanyVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.update_version_CompanyVersion).send_keys("600")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.update_version_LandmarkVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.update_version_LandmarkVersion).send_keys("601")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.update_version_ConfigVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.update_version_ConfigVersion).send_keys("948")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.update_version_PriceVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.update_version_PriceVersion).send_keys("601")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.update_version_RegionVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.update_version_RegionVersion).send_keys("601")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.update_version_AcronymVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.update_version_AcronymVersion).send_keys("586")
        time.sleep(1)

        var_stx.driver.find_element(By.XPATH, var_stx.igree3).click()
        time.sleep(1)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.3 Quản trị công ty - 10.3.6 Quản trị loại xe",
                                                  var_stx.check_sync_driver, "Cập nhật phiên bản đồng bộ lái xe thành công.", "_QuanTriLoaiXe_DongBoLaiXe.png")
        time.sleep(3)


    def admin_10_3_6_sync_customer(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_3_6)
        except:
            admin_10_3.admin_10_3_6(self, "", "", "")


        var_stx.driver.find_element(By.XPATH, var_stx.icon_sync_customer).click()
        time.sleep(2.5)

        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_CompanyVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_CompanyVersion).send_keys("614")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_ConfigPriceListVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_ConfigPriceListVersion).send_keys("10029")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_LandmarkRouteVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_LandmarkRouteVersion).send_keys("639")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_AdminFeedbackTypeVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_AdminFeedbackTypeVersion).send_keys("612")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_VehicleTypeVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_VehicleTypeVersion).send_keys("630")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_LandmarkVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_LandmarkVersion).send_keys("620")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_LandmarkRouteVehicleTypeVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_LandmarkRouteVehicleTypeVersion).send_keys("6038")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_ConfigCustVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_ConfigCustVersion).send_keys("838")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_HighlightAddressVersion).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.sync_customer_HighlightAddressVersion).send_keys("612")
        time.sleep(1)

        var_stx.driver.find_element(By.XPATH, var_stx.igree3).click()
        time.sleep(1)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.3 Quản trị công ty - 10.3.6 Quản trị loại xe",
                                                  var_stx.check_sync_customer, "Cập nhật phiên bản đồng bộ khách hàng thành công.",
                                                  "_QuanTriLoaiXe_DongBoKhachHang.png")
        time.sleep(2.5)


    def admin_10_3_6_add_new(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_3_6)
        except:
            admin_10_3.admin_10_3_6(self, "", "", "")


        try:
            admin_10_3.delete_type_vehicle(self, var_stx.data['admin']['add_new_type_vehicle_name'])
        except:
            pass

        try:
            admin_10_3.delete_type_vehicle(self, var_stx.data['admin']['add_new_type_vehicle_name_edit'])
        except:
            pass


        var_stx.driver.find_element(By.XPATH, var_stx.add_new1).click()
        time.sleep(2.5)

        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_minitor).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_level5).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_province_hn).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_price_re).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_air_port).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_name_app).send_keys(var_stx.data['admin']['add_new_type_vehicle_name'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_name_eng).send_keys("4 convenient")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_seat).send_keys("4")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_stt).send_keys("1")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_icon_route).send_keys("ic_type_4_cho")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_icon_map).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_type_vehicle).click()
        time.sleep(1)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_type_vehicle1).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_type_vehicle2).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_kd).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_kd1).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_describe).send_keys("Trường test thêm mới loại xe")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_image).send_keys("https://g7test.staxi.vn/Media/Uploads/%E2%80%94Pngtree%E2%80%94car_flag_icon_333837.png")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_company).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_company1).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_money).send_keys("20000")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_v).send_keys("40")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_time_free).send_keys("5")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_weight).send_keys("200")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_display_price).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_price_customer).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_location).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_end).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_tn).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.save3).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.3 Quản trị công ty - 10.3.6 Quản trị loại xe",
                                                  "//*[text()='"+var_stx.data['admin']['add_new_type_vehicle_name']+"']",
                                                  var_stx.data['admin']['add_new_type_vehicle_name'], "_QuanTriLoaiXe_ThemMoi.png")


    def admin_10_3_6_update(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_3_6)
        except:
            admin_10_3.admin_10_3_6_add_new(self, "", "", "")

        button = var_stx.driver.find_element(By.XPATH, "//*[text()='"+var_stx.data['admin']['add_new_type_vehicle_name']+"']")
        var_stx.driver.execute_script("arguments[0].click();", button)
        time.sleep(2.5)

        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_name_app).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.type_vehicle_name_app).send_keys(var_stx.data['admin']['add_new_type_vehicle_name_edit'])
        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.update).click()
        time.sleep(3.5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.3 Quản trị công ty - 10.3.6 Quản trị loại xe",
                                                  "//*[text()='"+var_stx.data['admin']['add_new_type_vehicle_name_edit']+"']",
                                                  var_stx.data['admin']['add_new_type_vehicle_name_edit'], "_QuanTriLoaiXe_CapNhat.png")


    def delete_type_vehicle(self, name):
        var_stx.driver.implicitly_wait(0.05)
        n = 0
        while (n < 50):
            n += 1
            n = str(n)
            path_name = "//*[@class='table table-hover table-bordered cf']/tbody/tr[" + n + "]/td[2]/a"
            path_delete = "//*[@class='table table-hover table-bordered cf']/tbody/tr[" + n + "]/td[7]/a/i"
            print(n)
            print(path_name)
            print(path_delete)
            try:
                name_data = var_stx.driver.find_element(By.XPATH, path_name).text
                print("name:".format(name_data))
                if name_data == name:
                    var_stx.driver.find_element(By.XPATH, path_delete).click()
                    time.sleep(3)
                    var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
                    time.sleep(3)
                    break
            except:
                pass
            n = int(n)


    def admin_10_3_6_delete(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_3_6)
        except:
            # admin_10_3.admin_10_3_6_add_new(self, "", "", "")
            admin_10_3.admin_10_3_6(self, "", "", "")


        admin_10_3.delete_type_vehicle(self, var_stx.data['admin']['add_new_type_vehicle_name'])
        time.sleep(1)
        admin_10_3.delete_type_vehicle(self, var_stx.data['admin']['add_new_type_vehicle_name_edit'])


        module_other_stx.write_result_not_displayed_try(code, eventname, result, "BÁO CÁO - 10.3 Quản trị công ty - 10.3.6 Quản trị loại xe",
                                                  "//*[text()='"+var_stx.data['admin']['add_new_type_vehicle_name']+"']", "_QuanTriLoaiXe_Xoa.png")

        module_other_stx.write_result_not_displayed_try(code, eventname, result, "BÁO CÁO - 10.3 Quản trị công ty - 10.3.6 Quản trị loại xe",
                                                  "//*[text()='"+var_stx.data['admin']['add_new_type_vehicle_name_edit']+"']", "_QuanTriLoaiXe_Xoa.png")





class admin_10_5:


    def admin_10_5_5(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_5).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_5).click()
            time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.admin_10_5_5).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.5 Quản trị hệ thống - 10.5.5 Danh sách tài khoản",
                                                  var_stx.title_page1, "10.5.5 Danh sách tài khoản", "_DanhSachTaiKhoan.png")


    def admin_10_5_5_search(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_5_5)
        except:
            admin_10_5.admin_10_5_5(self, "", "", "")


        data = var_stx.driver.find_element(By.XPATH, var_stx.datatable2_2).text
        var_stx.driver.find_element(By.XPATH, var_stx.name_account).send_keys(data)
        time.sleep(3)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.5 Quản trị hệ thống - 10.5.5 Danh sách tài khoản",
                                                  var_stx.datatable1_2, data, "_DanhSachTaiKhoan_TimKiem.png")


    def admin_10_5_5_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(2)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_5_5)
        except:
            admin_10_5.admin_10_5_5(self, "", "", "")


        var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        time.sleep(7)
        get_info_web()
        minitor_stx.get_info_excel1(5, "Sheet 1")
        minitor_stx.check_info_web_excel(code, eventname, result, "BÁO CÁO - 10.5 Quản trị hệ thống - 10.5.5 Danh sách tài khoản")


    def admin_10_5_5_add_new(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_5_5)
        except:
            admin_10_5.admin_10_5_5(self, "", "", "")


        var_stx.driver.find_element(By.XPATH, var_stx.add_new1).click()
        time.sleep(2.5)

        vehicle_driver_stx.increase()
        number = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 7, 2))
        random1 = (random.randint(1000000, 9999999))
        random1 = str(random1)

        var_stx.driver.find_element(By.XPATH, var_stx.create_user_full_name).send_keys("Trần Quang Trường")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.create_user_account).send_keys("auto"+number)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.create_user_password1).send_keys("Aa@12345678")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.create_user_password2).send_keys("Aa@12345678")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.create_user_partner).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.create_user_role_minitor).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.sdt).send_keys("035"+random1)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.create_user_link_app).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.create_user_not_change_account).click()
        try:
            var_stx.driver.implicitly_wait(1)
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.create_user_use_app_admin).click()
        except:
            pass

        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.save3).click()
        time.sleep(1)

        wait = WebDriverWait(var_stx.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.toast_message)))

        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.5 Quản trị hệ thống - 10.5.5 Danh sách tài khoản",
                                                  var_stx.toast_message, "Tài khoản đã tạo thành công", "_DanhSachTaiKhoan_ThemMoi.png")

        module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 14, "auto"+number)
        var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 32, 2, "auto"+number)

        time.sleep(3)


    def admin_10_5_5_update(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_5_5)
        except:
            admin_10_5.admin_10_5_5(self, "", "", "")

        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 32, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.name_account).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.name_account).send_keys(data)
        time.sleep(4)
        name = var_stx.driver.find_element(By.XPATH, var_stx.datatable1_2).text
        if name == data:
            var_stx.driver.find_element(By.XPATH, var_stx.datatable1_2_a).click()
            time.sleep(2.5)
            var_stx.driver.find_element(By.XPATH, var_stx.fil_again_pass_word).clear()
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.fil_again_pass_word).send_keys("Aa@123456789")
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.save3).click()
            time.sleep(1)
            wait = WebDriverWait(var_stx.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.toast_message)))

            module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.3 Quản trị công ty - 10.3.5 Quản trị tên xe",
                                                      var_stx.toast_message, "Tài khoản đã thay đổi thành công", "_DanhSachTaiKhoan_CapNhat.png")
            time.sleep(2)


    def admin_10_5_5_get_code(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_5_5)
        except:
            admin_10_5.admin_10_5_5(self, "", "", "")

        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 32, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.name_account).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.name_account).send_keys(data)
        time.sleep(4)
        name = var_stx.driver.find_element(By.XPATH, var_stx.datatable1_2).text
        if name == data:
            var_stx.driver.find_element(By.XPATH, var_stx.datatable1_9_button).click()
            time.sleep(2.5)
            var_stx.driver.find_element(By.XPATH, var_stx.LockActiveCodeOld).click()
            time.sleep(3.5)
            var_stx.driver.find_element(By.XPATH, var_stx.coppy).click()
            time.sleep(5)
            var_stx.driver.find_element(By.XPATH, var_stx.get_code_active_new).click()
            time.sleep(1.2)
            module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.3 Quản trị công ty - 10.3.5 Quản trị tên xe",
                                                      var_stx.toast_message, "Mã kích hoạt được cập nhật thành công", "_DanhSachTaiKhoan_LayMaKichHoat.png")
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.get_code_active_exit).click()
            time.sleep(2)


    def admin_10_5_5_role(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_5_5)
        except:
            admin_10_5.admin_10_5_5_add_new(self, "", "", "")

        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 32, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.name_account).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.name_account).send_keys(data)
        time.sleep(4)
        name = var_stx.driver.find_element(By.XPATH, var_stx.datatable1_2).text
        if name == data:
            var_stx.driver.find_element(By.XPATH, var_stx.datatable1_10_a).click()
            time.sleep(3.5)
            wait = WebDriverWait(var_stx.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.assign_role_user)))
            time.sleep(1)
            module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.3 Quản trị công ty - 10.3.5 Quản trị tên xe",
                                                      var_stx.assign_role_user, "GÁN VAI TRÒ NGƯỜI DÙNG", "_DanhSachTaiKhoan_VaiTro.png")
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.role1).click()
            time.sleep(1.2)
            # var_stx.driver.find_element(By.XPATH, var_stx.role2).click()
            # time.sleep(1.2)
            var_stx.driver.find_element(By.XPATH, var_stx.user1).click()
            time.sleep(1.2)
            var_stx.driver.find_element(By.XPATH, var_stx.back).click()
            time.sleep(3)


    def admin_10_5_5_decentralization(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_5_5)
        except:
            admin_10_5.admin_10_5_5_add_new(self, "", "", "")

        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 32, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.name_account).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.name_account).send_keys(data)
        time.sleep(4)
        name = var_stx.driver.find_element(By.XPATH, var_stx.datatable1_2).text
        if name == data:
            var_stx.driver.find_element(By.XPATH, var_stx.datatable1_11_a).click()
            time.sleep(3.5)
            module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.3 Quản trị công ty - 10.3.5 Quản trị tên xe",
                                                      var_stx.list_role_assign, "DANH SÁCH QUYỀN ĐƯỢC GÁN", "_DanhSachTaiKhoan_PhanQuyen.png")

            var_stx.driver.find_element(By.XPATH, var_stx.back).click()
            time.sleep(3.5)


    def admin_10_5_5_config(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_5_5)
        except:
            admin_10_5.admin_10_5_5_add_new(self, "", "", "")

        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 32, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.name_account).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.name_account).send_keys(data)
        time.sleep(4)
        name = var_stx.driver.find_element(By.XPATH, var_stx.datatable1_2).text
        if name == data:
            # var_stx.driver.find_element(By.XPATH, var_stx.icon_config1).click()
            var_stx.driver.find_element(By.XPATH, var_stx.datatable1_12_a).click()
            time.sleep(2.5)
            try:
                var_stx.driver.find_element(By.XPATH, var_stx.RedirectPage).click()
            except:
                var_stx.driver.find_element(By.XPATH, var_stx.datatable1_12_a).click()
                time.sleep(2.5)
                var_stx.driver.find_element(By.XPATH, var_stx.RedirectPage).click()
            time.sleep(1.5)
            var_stx.driver.find_element(By.XPATH, var_stx.page_default_sumarry).click()
            time.sleep(1.5)
            var_stx.driver.find_element(By.XPATH, var_stx.save2).click()
            time.sleep(1.2)
            module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.3 Quản trị công ty - 10.3.5 Quản trị tên xe",
                                                      var_stx.toast_message, "Tài khoản đã thay đổi thành công.", "_DanhSachTaiKhoan_CauHinh.png")


    def admin_10_5_5_lock(self, code, eventname, result, desire, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_5_5)
        except:
            admin_10_5.admin_10_5_5_add_new(self, "", "", "")

        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 32, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.name_account).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.name_account).send_keys(data)
        time.sleep(4)
        name = var_stx.driver.find_element(By.XPATH, var_stx.datatable1_2).text
        if name == data:
            var_stx.driver.find_element(By.XPATH, var_stx.datatable1_13_i).click()
            time.sleep(2.5)
            var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
            time.sleep(1.5)
            module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.3 Quản trị công ty - 10.3.5 Quản trị tên xe",
                                                      var_stx.toast_message, desire, name_image)
            time.sleep(3)


    def admin_10_5_5_delete(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_5_5)
        except:
            admin_10_5.admin_10_5_5_add_new(self, "", "", "")

        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 32, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.name_account).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.name_account).send_keys(data)
        time.sleep(4)
        name = var_stx.driver.find_element(By.XPATH, var_stx.datatable1_2).text
        if name == data:
            var_stx.driver.find_element(By.XPATH, var_stx.datatable1_14_i).click()
            time.sleep(2.5)
            var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
            time.sleep(1.5)
            module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.3 Quản trị công ty - 10.3.5 Quản trị tên xe",
                                                      var_stx.toast_message, "Xóa thành công.", "_DanhSachTaiKhoan_Xoa.png")
            time.sleep(3)







    def admin_10_5_7(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_5).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_5).click()
            time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.admin_10_5_7).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.5 Quản trị hệ thống - 10.5.7 Lịch sử tài khoản",
                                                  var_stx.title_page1, "10.5.7 Lịch sử tài khoản", "_LichSuTaiKhoan.png")


    def admin_10_5_7_x(self):
        var_stx.driver.implicitly_wait(0.2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.name_account).clear()
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.data_change).clear()
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.table_impact_table).click()
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.type_action).click()
            time.sleep(0.3)
        except:
            pass


    def admin_10_5_7_detail(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_5_7)
        except:
            admin_10_5.admin_10_5_7(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.from_day).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(var_stx.data['admin']['from_day'])
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.to_day).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(var_stx.data['admin']['to_day'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.table_1_2_a)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.from_day).clear()
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.to_day).clear()
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(3)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(3)
        var_stx.driver.find_element(By.XPATH, var_stx.table_1_2_a).click()
        time.sleep(3)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.5 Quản trị hệ thống - 10.5.7 Lịch sử tài khoản",
                                                  var_stx.history_active, "LỊCH SỬ HOẠT ĐỘNG", "_LichSuTaiKhoan_ChiTiet.png")

        var_stx.driver.find_element(By.XPATH, var_stx.table_impact_table).click()
        time.sleep(3)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3)


    def admin_10_5_7_from_to_day(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.history_active)
        except:
            admin_10_5.admin_10_5_7_detail(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.from_day).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(var_stx.data['admin']['from_day'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(var_stx.data['admin']['to_day'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.list_data2_3)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.from_day).clear()
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys("03/03/2025 00:00")
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.to_day).clear()
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys("03/03/2025 23:59")
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(3)

        module_other_stx.write_result_text_try_if_cut2(code, eventname, result, "BÁO CÁO - 10.5 Quản trị hệ thống - 10.5.7 Lịch sử tài khoản",
                                                  var_stx.list_data2_3, "10/12/2024", "_LichSuTaiKhoan_ChiTiet.png", 0, 10)


    def admin_10_5_7_search(self, code, eventname, result, path_input, data, path_check, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.history_active)
        except:
            admin_10_5.admin_10_5_7_detail(self, "", "", "")

        admin_10_5.admin_10_5_7_x(self)


        var_stx.driver.find_element(By.XPATH, path_input).send_keys(data)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.5 Quản trị hệ thống - 10.5.7 Lịch sử tài khoản",
                                                  path_check, data, name_image)


    def admin_10_5_7_table(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.history_active)
        except:
            admin_10_5.admin_10_5_7_detail(self, "", "", "")

        admin_10_5.admin_10_5_7_x(self)

        var_stx.driver.find_element(By.XPATH, var_stx.table_user).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.5 Quản trị hệ thống - 10.5.7 Lịch sử tài khoản",
                                                  var_stx.list_data_2_5, "Người dùng hệ thống (AdminUser)", "_LichSuTaiKhoan_BangTacDong.png")


    def admin_10_5_7_type_action(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.history_active)
        except:
            admin_10_5.admin_10_5_7_detail(self, "", "", "")

        admin_10_5.admin_10_5_7_x(self)

        var_stx.driver.find_element(By.XPATH, var_stx.type_action_edit).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.5 Quản trị hệ thống - 10.5.7 Lịch sử tài khoản",
                                                  var_stx.list_data_2_4, "Sửa", "_LichSuTaiKhoan_LoaiHanhDong.png")





class admin_10_6:


    def admin_10_6_1(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6).click()
            time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6_1).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.6 Cấu hình hệ thống - 10.6.1 Cấu hình lái xe",
                                                  var_stx.title_page1, "10.6.1 Cấu hình lái xe", "_CauHinhLaiXe.png")

    def admin_10_6_1_check(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_6_1)
        except:
            admin_10_6.admin_10_6_1(self, "", "", "")

        logging.info("-------------------------")
        logging.info("BÁO CÁO - 10.6 Cấu hình hệ thống - 10.6.1 Cấu hình lái xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            flied1 = var_stx.driver.find_element(By.XPATH, var_stx.datatable1_1).text
            flied2 = var_stx.driver.find_element(By.XPATH, var_stx.datatable1_2).text
            flied3 = var_stx.driver.find_element(By.XPATH, var_stx.datatable1_3).text
            flied4 = var_stx.driver.find_element(By.XPATH, var_stx.datatable1_4).text
            flied5 = var_stx.driver.find_element(By.XPATH, var_stx.datatable1_5).text
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "STT: {}\nTên cấu hình: {}\nGiá trị: {}\nKiểu dữ liệu: {}\nGhi chú: {}"
                                       .format(flied1, flied2, flied3, flied4, flied5))
            if (flied1 and flied2 and flied3 and flied4 != None):
                logging.info("True")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_stx.driver.save_screenshot(var_stx.imagepath + code + "_CauHinhLaiXe_CheckHienThi.png")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_CauHinhLaiXe_CheckHienThi.png")
        except:
            logging.info("False")
            var_stx.driver.save_screenshot(var_stx.imagepath + code + "_CauHinhLaiXe_CheckHienThi.png")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_CauHinhLaiXe_CheckHienThi.png")




    def admin_10_6_2(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6).click()
            time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6_2).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.6 Cấu hình hệ thống - 10.6.2 Cấu hình khách hàng",
                                                  var_stx.title_page1, "10.6.2 Cấu hình khách hàng", "_CauHinhKhachHang.png")

    def admin_10_6_2_check(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_6_2)
        except:
            admin_10_6.admin_10_6_2(self, "", "", "")

        logging.info("-------------------------")
        logging.info("BÁO CÁO - 10.6 Cấu hình hệ thống - 10.6.2 Cấu hình khách hàng")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            flied1 = var_stx.driver.find_element(By.XPATH, var_stx.datatable1_1).text
            flied2 = var_stx.driver.find_element(By.XPATH, var_stx.datatable1_2).text
            flied3 = var_stx.driver.find_element(By.XPATH, var_stx.datatable1_3).text
            flied4 = var_stx.driver.find_element(By.XPATH, var_stx.datatable1_4).text
            flied5 = var_stx.driver.find_element(By.XPATH, var_stx.datatable1_5).text
            flied6 = var_stx.driver.find_element(By.XPATH, var_stx.datatable1_6).text
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "STT: {}\nTên cấu hình: {}\nGiá trị: {}\nKiểu dữ liệu: {}\nCông ty: {}\nGhi chú: {}"
                                       .format(flied1, flied2, flied3, flied4, flied5, flied6))
            if (flied1 and flied2 and flied3 and flied4 and flied5 != None):
                logging.info("True")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_stx.driver.save_screenshot(var_stx.imagepath + code + "_CauHinhKhachHang_CheckHienThi.png")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_CauHinhKhachHang_CheckHienThi.png")
        except:
            logging.info("False")
            var_stx.driver.save_screenshot(var_stx.imagepath + code + "_CauHinhKhachHang_CheckHienThi.png")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_CauHinhKhachHang_CheckHienThi.png")




    def admin_10_6_3(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6).click()
            time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6_3).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.6 Cấu hình hệ thống - 10.6.3 Cấu hình quản trị",
                                                  var_stx.title_page1, "10.6.3 Cấu hình quản trị", "_CauHinhQuanTri.png")

    def admin_10_6_3_check(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_6_3)
        except:
            admin_10_6.admin_10_6_3(self, "", "", "")

        logging.info("-------------------------")
        logging.info("BÁO CÁO - 10.6 Cấu hình hệ thống - 10.6.3 Cấu hình quản trị")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            flied1 = var_stx.driver.find_element(By.XPATH, var_stx.table_1_1).text
            flied2 = var_stx.driver.find_element(By.XPATH, var_stx.table_1_2).text
            flied3 = var_stx.driver.find_element(By.XPATH, var_stx.table_1_3).text
            flied4 = var_stx.driver.find_element(By.XPATH, var_stx.table_1_4).text
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "STT: {}\nTên cấu hình: {}\nGiá trị: {}\nGhi chú: {}"
                                       .format(flied1, flied2, flied3, flied4))
            if (flied1 and flied2 and flied3 != None):
                logging.info("True")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_stx.driver.save_screenshot(var_stx.imagepath + code + "_CauHinhQuanTri_CheckHienThi.png")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_CauHinhQuanTri_CheckHienThi.png")
        except:
            logging.info("False")
            var_stx.driver.save_screenshot(var_stx.imagepath + code + "_CauHinhQuanTri_CheckHienThi.png")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_CauHinhQuanTri_CheckHienThi.png")




    def admin_10_6_4(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6).click()
            time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6_4).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.6 Cấu hình hệ thống - 10.6.4 Cấu hình server",
                                                  var_stx.title_page1, "10.6.4 Cấu hình server", "_CauHinhSever.png")

    def admin_10_6_4_check(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_6_4)
        except:
            admin_10_6.admin_10_6_4(self, "", "", "")

        logging.info("-------------------------")
        logging.info("BÁO CÁO - 10.6 Cấu hình hệ thống - 10.6.4 Cấu hình server")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            flied1 = var_stx.driver.find_element(By.XPATH, var_stx.table_1_1).text
            flied2 = var_stx.driver.find_element(By.XPATH, var_stx.table_1_2).text
            flied3 = var_stx.driver.find_element(By.XPATH, var_stx.table_1_3).text
            flied4 = var_stx.driver.find_element(By.XPATH, var_stx.table_1_4).text
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "STT: {}\nTên cấu hình: {}\nGiá trị: {}\nGhi chú: {}"
                                       .format(flied1, flied2, flied3, flied4))
            if (flied1 and flied2 and flied3 != None):
                logging.info("True")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_stx.driver.save_screenshot(var_stx.imagepath + code + "_CauHinhSever_CheckHienThi.png")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_CauHinhSever_CheckHienThi.png")
        except:
            logging.info("False")
            var_stx.driver.save_screenshot(var_stx.imagepath + code + "_CauHinhSever_CheckHienThi.png")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_CauHinhSever_CheckHienThi.png")



    def admin_10_6_5(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6).click()
            time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6_5).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.6 Cấu hình hệ thống - 10.6.5 Cấu hình tin nhắn",
                                                  var_stx.title_page1, "10.6.5 Cấu hình tin nhắn", "_CauHinhTinNhan.png")

    def admin_10_6_5_check(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_6_5)
        except:
            admin_10_6.admin_10_6_5(self, "", "", "")

        logging.info("-------------------------")
        logging.info("BÁO CÁO - 10.6 Cấu hình hệ thống - 10.6.5 Cấu hình tin nhắn")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            flied1 = var_stx.driver.find_element(By.XPATH, var_stx.table_1_1).text
            flied2 = var_stx.driver.find_element(By.XPATH, var_stx.table_1_2).text
            flied3 = var_stx.driver.find_element(By.XPATH, var_stx.table_1_3).text
            flied4 = var_stx.driver.find_element(By.XPATH, var_stx.table_1_4).text
            flied5 = var_stx.driver.find_element(By.XPATH, var_stx.table_1_5).text
            flied6 = var_stx.driver.find_element(By.XPATH, var_stx.table_1_6).text
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "STT: {}\nNhóm tuyến: {}\nTên cấu hình: {}\nThời điểm: {}\nTrạng thái: {}\nGhi chú: {}"
                                       .format(flied1, flied2, flied3, flied4, flied5, flied6))
            if (flied1 and flied2 and flied3 and flied4 and flied5 and flied6 != None):
                logging.info("True")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_stx.driver.save_screenshot(var_stx.imagepath + code + "_CauHinhTinNhan_CheckHienThi.png")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_CauHinhTinNhan_CheckHienThi.png")
        except:
            logging.info("False")
            var_stx.driver.save_screenshot(var_stx.imagepath + code + "_CauHinhTinNhan_CheckHienThi.png")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_CauHinhTinNhan_CheckHienThi.png")




    def admin_10_6_6(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6).click()
            time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6_6).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.6 Cấu hình hệ thống - 10.6.6 Mẫu tin nhắn",
                                                  var_stx.title_page1, "10.6.6 Mẫu tin nhắn", "_MauTinNhan.png")


    def admin_10_6_6_check(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_6_6)
        except:
            admin_10_6.admin_10_6_6(self, "", "", "")

        logging.info("-------------------------")
        logging.info("BÁO CÁO - 10.6 Cấu hình hệ thống - 10.6.6 Mẫu tin nhắn")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            flied1 = var_stx.driver.find_element(By.XPATH, var_stx.list_data1).text
            flied2 = var_stx.driver.find_element(By.XPATH, var_stx.list_data2).text
            flied3 = var_stx.driver.find_element(By.XPATH, var_stx.list_data3).text
            flied4 = var_stx.driver.find_element(By.XPATH, var_stx.list_data4).text
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "STT: {}\nMã số: {}\nNội dung: {}\nTham số: {}"
                                       .format(flied1, flied2, flied3, flied4))
            if (flied1 and flied2 and flied3 and flied4 != None):
                logging.info("True")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_stx.driver.save_screenshot(var_stx.imagepath + code + "_MauTinNhan_CheckHienThi.png")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_MauTinNhan_CheckHienThi.png")
        except:
            logging.info("False")
            var_stx.driver.save_screenshot(var_stx.imagepath + code + "_MauTinNhan_CheckHienThi.png")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_MauTinNhan_CheckHienThi.png")




    def admin_10_6_7(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6).click()
            time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6_7).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.6 Cấu hình hệ thống - 10.6.7 Cấu hình bản đồ",
                                                  var_stx.title_page1, "10.6.7 Cấu hình bản đồ", "_CauHinhBanDo.png")


    def admin_10_6_7_check(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_6_7)
        except:
            admin_10_6.admin_10_6_7(self, "", "", "")

        logging.info("-------------------------")
        logging.info("BÁO CÁO - 10.6 Cấu hình hệ thống - 10.6.7 Cấu hình bản đồ")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            flied1 = var_stx.driver.find_element(By.XPATH, var_stx.table_1_1).text
            flied2 = var_stx.driver.find_element(By.XPATH, var_stx.table_1_2).text
            flied3 = var_stx.driver.find_element(By.XPATH, var_stx.table_1_3).text
            flied4 = var_stx.driver.find_element(By.XPATH, var_stx.table_1_4).text
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "STT: {}\nTên cấu hình: {}\nGiá trị: {}\nGhi chú: {}"
                                       .format(flied1, flied2, flied3, flied4))
            if (flied1 and flied2 and flied3 != None):
                logging.info("True")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_stx.driver.save_screenshot(var_stx.imagepath + code + "_CauHinhBanDo_CheckHienThi.png")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_CauHinhBanDo_CheckHienThi.png")
        except:
            logging.info("False")
            var_stx.driver.save_screenshot(var_stx.imagepath + code + "_CauHinhBanDo_CheckHienThi.png")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_CauHinhBanDo_CheckHienThi.png")




    def admin_10_6_8(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6).click()
            time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6_8).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.6 Cấu hình hệ thống - 10.6.8 Cấu hình rời lốt",
                                                  var_stx.title_page1, "10.6.8 Cấu hình rời lốt", "_CauHinhRoiLot.png")

        try:
            var_stx.driver.implicitly_wait(2)
            eror = var_stx.driver.find_element(By.XPATH, var_stx.not_role).text
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, eror)
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
        except:
            pass




    def admin_10_6_9(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6).click()
            time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6_9).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.6 Cấu hình hệ thống - 10.6.9 Kích hoạt dịch vụ",
                                                  var_stx.title_page1, "10.6.9 Kích hoạt dịch vụ", "_KichHoatDichVu.png")


    def admin_10_6_9_check(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_6_9)
        except:
            admin_10_6.admin_10_6_9(self, "", "", "")

        logging.info("-------------------------")
        logging.info("BÁO CÁO - 10.6 Cấu hình hệ thống - 10.6.9 Kích hoạt dịch vụ")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            flied1 = var_stx.driver.find_element(By.XPATH, var_stx.vn_pay).text
            flied2 = var_stx.driver.find_element(By.XPATH, var_stx.be).text
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "{}\n{}"
                                       .format(flied1, flied2))
            if (flied1 and flied2 != None):
                logging.info("True")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_stx.driver.save_screenshot(var_stx.imagepath + code + "_KichHoatDichVu_CheckHienThi.png")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_KichHoatDichVu_CheckHienThi.png")
        except:
            logging.info("False")
            var_stx.driver.save_screenshot(var_stx.imagepath + code + "_KichHoatDichVu_CheckHienThi.png")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_KichHoatDichVu_CheckHienThi.png")




    def admin_10_6_10(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6).click()
            time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6_10).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.6 Cấu hình hệ thống - 10.6.10 Cấu hình hạng thẻ",
                                                  var_stx.title_page1, "10.6.10 Cấu hình hạng thẻ", "_CauHinhHangThe.png")

    def admin_10_6_10_check(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_6_10)
        except:
            admin_10_6.admin_10_6_10(self, "", "", "")

        logging.info("-------------------------")
        logging.info("BÁO CÁO - 10.6 Cấu hình hệ thống - 10.6.10 Cấu hình hạng thẻ")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            flied1 = var_stx.driver.find_element(By.XPATH, var_stx.list_data2_1).text
            flied2 = var_stx.driver.find_element(By.XPATH, var_stx.list_data2_2).text
            flied3 = var_stx.driver.find_element(By.XPATH, var_stx.list_data2_3).text
            flied4 = var_stx.driver.find_element(By.XPATH, var_stx.list_data2_4).text
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "STT: {}\nLoại thẻ: {}\nMàu thẻ: {}\nGhi chú: {}"
                                       .format(flied1, flied2, flied3, flied4))
            if (flied1 and flied2 and flied3 != None):
                logging.info("True")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_stx.driver.save_screenshot(var_stx.imagepath + code + "_CauHinhHangThe_CheckHienThi.png")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_CauHinhHangThe_CheckHienThi.png")
        except:
            logging.info("False")
            var_stx.driver.save_screenshot(var_stx.imagepath + code + "_CauHinhHangThe_CheckHienThi.png")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_CauHinhHangThe_CheckHienThi.png")




    def admin_10_6_11(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6).click()
            time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.admin_10_6_11).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.6 Cấu hình hệ thống - 10.6.11 Kích hoạt dịch vụ",
                                                  var_stx.title_page1, "10.6.11 Kích hoạt dịch vụ", "_KichHoatDichVu.png")


    def admin_10_6_11_check(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_6_11)
        except:
            admin_10_6.admin_10_6_11(self, "", "", "")

        logging.info("-------------------------")
        logging.info("BÁO CÁO - 10.6 Cấu hình hệ thống - 10.6.11 Kích hoạt dịch vụ")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            flied1 = var_stx.driver.find_element(By.XPATH, var_stx.zalo).text
            flied2 = var_stx.driver.find_element(By.XPATH, var_stx.vnpt).text
            flied3 = var_stx.driver.find_element(By.XPATH, var_stx.vmg).text
            flied4 = var_stx.driver.find_element(By.XPATH, var_stx.brand).text
            flied5 = var_stx.driver.find_element(By.XPATH, var_stx.vn_taxi).text
            flied6 = var_stx.driver.find_element(By.XPATH, var_stx.gsm).text
            flied7 = var_stx.driver.find_element(By.XPATH, var_stx.be1).text
            flied8 = var_stx.driver.find_element(By.XPATH, var_stx.vn_pay1).text
            flied9 = var_stx.driver.find_element(By.XPATH, var_stx.momo).text
            flied10 = var_stx.driver.find_element(By.XPATH, var_stx.mb).text
            flied11 = var_stx.driver.find_element(By.XPATH, var_stx.mifi).text
            flied12 = var_stx.driver.find_element(By.XPATH, var_stx._3a).text

            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}"
                                       .format(flied1, flied2, flied3, flied4, flied5, flied6, flied7, flied8, flied9, flied10, flied11, flied12))
            if (flied1 and flied2 and flied3 and flied4 and flied5 and flied6 and flied7 and flied8 and flied9 and flied10 and flied11 and flied12 != None):
                logging.info("True")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_stx.driver.save_screenshot(var_stx.imagepath + code + "_KichHoatDichVu_CheckHienThi.png")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_KichHoatDichVu_CheckHienThi.png")
        except:
            logging.info("False")
            var_stx.driver.save_screenshot(var_stx.imagepath + code + "_KichHoatDichVu_CheckHienThi.png")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_KichHoatDichVu_CheckHienThi.png")




class admin_10_7:


    def admin_10_7_1(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_7).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_7).click()
            time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.admin_10_7_1).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.7 Quản trị lái xe - 10.7.1 Quản trị thông báo lái xe",
                                                  var_stx.title_page1, "10.7.1 Quản trị thông báo lái xe", "_QuanTriThongBaoLaiXe.png")


    def admin_10_7_1_x(self):
        var_stx.driver.implicitly_wait(0.2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.title).clear()
            time.sleep(0.2)
            var_stx.driver.find_element(By.XPATH, var_stx.title).clear()
            time.sleep(0.2)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.DriverIdSearch1).click()
            time.sleep(0.2)
            var_stx.driver.find_element(By.XPATH, var_stx.DriverIdSearch1).click()
            time.sleep(0.2)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.ArticleType1).click()
            time.sleep(0.2)
            var_stx.driver.find_element(By.XPATH, var_stx.ArticleType1).click()
            time.sleep(0.2)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.PeriodId1).click()
            time.sleep(0.2)
            var_stx.driver.find_element(By.XPATH, var_stx.PeriodId1).click()
            time.sleep(0.2)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.SendArticleTypeSearch1).click()
            time.sleep(0.2)
            var_stx.driver.find_element(By.XPATH, var_stx.SendArticleTypeSearch1).click()
            time.sleep(0.2)
        except:
            pass


    def admin_10_7_1_search(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_7_1)
        except:
            admin_10_7.admin_10_7_1(self, "", "", "")

        admin_10_7.admin_10_7_1_x(self)
        data = var_stx.driver.find_element(By.XPATH, var_stx.list_data3_2).text
        var_stx.driver.find_element(By.XPATH, var_stx.title).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3.5)
        module_other_stx.write_result_text_try_if(code, eventname, result,"BÁO CÁO - 10.7 Quản trị lái xe - 10.7.1 Quản trị thông báo lái xe",
                                                  var_stx.list_data2_2, data, "_QuanTriThongBaoLaiXe_TieuDe.png")


    def admin_10_7_1_combobox_select(self, code, eventname, result, path_combobox_icon, path_combobox, path_check, desire, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_7_1)
        except:
            admin_10_7.admin_10_7_1(self, "", "", "")

        admin_10_7.admin_10_7_1_x(self)
        try:
            var_stx.driver.implicitly_wait(1)
            var_stx.driver.find_element(By.XPATH, path_combobox_icon).click()
            time.sleep(1.5)
        except:
            pass
        var_stx.driver.find_element(By.XPATH, path_combobox).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(8)
        var_stx.driver.find_element(By.XPATH, var_stx.list_data2_2_a).click()
        time.sleep(2)
        wait = WebDriverWait(var_stx.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.title1)))
        time.sleep(1)
        module_other_stx.write_result_text_try_if(code, eventname, result,"BÁO CÁO - 10.7 Quản trị lái xe - 10.7.1 Quản trị thông báo lái xe",
                                                  path_check, desire, name_image)

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.back).click()
            time.sleep(6)
        except:
            pass


    def admin_10_7_1_combobox(self, code, eventname, result, path_combobox, path_check, desire, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_7_1)
        except:
            admin_10_7.admin_10_7_1(self, "", "", "")

        admin_10_7.admin_10_7_1_x(self)
        var_stx.driver.find_element(By.XPATH, path_combobox).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(8)
        wait = WebDriverWait(var_stx.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, path_check)))
        time.sleep(0.5)
        module_other_stx.write_result_text_try_if(code, eventname, result,"BÁO CÁO - 10.7 Quản trị lái xe - 10.7.1 Quản trị thông báo lái xe",
                                                  path_check, desire, name_image)


    def admin_10_7_1_combobox1(self, code, eventname, result, path_combobox, desire, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_7_1)
        except:
            admin_10_7.admin_10_7_1(self, "", "", "")

        admin_10_7.admin_10_7_1_x(self)
        var_stx.driver.find_element(By.XPATH, path_combobox).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(8)
        var_stx.driver.find_element(By.XPATH, var_stx.list_data2_2_a).click()
        time.sleep(4)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.ddlSendArticleType).click()
            time.sleep(1.5)

            var_stx.driver.implicitly_wait(0.05)
            n = 0
            while (n < 10):
                n += 1
                n = str(n)
                path_data = "//*[@id='ddlSendArticleType']/option[" + n + "]"
                print(n)
                try:
                    name_select = var_stx.driver.find_element(By.XPATH, path_data).get_attribute("selected")
                    name_text = var_stx.driver.find_element(By.XPATH, path_data).text
                    print("selected: {}".format(name_select))
                    print("name: {}".format(name_text))
                    if name_select == "true":
                        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.7 Quản trị lái xe - 10.7.1 Quản trị thông báo lái xe",
                                                                  path_data, desire, name_image)
                        break
                except:
                    pass
                n = int(n)
        except:
            module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.7 Quản trị lái xe - 10.7.1 Quản trị thông báo lái xe",
                                                      var_stx.flow_liscense, desire, name_image)

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.update_nitification)
            var_stx.driver.find_element(By.XPATH, var_stx.back).click()
            time.sleep(5)
        except:
            pass


    def admin_10_7_1_excel_download(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_7_1)
        except:
            admin_10_7.admin_10_7_1(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.import_from_excel).click()
        time.sleep(3)

        var_stx.driver.find_element(By.XPATH, var_stx.dowload_simple_file).click()
        time.sleep(4)
        module_other_stx.write_result_dowload_file(code, eventname, result, "BÁO CÁO - 10.7 Quản trị lái xe - 10.7.1 Quản trị thông báo lái xe",
                                                   "nhap_danh_danh_thong_bao.xlsx", "_QuanTriThongBaoLaiXe_TaiFileMau.png")


    def admin_10_7_1_excel_upload(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.import_list_noti)
        except:
            admin_10_7.admin_10_7_1_excel_download(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.upload2).click()
        time.sleep(1.5)
        subprocess.Popen(var_stx.uploadpath+"template_vehicle_article.exe")
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.upload1).click()
        time.sleep(2.5)
        module_other_stx.write_result_text_try_if_other(code, eventname, result, "BÁO CÁO - 10.7 Quản trị lái xe - 10.7.1 Quản trị thông báo lái xe",
                                                   var_stx.not_role, "Bạn không thể thực hiện chức năng này. Hãy liên lạc bộ phận CSKH - Hotline(1900 6415) để biết thêm thông tin.",
                                                        "_QuanTriThongBaoLaiXe_UploadFile.png")


        try:
            var_stx.driver.find_element(By.XPATH, var_stx.not_role)
            var_stx.driver.back()
            time.sleep(3)
            var_stx.driver.back()
            time.sleep(4)
        except:
            pass


    def admin_10_7_1_add_new(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_7_1)
        except:
            admin_10_7.admin_10_7_1(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.add_new1).click()
        time.sleep(3)
        vehicle_driver_stx.increase()
        number = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 7, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.title).send_keys("Auto_ThongBao_"+number)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.create_noti_type).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.create_noti_flow).click()
        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.create_noti_name_driver).click()
        time.sleep(1)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.create_noti_name_driver1).click()
            time.sleep(1)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.create_noti_name_driver2).click()
            time.sleep(1)

        # Đường dẫn tệp tuyệt đối
        file_input = var_stx.driver.find_element(By.XPATH, var_stx.chose_file2)
        # file_path = os.path.abspath(var_stx.uploadpath + "template_vehicle_article.xlsx")
        # file_input.send_keys(file_path)

        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.create_noti_repeat).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.create_noti_time).send_keys(var_stx.data['admin']['create_noti_time'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.title).click()
        time.sleep(1)

        iframe = var_stx.driver.find_element(By.XPATH, var_stx.promotion_add_new_conten)
        var_stx.driver.switch_to.frame(iframe)
        content_area = var_stx.driver.find_element(By.XPATH, var_stx.promotion_add_new_conten_body)
        content_area.send_keys(var_stx.data['admin']['create_noti_conten'])
        var_stx.driver.switch_to.default_content()

        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.create_noti_phone).send_keys(var_stx.data['admin']['create_noti_phone'])
        time.sleep(1)

        var_stx.driver.find_element(By.XPATH, var_stx.save).click()
        time.sleep(3)
        var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 33, 2, "Auto_ThongBao_"+number)
        module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 14, "Auto_ThongBao_"+number)

        module_other_stx.write_result_text_try_if(code, eventname, result,"BÁO CÁO - 10.7 Quản trị lái xe - 10.7.1 Quản trị thông báo lái xe",
                                                  var_stx.text_success, "Thông báo đã tạo thành công.", "_QuanTriThongBaoLaiXe_ThemMoi.png")


        try:
            var_stx.driver.find_element(By.XPATH, var_stx.back).click()
            time.sleep(5)
        except:
            pass


    def admin_10_7_1_update(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_7_1)
        except:
            admin_10_7.admin_10_7_1(self, "", "", "")

        admin_10_7.admin_10_7_1_x(self)
        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 33, 2))


        var_stx.driver.find_element(By.XPATH, var_stx.title).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        name = var_stx.driver.find_element(By.XPATH, var_stx.list_data2_2_a).text
        if name == data:
            var_stx.driver.find_element(By.XPATH, var_stx.list_data2_2_a).click()
            time.sleep(3.5)

            wait = WebDriverWait(var_stx.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.create_noti_phone)))
            var_stx.driver.find_element(By.XPATH, var_stx.create_noti_phone).clear()
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.create_noti_phone).send_keys(var_stx.data['admin']['create_noti_phone_edit'])
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.save).click()
            time.sleep(2.5)
            module_other_stx.write_result_text_try_if(code, eventname, result,"BÁO CÁO - 10.7 Quản trị lái xe - 10.7.1 Quản trị thông báo lái xe",
                                                      var_stx.text_success, "Thông báo đã được cập nhật thành công.", "_QuanTriThongBaoLaiXe_CapNhat.png")

            try:
                var_stx.driver.find_element(By.XPATH, var_stx.back).click()
                time.sleep(5)
            except:
                pass


    def admin_10_7_1_see(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_7_1)
        except:
            admin_10_7.admin_10_7_1(self, "", "", "")

        admin_10_7.admin_10_7_1_x(self)
        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 33, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.title).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        name = var_stx.driver.find_element(By.XPATH, var_stx.list_data2_2_a).text
        if name == data:
            var_stx.driver.find_element(By.XPATH, var_stx.list_data2_7_a).click()
            time.sleep(3)
            var_stx.driver.switch_to.window(var_stx.driver.window_handles[1])
            time.sleep(2)
            module_other_stx.write_result_text_try_if(code, eventname, result,"BÁO CÁO - 10.7 Quản trị lái xe - 10.7.1 Quản trị thông báo lái xe",
                                                      var_stx.check_admin_10_7_1_see, var_stx.data['admin']['create_noti_conten'],
                                                      "_QuanTriThongBaoLaiXe_Xem.png")
            module_other_stx.close_tab()
            var_stx.driver.switch_to.window(var_stx.driver.window_handles[0])
            time.sleep(1)


    def admin_10_7_1_detail(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_7_1)
        except:
            admin_10_7.admin_10_7_1(self, "", "", "")

        admin_10_7.admin_10_7_1_x(self)
        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 33, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.title).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        name = var_stx.driver.find_element(By.XPATH, var_stx.list_data2_2_a).text
        if name == data:
            var_stx.driver.find_element(By.XPATH, var_stx.list_data2_8_i).click()
            time.sleep(3)
            wait = WebDriverWait(var_stx.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.list_driver_readed)))
            time.sleep(1)
            module_other_stx.write_result_text_try_if(code, eventname, result,"BÁO CÁO - 10.7 Quản trị lái xe - 10.7.1 Quản trị thông báo lái xe",
                                                      var_stx.list_driver_readed, "DANH SÁCH LÁI XE ĐÃ ĐỌC THÔNG BÁO", "_QuanTriThongBaoLaiXe_ChiTiet.png")
            var_stx.driver.back()
            time.sleep(3)


    def admin_10_7_1_delete(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_7_1)
        except:
            admin_10_7.admin_10_7_1(self, "", "", "")

        admin_10_7.admin_10_7_1_x(self)
        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 33, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.title).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        name = var_stx.driver.find_element(By.XPATH, var_stx.list_data2_2_a).text
        if name == data:
            var_stx.driver.find_element(By.XPATH, var_stx.list_data2_9_i).click()
            time.sleep(10)
            var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
            time.sleep(2)
            module_other_stx.write_result_text_try_if(code, eventname, result,"BÁO CÁO - 10.7 Quản trị lái xe - 10.7.1 Quản trị thông báo lái xe",
                                                      var_stx.message, "Xóa thông báo thành công.", "_QuanTriThongBaoLaiXe_Xoa.png")
            try:
                var_stx.driver.find_element(By.XPATH, var_stx.close).click()
                time.sleep(4)
            except:
                pass










    def admin_10_7_4(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_7).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_7).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.admin_10_7_4).click()
        time.sleep(2)
        wait = WebDriverWait(var_stx.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.title_page1)))
        time.sleep(1.5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.7 Quản trị lái xe - 10.7.4 Quản trị thông báo lái xe v2",
                                                  var_stx.title_page1, "10.7.4 Quản trị thông báo lái xe v2", "_QuanTriThongBaoLaiXeV2.png")


    def admin_10_7_4_x(self):
        var_stx.driver.implicitly_wait(0.2)
        # try:
        #     var_stx.driver.find_element(By.XPATH, var_stx.reportrange).click()
        #     time.sleep(2)
        #     var_stx.driver.find_element(By.XPATH, var_stx.daterangepicker_start).send_keys("07/04/2025")
        #     time.sleep(0.5)
        #     var_stx.driver.find_element(By.XPATH, var_stx.apply).click()
        #     time.sleep(1.5)
        # except:
        #     pass
        #
        # try:
        #     var_stx.driver.find_element(By.XPATH, var_stx.from_day).clear()
        #     time.sleep(0.5)
        #     var_stx.driver.find_element(By.XPATH, var_stx.to_day).clear()
        #     time.sleep(0.5)
        # except:
        #     pass

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.title).clear()
            time.sleep(0.2)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.SendTypeSearch_1).click()
            time.sleep(0.2)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.Period_1).click()
            time.sleep(0.2)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.ParentArticleTypeSearch_1).click()
            time.sleep(0.2)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.title).click()
            time.sleep(0.2)
        except:
            pass


    def admin_10_7_4_from_to_day(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_7_4)
        except:
            admin_10_7.admin_10_7_4(self, "", "", "")

        admin_10_7.admin_10_7_4_x(self)


        from_day = var_stx.driver.find_element(By.XPATH, var_stx.ag2_9).text
        to_day = var_stx.driver.find_element(By.XPATH, var_stx.ag2_10).text

        var_stx.driver.find_element(By.XPATH, var_stx.reportrange).click()
        time.sleep(2.5)
        var_stx.driver.find_element(By.XPATH, var_stx.daterangepicker_start).send_keys(from_day)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.daterangepicker_end).send_keys(to_day)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.apply).click()
        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.7 Quản trị lái xe - 10.7.4 Quản trị thông báo lái xe v2",
                                                  var_stx.ag1_9, from_day, "_QuanTriThongBaoLaiXeV2_TuNgay.png")

        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.7 Quản trị lái xe - 10.7.4 Quản trị thông báo lái xe v2",
                                                  var_stx.ag1_10, to_day, "_QuanTriThongBaoLaiXeV2_DenNgay.png")
        var_stx.driver.refresh()
        time.sleep(5)
        wait = WebDriverWait(var_stx.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.search)))
        time.sleep(1.5)


    def admin_10_7_4_search(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_7_4)
        except:
            admin_10_7.admin_10_7_4(self, "", "", "")

        admin_10_7.admin_10_7_4_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3)
        data = var_stx.driver.find_element(By.XPATH, var_stx.ag2_2).text

        var_stx.driver.find_element(By.XPATH, var_stx.title).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.7 Quản trị lái xe - 10.7.4 Quản trị thông báo lái xe v2",
                                                  var_stx.ag1_2, data, "_QuanTriThongBaoLaiXeV2_TieuDe.png")


    def admin_10_7_4_combobox(self, code, eventname, result, path_combobox, path_check, desire, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_7_4)
        except:
            admin_10_7.admin_10_7_4(self, "", "", "")

        admin_10_7.admin_10_7_4_x(self)
        var_stx.driver.find_element(By.XPATH, path_combobox).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3.5)
        wait = WebDriverWait(var_stx.driver, 10)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, path_check)))
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(3.5)
        module_other_stx.write_result_text_try_if(code, eventname, result,"BÁO CÁO - 10.7 Quản trị lái xe - 10.7.4 Quản trị thông báo lái xe v2",
                                                  path_check, desire, name_image)


    def admin_10_7_4_excel_download(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_7_4)
        except:
            admin_10_7.admin_10_7_4(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.import_excel1).click()
        time.sleep(3)

        var_stx.driver.find_element(By.XPATH, var_stx.dowload_simple_file).click()
        time.sleep(4)
        module_other_stx.write_result_dowload_file(code, eventname, result, "BÁO CÁO - 10.7 Quản trị lái xe - 10.7.4 Quản trị thông báo lái xe v2",
                                                   "quan_tri_thong_bao_lai_xe_v2.xlsx", "_QuanTriThongBaoLaiXeV2_TaiFileMau.png")


    def admin_10_7_4_excel_upload(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_7_4)
        except:
            admin_10_7.admin_10_7_4(self, "", "", "")


        var_stx.driver.find_element(By.XPATH, var_stx.choose_file).click()
        time.sleep(1.5)
        subprocess.Popen(var_stx.uploadpath+"template_vehicle_article.exe")
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.upload1).click()
        time.sleep(2.5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.7 Quản trị lái xe - 10.7.4 Quản trị thông báo lái xe v2",
                                                   var_stx.not_found_driver, "Không tìm thấy tài xế được gán xe này", "_QuanTriThongBaoLaiXeV2_UploadFile.png")

        try:
            button = var_stx.driver.find_element(By.XPATH, var_stx.exit1)
            var_stx.driver.execute_script("arguments[0].click();", button)
            time.sleep(3)
        except:
            pass


    def admin_10_7_4_add_new(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_7_4)
        except:
            admin_10_7.admin_10_7_4(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.add_new1).click()
        time.sleep(3)
        vehicle_driver_stx.increase()
        number = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 7, 2))

        wait = WebDriverWait(var_stx.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.title)))
        element.send_keys("Auto_ThongBaoV2_"+number)
        # var_stx.driver.find_element(By.XPATH, var_stx.title).send_keys("Auto_ThongBaoV2_"+number)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.create_notiv2_type1).click()  #Kiểu thông báo
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.create_notiv2_group).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.create_notiv2_type2).click()  #Loại thông báo
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.create_notiv2_send_flow).click()
        time.sleep(1.5)

        # var_stx.driver.find_element(By.XPATH, var_stx.dowload_simple_file1).click()
        # time.sleep(3)
        # var_stx.driver.find_element(By.XPATH, var_stx.upload_file)
        # time.sleep(1)
        # subprocess.Popen(var_stx.uploadpath+"template_vehicle.exe")
        # time.sleep(1)

        var_stx.driver.find_element(By.XPATH, var_stx.create_notiv2_send_flow_input).send_keys("auto")
        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.create_notiv2_send_flow_li1).click()
        time.sleep(1.5)
        # var_stx.driver.find_element(By.XPATH, var_stx.create_notiv2_send_flow_truongvc).click()
        # time.sleep(1.5)

        var_stx.driver.find_element(By.XPATH, var_stx.create_notiv2_repeat).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.create_notiv2_time)
        time.sleep(0.5)

        iframe = var_stx.driver.find_element(By.XPATH, var_stx.promotion_add_new_conten)
        var_stx.driver.switch_to.frame(iframe)
        content_area = var_stx.driver.find_element(By.XPATH, var_stx.promotion_add_new_conten_body)
        content_area.send_keys(var_stx.data['admin']['create_noti_conten_v2'])
        var_stx.driver.switch_to.default_content()

        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.create_notiv2_phone).send_keys(var_stx.data['admin']['create_noti_phone'])
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.save).click()

        var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 34, 2, "Auto_ThongBaoV2_"+number)
        module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 14, "Auto_ThongBaoV2_"+number)

        wait = WebDriverWait(var_stx.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.add_new_succes1)))
        module_other_stx.write_result_text_try_if(code, eventname, result,"BÁO CÁO - 10.7 Quản trị lái xe - BÁO CÁO - 10.7 Quản trị lái xe - 10.7.4 Quản trị thông báo lái xe v2",
                                                  var_stx.add_new_succes1, "Thêm mới thành công!", "_QuanTriThongBaoLaiXeV2_ThemMoi.png")
        time.sleep(3)


    def admin_10_7_4_detail1(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_7_4)
        except:
            admin_10_7.admin_10_7_4(self, "", "", "")

        admin_10_7.admin_10_7_4_x(self)
        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 34, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.title).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3.5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.ag1_2)
        except:
            var_stx.driver.refresh()
            time.sleep(5)
            var_stx.driver.find_element(By.XPATH, var_stx.title).send_keys(data)
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(3.5)


        name = var_stx.driver.find_element(By.XPATH, var_stx.ag1_2).text
        if name == data:
            var_stx.driver.find_element(By.XPATH, var_stx.ag1_2_a).click()
            time.sleep(3.5)
            module_other_stx.write_result_text_try_if(code, eventname, result,"BÁO CÁO - 10.7 Quản trị lái xe - 10.7.4 Quản trị thông báo lái xe v2",
                                                      var_stx.detail_notification, "Chi tiết thông báo", "_QuanTriThongBaoLaiXe_XemChiTiet.png")
            try:
                var_stx.driver.find_element(By.XPATH, var_stx.back).click()
                time.sleep(3.5)
            except:
                pass


    def admin_10_7_4_detail2(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_7_4)
        except:
            admin_10_7.admin_10_7_4(self, "", "", "")

        admin_10_7.admin_10_7_4_x(self)
        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 34, 2))


        var_stx.driver.find_element(By.XPATH, var_stx.title).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3.5)
        name = var_stx.driver.find_element(By.XPATH, var_stx.ag1_2).text
        if name == data:
            var_stx.driver.find_element(By.XPATH, var_stx.icon_detail1).click()
            time.sleep(3.5)
            module_other_stx.write_result_text_try_if(code, eventname, result,"BÁO CÁO - 10.7 Quản trị lái xe - 10.7.4 Quản trị thông báo lái xe v2",
                                                      var_stx.detail_notification_title, data, "_QuanTriThongBaoLaiXe_XemChiTiet.png")

            try:
                name = var_stx.driver.find_element(By.XPATH, var_stx.not_role1).text
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, name)
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                var_stx.driver.back()
                time.sleep(3)
            except:
                pass

            try:
                var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_7_4)
            except:
                var_stx.driver.back()
                time.sleep(3)


    def admin_10_7_4_coppy(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_7_4)
        except:
            admin_10_7.admin_10_7_4(self, "", "", "")

        admin_10_7.admin_10_7_4_x(self)
        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 34, 2))


        var_stx.driver.find_element(By.XPATH, var_stx.title).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3.5)
        name = var_stx.driver.find_element(By.XPATH, var_stx.ag1_2).text
        if name == data:
            var_stx.driver.find_element(By.XPATH, var_stx.icon_coppy1).click()
            time.sleep(3.5)
            module_other_stx.write_result_text_try_if(code, eventname, result,"BÁO CÁO - 10.7 Quản trị lái xe - 10.7.4 Quản trị thông báo lái xe v2",
                                                      var_stx.coppy_notification, "NHÂN BẢN THÔNG BÁO", "_QuanTriThongBaoLaiXe_NhanBanThongBao.png")

            try:
                var_stx.driver.find_element(By.XPATH, var_stx.back).click()
                time.sleep(3.5)
            except:
                pass


    def admin_10_7_4_pc(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_7_4)
        except:
            admin_10_7.admin_10_7_4(self, "", "", "")

        admin_10_7.admin_10_7_4_x(self)
        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 34, 2))


        var_stx.driver.find_element(By.XPATH, var_stx.title).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3.5)
        name = var_stx.driver.find_element(By.XPATH, var_stx.ag1_2).text
        if name == data:
            var_stx.driver.find_element(By.XPATH, var_stx.ag1_14_i_pc).click()
            time.sleep(3)
            var_stx.driver.switch_to.window(var_stx.driver.window_handles[1])
            time.sleep(1)
            module_other_stx.write_result_text_try_if(code, eventname, result,"BÁO CÁO - 10.7 Quản trị lái xe - 10.7.4 Quản trị thông báo lái xe v2",
                                                      var_stx.conten_notification, var_stx.data['admin']['create_noti_conten_v2'],
                                                      "_QuanTriThongBaoLaiXe_XemPc.png")
            module_other_stx.close_tab()
            var_stx.driver.switch_to.window(var_stx.driver.window_handles[0])
            time.sleep(1)


    def admin_10_7_4_phone(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_7_4)
        except:
            admin_10_7.admin_10_7_4(self, "", "", "")

        admin_10_7.admin_10_7_4_x(self)
        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 34, 2))


        var_stx.driver.find_element(By.XPATH, var_stx.title).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3.5)
        name = var_stx.driver.find_element(By.XPATH, var_stx.ag1_2).text
        if name == data:
            var_stx.driver.find_element(By.XPATH, var_stx.ag1_14_i_phone).click()
            time.sleep(3)
            module_other_stx.write_result_text_try_if(code, eventname, result,"BÁO CÁO - 10.7 Quản trị lái xe - 10.7.4 Quản trị thông báo lái xe v2",
                                                      "//*[text()='Test tạo thông báo theo lái xe v2']", var_stx.data['admin']['create_noti_conten_v2'],
                                                      "_QuanTriThongBaoLaiXe_XemPhone.png")
            var_stx.driver.refresh()
            time.sleep(5)


    def admin_10_7_4_delete(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_7_4)
        except:
            admin_10_7.admin_10_7_4(self, "", "", "")

        admin_10_7.admin_10_7_4_x(self)
        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 34, 2))


        var_stx.driver.find_element(By.XPATH, var_stx.title).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3.5)
        name = var_stx.driver.find_element(By.XPATH, var_stx.ag1_2).text
        if name == data:
            var_stx.driver.find_element(By.XPATH, var_stx.icon_delete1).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
            wait = WebDriverWait(var_stx.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.toast_message)))

            module_other_stx.write_result_text_try_if(code, eventname, result,"BÁO CÁO - 10.7 Quản trị lái xe - 10.7.4 Quản trị thông báo lái xe v2",
                                                      var_stx.toast_message, "Xóa thông báo thành công", "_QuanTriThongBaoLaiXe_Xoa.png")




class admin_10_10:


    def admin_10_10_2(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.admin_10_10).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.admin_10_10_2).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.10 Quản trị bảng giá - 10.10.2 Phụ phí loại hàng hóa",
                                                  var_stx.title_page1, "10.10.2 Phụ phí loại hàng hóa", "_PhuPhiLoaiHangHoa.png")


    def admin_10_10_2_search(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_10_2)
        except:
            admin_10_10.admin_10_10_2(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.type_of_goods).clear()
        data = var_stx.driver.find_element(By.XPATH, var_stx.table_table2_2).text
        var_stx.driver.find_element(By.XPATH, var_stx.type_of_goods).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3)

        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.10 Quản trị bảng giá - 10.10.2 Phụ phí loại hàng hóa",
                                                  var_stx.table_table1_2, data, "_PhuPhiLoaiHangHoa_TimKiem.png")

        var_stx.driver.find_element(By.XPATH, var_stx.type_of_goods).clear()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(2)


    def admin_10_10_2_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(2)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_10_2)
        except:
            admin_10_10.admin_10_10_2(self, "", "", "")


        var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        time.sleep(5)
        get_info_web1()
        minitor_stx.get_info_excel(5, "Sheet 1")
        minitor_stx.check_info_web_excel(code, eventname, result, "BÁO CÁO - 10.10 Quản trị bảng giá - 10.10.2 Phụ phí loại hàng hóa")


    def admin_10_10_2_add_new(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_10_2)
        except:
            admin_10_10.admin_10_10_2(self, "", "", "")


        try:
            admin_10_10.admin_10_10_2_delete(self, "", "", "")
        except:
            var_stx.driver.refresh()
            time.sleep(4)

        var_stx.driver.find_element(By.XPATH, var_stx.add_new1).click()
        time.sleep(3)

        var_stx.driver.find_element(By.XPATH, var_stx.add_new_goods).send_keys(var_stx.data['admin']['add_new_goods'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_surcharge).send_keys(var_stx.data['admin']['add_new_surcharge'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_describe).send_keys(var_stx.data['admin']['add_new_describe'])
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new2).click()
        time.sleep(2.5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.10 Quản trị bảng giá - 10.10.2 Phụ phí loại hàng hóa",
                                                  var_stx.message, "Lưu loại hàng hóa thành công", "_PhuPhiLoaiHangHoa_ThemMoi.png")

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.close).click()
            time.sleep(2)
        except:
            pass


    def admin_10_10_2_update(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_10_2)
        except:
            admin_10_10.admin_10_10_2(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.type_of_goods).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.type_of_goods).send_keys(var_stx.data['admin']['add_new_goods'])
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3.5)
        name = var_stx.driver.find_element(By.XPATH, var_stx.table_table1_2).text
        if name == var_stx.data['admin']['add_new_goods']:
            var_stx.driver.find_element(By.XPATH, var_stx.table_table1_2_a).click()
            time.sleep(2.5)
            var_stx.driver.find_element(By.XPATH, var_stx.add_new_surcharge).clear()
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.add_new_surcharge).send_keys("20")
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.update).click()
            time.sleep(2)
            module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.10 Quản trị bảng giá - 10.10.2 Phụ phí loại hàng hóa",
                                                      var_stx.message, "Lưu loại hàng hóa thành công", "_PhuPhiLoaiHangHoa_CapNhat.png")
            try:
                var_stx.driver.find_element(By.XPATH, var_stx.close).click()
                time.sleep(2.5)
            except:
                pass


    def admin_10_10_2_delete(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_10_2)
        except:
            admin_10_10.admin_10_10_2(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.type_of_goods).clear()
        var_stx.driver.find_element(By.XPATH, var_stx.type_of_goods).send_keys(var_stx.data['admin']['add_new_goods'])
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3.5)
        name = var_stx.driver.find_element(By.XPATH, var_stx.table_table1_2).text
        if name == var_stx.data['admin']['add_new_goods']:
            var_stx.driver.find_element(By.XPATH, var_stx.table_table1_5_i).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
            time.sleep(2)
            module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.10 Quản trị bảng giá - 10.10.2 Phụ phí loại hàng hóa",
                                                      var_stx.message, "Xóa loại hàng hóa thành công", "_PhuPhiLoaiHangHoa_Xóa.png")
            try:
                var_stx.driver.find_element(By.XPATH, var_stx.close).click()
                time.sleep(2.5)
            except:
                pass








    def admin_10_10_3(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_10).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_10).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.admin_10_10_3).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.10 Quản trị bảng giá - 10.10.3 Phụ phí theo thời gian",
                                                  var_stx.title_page1, "10.10.3 Phụ phí theo thời gian", "_PhuPhiTheoThoiGian.png")


    def admin_10_10_3_search(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_10_3)
        except:
            admin_10_10.admin_10_10_3(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.time).clear()
        data = var_stx.driver.find_element(By.XPATH, var_stx.table_table2_2).text
        var_stx.driver.find_element(By.XPATH, var_stx.time).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3)

        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.10 Quản trị bảng giá - 10.10.3 Phụ phí theo thời gian",
                                                  "//*[text()='  "+data+"']", data, "_PhuPhiTheoThoiGian_TimKiem.png")

        var_stx.driver.find_element(By.XPATH, var_stx.time).clear()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(2)


    def admin_10_10_3_add_new(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_10_3)
        except:
            admin_10_10.admin_10_10_3(self, "", "", "")


        # try:
        #     admin_10_10.admin_10_10_3_delete(self, "", "", "")
        # except:
        #     var_stx.driver.refresh()
        #     time.sleep(4)

        var_stx.driver.find_element(By.XPATH, var_stx.add_new1).click()
        time.sleep(3)

        var_stx.driver.find_element(By.XPATH, var_stx.add_new_time_from).send_keys(var_stx.data['admin']['add_new_time_from'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_time_to).send_keys(var_stx.data['admin']['add_new_time_to'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_time_type_surcharge).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_time_surcharge).send_keys(var_stx.data['admin']['add_new_time_surcharge'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_time_type_vehicle).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_time_describe).send_keys(var_stx.data['admin']['add_new_time_describe'])
        time.sleep(1)

        var_stx.driver.find_element(By.XPATH, var_stx.add_new2).click()
        time.sleep(2.5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.10 Quản trị bảng giá - 10.10.3 Phụ phí theo thời gian",
                                                  var_stx.message, "Lưu cấu hình thời gian thành công", "_PhuPhiTheoThoiGian_ThemMoi.png")

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.close).click()
            time.sleep(2)
        except:
            pass


    def admin_10_10_3_update(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_10_3)
        except:
            admin_10_10.admin_10_10_3(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.time).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.time).send_keys(var_stx.data['admin']['add_new_time_from'])
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3.5)
        name = var_stx.driver.find_element(By.XPATH, var_stx.table_table1_2).text
        if name == var_stx.data['admin']['add_new_time_from']:
            var_stx.driver.find_element(By.XPATH, var_stx.table_table1_2_a).click()
            time.sleep(2.5)

            var_stx.driver.find_element(By.XPATH, var_stx.add_new_time_describe).clear()
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.add_new_time_describe).send_keys(var_stx.data['admin']['add_new_time_describe_edit'])
            time.sleep(1)

            var_stx.driver.find_element(By.XPATH, var_stx.update).click()
            time.sleep(2)
            module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.10 Quản trị bảng giá - 10.10.3 Phụ phí theo thời gian",
                                                      var_stx.message, "Lưu cấu hình thời gian thành công", "_PhuPhiTheoThoiGian_CapNhat.png")

            try:
                var_stx.driver.find_element(By.XPATH, var_stx.close).click()
                time.sleep(2.5)
            except:
                pass


    def admin_10_10_3_delete(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_10_3)
        except:
            admin_10_10.admin_10_10_3(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.time).clear()
        var_stx.driver.find_element(By.XPATH, var_stx.time).send_keys(var_stx.data['admin']['add_new_time_from'])
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3.5)
        name = var_stx.driver.find_element(By.XPATH, var_stx.table_table1_2).text
        if name == var_stx.data['admin']['add_new_time_from']:
            var_stx.driver.find_element(By.XPATH, var_stx.table_table1_8_i).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
            time.sleep(2)
            module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.10 Quản trị bảng giá - 10.10.3 Phụ phí theo thời gian",
                                                      var_stx.message, "Xóa cấu hình thời gian thành công", "_PhuPhiTheoThoiGian_Xóa.png")
            try:
                var_stx.driver.find_element(By.XPATH, var_stx.close).click()
                time.sleep(2.5)
            except:
                pass







    def admin_10_10_4(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.admin_10_10).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.admin_10_10_4).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.10 Quản trị bảng giá - 10.10.4 Phụ phí thu hộ",
                                                  var_stx.title_page1, "10.10.4 Phụ phí thu hộ", "_PhuPhiTheoThuHo.png")


    def admin_10_10_4_x(self):
        var_stx.driver.implicitly_wait(0.2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.price).clear()
            time.sleep(0.3)
        except:
            pass

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.FeeType).click()
            time.sleep(0.3)
        except:
            pass


    def admin_10_10_4_search(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_10_4)
        except:
            admin_10_10.admin_10_10_4(self, "", "", "")


        admin_10_10.admin_10_10_4_x(self)
        data = var_stx.driver.find_element(By.XPATH, var_stx.table_table2_2).text
        data = ''.join(re.findall(r'\d+', data))


        var_stx.driver.find_element(By.XPATH, var_stx.price).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        var_stx.driver.implicitly_wait(1)
        logging.info("-------------------------")
        logging.info("BÁO CÁO - 10.10 Quản trị bảng giá - 10.10.4 Phụ phí thu hộ")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            check_text = var_stx.driver.find_element(By.XPATH, var_stx.table_table1_2).text
            check_text = ''.join(re.findall(r'\d+', check_text))
            logging.info(check_text)
            logging.info(data)
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, check_text)

            if check_text == data:
                logging.info("True")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_stx.driver.save_screenshot(var_stx.imagepath + code + "_PhuPhiTheoThuHo_TimKiem.png")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_PhuPhiTheoThuHo_TimKiem.png")
        except:
            logging.info("False")
            var_stx.driver.save_screenshot(var_stx.imagepath + code + "_PhuPhiTheoThuHo_TimKiem.png")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_PhuPhiTheoThuHo_TimKiem.png")



        var_stx.driver.find_element(By.XPATH, var_stx.price).clear()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(2)


    def admin_10_10_4_combobox(self, code, eventname, result, path_combobox, path_check, desire, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_10_4)
        except:
            admin_10_10.admin_10_10_4(self, "", "", "")


        admin_10_10.admin_10_10_4_x(self)
        var_stx.driver.find_element(By.XPATH, path_combobox).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        wait = WebDriverWait(var_stx.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, path_check)))
        time.sleep(0.5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.10 Quản trị bảng giá - 10.10.4 Phụ phí thu hộ",
                                                  path_check, desire, name_image)


    def admin_10_10_4_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(2)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_10_4)
        except:
            admin_10_10.admin_10_10_4(self, "", "", "")


        var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        time.sleep(5)
        get_info_web1()
        minitor_stx.get_info_excel(5, "Sheet 1")
        minitor_stx.check_info_web_excel(code, eventname, result, "BÁO CÁO - 10.10 Quản trị bảng giá - 10.10.4 Phụ phí thu hộ")


    def admin_10_10_4_add_new(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_10_4)
        except:
            admin_10_10.admin_10_10_4(self, "", "", "")


        try:
            admin_10_10.admin_10_10_4_delete(self, "", "", "")
        except:
            var_stx.driver.refresh()
            time.sleep(4)

        var_stx.driver.find_element(By.XPATH, var_stx.add_new1).click()
        time.sleep(3)

        var_stx.driver.find_element(By.XPATH, var_stx.add_surcharge_from).send_keys(var_stx.data['admin']['add_surcharge_from'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_surcharge_to).send_keys(var_stx.data['admin']['add_surcharge_to'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_surcharge_type1).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_surcharge_surcharge).send_keys(var_stx.data['admin']['add_surcharge_surcharge'])
        time.sleep(0.5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.add_surcharge_type2).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.add_surcharge_type2_1).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new2).click()
        time.sleep(2.5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.10 Quản trị bảng giá - 10.10.4 Phụ phí thu hộ",
                                                  var_stx.message, "Lưu phụ phí thành công", "_PhuPhiThuHo_ThemMoi.png")


        try:
            var_stx.driver.find_element(By.XPATH, var_stx.close).click()
            time.sleep(2)
        except:
            pass


    def admin_10_10_4_update(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_10_4)
        except:
            admin_10_10.admin_10_10_4(self, "", "", "")

        admin_10_10.admin_10_10_4_x(self)

        var_stx.driver.find_element(By.XPATH, var_stx.price).send_keys("30000")
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3.5)
        name = var_stx.driver.find_element(By.XPATH, var_stx.table_table1_6).text
        if name == "G7 Xe Avante" or name == "G7 Ecopark 7 chỗ (Ko dùng)":
            var_stx.driver.find_element(By.XPATH, var_stx.table_table1_2_a).click()
            time.sleep(2.5)
            var_stx.driver.find_element(By.XPATH, var_stx.add_surcharge_surcharge).clear()
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.add_surcharge_surcharge).send_keys("25")
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.update).click()
            time.sleep(2)
            module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.10 Quản trị bảng giá - 10.10.4 Phụ phí thu hộ",
                                                      var_stx.message, "Lưu phụ phí thành công", "_PhuPhiThuHo_CapNhat.png")
            try:
                var_stx.driver.find_element(By.XPATH, var_stx.close).click()
                time.sleep(2.5)
            except:
                pass


    def admin_10_10_4_delete(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_10_4)
        except:
            admin_10_10.admin_10_10_4(self, "", "", "")

        admin_10_10.admin_10_10_4_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.price).send_keys("30000")
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3.5)
        name = var_stx.driver.find_element(By.XPATH, var_stx.table_table1_6).text
        #"G7 Xe Avante" or name == "G7 Ecopark 7 chỗ (Ko dùng)":
        if name == "G7 Xe Avante" or name == "G7 Ecopark 7 chỗ (Ko dùng)":
            var_stx.driver.find_element(By.XPATH, var_stx.table_table1_7_i).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
            time.sleep(2)
            module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.10 Quản trị bảng giá - 10.10.4 Phụ phí thu hộ",
                                                      var_stx.message, "Xóa phụ phí thành công", "_PhuPhiThuHo_Xóa.png")
            try:
                var_stx.driver.find_element(By.XPATH, var_stx.close).click()
                time.sleep(2.5)
            except:
                pass








    def admin_10_10_5(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_10).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.admin).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.admin_10_10).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.admin_10_10_5).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.10 Quản trị bảng giá - 10.10.5 Phụ phí theo thời tiết",
                                                  var_stx.title_page1, "10.10.5 Phụ phí theo thời tiết", "_PhuPhiTheoThoiTiet.png")


    def admin_10_10_5_search(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_10_5)
        except:
            admin_10_10.admin_10_10_5(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.CarType).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        data = var_stx.driver.find_element(By.XPATH, var_stx.table_table2_2).text

        var_stx.driver.find_element(By.XPATH, "//*[@id='CarType']//*[text()='"+data+"']").click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.10 Quản trị bảng giá - 10.10.5 Phụ phí theo thời tiết",
                                                  var_stx.table_table1_2, data, "_PhuPhiTheoThoiTiet_TimKiem.png")


        var_stx.driver.find_element(By.XPATH, var_stx.CarType).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)


    def admin_10_10_5_add_new(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_10_5)
        except:
            admin_10_10.admin_10_10_5(self, "", "", "")


        try:
            admin_10_10.admin_10_10_5_delete(self, "", "", "")
        except:
            var_stx.driver.refresh()
            time.sleep(4)

        var_stx.driver.find_element(By.XPATH, var_stx.add_new1).click()
        time.sleep(3)

        var_stx.driver.find_element(By.XPATH, var_stx.add_wearther_type_vehicle).click()
        time.sleep(1.5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.add_wearther_type_vehicle1).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.add_wearther_type_vehicle1_1).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_wearther_type_surcharge).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_wearther_surcharge).send_keys(var_stx.data['admin']['add_wearther_surcharge'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_wearther_price_increase).click()
        time.sleep(1)

        var_stx.driver.find_element(By.XPATH, var_stx.add_new2).click()
        time.sleep(2.5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.10 Quản trị bảng giá - 10.10.5 Phụ phí theo thời tiết",
                                                  var_stx.message, "Lưu phụ phí theo thời tiết", "_PhuPhiTheoThoiTiet_ThemMoi.png")

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.close).click()
            time.sleep(2)
        except:
            pass


    def admin_10_10_5_update(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_10_5)
        except:
            admin_10_10.admin_10_10_5(self, "", "", "")


        var_stx.driver.find_element(By.XPATH, var_stx.CarType1).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(2.5)
        name = var_stx.driver.find_element(By.XPATH, var_stx.table_table1_2).text
        if name == "Eco 4 Chỗ Plus" or name == "G7 Vios":
            var_stx.driver.find_element(By.XPATH, var_stx.table_table1_2_a).click()
            time.sleep(2.5)
            var_stx.driver.find_element(By.XPATH, var_stx.add_surcharge_surcharge).clear()
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.add_surcharge_surcharge).send_keys("25")
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.update).click()
            time.sleep(2)
            module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.10 Quản trị bảng giá - 10.10.5 Phụ phí theo thời tiết",
                                                      var_stx.message, "Lưu phụ phí theo thời tiết", "_PhuPhiTheoThoiTiet_CapNhat.png")
            try:
                var_stx.driver.find_element(By.XPATH, var_stx.close).click()
                time.sleep(2.5)
            except:
                pass


    def admin_10_10_5_delete(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_admin_10_10_5)
        except:
            admin_10_10.admin_10_10_5(self, "", "", "")

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.weather_close3).click()
            time.sleep(2)
        except:
            pass


        try:
            var_stx.driver.find_element(By.XPATH, var_stx.CarType1).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.CarType2).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(2.5)
        # name = var_stx.driver.find_element(By.XPATH, var_stx.table_table1_2).text
        # if name == "G7 4 chỗ nhỏ khác":
        var_stx.driver.find_element(By.XPATH, var_stx.table_table1_6_i).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
        time.sleep(2)
        module_other_stx.write_result_text_try_if(code, eventname, result, "BÁO CÁO - 10.10 Quản trị bảng giá - 10.10.5 Phụ phí theo thời tiết",
                                                  var_stx.message, "Xóa phụ phí theo thời tiết thành công", "_PhuPhiTheoThoiTiet_Xóa.png")
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.close).click()
            time.sleep(2.5)
        except:
            pass









