import logging
import var_stx
import time
from selenium.webdriver.common.by import By
import module_other_stx
import login_stx
import minitor_stx
import subprocess
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import random


def check_account(name_check):
    var_stx.driver.implicitly_wait(1)
    name = var_stx.driver.find_element(By.XPATH, var_stx.check_account).text
    print("name1: " + name)
    if name == name_check:
        print("name2: " + name)
    else:
        var_stx.driver.find_element(By.XPATH, "")



def get_driver():
    var_stx.driver.implicitly_wait(0.05)
    try:
        var_stx.driver.find_element(By.XPATH, var_stx.State1).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(2.5)
    except:
        pass



    n = 0
    while (n < 20):
        n += 1
        n = str(n)
        print("n: " + n)
        path_driver = "//*[@class='ag-center-cols-container']/div[" + n + "]/div[6]"
        try:
            name_driver = var_stx.driver.find_element(By.XPATH, path_driver).text
            print("---------")
            print("driver: " + name_driver)
            var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 19, 2, name_driver)
            if name_driver != "-":
                break
        except:
            pass
        n = int(n)



def get_info_web():
    var_stx.driver.implicitly_wait(0.05)
    row = 119
    n = 0
    while (n < 50):
        n += 1
        n = str(n)
        row += 1
        path_column = "//*[@class='ag-header-viewport']/div/div/div[" + n + "]"
        path_data = "//*[@class='ag-center-cols-container']/div[1]/div[" + n + "]"
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








def increase():
    count = int(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 7, 2))
    print("Giá trị trước khi tăng:", count)
    count += 1
    var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 7, 2, count)
    count_after_write = int(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 7, 2))  # đọc lại để xác nhận
    print("Giá trị sau khi ghi:", count_after_write)

    time_string1 = time.strftime("_%d%m%Y_", time.localtime())
    print("Thời gian hiện tại:", time_string1)

    a = (f"{time_string1+str(count_after_write)}")
    var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 7, 3, a)
    print(a)

# increase()
# number = int(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 7, 3))







