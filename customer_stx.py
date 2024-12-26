import logging
import var_stx
import time
from selenium.webdriver.common.by import By
import module_other_stx
import login_stx
import minitor_stx
import vehicle_driver_stx
from retry import retry
import minitor_stx
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import promotion_stx




def get_info_web():
    var_stx.driver.implicitly_wait(0.05)
    row = 119
    n = 1
    while (n < 50):
        n += 1
        n = str(n)
        row += 1
        path_column = "//*[@class='table table-hover table-bordered']/tbody/tr[1]/th[" + n + "]"
        path_data = "//*[@class='table table-hover table-bordered']/tbody/tr[2]/td[" + n + "]"
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






class list_customer:

    def list_customer(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])


        var_stx.driver.find_element(By.XPATH, var_stx.customer).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.list_customer).click()
        time.sleep(10)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.1 Danh sách khách hàng",
                                                  var_stx.title_page, "7.1 Danh sách khách hàng", "_DanhSachKhachHang.png")


    def list_customer_g7_test(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx_g7test(self, var_stx.data['login']['tk_admin_test'],  var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.customer).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.list_customer).click()
        time.sleep(2.5)


    def list_customer_x(self):
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
            var_stx.driver.find_element(By.XPATH, var_stx.name_sdt_email).clear()
        except:
            pass
        var_stx.driver.find_element(By.XPATH, var_stx.groupid0).click()
        time.sleep(0.3)
        var_stx.driver.find_element(By.XPATH, var_stx.custrank0).click()
        time.sleep(0.3)
        var_stx.driver.find_element(By.XPATH, var_stx.name_sdt_email).click()
        time.sleep(0.3)


    def list_customer_from_to_day(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_customer)
        except:
            list_customer.list_customer(self, "", "", "")

        list_customer.list_customer_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys(var_stx.data['customer']['from_day'])
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys(var_stx.data['customer']['to_day'])
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if_cut1(code, eventname, result, "KHÁCH HÀNG - 7.1 Danh sách khách hàng",
                                              var_stx.list_data2_7, "22/11/2024", "_DanhSachKhachHang_TuNgayDenNgay.png", -10)


    def list_customer_search(self, code, eventname, result, data, path_check, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_customer)
        except:
            list_customer.list_customer(self, "", "", "")

        list_customer.list_customer_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.name_sdt_email).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(10)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.1 Danh sách khách hàng",
                                              path_check, data, name_image)


    def list_customer_group(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_customer)
        except:
            list_customer.list_customer(self, "", "", "")

        list_customer.list_customer_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.groupid).click()
        time.sleep(1)
        name_group = var_stx.driver.find_element(By.XPATH, var_stx.groupid2).text
        print("name group"+ name_group)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.groupid2).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(10)
        var_stx.driver.find_element(By.XPATH, var_stx.list_data2_12).click()
        time.sleep(2.5)

        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.1 Danh sách khách hàng",
                                              var_stx.check_list_customer_group, name_group, "_DanhSachKhachHang_Nhom.png")

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.exit).click()
            time.sleep(2)
        except:
            pass


    def list_customer_rank(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_customer)
        except:
            list_customer.list_customer(self, "", "", "")

        list_customer.list_customer_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.custrank).click()
        time.sleep(1.5)
        name_rank = var_stx.driver.find_element(By.XPATH, var_stx.custrank1).text
        print("rank: "+ name_rank)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.custrank1).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(8)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.1 Danh sách khách hàng",
                                              var_stx.list_data2_4, name_rank, "_DanhSachKhachHang_Hang.png")


    def list_customer_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_customer)
        except:
            list_customer.list_customer_group(self, "", "", "")

        list_customer.list_customer_x(self)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.groupid2).click()
        time.sleep(1)

        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(10)
        var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        time.sleep(13)
        module_other_stx.write_result_dowload_file(code, eventname, result, "KHÁCH HÀNG - 7.1 Danh sách khách hàng",
                                                        "_DanhSachKhachHang.xls", "_DanhSachKhachHang_XuatExcel.png")

        # minitor_stx.get_info_web()
        # try:
        #     minitor_stx.get_info_excel(5, "Sheet 1")
        # except:
        #     var_stx.driver.refresh()
        #     time.sleep(7)
        #     var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        #     time.sleep(7)
        #     minitor_stx.get_info_web()
        #     minitor_stx.get_info_excel(5, "Sheet 1")
        # minitor_stx.check_info_web_excel(code, eventname, result, "KHÁCH HÀNG - 7.1 Danh sách khách hàng")
        #
        # var_stx.driver.back()
        # time.sleep(5)


    def list_customer_addnew(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_customer)
        except:
            list_customer.list_customer_rank(self, "", "", "")

        vehicle_driver_stx.increase()
        number = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 7, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.add_new3).click()
        time.sleep(3.5)
        var_stx.driver.find_element(By.XPATH, var_stx.phone_number).send_keys("0835210"+number)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.full_name).send_keys("Auto_customer_"+number)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.email).send_keys("Auto" + number + "@gmail.com")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.list_customer_addnew_group).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.save).click()
        time.sleep(3)
        var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 28, 2, "Auto_customer_"+number)
        module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 14, "Auto_customer_"+number)

        print("message: " + "Khách hàng Auto_customer_"+number+" đã được thêm mới thành công")

        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.1 Danh sách khách hàng",
                                              var_stx.text_success, "Khách hàng Auto_customer_"+number+" đã được thêm mới thành công", "_DanhSachKhachHang_ThemMoi.png")
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.back1).click()
            time.sleep(7)
        except:
            pass

        #Khách hàng Auto_customer163 đã được thêm mới thành công


    def list_customer_lock(self, code, eventname, result, desire, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_customer)
        except:
            list_customer.list_customer(self, "", "", "")


        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 28, 2))
        try:
            var_stx.driver.implicitly_wait(1)
            var_stx.driver.find_element(By.XPATH, "//*[@class='table table-hover table-bordered']/tbody/tr[2]//*[text()='"+data+"']")
        except:
            list_customer.list_customer_x(self)
            var_stx.driver.find_element(By.XPATH, var_stx.name_sdt_email).send_keys(data)
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(15)
        var_stx.driver.find_element(By.XPATH, var_stx.list_data2_10_button).click()
        time.sleep(5)
        var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
        time.sleep(2.5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.1 Danh sách khách hàng",
                                                        var_stx.message, desire, name_image)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.close1).click()
            time.sleep(12)
        except:
            pass


    def list_customer_get_code(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_customer)
        except:
            list_customer.list_customer(self, "", "", "")

        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 28, 2))
        try:
            var_stx.driver.implicitly_wait(1)
            var_stx.driver.find_element(By.XPATH, "//*[@class='table table-hover table-bordered']/tbody/tr[2]//*[text()='"+data+"']")
        except:
            list_customer.list_customer_x(self)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(10)
        var_stx.driver.find_element(By.XPATH, var_stx.list_data2_11_button).click()
        time.sleep(3)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.1 Danh sách khách hàng",
                                                        var_stx.popup_message, "Bạn chưa đăng ký mã kích hoạt", "_DanhSachKhachHang_LayMaKichHoat.png")

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.exit).click()
            time.sleep(7)
        except:
            pass


    def list_customer_assign_group(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_customer)
        except:
            list_customer.list_customer(self, "", "", "")

        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 28, 2))
        try:
            var_stx.driver.implicitly_wait(1)
            var_stx.driver.find_element(By.XPATH, "//*[@class='table table-hover table-bordered']/tbody/tr[2]//*[text()='"+data+"']")
        except:
            list_customer.list_customer_x(self)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(10)

        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.list_data2_12_button).click()
        time.sleep(3)
        try:
            var_stx.driver.implicitly_wait(1)
            var_stx.driver.find_element(By.XPATH, var_stx.list_customer_assign_group_x).click()
        except:
            pass

        var_stx.driver.find_element(By.XPATH, var_stx.list_customer_addnew_group_select).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.list_customer_addnew_group1).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.igree2).click()
        time.sleep(3)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.1 Danh sách khách hàng",
                                                        var_stx.message, "Gán nhóm khách hàng thành công!", "_DanhSachKhachHang_GanNhom.png")

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.close1).click()
            time.sleep(7)
        except:
            pass


    def list_customer_detail_device(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_customer)
        except:
            # list_customer.list_customer_addnew(self, "", "", "")
            list_customer.list_customer(self, "", "", "")

        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 28, 2))
        try:
            var_stx.driver.implicitly_wait(1)
            var_stx.driver.find_element(By.XPATH, "//*[@class='table table-hover table-bordered']/tbody/tr[2]//*[text()='"+data+"']")
        except:
            list_customer.list_customer_x(self)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(10)

        var_stx.driver.find_element(By.XPATH, var_stx.list_data2_13_button).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.1 Danh sách khách hàng",
                                                        var_stx.check_list_customer_detail_device, "Thông tin thiết bị",
                                                  "_DanhSachKhachHang_ThongTinthietBi.png")

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.list_customer_detail_device_exit).click()
            time.sleep(8)
        except:
            pass


    def list_customer_detail_icon(self, code, eventname, result, path_icon, desire, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_customer)
        except:
            list_customer.list_customer(self, "", "", "")


        data = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 28, 2))
        try:
            var_stx.driver.implicitly_wait(1)
            var_stx.driver.find_element(By.XPATH, "//*[@class='table table-hover table-bordered']/tbody/tr[2]//*[text()='"+data+"']")
        except:

            list_customer.list_customer_x(self)
            var_stx.driver.find_element(By.XPATH, var_stx.name_sdt_email).send_keys(data)
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(10)

        var_stx.driver.find_element(By.XPATH, path_icon).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.1 Danh sách khách hàng",
                                                  var_stx.title_page2, desire, name_image)


        check_page = var_stx.driver.find_element(By.XPATH, var_stx.title_page2).text
        if check_page == desire:
            var_stx.driver.back()
            time.sleep(7)








