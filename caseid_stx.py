import login_stx
import module_other_stx
import var_stx
import openpyxl
from retry import retry
import minitor_stx
import vehicle_driver_stx
import driver_wallet_stx
import promotion_stx
import customer_stx
import report_stx
import administration
import accounting
#1









def get_datachecklist(ma):
    wordbook = openpyxl.load_workbook(var_stx.checklistpath)
    sheet = wordbook.get_sheet_by_name("Checklist")
    rownum = 9
    while (rownum < 3000):
        rownum += 1
        rownum = str(rownum)
        if sheet["A" + rownum].value == ma:
            tensukien = sheet["B" + rownum].value
            ketqua = sheet["E" + rownum].value
            print(tensukien)
            print(ketqua)
            var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 42, 2, tensukien)
            var_stx.writeData(var_stx.path_luutamthoi, "Sheet1", 43, 2, ketqua)
            return tensukien, ketqua
        rownum = int(rownum)







def caseid_login01(self):
    get_datachecklist("Login01")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    login_stx.login.login_stx1(self, "Login01", event, result, "https://app.g7taxi.vn/", var_stx.check_login_admin,
                               "Chào mừng đến với trang quản trị hệ thống Staxi", "Login_Admin.png",
                               var_stx.data['login']['tk_admin'], var_stx.data['login']['mk_admin'])


def caseid_login02(self):
    get_datachecklist("Login02")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    login_stx.login.login_stx1(self, "Login02", event, result, "https://app.staxi.vn/", var_stx.check_login,
                               "Xin chào: [9348] Taxi Nguyễn Gia [9348]", "Login_Admin.png",
                               var_stx.data['login']['tk_company'], var_stx.data['login']['mk_company'])

def caseid_login03(self):
    get_datachecklist("Login03")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    login_stx.login.login_stx1(self, "Login03", event, result, "https://app.staxi.vn/", var_stx.check_login,
                               "Xin chào: [1996] Test 12/10 [1996]", "Login_Admin.png",
                               var_stx.data['login']['tk_test'], var_stx.data['login']['mk_test'])

def caseid_login04(self):
    pass


def caseid_login05(self):
    pass


def caseid_login06(self):
    get_datachecklist("Login06")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    login_stx.link.affiliate(self, "Login06", event, result, var_stx.link1, var_stx.check_link1,
                             "THIẾT BỊ GIÁM SÁT HÀNH TRÌNH", "DangNhap_LienKet_ThongTinGiaiPhap.png", "0")

def caseid_login07(self):
    get_datachecklist("Login07")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    login_stx.link.affiliate(self, "Login07", event, result, var_stx.link2, var_stx.check_link2,
                             "HƯỚNG DẪN SỬ DỤNG", "DangNhap_LienKet_hdsd.png", "0")


def caseid_login08(self):
    get_datachecklist("Login08")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    login_stx.link.affiliate(self, "Login08", event, result, var_stx.link3, "",
                             "Tin tức - BA GPS", "DangNhap_LienKet_TinTucNghanhGTVT.png", "1")


def caseid_login09(self):
    get_datachecklist("Login09")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    login_stx.link.affiliate(self, "Login09", event, result, var_stx.link4, "",
                             "Về chúng tôi - BA GPS", "DangNhap_LienKet_VeChungToi.png", "1")

def caseid_login10(self):
    get_datachecklist("Login10")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    login_stx.link.affiliate(self, "Login10", event, result, var_stx.ch_play, var_stx.check_ch_play,
                             "G7 Taxi", "DangNhap_LienKet_ChPlay.png", "0")

def caseid_login11(self):
    get_datachecklist("Login11")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    login_stx.link.affiliate(self, "Login11", event, result, var_stx.app_store, var_stx.check_app_store,
                             "G7 Taxi", "DangNhap_LienKet_Store.png", "0")

def caseid_login12(self):
    get_datachecklist("Login12")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    login_stx.link.affiliate(self, "Login12", event, result, var_stx.link5, "",
                             "GIÁM SÁT HÀNH TRÌNH SỐ 1 VIỆT NAM - BA GPS", "DangNhap_LienKet_bagps.png", "1")





def caseid_minitor01(self):
    get_datachecklist("Minitor01")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.vehicle_online.vehicle_online(self, "Minitor01", event, result)



# def caseid_minitor02(self):
#     get_datachecklist("Minitor02")
#     event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
#     result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
#     minitor_stx.vehicle_online.search_vehicle(self, "Minitor02", event, result, "0", var_stx.list_data2, var_stx.search_vehicle_input,
#                                               var_stx.check_list_data2, "", "GiamSat_TimKiem_BienSo.png")


def caseid_minitor02(self):
    get_datachecklist("Minitor02")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.vehicle_online.search_vehicle(self, "Minitor02", event, result, "0", var_stx.list_data2, var_stx.vehicle_input1,
                                              var_stx.check_list_data2, "", "GiamSat_TimKiem_BienSo.png")



def caseid_minitor03(self):
    pass



# def caseid_minitor03(self):
#     get_datachecklist("Minitor03")
#     event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
#     result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
#     minitor_stx.vehicle_online.search_vehicle(self, "Minitor03", event, result, "0", var_stx.list_data3, var_stx.search_vehicle_input,
#                                               var_stx.check_list_data3, "", "GiamSat_TimKiem_MaDam.png")


def caseid_minitor04(self):
    get_datachecklist("Minitor04")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.vehicle_online.search_vehicle(self, "Minitor04", event, result, "1", var_stx.check_list_data3_5, var_stx.search_driver_input,
                                              var_stx.check_list_data2_5, "", "GiamSat_TimKiem_LaiXe.png")


def caseid_minitor05(self):
    get_datachecklist("Minitor05")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.vehicle_online.search_vehicle(self, "Minitor05", event, result, "6", "", var_stx.search_into_recently_input,
                                              var_stx.check_list_data2_7, "", "GiamSat_TimKiem_VaoCaGanDay.png")

def caseid_minitor06(self):
    get_datachecklist("Minitor06")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.vehicle_online.search_vehicle(self, "Minitor06", event, result, "2", "", var_stx.search_lost_signal_input,
                                              var_stx.check_list_data2_8, "", "GiamSat_TimKiem_MatKetNoiGanDay.png")


def caseid_minitor07(self):
    get_datachecklist("Minitor07")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.vehicle_online.search_vehicle(self, "Minitor07", event, result, "3", "", var_stx.search_status_online,
                                              var_stx.check_list_data2_10, "", "GiamSat_TimKiem_TrangThaiOnline.png")


def caseid_minitor08(self):
    get_datachecklist("Minitor08")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.vehicle_online.search_vehicle(self, "Minitor08", event, result, "4", "", var_stx.search_status_online2,
                                              var_stx.check_list_data2_10, "Mở", "GiamSat_TimKiem_DangVaoCaVaKetNoiTot.png")


def caseid_minitor09(self):
    get_datachecklist("Minitor09")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.vehicle_online.search_vehicle(self, "Minitor09", event, result, "4", "", var_stx.search_status_online3,
                                              var_stx.check_list_data2_10, "Đóng", "GiamSat_TimKiem_DangVaoCaVaMatKetNoi.png")

def caseid_minitor10(self):
    get_datachecklist("Minitor10")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.vehicle_online.search_vehicle(self, "Minitor10", event, result, "5", "", var_stx.search_status_online4,
                                              var_stx.check_list_data11, "", "GiamSat_TimKiem_ChuaVaoCa.png")


def caseid_minitor11(self):
    get_datachecklist("Minitor11")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.vehicle_online.search_vehicle(self, "Minitor11", event, result, "3", "", var_stx.search_status_online5,
                                              var_stx.check_list_data2_6, "", "GiamSat_TimKiem_DangVaoCa.png")


def caseid_minitor12(self):
    get_datachecklist("Minitor12")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.vehicle_online.search_vehicle(self, "Minitor12", event, result, "3", "", var_stx.search_status_blackbox,
                                              var_stx.check_list_data2_2, "", "GiamSat_TimKiem_TrangThaiHopDen.png")

def caseid_minitor13(self):
    get_datachecklist("Minitor13")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.vehicle_online.search_vehicle(self, "Minitor13", event, result, "4", "", var_stx.search_status_blackbox2,
                                              var_stx.check_list_data2_11, "Không khách", "GiamSat_TimKiem_KetNoiKhongKhach.png")


def caseid_minitor14(self):
    get_datachecklist("Minitor14")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.vehicle_online.search_vehicle(self, "Minitor14", event, result, "7", "", var_stx.search_status_blackbox3,
                                              var_stx.check_list_data2_11, "Có khách", "GiamSat_TimKiem_KetNoiCoKhach.png")


def caseid_minitor15(self):
    get_datachecklist("Minitor15")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.vehicle_online.search_vehicle(self, "Minitor15", event, result, "7", "", var_stx.search_status_blackbox4,
                                              var_stx.check_list_data2_11, "Mất kết nối", "GiamSat_TimKiem_MatKetNoi.png")


def caseid_minitor16(self):
    get_datachecklist("Minitor16")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.vehicle_online.vehicle_online_excel(self, "Minitor16", event, result)


def caseid_minitor17(self):
    get_datachecklist("Minitor17")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.vehicle_online.vehicle_online_logout_all(self, "Minitor17", event, result, var_stx.vehicle_into_ca_input,
                                                         "0", "GiamSat_LogoutTatCa_XeVaoCa.png")

def caseid_minitor18(self):
    get_datachecklist("Minitor18")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.vehicle_online.vehicle_online_logout_all(self, "Minitor18", event, result, var_stx.vehicle_into_ca_good_connect_input,
                                                         "0", "GiamSat_LogoutTatCa_XeVaoCaKetNoiTot.png")

def caseid_minitor19(self):
    get_datachecklist("Minitor19")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.vehicle_online.vehicle_online_logout_all(self, "Minitor19", event, result, var_stx.vehicle_into_ca_lost_connect_input,
                                                         "0", "GiamSat_LogoutTatCa_XeVaoCaMatKetNoi.png")

def caseid_minitor20(self):
    get_datachecklist("Minitor20")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.vehicle_online.vehicle_online_logout_all(self, "Minitor20", event, result, var_stx.dowload_file_txt_input,
                                                         "1", "GiamSat_LogoutTatCa_TaiXuongTuFileTXT.png")

def caseid_minitor21(self):
    get_datachecklist("Minitor21")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.vehicle_online.vehicle_online_logout_driver(self, "Minitor21", event, result)


def caseid_minitor22(self):
    get_datachecklist("Minitor22")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.minitor_vehicle(self, "Minitor22", event, result)


def caseid_minitor23(self):
    get_datachecklist("Minitor23")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.minitor_vehicle_icon_search(self, "Minitor23", event, result)


def caseid_minitor24(self):
    get_datachecklist("Minitor24")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.minitor_vehicle_icon(self, "Minitor24", event, result, var_stx.icon_config_type_vehicle,
                                                            var_stx.save1, var_stx.save_success, "Lưu thành công!", "_GiamSatXe_CauHinhIconLoaiXe.png", "0")


def caseid_minitor25(self):
    get_datachecklist("Minitor25")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.minitor_vehicle_icon(self, "Minitor25", event, result, var_stx.icon_config,
                                                            var_stx.config_save, var_stx.title_config, "Cập nhật cấu hình khởi động", "_GiamSatXe_CauHinh.png", "1")


def caseid_minitor26(self):
    get_datachecklist("Minitor26")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.minitor_vehicle_icon(self, "Minitor26", event, result, var_stx.icon_help,
                                                            "", var_stx.help, "Trợ Giúp", "_GiamSatXe_TroGiup.png", "2")


def caseid_minitor27(self):
    get_datachecklist("Minitor27")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.minitor_vehicle_satus(self, "Minitor27", event, result, var_stx.minitor_vehicle_status1,
                                                            "0", "", "/Content/themes/img/RedCar.png", "_GiamSatXe_TrangThaiSanSang_.png", -30, "1")

def caseid_minitor28(self):
    get_datachecklist("Minitor28")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.minitor_vehicle_satus(self, "Minitor28", event, result, var_stx.minitor_vehicle_status2,
                                                            "0", "", "/Content/themes/img/BlueCar.png", "_GiamSatXe_TrangThaiSanSang_.png", -31, "2")

def caseid_minitor29(self):
    get_datachecklist("Minitor29")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.minitor_vehicle_satus(self, "Minitor29", event, result, var_stx.minitor_vehicle_status3,
                                                            "0", "", "/Content/themes/img/GreenCar.png", "_GiamSatXe_TrangThaiSanSang_.png", -32,"3")

def caseid_minitor30(self):
    get_datachecklist("Minitor30")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.minitor_vehicle_satus(self, "Minitor30", event, result, var_stx.minitor_vehicle_status8,
                                                            "0", "", "/Content/themes/img/RedCar.png", "_GiamSatXe_TrangThaiDangKD_.png", -30, "1")

def caseid_minitor31(self):
    get_datachecklist("Minitor31")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.minitor_vehicle_satus(self, "Minitor31", event, result, var_stx.minitor_vehicle_status4,
                                                            "2", var_stx.check_minitor_vehicle_status4, "", "_GiamSatXe_TrangThaiRoiCa_.png", "", "")

def caseid_minitor32(self):
    get_datachecklist("Minitor32")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.minitor_vehicle_satus(self, "Minitor32", event, result, var_stx.minitor_vehicle_status5,
                                                            "0", "", "/Content/themes/img/WarGreenCar.png", "_GiamSatXe_TrangThaiMTD_.png", -35, "5")


def caseid_minitor33(self):
    get_datachecklist("Minitor33")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.minitor_vehicle_satus(self, "Minitor33", event, result, var_stx.minitor_vehicle_status6,
                                                            "0", "", "/Content/themes/img/RedCar.png", "_GiamSatXe_TrangThaiKetNoiMo_.png", -30, "1")



def caseid_minitor34(self):
    get_datachecklist("Minitor34")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.minitor_vehicle_satus(self, "Minitor34", event, result, var_stx.minitor_vehicle_status0,
                                                            "3", var_stx.check_minitor_vehicle_status4, "", "_GiamSatXe_TrangThaiTatCa_.png", "", "")

def caseid_minitor35(self):
    get_datachecklist("Minitor35")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.minitor_vehicle_minitor_search(self, "Minitor35", event, result)


def caseid_minitor36(self):
    get_datachecklist("Minitor36")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.minitor_vehicle_route_search(self, "Minitor36", event, result)


@retry(tries=3, delay=2, backoff=1, jitter=5, )
def caseid_minitor37(self):
    get_datachecklist("Minitor37")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.info_vehicle(self, "Minitor37", event, result)


def caseid_minitor38(self):
    get_datachecklist("Minitor38")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.check_info_none(self, "Minitor38", event, result, 8)


def caseid_minitor39(self):
    get_datachecklist("Minitor39")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.check_info_popup_list(self, "Minitor39", event, result, 9)


def caseid_minitor40(self):
    get_datachecklist("Minitor40")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.check_info_none(self, "Minitor40", event, result, 11)


def caseid_minitor41(self):
    get_datachecklist("Minitor41")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.check_info_none(self, "Minitor41", event, result, 12)


def caseid_minitor42(self):
    get_datachecklist("Minitor42")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.check_info_none(self, "Minitor42", event, result, 10)


def caseid_minitor43(self):
    get_datachecklist("Minitor43")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.check_info_popup_list(self, "Minitor43", event, result, 13)


def caseid_minitor44(self):
    get_datachecklist("Minitor44")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.check_info_popup_list(self, "Minitor44", event, result, 14)


def caseid_minitor45(self):
    get_datachecklist("Minitor45")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.check_info_none(self, "Minitor45", event, result, 15)


def caseid_minitor46(self):
    get_datachecklist("Minitor46")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.check_info_popup_list(self, "Minitor46", event, result, 16)


def caseid_minitor47(self):
    get_datachecklist("Minitor47")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.check_info_none(self, "Minitor47", event, result, 17)


def caseid_minitor48(self):
    get_datachecklist("Minitor48")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.check_info_none(self, "Minitor48", event, result, 18)


def caseid_minitor49(self):
    get_datachecklist("Minitor49")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.check_info_none(self, "Minitor49", event, result, 19)