class vehicle:


    def vehicle(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        # login_stx.login.login_stx(self, var_stx.data['login']['tk_admin'], var_stx.data['login']['mk_admin'])
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.vehicle_driver).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.vehicle).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.vehicle_driver).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.vehicle).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.1 Xe",
                                                 var_stx.title_page, "2.1 Xe", "_XeLaiXe_Xe.png")


    def vehicle_company_7g_test(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx_g7test(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.vehicle_driver).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.vehicle).click()
        time.sleep(2.5)


    def vehicle_x(self):
        var_stx.driver.implicitly_wait(0.2)
        # try:
        #     var_stx.driver.find_element(By.XPATH, var_stx.vehicle_x1).clear()
        #     time.sleep(0.2)
        # except:
        #     pass
        # try:
        #     var_stx.driver.find_element(By.XPATH, var_stx.vehicle_x2).clear()
        #     time.sleep(0.2)
        # except:
        #     pass

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.vehicle_x3).clear()
            time.sleep(0.2)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.vehicle_x4).clear()
            time.sleep(0.2)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.vehicle_x5).clear()
            time.sleep(0.2)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.vehicle_x5).click()
        except:
            pass

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.vehicle_x6).click()
            time.sleep(0.2)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.vehicle_x7).click()
            time.sleep(0.2)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.vehicle_x8).click()
            time.sleep(0.2)
        except:
            pass



    def search_vehicle_from_to_day(self, code, eventname, result, path_check, desire, path_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver)
        except:
            vehicle.vehicle(self, "", "", "")

        var_stx.driver.refresh()
        time.sleep(5)

        var_stx.driver.find_element(By.XPATH, var_stx.reportrange).click()
        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.reportrange_30day).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(2.5)
        module_other_stx.write_result_text_try_if_other(code, eventname, result, "Xe & Lái xe - 2.1 Xe",
                                               path_check, desire, path_image)
        var_stx.driver.refresh()
        time.sleep(5)



    def search_vehicle(self, code, eventname, result, type_check, path_data, path_input, path_check, path_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver)
        except:
            vehicle.vehicle(self, "", "", "")

        vehicle.vehicle_x(self)
        try:
            var_stx.driver.implicitly_wait(1)
            var_stx.driver.find_element(By.XPATH, var_stx.vehicle_x3).send_keys("30E680")
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(10)
        except:
            pass


        try:
            var_stx.driver.implicitly_wait(0.3)
            var_stx.driver.find_element(By.XPATH, var_stx.listdata1_2)
        except:
            vehicle.vehicle_x(self)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(7)

        if type_check == "0":
            data = var_stx.driver.find_element(By.XPATH, path_data).text
            var_stx.driver.find_element(By.XPATH, path_input).clear()
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, path_input).send_keys(data)
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(10)
            module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.1 Xe",
                                                   path_check, data, path_image)


        if type_check == "1":
            # get_driver()
            # text = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 19, 2))
            vehicle.vehicle_x(self)
            var_stx.driver.find_element(By.XPATH, var_stx.DriverCodeId).send_keys("a")
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(10)
            text = var_stx.driver.find_element(By.XPATH, var_stx.listdata2_6).text
            data = text.split('-')[0]
            print(data)
            var_stx.driver.find_element(By.XPATH, path_input).clear()
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, path_input).send_keys(data)
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(10)
            logging.info("-------------------------")
            logging.info("Xe & Lái xe - 2.1 Xe")
            logging.info("Mã - " + code)
            logging.info("Tên sự kiện - " + eventname)
            logging.info("Kết quả - " + result)
            try:
                check_text = var_stx.driver.find_element(By.XPATH, path_check).text
                check_text = check_text.split('-')[0]
                logging.info(check_text)
                logging.info(data)
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, check_text)
                if check_text == data:
                    logging.info("True")
                    module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    logging.info("False")
                    var_stx.driver.save_screenshot(var_stx.imagepath + code + path_image)
                    module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                    module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + path_image)
            except:
                logging.info("False")
                var_stx.driver.save_screenshot(var_stx.imagepath + code + path_image)
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + path_image)

            #
            # module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.1 Xe",
            #                                        path_check, text, path_image)



    def search_vehicle_combobox(self, code, eventname, result, select_combobox, type_check, path_check, desire, path_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver)
            # var_stx.driver.find_element(By.XPATH, var_stx.g7_taxi_hn)
            # check_account("Autostaxi [209]")
        except:
            vehicle.vehicle(self, "", "", "")

        vehicle.vehicle_x(self)

        if path_image == "_Xe_BienSo.png" or path_image == "_Xe_SoHieu.png" or path_image == "_Xe_DangLai.png"\
                or path_image == "_Xe_TrangThai_KetNoiTot.png" or path_image == "_Xe_TrangThai_MatKetNoi.png" or path_image == "_Xe_TrangThai_KhongKetNoi.png":
            var_stx.driver.find_element(By.XPATH, var_stx.vehicle_x5).send_keys("a")
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(2.5)
            var_stx.driver.find_element(By.XPATH, var_stx.vehicle_x5).clear()
            try:
                var_stx.driver.find_element(By.XPATH, var_stx.listdata1_1)
            except:
                var_stx.driver.refresh()
                time.sleep(7)
                var_stx.driver.find_element(By.XPATH, var_stx.search).click()
                time.sleep(2)



        if path_image == "_Xe_Khoa.png" or path_image == "_Xe_Khoa_Khoa.png" or path_image == "_Xe_Khoa_MoKhoa.png" \
                or path_image == "_Xe_Khoa_LoaiXe.png" or path_image == "_Xe_Khoa_LoaiXe_Tatca.png" or path_image == "_Xe_Khoa_LoaiXe_Chon1.png":
            var_stx.driver.find_element(By.XPATH, var_stx.liscense_plate).send_keys("12")
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(2.5)
            try:
                var_stx.driver.find_element(By.XPATH, var_stx.listdata1_1)
                var_stx.driver.find_element(By.XPATH, var_stx.liscense_plate).clear()
            except:
                var_stx.driver.refresh()
                time.sleep(7)
                var_stx.driver.find_element(By.XPATH, var_stx.search).click()
                time.sleep(2)


        if path_image == "_Xe_TrangThai.png":
            try:
                var_stx.driver.implicitly_wait(1)
                var_stx.driver.find_element(By.XPATH, var_stx.state_0).click()
            except:
                var_stx.driver.find_element(By.XPATH, var_stx.search_advanced).click()
                time.sleep(1.5)
                var_stx.driver.find_element(By.XPATH, var_stx.enableCStatus).click()
                time.sleep(1.5)
                var_stx.driver.find_element(By.XPATH, var_stx.search).click()
                time.sleep(2)




        if path_image == "_Xe_Khoa_LoaiXe.png" or path_image == "_Xe_Khoa_LoaiXe_Tatca.png" or path_image == "_Xe_Khoa_LoaiXe_Chon1.png":
            try:
                var_stx.driver.implicitly_wait(1)
                var_stx.driver.find_element(By.XPATH, var_stx.FasttaxiVehicleTypeId1).click()
            except:
                var_stx.driver.find_element(By.XPATH, var_stx.search_advanced).click()
                time.sleep(1.5)
                var_stx.driver.find_element(By.XPATH, var_stx.enableVType).click()
                time.sleep(1.5)
                var_stx.driver.find_element(By.XPATH, var_stx.search).click()
                time.sleep(2)



        var_stx.driver.find_element(By.XPATH, select_combobox).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(2)
        if type_check == "0":
            logging.info("-------------------------")
            logging.info("Xe & Lái xe - 2.1 Xe")
            logging.info("Mã - " + code)
            logging.info("Tên sự kiện - " + eventname)
            logging.info("Kết quả - " + result)
            logging.info("True")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")

        if type_check == "1":
            module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.1 Xe",
                                                      path_check, desire, path_image)

        if type_check == "2":
            module_other_stx.write_result_text_try_if_other(code, eventname, result, "Xe & Lái xe - 2.1 Xe",
                                                      path_check, desire, path_image)

        if type_check == "3":
            var_stx.driver.find_element(By.XPATH, var_stx.vehicle_type).click()
            time.sleep(1)
            name_vehicle = var_stx.driver.find_element(By.XPATH, var_stx.vehicle_type_3).text
            module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.1 Xe",
                                                      path_check, name_vehicle, path_image)

        if type_check == "4":
            module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.1 Xe",
                                                      path_check, desire, path_image)

            try:
                var_stx.driver.find_element(By.XPATH, path_check)
            except:
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "Không có dữ liệu")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, "")





    def search_vehicle_type_vehicle(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver)
        except:
            vehicle.vehicle(self, "", "", "")

        vehicle.vehicle_x(self)

        var_stx.driver.find_element(By.XPATH, var_stx.liscense_plate).send_keys("12")
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(2.5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.listdata1_1)
            var_stx.driver.find_element(By.XPATH, var_stx.liscense_plate).clear()
        except:
            var_stx.driver.refresh()
            time.sleep(7)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(2)

        try:
            var_stx.driver.implicitly_wait(1)
            var_stx.driver.find_element(By.XPATH, var_stx.FasttaxiVehicleTypeId1).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.search_advanced).click()
            time.sleep(1.5)
            var_stx.driver.find_element(By.XPATH, var_stx.enableVType).click()
            time.sleep(1.5)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(2)

        type_vehicle = var_stx.driver.find_element(By.XPATH, var_stx.listdata2_4).text

        var_stx.driver.find_element(By.XPATH, "//*[@id='FasttaxiVehicleTypeId']//*[text()='"+type_vehicle+"']").click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(2)
        module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.1 Xe",
                                                        var_stx.listdata1_4, type_vehicle, "_Xe_Khoa_LoaiXe_Chon1.png")







    def search_vehicle_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")

        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver)
        except:
            vehicle.vehicle(self, "", "", "")

        vehicle.vehicle_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.vehicle_x5).send_keys("a")
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(10)

        var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        time.sleep(7)
        module_other_stx.write_result_dowload_file(code, eventname, result, "Xe & Lái xe - 2.1 Xe",
                                                        "xe_LaiXe.xls", "xe_LaiXe_XuatExcel.png")

        # get_info_web()
        #
        # try:
        #     minitor_stx.get_info_excel(5, "Sheet 1")
        # except:
        #     var_stx.driver.refresh()
        #     time.sleep(7)
        #     var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        #     time.sleep(7)
        #     get_info_web()
        #     minitor_stx.get_info_excel(5, "Sheet 1")
        # minitor_stx.check_info_web_excel(code, eventname, result, "Xe & Lái xe - 2.1 Xe")


    def vehicle_dowload_file(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        vehicle.vehicle(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.import_excel).click()
        time.sleep(2.5)
        var_stx.driver.find_element(By.XPATH, var_stx.dowload_simple_file).click()
        time.sleep(4)
        module_other_stx.write_result_dowload_file(code, eventname, result, "Xe & Lái xe - 2.1 Xe",
                                                   "_xe.xls", "_Xe_TaiFileMau.png")


    def vehicle_import_file(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.chose_file)
        except:
            vehicle.vehicle_dowload_file(self, "", "", "")

        button = var_stx.driver.find_element(By.XPATH, var_stx.chose_file)
        var_stx.driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        file_input = var_stx.driver.find_element(By.XPATH, var_stx.fileUpload)
        file_path = os.path.abspath(var_stx.uploadpath + "template_vehicle.xlsx")
        file_input.send_keys(file_path)
        time.sleep(4)
        # button = var_stx.driver.find_element(By.XPATH, var_stx.chose_file)
        # var_stx.driver.execute_script("arguments[0].click();", button)
        # time.sleep(1)
        # subprocess.Popen(var_stx.uploadpath+"template_vehicle.exe")
        # time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.upload1).click()
        time.sleep(2.5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.1 Xe",
                                                 var_stx.list_import_1_6, "Số hiệu đã tồn tại trong hệ thống với biển số 30E09187, Loại xe không tồn tại, Tên xe không tồn tại",
                                                  "_XeLaiXe_Xe_Upload2.png")

        try:
            var_stx.driver.implicitly_wait(1)
            var_stx.driver.find_element(By.XPATH, var_stx.exit).click()
            time.sleep(3)
        except:
            pass


    def vehicle_addnew(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver)
        except:
            vehicle.vehicle(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.add_new).click()
        time.sleep(2.5)
        increase()
        number = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 7, 2))
        var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 2, 2, "2024AUTO"+number)


        var_stx.driver.find_element(By.XPATH, var_stx.add_new_vehicle_liscense_plate).send_keys("2024AUTO"+number)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_vehicle_code).send_keys("2024"+number)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_vehicle_type).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_vehicle_name).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_vehicle_color).send_keys(var_stx.data['vehicle']['add_new_color'])
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_vehicle_image).send_keys(var_stx.data['vehicle']['add_new_image'])
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_vehicle_manager).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_vehicle_number1).send_keys(var_stx.data['vehicle']['add_new_number1'])
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_vehicle_number2).send_keys(var_stx.data['vehicle']['add_new_number2'])
        time.sleep(0.5)
        try:
            var_stx.driver.implicitly_wait(1)
            var_stx.driver.find_element(By.XPATH, var_stx.add_new_vehicle_company_manager).click()
            time.sleep(0.5)
        except:
            pass

        var_stx.driver.find_element(By.XPATH, var_stx.add_new_vehicle_black_box)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_vehicle_bluetooth).click()
        time.sleep(0.5)
        try:
            var_stx.driver.implicitly_wait(1)
            var_stx.driver.find_element(By.XPATH, var_stx.add_new_vehicle_asign_gsm)
            time.sleep(0.5)
        except:
            pass

        var_stx.driver.find_element(By.XPATH, var_stx.add_new_vehilce_add_new).click()
        time.sleep(2.5)
        print("2024AUTO"+number)
        module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 14, "2024AUTO"+number)

        module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.1 Xe",
                                                 var_stx.add_new_succes, "Thêm mới xe thành công.", "_XeLaiXe_Xe_ThemMoi.png")

        try:
            var_stx.driver.implicitly_wait(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.close).click()
            time.sleep(5)
        except:
            pass

        try:
            var_stx.driver.implicitly_wait(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.exit).click()
            time.sleep(5)
        except:
            pass


    def vehicle_checkbox(self, code, eventname, result, path_input, desire_checkbox, path_check, desire, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver)
        except:
            vehicle.vehicle(self, "", "", "")

        liscense_plate = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 2, 2))

        try:
            var_stx.driver.find_element(By.XPATH, "//*[@class='ag-center-cols-container']/div[1]//*[text()='"+liscense_plate+"']")
        except:
            vehicle.vehicle_x(self)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(3)
            var_stx.driver.find_element(By.XPATH, var_stx.vehicle_input1).send_keys(liscense_plate)
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(5)


        button = var_stx.driver.find_element(By.XPATH, path_input)
        var_stx.driver.execute_script("arguments[0].click();", button)

        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.confirm).click()
        # time.sleep(0.6)
        try:
            element = WebDriverWait(var_stx.driver, 10).until(EC.presence_of_element_located((By.XPATH, path_check)))
        except:
            pass
        #Kết nối hộp đen thành công
        module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.1 Xe",
                                                 path_check, desire, name_image)
        time.sleep(7)
        try:
            var_stx.driver.find_element(By.XPATH, path_check)
        except:
            var_stx.driver.refresh()
            time.sleep(5)




    def vehicle_clock(self, code, eventname, result, path_clock, type_clock, path_check, desire, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver)
        except:
            vehicle.vehicle(self, "", "", "")


        liscense_plate = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 2, 2))
        try:
            var_stx.driver.find_element(By.XPATH, "//*[@class='ag-center-cols-container']/div[1]//*[text()='"+liscense_plate+"']")
        except:
            vehicle.vehicle_x(self)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(3)
            var_stx.driver.find_element(By.XPATH, var_stx.vehicle_input1).send_keys(liscense_plate)
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(5)
        # var_stx.driver.find_element(By.XPATH, var_stx.listdata1_11).click()
        try:
            var_stx.driver.find_element(By.XPATH, path_clock).click()
        except:
            var_stx.driver.refresh()
            time.sleep(5)
            var_stx.driver.find_element(By.XPATH, path_clock).click()

        time.sleep(2)
        if type_clock == "0":
            var_stx.driver.find_element(By.XPATH, var_stx.confirm_lock_day_input).send_keys(var_stx.data['vehicle']['lock_day'])
            var_stx.driver.find_element(By.XPATH, var_stx.confirm_lock_reason_input).click()
            var_stx.driver.find_element(By.XPATH, var_stx.confirm_lock_reason_input).send_keys(var_stx.data['vehicle']['lock_reason'])
            time.sleep(1)

        if type_clock == "1":
            var_stx.driver.find_element(By.XPATH, var_stx.reason_clock1).click()
            time.sleep(1)

        var_stx.driver.find_element(By.XPATH, var_stx.confirm).click()
        time.sleep(5)
        wait = WebDriverWait(var_stx.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, path_check)))

        # element = WebDriverWait(var_stx.driver, 10).until(EC.presence_of_element_located((By.XPATH, path_check)))
        module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.1 Xe",
                                                  path_check, desire, name_image)

        time.sleep(3)
        try:
            var_stx.driver.implicitly_wait(1)
            var_stx.driver.find_element(By.XPATH, var_stx.close).click()
            time.sleep(4)
        except:
            pass


    def vehicle_update(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver)
        except:
            vehicle.vehicle(self, "", "", "")

        liscense_plate = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 2, 2))
        try:
            var_stx.driver.find_element(By.XPATH, "//*[@class='ag-center-cols-container']/div[1]//*[text()='"+liscense_plate+"']")
        except:
            vehicle.vehicle_x(self)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(3)
            var_stx.driver.find_element(By.XPATH, var_stx.vehicle_input1).send_keys(liscense_plate)
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(5)


        try:
            var_stx.driver.find_element(By.XPATH, var_stx.listdata1_2a).click()
        except:
            var_stx.driver.refresh()
            time.sleep(5)
            var_stx.driver.find_element(By.XPATH, var_stx.listdata1_2a).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_vehicle_color).clear()
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_vehicle_color).send_keys(var_stx.data['vehicle']['add_new_color_edit'])
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.update).click()
        element = WebDriverWait(var_stx.driver, 10).until(EC.presence_of_element_located((By.XPATH, var_stx.check_vehicle_update)))
        time.sleep(1)
        module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.1 Xe",
                                                  var_stx.check_vehicle_update, "Cập nhật xe thành công.", "_Xe_CapNhat.png")
        try:
            var_stx.driver.implicitly_wait(1)
            var_stx.driver.find_element(By.XPATH, var_stx.close).click()
            time.sleep(3)
        except:
            pass


    def vehicle_delete(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver)
            # var_stx.driver.find_element(By.XPATH, var_stx.STAXI)
        except:
            vehicle.vehicle(self, "", "", "")
            # vehicle.vehicle_company_7g_test(self, "", "", "")


        liscense_plate = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 2, 2))
        vehicle.vehicle_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.vehicle_input1).send_keys(liscense_plate)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        name_check = var_stx.driver.find_element(By.XPATH, var_stx.listdata1_2).text
        if name_check == liscense_plate:
            var_stx.driver.find_element(By.XPATH, var_stx.icon_delete).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.confirm).click()
            wait = WebDriverWait(var_stx.driver, 5)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.check_vehicle_delete)))
            module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.1 Xe",
                                                      var_stx.check_vehicle_delete, "Xóa xe thành công", "_Xe_XoaXe.png")
        time.sleep(5)


    def vehicle_hide_column(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver)
            # var_stx.driver.find_element(By.XPATH, var_stx.STAXI)
        except:
            # vehicle.vehicle_company_7g_test(self, "", "", "")
            vehicle.vehicle(self, "", "", "")

        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.hide_column).click()
        time.sleep(2)
        if var_stx.driver.find_element(By.XPATH, var_stx.hide_column1_input).is_selected() == True:
            var_stx.driver.find_element(By.XPATH, var_stx.hide_column1_input).click()
            time.sleep(1.5)
        module_other_stx.write_result_not_displayed_try(code, eventname, result, "Xe & Lái xe - 2.1 Xe",
                                                  var_stx.vehicle_hide_column_stt, "_Xe_AnHienCot.png")



        if var_stx.driver.find_element(By.XPATH, var_stx.hide_column1_input).is_selected() == False:
            var_stx.driver.find_element(By.XPATH, var_stx.hide_column1_input).click()
            time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.hide_column).click()
        time.sleep(3)




