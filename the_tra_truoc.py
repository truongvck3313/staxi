import time

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



#pip install selenium==3.141.0


class Test(unittest.TestCase):
    def test_run1(self):
        module_other_stx.clearData(var_stx.checklistpath, "Checklist", "", "", "")
        module_other_stx.clear_log()
        module_other_stx.delete_image()
        # module_stx.ModuleTest()
        # module_stx.retest_casenone(self)
        # module_stx.retest_casefail(self)
        # try:
        #     module_other_stx.notification_telegram()
        # except:
        #     pass



        caseid_stx.caseid_customer85_1(self)
        # customer_stx.contract_card.check_the_tra_truoc2(self, 2, "9999800010000046")




if __name__ == "__main__":
    unittest.main()