def caseid_minitor50(self):
    get_datachecklist("Minitor50")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.check_info_none(self, "Minitor50", event, result, 20)


def caseid_minitor51(self):
    get_datachecklist("Minitor51")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.check_info_none(self, "Minitor51", event, result, 21)


def caseid_minitor52(self):
    get_datachecklist("Minitor52")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.check_info_none(self, "Minitor52", event, result, 22)



def caseid_minitor53(self):
    get_datachecklist("Minitor53")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.route.dowload_route(self, "Minitor53", event, result)


def caseid_minitor54(self):
    get_datachecklist("Minitor54")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.route.route_icon(self, "Minitor54", event, result, var_stx.icon_stop, "GiamSat_LoTrinh_IconDung.png")


def caseid_minitor55(self):
    get_datachecklist("Minitor55")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.route.route_icon(self, "Minitor55", event, result, var_stx.icon_run, "GiamSat_LoTrinh_IconChay.png")


def caseid_minitor56(self):
    get_datachecklist("Minitor56")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.route.route_icon(self, "Minitor56", event, result, var_stx.icon_slow_speed, "GiamSat_LoTrinh_IconGiamToc.png")

def caseid_minitor57(self):
    get_datachecklist("Minitor57")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.route.route_icon(self, "Minitor57", event, result, var_stx.icon_hight_speed, "GiamSat_LoTrinh_IconTangToc.png")

def caseid_minitor58(self):
    get_datachecklist("Minitor58")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.route.route_icon(self, "Minitor58", event, result, var_stx.icon_max_speed, "GiamSat_LoTrinh_IconTocDoToiDa.png")


def caseid_minitor59(self):
    get_datachecklist("Minitor59")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.route.route_icon(self, "Minitor59", event, result, var_stx.icon_max_route, "GiamSat_LoTrinh_IconChayHetLoTrinh.png")


def caseid_minitor60(self):
    get_datachecklist("Minitor60")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.route.route_print(self, "Minitor60", event, result)


def caseid_minitor61(self):
    get_datachecklist("Minitor61")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.route.route_excel(self, "Minitor61", event, result)


def caseid_minitor62(self):
    get_datachecklist("Minitor62")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.route.route_help(self, "Minitor62", event, result)


def caseid_minitor63(self):
    get_datachecklist("Minitor63")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.minitor_vehicle_group(self, "Minitor63", event, result)


def caseid_minitor64(self):
    get_datachecklist("Minitor64")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.minitor_vehicle_group_icon_config(self, "Minitor64", event, result)


def caseid_minitor65(self):
    get_datachecklist("Minitor65")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.minitor_vehicle_group_icon_help(self, "Minitor65", event, result)


def caseid_minitor66(self):
    get_datachecklist("Minitor66")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.minitor_vehicle_group_status(self, "Minitor66", event, result)

def caseid_minitor67(self):
    get_datachecklist("Minitor67")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.minitor_vehicle_group_group(self, "Minitor67", event, result)


def caseid_minitor68(self):
    get_datachecklist("Minitor68")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.minitor_vehicle_group_search(self, "Minitor68", event, result)


def caseid_minitor69(self):
    get_datachecklist("Minitor69")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.check_info_group_none(self, "Minitor69", event, result,
                                                      var_stx.minitor_info_group_vehicle, "_GiamSatXeNhom_HienTrang_BienSo.png")

def caseid_minitor70(self):
    get_datachecklist("Minitor70")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.check_info_group_none(self, "Minitor70", event, result,
                                                      var_stx.minitor_info_group_codedam, "_GiamSatXeNhom_HienTrang_MaDam.png")


def caseid_minitor71(self):
    get_datachecklist("Minitor71")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.check_info_group_none(self, "Minitor71", event, result,
                                                      var_stx.minitor_info_group_time, "_GiamSatXeNhom_HienTrang_ThoiGian.png")

def caseid_minitor72(self):
    get_datachecklist("Minitor72")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.check_info_group_none(self, "Minitor72", event, result,
                                                      var_stx.minitor_info_group_latitude, "_GiamSatXeNhom_HienTrang_ViDo.png")

def caseid_minitor73(self):
    get_datachecklist("Minitor73")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.check_info_group_none(self, "Minitor73", event, result,
                                                      var_stx.minitor_info_group_longitude, "_GiamSatXeNhom_HienTrang_KinhDo.png")

def caseid_minitor74(self):
    get_datachecklist("Minitor74")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.check_info_group_none(self, "Minitor74", event, result,
                                                      var_stx.minitor_info_group_location, "_GiamSatXeNhom_HienTrang_ViTri.png")

def caseid_minitor75(self):
    get_datachecklist("Minitor75")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.check_info_group_none(self, "Minitor75", event, result,
                                                      var_stx.minitor_info_group_vgps, "_GiamSatXeNhom_HienTrang_VanTocGPS.png")

def caseid_minitor76(self):
    get_datachecklist("Minitor76")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.check_info_group_none(self, "Minitor76", event, result,
                                                      var_stx.minitor_info_group_driver, "_GiamSatXeNhom_HienTrang_TaiXe.png")

def caseid_minitor77(self):
    get_datachecklist("Minitor77")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.check_info_group_none(self, "Minitor77", event, result,
                                                      var_stx.minitor_info_group_phone, "_GiamSatXeNhom_HienTrang_DienThoai.png")

def caseid_minitor78(self):
    get_datachecklist("Minitor78")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.check_info_group_none(self, "Minitor78", event, result,
                                                      var_stx.minitor_info_group_typevehicle, "_GiamSatXeNhom_HienTrang_LoaiXe.png")

def caseid_minitor79(self):
    get_datachecklist("Minitor79")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.check_info_group_none(self, "Minitor79", event, result,
                                                      var_stx.minitor_info_group_trip, "_GiamSatXeNhom_HienTrang_CuocKhach.png")

def caseid_minitor80(self):
    get_datachecklist("Minitor80")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_stx.minitor_vehicle.check_info_group_none(self, "Minitor80", event, result,
                                                      var_stx.minitor_info_group_version, "_GiamSatXeNhom_HienTrang_PhienBan.png")


def caseid_vehicle01(self):
    get_datachecklist("Vehicle01")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.vehicle(self, "Vehicle01", event, result)


def caseid_vehicle02(self):
    pass
    # get_datachecklist("Vehicle02")
    # event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    # result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    # vehicle_driver_stx.vehicle.search_vehicle_from_to_day(self, "Vehicle02", event, result,
    #                                                       var_stx.listdata1_2, "", "_Xe_TuNgayDenNgay.png")



def caseid_vehicle03(self):
    get_datachecklist("Vehicle03")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.search_vehicle(self, "Vehicle03", event, result, "0", var_stx.listdata2_2, var_stx.vehicle_input1,
                                                           var_stx.listdata1_2, "_Xe_BienSo.png")

def caseid_vehicle04(self):
    get_datachecklist("Vehicle04")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.search_vehicle(self, "Vehicle04", event, result, "0", var_stx.listdata2_3, var_stx.number,
                                                           var_stx.listdata1_3, "_Xe_SoHieu.png")

def caseid_vehicle05(self):
    get_datachecklist("Vehicle05")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.search_vehicle(self, "Vehicle05", event, result, "1", var_stx.listdata2_3, var_stx.drivering,
                                                           var_stx.listdata1_6, "_Xe_DangLai.png")

def caseid_vehicle06(self):
    get_datachecklist("Vehicle06")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.search_vehicle_combobox(self, "Vehicle06", event, result, var_stx.state_1, "2", var_stx.listdata1_2,
                                                       "", "_Xe_TrangThai.png")

def caseid_vehicle07(self):
    get_datachecklist("Vehicle07")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.search_vehicle_combobox(self, "Vehicle07", event, result, var_stx.state_2, "4", var_stx.listdata1_7,
                                                       "Kết nối tốt", "_Xe_TrangThai_KetNoiTot.png")

def caseid_vehicle08(self):
    get_datachecklist("Vehicle08")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.search_vehicle_combobox(self, "Vehicle08", event, result, var_stx.state_3, "1", var_stx.listdata1_7,
                                                       "Mất kết nối", "_Xe_TrangThai_MatKetNoi.png")


def caseid_vehicle09(self):
    get_datachecklist("Vehicle09")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.search_vehicle_combobox(self, "Vehicle09", event, result, var_stx.state_4, "4", var_stx.listdata1_7,
                                                       "", "_Xe_TrangThai_KhongKetNoi.png")



def caseid_vehicle10(self):
    get_datachecklist("Vehicle10")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.search_vehicle_combobox(self, "Vehicle10", event, result, var_stx.state_lock_1, "2", var_stx.listdata1_12,
                                                       "", "_Xe_Khoa.png")

def caseid_vehicle11(self):
    get_datachecklist("Vehicle11")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.search_vehicle_combobox(self, "Vehicle11", event, result, var_stx.state_lock_2, "1", var_stx.listdata1_13,
                                                       "Mở khóa", "_Xe_Khoa_Khoa.png")

def caseid_vehicle12(self):
    get_datachecklist("Vehicle12")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.search_vehicle_combobox(self, "Vehicle12", event, result, var_stx.state_lock_3, "1", var_stx.listdata1_13,
                                                       "", "_Xe_Khoa_MoKhoa.png")


def caseid_vehicle13(self):
    get_datachecklist("Vehicle13")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.search_vehicle_combobox(self, "Vehicle13", event, result, var_stx.vehicle_type_1, "2", var_stx.listdata1_4,
                                                       "", "_Xe_Khoa_LoaiXe.png")


def caseid_vehicle14(self):
    get_datachecklist("Vehicle14")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.search_vehicle_type_vehicle(self, "Vehicle14", event, result)


# def caseid_vehicle14(self):
#     get_datachecklist("Vehicle14")
#     event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
#     result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
#     vehicle_driver_stx.vehicle.search_vehicle_combobox(self, "Vehicle14", event, result, var_stx.vehicle_type_3, "2", var_stx.listdata1_4,
#                                                        "", "_Xe_Khoa_LoaiXe_Chon1.png")

def caseid_vehicle15(self):
    pass
    # get_datachecklist("Vehicle15")
    # event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    # result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    # vehicle_driver_stx.vehicle.search_vehicle_combobox(self, "Vehicle15", event, result, var_stx.vehicle_type_3, "3", var_stx.listdata1_4,
    #                                                    "", "_Xe_Khoa_LoaiXe_TatCa.png")

def caseid_vehicle16(self):
    get_datachecklist("Vehicle16")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.search_vehicle_excel(self, "Vehicle16", event, result)


def caseid_vehicle17(self):
    get_datachecklist("Vehicle17")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.vehicle_dowload_file(self, "Vehicle17", event, result)


def caseid_vehicle18(self):
    get_datachecklist("Vehicle18")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.vehicle_import_file(self, "Vehicle18", event, result)


def caseid_vehicle19(self):
    get_datachecklist("Vehicle19")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.vehicle_addnew(self, "Vehicle19", event, result)


def caseid_vehicle20(self):
    get_datachecklist("Vehicle20")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.vehicle_checkbox(self, "Vehicle20", event, result, var_stx.black_box_input, False,
                                                var_stx.check_black_box1, "Hủy kết nối hộp đen thành công", "_Xe_HopDen_BoTichChon.png")

def caseid_vehicle21(self):
    get_datachecklist("Vehicle21")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.vehicle_checkbox(self, "Vehicle21", event, result, var_stx.black_box_input, False,
                                                var_stx.check_black_box2, "Kết nối hộp đen thành công", "_Xe_HopDen_TichChon.png")


def caseid_vehicle22(self):
    get_datachecklist("Vehicle22")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.vehicle_checkbox(self, "Vehicle22", event, result, var_stx.clock_input, False,
                                                var_stx.check_clock1, "Cập nhật trạng thái kết nối đồng hồ thành công", "_Xe_DongHo_TichChon.png")


def caseid_vehicle23(self):
    get_datachecklist("Vehicle23")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.vehicle_checkbox(self, "Vehicle23", event, result, var_stx.clock_input, False,
                                                var_stx.check_clock1, "Cập nhật trạng thái kết nối đồng hồ thành công", "_Xe_DongHo_BoTichChon.png")


def caseid_vehicle24(self):
    get_datachecklist("Vehicle24")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.vehicle_checkbox(self, "Vehicle24", event, result, var_stx.cam_ai_input, False,
                                                var_stx.check_cam_ai, "Thành công", "_Xe_CamAi_TichChon.png")

def caseid_vehicle25(self):
    get_datachecklist("Vehicle25")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.vehicle_checkbox(self, "Vehicle25", event, result, var_stx.cam_ai_input, False,
                                                var_stx.check_cam_ai, "Thành công", "_Xe_CamAi_BoTichChon.png")

def caseid_vehicle26(self):
    get_datachecklist("Vehicle26")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.vehicle_clock(self, "Vehicle26", event, result, var_stx.listdata1_12, "0",
                                                var_stx.check_clock_vehicle1, "Khóa xe thành công.", "_Xe_KhoaXe.png")


def caseid_vehicle27(self):
    get_datachecklist("Vehicle27")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.vehicle_clock(self, "Vehicle27", event, result, var_stx.listdata1_13, "1",
                                                var_stx.check_clock_vehicle2, "Mở khóa xe thành công.", "_Xe_MoKhoaXe.png")


def caseid_vehicle28(self):
    get_datachecklist("Vehicle28")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.vehicle_update(self, "Vehicle28", event, result)


def caseid_vehicle29(self):
    get_datachecklist("Vehicle29")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.vehicle_delete(self, "Vehicle29", event, result)


def caseid_vehicle30(self):
    get_datachecklist("Vehicle30")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.vehicle.vehicle_hide_column(self, "Vehicle30", event, result)


def caseid_vehicle31(self):
    get_datachecklist("Vehicle31")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.driver(self, "Vehicle31", event, result)


def caseid_vehicle32(self):
    get_datachecklist("Vehicle32")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.search_driver_from_to_day(self, "Vehicle32", event, result)

def caseid_vehicle33(self):
    get_datachecklist("Vehicle33")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.search_driver(self, "Vehicle33", event, result, var_stx.listdata2_2, var_stx.search_driver_input,
                                            var_stx.listdata1_2, "_XeLaiXe_TimKiem_LaiXe.png")

def caseid_vehicle34(self):
    get_datachecklist("Vehicle34")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.search_driver(self, "Vehicle34", event, result, var_stx.LatestVehiclePlate2, var_stx.liscense_plate,
                                            var_stx.LatestVehiclePlate1, "_XeLaiXe_TimKiem_BienSo.png")

def caseid_vehicle35(self):
    get_datachecklist("Vehicle35")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.search_driver(self, "Vehicle35", event, result, var_stx.listdata2_4, var_stx.number,
                                            var_stx.listdata1_4, "_XeLaiXe_TimKiem_SoHieu.png")

def caseid_vehicle36(self):
    get_datachecklist("Vehicle36")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.search_driver(self, "Vehicle36", event, result, var_stx.listdata2_8, var_stx.cccd,
                                            var_stx.listdata1_8, "_XeLaiXe_TimKiem_CCCD.png")

def caseid_vehicle37(self):
    get_datachecklist("Vehicle37")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.search_driver(self, "Vehicle37", event, result, var_stx.PhoneNumber2, var_stx.sdt_account,
                                            var_stx.PhoneNumber1, "_XeLaiXe_TimKiem_SoDienThoai.png")

def caseid_vehicle38(self):
    get_datachecklist("Vehicle38")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.search_driver_assign(self, "Vehicle38", event, result)

def caseid_vehicle39(self):
    get_datachecklist("Vehicle39")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.search_driver_combobox(self, "Vehicle39", event, result, var_stx.state_lock, "0", var_stx.listdata1_11,
                                                     "", "_XeLaiXe_LyDoMoKhoa.png")

def caseid_vehicle40(self):
    get_datachecklist("Vehicle40")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.search_driver_combobox(self, "Vehicle40", event, result, var_stx.state_lock, "1", var_stx.listdata1_10,
                                                     "Mở khóa", "_XeLaiXe_TrangThai_Khoa.png")