class driver:


    def driver(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        # login_stx.login.login_stx(self, var_stx.data['login']['tk_admin'], var_stx.data['login']['mk_admin'])
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.vehicle_driver).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.vehicle_driver).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.driver1).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.vehicle_driver).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.driver1).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.2 Lái xe",
                                                 var_stx.title_page, "2.2 Lái xe", "_XeLaiXe_LaiXe.png")


    def driver_company_7g_test(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx_g7test(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.vehicle_driver).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.driver1).click()
        time.sleep(2.5)


    def driver_x(self):
        var_stx.driver.implicitly_wait(0.2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.from_day).clear()
            time.sleep(0.2)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.to_day).clear()
            time.sleep(0.2)
        except:
            pass

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.search_driver_input).clear()
            time.sleep(0.2)
        except:
            pass

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.liscense_plate).clear()
            time.sleep(0.2)
        except:
            pass

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.vehicle_x4).clear()
            time.sleep(0.2)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.vehicle_assign).clear()
            time.sleep(0.2)
        except:
            pass

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.driver_liscense).clear()
            time.sleep(0.2)
        except:
            pass

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.vehicle_x4).click()
        except:
            pass

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.cccd).clear()
            time.sleep(0.2)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.sdt).clear()
            time.sleep(0.2)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.state_1).click()
            time.sleep(0.2)
        except:
            pass



    def search_driver_from_to_day(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver2_2)
            # var_stx.driver.find_element(By.XPATH, var_stx.g7_taxi_hn)
            # check_account("Autostaxi [209]")
        except:
            driver.driver(self, "", "", "")

        driver.driver_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3.5)
        date = var_stx.driver.find_element(By.XPATH, var_stx.listdata2_11).text
        date1 = date[0:10]
        date2 = date1 + " 00:00"
        date3 = date1 + " 23 :00"
        print(date)
        var_stx.driver.find_element(By.XPATH, var_stx.from_day).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(date2)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(date3)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.liscense_plate).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3.5)
        module_other_stx.write_result_text_try_if_cut2(code, eventname, result, "Xe & Lái xe - 2.2 Lái xe",
                                              var_stx.listdata1_11, date1, "_LaiXe_TuNgayDenNgay.png", 0, 10)


    def search_driver(self, code, eventname, result, path_data, path_input, path_check, path_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver2_2)
        except:
            driver.driver(self, "", "", "")

        driver.driver_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.liscense_plate).send_keys("2")
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(10)

        try:
            var_stx.driver.implicitly_wait(0.3)
            var_stx.driver.find_element(By.XPATH, var_stx.listdata1_2)
        except:
            driver.driver_x(self)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(7)

        driver.driver_x(self)
        data = var_stx.driver.find_element(By.XPATH, path_data).text
        var_stx.driver.find_element(By.XPATH, path_input).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(10)
        module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.2 Lái xe",
                                               path_check, data, path_image)


    def search_driver_assign(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver2_2)
            # var_stx.driver.find_element(By.XPATH, var_stx.g7_taxi_hn)
        except:
            driver.driver(self, "", "", "")

        driver.driver_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.liscense_plate).send_keys("2")
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(2)
        driver.driver_x(self)

        scroll_bar = var_stx.driver.find_element(By.XPATH, "//*[@class='ag-body-horizontal-scroll-viewport']")
        ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(800, 0).release().perform()
        time.sleep(5)
        data0 = var_stx.driver.find_element(By.XPATH, var_stx.listdata2_12).text
        print("data0:" + data0)
        data0 = data0.split(",")[0]

        data1 = var_stx.driver.find_element(By.XPATH, var_stx.listdata2_13).text
        print("data1:" + data1)
        data1 = data1.split(",")[0]

        data2 = var_stx.driver.find_element(By.XPATH, var_stx.listdata2_14).text
        print("data2:" + data2)
        data2 = data2.split(",")[0]

        data3 = var_stx.driver.find_element(By.XPATH, var_stx.listdata2_15).text
        print("data3:" + data3)
        data3 = data3.split(",")[0]

        data4= var_stx.driver.find_element(By.XPATH, var_stx.listdata1_15).text
        print("data4:" + data4)
        data4 = data4.split(",")[0]

        data5 = var_stx.driver.find_element(By.XPATH, var_stx.listdata2_16).text
        print("data5:" + data5)
        data5 = data5.split(",")[0]


        var_stx.driver.find_element(By.XPATH, var_stx.vehicle_assign).send_keys(data3)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3)
        logging.info("-------------------------")
        logging.info("Xe & Lái xe - 2.2 Lái xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            check_text = var_stx.driver.find_element(By.XPATH, var_stx.listdata1_15).text
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, check_text)

            check_text = check_text.split(",")[0]
            logging.info(check_text)
            logging.info(data3)
            if check_text == data3:
                logging.info("True")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_stx.driver.save_screenshot(var_stx.imagepath + code + "_XeLaiXe_TimKiem_XeDaGan.png")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_XeLaiXe_TimKiem_XeDaGan.png")
        except:
            logging.info("False")
            var_stx.driver.save_screenshot(var_stx.imagepath + code + "_XeLaiXe_TimKiem_XeDaGan.png")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_XeLaiXe_TimKiem_XeDaGan.png")


        # module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.2 Lái xe",
        #                                        var_stx.listdata1_14, data, "_XeLaiXe_TimKiem_XeDaGan.png")

        data = var_stx.driver.find_element(By.XPATH, var_stx.listdata1_12).text
        print("data1b:" + data)
        data1 = var_stx.driver.find_element(By.XPATH, var_stx.listdata1_13).text
        print("data2b:" + data1)
        data2 = var_stx.driver.find_element(By.XPATH, var_stx.listdata1_14).text
        print("data3b:" + data2)
        data3 = var_stx.driver.find_element(By.XPATH, var_stx.listdata1_15).text
        print("data4b:" + data3)


    def search_driver_combobox(self, code, eventname, result, path_combobox, type_check, path_check, desire, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver2_2)
            # var_stx.driver.find_element(By.XPATH, var_stx.g7_taxi_hn)
        except:
            driver.driver(self, "", "", "")

        driver.driver_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.cccd).send_keys("12")
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.listdata1_1)
        except:
            var_stx.driver.refresh()
            time.sleep(6)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(2.5)

        # try:
        #     var_stx.driver.find_element(By.XPATH, path_combobox).click()
        #     time.sleep(1)
        # except:
        #     var_stx.driver.find_element(By.XPATH, var_stx.search_advanced).click()
        #     time.sleep(1.5)
        #     if var_stx.driver.find_element(By.XPATH, var_stx.enableVType).is_selected() == False:
        #         var_stx.driver.find_element(By.XPATH, var_stx.enableVType).click()
        #         time.sleep(0.5)
        #
        #     if var_stx.driver.find_element(By.XPATH, var_stx.enableVName).is_selected() == False:
        #         var_stx.driver.find_element(By.XPATH, var_stx.enableVName).click()
        #         time.sleep(0.5)
        #
        #     if var_stx.driver.find_element(By.XPATH, var_stx.enableCStatus).is_selected() == False:
        #         var_stx.driver.find_element(By.XPATH, var_stx.enableCStatus).click()



        try:
            var_stx.driver.find_element(By.XPATH, var_stx.vehicle_assign1)
        except:
            scroll_bar = var_stx.driver.find_element(By.XPATH, "//*[@class='ag-body-horizontal-scroll-viewport']")
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(800, 0).release().perform()
            time.sleep(2)

        var_stx.driver.find_element(By.XPATH, path_combobox).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3)
        if type_check == "0":
            module_other_stx.write_result_text_try_if_other(code, eventname, result, "Xe & Lái xe - 2.2 Lái xe",
                                                      path_check, desire, name_image)
        if type_check == "1":
            module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.2 Lái xe",
                                                      path_check, desire, name_image)
        data = var_stx.driver.find_element(By.XPATH, var_stx.listdata1_9).text
        print("data1b:" + data)
        data1 = var_stx.driver.find_element(By.XPATH, var_stx.listdata1_10).text
        print("data2b:" + data1)
        data2 = var_stx.driver.find_element(By.XPATH, var_stx.listdata1_11).text
        print("data3b:" + data2)
        data3 = var_stx.driver.find_element(By.XPATH, var_stx.listdata1_12).text
        print("data4b:" + data3)





    def driver_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")

        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver2_2)
        except:
            driver.driver(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.liscense_plate).send_keys("2")
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(10)
        var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        time.sleep(7)
        module_other_stx.write_result_dowload_file(code, eventname, result, "Xe & Lái xe - 2.2 Lái xe",
                                                   "_laixe.xls", "_LaiXe_TaiExcel.png")


    def driver_dowload_file(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver2_2)
        except:
            driver.driver(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.liscense_plate).send_keys("2")
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(2.5)

        var_stx.driver.find_element(By.XPATH, var_stx.import_excel).click()
        time.sleep(2.5)
        var_stx.driver.find_element(By.XPATH, var_stx.dowload_simple_file).click()
        time.sleep(4)
        module_other_stx.write_result_dowload_file(code, eventname, result, "Xe & Lái xe - 2.2 Lái xe",
                                                   "_filemaulaixe.xls", "_LaiXe_TaiFileMau.png")


    def driver_import_file(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.chose_file)
        except:
            driver.driver_dowload_file(self, "", "", "")

        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.chose_file1).click()
        except:
            button = var_stx.driver.find_element(By.XPATH, var_stx.chose_file)
            var_stx.driver.execute_script("arguments[0].click();", button)

        time.sleep(1)
        subprocess.Popen(var_stx.uploadpath+"template_driver.exe")
        time.sleep(3)
        var_stx.driver.find_element(By.XPATH, var_stx.upload1).click()
        time.sleep(5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_import_1_6_no)
            module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.2 Lái xe",
                                                     var_stx.list_import_1_6, "Số điện thoại đã tồn tại trong hệ thống với tài khoản TRANQUANGTRUONG2",
                                                      "_LaiXe_Upload1.png")
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_import_1_6_ys)
            module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.2 Lái xe",
                                                     var_stx.list_import_1_6, "Bản ghi hợp lệ",
                                                      "_LaiXe_Upload1.png")

        try:
            var_stx.driver.implicitly_wait(1)
            var_stx.driver.find_element(By.XPATH, var_stx.exit).click()
            time.sleep(3)
        except:
            pass


    def driver_add_new(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver2_2)
        except:
            driver.driver(self, "", "", "")

        number_random = random.randint(2000000, 9999999)
        number_random = str(number_random)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new1).click()
        time.sleep(4)
        increase()
        number = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 7, 2))
        var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 2, 2, "auto"+number)

        wait = WebDriverWait(var_stx.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.add_new_driver_name1)))
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_name1).send_keys("2024auto"+number)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_name2).send_keys("auto"+number)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_phone).send_keys("0359667"+number)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_birth_day).send_keys(var_stx.data['vehicle']['birth_day'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_name1).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_cccd).send_keys("0"+number_random+number)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_email).send_keys(var_stx.data['vehicle']['email'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_account).send_keys("auto"+number)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_password).send_keys(var_stx.data['vehicle']['password'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_manager).click()
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_image)
        time.sleep(1)
        # var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_image).click()
        # time.sleep(2)
        # var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_image_test).click()
        # time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_device_type).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_operating_system).click()   #hệ điều hành
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_fee).click()   #loại cước phí
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_version).click()   #loại cước phí
        time.sleep(1)

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_lot).click()   #sử dụng lốt
            time.sleep(0.5)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_driver_share).click()   #Driver Share
            time.sleep(0.5)
        except:
            pass
        try:
            var_stx.driver.implicitly_wait(0.3)
            var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_gsm1).click()   #Cho phép nhận cuốc GSM
            time.sleep(0.5)
        except:
            pass
        try:
            var_stx.driver.implicitly_wait(0.3)
            var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_gsm2)   #Đồng bộ GSM
            time.sleep(0.5)
        except:
            pass


        #File đính kèm
        button = var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_file_icon)
        var_stx.driver.execute_script("arguments[0].click();", button)
        time.sleep(2)

        # button = var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_file_other)
        # button = var_stx.driver.find_element(By.XPATH, var_stx.add_new4)
        # var_stx.driver.execute_script("arguments[0].click();", button)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new4).click()
        time.sleep(2)
        subprocess.Popen(var_stx.uploadpath+"template_driver.exe")
        time.sleep(4)



        #Thông tin khác
        button = var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_info_icon)
        var_stx.driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        save_button = var_stx.driver.find_element(By.XPATH, var_stx.save)
        ActionChains(var_stx.driver).move_to_element(save_button).perform()
        time.sleep(2)
        #Liên kết dịch vụ - lái hộ
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_driver)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_driver_radio)
        time.sleep(1)
        #Cấu hình khác
        var_stx.driver.find_element(By.XPATH, var_stx.config_other).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_sd_lot)  # sử dụng lốt
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.add_new_debug)  # debug
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, "")
        except:
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, "Tài khoản không có nút debug")


        #Gán xe
        var_stx.driver.find_element(By.XPATH, var_stx.assign_car).click()
        time.sleep(2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.assign_car_choose_car).send_keys("30A38866")
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.assign_car_choose_car1).click()
            time.sleep(2)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.assign_car_choose_car).clear()
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.assign_car_choose_car).send_keys("26 - 30E03976")
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.assign_car_choose_car2).click()
            time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.assign_car1).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.check_assign_car1)
        time.sleep(1)

        button = var_stx.driver.find_element(By.XPATH, var_stx.save)
        var_stx.driver.execute_script("arguments[0].click();", button)
        time.sleep(2.5)
        print("auto"+number)
        module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 14, "auto"+number)

        wait = WebDriverWait(var_stx.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.add_new_driver_message)))
        time.sleep(2)
        module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.2 Lái xe",
                                                 var_stx.add_new_driver_message, "Thêm mới thành công", "_LaiXe_ThemMoi.png")

        var_stx.driver.find_element(By.XPATH, var_stx.close).click()
        time.sleep(4)
        var_stx.driver.back()
        time.sleep(4)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver2_2)
        except:
            var_stx.driver.back()
            time.sleep(4)


        try:
            var_stx.driver.implicitly_wait(1)
            var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_back).click()
            time.sleep(4)
        except:
            try:
                var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver2_2)
            except:
                var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_back1).click()
                time.sleep(4)





    def driver_add_stk(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver2_2)
            # var_stx.driver.find_element(By.XPATH, var_stx.STAXI)
        except:
            driver.driver_add_new(self, "", "", "")
            # driver.driver(self, "", "", "")


        driver1 = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 2, 2))
        driver.driver_x(self)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.search_driver_input).send_keys(driver1)
        except:
            driver.driver(self, "", "", "")
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(2.5)
        try:
            name_check = var_stx.driver.find_element(By.XPATH, var_stx.listdata1_2).text
        except:
            var_stx.driver.refresh()
            time.sleep(7)
            var_stx.driver.find_element(By.XPATH, var_stx.search_driver_input).send_keys(driver1)
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(2.5)
            name_check = var_stx.driver.find_element(By.XPATH, var_stx.listdata1_2).text
        if name_check == driver1:
            var_stx.driver.find_element(By.XPATH, var_stx.listdata1_2a).click()
            time.sleep(5)
            wait = WebDriverWait(var_stx.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.receive_the_activation_code_again)))
            var_stx.driver.find_element(By.XPATH, var_stx.receive_the_activation_code_again).click()
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.receive_the_activation_code_again_cccd).click()
            time.sleep(1)

            var_stx.driver.find_element(By.XPATH, var_stx.info_other_icon).click()
            time.sleep(2)
            element = var_stx.driver.find_element(By.XPATH, "//*[text()='Liên kết ngân hàng']")
            var_stx.driver.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(1)
            element.click()
            time.sleep(2)

            #Liên kết ngân hàng
            # button = var_stx.driver.find_element(By.XPATH, var_stx.bank_Link)
            # var_stx.driver.execute_script("arguments[0].click();", button)

            var_stx.driver.find_element(By.XPATH, var_stx.bank_Link).click()
            time.sleep(2)
            wait = WebDriverWait(var_stx.driver, 20)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.payment_channel)))
            time.sleep(1)
            # element.click()
            # time.sleep(1.5)
            var_stx.driver.find_element(By.XPATH, var_stx.payment_channel_mb).click()
            time.sleep(1.5)
            var_stx.driver.find_element(By.XPATH, var_stx.bank_Link_bank_mb).click()

            var_stx.driver.execute_script("window.scrollBy(0,700)", "")

            # var_stx.driver.find_element(By.XPATH, var_stx.bank_Link_bank).send_keys(var_stx.data['vehicle']['bank'])
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.bank_Link_stk).send_keys(var_stx.data['vehicle']['bank_stk'])
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.bank_Link_name).click()
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.bank_Link_note).send_keys(var_stx.data['vehicle']['bank_note'])
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.bank_Link_qypay)
            var_stx.driver.find_element(By.XPATH, var_stx.bank_Link_auto_get_money)
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.save3).click()
            time.sleep(0.5)

            wait = WebDriverWait(var_stx.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.toast_message)))
            module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.1 Xe",
                                                      var_stx.toast_message, "Thêm tài khoản ngân hàng thành công", "_Xe_CapNhat.png")
            try:
                var_stx.driver.implicitly_wait(1)
                var_stx.driver.find_element(By.XPATH, var_stx.cancel).click()
                time.sleep(3)
            except:
                pass
            var_stx.driver.back()
            time.sleep(5)




    def driver_update(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_cccd)
        except:
            # driver.driver_add_stk(self, "", "", "")
            driver.driver(self, "", "", "")

        driver1 = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 2, 2))
        driver.driver_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.search_driver_input).send_keys(driver1)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.listdata1_2a).click()
        wait = WebDriverWait(var_stx.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Mật khẩu']")))
        time.sleep(2)

        var_stx.driver.find_element(By.XPATH, var_stx.update_driver_makichhoat1).click()    #Nhận lại mã kích hoạt
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.update_driver_makichhoat2).click()    #Nhận lại mã kích hoạt theo CCCD mới
        time.sleep(1)

        var_stx.driver.find_element(By.XPATH, var_stx.add_new_Point).clear()
        var_stx.driver.find_element(By.XPATH, var_stx.add_new_Point).send_keys("99")
        time.sleep(1)
        var_stx.driver.execute_script("window.scrollBy(0,700)", "")

        button = var_stx.driver.find_element(By.XPATH, var_stx.save)
        var_stx.driver.execute_script("arguments[0].click();", button)
        time.sleep(3)
        wait = WebDriverWait(var_stx.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.add_new_driver_message)))
        module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.2 Lái xe",
                                                 var_stx.add_new_driver_message, "Cập nhật thành công", "_LaiXe_CapNhat.png")
        var_stx.driver.find_element(By.XPATH, var_stx.close).click()
        time.sleep(4)

        # try:
        #     var_stx.driver.implicitly_wait(1)
        #     var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_back).click()
        # except:
        #     try:
        #         var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_back1).click()
        #     except:
        #         element = var_stx.driver.find_element(By.XPATH, var_stx.add_new_driver_back)
        #         var_stx.driver.execute_script("arguments[0].scrollIntoView();", element)
        var_stx.driver.back()
        time.sleep(4)

    def detail_vehicle(self, name):
        n = 0
        while (n < 25):
            n = n + 1
            n = str(n)
            path_name = "//*[@class='ag-header-row ag-header-row-column']/div[" + n + "]"
            path_detail = "//*[@class='ag-center-cols-container']/div[1]/div[" + n + "]"
            path_detail_icon = "//*[@class='ag-center-cols-container']/div[1]/div[" + n + "]/span/a/i"

            try:
                name_column = var_stx.driver.find_element(By.XPATH, path_name).text
                print(name_column)
                if name_column == name:
                    try:
                        print("n1")
                        var_stx.driver.find_element(By.XPATH, path_detail).click()
                        time.sleep(1)
                        var_stx.driver.find_element(By.XPATH, path_detail_icon).click()
                        print("n2")
                    except:
                        print("n3")
                        var_stx.driver.find_element(By.XPATH, path_detail_icon).click()
                        print("n4")
                    time.sleep(3)
                    print("n5")
                    break
            except:
                pass
            n = int(n)


    def driver_clock(self, code, eventname, result, path_clock, type_clock, path_check, desire, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver2_2)
        except:
            driver.driver_add_new(self, "", "", "")



        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 2, 2))
        driver.driver_x(self)

        var_stx.driver.find_element(By.XPATH, var_stx.search_driver_input).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)

        scroll_bar = var_stx.driver.find_element(By.XPATH, "//*[@class='ag-body-horizontal-scroll-viewport']")
        try:
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(700, 0).release().perform()
        except:
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(400, 0).release().perform()
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(300, 0).release().perform()
        time.sleep(2.5)

        name1 = var_stx.driver.find_element(By.XPATH, var_stx.listdata1_4).text
        print("name1: "+name1)
        name2 = var_stx.driver.find_element(By.XPATH, var_stx.listdata1_5).text
        print("name2: "+name2)
        name3 = var_stx.driver.find_element(By.XPATH, var_stx.listdata1_6).text
        print("name3: "+name3)
        name4 = var_stx.driver.find_element(By.XPATH, var_stx.listdata1_7).text
        print("name4: "+name4)
        name5 = var_stx.driver.find_element(By.XPATH, var_stx.listdata1_8).text
        print("name5: "+name5)


        if type_clock == "0":
            try:
                var_stx.driver.find_element(By.XPATH, "//*[@class='ag-center-cols-container']/div[1]//*[@class='fa fa-unlock']").click()
                time.sleep(7)
                var_stx.driver.find_element(By.XPATH, var_stx.confirm_lock_day_input).send_keys(var_stx.data['vehicle']['lock_day'])
            except:
                driver.detail_vehicle(self, path_clock)
                var_stx.driver.find_element(By.XPATH, var_stx.confirm_lock_day_input).send_keys(var_stx.data['vehicle']['lock_day'])
            var_stx.driver.find_element(By.XPATH, var_stx.confirm_lock_reason_input).click()
            var_stx.driver.find_element(By.XPATH, var_stx.confirm_lock_reason_input).send_keys(var_stx.data['vehicle']['lock_reason'])

        if type_clock == "1":
            driver.detail_vehicle(self, path_clock)
            time.sleep(7)
            if var_stx.driver.find_element(By.XPATH, var_stx.reason_clock1).is_selected() == False:
                var_stx.driver.find_element(By.XPATH, var_stx.reason_clock1).click()

        time.sleep(3.5)
        var_stx.driver.find_element(By.XPATH, var_stx.confirm).click()
        time.sleep(2)
        wait = WebDriverWait(var_stx.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, path_check)))
        module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.2 Lái xe",
                                                  path_check, desire, name_image)

        try:
            var_stx.driver.implicitly_wait(1)
            var_stx.driver.find_element(By.XPATH, var_stx.close).click()
            time.sleep(1.5)
        except:
            pass


    def driver_detail(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver2_2)
        except:
            driver.driver(self, "", "", "")


        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 2, 2))

        driver.driver_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.search_driver_input).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(7)
        scroll_bar = var_stx.driver.find_element(By.XPATH, "//*[@class='ag-body-horizontal-scroll-viewport']")
        try:
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(700, 0).release().perform()
        except:
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(400, 0).release().perform()
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(300, 0).release().perform()
        time.sleep(2)
        driver.detail_vehicle(self, "Lý do khóa/mở khóa")

        # var_stx.driver.find_element(By.XPATH, var_stx.listdata1_10).click()
        time.sleep(1)
        logging.info("-------------------------")
        logging.info("Xe & Lái xe - 2.2 Lái xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            reason_lock_stt = var_stx.driver.find_element(By.XPATH, var_stx.reason_lock_stt).text
            reason_lock_reason_lock = var_stx.driver.find_element(By.XPATH, var_stx.reason_lock_reason_lock).text
            reason_lock_date = var_stx.driver.find_element(By.XPATH, var_stx.reason_lock_date).text
            logging.info(reason_lock_stt)
            logging.info(reason_lock_reason_lock)
            logging.info(reason_lock_date)
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "STT: {}\nLý do khóa: {}\nNgày khóa: {}"
                                       .format(reason_lock_stt, reason_lock_reason_lock, reason_lock_date))

            if (reason_lock_stt != "") and (reason_lock_reason_lock != "") and (reason_lock_date != ""):
                logging.info("True")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_stx.driver.save_screenshot(var_stx.imagepath + code + "_LaiXe_LyDoKhoa.png")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_LaiXe_LyDoKhoa.png")
        except:
            logging.info("False")
            var_stx.driver.save_screenshot(var_stx.imagepath + code + "_LaiXe_LyDoKhoa.png")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_LaiXe_LyDoKhoa.png")

        time.sleep(1)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.detail_close).click()
            time.sleep(2)
        except:
            pass


    def driver_reward(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver2_2)
            # var_stx.driver.find_element(By.XPATH, var_stx.STAXI)
        except:
            # driver.driver_company_7g_test(self, "", "", "")
            driver.driver(self, "", "", "")



        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 2, 2))
        driver.driver_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.search_driver_input).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(7)
        scroll_bar = var_stx.driver.find_element(By.XPATH, "//*[@class='ag-body-horizontal-scroll-viewport']")
        try:
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(700, 0).release().perform()
        except:
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(400, 0).release().perform()
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(300, 0).release().perform()
        time.sleep(1)

        driver.detail_vehicle(self, "Khen thưởng")


        # var_stx.driver.find_element(By.XPATH, var_stx.listdata1_12).click()
        time.sleep(2)
        try:
            wait = WebDriverWait(var_stx.driver, 15)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.chose_reward)))
            time.sleep(2)
        except:
            pass

        var_stx.driver.find_element(By.XPATH, var_stx.chose_reward).click()
        time.sleep(1.5)
        try:
            var_stx.driver.implicitly_wait(0.3)
            var_stx.driver.find_element(By.XPATH, var_stx.chose_reward_500k).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.chose_reward1).click()
        time.sleep(2)

        var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
        time.sleep(3)
        wait = WebDriverWait(var_stx.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.message)))

        module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.2 Lái xe",
                                                 var_stx.message, "Khen thưởng thành công.", "_LaiXe_Khen.png")

        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.assign_close).click()
            time.sleep(2)
        except:
            pass


    def driver_assign(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver2_2)
            # var_stx.driver.find_element(By.XPATH, var_stx.STAXI)
        except:
            # driver.driver_company_7g_test(self, "", "", "")
            driver.driver(self, "", "", "")



        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 2, 2))
        driver.driver_x(self)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.search_driver_input).send_keys(data)
        except:
            var_stx.driver.refresh()
            time.sleep(6)
            var_stx.driver.find_element(By.XPATH, var_stx.search_driver_input).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(7)
        scroll_bar = var_stx.driver.find_element(By.XPATH, "//*[@class='ag-body-horizontal-scroll-viewport']")
        try:
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(700, 0).release().perform()
        except:
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(400, 0).release().perform()
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(300, 0).release().perform()
        time.sleep(1)

        driver.detail_vehicle(self, "Gán xe")

        # var_stx.driver.find_element(By.XPATH, var_stx.listdata1_13).click()
        time.sleep(2)
        try:
            var_stx.driver.implicitly_wait(1)
            var_stx.driver.find_element(By.XPATH, var_stx.icon_x3).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.assign_confirm).click()
            time.sleep(3)
        except:
            pass

        try:
            wait = WebDriverWait(var_stx.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.chose_vehicle)))
            time.sleep(2)
        except:
            pass
        var_stx.driver.find_element(By.XPATH, var_stx.chose_vehicle).click()
        time.sleep(1.5)
        try:
            var_stx.driver.implicitly_wait(0.3)
            var_stx.driver.find_element(By.XPATH, var_stx.chose_vehicle08).click()
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.chose_vehicle01).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
        time.sleep(1)

        try:
            wait = WebDriverWait(var_stx.driver, 3)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.toast_message)))
            module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.2 Lái xe",
                                                     var_stx.toast_message, "Gán xe thành công", "_LaiXe_GanXe.png")
        except:
            module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.2 Lái xe",
                                                     var_stx.assign_vehicle_success, "Gán xe thành công.", "_LaiXe_GanXe.png")


        time.sleep(4)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.assign_close1).click()
            time.sleep(2)
        except:
            pass
        try:
            var_stx.driver.implicitly_wait(0.3)
            var_stx.driver.find_element(By.XPATH, var_stx.assign_close2).click()
            time.sleep(2)
        except:
            pass


    def driver_get_code_active(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver2_2)
            # var_stx.driver.find_element(By.XPATH, var_stx.STAXI)
        except:
            # driver.driver_company_7g_test(self, "", "", "")
            driver.driver(self, "", "", "")



        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 2, 2))
        driver.driver_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.search_driver_input).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(7)
        scroll_bar = var_stx.driver.find_element(By.XPATH, "//*[@class='ag-body-horizontal-scroll-viewport']")
        try:
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(700, 0).release().perform()
        except:
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(400, 0).release().perform()
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(300, 0).release().perform()
        time.sleep(1)
        driver.detail_vehicle(self, "Lấy mã kích hoạt")

        # var_stx.driver.find_element(By.XPATH, var_stx.listdata1_15).click()
        time.sleep(1)
        try:
            wait = WebDriverWait(var_stx.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.get_code_active)))
            time.sleep(2)
        except:
            pass

        var_stx.driver.find_element(By.XPATH, var_stx.get_code_active).click()
        time.sleep(2)
        wait = WebDriverWait(var_stx.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.check_message)))
        module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.2 Lái xe",
                                                 var_stx.check_message, "Mã kích hoạt đã được cập nhật thành công.", "_LaiXe_LayMaKichHoat.png")

        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.exit).click()
            time.sleep(2)
        except:
            pass


    def driver_change_password(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver2_2)
            # var_stx.driver.find_element(By.XPATH, var_stx.STAXI)
        except:
            # driver.driver_company_7g_test(self, "", "", "")
            driver.driver(self, "", "", "")


        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 2, 2))

        driver.driver_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.search_driver_input).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(7)
        scroll_bar = var_stx.driver.find_element(By.XPATH, "//*[@class='ag-body-horizontal-scroll-viewport']")
        try:
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(700, 0).release().perform()
        except:
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(400, 0).release().perform()
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(300, 0).release().perform()
        time.sleep(1)
        driver.detail_vehicle(self, "Đổi mật khẩu")

        # var_stx.driver.find_element(By.XPATH, var_stx.listdata1_16).click()
        time.sleep(2)

        try:
            wait = WebDriverWait(var_stx.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.driver_change_password)))
            time.sleep(2)
        except:
            pass


        var_stx.driver.find_element(By.XPATH, var_stx.driver_change_password).send_keys(var_stx.data['vehicle']['new_password'])
        time.sleep(3)
        var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
        time.sleep(2)
        wait = WebDriverWait(var_stx.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.message)))
        module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.2 Lái xe",
                                                 var_stx.message, "Đổi mật khẩu thành công.", "_LaiXe_DoiMatKhau.png")

        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.close).click()
            time.sleep(2)
        except:
            pass


    def driver_detail_device(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver2_2)
            # var_stx.driver.find_element(By.XPATH, var_stx.STAXI)
        except:
            # driver.driver_company_7g_test(self, "", "", "")
            driver.driver(self, "", "", "")


        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 2, 2))

        driver.driver_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.search_driver_input).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(10)
        scroll_bar = var_stx.driver.find_element(By.XPATH, "//*[@class='ag-body-horizontal-scroll-viewport']")
        try:
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(700, 0).release().perform()
        except:
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(400, 0).release().perform()
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(300, 0).release().perform()
        time.sleep(1)
        driver.detail_vehicle(self, "Chi tiết thiết bị")

        # var_stx.driver.find_element(By.XPATH, var_stx.listdata1_18).click()
        time.sleep(2)
        try:
            wait = WebDriverWait(var_stx.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.update_driver_imei)))
            time.sleep(2)
        except:
            pass


        logging.info("-------------------------")
        logging.info("Xe & Lái xe - 2.2 Lái xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            update_driver_imei = var_stx.driver.find_element(By.XPATH, var_stx.update_driver_imei).text
            update_driver_day = var_stx.driver.find_element(By.XPATH, var_stx.update_driver_day).text
            update_driver_code = var_stx.driver.find_element(By.XPATH, var_stx.update_driver_code).text
            update_driver_disign = var_stx.driver.find_element(By.XPATH, var_stx.update_driver_disign).text
            update_driver_sx = var_stx.driver.find_element(By.XPATH, var_stx.update_driver_sx).text
            update_driver_version = var_stx.driver.find_element(By.XPATH, var_stx.update_driver_version).text
            update_driver_device = var_stx.driver.find_element(By.XPATH, var_stx.update_driver_device).text
            update_driver_network = var_stx.driver.find_element(By.XPATH, var_stx.update_driver_network).text

            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "{}, {}, {}, {}, {}, {}"
                                       .format(update_driver_imei, update_driver_day, update_driver_code, update_driver_disign,
                                               update_driver_sx, update_driver_version, update_driver_device, update_driver_network))

            if (update_driver_imei == "IMEI") and (update_driver_day == "Ngày hiệu lực") and (update_driver_code == "Mã kích hoạt") and \
                (update_driver_disign == "Mẫu thiết kế") and (update_driver_sx == "Hãng sản xuất") and (update_driver_version == "Phiên bản") and \
                    (update_driver_device == "Thiết bị") and (update_driver_network == "Mạng"):
                logging.info("True")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_stx.driver.save_screenshot(var_stx.imagepath + code + "_LaiXe_ChiTietThietBi.png")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_LaiXe_ChiTietThietBi.png")
        except:
            logging.info("False")
            var_stx.driver.save_screenshot(var_stx.imagepath + code + "_LaiXe_ChiTietThietBi.png")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_LaiXe_ChiTietThietBi.png")


        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.back1).click()
            time.sleep(3)
        except:
            pass


    def driver_info_driver(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver2_2)
            # var_stx.driver.find_element(By.XPATH, var_stx.STAXI)
        except:
            # driver.driver_company_7g_test(self, "", "", "")
            driver.driver(self, "", "", "")


        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 2, 2))
        driver.driver_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.search_driver_input).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(10)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.listdata1_2)
        except:
            var_stx.driver.refresh()
            time.sleep(7)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(10)

        scroll_bar = var_stx.driver.find_element(By.XPATH, "//*[@class='ag-body-horizontal-scroll-viewport']")
        try:
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(700, 0).release().perform()
        except:
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(400, 0).release().perform()
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(300, 0).release().perform()
        time.sleep(1)

        driver.detail_vehicle(self, "Cấu hình lái xe")

        # var_stx.driver.find_element(By.XPATH, var_stx.listdata1_21).click()
        time.sleep(2)

        try:
            wait = WebDriverWait(var_stx.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.info_driver1)))
            time.sleep(2)
        except:
            pass


        logging.info("-------------------------")
        logging.info("Xe & Lái xe - 2.2 Lái xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            info_driver1 = var_stx.driver.find_element(By.XPATH, var_stx.info_driver1).text
            info_driver2 = var_stx.driver.find_element(By.XPATH, var_stx.info_driver2).text
            info_driver3 = var_stx.driver.find_element(By.XPATH, var_stx.info_driver3).text
            info_driver4 = var_stx.driver.find_element(By.XPATH, var_stx.info_driver4).text
            info_driver5 = var_stx.driver.find_element(By.XPATH, var_stx.info_driver5).text
            info_driver6 = var_stx.driver.find_element(By.XPATH, var_stx.info_driver6).text
            info_driver7 = var_stx.driver.find_element(By.XPATH, var_stx.info_driver7).text
            info_driver8 = var_stx.driver.find_element(By.XPATH, var_stx.info_driver8).text


            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, "{}, {}, {}, {}, {}, {}, {}, {}"
                                       .format(info_driver1, info_driver2, info_driver3, info_driver4, info_driver5, info_driver6,
                                               info_driver7, info_driver8))

            if (info_driver1 == "Cho phép nhận cuốc BE:") and (info_driver2 == "Bật nhận cuốc BE:") and (info_driver3 == "Tự động nhận cuốc BE:") and \
                (info_driver4 == "Cho phép nhận cuốc GSM:") and (info_driver5 == "Bật nhận cuốc GSM:") and (info_driver6 == "Tự động nhận cuốc GSM:")\
                    and (info_driver7 == "Cho phép nhận cuốc Lái hộ:") and (info_driver8 == "Bật nhận cuốc Lái hộ:"):
                logging.info("True")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_stx.driver.save_screenshot(var_stx.imagepath + code + "_LaiXe_ThongTinLaiXe.png")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_LaiXe_ThongTinLaiXe.png")
        except:
            logging.info("False")
            var_stx.driver.save_screenshot(var_stx.imagepath + code + "_LaiXe_ThongTinLaiXe.png")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_LaiXe_ThongTinLaiXe.png")


        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.exit).click()
            time.sleep(3)
        except:
            pass


    def driver_info_driver_sync(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver2_2)
            # var_stx.driver.find_element(By.XPATH, var_stx.STAXI)
        except:
            # driver.driver_company_7g_test(self, "", "", "")
            driver.driver(self, "", "", "")


        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 2, 2))
        driver.driver_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.search_driver_input).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(7)
        scroll_bar = var_stx.driver.find_element(By.XPATH, "//*[@class='ag-body-horizontal-scroll-viewport']")
        try:
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(700, 0).release().perform()
        except:
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(400, 0).release().perform()
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(300, 0).release().perform()
        time.sleep(1)
        driver.detail_vehicle(self, "SyncGSM")

        # var_stx.driver.find_element(By.XPATH, var_stx.listdata1_20).click()
        time.sleep(2)
        wait = WebDriverWait(var_stx.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.toast_message)))
        module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.2 Lái xe",
                                                 var_stx.toast_message, "Đồng bộ dữ liệu GSM thất bại, vui lòng kiểm tra thông tin thành phố Cấu hình tại đây",
                                                  "_LaiXe_SyncGSM.png")



    def driver_delete(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver2_2)
            # var_stx.driver.find_element(By.XPATH, var_stx.STAXI)
        except:
            # driver.driver_company_7g_test(self, "", "", "")
            driver.driver(self, "", "", "")


        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 2, 2))
        driver.driver_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.search_driver_input).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3)
        scroll_bar = var_stx.driver.find_element(By.XPATH, "//*[@class='ag-body-horizontal-scroll-viewport']")
        try:
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(700, 0).release().perform()
        except:
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(400, 0).release().perform()
            ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(300, 0).release().perform()
        time.sleep(1)
        # var_stx.driver.find_element(By.XPATH, var_stx.listdata1_17).click()
        driver.detail_vehicle(self, "Xóa")

        time.sleep(3)

        try:
            wait = WebDriverWait(var_stx.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.delete_driver_confirm)))
            time.sleep(2)
        except:
            pass

        try:
            check_name = var_stx.driver.find_element(By.XPATH, var_stx.name_driver_delete).text
        except:
            var_stx.driver.refresh()
            time.sleep(5)
            driver.driver_x(self)
            var_stx.driver.find_element(By.XPATH, var_stx.search_driver_input).send_keys(data)
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(3)
            scroll_bar = var_stx.driver.find_element(By.XPATH, "//*[@class='ag-body-horizontal-scroll-viewport']")
            try:
                ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(700, 0).release().perform()
            except:
                ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(400, 0).release().perform()
                ActionChains(var_stx.driver).click_and_hold(scroll_bar).move_by_offset(300, 0).release().perform()
            driver.detail_vehicle(self, "Xóa")
            check_name = var_stx.driver.find_element(By.XPATH, var_stx.name_driver_delete).text

        if check_name == data:
            var_stx.driver.find_element(By.XPATH, var_stx.delete_driver_confirm).click()
            element = WebDriverWait(var_stx.driver, 10).until(EC.presence_of_element_located((By.XPATH, var_stx.delete_driver_succes)))
            time.sleep(0.2)
            module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.2 Lái xe",
                                                      var_stx.delete_driver_succes, "Xóa lái xe thành công", "_LaiXe_Xoa.png")
        else:
            var_stx.driver.find_element(By.XPATH, var_stx.cancel).click()
        time.sleep(5)


    def driver_hide_column(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver2_2)
        except:
            driver.driver(self, "", "", "")


        var_stx.driver.refresh()
        time.sleep(5)

        # driver.driver_x(self)
        # var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        # time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.hide_column).click()
        time.sleep(2)
        if var_stx.driver.find_element(By.XPATH, var_stx.hide_column1_input).is_selected() == True:
            var_stx.driver.find_element(By.XPATH, var_stx.hide_column1_input).click()
            time.sleep(1.5)
        module_other_stx.write_result_not_displayed_try(code, eventname, result, "Xe & Lái xe - 2.2 Lái xe",
                                                  var_stx.vehicle_hide_column_stt, "_LaiXe_AnHienCot.png")



        if var_stx.driver.find_element(By.XPATH, var_stx.hide_column1_input).is_selected() == False:
            var_stx.driver.find_element(By.XPATH, var_stx.hide_column1_input).click()
            time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.hide_column).click()
        time.sleep(1.5)


    def driver_sd_lot(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_vehicle_driver2_2)
        except:
            driver.driver(self, "", "", "")

        var_stx.driver.refresh()
        time.sleep(7)

        var_stx.driver.find_element(By.XPATH, var_stx.driver_sd_lot).click()
        time.sleep(2.5)
        var_stx.driver.find_element(By.XPATH, var_stx.ddlSendArticleType3).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.SendListDriver_chosen).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.SendListDriver_chosen_select).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.update).click()
        time.sleep(2.5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "Xe & Lái xe - 2.2 Lái xe",
                                                 var_stx.message, "Gắn lái xe sử dụng lốt thành công", "_LaiXe_SuDungLot.png")

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.close).click()
            time.sleep(2.5)
        except:
            pass