class contract_card:



    def partner(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.customer).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.contract_card).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.partner).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.1 Đối tác",
                                                  var_stx.title_page1, "7.7.1 Đối tác", "_Doitac.png")


    def partner_g7_test(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx_g7test(self, var_stx.data['login']['tk_admin_test'],  var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.customer).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.contract_card).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.partner).click()
        time.sleep(3.5)


    def partner_x(self):
        var_stx.driver.implicitly_wait(0.2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.name).clear()
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.sdt).clear()
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.SearchCompanyId).click()
            time.sleep(0.3)
        except:
            pass


    def partner_search(self, code, eventname, result, path_input, data, path_check, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_partner)
        except:
            contract_card.partner(self, "", "", "")

        contract_card.partner_x(self)
        var_stx.driver.find_element(By.XPATH, path_input).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(7)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.1 Đối tác",
                                              path_check, data, name_image)


    def partner_combobox(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_partner)
        except:
            contract_card.partner(self, "", "", "")

        contract_card.partner_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.SearchCompanyId_select).click()
        time.sleep(1.5)
        name_company = var_stx.driver.find_element(By.XPATH, var_stx.SearchCompanyId_2).text
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.SearchCompanyId_2).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(7)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.1 Đối tác",
                                              var_stx.list_data2_5, name_company, "_Doitac_CongTy.png")


    def partner_addnew(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_partner)
        except:
            contract_card.partner(self, "", "", "")

        contract_card.partner_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new1).click()
        time.sleep(2.5)

        vehicle_driver_stx.increase()
        number = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 7, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.partner_addnew_code).send_keys("Auto_" + number)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.partner_addnew_name).send_keys("Auto_name_partner_" + number)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.partner_addnew_phone).send_keys("0835219" + number)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.partner_addnew_email).send_keys(f"Auto_{number}@gmail.com")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.partner_addnew_company1).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.save_1).click()
        time.sleep(1.5)
        module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 14, "Auto_name_partner_" + number)
        var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 29, 2, "Auto_name_partner_"+number)

        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.1 Đối tác",
                                                  var_stx.partner_addnew, "Thêm mới đối tác thành công!", "_Doitac_ThemMoi.png")


    def partner_update(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_partner)
        except:
            contract_card.partner_addnew(self, "", "", "")


        contract_card.partner_x(self)
        vehicle_driver_stx.increase()
        number = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 7, 2))
        name = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 29, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.name).send_keys(name)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(7)
        var_stx.driver.find_element(By.XPATH, var_stx.list_data2_2_button).click()
        time.sleep(2.5)
        var_stx.driver.find_element(By.XPATH, var_stx.partner_addnew_phone).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.partner_addnew_phone).send_keys(" 0995219" + number)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.save_1).click()
        time.sleep(1.5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.1 Đối tác",
                                                  var_stx.partner_update, "Cập nhật thông tin danh sách đối tác thành công!", "_Doitac_CapNhat.png")
        time.sleep(1.5)


    def partner_delete(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_partner)
            var_stx.driver.find_element(By.XPATH, var_stx.STAXI)
        except:
            contract_card.partner_addnew(self, "", "", "")


        contract_card.partner_x(self)
        vehicle_driver_stx.increase()
        number = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 7, 2))
        name = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 29, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.name).send_keys(name)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(7)
        var_stx.driver.find_element(By.XPATH, var_stx.list_data2_delete).click()
        time.sleep(2.5)
        var_stx.driver.find_element(By.XPATH, var_stx.delete).click()
        time.sleep(2)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.1 Đối tác",
                                                  var_stx.partner_delete, "Xóa thông tin đối tác thành công!", "_Doitac_Xoa.png")
        time.sleep(1.5)










    def contract(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.customer).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.contract_card).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.contract).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.2 Hợp đồng",
                                                  var_stx.title_page1, "7.7.2 Hợp đồng", "_HopDong.png")


    def contract_g7_test(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx_g7test(self, var_stx.data['login']['tk_admin_test'],  var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.customer).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.contract_card).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.contract).click()
        time.sleep(3.5)


    def contract_x(self):
        var_stx.driver.implicitly_wait(0.2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.code_contract).clear()
            time.sleep(0.3)
        except:
            pass
        var_stx.driver.find_element(By.XPATH, var_stx.SearchCompanyId).click()
        time.sleep(0.3)


    def contract_search(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_contract)
        except:
            contract_card.contract(self, "", "", "")

        contract_card.contract_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(6)
        data = var_stx.driver.find_element(By.XPATH, var_stx.list_data3_1).text

        var_stx.driver.find_element(By.XPATH, var_stx.code_contract).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(6)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.2 Hợp đồng",
                                              var_stx.list_data2_1, data, "_HopDong_Ten.png")


    def contract_combobox(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_contract)
        except:
            contract_card.contract(self, "", "", "")

        contract_card.contract_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.SearchCompanyId_select).click()
        time.sleep(1.5)
        name_company = var_stx.driver.find_element(By.XPATH, var_stx.SearchCompanyId_2).text
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.SearchCompanyId_2).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(6)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.2 Hợp đồng",
                                              var_stx.list_data2_2, name_company, "_HopDong_CongTy.png")


    def contract_addnew(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_contract)
        except:
            contract_card.contract(self, "", "", "")

        contract_card.partner_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.add_new1).click()
        time.sleep(2.5)

        vehicle_driver_stx.increase()
        number = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 7, 2))
        var_stx.driver.find_element(By.XPATH, var_stx.contract_addnew_contract).click()
        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.contract_addnew_code).send_keys("Auto_" + number)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.contract_addnew_sdt).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.contract_addnew_sdt).send_keys("0835219" + number)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.contract_addnew_hd).send_keys("100.000.000")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.contract_addnew_kyquy).send_keys("10.000.000")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.contract_addnew_status).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.contract_addnew_image).send_keys("https://g7test.staxi.vn/Media/Uploads/%E2%80%94Pngtree%E2%80%94car_flag_icon_333837.png")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.contract_addnew_company).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.contract_addnew_note).send_keys("Test ghi chú tạo hợp đồng")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.contract_addnew_tk_company).click()
        time.sleep(1.5)

        var_stx.driver.find_element(By.XPATH, var_stx.contract_addnew_mst).send_keys("350080643")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.contract_addnew_adress).send_keys("Lô 14 Nguyễn Cảnh Dị, Đại Kim, Hoàng Mai, Hà Nội")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.contract_addnew_email).send_keys(f"Auto_{number}@gmail.com")
        time.sleep(1.5)

        var_stx.driver.find_element(By.XPATH, var_stx.save_1).click()
        time.sleep(1.5)
        module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 14, "Auto_" + number)
        var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 30, 2, "Auto_" + number)

        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.2 Hợp đồng",
                                                  var_stx.contract_addnew, "Thêm mới hợp đồng thành công", "_HopDong_ThemMoi.png")


    def contract_update(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_contract)
        except:
            contract_card.contract_addnew(self, "", "", "")


        contract_card.contract_x(self)
        vehicle_driver_stx.increase()
        number = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 7, 2))
        name = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 30, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.code_contract).send_keys(name)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        var_stx.driver.find_element(By.XPATH, var_stx.list_data1_button).click()
        time.sleep(2.5)
        var_stx.driver.find_element(By.XPATH, var_stx.sdt).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.sdt).send_keys(" 0995219" + number)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.save_1).click()
        time.sleep(1.5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.2 Hợp đồng",
                                                  var_stx.contract_update, "Cập nhật hợp đồng thành công", "_HopDong_CapNhat.png")
        time.sleep(1.5)


    def contract_see_file(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_contract)
        except:
            contract_card.contract_addnew(self, "", "", "")


        contract_card.contract_x(self)
        name = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 30, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.code_contract).send_keys(name)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(6)
        var_stx.driver.find_element(By.XPATH, var_stx.list_data2_3_button).click()
        time.sleep(2.5)
        module_other_stx.write_result_text_try_if_src(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.2 Hợp đồng",
                                              var_stx.contract_see_file, "https://g7test.staxi.vn/Media/Uploads/%E2%80%94Pngtree%E2%80%94car_flag_icon_333837.png",
                                                      "_HopDong_XemFile.png")

        try:
            button = var_stx.driver.find_element(By.XPATH, var_stx.contract_see_file_close)
            var_stx.driver.execute_script("arguments[0].click();", button)
            time.sleep(5)
        except:
            pass


    def contract_delete(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_contract)
        except:
            contract_card.contract_addnew(self, "", "", "")


        contract_card.contract_x(self)
        name = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 30, 2))

        var_stx.driver.find_element(By.XPATH, var_stx.code_contract).send_keys(name)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(6)
        check_name = var_stx.driver.find_element(By.XPATH, var_stx.list_data2_1).text
        if name == check_name:
            var_stx.driver.find_element(By.XPATH, var_stx.list_data2_delete).click()
            time.sleep(2)
            var_stx.driver.find_element(By.XPATH, var_stx.delete).click()
            time.sleep(1.5)
            module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.2 Hợp đồng",
                                                      var_stx.contract_delete, "Xóa hợp đồng thành công", "_HopDong_Xoa.png")
            time.sleep(1.5)










    def card_management(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.customer).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.contract_card).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.card_management).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.3 Quản lý thẻ",
                                                  var_stx.title_page1, "7.7.3 Quản lý thẻ", "_QuanLyThe.png")


    def card_management_g7_test(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx_g7test(self, var_stx.data['login']['tk_admin_test'],  var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.customer).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.contract_card).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.card_management).click()
        time.sleep(5)


    def card_management_x(self):
        var_stx.driver.implicitly_wait(0.2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.number_serial).clear()
            time.sleep(0.3)
        except:
            pass

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.sdt).clear()
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.code_hd).clear()
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.name_customer).clear()
            time.sleep(0.3)
        except:
            pass

        var_stx.driver.find_element(By.XPATH, var_stx.SearchCompanyId).click()
        time.sleep(0.3)
        var_stx.driver.find_element(By.XPATH, var_stx.CardControl).click()
        time.sleep(0.3)
        var_stx.driver.find_element(By.XPATH, var_stx.StatusSearch).click()
        time.sleep(0.3)
        var_stx.driver.find_element(By.XPATH, var_stx.PaidMethod).click()
        time.sleep(0.3)
        var_stx.driver.find_element(By.XPATH, var_stx.StatusBFA).click()
        time.sleep(0.3)


    def card_management_x1(self):
        var_stx.driver.implicitly_wait(0.2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.number_serial).clear()
            time.sleep(0.3)
        except:
            pass

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.sdt).clear()
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.code_hd).clear()
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.name_customer).clear()
            time.sleep(0.3)
        except:
            pass

        var_stx.driver.find_element(By.XPATH, var_stx.SearchCompanyId).click()
        time.sleep(0.3)
        var_stx.driver.find_element(By.XPATH, var_stx.CardControl).click()
        time.sleep(0.3)
        var_stx.driver.find_element(By.XPATH, var_stx.StatusSearch).click()
        time.sleep(0.3)
        var_stx.driver.find_element(By.XPATH, var_stx.PaidMethod).click()
        time.sleep(0.3)
        var_stx.driver.find_element(By.XPATH, var_stx.StatusBFA).click()
        time.sleep(0.3)

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.sdt).send_keys("0987")
            time.sleep(0.3)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(5)
        except:
            pass


    def card_management_search(self, code, eventname, result, path_input, data, path_check, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_card_management)
        except:
            contract_card.card_management(self, "", "", "")

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.check_page2)
            contract_card.card_management_x1(self)
        except:
            pass
        contract_card.card_management_x(self)

        var_stx.driver.find_element(By.XPATH, path_input).send_keys(data)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.3 Quản lý thẻ",
                                              path_check, data, name_image)


    def card_management_company(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_card_management)
        except:
            contract_card.card_management(self, "", "", "")

        # try:
        #     var_stx.driver.find_element(By.XPATH, var_stx.check_page2)
        #     contract_card.card_management_x1(self)
        # except:
        #     pass

        contract_card.card_management_x(self)

        var_stx.driver.find_element(By.XPATH, var_stx.SearchCompanyId).click()
        time.sleep(1)
        name = var_stx.driver.find_element(By.XPATH, var_stx.SearchCompanyId1).text
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.SearchCompanyId1).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)


        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.3 Quản lý thẻ",
                                              var_stx.list_data2_4, name, "_QuanLyThe_CongTy.png")


    def card_management_status(self, code, eventname, result, path_card_management_status, path_check, desire, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_card_management)
        except:
            contract_card.card_management(self, "", "", "")


        # try:
        #     var_stx.driver.find_element(By.XPATH, var_stx.check_page2)
        #     contract_card.card_management_x1(self)
        # except:
        #     pass

        contract_card.card_management_x(self)

        var_stx.driver.find_element(By.XPATH, path_card_management_status).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        logging.info("-------------------------")
        logging.info("KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.3 Quản lý thẻ")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            check_text = var_stx.driver.find_element(By.XPATH, path_check).get_attribute("title")
            logging.info(check_text)
            logging.info(desire)
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, check_text)
            if check_text == desire:
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


    def card_management_card(self, code, eventname, result, card_management_card, path_check, desire, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_card_management)
        except:
            contract_card.card_management(self, "", "", "")

        # try:
        #     var_stx.driver.find_element(By.XPATH, var_stx.check_page2)
        #     contract_card.card_management_x1(self)
        # except:
        #     pass

        contract_card.card_management_x(self)

        var_stx.driver.find_element(By.XPATH, card_management_card).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.3 Quản lý thẻ",
                                              path_check, desire, name_image)


    def card_management_qr(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_card_management)
        except:
            contract_card.card_management(self, "", "", "")


        # try:
        #     var_stx.driver.find_element(By.XPATH, var_stx.check_page2)
        #     contract_card.card_management_x1(self)
        # except:
        #     pass

        var_stx.driver.find_element(By.XPATH, var_stx.card_management_qr).click()
        time.sleep(1.5)
        module_other_stx.write_result_text_try_if_cut2(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.3 Quản lý thẻ",
                                              var_stx.toast_message, "Thành công lưu lại:", "_QuanLyThe_QRCode.png", 0, 19)


    def card_management_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_card_management)
        except:
            contract_card.card_management(self, "", "", "")

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.check_page2)
            contract_card.card_management_x1(self)
        except:
            pass

        var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        time.sleep(5)
        module_other_stx.write_result_dowload_file(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.3 Quản lý thẻ",
                                                        "_QuanLyThe.xlsx", "_QuanLyThe_XuatExcel.png")

        # minitor_stx.get_info_web()
        # try:
        #     minitor_stx.get_info_excel1(5, "Sheet 1")
        # except:
        #     var_stx.driver.refresh()
        #     time.sleep(7)
        #     var_stx.driver.find_element(By.XPATH, var_stx.MobileSearch).clear()
        #     var_stx.driver.find_element(By.XPATH, var_stx.MobileSearch).send_keys("09881")
        #     time.sleep(1)
        #     var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        #     time.sleep(4)
        #     var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        #     time.sleep(7)
        #     minitor_stx.get_info_web()
        #     minitor_stx.get_info_excel1(5, "Sheet 1")
        # minitor_stx.check_info_web_excel(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.3 Quản lý thẻ")
        #
        # var_stx.driver.back()
        # time.sleep(5)


    def card_management_card_1time(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_card_management)
        except:
            contract_card.card_management(self, "", "", "")

        contract_card.card_management_x(self)

        var_stx.driver.find_element(By.XPATH, var_stx.PaidMethod_1time).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.3 Quản lý thẻ",
                                              var_stx.list_data2_13, "Dùng 1 lần", "_QuanLyThe_Dung1Lan.png")


    def card_management_addnew(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_card_management)
        except:
            contract_card.card_management(self, "", "", "")


        contract_card.partner_x(self)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.add_new1).click()
        except:
            var_stx.driver.refresh()
            time.sleep(7)
            var_stx.driver.find_element(By.XPATH, var_stx.add_new1).click()
        time.sleep(3)
        vehicle_driver_stx.increase()
        number = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 7, 2))


        var_stx.driver.find_element(By.XPATH, var_stx.info_card_serial).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_card_name).send_keys("Auto_" + number)
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_card_dat_ho).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_card_code_hd).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_card_day1).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_card_day2).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_card_serial).click()
        time.sleep(0.5)
        # var_stx.driver.find_element(By.XPATH, var_stx.info_card_pay).click()
        var_stx.driver.find_element(By.XPATH, var_stx.info_card_pay1).click()
        time.sleep(0.5)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.info_card_money1).send_keys("1.000.000")
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.info_card_money).send_keys("1.000.000")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_card_link_app).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_card_sdt).send_keys("0835210" + number)
        # var_stx.driver.find_element(By.XPATH, var_stx.info_card_sdt).send_keys("0902200780")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_card_rank_card).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_card_confirm).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_card_rank_note).send_keys("Trường test Tạo mới thẻ")
        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.save_1).click()
        time.sleep(1.5)
        module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 14, "Auto_" + number)
        var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 31, 2, "Auto_" + number)

        wait = WebDriverWait(var_stx.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx.card_management_addnew)))

        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.3 Quản lý thẻ",
                                                  var_stx.card_management_addnew, "Thêm mới thẻ thành công!", "_QuanLyThe_ThemMoi.png")


    def card_management_update(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_card_management)
        except:
            contract_card.card_management_addnew(self, "", "", "")


        vehicle_driver_stx.increase()
        number = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 7, 2))
        name = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 31, 2))

        contract_card.card_management_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.name_customer).send_keys(name)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(4)
        var_stx.driver.find_element(By.XPATH, var_stx.list_data2_2_button).click()
        time.sleep(2.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_card_sdt).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.info_card_sdt).send_keys("0995219" + number)
        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.save_1).click()
        time.sleep(1.5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.3 Quản lý thẻ",
                                                  var_stx.card_management_update, "Cập nhật thẻ thành công!", "_QuanLyThe_CapNhat.png")
        time.sleep(1.5)


    def card_management_see_file(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_card_management)
        except:
            contract_card.card_management_addnew(self, "", "", "")

        name = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 31, 2))

        contract_card.card_management_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.name_customer).send_keys(name)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(4)
        var_stx.driver.find_element(By.XPATH, var_stx.list_data2_7_button).click()
        time.sleep(2.5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.3 Quản lý thẻ",
                                                  var_stx.card_management_see_file, "MÃ QRCODE", "_QuanLyThe_XemQrCode.png")

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.qr_x).click()
            time.sleep(2)
        except:
            pass


    def card_management_clock(self, code, eventname, result, path_check, desire, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_card_management)
        except:
            contract_card.card_management_addnew(self, "", "", "")

        name = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 31, 2))

        contract_card.card_management_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.name_customer).send_keys(name)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(4)
        var_stx.driver.find_element(By.XPATH, var_stx.list_data2_15_button).click()
        time.sleep(2.5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.reason_clock).send_keys(var_stx.data['customer']['reason_lock'])
        except:
            pass
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.thuchien).click()
        time.sleep(1.5)

        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.3 Quản lý thẻ",
                                                  path_check, desire, name_image)


    def card_management_recharge(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_card_management)
        except:
            contract_card.card_management_addnew(self, "", "", "")

        name = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 31, 2))

        contract_card.card_management_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.name_customer).send_keys(name)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(4)
        var_stx.driver.find_element(By.XPATH, var_stx.list_data2_16_button).click()
        time.sleep(2.5)
        var_stx.driver.find_element(By.XPATH, var_stx.recharge_card_money).send_keys(var_stx.data['customer']['recharge_card_money'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.recharge_card_note).send_keys(var_stx.data['customer']['recharge_card_note'])
        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.card_management_recharge_save).click()
        time.sleep(2)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.3 Quản lý thẻ",
                                                  var_stx.card_management_recharge, "Thêm tiền vào thẻ thành công!", "_QuanLyThe_NapTien.png")


    def card_management_recharge_km(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_card_management)
        except:
            contract_card.card_management_addnew(self, "", "", "")

        name = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 31, 2))

        contract_card.card_management_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.name_customer).send_keys(name)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(4)
        var_stx.driver.find_element(By.XPATH, var_stx.list_data2_17_button).click()
        time.sleep(2.5)
        var_stx.driver.find_element(By.XPATH, var_stx.recharge_km_money).send_keys(var_stx.data['customer']['recharge_card_money'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.recharge_km_note).send_keys(var_stx.data['customer']['recharge_km_note'])
        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.card_management_recharge_km_save).click()
        time.sleep(1.5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.3 Quản lý thẻ",
                                                  var_stx.check_card_management_recharge_km, "Chỉnh sửa tiền khuyến mại thành công!", "_QuanLyThe_NapTienKm.png")


    def card_management_active(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_card_management)
        except:
            contract_card.card_management_addnew(self, "", "", "")

        name = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 31, 2))

        contract_card.card_management_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.name_customer).send_keys(name)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(4)
        var_stx.driver.find_element(By.XPATH, var_stx.list_data2_19_button).click()
        time.sleep(2.5)
        var_stx.driver.find_element(By.XPATH, var_stx.card_management_active).click()
        time.sleep(1.5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.3 Quản lý thẻ",
                                                  var_stx.check_card_management_active, "Kích hoạt thẻ thành công!", "_QuanLyThe_KichHoat.png")


    def card_management_cancel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_card_management)
        except:
            contract_card.card_management_addnew(self, "", "", "")

        name = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 31, 2))

        contract_card.card_management_x(self)
        var_stx.driver.find_element(By.XPATH, var_stx.name_customer).send_keys(name)
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(4)
        check_name = var_stx.driver.find_element(By.XPATH, var_stx.list_data2_6).text
        if check_name == name:
            var_stx.driver.find_element(By.XPATH, var_stx.list_data2_21_button).click()
            time.sleep(2.5)
            var_stx.driver.find_element(By.XPATH, var_stx.delete).click()
            time.sleep(1.5)
            module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.3 Quản lý thẻ",
                                                      var_stx.check_card_management_cancel, "Xóa thẻ thành công!", "_QuanLyThe_Xoa.png")











    def closing_debts(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.customer).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.contract_card).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.closing_debts).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.4 Chốt công nợ",
                                                  var_stx.title_page1, "7.7.4 Chốt công nợ", "_ChotCongNo.png")


    def closing_debts_x(self):
        var_stx.driver.implicitly_wait(0.2)
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.code_hd_sdt).clear()
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.from_day).clear()
            time.sleep(0.3)
            var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys("20/10/2024 00:00")
            time.sleep(0.3)
        except:
            pass
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.to_day).clear()
            time.sleep(0.3)
            var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys("20/12/2024 23:59")
            time.sleep(0.3)
        except:
            pass
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(3.5)


    def closing_debts_g7_test(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx_g7test(self, var_stx.data['login']['tk_admin_test'],  var_stx.data['login']['mk_admin_test'])
        var_stx.driver.find_element(By.XPATH, var_stx.customer).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.contract_card).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.closing_debts).click()
        time.sleep(5)


    def closing_debts_search(self, code, eventname, result, type_check, path_data, path_check, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_closing_debts)
        except:
            contract_card.closing_debts(self, "", "", "")

        contract_card.closing_debts_x(self)


        if type_check == "0":
            data = var_stx.driver.find_element(By.XPATH, path_data).text
            var_stx.driver.find_element(By.XPATH, var_stx.code_hd_sdt).send_keys(data)
            time.sleep(1)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(3.5)
            module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.4 Chốt công nợ",
                                                  path_check, data, name_image)

        if type_check == "1":
            module_other_stx.write_result_text_try_if_other(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.4 Chốt công nợ",
                                                  path_check, "", name_image)


    def closing_debts_reset(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_closing_debts)
        except:
            contract_card.closing_debts(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.closing_debts_reset).click()
        time.sleep(0.5)
        module_other_stx.write_result_displayed_try(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.4 Chốt công nợ",
                                              var_stx.closing_debts_reset, "_ChotCongNo_DatLai.png")


    def closing_debts_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_closing_debts)
        except:
            contract_card.closing_debts(self, "", "", "")

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_data2_2)
        except:
            contract_card.closing_debts_x(self)


        var_stx.driver.find_element(By.XPATH, var_stx.closing_debts_excel).click()
        time.sleep(5)
        # module_other_stx.write_result_dowload_file(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.4 Chốt công nợ",
        #                                                 "_ChotCongNo.xls", "_DanhSachKhachHang_XuatExcel.png")

        get_info_web()
        try:
            minitor_stx.get_info_excel1(5, "Sheet 1")
        except:
            var_stx.driver.refresh()
            time.sleep(7)
            var_stx.driver.find_element(By.XPATH, var_stx.closing_debts_excel).click()
            time.sleep(7)
            get_info_web()
            minitor_stx.get_info_excel1(5, "Sheet 1")
        minitor_stx.check_info_web_excel(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.4 Chốt công nợ")

        var_stx.driver.back()
        time.sleep(5)


    def closing_debts_link(self, code, eventname, result, button, path_check, desire, name_image):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_closing_debts)
        except:
            contract_card.closing_debts(self, "", "", "")

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_data2_2)
        except:
            contract_card.closing_debts_x(self)

        var_stx.driver.find_element(By.XPATH, button).click()
        time.sleep(4)
        var_stx.driver.switch_to.window(var_stx.driver.window_handles[1])
        time.sleep(2)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.4 Chốt công nợ",
                                              path_check, desire, name_image)

        module_other_stx.close_tab()
        var_stx.driver.switch_to.window(var_stx.driver.window_handles[0])
        time.sleep(1)


    def closing_debts_closing_debts(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_closing_debts)
        except:
            contract_card.closing_debts(self, "", "", "")

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.check_list_data2_2)
        except:
            contract_card.closing_debts_x(self)

        var_stx.driver.find_element(By.XPATH, var_stx.list_data2_1_input).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.closing_debts_closing_debts).click()
        time.sleep(2.5)

        var_stx.driver.find_element(By.XPATH, var_stx.closing_debts_day).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.closing_debts_note).click()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.closing_debts_note).send_keys(var_stx.data['customer']['closing_debts_note'])
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.closing_debts_mail).click()
        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.closing_debts_mail_input).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.closing_debts_mail_input).send_keys(var_stx.data['customer']['closing_debts_email'])
        time.sleep(0.5)
        module_other_stx.write_result_text_try_if_other(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.4 Chốt công nợ",
                                                  var_stx.check_closing_debts_closing_debts, "", "_ChotCongNo_ChotCongNo.png")


    def closing_debts_closing_debts_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(2)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")
        try:
            var_stx.driver.find_element(By.XPATH, var_stx.check_closing_debts_closing_debts)
        except:
            contract_card.closing_debts_closing_debts(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.export_excel3).click()
        time.sleep(5)
        module_other_stx.write_result_dowload_file(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.4 Chốt công nợ",
                                                        "ChotCongNo_ChotCongNo.xls", "_ChotCongNo_ChotCongNo_XuatExcel.png")


        try:
            name = var_stx.driver.find_element(By.XPATH, var_stx.not_role).text
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 14, name)
            var_stx.driver.back()
            time.sleep(5)
        except:
            pass


        try:
            var_stx.driver.find_element(By.XPATH, var_stx.close).click()
            time.sleep(2)
        except:
            pass










    def report_customer_card_details(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.customer).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.contract_card).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.report_customer_card_details).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.10 Báo cáo chi tiết cuốc khách thẻ",
                                                  var_stx.title_page1, "7.7.10 Báo cáo chi tiết cuốc khách thẻ", "_BaoCaoCHiTietCuocKhachNo.png")


    def report_customer_card_details_search(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_report_customer_card_details)
        except:
            contract_card.report_customer_card_details(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.reportrange).click()
        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.month_before).click()
        time.sleep(1.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(7)
        module_other_stx.write_result_text_try_if_other(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.10 Báo cáo chi tiết cuốc khách thẻ",
                                              var_stx.presentation1_2, "", "_BaoCaoCHiTietCuocKhachNo_TimKiem.png")


    def report_customer_card_details_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(2)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_report_customer_card_details)
        except:
            contract_card.report_customer_card_details_search(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.closing_debts_closing_debts_excel).click()
        time.sleep(7)
        try:
            # minitor_stx.get_info_web()
            # minitor_stx.get_info_excel1(5, "Sheet 1")
            # minitor_stx.check_info_web_excel(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.10 Báo cáo chi tiết cuốc khách thẻ")
            module_other_stx.write_result_dowload_file(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.10 Báo cáo chi tiết cuốc khách thẻ",
                                                            "_BaoCaoCHiTietCuocKhachNo_Excel.xlsx", "__BaoCaoCHiTietCuocKhachNo_XuatExcel.png")

        except:
            nodata = var_stx.driver.find_element(By.XPATH, var_stx.not_role).text
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, nodata)
            var_stx.driver.back()
            time.sleep(4)


    def report_customer_card_details_excel_full(self, code, eventname, result):
        var_stx.driver.implicitly_wait(2)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_report_customer_card_details)
        except:
            contract_card.report_customer_card_details_search(self, "", "", "")


        var_stx.driver.find_element(By.XPATH, var_stx.closing_debts_closing_debts_excel_full).click()
        time.sleep(7)
        try:
            nodata = var_stx.driver.find_element(By.XPATH, var_stx.not_role).text
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, nodata)
            var_stx.driver.back()
            time.sleep(4)
        except:
            module_other_stx.write_result_dowload_file(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.10 Báo cáo chi tiết cuốc khách thẻ",
                                                            "_BaoCaoCHiTietCuocKhachNo_ExcelFull.xlsx", "__BaoCaoCHiTietCuocKhachNo_XuatExcelDayDuThongTin.png")








    def report_card_top_up_transactions(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.customer).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.contract_card).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.report_card_top_up_transactions).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.11 Báo cáo giao dịch nạp thẻ",
                                                  var_stx.title_page1, "7.7.11 Báo cáo giao dịch nạp thẻ", "_BaoCaoGiaoDichNapThe.png")


    def report_card_top_up_transactions_search(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_report_card_top_up_transactions)
        except:
            contract_card.report_card_top_up_transactions(self, "", "", "")


        var_stx.driver.find_element(By.XPATH, var_stx.from_day).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys("12/12/2024 00:00")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys("20/12/2024 13:08")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if_other(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.11 Báo cáo giao dịch nạp thẻ",
                                              var_stx.list_data2_2, "", "_BaoCaoGiaoDichNapThe_TimKiem.png")


    def report_card_top_up_transactions_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(2)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_report_card_top_up_transactions)
        except:
            contract_card.report_card_top_up_transactions_search(self, "", "", "")


        var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        time.sleep(7)
        try:
            nodata = var_stx.driver.find_element(By.XPATH, var_stx.not_role).text
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 6, nodata)
            var_stx.driver.back()
            time.sleep(4)
        except:
            minitor_stx.get_info_web()
            minitor_stx.get_info_excel1(5, "Sheet 1")
            minitor_stx.check_info_web_excel(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.10 Báo cáo chi tiết cuốc khách thẻ")









    def report_the_trip_with_the_driver_card(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.customer).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.contract_card).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.report_the_trip_with_the_driver_card).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.12 Báo cáo cuốc đi thẻ theo lái xe",
                                                  var_stx.title_page1, "7.7.12 Báo cáo cuốc đi thẻ theo lái xe", "_BaoCaoCuocDiTheTheoLaiXe.png")


    def report_the_trip_with_the_driver_card_search(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_report_the_trip_with_the_driver_card)
        except:
            contract_card.report_the_trip_with_the_driver_card(self, "", "", "")


        var_stx.driver.find_element(By.XPATH, var_stx.from_day).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys("15/12/2024 00:00")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys("20/12/2024 23:59")
        time.sleep(0.5)

        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if_other(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.12 Báo cáo cuốc đi thẻ theo lái xe",
                                              var_stx.list_data2_2, "", "_BaoCaoCuocDiTheTheoLaiXe_TimKiem.png")


    def report_the_trip_with_the_driver_card_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(2)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_report_the_trip_with_the_driver_card)
        except:
            contract_card.report_the_trip_with_the_driver_card_search(self, "", "", "")


        var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        time.sleep(7)
        minitor_stx.get_info_web()
        try:
            minitor_stx.get_info_excel1(5, "Sheet 1")
        except:
            var_stx.driver.refresh()
            time.sleep(7)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(5)
            var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
            time.sleep(7)
            minitor_stx.get_info_web()
            minitor_stx.get_info_excel1(5, "Sheet 1")
        minitor_stx.check_info_web_excel(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.12 Báo cáo cuốc đi thẻ theo lái xe")










    def customer_summary_report(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.customer).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.contract_card).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.customer_summary_report).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.13 Báo cáo tổng hợp khách hàng",
                                                  var_stx.title_page1, "7.7.13 Báo cáo tổng hợp khách hàng", "_BaoCaoTongHopKhachHang.png")


    def customer_summary_report_search(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_customer_summary_report)
        except:
            contract_card.customer_summary_report(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.sdt).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.sdt).send_keys("0984")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if_other(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.13 Báo cáo tổng hợp khách hàng",
                                              var_stx.table_1_4, "", "_BaoCaoTongHopKhachHang_TimKiem.png")


    def customer_summary_report_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(2)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_customer_summary_report)
        except:
            contract_card.customer_summary_report_search(self, "", "", "")

        try:
            var_stx.driver.find_element(By.XPATH, var_stx.table_1_4)
        except:
            var_stx.driver.find_element(By.XPATH, var_stx.sdt).clear()
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.sdt).send_keys("0984")
            time.sleep(0.5)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(5)

        var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        time.sleep(7)
        promotion_stx.get_info_web1()
        try:
            minitor_stx.get_info_excel(5, "Sheet 1")
        except:
            var_stx.driver.refresh()
            time.sleep(7)
            var_stx.driver.find_element(By.XPATH, var_stx.search).click()
            time.sleep(5)
            var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
            time.sleep(7)
            promotion_stx.get_info_web1()
            minitor_stx.get_info_excel(5, "Sheet 1")
        minitor_stx.check_info_web_excel(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.13 Báo cáo tổng hợp khách hàng")









    def card_transaction_report(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        login_stx.login.login_stx(self, var_stx.data['login']['tk_admin_test'], var_stx.data['login']['mk_admin_test'])

        var_stx.driver.find_element(By.XPATH, var_stx.customer).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.contract_card).click()
        time.sleep(2)
        var_stx.driver.find_element(By.XPATH, var_stx.card_transaction_report).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.14 Báo cáo giao dịch thẻ",
                                                  var_stx.title_page1, "7.7.14 Báo cáo giao dịch thẻ", "_BaoCaoGiaoDichThe.png")


    def card_transaction_report_search(self, code, eventname, result):
        var_stx.driver.implicitly_wait(5)
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_card_transaction_report)
        except:
            contract_card.card_transaction_report(self, "", "", "")

        var_stx.driver.find_element(By.XPATH, var_stx.from_day).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.from_day).send_keys("20/12/2024 00:00")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).clear()
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.to_day).send_keys("20/12/2024 13:42")
        time.sleep(0.5)
        var_stx.driver.find_element(By.XPATH, var_stx.sdt).click()
        time.sleep(1)
        var_stx.driver.find_element(By.XPATH, var_stx.search).click()
        time.sleep(5)
        module_other_stx.write_result_text_try_if_other(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.14 Báo cáo giao dịch thẻ",
                                              var_stx.list_data2_7, "", "_BaoCaoGiaoDichThe_TimKiem.png")


    def card_transaction_report_excel(self, code, eventname, result):
        var_stx.driver.implicitly_wait(2)
        module_other_stx.delete_excel()
        minitor_stx.clearData_luutamthoi_checkexcel(var_stx.path_luutamthoi, "Sheet1", "", "", "", "", "", "")
        try:
            var_stx.driver.implicitly_wait(2)
            var_stx.driver.find_element(By.XPATH, var_stx.check_card_transaction_report)
        except:
            contract_card.card_transaction_report_search(self, "", "", "")


        var_stx.driver.find_element(By.XPATH, var_stx.export_excel2).click()
        time.sleep(7)
        try:
            minitor_stx.get_info_web()
            minitor_stx.get_info_excel1(5, "Sheet 1")
            minitor_stx.check_info_web_excel(code, eventname, result, "KHÁCH HÀNG - 7.7 Hợp đồng thẻ & thẻ - 7.7.14 Báo cáo giao dịch thẻ")
        except:
            logging.info("False")
            var_stx.driver.save_screenshot(var_stx.imagepath + code + "_KhachHang_BaoCaoGiaoDichThe.png")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx.writeData(var_stx.checklistpath, "Checklist", code, 13, code + "_KhachHang_BaoCaoGiaoDichThe.png")
            var_stx.driver.back()
            time.sleep(4)