def caseid_vehicle41(self):
    get_datachecklist("Vehicle41")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.search_driver_combobox(self, "Vehicle41", event, result, var_stx.state_unlock, "1", var_stx.listdata1_9,
                                                     "Khóa", "_XeLaiXe_TrangThai_MoKhoa.png")


def caseid_vehicle42(self):
    get_datachecklist("Vehicle42")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.driver_excel(self, "Vehicle42", event, result)


def caseid_vehicle43(self):
    get_datachecklist("Vehicle43")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.driver_dowload_file(self, "Vehicle43", event, result)


def caseid_vehicle44(self):
    get_datachecklist("Vehicle44")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.driver_import_file(self, "Vehicle44", event, result)


def caseid_vehicle45(self):
    get_datachecklist("Vehicle45")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.driver_add_new(self, "Vehicle45", event, result)


def caseid_vehicle46(self):
    get_datachecklist("Vehicle46")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.driver_add_stk(self, "Vehicle46", event, result)


def caseid_vehicle47(self):
    get_datachecklist("Vehicle47")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.driver_update(self, "Vehicle47", event, result)


def caseid_vehicle48(self):
    get_datachecklist("Vehicle48")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.driver_clock(self, "Vehicle48", event, result, "Khóa", "0",
                                                var_stx.check_clock_driver1, "Khóa lái xe thành công.", "_LaiXe_KhoaLaiXe.png")


def caseid_vehicle49(self):
    get_datachecklist("Vehicle49")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.driver_detail(self, "Vehicle49", event, result)


def caseid_vehicle50(self):
    get_datachecklist("Vehicle50")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.driver_clock(self, "Vehicle50", event, result, "Mở khóa", "1",
                                                var_stx.check_clock_driver2, "Mở khóa lái xe thành công.", "_LaiXe_MoKhoaLaiXe.png")




def caseid_vehicle51(self):
    get_datachecklist("Vehicle51")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.driver_reward(self, "Vehicle51", event, result)


def caseid_vehicle52(self):
    get_datachecklist("Vehicle52")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.driver_assign(self, "Vehicle52", event, result)


def caseid_vehicle53(self):
    get_datachecklist("Vehicle53")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.driver_get_code_active(self, "Vehicle53", event, result)


def caseid_vehicle54(self):
    get_datachecklist("Vehicle54")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.driver_change_password(self, "Vehicle54", event, result)

def caseid_vehicle55(self):
    get_datachecklist("Vehicle55")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.driver_detail_device(self, "Vehicle55", event, result)


def caseid_vehicle56(self):
    get_datachecklist("Vehicle56")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.driver_info_driver(self, "Vehicle56", event, result)

def caseid_vehicle57(self):
    get_datachecklist("Vehicle57")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.driver_info_driver_sync(self, "Vehicle57", event, result)


def caseid_vehicle58(self):
    get_datachecklist("Vehicle58")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.driver_delete(self, "Vehicle58", event, result)


def caseid_vehicle59(self):
    get_datachecklist("Vehicle59")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.driver_hide_column(self, "Vehicle59", event, result)


def caseid_vehicle60(self):
    get_datachecklist("Vehicle60")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle_driver_stx.driver.driver_sd_lot(self, "Vehicle60", event, result)


def caseid_wallet01(self):
    get_datachecklist("Wallet01")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.list_wallet_driver.list_wallet_driver(self, "Wallet01", event, result)


def caseid_wallet02(self):
    get_datachecklist("Wallet02")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.list_wallet_driver.list_wallet_driver_toolbar(self, "Wallet02", event, result)


def caseid_wallet03(self):
    get_datachecklist("Wallet03")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.list_wallet_driver.list_wallet_driver_search(self, "Wallet03", event, result, var_stx.name_drive, var_stx.col_id_FullName1,
                                                                   var_stx.col_id_FullName0, "_DanhSachViLaiXe_TenLaiXe.png")

def caseid_wallet04(self):
    get_datachecklist("Wallet04")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.list_wallet_driver.list_wallet_driver_search(self, "Wallet04", event, result, var_stx.account, var_stx.col_id_DriverCode1,
                                                                   var_stx.col_id_DriverCode0, "_DanhSachViLaiXe_TaiKhoan.png")

def caseid_wallet05(self):
    get_datachecklist("Wallet05")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.list_wallet_driver.list_wallet_driver_search(self, "Wallet05", event, result, var_stx.number, var_stx.col_id_PrivateCode1,
                                                                   var_stx.col_id_PrivateCode0, "_DanhSachViLaiXe_SoHieu.png")

def caseid_wallet06(self):
    get_datachecklist("Wallet06")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.list_wallet_driver.list_wallet_driver_excel(self, "Wallet06", event, result)


def caseid_wallet07(self):
    get_datachecklist("Wallet07")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.list_wallet_driver.list_wallet_driver_recharge(self, "Wallet07", event, result)


def caseid_wallet08(self):
    get_datachecklist("Wallet08")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.list_wallet_driver.list_wallet_driver_withdraw(self, "Wallet08", event, result)


def caseid_wallet09(self):
    get_datachecklist("Wallet09")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.list_wallet_driver.list_wallet_driver_hisory(self, "Wallet09", event, result)


def caseid_wallet10(self):
    get_datachecklist("Wallet10")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.recharge.pay_money_into_the_driver_wallet(self, "Wallet10", event, result)


def caseid_wallet11(self):
    get_datachecklist("Wallet11")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.recharge.pay_money_into_the_driver_wallet_fill(self, "Wallet11", event, result)


def caseid_wallet12(self):
    get_datachecklist("Wallet12")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.withdraw.withdraw_money_from_driver_wallet(self, "Wallet12", event, result)

def caseid_wallet13(self):
    get_datachecklist("Wallet13")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.withdraw.withdraw_money_from_driver_wallet_fill(self, "Wallet13", event, result)


def caseid_wallet14(self):
    get_datachecklist("Wallet14")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.transaction_confirmation.transaction_confirmation(self, "Wallet14", event, result)

def caseid_wallet15(self):
    get_datachecklist("Wallet15")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.transaction_confirmation.transaction_confirmation_from_to_day(self, "Wallet15", event, result)


def caseid_wallet16(self):
    pass
    # get_datachecklist("Wallet16")
    # event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    # result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    # driver_wallet_stx.transaction_confirmation.transaction_confirmation_search(self, "Wallet16", event, result, var_stx.list_data3_3, "0",
    #                                                                            var_stx.list_data2_3, "_XacNhanGiaoDich_TenTaiKhoanLaiXe.png")

def caseid_wallet17(self):
    get_datachecklist("Wallet17")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.transaction_confirmation.transaction_confirmation_search(self, "Wallet17", event, result, var_stx.ag2_5, "0",
                                                                               var_stx.ag1_5, "_XacNhanGiaoDich_TenLaiXe.png")

def caseid_wallet18(self):
    get_datachecklist("Wallet18")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.transaction_confirmation.transaction_confirmation_search(self, "Wallet18", event, result, var_stx.ag2_6, "0",
                                                                               var_stx.ag1_6, "_XacNhanGiaoDich_SDT.png")

def caseid_wallet19(self):
    get_datachecklist("Wallet19")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.transaction_confirmation.transaction_confirmation_excel(self, "Wallet19", event, result)


def caseid_wallet20(self):
    get_datachecklist("Wallet20")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.transaction_confirmation.transaction_confirmation_pay(self, "Wallet20", event, result)


def caseid_wallet21(self):
    get_datachecklist("Wallet21")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.transaction_confirmation.transaction_confirmation_history_pay(self, "Wallet21", event, result)


def caseid_wallet22(self):
    get_datachecklist("Wallet22")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.transaction_confirmation.transaction_confirmation_igree(self, "Wallet22", event, result, var_stx.agree_to_confirm,
                                                                              "Xác nhận thành công.", "_XacNhanGiaoDich_DongYXacNhan.png")

def caseid_wallet23(self):
    get_datachecklist("Wallet23")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.transaction_confirmation.transaction_confirmation_igree(self, "Wallet23", event, result, var_stx.cancel_gd,
                                                                              "Hủy giao dịch thành công.", "_XacNhanGiaoDich_HuyGiaoDich.png")

def caseid_wallet24(self):
    get_datachecklist("Wallet24")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.wallet_history.wallet_history(self, "Wallet24", event, result)


def caseid_wallet25(self):
    pass
    # get_datachecklist("Wallet25")
    # event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    # result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    # driver_wallet_stx.wallet_history.wallet_history_from_to_day(self, "Wallet25", event, result)


def caseid_wallet26(self):
    get_datachecklist("Wallet26")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.wallet_history.wallet_history_search(self, "Wallet26", event, result, var_stx.ag2_9, var_stx.driver_sdt,
                                                           var_stx.ag1_9, "_LichSuViTien_TenLaiXe.png")

def caseid_wallet27(self):
    pass
    # get_datachecklist("Wallet27")
    # event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    # result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    # driver_wallet_stx.wallet_history.wallet_history_search(self, "Wallet27", event, result, var_stx.list_data3_3, var_stx.driver_sdt,
    #                                                        var_stx.list_data2_3, "_LichSuViTien_SoDienThoai.png")

def caseid_wallet28(self):
    get_datachecklist("Wallet28")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.wallet_history.wallet_history_search(self, "Wallet28", event, result, var_stx.ag2_7, var_stx.code_hieu,
                                                           var_stx.ag1_7, "_LichSuViTien_MaDam.png")


def caseid_wallet29(self):
    get_datachecklist("Wallet29")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.wallet_history.wallet_history_search_scroll(self, "Wallet29", event, result, var_stx.ag2_8, var_stx.code_gd,
                                                           var_stx.ag1_8, "_LichSuViTien_MaGiaoDich.png")


def caseid_wallet30(self):
    get_datachecklist("Wallet30")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.wallet_history.wallet_history_bombobox(self, "Wallet30", event, result, var_stx.walletkind,
                                                             var_stx.ag1_11, "Ví tài khoản", "_LichSuViTien_ViTaiKhoan.png")


def caseid_wallet31(self):
    get_datachecklist("Wallet31")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.wallet_history.wallet_history_bombobox(self, "Wallet31", event, result, var_stx.cash_wallet,
                                                             var_stx.ag1_11, "Ví tiền mặt", "_LichSuViTien_ViTienMat.png")

def caseid_wallet32(self):
    get_datachecklist("Wallet32")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.wallet_history.wallet_history_bombobox(self, "Wallet32", event, result, var_stx.recharge1,
                                                             var_stx.ag1_10, "Nạp tiền", "_LichSuViTien_NapTien.png")

def caseid_wallet33(self):
    get_datachecklist("Wallet33")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.wallet_history.wallet_history_bombobox(self, "Wallet33", event, result, var_stx.withdraw_money,
                                                             var_stx.ag1_10, "Rút tiền", "_LichSuViTien_RútTien.png")

def caseid_wallet34(self):
    pass
    # get_datachecklist("Wallet34")
    # event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    # result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    # driver_wallet_stx.wallet_history.wallet_history_bombobox(self, "Wallet34", event, result, var_stx.transfer_money,
                                                            # var_stx.list_data2_5, "Chuyển tiền", "_LichSuViTien_ChuyenTien.png")


def caseid_wallet35(self):
    get_datachecklist("Wallet35")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.wallet_history.wallet_history_bombobox(self, "Wallet35", event, result, var_stx.status_0,
                                                             var_stx.ag1_3, "Chưa xác nhận", "_LichSuViTien_ChuaXacNhan.png")

def caseid_wallet36(self):
    get_datachecklist("Wallet36")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.wallet_history.wallet_history_bombobox(self, "Wallet36", event, result, var_stx.status_1,
                                                             var_stx.ag1_3, "Đã xác nhận", "_LichSuViTien_DaXacNhan.png")

def caseid_wallet37(self):
    get_datachecklist("Wallet37")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.wallet_history.wallet_history_bombobox(self, "Wallet37", event, result, var_stx.status_2,
                                                             var_stx.ag1_3, "Hủy giao dịch", "_LichSuViTien_HuyGiaoDich.png")


def caseid_wallet38(self):
    get_datachecklist("Wallet38")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.wallet_history.wallet_history_detail(self, "Wallet38", event, result)


def caseid_wallet39(self):
    get_datachecklist("Wallet39")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.wallet_history.wallet_history_excel(self, "Wallet39", event, result)


def caseid_wallet40(self):
    get_datachecklist("Wallet40")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    driver_wallet_stx.wallet_history.wallet_history_print(self, "Wallet40", event, result)









def caseid_promotion01(self):
    get_datachecklist("Promotion01")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.list_promotion.list_promotion(self, "Promotion01", event, result)


def caseid_promotion02(self):
    pass
    # get_datachecklist("Promotion02")
    # event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    # result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    # promotion_stx.list_promotion.list_promotion_from_to_day(self, "Promotion02", event, result)


def caseid_promotion03(self):
    get_datachecklist("Promotion03")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.list_promotion.list_promotion_search(self, "Promotion03", event, result)


def caseid_promotion04(self):
    get_datachecklist("Promotion04")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.list_promotion.list_promotion_add_new(self, "Promotion04", event, result, "Khuyến mại chung",
                                                                "_DanhSachKhuyenmai_ThemMoi_KhuyenMaiChung.png")

def caseid_promotion05(self):
    get_datachecklist("Promotion05")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.list_promotion.list_promotion_add_new(self, "Promotion05", event, result, "Khuyến mại riêng",
                                                                "_DanhSachKhuyenmai_ThemMoi_KhuyenMaiRieng.png")


def caseid_promotion05_1(self):
    get_datachecklist("Promotion05_1")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.list_promotion.list_promotion_check_info(self, "Promotion05_1", event, result)


def caseid_promotion06(self):
    get_datachecklist("Promotion06")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.list_promotion.list_promotion_update(self, "Promotion06", event, result)


def caseid_promotion07(self):
    get_datachecklist("Promotion07")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.list_promotion.list_promotion_create_code(self, "Promotion07", event, result)


def caseid_promotion08(self):
    get_datachecklist("Promotion08")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.list_promotion.list_promotion_active(self, "Promotion08", event, result,"_DanhSachKhuyenmai_DangKichHoat.png")


def caseid_promotion09(self):
    get_datachecklist("Promotion09")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.list_promotion.list_promotion_active(self, "Promotion09", event, result, "_DanhSachKhuyenmai_DaSuDung.png")


def caseid_promotion10(self):
    get_datachecklist("Promotion10")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.list_promotion.list_promotion_icon(self, "Promotion10", event, result, var_stx.row_index0_icon_see, var_stx.check_list_promotion1,
                                                     "DANH SÁCH MÃ KHUYẾN MẠI", "_DanhSachKhuyenmai_XemMa.png")


def caseid_promotion11(self):
    get_datachecklist("Promotion11")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.list_promotion.wallet_history_excel(self, "Promotion11", event, result)


def caseid_promotion12(self):
    get_datachecklist("Promotion12")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.list_promotion.list_promotion_icon(self, "Promotion12", event, result, var_stx.row_index0_icon_report, var_stx.check_icon_report,
                                                     "6.4.7 BC KM theo cuốc khách", "_DanhSachKhuyenmai_BaoCao.png")


def caseid_promotion13(self):
    get_datachecklist("Promotion13")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.list_promotion.list_promotion_icon(self, "Promotion13", event, result, var_stx.row_index0_icon_coppy, var_stx.check_icon_coppy,
                                                     "THÊM MỚI KHUYẾN MẠI", "_DanhSachKhuyenmai_SaoChep.png")


def caseid_promotion14(self):
    get_datachecklist("Promotion14")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.list_promotion.list_promotion_delete(self, "Promotion14", event, result)


def caseid_promotion15(self):
    get_datachecklist("Promotion15")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.introduce_list_account.introduce_list_account(self, "Promotion15", event, result)


def caseid_promotion16(self):
    get_datachecklist("Promotion16")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.introduce_list_account.introduce_list_account_from_to_day(self, "Promotion16", event, result)


def caseid_promotion17(self):
    get_datachecklist("Promotion17")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.introduce_list_account.introduce_list_account_search(self, "Promotion17", event, result, var_stx.account, var_stx.table_2_2,
                                                                       var_stx.table_1_2, "_DanhSachTaiKhoanGioiThieu_TaiKhoan.png")

