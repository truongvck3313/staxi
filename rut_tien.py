import time

import driver_wallet_stx
import module_other_stx
import login_stx
import var_stx
import unittest
import caseid_stx
module_other_stx.timerun()
import module_stx
import minitor_stx
import vehicle_driver_stx
import customer_stx
from selenium.webdriver.common.keys import Keys


#pip install selenium==3.141.0


class Test(unittest.TestCase):
    def test_run1(self):
        module_other_stx.clear_log()
        driver_wallet_stx.withdraw_money.run_tc(self)#tool rút tiền





if __name__ == "__main__":
    unittest.main()


# pyinstaller.exe --icon=C:\Users\truongtq.BA\PycharmProjects\pythonProject\ba_v2\icon_ba.ico .\test_main.py
# pyinstaller.exe --icon=C:\Users\truongtq.BA\PycharmProjects\pythonProject\ba_v2\tele.ico .\test_main.py




