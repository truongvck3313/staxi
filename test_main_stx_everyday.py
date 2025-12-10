import time

import module_other_stx
import login_stx
import var_stx
import unittest
import caseid_stx

import module_stx
import minitor_stx
import vehicle_driver_stx


#a

class Test(unittest.TestCase):
    def test_run(self):
        day = 0
        while True:
            module_other_stx.timerun()
            day += 1
            module_other_stx.clearData(var_stx.checklistpath, "Checklist", "", "", "")
            module_other_stx.clear_log()
            module_other_stx.delete_image()
            module_other_stx.timerun()
            module_stx.ModuleTest()
            module_stx.retest_casenone(self)
            module_stx.retest_casefail(self)
            module_other_stx.send_viber()

            print("đang chạy ngày thứ n: ", day)
            if day == 7:
                module_other_stx.clear_log()
                day = 0


if __name__ == "__main__":
    unittest.main()