def caseid_promotion18(self):
    get_datachecklist("Promotion18")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.introduce_list_account.introduce_list_account_search(self, "Promotion18", event, result, var_stx.my_introduce_code, var_stx.table_2_3,
                                                                       var_stx.table_1_3, "_DanhSachTaiKhoanGioiThieu_MaGioiThieuCuaToi.png")

def caseid_promotion19(self):
    get_datachecklist("Promotion19")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.introduce_list_account.introduce_list_account_search(self, "Promotion19", event, result, var_stx.person_code_introduce, var_stx.table_2_4,
                                                                       var_stx.table_1_4, "_DanhSachTaiKhoanGioiThieu_MaNguoiGioiThieu.png")

def caseid_promotion20(self):
    get_datachecklist("Promotion20")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.introduce_list_account.introduce_list_account_combobox(self, "Promotion20", event, result, var_stx.type_account_introduce_combobox,
                                                                         var_stx.type_account_introduce_combobox1, var_stx.table_1_5,
                                                                         "_DanhSachTaiKhoanGioiThieu_LoaiTaiKhoanGioiThieu.png")


def caseid_promotion21(self):
    get_datachecklist("Promotion21")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.introduce_list_account.introduce_list_account_combobox(self, "Promotion21", event, result, var_stx.group_account_combobox,
                                                                         var_stx.group_account_combobox1, var_stx.table_1_6,
                                                                         "_DanhSachTaiKhoanGioiThieu_NhomTaiKhoan.png")

def caseid_promotion22(self):
    get_datachecklist("Promotion22")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.introduce_list_account.introduce_list_account_addnew(self, "Promotion22", event, result, "Đã kích hoạt")


def caseid_promotion23(self):
    get_datachecklist("Promotion23")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.introduce_list_account.introduce_list_account_addnew(self, "Promotion23", event, result, "Chưa kích hoạt")


def caseid_promotion24(self):
    get_datachecklist("Promotion24")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.introduce_list_account.introduce_list_account_update(self, "Promotion24", event, result)


def caseid_promotion25(self):
    get_datachecklist("Promotion25")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.introduce_list_account.introduce_list_account_delete(self, "Promotion25", event, result)


def caseid_promotion26(self):
    get_datachecklist("Promotion26")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.install_new_app.install_new_app(self, "Promotion26", event, result)


def caseid_promotion27(self):
    get_datachecklist("Promotion27")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.install_new_app.install_new_app_search(self, "Promotion27", event, result)


def caseid_promotion28(self):
    get_datachecklist("Promotion28")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.install_new_app.install_new_app_addnew(self, "Promotion28", event, result)


def caseid_promotion29(self):
    get_datachecklist("Promotion29")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.install_new_app.install_new_app_update(self, "Promotion29", event, result)


def caseid_promotion30(self):
    get_datachecklist("Promotion30")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.install_new_app.install_new_app_active(self, "Promotion30", event, result, var_stx.active,
                                                         "_CaiAppMoi_KichHoat.png")

def caseid_promotion31(self):
    get_datachecklist("Promotion31")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.install_new_app.install_new_app_active(self, "Promotion31", event, result, var_stx.stop_active,
                                                         "_CaiAppMoi_NgungKichHoat.png")

def caseid_promotion32(self):
    get_datachecklist("Promotion32")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.report.summary_report_on_promotions_by_company(self, "Promotion32", event, result)


def caseid_promotion33(self):
    get_datachecklist("Promotion33")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.report.summary_report_on_promotions_by_company_search(self, "Promotion33", event, result)


def caseid_promotion34(self):
    get_datachecklist("Promotion34")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.report.summary_report_on_promotions_by_company_excel(self, "Promotion34", event, result)



def caseid_promotion35(self):
    get_datachecklist("Promotion35")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.report.detailed_km_reports_by_company(self, "Promotion35", event, result)


def caseid_promotion36(self):
    get_datachecklist("Promotion36")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.report.detailed_km_reports_by_company_search(self, "Promotion36", event, result)


def caseid_promotion37(self):
    get_datachecklist("Promotion37")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.report.detailed_km_reports_by_company_excel(self, "Promotion37", event, result)



def caseid_promotion38(self):
    get_datachecklist("Promotion38")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.report.reports_km_by_day(self, "Promotion38", event, result)


def caseid_promotion39(self):
    get_datachecklist("Promotion39")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.report.reports_km_by_day_search(self, "Promotion39", event, result)


def caseid_promotion40(self):
    get_datachecklist("Promotion40")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.report.reports_km_by_day_excel(self, "Promotion40", event, result)


def caseid_promotion41(self):
    get_datachecklist("Promotion41")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.report.reports_km_by_month(self, "Promotion41", event, result)


def caseid_promotion42(self):
    get_datachecklist("Promotion42")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.report.reports_km_by_month_search(self, "Promotion42", event, result)


def caseid_promotion43(self):
    get_datachecklist("Promotion43")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.report.reports_km_by_month_excel(self, "Promotion43", event, result)



def caseid_promotion44(self):
    get_datachecklist("Promotion44")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.report.reports_km_by_kh(self, "Promotion44", event, result)


def caseid_promotion45(self):
    get_datachecklist("Promotion45")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.report.reports_km_by_kh_search(self, "Promotion45", event, result)


def caseid_promotion46(self):
    get_datachecklist("Promotion46")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.report.reports_km_by_kh_excel(self, "Promotion46", event, result)




def caseid_promotion47(self):
    get_datachecklist("Promotion47")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.report.reports_km_by_lx(self, "Promotion47", event, result)


def caseid_promotion48(self):
    get_datachecklist("Promotion48")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.report.reports_km_by_lx_search(self, "Promotion48", event, result)


def caseid_promotion49(self):
    get_datachecklist("Promotion49")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.report.reports_km_by_lx_excel(self, "Promotion49", event, result)



def caseid_promotion50(self):
    get_datachecklist("Promotion50")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.report.reports_km_by_customer(self, "Promotion50", event, result)


def caseid_promotion51(self):
    get_datachecklist("Promotion51")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.report.reports_km_by_customer_search(self, "Promotion51", event, result)


def caseid_promotion52(self):
    get_datachecklist("Promotion52")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.report.reports_km_by_customer_excel(self, "Promotion52", event, result)


def caseid_promotion53(self):
    get_datachecklist("Promotion53")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.report.reports_km_not_use(self, "Promotion53", event, result)


def caseid_promotion54(self):
    get_datachecklist("Promotion54")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.report.reports_km_not_use_search(self, "Promotion54", event, result)


def caseid_promotion55(self):
    get_datachecklist("Promotion55")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.report.reports_km_not_use_excel(self, "Promotion55", event, result)


def caseid_promotion56(self):
    get_datachecklist("Promotion56")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.report.referral_account_summary_report(self, "Promotion56", event, result)


def caseid_promotion57(self):
    get_datachecklist("Promotion57")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.report.referral_account_summary_report_search(self, "Promotion57", event, result)


def caseid_promotion58(self):
    get_datachecklist("Promotion58")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.report.referral_account_summary_report_excel(self, "Promotion58", event, result)


def caseid_promotion59(self):
    get_datachecklist("Promotion59")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.list_account_introduce.list_account_introduce(self, "Promotion59", event, result)


def caseid_promotion60(self):
    get_datachecklist("Promotion60")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.list_account_introduce.list_account_introduce_search(self, "Promotion60", event, result)


def caseid_promotion61(self):
    get_datachecklist("Promotion61")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.list_account_introduce.list_account_introduce_addnew(self, "Promotion61", event, result)


def caseid_promotion62(self):
    get_datachecklist("Promotion62")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.list_account_introduce.list_account_introduce_delete(self, "Promotion62", event, result)


def caseid_promotion63(self):
    get_datachecklist("Promotion63")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.list_group_account_introduce.list_group_account_introduce(self, "Promotion63", event, result)


def caseid_promotion64(self):
    get_datachecklist("Promotion64")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.list_group_account_introduce.list_group_account_introduce_search(self, "Promotion64", event, result)


def caseid_promotion65(self):
    get_datachecklist("Promotion65")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.list_group_account_introduce.list_group_account_introduce_addnew(self, "Promotion65", event, result)


def caseid_promotion66(self):
    get_datachecklist("Promotion66")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    promotion_stx.list_group_account_introduce.list_group_account_introduce_delete(self, "Promotion66", event, result)


def caseid_customer01(self):
    get_datachecklist("Customer01")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.list_customer.list_customer(self, "Customer01", event, result)


def caseid_customer02(self):
    pass
    # get_datachecklist("Customer02")
    # event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    # result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    # customer_stx.list_customer.list_customer_from_to_day(self, "Customer02", event, result)


def caseid_customer03(self):
    get_datachecklist("Customer03")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.list_customer.list_customer_search(self, "Customer03", event, result, var_stx.list_data3_3,
                                                    var_stx.list_data2_3, "_DanhSachKhachHang_TenHienThi.png")

def caseid_customer04(self):
    get_datachecklist("Customer04")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.list_customer.list_customer_search(self, "Customer04", event, result, var_stx.list_data3_2,
                                                    var_stx.list_data2_2, "_DanhSachKhachHang_TenDangNhap.png")

def caseid_customer05(self):
    get_datachecklist("Customer05")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.list_customer.list_customer_search(self, "Customer05", event, result, var_stx.list_data3_6,
                                                    var_stx.list_data2_6, "_DanhSachKhachHang_Email.png")


def caseid_customer06(self):
    get_datachecklist("Customer06")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.list_customer.list_customer_group(self, "Customer06", event, result)


def caseid_customer07(self):
    get_datachecklist("Customer07")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.list_customer.list_customer_rank(self, "Customer07", event, result)

def caseid_customer08(self):
    get_datachecklist("Customer08")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.list_customer.list_customer_excel(self, "Customer08", event, result)


def caseid_customer09(self):
    get_datachecklist("Customer09")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.list_customer.list_customer_addnew(self, "Customer09", event, result)

def caseid_customer10(self):
    get_datachecklist("Customer10")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.list_customer.list_customer_lock(self, "Customer10", event, result, "Khóa tài khoản thành công.",
                                                  "_DanhSachKhachHang_Khoa.png")

def caseid_customer11(self):
    get_datachecklist("Customer11")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.list_customer.list_customer_lock(self, "Customer11", event, result, "Mở khóa tài khoản thành công.",
                                                  "_DanhSachKhachHang_MoKhoa.png")

def caseid_customer12(self):
    get_datachecklist("Customer12")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.list_customer.list_customer_get_code(self, "Customer12", event, result)


def caseid_customer13(self):
    get_datachecklist("Customer13")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.list_customer.list_customer_assign_group(self, "Customer13", event, result)


def caseid_customer14(self):
    get_datachecklist("Customer14")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.list_customer.list_customer_detail_device(self, "Customer14", event, result)


def caseid_customer15(self):
    get_datachecklist("Customer15")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.list_customer.list_customer_detail_icon(self, "Customer15", event, result, var_stx.list_data2_16_button,
                                                         "BÁO CÁO CHI TIẾT DOANH THU THEO KHÁCH HÀNG", "_DanhSachKhachHang_TienQuoc.png")

def caseid_customer16(self):
    get_datachecklist("Customer16")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.list_customer.list_customer_detail_icon(self, "Customer16", event, result, var_stx.list_data2_17_button,
                                                         "DANH SÁCH CUỐC KHÁCH HÀNG ĐẶT", "_DanhSachKhachHang_ChiTietQuoc.png")

def caseid_customer17(self):
    get_datachecklist("Customer17")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.list_customer.list_customer_detail_icon(self, "Customer17", event, result, var_stx.list_data2_18_button,
                                                         "LỊCH SỬ KHÓA TÀI KHOẢN", "_DanhSachKhachHang_LichSuKhoa.png")

def caseid_customer17_1(self):
    get_datachecklist("Customer17_1")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.list_customer.list_customer_detail_delete(self, "Customer17_1", event, result)


def caseid_customer18(self):
    get_datachecklist("Customer18")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.partner(self, "Customer18", event, result)


def caseid_customer19(self):
    get_datachecklist("Customer19")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.partner_search(self, "Customer19", event, result, var_stx.partner_name, var_stx.list_data3_3,
                                              var_stx.list_data2_3, "_Doitac_TenDoiTac.png")

def caseid_customer20(self):
    get_datachecklist("Customer20")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.partner_search(self, "Customer20", event, result, var_stx.sdt, var_stx.list_data3_4,
                                              var_stx.list_data2_4, "_Doitac_SoDienthoai.png")

def caseid_customer21(self):
    get_datachecklist("Customer21")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.partner_search(self, "Customer21", event, result, var_stx.code_partner, var_stx.list_data3_2,
                                              var_stx.list_data2_2, "_Doitac_MaDoiTac.png")

# def caseid_customer21(self):
#     get_datachecklist("Customer21")
#     event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
#     result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
#     customer_stx.contract_card.partner_combobox(self, "Customer21", event, result)


def caseid_customer22(self):
    get_datachecklist("Customer22")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.partner_addnew(self, "Customer22", event, result)


def caseid_customer23(self):
    get_datachecklist("Customer23")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.partner_update(self, "Customer23", event, result)


def caseid_customer24(self):
    get_datachecklist("Customer24")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.partner_delete(self, "Customer24", event, result)


def caseid_customer25(self):
    get_datachecklist("Customer25")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.contract(self, "Customer25", event, result)

def caseid_customer26(self):
    get_datachecklist("Customer26")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.contract_search(self, "Customer26", event, result, var_stx.list_data3_2, var_stx.code_contract,
                                               var_stx.list_data2_2, "_HopDong_MaHopDong.png")

def caseid_customer26_1(self):
    get_datachecklist("Customer26_1")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.contract_search(self, "Customer26_1", event, result, var_stx.list_data3_5, var_stx.code_partner,
                                               var_stx.list_data2_5, "_HopDong_MaDoiTac.png")

def caseid_customer26_2(self):
    get_datachecklist("Customer26_2")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.contract_search(self, "Customer26_2", event, result, var_stx.list_data3_6, var_stx.partner_name,
                                               var_stx.list_data2_6, "_HopDong_TenDoiTac.png")



def caseid_customer27(self):
    get_datachecklist("Customer27")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.contract_combobox(self, "Customer27", event, result)


def caseid_customer28(self):
    get_datachecklist("Customer28")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.contract_addnew(self, "Customer28", event, result)


def caseid_customer29(self):
    get_datachecklist("Customer29")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.contract_update(self, "Customer29", event, result)


def caseid_customer30(self):
    get_datachecklist("Customer30")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.contract_see_file(self, "Customer30", event, result)


def caseid_customer31(self):
    get_datachecklist("Customer31")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.contract_delete(self, "Customer31", event, result)


def caseid_customer32(self):
    get_datachecklist("Customer32")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_management(self, "Customer32", event, result)


def caseid_customer33(self):
    get_datachecklist("Customer33")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_management_search(self, "Customer33", event, result, var_stx.number_serial, var_stx.col_id_serial3,
                                                      var_stx.col_id_serial2, "_QuanLyThe_SoSerial.png")

def caseid_customer34(self):
    get_datachecklist("Customer34")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_management_search(self, "Customer34", event, result, var_stx.sdt, var_stx.col_id_mobile3,
                                                      var_stx.col_id_mobile2, "_QuanLyThe_SoDienThoai.png")

def caseid_customer35(self):
    get_datachecklist("Customer35")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_management_search(self, "Customer35", event, result, var_stx.code_hd, var_stx.col_id_hd3,
                                                      var_stx.col_id_hd2, "_QuanLyThe_MaHopDong.png")

def caseid_customer36(self):
    get_datachecklist("Customer36")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_management_search(self, "Customer36", event, result, var_stx.name_customer, var_stx.col_id_namecustomer3,
                                                      var_stx.col_id_namecustomer2, "_QuanLyThe_TenKhachHang.png")

def caseid_customer37(self):
    get_datachecklist("Customer37")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_management_company(self, "Customer37", event, result)


def caseid_customer38(self):
    pass


def caseid_customer39(self):
    pass


