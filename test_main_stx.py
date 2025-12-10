import time

import driver_wallet_stx
import module_other_stx
import login_stx
import report_stx
import var_stx
import unittest
import caseid_stx

import module_stx
import minitor_stx
import vehicle_driver_stx
import customer_stx



#pip install selenium==3.141.0
#git checkout -b feature-update-03122

class Test(unittest.TestCase):
    def test_run1(self):
        module_other_stx.clearData(var_stx.checklistpath, "Checklist", "", "", "")
        module_other_stx.clear_log()
        module_other_stx.delete_image()
        module_other_stx.timerun()
        module_stx.ModuleTest()
        module_stx.retest_casenone(self)
        module_stx.retest_casefail(self)
        module_other_stx.send_viber()
        #staxi_test1122



#
        # caseid_stx.caseid_login01(self)
        # caseid_stx.caseid_login02(self)
        # caseid_stx.caseid_login03(self)

        # caseid_stx.caseid_login06(self)
        # caseid_stx.caseid_login07(self)
        # caseid_stx.caseid_login08(self)
        # caseid_stx.caseid_login09(self)
        # caseid_stx.caseid_login10(self)
        # caseid_stx.caseid_login11(self)
        # caseid_stx.caseid_login12(self)



        #
        # caseid_stx.caseid_minitor01(self)
        # caseid_stx.caseid_minitor02(self)
        # caseid_stx.caseid_minitor03(self)
        # caseid_stx.caseid_minitor04(self)
        # caseid_stx.caseid_minitor05(self)
        # caseid_stx.caseid_minitor06(self)
        # caseid_stx.caseid_minitor07(self)
        # caseid_stx.caseid_minitor08(self)
        # caseid_stx.caseid_minitor09(self)
        # caseid_stx.caseid_minitor10(self)
        # caseid_stx.caseid_minitor11(self)
        # caseid_stx.caseid_minitor12(self)
        # caseid_stx.caseid_minitor13(self)
        # caseid_stx.caseid_minitor14(self)
        # caseid_stx.caseid_minitor15(self)
        # caseid_stx.caseid_minitor16(self)
        # caseid_stx.caseid_minitor17(self)
        # caseid_stx.caseid_minitor18(self)
        # caseid_stx.caseid_minitor19(self)
        # caseid_stx.caseid_minitor20(self)
        # caseid_stx.caseid_minitor21(self)

        # caseid_stx.caseid_minitor22(self)
        # caseid_stx.caseid_minitor23(self)
        # caseid_stx.caseid_minitor24(self)
        # caseid_stx.caseid_minitor25(self)
        # caseid_stx.caseid_minitor26(self)
        # caseid_stx.caseid_minitor27(self)
        # caseid_stx.caseid_minitor28(self)
        # caseid_stx.caseid_minitor29(self)
        # caseid_stx.caseid_minitor30(self)
        # caseid_stx.caseid_minitor31(self)
        # caseid_stx.caseid_minitor32(self)
        # caseid_stx.caseid_minitor33(self)
        # caseid_stx.caseid_minitor34(self)
        # caseid_stx.caseid_minitor35(self)
        # caseid_stx.caseid_minitor36(self)
        #
        #
        # caseid_stx.caseid_minitor37(self)
        # caseid_stx.caseid_minitor38(self)
        # caseid_stx.caseid_minitor39(self)
        # caseid_stx.caseid_minitor40(self)
        # caseid_stx.caseid_minitor41(self)
        # caseid_stx.caseid_minitor42(self)
        # caseid_stx.caseid_minitor43(self)
        # caseid_stx.caseid_minitor44(self)
        # caseid_stx.caseid_minitor45(self)
        # caseid_stx.caseid_minitor46(self)
        # caseid_stx.caseid_minitor47(self)
        # caseid_stx.caseid_minitor48(self)
        # caseid_stx.caseid_minitor49(self)
        # caseid_stx.caseid_minitor50(self)
        # caseid_stx.caseid_minitor51(self)
        # caseid_stx.caseid_minitor52(self)
        #
        # caseid_stx.caseid_minitor53(self)
        # caseid_stx.caseid_minitor54(self)
        # caseid_stx.caseid_minitor55(self)
        # caseid_stx.caseid_minitor56(self)
        # caseid_stx.caseid_minitor57(self)
        # caseid_stx.caseid_minitor58(self)
        # caseid_stx.caseid_minitor59(self)
        # caseid_stx.caseid_minitor60(self)
        # caseid_stx.caseid_minitor61(self)
        # caseid_stx.caseid_minitor62(self)
        #
        # caseid_stx.caseid_minitor63(self)
        # # caseid_stx.caseid_minitor64(self)
        # # caseid_stx.caseid_minitor65(self)
        # caseid_stx.caseid_minitor66(self)
        # caseid_stx.caseid_minitor67(self)
        # #
        # caseid_stx.caseid_minitor68(self)
        # caseid_stx.caseid_minitor69(self)
        # caseid_stx.caseid_minitor70(self)
        # caseid_stx.caseid_minitor71(self)
        # caseid_stx.caseid_minitor72(self)
        # caseid_stx.caseid_minitor73(self)
        # caseid_stx.caseid_minitor74(self)
        # caseid_stx.caseid_minitor75(self)
        # caseid_stx.caseid_minitor76(self)
        # caseid_stx.caseid_minitor77(self)
        # caseid_stx.caseid_minitor78(self)
        # caseid_stx.caseid_minitor79(self)
        # caseid_stx.caseid_minitor80(self)
        # #
        # caseid_stx.caseid_vehicle01(self)
        # # caseid_stx.caseid_vehicle02(self)
        # caseid_stx.caseid_vehicle03(self)
        # caseid_stx.caseid_vehicle04(self)
        # caseid_stx.caseid_vehicle05(self)
        # caseid_stx.caseid_vehicle06(self)
        # caseid_stx.caseid_vehicle07(self)
        # caseid_stx.caseid_vehicle08(self)
        # caseid_stx.caseid_vehicle09(self)
        # caseid_stx.caseid_vehicle10(self)
        # caseid_stx.caseid_vehicle11(self)
        # caseid_stx.caseid_vehicle12(self)
        # caseid_stx.caseid_vehicle13(self)
        # caseid_stx.caseid_vehicle14(self)
        # caseid_stx.caseid_vehicle15(self)
        # caseid_stx.caseid_vehicle16(self)
        # #
        # caseid_stx.caseid_vehicle17(self)
        # caseid_stx.caseid_vehicle18(self)
        # caseid_stx.caseid_vehicle19(self)
        # caseid_stx.caseid_vehicle20(self)
        # caseid_stx.caseid_vehicle21(self)
        # caseid_stx.caseid_vehicle22(self)
        # caseid_stx.caseid_vehicle23(self)
        # # caseid_stx.caseid_vehicle24(self)     #đang mất trường cam ai
        # # caseid_stx.caseid_vehicle25(self)     #đang mất trường cam ai
        # caseid_stx.caseid_vehicle26(self)
        # caseid_stx.caseid_vehicle27(self)
        # caseid_stx.caseid_vehicle28(self)
        # caseid_stx.caseid_vehicle29(self)
        # caseid_stx.caseid_vehicle30(self)

        # caseid_stx.caseid_vehicle31(self)
        # # caseid_stx.caseid_vehicle32(self)
        # caseid_stx.caseid_vehicle33(self)
        # caseid_stx.caseid_vehicle34(self)
        # caseid_stx.caseid_vehicle35(self)
        # caseid_stx.caseid_vehicle36(self)
        # caseid_stx.caseid_vehicle37(self)
        # caseid_stx.caseid_vehicle38(self)
        # caseid_stx.caseid_vehicle39(self)
        # caseid_stx.caseid_vehicle40(self)
        # caseid_stx.caseid_vehicle41(self)
        # caseid_stx.caseid_vehicle42(self)
        # caseid_stx.caseid_vehicle43(self)
        # caseid_stx.caseid_vehicle44(self)
        # caseid_stx.caseid_vehicle45(self)
        # caseid_stx.caseid_vehicle46(self)
        # caseid_stx.caseid_vehicle47(self)
        # caseid_stx.caseid_vehicle48(self)
        # caseid_stx.caseid_vehicle49(self)
        # caseid_stx.caseid_vehicle50(self)
        # caseid_stx.caseid_vehicle51(self)
        # caseid_stx.caseid_vehicle52(self)
        # caseid_stx.caseid_vehicle53(self)
        # caseid_stx.caseid_vehicle54(self)
        # caseid_stx.caseid_vehicle55(self)
        # caseid_stx.caseid_vehicle56(self)
        # caseid_stx.caseid_vehicle57(self)
        # caseid_stx.caseid_vehicle58(self)
        # caseid_stx.caseid_vehicle59(self)
        # caseid_stx.caseid_vehicle60(self)



        # caseid_stx.caseid_wallet01(self)
        # caseid_stx.caseid_wallet02(self)
        # caseid_stx.caseid_wallet03(self)
        # caseid_stx.caseid_wallet04(self)
        # caseid_stx.caseid_wallet05(self)
        # caseid_stx.caseid_wallet06(self)
        #
        # caseid_stx.caseid_wallet07(self)
        # caseid_stx.caseid_wallet08(self)
        # caseid_stx.caseid_wallet09(self)

        # caseid_stx.caseid_wallet10(self)
        # caseid_stx.caseid_wallet11(self)
        #
        # caseid_stx.caseid_wallet12(self)
        # caseid_stx.caseid_wallet13(self)
        #
        # caseid_stx.caseid_wallet14(self)
        # caseid_stx.caseid_wallet15(self)
        # caseid_stx.caseid_wallet16(self)
        # caseid_stx.caseid_wallet17(self)
        # caseid_stx.caseid_wallet18(self)
        # caseid_stx.caseid_wallet19(self)
        # caseid_stx.caseid_wallet20(self)
        # caseid_stx.caseid_wallet21(self)
        # caseid_stx.caseid_wallet22(self)
        # caseid_stx.caseid_wallet23(self)


        # caseid_stx.caseid_wallet24(self)
        # # caseid_stx.caseid_wallet25(self)
        # caseid_stx.caseid_wallet26(self)
        # # caseid_stx.caseid_wallet27(self)
        # caseid_stx.caseid_wallet28(self)
        # caseid_stx.caseid_wallet29(self)
        # caseid_stx.caseid_wallet30(self)
        # caseid_stx.caseid_wallet31(self)
        # caseid_stx.caseid_wallet32(self)
        # caseid_stx.caseid_wallet33(self)
        # # caseid_stx.caseid_wallet34(self)
        # caseid_stx.caseid_wallet35(self)
        # caseid_stx.caseid_wallet36(self)
        # caseid_stx.caseid_wallet37(self)
        # caseid_stx.caseid_wallet38(self)
        # caseid_stx.caseid_wallet39(self)
        # caseid_stx.caseid_wallet40(self)

        # caseid_stx.caseid_promotion01(self)
        # # caseid_stx.caseid_promotion02(self)   #đã bỏ
        # caseid_stx.caseid_promotion03(self)
        # #
        # caseid_stx.caseid_promotion04(self)
        # caseid_stx.caseid_promotion05(self)
        # caseid_stx.caseid_promotion05_1(self)
        # caseid_stx.caseid_promotion06(self)
        # caseid_stx.caseid_promotion07(self)
        # caseid_stx.caseid_promotion08(self)
        # caseid_stx.caseid_promotion09(self)
        # caseid_stx.caseid_promotion10(self)
        # caseid_stx.caseid_promotion11(self)
        # caseid_stx.caseid_promotion12(self)
        # caseid_stx.caseid_promotion13(self)
        # caseid_stx.caseid_promotion14(self)


        # caseid_stx.caseid_promotion15(self)
        # caseid_stx.caseid_promotion16(self)
        # caseid_stx.caseid_promotion17(self)
        # caseid_stx.caseid_promotion18(self)
        # caseid_stx.caseid_promotion19(self)
        # caseid_stx.caseid_promotion20(self)
        # caseid_stx.caseid_promotion21(self)

        # caseid_stx.caseid_promotion22(self)
        # caseid_stx.caseid_promotion23(self)
        # caseid_stx.caseid_promotion24(self)
        # caseid_stx.caseid_promotion25(self)


        # caseid_stx.caseid_promotion26(self)
        # caseid_stx.caseid_promotion27(self)
        # caseid_stx.caseid_promotion28(self)
        # caseid_stx.caseid_promotion29(self)
        # caseid_stx.caseid_promotion30(self)
        # caseid_stx.caseid_promotion31(self)


        # caseid_stx.caseid_promotion32(self)
        # caseid_stx.caseid_promotion33(self)
        # caseid_stx.caseid_promotion34(self)
        # #
        # caseid_stx.caseid_promotion35(self)
        # caseid_stx.caseid_promotion36(self)
        # caseid_stx.caseid_promotion37(self)

        # caseid_stx.caseid_promotion38(self)
        # caseid_stx.caseid_promotion39(self)
        # caseid_stx.caseid_promotion40(self)

        # caseid_stx.caseid_promotion41(self)
        # caseid_stx.caseid_promotion42(self)
        # caseid_stx.caseid_promotion43(self)
        #
        # caseid_stx.caseid_promotion44(self)
        # caseid_stx.caseid_promotion45(self)
        # caseid_stx.caseid_promotion46(self)
        #
        # caseid_stx.caseid_promotion47(self)
        # caseid_stx.caseid_promotion48(self)
        # caseid_stx.caseid_promotion49(self)
        #
        #
        # caseid_stx.caseid_promotion50(self)
        # caseid_stx.caseid_promotion51(self)
        # caseid_stx.caseid_promotion52(self)
        #
        # caseid_stx.caseid_promotion53(self)
        # caseid_stx.caseid_promotion54(self)
        # caseid_stx.caseid_promotion55(self)

        # caseid_stx.caseid_promotion56(self)
        # caseid_stx.caseid_promotion57(self)
        # caseid_stx.caseid_promotion58(self)


        # caseid_stx.caseid_promotion59(self)
        # caseid_stx.caseid_promotion60(self)
        # caseid_stx.caseid_promotion61(self)
        # caseid_stx.caseid_promotion62(self)


        # caseid_stx.caseid_promotion63(self)
        # caseid_stx.caseid_promotion64(self)
        # caseid_stx.caseid_promotion65(self)
        # caseid_stx.caseid_promotion66(self)

        # caseid_stx.caseid_customer01(self)
        # caseid_stx.caseid_customer02(self)
        # caseid_stx.caseid_customer03(self)
        # caseid_stx.caseid_customer04(self)
        # caseid_stx.caseid_customer05(self)
        # caseid_stx.caseid_customer06(self)
        # caseid_stx.caseid_customer07(self)
        # caseid_stx.caseid_customer08(self)
        #
        # caseid_stx.caseid_customer09(self)
        # caseid_stx.caseid_customer10(self)
        # caseid_stx.caseid_customer11(self)
        # caseid_stx.caseid_customer12(self)
        # caseid_stx.caseid_customer13(self)
        # caseid_stx.caseid_customer14(self)
        # caseid_stx.caseid_customer15(self)
        # caseid_stx.caseid_customer16(self)
        # caseid_stx.caseid_customer17(self)
        # caseid_stx.caseid_customer17_1(self)

        # caseid_stx.caseid_customer18(self)
        # caseid_stx.caseid_customer19(self)
        # caseid_stx.caseid_customer20(self)
        # caseid_stx.caseid_customer21(self)
        # caseid_stx.caseid_customer22(self)
        # caseid_stx.caseid_customer23(self)
        # caseid_stx.caseid_customer24(self)

        #
        # caseid_stx.caseid_customer25(self)
        # caseid_stx.caseid_customer26(self)
        # caseid_stx.caseid_customer26_1(self)
        # caseid_stx.caseid_customer26_2(self)
        # caseid_stx.caseid_customer27(self)
        # caseid_stx.caseid_customer28(self)
        # caseid_stx.caseid_customer29(self)
        # caseid_stx.caseid_customer30(self)
        # caseid_stx.caseid_customer31(self)


        # caseid_stx.caseid_customer32(self)
        # caseid_stx.caseid_customer33(self)
        # caseid_stx.caseid_customer34(self)
        # caseid_stx.caseid_customer35(self)
        # caseid_stx.caseid_customer36(self)
        # caseid_stx.caseid_customer37(self)
        # caseid_stx.caseid_customer38(self)
        # caseid_stx.caseid_customer39(self)
        # caseid_stx.caseid_customer40(self)
        # caseid_stx.caseid_customer41(self)
        # caseid_stx.caseid_customer42(self)
        # caseid_stx.caseid_customer43(self)
        # caseid_stx.caseid_customer44(self)
        # caseid_stx.caseid_customer45(self)
        # caseid_stx.caseid_customer46(self)
        # caseid_stx.caseid_customer47(self)
        # caseid_stx.caseid_customer48(self)
        # caseid_stx.caseid_customer49(self)
        # caseid_stx.caseid_customer50(self)
        # caseid_stx.caseid_customer51(self)
        # caseid_stx.caseid_customer52(self)
        # caseid_stx.caseid_customer53(self)
        # # caseid_stx.caseid_customer54(self)
        # # caseid_stx.caseid_customer55(self)
        # caseid_stx.caseid_customer56(self)
        # caseid_stx.caseid_customer57(self)
        # caseid_stx.caseid_customer57_1(self)
        # caseid_stx.caseid_customer57_2(self)
        # caseid_stx.caseid_customer57_3(self)
        # caseid_stx.caseid_customer57_4(self)
        # caseid_stx.caseid_customer57_5(self)


        # caseid_stx.caseid_customer58(self)
        # caseid_stx.caseid_customer59(self)
        # caseid_stx.caseid_customer60(self)
        # caseid_stx.caseid_customer61(self)
        # caseid_stx.caseid_customer62(self)
        # caseid_stx.caseid_customer63(self)
        # caseid_stx.caseid_customer64(self)
        # caseid_stx.caseid_customer65(self)
        # caseid_stx.caseid_customer66(self)
        # caseid_stx.caseid_customer67(self)

        # caseid_stx.caseid_customer68(self)
        # caseid_stx.caseid_customer69(self)
        # caseid_stx.caseid_customer70(self)
        # caseid_stx.caseid_customer71(self)
        #
        # caseid_stx.caseid_customer72(self)
        # caseid_stx.caseid_customer73(self)
        # caseid_stx.caseid_customer74(self)
        #
        # caseid_stx.caseid_customer75(self)
        # caseid_stx.caseid_customer76(self)
        # caseid_stx.caseid_customer77(self)
        # caseid_stx.caseid_customer77_1(self)
        #
        # caseid_stx.caseid_customer78(self)
        # caseid_stx.caseid_customer79(self)
        # caseid_stx.caseid_customer80(self)
        #
        # caseid_stx.caseid_customer81(self)
        # caseid_stx.caseid_customer82(self)
        # caseid_stx.caseid_customer83(self)
        # #
        # caseid_stx.caseid_customer84(self)
        # caseid_stx.caseid_customer85(self)
        #
        # caseid_stx.caseid_customer86(self)
        # caseid_stx.caseid_customer87(self)
        # caseid_stx.caseid_customer88(self)
        # caseid_stx.caseid_customer89(self)

        # customer_stx.contract_card.check_card_after(self, 2)
        # customer_stx.contract_card.card_after5(self, "", "", "")




        # caseid_stx.caseid_customer90(self)
        # caseid_stx.caseid_customer91(self)


        # caseid_stx.caseid_report01(self)
        # caseid_stx.caseid_report02(self)
        # caseid_stx.caseid_report03(self)
        # caseid_stx.caseid_report04(self)
        #
        # caseid_stx.caseid_report05(self)
        # caseid_stx.caseid_report06(self)
        # caseid_stx.caseid_report07(self)
        # caseid_stx.caseid_report07_1(self)
        # caseid_stx.caseid_report07_2(self)



        #
        # caseid_stx.caseid_report08(self)
        # caseid_stx.caseid_report09(self)
        # caseid_stx.caseid_report10(self)

        # caseid_stx.caseid_report11(self)
        # caseid_stx.caseid_report12(self)
        # caseid_stx.caseid_report13(self)
        #
        # caseid_stx.caseid_report14(self)
        # caseid_stx.caseid_report15(self)
        # caseid_stx.caseid_report16(self)
        #
        # caseid_stx.caseid_report17(self)
        # caseid_stx.caseid_report18(self)
        # caseid_stx.caseid_report19(self)
        #
        # caseid_stx.caseid_report20(self)
        # caseid_stx.caseid_report21(self)
        # caseid_stx.caseid_report22(self)
        # #
        # caseid_stx.caseid_report23(self)
        # caseid_stx.caseid_report24(self)
        # caseid_stx.caseid_report25(self)
        #
        # caseid_stx.caseid_report26(self)
        # caseid_stx.caseid_report27(self)
        # caseid_stx.caseid_report28(self)

        # caseid_stx.caseid_report29(self)
        # caseid_stx.caseid_report30(self)
        # caseid_stx.caseid_report31(self)

        # caseid_stx.caseid_report32(self)
        # caseid_stx.caseid_report33(self)
        # caseid_stx.caseid_report34(self)
        #
        # caseid_stx.caseid_report35(self)
        # caseid_stx.caseid_report36(self)
        # caseid_stx.caseid_report37(self)

        # caseid_stx.caseid_report38(self)
        # caseid_stx.caseid_report39(self)
        # caseid_stx.caseid_report40(self)

        # caseid_stx.caseid_report41(self)
        # caseid_stx.caseid_report42(self)
        # caseid_stx.caseid_report43(self)
        #
        # caseid_stx.caseid_report44(self)
        # caseid_stx.caseid_report45(self)
        # caseid_stx.caseid_report46(self)
        #
        # caseid_stx.caseid_report47(self)
        # caseid_stx.caseid_report48(self)
        # caseid_stx.caseid_report49(self)
        #
        # caseid_stx.caseid_report50(self)
        # caseid_stx.caseid_report51(self)
        # caseid_stx.caseid_report52(self)
        # caseid_stx.caseid_report53(self)
        #
        # caseid_stx.caseid_report54(self)
        # caseid_stx.caseid_report55(self)
        # caseid_stx.caseid_report56(self)
        #
        # caseid_stx.caseid_report57(self)
        # caseid_stx.caseid_report58(self)
        # caseid_stx.caseid_report59(self)
        #
        # caseid_stx.caseid_report60(self)
        # caseid_stx.caseid_report61(self)
        # caseid_stx.caseid_report62(self)

        # caseid_stx.caseid_report63(self)
        # caseid_stx.caseid_report64(self)
        # caseid_stx.caseid_report65(self)
        #
        # caseid_stx.caseid_report66(self)
        # caseid_stx.caseid_report67(self)
        # caseid_stx.caseid_report68(self)
        #
        # caseid_stx.caseid_report69(self)
        # caseid_stx.caseid_report70(self)
        # caseid_stx.caseid_report71(self)

        # caseid_stx.caseid_report72(self)
        # caseid_stx.caseid_report73(self)
        # caseid_stx.caseid_report74(self)

        # caseid_stx.caseid_report75(self)
        # caseid_stx.caseid_report76(self)
        # caseid_stx.caseid_report77(self)
        # caseid_stx.caseid_report77_1(self)
        # caseid_stx.caseid_report77_2(self)




        # caseid_stx.caseid_report78(self)
        # caseid_stx.caseid_report79(self)
        # caseid_stx.caseid_report80(self)





        # caseid_stx.caseid_admin01(self)
        # caseid_stx.caseid_admin02(self)
        # caseid_stx.caseid_admin03(self)

        # caseid_stx.caseid_admin04(self)
        # caseid_stx.caseid_admin05(self)
        # caseid_stx.caseid_admin06(self)
        # caseid_stx.caseid_admin07(self)
        # caseid_stx.caseid_admin08(self)

        # caseid_stx.caseid_admin09(self)
        # caseid_stx.caseid_admin10(self)
        # caseid_stx.caseid_admin11(self)
        # caseid_stx.caseid_admin12(self)
        # caseid_stx.caseid_admin13(self)

        # caseid_stx.caseid_admin14(self)
        # caseid_stx.caseid_admin15(self)
        # caseid_stx.caseid_admin16(self)
        # caseid_stx.caseid_admin17(self)
        #
        # caseid_stx.caseid_admin18(self)
        # caseid_stx.caseid_admin19(self)
        # caseid_stx.caseid_admin20(self)


        # caseid_stx.caseid_admin21(self)
        # caseid_stx.caseid_admin22(self)
        # caseid_stx.caseid_admin23(self)
        # #
        # caseid_stx.caseid_admin24(self)
        # caseid_stx.caseid_admin25(self)
        # caseid_stx.caseid_admin26(self)
        # caseid_stx.caseid_admin27(self)
        # caseid_stx.caseid_admin28(self)
        # caseid_stx.caseid_admin29(self)
        # caseid_stx.caseid_admin30(self)
        # caseid_stx.caseid_admin31(self)
        # caseid_stx.caseid_admin32(self)

        # caseid_stx.caseid_admin33(self)
        # caseid_stx.caseid_admin34(self)
        # caseid_stx.caseid_admin35(self)
        # caseid_stx.caseid_admin36(self)
        # caseid_stx.caseid_admin37(self)
        # caseid_stx.caseid_admin38(self)
        # caseid_stx.caseid_admin39(self)


        # caseid_stx.caseid_admin40(self)
        # caseid_stx.caseid_admin41(self)
        #
        # caseid_stx.caseid_admin42(self)
        # caseid_stx.caseid_admin43(self)
        #
        # caseid_stx.caseid_admin44(self)
        # caseid_stx.caseid_admin45(self)
        #
        # caseid_stx.caseid_admin46(self)
        # caseid_stx.caseid_admin47(self)
        #
        # caseid_stx.caseid_admin48(self)
        # caseid_stx.caseid_admin49(self)
        #
        # caseid_stx.caseid_admin50(self)
        # caseid_stx.caseid_admin51(self)
        #
        # caseid_stx.caseid_admin52(self)
        # caseid_stx.caseid_admin53(self)
        #
        # caseid_stx.caseid_admin54(self)
        #
        # caseid_stx.caseid_admin55(self)
        # caseid_stx.caseid_admin56(self)
        #
        # caseid_stx.caseid_admin57(self)
        # caseid_stx.caseid_admin58(self)
        #
        # caseid_stx.caseid_admin59(self)
        # caseid_stx.caseid_admin60(self)
        #
        # caseid_stx.caseid_admin61(self)
        # caseid_stx.caseid_admin62(self)
        # caseid_stx.caseid_admin63(self)
        # caseid_stx.caseid_admin64(self)
        # caseid_stx.caseid_admin65(self)
        # caseid_stx.caseid_admin66(self)
        # caseid_stx.caseid_admin67(self)
        # caseid_stx.caseid_admin68(self)
        # caseid_stx.caseid_admin69(self)
        # caseid_stx.caseid_admin70(self)
        # caseid_stx.caseid_admin71(self)
        # caseid_stx.caseid_admin72(self)
        # caseid_stx.caseid_admin73(self)
        # caseid_stx.caseid_admin74(self)
        # caseid_stx.caseid_admin75(self)
        # caseid_stx.caseid_admin76(self)
        # caseid_stx.caseid_admin77(self)
        # caseid_stx.caseid_admin78(self)
        # caseid_stx.caseid_admin79(self)
        # caseid_stx.caseid_admin80(self)
        # caseid_stx.caseid_admin81(self)


        # caseid_stx.caseid_admin82(self)
        # caseid_stx.caseid_admin83(self)
        # caseid_stx.caseid_admin84(self)
        # caseid_stx.caseid_admin85(self)
        # caseid_stx.caseid_admin86(self)
        # caseid_stx.caseid_admin87(self)
        # caseid_stx.caseid_admin88(self)
        # caseid_stx.caseid_admin89(self)
        # caseid_stx.caseid_admin90(self)
        # caseid_stx.caseid_admin91(self)
        # caseid_stx.caseid_admin92(self)
        # caseid_stx.caseid_admin93(self)
        # caseid_stx.caseid_admin93_1(self)
        # caseid_stx.caseid_admin94(self)

        # caseid_stx.caseid_admin95(self)
        # caseid_stx.caseid_admin96(self)
        # caseid_stx.caseid_admin97(self)
        # caseid_stx.caseid_admin98(self)

        # caseid_stx.caseid_admin99(self)
        # caseid_stx.caseid_admin100(self)
        # caseid_stx.caseid_admin101(self)
        # caseid_stx.caseid_admin102(self)

        # caseid_stx.caseid_admin103(self)
        # caseid_stx.caseid_admin104(self)
        # caseid_stx.caseid_admin105(self)


        # caseid_stx.caseid_admin106(self)
        # caseid_stx.caseid_admin107(self)
        # caseid_stx.caseid_admin108(self)
        # caseid_stx.caseid_admin109(self)
        # caseid_stx.caseid_admin110(self)
        # caseid_stx.caseid_admin111(self)

        # caseid_stx.caseid_admin112(self)
        # caseid_stx.caseid_admin113(self)
        # caseid_stx.caseid_admin114(self)
        # caseid_stx.caseid_admin115(self)
        # caseid_stx.caseid_admin116(self)
        #
        # caseid_stx.caseid_admin117(self)
        # caseid_stx.caseid_admin118(self)
        # caseid_stx.caseid_admin119(self)
        # caseid_stx.caseid_admin120(self)
        # caseid_stx.caseid_admin121(self)
        # caseid_stx.caseid_admin122(self)
        # caseid_stx.caseid_admin123(self)
        # caseid_stx.caseid_admin124(self)
        #
        #
        # caseid_stx.caseid_admin125(self)
        # caseid_stx.caseid_admin126(self)
        # caseid_stx.caseid_admin127(self)
        # caseid_stx.caseid_admin128(self)
        # caseid_stx.caseid_admin129(self)


        # caseid_stx.caseid_customer84(self)
        # caseid_stx.caseid_customer85(self)
        #
        # caseid_stx.caseid_customer86(self)
        # caseid_stx.caseid_customer87(self)
        # caseid_stx.caseid_customer88(self)
        # caseid_stx.caseid_customer89(self)
        # customer_stx.contract_card.check_card_after(self, 7)



        # caseid_stx.caseid_customer90(self)
        # caseid_stx.caseid_customer91(self)
        # caseid_stx.caseid_customer92(self)
        # caseid_stx.caseid_customer93(self)



        # caseid_stx.caseid_PartnerTrip01(self)
        # caseid_stx.caseid_PartnerTrip02(self)
        # caseid_stx.caseid_PartnerTrip03(self)

        # caseid_stx.caseid_PartnerTrip04(self)
        # caseid_stx.caseid_PartnerTrip05(self)
        # caseid_stx.caseid_PartnerTrip06(self)



        # caseid_stx.caseid_accounting01(self)
        # caseid_stx.caseid_accounting02(self)
        # caseid_stx.caseid_accounting03(self)
        # caseid_stx.caseid_accounting04(self)
        # caseid_stx.caseid_accounting05(self)
        # caseid_stx.caseid_accounting06(self)
        # caseid_stx.caseid_accounting07(self)
        # caseid_stx.caseid_accounting08(self)
        # caseid_stx.caseid_accounting09(self)
        # caseid_stx.caseid_accounting10(self)
        # caseid_stx.caseid_accounting11(self)
        # caseid_stx.caseid_accounting12(self)
        # caseid_stx.caseid_accounting13(self)
        # caseid_stx.caseid_accounting14(self)
        # caseid_stx.caseid_accounting15(self)
        # caseid_stx.caseid_accounting16(self)
        # caseid_stx.caseid_accounting17(self)
        # caseid_stx.caseid_accounting18(self)
        #
        # caseid_stx.caseid_accounting19(self)
        # caseid_stx.caseid_accounting20(self)
        # caseid_stx.caseid_accounting21(self)
        # caseid_stx.caseid_accounting22(self)
        # caseid_stx.caseid_accounting23(self)
        # caseid_stx.caseid_accounting24(self)
        # caseid_stx.caseid_accounting25(self)

        # caseid_stx.caseid_accounting26(self)
        # caseid_stx.caseid_accounting27(self)
        # caseid_stx.caseid_accounting28(self)
        #
        # caseid_stx.caseid_accounting29(self)
        # caseid_stx.caseid_accounting30(self)
        # caseid_stx.caseid_accounting31(self)
        # caseid_stx.caseid_accounting32(self)
        #
        # caseid_stx.caseid_accounting33(self)
        # caseid_stx.caseid_accounting34(self)
        # caseid_stx.caseid_accounting35(self)
        # caseid_stx.caseid_accounting36(self)
        # caseid_stx.caseid_accounting37(self)
        #
        # caseid_stx.caseid_accounting38(self)
        # caseid_stx.caseid_accounting39(self)
        # caseid_stx.caseid_accounting40(self)
        # caseid_stx.caseid_accounting41(self)
        # caseid_stx.caseid_accounting42(self)
        # caseid_stx.caseid_accounting43(self)
        # caseid_stx.caseid_accounting44(self)
        # caseid_stx.caseid_accounting45(self)
        # caseid_stx.caseid_accounting46(self)
        # caseid_stx.caseid_accounting47(self)
        # caseid_stx.caseid_accounting48(self)
        # caseid_stx.caseid_accounting49(self)
        # caseid_stx.caseid_accounting50(self)
        # caseid_stx.caseid_accounting51(self)
        # caseid_stx.caseid_accounting52(self)
        # caseid_stx.caseid_accounting53(self)
        # caseid_stx.caseid_accounting54(self)
        # caseid_stx.caseid_accounting55(self)
        # caseid_stx.caseid_accounting56(self)
        # caseid_stx.caseid_accounting57(self)
        # caseid_stx.caseid_accounting58(self)
        # caseid_stx.caseid_accounting59(self)
        # caseid_stx.caseid_accounting60(self)
        # caseid_stx.caseid_accounting61(self)
        # caseid_stx.caseid_accounting62(self)
        # caseid_stx.caseid_accounting63(self)
        # caseid_stx.caseid_accounting64(self)
        # caseid_stx.caseid_accounting65(self)
        # caseid_stx.caseid_accounting66(self)
        # caseid_stx.caseid_accounting67(self)
        # caseid_stx.caseid_accounting68(self)
        # caseid_stx.caseid_accounting69(self)
        # caseid_stx.caseid_accounting70(self)
        # caseid_stx.caseid_accounting71(self)
        # caseid_stx.caseid_accounting72(self)
        # caseid_stx.caseid_accounting73(self)
        # caseid_stx.caseid_accounting74(self)
        # caseid_stx.caseid_accounting75(self)
        # caseid_stx.caseid_accounting76(self)
        # caseid_stx.caseid_accounting77(self)
        # caseid_stx.caseid_accounting78(self)
        #
        # caseid_stx.caseid_accounting79(self)

        # module_other_stx.write_caseif()

        # driver_wallet_stx.withdraw_money.run_tc(self)#tool rút tiền






if __name__ == "__main__":
    unittest.main()


# pyinstaller.exe --icon=C:\Users\truongtq.BA\PycharmProjects\pythonProject\ba_v2\icon_ba.ico .\test_main.py
# pyinstaller.exe --icon=C:\Users\truongtq.BA\PycharmProjects\pythonProject\ba_v2\tele.ico .\test_main.py