def caseid_customer40(self):
    get_datachecklist("Customer40")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_management_status(self, "Customer40", event, result, var_stx.Status_not_active,
                                                      var_stx.col_id_status2, "Kích hoạt", "_QuanLyThe_KhongKichHoat.png")

def caseid_customer41(self):
    get_datachecklist("Customer41")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_management_status(self, "Customer41", event, result, var_stx.Status_active,
                                                      var_stx.col_id_status2, "Thẻ đã kích hoạt", "_QuanLyThe_KichHoat.png")

def caseid_customer42(self):
    get_datachecklist("Customer42")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_management_card(self, "Customer42", event, result, var_stx.PaidMethod_before,
                                                      var_stx.col_id_type2, "Trả trước", "_QuanLyThe_TraTruoc.png")

def caseid_customer43(self):
    get_datachecklist("Customer43")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_management_card(self, "Customer43", event, result, var_stx.PaidMethod_after,
                                                      var_stx.col_id_type2, "Trả sau", "_QuanLyThe_TraSau.png")


def caseid_customer44(self):
    get_datachecklist("Customer44")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_management_status(self, "Customer44", event, result, var_stx.StatusBFA2,
                                                      var_stx.col_id_BookForAnother2,  "Đã kích hoạt", "_QuanLyThe_TrangThaiDatHo_KichHoat.png")

def caseid_customer45(self):
    get_datachecklist("Customer45")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_management_status(self, "Customer45", event, result, var_stx.StatusBFA3,
                                                      var_stx.col_id_BookForAnother2,  "Chưa kích hoạt", "_QuanLyThe_TrangThaiDatHo_ChuaKichHoat.png")


def caseid_customer46(self):
    get_datachecklist("Customer46")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_management_qr(self, "Customer46", event, result)


def caseid_customer47(self):
    get_datachecklist("Customer47")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_management_excel(self, "Customer47", event, result)


def caseid_customer48(self):
    get_datachecklist("Customer48")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_management_card_1time(self, "Customer48", event, result)


def caseid_customer49(self):
    get_datachecklist("Customer49")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_management_addnew(self, "Customer49", event, result)


def caseid_customer50(self):
    get_datachecklist("Customer50")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_management_update(self, "Customer50", event, result)


def caseid_customer51(self):
    get_datachecklist("Customer51")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_management_see_file(self, "Customer51", event, result)


def caseid_customer52(self):
    get_datachecklist("Customer52")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_management_clock(self, "Customer52", event, result, var_stx.toast_message,
                                                     "Khóa thẻ thành công!", "Khóa thẻ thành công!", "_QuanLyThe_KhoaThe.png")

def caseid_customer53(self):
    get_datachecklist("Customer53")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_management_clock(self, "Customer53", event, result, var_stx.toast_message,
                                                     "Mở khóa thẻ thành công!", "Mở thẻ thành công!", "_QuanLyThe_MoThe.png")

def caseid_customer54(self):
    get_datachecklist("Customer54")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_management_recharge(self, "Customer54", event, result)


def caseid_customer55(self):
    get_datachecklist("Customer55")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_management_recharge_km(self, "Customer55", event, result)


def caseid_customer56(self):
    get_datachecklist("Customer56")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_management_active(self, "Customer56", event, result)


def caseid_customer57(self):
    get_datachecklist("Customer57")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_management_cancel(self, "Customer57", event, result)


def caseid_customer57_1(self):
    get_datachecklist("Customer57_1")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.issue_white_cards(self, "Customer57_1", event, result)

def caseid_customer57_2(self):
    get_datachecklist("Customer57_2")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.one_time_card(self, "Customer57_2", event, result)


def caseid_customer57_3(self):
    get_datachecklist("Customer57_3")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.one_time_card_coppy(self, "Customer57_3", event, result)

def caseid_customer57_4(self):
    get_datachecklist("Customer57_4")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.one_time_card_print(self, "Customer57_4", event, result)


def caseid_customer57_5(self):
    get_datachecklist("Customer57_5")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.one_time_card_save(self, "Customer57_5", event, result)



def caseid_customer58(self):
    get_datachecklist("Customer58")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.closing_debts(self, "Customer58", event, result)


def caseid_customer59(self):
    get_datachecklist("Customer59")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.closing_debts_search(self, "Customer59", event, result, "0", var_stx.ag2_3,
                                                    var_stx.ag1_3, "_ChotCongNo_MaHopDong.png")


def caseid_customer60(self):
    get_datachecklist("Customer60")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.closing_debts_search(self, "Customer60", event, result, "0", var_stx.col_id_mobile3,
                                                    var_stx.col_id_mobile2, "_ChotCongNo_SoDienThoai.png")

def caseid_customer61(self):
    get_datachecklist("Customer61")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.closing_debts_search(self, "Customer61", event, result, "1", "",
                                                    var_stx.ag1_3, "_ChotCongNo_TuNgayDenNgay.png")

def caseid_customer62(self):
    get_datachecklist("Customer62")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.closing_debts_reset(self, "Customer62", event, result)


def caseid_customer63(self):
    get_datachecklist("Customer63")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.closing_debts_excel(self, "Customer63", event, result)


def caseid_customer64(self):
    get_datachecklist("Customer64")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.closing_debts_link(self, "Customer64", event, result, var_stx.closing_debts_list_debts_icon,
                                                  var_stx.check_closing_debts_list_debts, "DANH SÁCH CÔNG NỢ ĐÃ CHỐT",
                                                  "_ChotCongNo_DanhSachCongNoDaChot.png")

def caseid_customer65(self):
    get_datachecklist("Customer65")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.closing_debts_link(self, "Customer65", event, result, var_stx.ag1_i,
                                                  var_stx.check_page3, "7.7.10 Báo cáo chi tiết cuốc khách thẻ",
                                                  "_ChotCongNo_BaoCaoChiTietCuocKhachThe.png")

def caseid_customer66(self):
    get_datachecklist("Customer66")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.closing_debts_closing_debts(self, "Customer66", event, result)


def caseid_customer67(self):
    get_datachecklist("Customer67")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.closing_debts_closing_debts_excel(self, "Customer67", event, result)


def caseid_customer68(self):
    get_datachecklist("Customer68")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.report_customer_card_details(self, "Customer68", event, result)

def caseid_customer69(self):
    get_datachecklist("Customer69")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.report_customer_card_details_search(self, "Customer69", event, result)


def caseid_customer70(self):
    get_datachecklist("Customer70")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.report_customer_card_details_excel(self, "Customer70", event, result)


def caseid_customer71(self):
    get_datachecklist("Customer71")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.report_customer_card_details_excel_full(self, "Customer71", event, result)


def caseid_customer72(self):
    get_datachecklist("Customer72")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.report_card_top_up_transactions(self, "Customer72", event, result)


def caseid_customer73(self):
    get_datachecklist("Customer73")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.report_card_top_up_transactions_search(self, "Customer73", event, result)


def caseid_customer74(self):
    get_datachecklist("Customer74")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.report_card_top_up_transactions_excel(self, "Customer74", event, result)


def caseid_customer75(self):
    get_datachecklist("Customer75")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.report_the_trip_with_the_driver_card(self, "Customer75", event, result)


def caseid_customer76(self):
    get_datachecklist("Customer76")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.report_the_trip_with_the_driver_card_search(self, "Customer76", event, result)


def caseid_customer77(self):
    get_datachecklist("Customer77")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.report_the_trip_with_the_driver_card_excel(self, "Customer77", event, result)


def caseid_customer77_1(self):
    get_datachecklist("Customer77_1")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.report_the_trip_with_the_driver_card_payment(self, "Customer77_1", event, result)


def caseid_customer78(self):
    get_datachecklist("Customer78")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.customer_summary_report(self, "Customer78", event, result)


def caseid_customer79(self):
    get_datachecklist("Customer79")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.customer_summary_report_search(self, "Customer79", event, result)


def caseid_customer80(self):
    get_datachecklist("Customer80")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.customer_summary_report_excel(self, "Customer80", event, result)


def caseid_customer81(self):
    get_datachecklist("Customer81")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_transaction_report(self, "Customer81", event, result)


def caseid_customer82(self):
    get_datachecklist("Customer82")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_transaction_report_search(self, "Customer82", event, result)

def caseid_customer83(self):
    get_datachecklist("Customer83")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_transaction_report_excel(self, "Customer83", event, result)

def caseid_customer84(self):
    get_datachecklist("Customer84")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.check_prepaid_cards(self, "Customer84", event, result, "9999209842501710")


def caseid_customer85(self):
    get_datachecklist("Customer85")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.check_prepaid_cards_status(self, "Customer85", event, result, "9999209842501710")

def caseid_customer85_1(self):
    get_datachecklist("Customer85_1")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.the_tra_truoc(self)


def caseid_customer86(self):
    get_datachecklist("Customer86")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_after1(self, "Customer86", event, result, "9999992992096773", "01/01/2023 00:02", "09/02/2027 00:00", "209")


def caseid_customer87(self):
    get_datachecklist("Customer87")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_after2(self, "Customer87", event, result, "9999992992096773", "209")

def caseid_customer88(self):
    get_datachecklist("Customer88")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_after3(self, "Customer88", event, result, "9999992992096773", "209")

def caseid_customer89(self):
    get_datachecklist("Customer89")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_after4(self, "Customer89", event, result, "9999992992096773", "01/01/2023 00:02", "09/02/2027 00:00", "209")


def caseid_customer90(self):
    customer_stx.contract_card.get_number_serial(self, "Customer90")
    number_serial = var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 188, 2)
    get_datachecklist("Customer90")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.card_debt_closing(self, "Customer90", event, result, number_serial, "01/01/2023 00:02", "09/02/2027 00:00", "209")


def caseid_customer91(self):
    get_datachecklist("Customer91")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.check_card_debt_closing_1phan(self, "Customer91", event, result)


def caseid_customer92(self):
    get_datachecklist("Customer92")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.check_card_debt_closing_toanbo_1phan(self, "Customer92", event, result)


def caseid_customer93(self):
    get_datachecklist("Customer93")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    customer_stx.contract_card.check_card_debt_closing_toanbo_toanbo(self, "Customer93", event, result)







def caseid_report01(self):
    get_datachecklist("Report01")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_0(self, "Report01", event, result)


def caseid_report02(self):
    get_datachecklist("Report02")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_0_search(self, "Report02", event, result)


def caseid_report03(self):
    get_datachecklist("Report03")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_0_excel(self, "Report03", event, result)


def caseid_report04(self):
    get_datachecklist("Report04")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_0_excel_full(self, "Report04", event, result)


def caseid_report05(self):
    get_datachecklist("Report05")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_1(self, "Report05", event, result)


def caseid_report06(self):
    get_datachecklist("Report06")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_1_search(self, "Report06", event, result)


def caseid_report07(self):
    get_datachecklist("Report07")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_1_excel(self, "Report07", event, result)


def caseid_report07_1(self):
    get_datachecklist("Report07_1")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.check_origin_1(self, "Report07_1", event, result)


def caseid_report07_2(self):
    get_datachecklist("Report07_2")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.check_origin_2(self, "Report07_2", event, result)




def caseid_report08(self):
    get_datachecklist("Report08")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_4(self, "Report08", event, result)

def caseid_report09(self):
    get_datachecklist("Report09")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_4_search(self, "Report09", event, result)


def caseid_report10(self):
    get_datachecklist("Report10")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_4_excel(self, "Report10", event, result)


def caseid_report11(self):
    get_datachecklist("Report11")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_5(self, "Report11", event, result)


def caseid_report12(self):
    get_datachecklist("Report12")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_5_search(self, "Report12", event, result)


def caseid_report13(self):
    get_datachecklist("Report13")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_5_excel(self, "Report13", event, result)


def caseid_report14(self):
    get_datachecklist("Report14")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_6(self, "Report14", event, result)


def caseid_report15(self):
    get_datachecklist("Report15")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_6_search(self, "Report15", event, result)


def caseid_report16(self):
    get_datachecklist("Report16")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_6_excel(self, "Report16", event, result)


def caseid_report17(self):
    get_datachecklist("Report17")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_7(self, "Report17", event, result)


def caseid_report18(self):
    get_datachecklist("Report18")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_7_search(self, "Report18", event, result)


def caseid_report19(self):
    get_datachecklist("Report19")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_7_excel(self, "Report19", event, result)




def caseid_report20(self):
    get_datachecklist("Report20")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_8(self, "Report20", event, result)


def caseid_report21(self):
    get_datachecklist("Report21")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_8_search(self, "Report21", event, result)


def caseid_report22(self):
    get_datachecklist("Report22")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_8_excel(self, "Report22", event, result)


def caseid_report23(self):
    get_datachecklist("Report23")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_11(self, "Report23", event, result)


def caseid_report24(self):
    get_datachecklist("Report24")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_11_search(self, "Report24", event, result)


def caseid_report25(self):
    get_datachecklist("Report25")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_11_excel(self, "Report25", event, result)


def caseid_report26(self):
    get_datachecklist("Report26")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_12(self, "Report26", event, result)


def caseid_report27(self):
    get_datachecklist("Report27")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_12_search(self, "Report27", event, result)


def caseid_report28(self):
    get_datachecklist("Report28")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_12_excel(self, "Report28", event, result)


def caseid_report29(self):
    get_datachecklist("Report29")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_19(self, "Report29", event, result)


def caseid_report30(self):
    get_datachecklist("Report30")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_19_search(self, "Report30", event, result)


def caseid_report31(self):
    get_datachecklist("Report31")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_1.report_8_1_19_excel(self, "Report31", event, result)


def caseid_report32(self):
    get_datachecklist("Report32")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_3.report_8_3_1(self, "Report32", event, result)


def caseid_report33(self):
    get_datachecklist("Report33")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_3.report_8_3_1_search(self, "Report33", event, result)


def caseid_report34(self):
    get_datachecklist("Report34")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_3.report_8_3_1_excel(self, "Report34", event, result)


def caseid_report35(self):
    get_datachecklist("Report35")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_3.report_8_3_2(self, "Report35", event, result)


def caseid_report36(self):
    get_datachecklist("Report36")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_3.report_8_3_2_search(self, "Report36", event, result)


def caseid_report37(self):
    get_datachecklist("Report37")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_3.report_8_3_2_excel(self, "Report37", event, result)


def caseid_report38(self):
    get_datachecklist("Report38")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_3.report_8_3_3(self, "Report38", event, result)


def caseid_report39(self):
    get_datachecklist("Report39")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_3.report_8_3_3_search(self, "Report39", event, result)


def caseid_report40(self):
    get_datachecklist("Report40")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_3.report_8_3_3_excel(self, "Report40", event, result)


def caseid_report41(self):
    get_datachecklist("Report41")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_3.report_8_3_4(self, "Report41", event, result)


def caseid_report42(self):
    get_datachecklist("Report42")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_3.report_8_3_4_search(self, "Report42", event, result)


def caseid_report43(self):
    get_datachecklist("Report43")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_3.report_8_3_4_excel(self, "Report43", event, result)


def caseid_report44(self):
    get_datachecklist("Report44")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_3.report_8_3_5(self, "Report44", event, result)


def caseid_report45(self):
    get_datachecklist("Report45")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_3.report_8_3_5_search(self, "Report45", event, result)


def caseid_report46(self):
    get_datachecklist("Report46")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_3.report_8_3_5_excel(self, "Report46", event, result)


def caseid_report47(self):
    get_datachecklist("Report47")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_1(self, "Report47", event, result)


def caseid_report48(self):
    get_datachecklist("Report48")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_1_search(self, "Report48", event, result)


def caseid_report49(self):
    get_datachecklist("Report49")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_1_excel(self, "Report49", event, result)

def caseid_report50(self):
    get_datachecklist("Report50")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_2(self, "Report50", event, result)

def caseid_report51(self):
    get_datachecklist("Report51")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_2_search(self, "Report51", event, result)


def caseid_report52(self):
    get_datachecklist("Report52")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_2_excel(self, "Report52", event, result)


def caseid_report53(self):
    get_datachecklist("Report53")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_2_excel_full(self, "Report53", event, result)


def caseid_report54(self):
    get_datachecklist("Report54")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_3(self, "Report54", event, result)

def caseid_report55(self):
    get_datachecklist("Report55")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_3_search(self, "Report55", event, result)

def caseid_report56(self):
    get_datachecklist("Report56")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_3_excel(self, "Report56", event, result)


def caseid_report57(self):
    get_datachecklist("Report57")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_4(self, "Report57", event, result)


def caseid_report58(self):
    get_datachecklist("Report58")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_4_search(self, "Report58", event, result)


def caseid_report59(self):
    get_datachecklist("Report59")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_4_excel(self, "Report59", event, result)


def caseid_report60(self):
    get_datachecklist("Report60")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_5(self, "Report60", event, result)


def caseid_report61(self):
    get_datachecklist("Report61")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_5_search(self, "Report61", event, result)


def caseid_report62(self):
    get_datachecklist("Report62")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_5_excel(self, "Report62", event, result)


def caseid_report63(self):
    get_datachecklist("Report63")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_6(self, "Report63", event, result)


def caseid_report64(self):
    get_datachecklist("Report64")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_6_search(self, "Report64", event, result)


def caseid_report65(self):
    get_datachecklist("Report65")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_6_excel(self, "Report65", event, result)


def caseid_report66(self):
    get_datachecklist("Report66")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_7(self, "Report66", event, result)


def caseid_report67(self):
    get_datachecklist("Report67")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_7_search(self, "Report67", event, result)


def caseid_report68(self):
    get_datachecklist("Report68")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_7_excel(self, "Report68", event, result)


def caseid_report69(self):
    get_datachecklist("Report69")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_8(self, "Report69", event, result)


def caseid_report70(self):
    get_datachecklist("Report70")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_8_search(self, "Report70", event, result)


def caseid_report71(self):
    get_datachecklist("Report71")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_8_excel(self, "Report71", event, result)



def caseid_report72(self):
    get_datachecklist("Report72")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_17(self, "Report72", event, result)


def caseid_report73(self):
    get_datachecklist("Report73")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_17_search(self, "Report73", event, result)


def caseid_report74(self):
    get_datachecklist("Report74")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_4.report_8_4_17_excel(self, "Report74", event, result)


def caseid_report75(self):
    get_datachecklist("Report75")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_8.report_8_8_2(self, "Report75", event, result)


def caseid_report76(self):
    get_datachecklist("Report76")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_8.report_8_8_2_search(self, "Report76", event, result)


def caseid_report77(self):
    get_datachecklist("Report77")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_8.report_8_8_2_excel(self, "Report77", event, result)


def caseid_report77_1(self):
    get_datachecklist("Report77_1")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_8.check_origin8_8_2_1day(self, "Report77_1", event, result)


def caseid_report77_2(self):
    get_datachecklist("Report77_2")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_8.check_origin8_8_2_2day(self, "Report77_2", event, result)


def caseid_report78(self):
    get_datachecklist("Report78")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_8.report_8_8_3(self, "Report78", event, result)


def caseid_report79(self):
    get_datachecklist("Report79")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_8.report_8_8_3_search(self, "Report79", event, result)


def caseid_report80(self):
    get_datachecklist("Report80")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.report_8_8.report_8_8_3_excel(self, "Report80", event, result)




def caseid_admin01(self):
    get_datachecklist("Admin01")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_1.admin_10_1_1(self, "Admin01", event, result)


def caseid_admin02(self):
    get_datachecklist("Admin02")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_1.admin_10_1_1_search(self, "Admin02", event, result, "0")


def caseid_admin03(self):
    get_datachecklist("Admin03")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_1.admin_10_1_1_search(self, "Admin03", event, result, "1")


def caseid_admin04(self):
    get_datachecklist("Admin04")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_3.admin_10_3_1(self, "Admin04", event, result)


def caseid_admin05(self):
    get_datachecklist("Admin05")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_3.admin_10_3_1_save(self, "Admin05", event, result)


def caseid_admin06(self):
    get_datachecklist("Admin06")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_3.admin_10_3_1_sync_driver(self, "Admin06", event, result)


def caseid_admin07(self):
    get_datachecklist("Admin07")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_3.admin_10_3_1_sync_customer(self, "Admin07", event, result)


def caseid_admin08(self):
    get_datachecklist("Admin08")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_3.admin_10_3_1_back(self, "Admin08", event, result)

def caseid_admin08_1(self):
    get_datachecklist("Admin08_1")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_3.admin_10_3_4(self, "Admin08_1", event, result)

def caseid_admin08_2(self):
    get_datachecklist("Admin08_2")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_3.admin_10_3_4_search(self, "Admin08_2", event, result,
                                                  var_stx.DataTables_Table_2_2, var_stx.group_name,
                                                  var_stx.DataTables_Table_1_2, "_QuanTriNhomDoi_TenNhomTimKiem.png")

def caseid_admin08_3(self):
    get_datachecklist("Admin08_3")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_3.admin_10_3_4_search(self, "Admin08_3", event, result,
                                                  var_stx.DataTables_Table_2_4, var_stx.group_name,
                                                  var_stx.DataTables_Table_1_4, "_QuanTriNhomDoi_TenHienThiTimKiem.png")

def caseid_admin08_4(self):
    get_datachecklist("Admin08_4")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_3.admin_10_3_4_add_new(self, "Admin08_4", event, result)

def caseid_admin08_5(self):
    get_datachecklist("Admin08_5")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_3.admin_10_3_4_update(self, "Admin08_5", event, result)

def caseid_admin08_6(self):
    get_datachecklist("Admin08_6")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_3.admin_10_3_4_delete(self, "Admin08_6", event, result)

def caseid_admin08_6(self):
    get_datachecklist("Admin08_7")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_3.admin_10_3_4_asignuser(self, "Admin08_7", event, result)
def caseid_admin09(self):
    get_datachecklist("Admin09")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_3.admin_10_3_5(self, "Admin09", event, result)

def caseid_admin10(self):
    get_datachecklist("Admin10")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_3.admin_10_3_5_search(self, "Admin10", event, result)

def caseid_admin11(self):
    get_datachecklist("Admin11")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_3.admin_10_3_5_add_new(self, "Admin11", event, result)

def caseid_admin12(self):
    get_datachecklist("Admin12")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_3.admin_10_3_5_update(self, "Admin12", event, result)


def caseid_admin13(self):
    get_datachecklist("Admin13")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_3.admin_10_3_5_delete(self, "Admin13", event, result)


def caseid_admin14(self):
    get_datachecklist("Admin14")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_3.admin_10_3_6(self, "Admin14", event, result)


def caseid_admin15(self):
    pass


def caseid_admin16(self):
    get_datachecklist("Admin16")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_3.admin_10_3_6_sync_driver(self, "Admin16", event, result)


def caseid_admin17(self):
    get_datachecklist("Admin17")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_3.admin_10_3_6_sync_customer(self, "Admin17", event, result)


def caseid_admin18(self):
    get_datachecklist("Admin18")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_3.admin_10_3_6_add_new(self, "Admin18", event, result)



def caseid_admin19(self):
    get_datachecklist("Admin19")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_3.admin_10_3_6_update(self, "Admin19", event, result)


def caseid_admin20(self):
    get_datachecklist("Admin20")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_3.admin_10_3_6_delete(self, "Admin20", event, result)


def caseid_admin21(self):
    get_datachecklist("Admin21")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_5.admin_10_5_5(self, "Admin21", event, result)


def caseid_admin22(self):
    get_datachecklist("Admin22")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_5.admin_10_5_5_search(self, "Admin22", event, result)


def caseid_admin23(self):
    get_datachecklist("Admin23")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_5.admin_10_5_5_excel(self, "Admin23", event, result)


def caseid_admin24(self):
    get_datachecklist("Admin24")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_5.admin_10_5_5_add_new(self, "Admin24", event, result)


def caseid_admin25(self):
    get_datachecklist("Admin25")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_5.admin_10_5_5_update(self, "Admin25", event, result)


def caseid_admin26(self):
    get_datachecklist("Admin26")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_5.admin_10_5_5_get_code(self, "Admin26", event, result)


def caseid_admin27(self):
    get_datachecklist("Admin27")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_5.admin_10_5_5_role(self, "Admin27", event, result)


def caseid_admin28(self):
    get_datachecklist("Admin28")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_5.admin_10_5_5_decentralization(self, "Admin28", event, result)


def caseid_admin29(self):
    get_datachecklist("Admin29")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_5.admin_10_5_5_config(self, "Admin29", event, result)


def caseid_admin30(self):
    get_datachecklist("Admin30")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_5.admin_10_5_5_lock(self, "Admin30", event, result, "Khóa thành công.", "_DanhSachTaiKhoan_Khoa.png")


def caseid_admin31(self):
    get_datachecklist("Admin31")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_5.admin_10_5_5_lock(self, "Admin31", event, result, "Mở khóa thành công.", "_DanhSachTaiKhoan_MoKhoa.png")


def caseid_admin32(self):
    get_datachecklist("Admin32")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_5.admin_10_5_5_delete(self, "Admin32", event, result)


def caseid_admin33(self):
    get_datachecklist("Admin33")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_5.admin_10_5_7(self, "Admin33", event, result)


def caseid_admin34(self):
    get_datachecklist("Admin34")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_5.admin_10_5_7_detail(self, "Admin34", event, result)


def caseid_admin35(self):
    get_datachecklist("Admin35")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_5.admin_10_5_7_from_to_day(self, "Admin35", event, result)


def caseid_admin36(self):
    get_datachecklist("Admin36")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_5.admin_10_5_7_search(self, "Admin36", event, result, var_stx.name_account, "autoba",
                                                  var_stx.list_data2_2, "_LichSuTaiKhoan_TenTaiKhoan.png")

def caseid_admin37(self):
    get_datachecklist("Admin37")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_5.admin_10_5_7_search(self, "Admin37", event, result, var_stx.data_change, "0835210360",
                                                  var_stx.check_data_new, "_LichSuTaiKhoan_DuLieuThayDoi.png")


def caseid_admin38(self):
    get_datachecklist("Admin38")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_5.admin_10_5_7_table(self, "Admin38", event, result)


def caseid_admin39(self):
    get_datachecklist("Admin39")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_5.admin_10_5_7_type_action(self, "Admin39", event, result)


def caseid_admin40(self):
    get_datachecklist("Admin40")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_6.admin_10_6_1(self, "Admin40", event, result)


def caseid_admin41(self):
    get_datachecklist("Admin41")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_6.admin_10_6_1_check(self, "Admin41", event, result)


def caseid_admin42(self):
    get_datachecklist("Admin42")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_6.admin_10_6_2(self, "Admin42", event, result)


def caseid_admin43(self):
    get_datachecklist("Admin43")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_6.admin_10_6_2_check(self, "Admin43", event, result)


def caseid_admin44(self):
    get_datachecklist("Admin44")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_6.admin_10_6_3(self, "Admin44", event, result)


def caseid_admin45(self):
    get_datachecklist("Admin45")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_6.admin_10_6_3_check(self, "Admin45", event, result)


def caseid_admin46(self):
    get_datachecklist("Admin46")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_6.admin_10_6_4(self, "Admin46", event, result)


def caseid_admin47(self):
    get_datachecklist("Admin47")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_6.admin_10_6_4_check(self, "Admin47", event, result)


def caseid_admin48(self):
    get_datachecklist("Admin48")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_6.admin_10_6_5(self, "Admin48", event, result)


def caseid_admin49(self):
    get_datachecklist("Admin49")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_6.admin_10_6_5_check(self, "Admin49", event, result)


def caseid_admin50(self):
    get_datachecklist("Admin50")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_6.admin_10_6_6(self, "Admin50", event, result)


def caseid_admin51(self):
    get_datachecklist("Admin51")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_6.admin_10_6_6_check(self, "Admin51", event, result)


def caseid_admin52(self):
    get_datachecklist("Admin52")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_6.admin_10_6_7(self, "Admin52", event, result)


def caseid_admin53(self):
    get_datachecklist("Admin53")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_6.admin_10_6_7_check(self, "Admin53", event, result)

def caseid_admin54(self):
    get_datachecklist("Admin54")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_6.admin_10_6_8(self, "Admin54", event, result)

def caseid_admin55(self):
    get_datachecklist("Admin55")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_6.admin_10_6_9(self, "Admin55", event, result)

def caseid_admin56(self):
    get_datachecklist("Admin56")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_6.admin_10_6_9_check(self, "Admin56", event, result)

def caseid_admin57(self):
    get_datachecklist("Admin57")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_6.admin_10_6_10(self, "Admin57", event, result)

def caseid_admin58(self):
    get_datachecklist("Admin58")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_6.admin_10_6_10_check(self, "Admin58", event, result)

def caseid_admin59(self):
    get_datachecklist("Admin59")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_6.admin_10_6_11(self, "Admin59", event, result)

def caseid_admin60(self):
    get_datachecklist("Admin60")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_6.admin_10_6_11_check(self, "Admin60", event, result)


def caseid_admin61(self):
    get_datachecklist("Admin61")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_1(self, "Admin61", event, result)


def caseid_admin62(self):
    get_datachecklist("Admin62")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_1_search(self, "Admin62", event, result)


def caseid_admin63(self):
    get_datachecklist("Admin63")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_1_combobox_select(self, "Admin63", event, result, var_stx.choose_driver_icon, var_stx.DriverIdSearch_truongvck33,
                                                           var_stx.auto383_dinhmanhcuong92, "auto383-Đinh Mạnh Cường 92", "_QuanTriThongBaoLaiXe_ChonLaiXeDuocGui.png")



def caseid_admin64(self):
    get_datachecklist("Admin64")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_1_combobox(self, "Admin64", event, result, var_stx.ArticleType_0, var_stx.list_data2_4,
                                                    "Thông báo", "_QuanTriThongBaoLaiXe_ThongBao.png")

def caseid_admin65(self):
    get_datachecklist("Admin65")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_1_combobox(self, "Admin65", event, result, var_stx.ArticleType_1, var_stx.list_data2_4,
                                                    "Tin tức", "_QuanTriThongBaoLaiXe_TinTuc.png")


def caseid_admin66(self):
    get_datachecklist("Admin66")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_1_combobox(self, "Admin66", event, result, var_stx.ArticleType_3, var_stx.list_data2_4,
                                                    "Thông báo Notify", "_QuanTriThongBaoLaiXe_ThongBaoNotify.png")

def caseid_admin67(self):
    get_datachecklist("Admin67")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_1_combobox(self, "Admin67", event, result, var_stx.PeriodId_0, var_stx.list_data2_3,
                                                    "Không lặp", "_QuanTriThongBaoLaiXe_KhongLap.png")


def caseid_admin68(self):
    get_datachecklist("Admin68")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_1_combobox(self, "Admin68", event, result, var_stx.PeriodId_1, var_stx.list_data2_3,
                                                    "Mỗi ngày", "_QuanTriThongBaoLaiXe_MoiNgay.png")

def caseid_admin69(self):
    get_datachecklist("Admin69")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_1_combobox(self, "Admin69", event, result, var_stx.PeriodId_2, var_stx.list_data2_3,
                                                    "Mỗi tuần", "_QuanTriThongBaoLaiXe_MoiTuan.png")

def caseid_admin70(self):
    get_datachecklist("Admin70")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_1_combobox(self, "Admin70", event, result, var_stx.PeriodId_3, var_stx.list_data2_3,
                                                    "Mỗi tháng", "_QuanTriThongBaoLaiXe_MoiThang.png")


def caseid_admin71(self):
    get_datachecklist("Admin71")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_1_combobox1(self, "Admin71", event, result, var_stx.SendArticleTypeSearch_1,
                                                           "Theo Công ty", "_QuanTriThongBaoLaiXe_CongTy.png")

def caseid_admin72(self):
    get_datachecklist("Admin72")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_1_combobox1(self, "Admin72", event, result, var_stx.SendArticleTypeSearch_2,
                                                           "Theo Nhóm đội", "_QuanTriThongBaoLaiXe_TheoNhomDoi.png")

def caseid_admin73(self):
    get_datachecklist("Admin73")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_1_combobox1(self, "Admin73", event, result, var_stx.SendArticleTypeSearch_3,
                                                           "Theo Lái xe", "_QuanTriThongBaoLaiXe_TheoLaiXe.png")


def caseid_admin74(self):
    get_datachecklist("Admin74")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_1_combobox1(self, "Admin74", event, result, var_stx.SendArticleTypeSearch_4,
                                                           "Theo Biển số", "_QuanTriThongBaoLaiXe_TheoBienSo.png")


def caseid_admin75(self):
    get_datachecklist("Admin75")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_1_excel_download(self, "Admin75", event, result)


def caseid_admin76(self):
    get_datachecklist("Admin76")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_1_excel_upload(self, "Admin76", event, result)


def caseid_admin77(self):
    get_datachecklist("Admin77")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_1_add_new(self, "Admin77", event, result)

def caseid_admin78(self):
    get_datachecklist("Admin78")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_1_update(self, "Admin78", event, result)

def caseid_admin79(self):
    get_datachecklist("Admin79")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_1_see(self, "Admin79", event, result)

def caseid_admin80(self):
    get_datachecklist("Admin80")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_1_detail(self, "Admin80", event, result)


def caseid_admin81(self):
    get_datachecklist("Admin81")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_1_delete(self, "Admin81", event, result)


def caseid_admin82(self):
    get_datachecklist("Admin82")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_4(self, "Admin82", event, result)


def caseid_admin83(self):
    get_datachecklist("Admin83")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_4_from_to_day(self, "Admin83", event, result)


def caseid_admin84(self):
    get_datachecklist("Admin84")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_4_search(self, "Admin84", event, result)


def caseid_admin85(self):
    get_datachecklist("Admin85")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_4_combobox(self, "Admin85", event, result, var_stx.SendTypeSearch_0, var_stx.ag1_3,
                                                    "Thông báo", "_QuanTriThongBaoLaiXeV2_ThongBao.png")

def caseid_admin86(self):
    get_datachecklist("Admin86")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_4_combobox(self, "Admin86", event, result, var_stx.SendTypeSearch_1a, var_stx.ag1_3,
                                                    "Tin tức", "_QuanTriThongBaoLaiXeV2_TinTuc.png")

def caseid_admin87(self):
    get_datachecklist("Admin87")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_4_combobox(self, "Admin87", event, result, var_stx.SendTypeSearch_3, var_stx.ag1_3,
                                                    "Thông báo Notify", "_QuanTriThongBaoLaiXeV2_ThongbaoNotify.png")

def caseid_admin88(self):
    get_datachecklist("Admin88")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_4_combobox(self, "Admin88", event, result, var_stx.Period_0, var_stx.ag1_7,
                                                    "Không lặp", "_QuanTriThongBaoLaiXeV2_KhongLap.png")

def caseid_admin89(self):
    get_datachecklist("Admin89")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_4_combobox(self, "Admin89", event, result, var_stx.Period_1a, var_stx.ag1_7,
                                                    "Mỗi ngày", "_QuanTriThongBaoLaiXeV2_MoiNgay.png")

def caseid_admin90(self):
    get_datachecklist("Admin90")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_4_combobox(self, "Admin90", event, result, var_stx.Period_7, var_stx.ag1_7,
                                                    "Mỗi tuần", "_QuanTriThongBaoLaiXeV2_MoiTuan.png")

def caseid_admin91(self):
    get_datachecklist("Admin91")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_4_combobox(self, "Admin91", event, result, var_stx.Period_30, var_stx.ag1_7,
                                                    "Mỗi tháng", "_QuanTriThongBaoLaiXeV2_MoiThang.png")

def caseid_admin92(self):
    get_datachecklist("Admin92")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_4_combobox(self, "Admin92", event, result, var_stx.ParentArticleTypeSearch_0, var_stx.ag1_4,
                                                    "Chung", "_QuanTriThongBaoLaiXeV2_Chung.png")

def caseid_admin93(self):
    get_datachecklist("Admin93")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_4_combobox(self, "Admin93", event, result, var_stx.ParentArticleTypeSearch_1a, var_stx.ag1_4,
                                                    "Cá nhân", "_QuanTriThongBaoLaiXeV2_CaNhan.png")


def caseid_admin93_1(self):
    get_datachecklist("Admin93_1")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_4_combobox(self, "Admin93_1", event, result, var_stx.ParentArticleTypeSearch_2, var_stx.ag1_4,
                                                    "Cuốc khách", "_QuanTriThongBaoLaiXeV2_CuocKhach.png")


def caseid_admin94(self):
    get_datachecklist("Admin94")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_4_combobox(self, "Admin94", event, result, var_stx.ParentArticleTypeSearch_3, var_stx.ag1_4,
                                                    "Quan trọng", "_QuanTriThongBaoLaiXeV2_QuanTrong.png")

def caseid_admin95(self):
    get_datachecklist("Admin95")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_4_combobox(self, "Admin95", event, result, var_stx.SendArticleTypeSearch_1b, var_stx.ag1_6,
                                                    "Theo Công ty", "_QuanTriThongBaoLaiXeV2_CongTy.png")

def caseid_admin96(self):
    get_datachecklist("Admin96")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_4_combobox(self, "Admin96", event, result, var_stx.SendArticleTypeSearch_3, var_stx.ag1_6,
                                                    "Theo Lái xe", "_QuanTriThongBaoLaiXeV2_LaiXe.png")


def caseid_admin97(self):
    get_datachecklist("Admin97")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_4_excel_download(self, "Admin97", event, result)


def caseid_admin98(self):
    get_datachecklist("Admin98")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_4_excel_upload(self, "Admin98", event, result)


def caseid_admin99(self):
    get_datachecklist("Admin99")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_4_add_new(self, "Admin99", event, result)


def caseid_admin100(self):
    get_datachecklist("Admin100")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_4_detail1(self, "Admin100", event, result)

def caseid_admin101(self):
    get_datachecklist("Admin101")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_4_detail2(self, "Admin101", event, result)

def caseid_admin102(self):
    get_datachecklist("Admin102")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_4_coppy(self, "Admin102", event, result)

def caseid_admin103(self):
    get_datachecklist("Admin103")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_4_pc(self, "Admin103", event, result)

def caseid_admin104(self):
    get_datachecklist("Admin104")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_4_phone(self, "Admin104", event, result)


def caseid_admin105(self):
    get_datachecklist("Admin105")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_7.admin_10_7_4_delete(self, "Admin105", event, result)

def caseid_admin106(self):
    get_datachecklist("Admin106")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_10.admin_10_10_2(self, "Admin106", event, result)

def caseid_admin107(self):
    get_datachecklist("Admin107")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_10.admin_10_10_2_search(self, "Admin107", event, result)


def caseid_admin108(self):
    get_datachecklist("Admin108")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_10.admin_10_10_2_excel(self, "Admin108", event, result)

def caseid_admin109(self):
    get_datachecklist("Admin109")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_10.admin_10_10_2_add_new(self, "Admin109", event, result)

def caseid_admin110(self):
    get_datachecklist("Admin110")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_10.admin_10_10_2_update(self, "Admin110", event, result)


def caseid_admin111(self):
    get_datachecklist("Admin111")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_10.admin_10_10_2_delete(self, "Admin111", event, result)


def caseid_admin112(self):
    get_datachecklist("Admin112")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_10.admin_10_10_3(self, "Admin112", event, result)

def caseid_admin113(self):
    get_datachecklist("Admin113")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_10.admin_10_10_3_search(self, "Admin113", event, result)

def caseid_admin114(self):
    get_datachecklist("Admin114")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_10.admin_10_10_3_add_new(self, "Admin114", event, result)

def caseid_admin115(self):
    get_datachecklist("Admin115")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_10.admin_10_10_3_update(self, "Admin115", event, result)

def caseid_admin116(self):
    get_datachecklist("Admin116")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_10.admin_10_10_3_delete(self, "Admin116", event, result)

def caseid_admin117(self):
    get_datachecklist("Admin117")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_10.admin_10_10_4(self, "Admin117", event, result)

def caseid_admin118(self):
    get_datachecklist("Admin118")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_10.admin_10_10_4_search(self, "Admin118", event, result)


def caseid_admin119(self):
    get_datachecklist("Admin119")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_10.admin_10_10_4_combobox(self, "Admin119", event, result, var_stx.FeeType_0, var_stx.table_table1_5,
                                                      "Cố định", "_PhuPhiTheoThuHo_CoDinh.png")


def caseid_admin120(self):
    get_datachecklist("Admin120")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_10.admin_10_10_4_combobox(self, "Admin120", event, result, var_stx.FeeType_1, var_stx.table_table1_5,
                                                      "Phần trăm", "_PhuPhiTheoThuHo_PhanTram.png")

def caseid_admin121(self):
    get_datachecklist("Admin121")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_10.admin_10_10_4_excel(self, "Admin121", event, result)


def caseid_admin122(self):
    get_datachecklist("Admin122")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_10.admin_10_10_4_add_new(self, "Admin122", event, result)


def caseid_admin123(self):
    get_datachecklist("Admin123")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_10.admin_10_10_4_update(self, "Admin123", event, result)


def caseid_admin124(self):
    get_datachecklist("Admin124")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_10.admin_10_10_4_delete(self, "Admin124", event, result)


def caseid_admin125(self):
    get_datachecklist("Admin125")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_10.admin_10_10_5(self, "Admin125", event, result)


def caseid_admin126(self):
    get_datachecklist("Admin126")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_10.admin_10_10_5_search(self, "Admin126", event, result)


def caseid_admin127(self):
    get_datachecklist("Admin127")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_10.admin_10_10_5_add_new(self, "Admin127", event, result)

def caseid_admin128(self):
    get_datachecklist("Admin128")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_10.admin_10_10_5_update(self, "Admin128", event, result)

def caseid_admin129(self):
    get_datachecklist("Admin129")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    administration.admin_10_10.admin_10_10_5_delete(self, "Admin129", event, result)



def caseid_PartnerTrip01(self):
    get_datachecklist("PartnerTrip01")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.PartnerTrip_12_1.PartnerTrip_12_1_1(self, "PartnerTrip01", event, result)


def caseid_PartnerTrip02(self):
    get_datachecklist("PartnerTrip02")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.PartnerTrip_12_1.PartnerTrip_12_1_1_search(self, "PartnerTrip02", event, result)


def caseid_PartnerTrip03(self):
    get_datachecklist("PartnerTrip03")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.PartnerTrip_12_1.PartnerTrip_12_1_1_excel(self, "PartnerTrip03", event, result)



def caseid_PartnerTrip04(self):
    get_datachecklist("PartnerTrip04")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.PartnerTrip_12_1.PartnerTrip_12_1_2(self, "PartnerTrip04", event, result)


def caseid_PartnerTrip05(self):
    get_datachecklist("PartnerTrip05")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.PartnerTrip_12_1.PartnerTrip_12_1_2_search(self, "PartnerTrip05", event, result)


def caseid_PartnerTrip06(self):
    get_datachecklist("PartnerTrip06")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    report_stx.PartnerTrip_12_1.PartnerTrip_12_1_2_excel(self, "PartnerTrip06", event, result)





def caseid_accounting01(self):
    get_datachecklist("Accounting01")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1(self, "Accounting01", event, result)


def caseid_accounting02(self):
    get_datachecklist("Accounting02")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_fromday_today(self, "Accounting02", event, result)


def caseid_accounting03(self):
    get_datachecklist("Accounting03")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_combobox(self, "Accounting03", event, result, var_stx.accounting_2_Source, var_stx.Source,
                                                        var_stx.accounting_1_Source, "_QuanLyXuatHoaDon_NguonCuoc.png")


def caseid_accounting04(self):
    get_datachecklist("Accounting04")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_input(self, "Accounting04", event, result, var_stx.accounting_2_DisplayPublicBookId, var_stx.DisplayPublicBookId,
                                                        var_stx.accounting_1_DisplayPublicBookId, "_QuanLyXuatHoaDon_MaCuocKhach.png")

def caseid_accounting05(self):
    get_datachecklist("Accounting05")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_other_input(self, "Accounting05", event, result, var_stx.Mobile, var_stx.MobileOrAddress,
                                                        var_stx.accounting_1_Mobile, "_QuanLyXuatHoaDon_SoDienThoai.png")

def caseid_accounting06(self):
    get_datachecklist("Accounting06")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_input(self, "Accounting06", event, result, var_stx.accounting_2_FromAddress, var_stx.MobileOrAddress,
                                                        var_stx.accounting_1_FromAddress, "_QuanLyXuatHoaDon_DiaChiDon.png")


def caseid_accounting07(self):
    get_datachecklist("Accounting07")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_other_input(self, "Accounting07", event, result, var_stx.id_InvoiceNo, var_stx.InvoiceNo,
                                                        var_stx.accounting_1_InvoiceNo, "_QuanLyXuatHoaDon_SoHoaDon.png")

def caseid_accounting08(self):
    get_datachecklist("Accounting08")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_combobox_other(self, "Accounting08", event, result, "Chưa xử lý", var_stx.Status,
                                                        var_stx.accounting_1_Status, "_QuanLyXuatHoaDon_ChuaXuLy.png")

def caseid_accounting09(self):
    get_datachecklist("Accounting09")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_combobox_other(self, "Accounting09", event, result, "Chờ NCC xử lý", var_stx.Status,
                                                        var_stx.accounting_1_Status, "_QuanLyXuatHoaDon_ChoNCCXuLy.png")

def caseid_accounting10(self):
    get_datachecklist("Accounting10")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_combobox_other(self, "Accounting10", event, result, "Đang xử lý", var_stx.Status,
                                                        var_stx.accounting_1_Status, "_QuanLyXuatHoaDon_DangXuLy.png")

def caseid_accounting11(self):
    get_datachecklist("Accounting11")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_combobox_other(self, "Accounting11", event, result, "Đã xuất", var_stx.Status,
                                                        var_stx.accounting_1_Status, "_QuanLyXuatHoaDon_DaXuat.png")
def caseid_accounting12(self):
    get_datachecklist("Accounting12")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_combobox_other(self, "Accounting12", event, result, "Xuất lỗi", var_stx.Status,
                                                        var_stx.accounting_1_Status, "_QuanLyXuatHoaDon_XuatLoi.png")
def caseid_accounting13(self):
    get_datachecklist("Accounting13")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_combobox_other(self, "Accounting13", event, result, "Gửi lỗi NCC", var_stx.Status,
                                                        var_stx.accounting_1_Status, "_QuanLyXuatHoaDon_GuiLoiNCC.png")

def caseid_accounting14(self):
    get_datachecklist("Accounting14")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_combobox_other(self, "Accounting14", event, result, "Không xuất", var_stx.Status,
                                                        var_stx.accounting_1_Status, "_QuanLyXuatHoaDon_KhongXuat.png")

def caseid_accounting15(self):
    get_datachecklist("Accounting15")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_combobox_other(self, "Accounting15", event, result, "Khách lẻ", var_stx.InvoiceType,
                                                        var_stx.accounting_1_InvoiceTypeName, "_QuanLyXuatHoaDon_KhackLe.png")

def caseid_accounting16(self):
    get_datachecklist("Accounting16")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_combobox_other(self, "Accounting16", event, result, "Theo yêu cầu", var_stx.InvoiceType,
                                                        var_stx.accounting_1_InvoiceTypeName, "_QuanLyXuatHoaDon_KhackLe.png")

def caseid_accounting17(self):
    get_datachecklist("Accounting17")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_combobox_other(self, "Accounting17", event, result, "Cuốc test/lỗi", var_stx.InvoiceType,
                                                        var_stx.accounting_1_InvoiceTypeName, "_QuanLyXuatHoaDon_KhackLe.png")



def caseid_accounting18(self):
    get_datachecklist("Accounting18")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_other_combobox(self, "Accounting18", event, result, "LegalEntityName", var_stx.LegalEntityId,
                                                        var_stx.accounting_1_LegalEntityName, "_QuanLyXuatHoaDon_DonViQuanLy.png")

def caseid_accounting19(self):
    get_datachecklist("Accounting19")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_search_advance(self, "Accounting19", event, result)


def caseid_accounting20(self):
    get_datachecklist("Accounting20")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_search_advance_delete(self, "Accounting20", event, result)

def caseid_accounting21(self):
    get_datachecklist("Accounting21")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_excel(self, "Accounting21", event, result)


def caseid_accounting22(self):
    get_datachecklist("Accounting22")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_button(self, "Accounting22", event, result, "1", var_stx.retail_invoice,
                                                      var_stx.check_retail_invoice, "Xác nhận xuất hoá đơn khách lẻ",
                                                      "Cuốc khách không đủ điều kiện xuất hóa đơn", "_QuanLyXuatHoaDon_XuatHoaDonKhachLe.png")

def caseid_accounting23(self):
    get_datachecklist("Accounting23")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_button(self, "Accounting23", event, result, "2", var_stx.not_export_invoice,
                                                      var_stx.check_not_export_invoice, "Xác nhận không xuất hóa đơn",
                                                      "", "_QuanLyXuatHoaDon_KhongXuatHoa.png")

def caseid_accounting24(self):
    get_datachecklist("Accounting24")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_button(self, "Accounting24", event, result, "1", var_stx.export_invoice,
                                                      var_stx.check_export_invoice, "Thông tin xuất hóa đơn",
                                                      "Cuốc khách không đủ điều kiện xuất hóa đơn", "_QuanLyXuatHoaDon_XuatHoaDon.png")


def caseid_accounting25(self):
    get_datachecklist("Accounting25")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_export_invoice_fillinfo(self, "Accounting25", event, result)


def caseid_accounting26(self):
    get_datachecklist("Accounting26")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_icon(self, "Accounting26", event, result, "ActualRevenue",
                                                    var_stx.toast_message, "Thay đổi thực thu thành công", "_QuanLyXuatHoaDon_ThucThu.png")

def caseid_accounting27(self):
    get_datachecklist("Accounting27")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_icon(self, "Accounting27", event, result, "InvoiceFromAddress",
                                                    var_stx.toast_message, "Thay đổi địa chỉ đón thành công", "_QuanLyXuatHoaDon_DiaChiDonXHD.png")

def caseid_accounting28(self):
    get_datachecklist("Accounting28")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_icon(self, "Accounting28", event, result, "InvoiceToAddress",
                                                    var_stx.toast_message, "Thay đổi địa chỉ trả thành công", "_QuanLyXuatHoaDon_DiaChiTraXHD.png")

def caseid_accounting29(self):
    get_datachecklist("Accounting29")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_electronic_invoice(self, "Accounting29", event, result, "Xem ")

def caseid_accounting30(self):
    get_datachecklist("Accounting30")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_electronic_invoice(self, "Accounting30", event, result, "Xuất ")

def caseid_accounting31(self):
    get_datachecklist("Accounting31")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_electronic_invoice(self, "Accounting31", event, result, "Xuất lại ")

def caseid_accounting32(self):
    get_datachecklist("Accounting32")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_electronic_invoice(self, "Accounting32", event, result, "Xem HĐ ")


def caseid_accounting33(self):
    get_datachecklist("Accounting33")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_link_icon(self, "Accounting33", event, result, var_stx.icon_bienlai,
                                                         var_stx.check_ReceiptLink, "CẢM ƠN QUÝ KHÁCH ĐÃ SỬ DỤNG DỊCH VỤ!",
                                                         "_QuanLyXuatHoaDon_BienLai.png")

def caseid_accounting34(self):
    get_datachecklist("Accounting34")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_link_icon(self, "Accounting34", event, result, var_stx.icon_hopdong,
                                                         var_stx.check_BookContractLink, "HỢP ĐỒNG VẬN CHUYỂN HÀNH KHÁCH",
                                                         "_QuanLyXuatHoaDon_HopDong.png")

def caseid_accounting35(self):
    get_datachecklist("Accounting35")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_link_icon(self, "Accounting35", event, result, var_stx.icon_chitietcuoc,
                                                         var_stx.title_page1, "8.1.0 Báo cáo cuốc khách tổng",
                                                         "_QuanLyXuatHoaDon_ChiTietCuoc.png")

def caseid_accounting36(self):
    get_datachecklist("Accounting36")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_link_icon(self, "Accounting36", event, result, var_stx.icon_cuockhachgps,
                                                         var_stx.check_accounting_1_1, "HOTLINE MUA HÀNG", "_QuanLyXuatHoaDon_CuocKhachGPS.png")

def caseid_accounting37(self):
    get_datachecklist("Accounting37")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_link_icon(self, "Accounting37", event, result, var_stx.icon_lotrinhgps,
                                                         var_stx.icon_lotrinhgps, "", "_QuanLyXuatHoaDon_LotrinhGPS.png")

def caseid_accounting38(self):
    get_datachecklist("Accounting38")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.accounting_14_1_info_order(self, "Accounting38", event, result)


def caseid_accounting39(self):
    get_datachecklist("Accounting39")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting39", event, result, "0", "value", var_stx.info_order_serial_name,
                                                                var_stx.info_order_serial_data, "Serial:", "_ThongTinCuoc_Serial.png")

def caseid_accounting40(self):
    get_datachecklist("Accounting40")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting40", event, result, "0", "value", var_stx.info_order_phone_name,
                                                                var_stx.info_order_phone_data, "Số điện thoại:", "_ThongTinCuoc_SoDienThoai.png")

def caseid_accounting41(self):
    get_datachecklist("Accounting41")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting41", event, result, "0", "value",var_stx.info_order_namecustomer_name,
                                                                var_stx.info_order_namecustomer_data, "Tên khách hàng:", "_ThongTinCuoc_TenKhachHang.png")

def caseid_accounting42(self):
    get_datachecklist("Accounting42")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting42", event, result, "0", "value",var_stx.info_order_typecar_name,
                                                                var_stx.info_order_typecar_data, "Loại thẻ:", "_ThongTinCuoc_LoaiThe.png")

def caseid_accounting43(self):
    get_datachecklist("Accounting43")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting43", event, result, "0", "value", var_stx.info_order_namepartner_name,
                                                                var_stx.info_order_namepartner_data, "Tên đối tác:", "_ThongTinCuoc_TenDoiTac.png")

def caseid_accounting44(self):
    get_datachecklist("Accounting44")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting44", event, result, "0", "value",var_stx.info_order_codehd_name,
                                                                var_stx.info_order_codehd_data, "Mã hợp đồng:", "_ThongTinCuoc_MaHopDong.png")

def caseid_accounting45(self):
    get_datachecklist("Accounting45")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting45", event, result, "0", "value", var_stx.info_order_namecompany_name,
                                                                var_stx.info_order_namecompany_data, "Tên công ty:", "_ThongTinCuoc_TenCongTy.png")

def caseid_accounting46(self):
    get_datachecklist("Accounting46")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting46", event, result, "0", "value", var_stx.info_order_rankcar_name,
                                                                var_stx.info_order_rankcar_data, "Hạng thẻ:", "_ThongTinCuoc_HangThe.png")

def caseid_accounting47(self):
    get_datachecklist("Accounting47")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting47", event, result, "1", "value", var_stx.info_order_DisplayPublicBookId_name,
                                                                var_stx.info_order_DisplayPublicBookId_data, "Mã cuốc khách:", "_ThongTinCuoc_MaCuocKhach.png")

def caseid_accounting48(self):
    get_datachecklist("Accounting48")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting48", event, result, "0", "value", var_stx.info_order_CustName_name,
                                                                var_stx.info_order_CustName_data, "Khách hàng:", "_ThongTinCuoc_KhachHang.png")

def caseid_accounting49(self):
    get_datachecklist("Accounting49")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting49", event, result, "0", "value", var_stx.info_order_BookForName_name,
                                                                var_stx.info_order_BookForName_data, "Đặt hộ:", "_ThongTinCuoc_DatHo.png")

def caseid_accounting50(self):
    get_datachecklist("Accounting50")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting50", event, result, "1", "value", var_stx.info_order_CarType_name,
                                                                var_stx.info_order_CarType_data, "Loại xe:", "_ThongTinCuoc_LoaiXe.png")

def caseid_accounting51(self):
    get_datachecklist("Accounting51")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting51", event, result, "1", "value", var_stx.info_order_SentTime_name,
                                                                var_stx.info_order_SentTime_data, "Thời điểm cuốc đặt:", "_ThongTinCuoc_ThoiDiemCuocDat.png")

def caseid_accounting52(self):
    get_datachecklist("Accounting52")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting52", event, result, "0", "text", var_stx.info_order_FromAddress_name,
                                                                var_stx.info_order_FromAddress_data, "Điểm đón:", "_ThongTinCuoc_DienDon.png")

def caseid_accounting53(self):
    get_datachecklist("Accounting53")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting53", event, result, "0", "text", var_stx.info_order_ToAddress_name,
                                                                var_stx.info_order_ToAddress_data, "Điểm trả:", "_ThongTinCuoc_DienTra.png")

def caseid_accounting54(self):
    get_datachecklist("Accounting54")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting54", event, result, "0", "value", var_stx.info_order_Comment_name,
                                                                var_stx.info_order_Comment_data, "Ghi chú:", "_ThongTinCuoc_GhiChu.png")

def caseid_accounting55(self):
    get_datachecklist("Accounting55")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting55", event, result, "1", "value", var_stx.info_order_SourceType_name,
                                                                var_stx.info_order_SourceType_data, "Nguồn cuốc:", "_ThongTinCuoc_NguocCuoc.png")

def caseid_accounting56(self):
    get_datachecklist("Accounting56")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting56", event, result, "1", "value", var_stx.info_order_PartnerBookId_name,
                                                                var_stx.info_order_PartnerBookId_data, "Mã nguồn cuốc:", "_ThongTinCuoc_MaNguocCuoc.png")

def caseid_accounting57(self):
    get_datachecklist("Accounting57")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting57", event, result, "1", "value", var_stx.info_order_BookTripType_name,
                                                                var_stx.info_order_BookTripType_data, "Loại cuốc:", "_ThongTinCuoc_LoaiCuoc.png")

def caseid_accounting58(self):
    get_datachecklist("Accounting58")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting58", event, result, "1", "value", var_stx.info_order_PaymentMethodCust_name,
                                                                var_stx.info_order_PaymentMethodCust_data, "Phương thức thanh toán:", "_ThongTinCuoc_pttt.png")


def caseid_accounting59(self):
    get_datachecklist("Accounting59")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting59", event, result, "1", "value", var_stx.info_order_CatchedTime_name,
                                                                var_stx.info_order_CatchedTime_data, "Thời điểm gặp khách:", "_ThongTinCuoc_ThoiDiemGapKhach.png")

def caseid_accounting60(self):
    get_datachecklist("Accounting60")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting60", event, result, "1", "text", var_stx.info_order_FromAddress_name2,
                                                                var_stx.info_order_FromAddress_data2, "Địa chỉ đón:", "_ThongTinCuoc_DiaChiDon.png")

def caseid_accounting61(self):
    get_datachecklist("Accounting61")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting61", event, result, "1", "text", var_stx.info_order_ToAddress_name2,
                                                                var_stx.info_order_ToAddress_data2, "Địa chỉ trả:", "_ThongTinCuoc_DiaChiTra.png")

def caseid_accounting62(self):
    get_datachecklist("Accounting62")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting62", event, result, "1", "text", var_stx.info_order_bookState_name,
                                                                var_stx.info_order_bookState_data, "Trạng thái:", "_ThongTinCuoc_TrangThai.png")

def caseid_accounting63(self):
    get_datachecklist("Accounting63")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting63", event, result, "1", "value", var_stx.info_order_PrivateCode_name,
                                                                var_stx.info_order_PrivateCode_data, "Số hiệu:", "_ThongTinCuoc_SoHieu.png")

def caseid_accounting64(self):
    get_datachecklist("Accounting64")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting64", event, result, "1", "value", var_stx.info_order_VehiclePlate_name,
                                                                var_stx.info_order_VehiclePlate_data, "Biến số xe:", "_ThongTinCuoc_BienSoXe.png")

def caseid_accounting65(self):
    get_datachecklist("Accounting65")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting65", event, result, "1", "value", var_stx.info_order_CarTypeName_name,
                                                                var_stx.info_order_CarTypeName_data, "Loại xe:", "_ThongTinCuoc_LoaiXe.png")

def caseid_accounting66(self):
    get_datachecklist("Accounting66")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting66", event, result, "1", "value", var_stx.info_order_DriverCode_name,
                                                                var_stx.info_order_DriverCode_data, "Tài khoản tài xế:", "_ThongTinCuoc_TaiKhoanLaiXe.png")

def caseid_accounting67(self):
    get_datachecklist("Accounting67")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting67", event, result, "1", "value", var_stx.info_order_DriverName_name,
                                                                var_stx.info_order_DriverName_data, "Tên tài xế:", "_ThongTinCuoc_TenLaiXe.png")

def caseid_accounting68(self):
    get_datachecklist("Accounting68")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting68", event, result, "1", "value", var_stx.info_order_DriverPhone_name,
                                                                var_stx.info_order_DriverPhone_data, "Số điện thoại:", "_ThongTinCuoc_SoDienThoai.png")

def caseid_accounting69(self):
    get_datachecklist("Accounting69")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting69", event, result, "1", "value", var_stx.info_order_PaymentType_name,
                                                                var_stx.info_order_PaymentType_data, "Phương thức thanh toán:", "_ThongTinCuoc_pttt.png")

def caseid_accounting70(self):
    get_datachecklist("Accounting70")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting70", event, result, "1", "value", var_stx.info_order_BuyDate_name,
                                                                var_stx.info_order_BuyDate_data, "Thời điểm thanh toán:", "_ThongTinCuoc_ThoiDiemThanhToan.png")

def caseid_accounting71(self):
    get_datachecklist("Accounting71")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting71", event, result, "1", "value", var_stx.info_order_space_name,
                                                                var_stx.info_order_space_data, "Khoảng cách:", "_ThongTinCuoc_KhoangCach.png")

def caseid_accounting72(self):
    get_datachecklist("Accounting72")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting72", event, result, "1", "value", var_stx.info_order_TripPrice_name,
                                                                var_stx.info_order_TripPrice_data, "Cước phí (Cước thật):", "_ThongTinCuoc_CuocPhi.png")

def caseid_accounting73(self):
    get_datachecklist("Accounting73")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting73", event, result, "1", "value", var_stx.info_order_promotion_name,
                                                                var_stx.info_order_promotion_data, "Khuyến mại:", "_ThongTinCuoc_KhuyenMai.png")

def caseid_accounting74(self):
    get_datachecklist("Accounting74")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting74", event, result, "1", "value", var_stx.info_order_MoneyExtendFromDriver_name,
                                                                var_stx.info_order_MoneyExtendFromDriver_data, "Phụ phí:", "_ThongTinCuoc_PhuPhi.png")

def caseid_accounting75(self):
    get_datachecklist("Accounting75")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting75", event, result, "2", "value", var_stx.info_order_ChangeMoney_name,
                                                                var_stx.info_order_ChangeMoney_data, "KH thanh toán:", "_ThongTinCuoc_KhThanhToan.png")

def caseid_accounting76(self):
    get_datachecklist("Accounting76")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting76", event, result, "0", "value", var_stx.info_order_SaleOffCode_name,
                                                                var_stx.info_order_SaleOffCode_data, "Mã khuyến mại:", "_ThongTinCuoc_MaKhuyenMai.png")

def caseid_accounting77(self):
    get_datachecklist("Accounting77")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting77", event, result, "0", "value", var_stx.info_order_PercentMN_name,
                                                                var_stx.info_order_PercentMN_data, "Tên khuyến mại:", "_ThongTinCuoc_TenKhuyenMai.png")

def caseid_accounting78(self):
    get_datachecklist("Accounting78")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order(self, "Accounting78", event, result, "3", "text", var_stx.info_order_DetailFee_name,
                                                                var_stx.info_order_DetailFee_data, "Chi tiết phụ phí:", "_ThongTinCuoc_ChiTietPhuPhi.png")


def caseid_accounting79(self):
    get_datachecklist("Accounting79")
    event = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_stx.readData(var_stx.path_luutamthoi, 'Sheet1', 43, 2))
    accounting.accounting_14_1.check_accounting_14_1_info_order_history(self, "Accounting79", event, result)









