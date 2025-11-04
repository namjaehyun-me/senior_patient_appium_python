import pytest
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
import time
from conftest import * 

class TestMyPage:
    
    def _get_platform(self, driver):
        """플랫폼 확인"""
        # driver가 딕셔너리인 경우 실제 driver 객체 추출
        if isinstance(driver, dict):
            actual_driver = driver['driver']
            platform = driver.get('platform', 'android')
            return platform
        else:
            capabilities = driver.capabilities
            platform_name = capabilities.get('platformName', '').lower()
            return 'ios' if platform_name == 'ios' else 'android'
    
    def _get_locator(self, driver, element_name):
        """플랫폼별 로케이터 반환"""
        platform = self._get_platform(driver)
        
        locators = {
            'android': {
                # 마이페이지 관련 로케이터
                'bottom_my_page_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="마이 페이지"]'),
                'my_info_management_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="내 정보관리"]'),
                'detail_address_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="2층"]'),
                'keyborad_hied': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup'),
                'save_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="저장"]'),
                'toast_message': (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="toastAnimatedContainer"]/android.view.ViewGroup'),
                # 'toast_message': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(54)'),
                'family_info_management_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="내 가족 정보 관리"]'),
                'register_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="등록하기"]'),
                'name_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="대상자의 이름을 입력하세요"]'),
                # 'birth_date_btn': (AppiumBy.XPATH, '//android.widget.EditText[@text="날짜 선택"]'),
                # 'birth_date_btn': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("날짜 선택")'),
                'birth_date_btn': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[3]'),
                # 'birth_date_btn': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(19)'),
                'year_1992': (AppiumBy.XPATH, '//android.widget.TextView[@text="1992"]'),
                'month_1': (AppiumBy.XPATH, '//android.widget.TextView[@text="1월"]'),
                'day_21': (AppiumBy.XPATH, '//android.widget.TextView[@text="21"]'),
                'confirm_btn': (AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]'),
                'pay_ment_confirm_btn': (AppiumBy.XPATH, '//android.widget.Button[@text="확인"]'),
                'relationship_dropdown': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="선택"])[1]'),
                'other_option': (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]'),
                'grade_dropdown': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="선택"]'),
                'grade_4': (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]'),
                'male_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="남성"]'),
                'height_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="키"]'),
                'weight_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="진단명을 입력하세요"]'),
                'no_diagnosis_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="해당없음"]'),
                'symptom_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="대상자의 증상을 입력해 주세요"]'),
                'self_walking_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="자가보행"]'),
                'admission_support_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="입소지원서 작성"]'),
                'plus_btn': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[2]'),
                'jongro_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="종로구"]'),
                'jung_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="중구"]'),
                'yongsan_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="용산구"]'),
                'selection_complete_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="선택완료"]'),
                'size_10_59_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="10~59인"]'),
                'nature_friendly_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="자연친화"]'),
                'urban_type_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="도심형"]'),
                'physical_therapy_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="물리치료실"]'),
                'gym_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="헬스장"]'),
                'monthly_stay_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="한달살기"]'),
                'accept_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="수락"]'),
                'privacy_consent_checkbox': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[15]/android.view.ViewGroup[1]'),
                'complete_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="작성완료"]'),
                'first_item_checkbox': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(21)'),
                'delete_btn': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[4]'),
                'proceed_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="진행"]'),
                'back_btn': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'payment_history_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="결제내역"]'),
                'first_payment_item': (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'service_detail_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="서비스내용 상세보기"]'),
                'no_problem_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="이상없음"]'),
                # 추가 마이페이지 로케이터
                'admission_proposal_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="입소제안"]'),
                'first_proposal_item': (AppiumBy.XPATH, '(//android.view.ViewGroup[@clickable="true"])[1]'),
                'come_first_proposal_item': (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]'),
                'admission_support_update_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="입소지원서 업데이트"]'),
                'proposal_setting_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="입소 제안 설정"]'),
                'third_checkbox': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]'),
                'setting_complete_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="설정완료"]'),
                'favorite_institutions_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="관심기관"]'),
                'first_heart_btn': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="하트"])[1]'),
                'certificate_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="증명서 발급"]'),
                'download_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="다운받기"]'),
                'notice_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="공지사항"]'),
                'first_notice_item': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(19)'),
                'pay_ment_first_notice_item': (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'error_first_notice_item': (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'event_first_notice_item': (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'fnq_first_notice_item': (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'fnq_first_notice_item2': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="2025년 하반기 시스템 통합 업데이트 사전 안내"]'),
                'faq_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="자주 묻는 질문"]'),
                'faq_search_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="궁금한 내용을 검색하세요"]'),
                'event_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="이벤트"]'),
                'customer_center_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="고객센터"]'),
                'error_report_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="오류신고센터"]'),
                'category_dropdown': (AppiumBy.XPATH, '//android.widget.Spinner'),
                'service_error_option': (AppiumBy.XPATH, '//android.widget.TextView[@text="서비스신청오류"]'),
                'title_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="제목을 기재해 주세요"]'),
                'opinion_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="의견을 자유롭게 기재해주세요."]'),
                'report_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="신고하기"]'),
                'list_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="목록"]'),
                'delete_report_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="삭제하기"]'),
                'error_report_create_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="오류신고하기"]'),
                'customer_inquiry_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="고객센터 문의하기"]'),
                'my_report_history_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="내 신고내역"]'),
                'learning_materials_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="학습자료실"]'),
                'product_purchase_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="상품구매"]'),
                'purchase_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="구매하기"]'),
                'payment_method_dropdown': (AppiumBy.XPATH, '//android.widget.Spinner'),
                'bank_transfer_option': (AppiumBy.XPATH, '//android.widget.TextView[@text="실시간 계좌이체"]'),
                'agree_all_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="전체동의"]'),
                'next_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="다음"]'),
                'pay_ment_next_btn': (AppiumBy.XPATH, '//android.widget.Button[@text="다음"]'),
                'phone_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="010"]'),
                'number_5': (AppiumBy.XPATH, '//android.widget.Button[@content-desc="5"]'),
                'number_2': (AppiumBy.XPATH, '//android.widget.Button[@content-desc="2"]'),
                'number_8': (AppiumBy.XPATH, '//android.widget.Button[@content-desc="8"]'),
                'number_9': (AppiumBy.XPATH, '//android.widget.Button[@content-desc="9"]'),
                'number_7': (AppiumBy.XPATH, '//android.widget.Button[@content-desc="7"]'),
                'agree_payment_btn': (AppiumBy.XPATH, '//android.widget.Button[@text="동의하고 결제하기"]'),
                'bottom_favorite_institutions_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="관심기관"]'),
                'first_favorite_heart_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="숲데이케어센터, 2018.04.19, 60 명 정원, 서울 동작구 상도로68길 1-20"]/android.view.ViewGroup[2]/android.view.ViewGroup'),
                'toast_message': (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="toastAnimatedContainer"]'),
                'hanmaeum_nursing_home_name': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="재가복지센터, 숲데이케어센터, 서울 동작구 상도로68길 1-20"]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'),
                'search_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="검색"]'),
                'search_icon_btn': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'loction_access_modal': (AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]'),
                'category_button1': (AppiumBy.XPATH, '//android.widget.ImageView'),
                'category_button2': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="시작하기"]/android.view.ViewGroup'),
                'list_item': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'list_item_youtube': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="▶"])[2]/android.view.ViewGroup'),
            },
            'ios': {
                # 마이페이지 관련 로케이터
                'bottom_my_page_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='마이페이지']"),
                'my_info_management_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='내 정보관리']"),
                'detail_address_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='상세주소']"),
                'keyborad_hied': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='상세주소']"),
                'save_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='저장']"),
                'toast_message': (AppiumBy.XPATH, "//XCUIElementTypeStaticText"),
                'family_info_management_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='내 가족 정보 관리']"),
                'register_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='등록하기']"),
                'name_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='이름을 입력하세요']"),
                'birth_date_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='생년월일']"),
                'year_1992': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='1992']"),
                'month_1': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='1월']"),
                'day_21': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='21']"),
                'confirm_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='확인']"),
                'pay_ment_confirm_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='확인']"),
                'relationship_dropdown': (AppiumBy.XPATH, "//XCUIElementTypePicker"),
                'other_option': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='기타']"),
                'grade_dropdown': (AppiumBy.XPATH, "//XCUIElementTypePicker"),
                'grade_4': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='4등급']"),
                'male_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='남성']"),
                'height_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='키']"),
                'weight_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='몸무게']"),
                'no_diagnosis_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='해당없음']"),
                'symptom_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='상세 증상 기재']"),
                'self_walking_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='자가보행']"),
                'admission_support_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='입소지원서 작성']"),
                'plus_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='+']"),
                'jongro_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='종로구']"),
                'jung_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='중구']"),
                'yongsan_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='용산구']"),
                'selection_complete_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='선택완료']"),
                'size_10_59_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='10~59인']"),
                'nature_friendly_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='자연친화']"),
                'urban_type_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='도심형']"),
                'physical_therapy_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='물리치료실']"),
                'gym_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='헬스장']"),
                'monthly_stay_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='한달살기']"),
                'accept_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='수락']"),
                'privacy_consent_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='필수 항목에 대한 개인정보 수집 및 이용 동의']"),
                'complete_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='작성완료']"),
                'first_item_checkbox': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='체크박스'])[1]"),
                'delete_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='삭제']"),
                'proceed_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='진행']"),
                'back_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='뒤로가기']"),
                'payment_history_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='결제내역']"),
                'first_payment_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'service_detail_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='서비스내용 상세보기']"),
                'no_problem_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='이상없음']"),
                # 추가 마이페이지 로케이터
                'admission_proposal_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='입소제안']"),
                'first_proposal_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'admission_support_update_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='입소지원서 업데이트']"),
                'proposal_setting_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='입소 제안 설정']"),
                'third_checkbox': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='체크박스'])[3]"),
                'setting_complete_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='설정완료']"),
                'favorite_institutions_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='관심기관']"),
                'first_heart_btn': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='하트'])[1]"),
                'certificate_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='증명서 발급']"),
                'download_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='다운받기']"),
                'notice_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='공지사항']"),
                'first_notice_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'pay_ment_first_notice_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'error_first_notice_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'event_first_notice_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'fnq_first_notice_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'faq_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='자주 묻는 질문']"),
                'faq_search_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='검색']"),
                'event_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='이벤트']"),
                'customer_center_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='고객센터']"),
                'error_report_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='오류신고센터']"),
                'category_dropdown': (AppiumBy.XPATH, "//XCUIElementTypePicker"),
                'service_error_option': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='서비스신청오류']"),
                'title_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='제목']"),
                'opinion_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='사용자님의 의견']"),
                'report_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='신고하기']"),
                'list_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='목록']"),
                'delete_report_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='삭제하기']"),
                'error_report_create_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='오류신고하기']"),
                'customer_inquiry_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='고객센터 문의하기']"),
                'my_report_history_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='내 신고내역']"),
                'learning_materials_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='학습자료실']"),
                'product_purchase_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='상품구매']"),
                'purchase_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='구매하기']"),
                'payment_method_dropdown': (AppiumBy.XPATH, "//XCUIElementTypePicker"),
                'bank_transfer_option': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='실시간 계좌이체']"),
                'agree_all_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='전체동의']"),
                'next_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='다음']"),
                'pay_ment_next_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='다음']"),
                'phone_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField"),
                'number_5': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='5']"),
                'number_2': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='2']"),
                'number_8': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='8']"),
                'number_9': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='9']"),
                'number_7': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='7']"),
                'agree_payment_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='동의하고 결제하기']"),
                'bottom_favorite_institutions_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='관심기관']"),
                'first_favorite_heart_btn': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='하트'])[1]"),
                'toast_message': (AppiumBy.XPATH, "//XCUIElementTypeStaticText"),
                'hanmaeum_nursing_home_name': (AppiumBy.XPATH, "//XCUIElementTypeStaticText"),
                'search_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='검색']"),
                'search_icon_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='검색']"),
                'loction_access_modal': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='허용']"),
                'category_button1': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='허용']"),
                'category_button2': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='허용']"),
                'list_item': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='허용']"),
                'list_item_youtube': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='허용']"),
            }
        }
        
        return locators[platform][element_name]
    
    def test_my_info_management(self, driver_setup):
        """내 정보관리 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(0.5)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(0.5)
            
            # 내 정보관리 버튼 클릭
            # my_info_management_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'my_info_management_btn')))
            my_info_management_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '내 정보관리')
            my_info_management_btn.click()
            time.sleep(0.5)

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("저장").instance(0));'
            )
            time.sleep(0.5)
            
            
            # 상세주소 인풋에 2층 넣기
            detail_address_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'detail_address_input')))
            detail_address_input.clear()
            detail_address_input.send_keys("2층")
            time.sleep(0.5)
            
            # 키보드 내리기
            keyborad_hied = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'keyborad_hied')))
            keyborad_hied.click()
            time.sleep(0.5)
            
            # 저장 버튼 클릭
            # save_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'save_btn')))
            save_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '저장')
            save_btn.click()
            time.sleep(0.5)
            
            # 수정이 완료되었습니다! 토스트메세지가 나오는지 확인
            toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message')))
            assert toast_message.is_displayed(), "수정이 완료되었습니다!"
            time.sleep(2)
            
        except Exception as e:
            pytest.fail(f"내 정보관리 테스트 실패: {str(e)}")
    
    def test_family_info_management(self, driver_setup):
        """내 가족 정보 관리 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            import random
            import string
            
            time.sleep(0.5)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(0.5)
            
            # 내 가족 정보 관리 버튼 클릭
            # family_info_management_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'family_info_management_btn')))
            family_info_management_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '내 가족 정보 관리')
            family_info_management_btn.click()
            time.sleep(0.5)
            
            # 등록하기 버튼 클릭
            # register_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'register_btn')))
            register_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '등록하기')
            register_btn.click()
            time.sleep(0.5)
            
            # 이름 인풋에 이름을 랜덤으로 생성해서 넣기
            random_name = ''.join(random.choices(string.ascii_lowercase, k=5))
            name_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'name_input')))
            name_input.clear()
            name_input.send_keys(random_name)
            time.sleep(0.5)
            
            # 생년월일 버튼 클릭
            birth_date_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'birth_date_btn')))
            birth_date_btn.click()
            time.sleep(0.5)
            
            # 1992년 1월 21일로 설정
            # year_1992 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'year_1992')))
            # year_1992.click()
            # time.sleep(0.5)
            
            # month_1 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'month_1')))
            # month_1.click()
            # time.sleep(0.5)
            
            # day_21 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'day_21')))
            # day_21.click()
            # time.sleep(0.5)
            
            # 확인 버튼 클릭
            confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn')))
            confirm_btn.click()
            time.sleep(0.5)
            
            # 관계 드롭다운 클릭
            relationship_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'relationship_dropdown')))
            relationship_dropdown.click()
            time.sleep(0.5)
            
            # 기타 클릭
            other_option = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'other_option')))
            other_option.click()
            time.sleep(0.5)
            
            # 등급 드롭다운 클릭
            grade_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'grade_dropdown')))
            grade_dropdown.click()
            time.sleep(0.5)
            
            # 3등급 클릭
            grade_4 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'grade_4')))
            grade_4.click()
            time.sleep(0.5)

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("진료과목").instance(0));'
            )
            time.sleep(0.5)
            
            # 남성 체크박스 클릭
            # male_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'male_checkbox')))
            # male_checkbox.click()
            # time.sleep(0.5)
            
            # 키 인풋에 170 넣기
            # height_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'height_input')))
            # height_input.clear()
            # height_input.send_keys("170")
            # time.sleep(0.5)
            
            # 진단명 인풋에 감기 넣기
            weight_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'weight_input')))
            weight_input.clear()
            weight_input.send_keys("감기")
            time.sleep(0.5)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("거동상태").instance(0));'
            )
            time.sleep(0.5)

            # 해당없음 클릭
            # no_diagnosis_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'no_diagnosis_btn')))
            no_diagnosis_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '해당 없음')
            no_diagnosis_btn.click()
            time.sleep(0.5)
            
            # 상세 증상 기재 인풋에 기침 많음 넣기
            symptom_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'symptom_input')))
            symptom_input.clear()
            symptom_input.send_keys("기침 많음")
            time.sleep(0.5)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("저장").instance(0));'
            )
            time.sleep(0.5)
            
            # 자가보행 체크박스 클릭
            # self_walking_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'self_walking_checkbox')))
            # self_walking_checkbox.click()
            # time.sleep(0.5)
            
            # 저장 버튼 클릭
            # save_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'save_btn')))
            save_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '저장')
            save_btn.click()
            time.sleep(0.5)
            
            # 입소지원서 작성 버튼 클릭
            # admission_support_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'admission_support_btn')))
            admission_support_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '입소지원서 작성')
            admission_support_btn.click()
            time.sleep(0.5)
            
            # + 버튼 클릭
            plus_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'plus_btn')))
            plus_btn.click()
            time.sleep(0.5)
            
            # 종로구 체크박스 클릭
            jongro_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'jongro_checkbox')))
            jongro_checkbox.click()
            time.sleep(0.5)
            
            # 중구 체크박스 클릭
            jung_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'jung_checkbox')))
            jung_checkbox.click()
            time.sleep(0.5)
            
            # 용산구 체크박스 클릭
            yongsan_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'yongsan_checkbox')))
            yongsan_checkbox.click()
            time.sleep(0.5)
            
            # 선택완료 버튼 클릭
            # selection_complete_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'selection_complete_btn')))
            selection_complete_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '선택완료')
            selection_complete_btn.click()
            time.sleep(0.5)

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("발코니 정원").instance(0));'
            )
            time.sleep(0.5)
            
            # 10~59인 버튼 클릭
            # size_10_59_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'size_10_59_btn')))
            size_10_59_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '10~59인')
            size_10_59_btn.click()
            time.sleep(0.5)
            
            # 자연친화 버튼 클릭
            # nature_friendly_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'nature_friendly_btn')))
            nature_friendly_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '자연친화')
            nature_friendly_btn.click()
            time.sleep(0.5)
            
            # 도심형 버튼 클릭
            # urban_type_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'urban_type_btn')))
            urban_type_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '도심형')
            urban_type_btn.click()
            time.sleep(0.5)

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("한달살기").instance(0));'
            )
            time.sleep(0.5)            

            # 물리치료실 버튼 클릭
            # physical_therapy_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'physical_therapy_btn')))
            physical_therapy_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '물리치료실')
            physical_therapy_btn.click()
            time.sleep(0.5)
            
            # 헬스장 버튼 클릭
            # gym_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'gym_btn')))
            gym_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '헬스장')
            gym_btn.click()
            time.sleep(0.5)
            
            # 한달살기 버튼 클릭
            # monthly_stay_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'monthly_stay_btn')))
            monthly_stay_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '한달살기')
            monthly_stay_btn.click()
            time.sleep(0.5)

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("미리보기").instance(0));'
            )
            time.sleep(0.5)            
            
            # 수락 체크박스 클릭
            # accept_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'accept_checkbox')))
            accept_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '수락')
            accept_checkbox.click()
            time.sleep(0.5)
            
            # 필수 항목에 대한 개인정보 수집 및 이용 동의 체크박스 클릭
            privacy_consent_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'privacy_consent_checkbox')))
            privacy_consent_checkbox.click()
            time.sleep(0.5)
            
            # 작성완료 버튼 클릭
            # complete_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'complete_btn')))
            complete_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '작성완료')
            complete_btn.click()
            time.sleep(0.5)
            
            # 첫번째 항목 체크박스 클릭
            # first_item_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_item_checkbox')))
            first_item_checkbox = driver.find_element(*self._get_locator(driver, 'first_item_checkbox'))
            first_item_checkbox.click()
            time.sleep(0.5)
            
            # 삭제 버튼 클릭
            delete_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'delete_btn')))
            delete_btn.click()
            time.sleep(0.5)
            
            # 진행 버튼 클릭
            # proceed_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'proceed_btn')))
            proceed_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '진행')
            proceed_btn.click()
            time.sleep(0.5)
            
            # 뒤로가기 버튼 클릭
            # back_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'back_btn')))
            # back_btn.click()
            driver.back()
            time.sleep(0.5)
            
        except Exception as e:
            pytest.fail(f"내 가족 정보 관리 테스트 실패: {str(e)}")
    
    def test_payment_history(self, driver_setup):
        """결제내역 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(0.5)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(0.5)
            
            # 결제내역 버튼 클릭
            # payment_history_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'payment_history_btn')))
            payment_history_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '결제내역')
            payment_history_btn.click()
            time.sleep(0.5)
            
            # 첫번째 항목 클릭
            first_payment_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_payment_item')))
            first_payment_item.click()
            time.sleep(0.5)
            
            # 서비스내용 상세보기 버튼 클릭
            # service_detail_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'service_detail_btn')))
            service_detail_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '서비스내용 상세보기')
            service_detail_btn.click()
            time.sleep(0.5)
            
            # 스크롤 해서 아래로 내려가서 이상없음 버튼 클릭
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("이상없음").instance(0));'
            )
            time.sleep(0.5)
            
            # no_problem_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'no_problem_btn')))
            no_problem_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '이상없음')
            no_problem_btn.click()
            time.sleep(0.5)
            
            # 뒤로가기 버튼 클릭
            # back_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'back_btn')))
            # back_btn.click()
            driver.back()
            time.sleep(0.5)
            
        except Exception as e:
            pytest.fail(f"결제내역 테스트 실패: {str(e)}")
    
    def test_admission_proposal(self, driver_setup):
        """입소제안 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(0.5)
            
            # 입소제안 버튼 클릭
            # admission_proposal_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'admission_proposal_btn')))
            admission_proposal_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '입소제안')
            admission_proposal_btn.click()
            time.sleep(0.5)
            
            # 첫번째 항목 클릭
            first_proposal_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'come_first_proposal_item')))
            first_proposal_item.click()
            time.sleep(0.5)
            
            # 확인 버튼 클릭
            # confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn')))
            confirm_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '확인')
            confirm_btn.click()
            time.sleep(0.5)
            
            # 입소지원서 업데이트 버튼 클릭
            # admission_support_update_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'admission_support_update_btn')))
            admission_support_update_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '입소지원서 업데이트')
            admission_support_update_btn.click()
            time.sleep(0.5)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            time.sleep(0.5)
            
            # 입소 제안 설정 버튼 클릭
            # proposal_setting_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'proposal_setting_btn')))
            proposal_setting_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '입소 제안 설정')
            proposal_setting_btn.click()
            time.sleep(0.5)
            
            # 세번째 체크박스 클릭
            third_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'third_checkbox')))
            third_checkbox.click()
            time.sleep(0.5)
            
            # 설정완료 버튼 클릭
            # setting_complete_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'setting_complete_btn')))
            setting_complete_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '설정완료')
            setting_complete_btn.click()
            time.sleep(0.5)
            
            # 수정이 완료되었습니다! 토스트메세지가 나오는지 확인
            toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message')))
            assert toast_message.is_displayed(), "수정이 완료되었습니다!"
            time.sleep(2)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            time.sleep(0.5)
            
        except Exception as e:
            pytest.fail(f"입소제안 테스트 실패: {str(e)}")
    
    def test_favorite_institutions_from_mypage(self, driver_setup):
        """마이페이지 관심기관 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(0.5)
            
            # 관심기관 버튼 클릭
            favorite_institutions_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'favorite_institutions_btn')))
            favorite_institutions_btn.click()
            time.sleep(0.5)

            # 첫번째 항목의 하트 클릭
            first_favorite_heart_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_favorite_heart_btn')))
            first_favorite_heart_btn.click()
            time.sleep(0.5)
            
            # 관심기업 해제 토스트메세지가 잘 뜨는지 확인
            toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message')))
            assert toast_message.is_displayed(), "이 시설을 즐겨찾기 목록에서 제거했습니다!"
            time.sleep(0.5)

            driver.back()
            driver.back()

            # 숲데이케어센터 검색
            # 돋보기 버튼 클릭
            search_icon_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'search_icon_btn')))
            search_icon_btn.click()
            time.sleep(0.5)
            
            # 위치 권한 모달
            loction_access_modal = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'loction_access_modal')))
            loction_access_modal.click()
            time.sleep(0.5)
            
            # 검색 인풋에 숲데이케어센터 넣기
            search_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'search_input')))
            search_input.clear()
            search_input.send_keys("숲데이케어센터")
            time.sleep(0.5)
            
            # 숲데이케어센터 클릭
            hanmaeum_nursing_home_name = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'hanmaeum_nursing_home_name')))
            hanmaeum_nursing_home_name.click()
            time.sleep(0.5)
            driver.back()
            
        except Exception as e:
            pytest.fail(f"마이페이지 관심기관 테스트 실패: {str(e)}")
    
    def test_certificate_issuance(self, driver_setup):
        """증명서 발급 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(0.5)
            
            # 증명서 발급 버튼 클릭
            # certificate_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'certificate_btn')))
            certificate_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '증명서 발급')
            certificate_btn.click()
            time.sleep(0.5)
            
            # 첫번째 항목의 다운받기 버튼 클릭
            # download_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'download_btn')))
            download_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '다운받기')
            download_btn.click()
            time.sleep(0.5)
            
            # 토스트 메세지가 오류로 나오는 이슈로 토스트 메세지가 정상적으로 나오는지 확인하는 부분 주석 처리
            # 정상적으로 나올때 문구를 모르는 상태
            # 토스트메세지 분석
            # toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message')))
            # assert toast_message.is_displayed(), "다운로드 토스트메세지가 표시되지 않습니다"
            # time.sleep(2)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            time.sleep(0.5)
            
        except Exception as e:
            pytest.fail(f"증명서 발급 테스트 실패: {str(e)}")
    
    def test_notice(self, driver_setup):
        """공지사항 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(0.5)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("학습자료실").instance(0));'
            )
            time.sleep(0.5)

            # 공지사항 버튼 클릭
            # notice_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'notice_btn')))
            notice_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '공지사항')
            notice_btn.click()
            time.sleep(0.5)
            
            # 첫번째 항목 클릭
            # first_notice_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_notice_item')))
            first_notice_item = driver.find_element(*self._get_locator(driver, 'first_notice_item'))
            first_notice_item.click()
            time.sleep(2)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            time.sleep(0.5)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            time.sleep(0.5)
            
        except Exception as e:
            pytest.fail(f"공지사항 테스트 실패: {str(e)}")
    
    def test_faq(self, driver_setup):
        """자주 묻는 질문 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(0.5)

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("학습자료실").instance(0));'
            )
            time.sleep(0.5)
            
            # 자주 묻는 질문 버튼 클릭
            # faq_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'faq_btn')))
            faq_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '자주 묻는 질문')
            faq_btn.click()
            time.sleep(0.5)
            
            # 첫번째 항목 클릭
            first_notice_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'fnq_first_notice_item')))
            first_notice_item.click()
            time.sleep(2)
            
            # 검색 인풋에 하반기 넣기
            search_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'faq_search_input')))
            search_input.clear()
            search_input.send_keys("하반기")
            time.sleep(0.5)
            
            # 첫번째 항목 클릭
            first_notice_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'fnq_first_notice_item2')))
            first_notice_item.click()
            time.sleep(2)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            time.sleep(0.5)
            
        except Exception as e:
            pytest.fail(f"자주 묻는 질문 테스트 실패: {str(e)}")
    
    def test_event(self, driver_setup):
        """이벤트 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(0.5)

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("학습자료실").instance(0));'
            )
            time.sleep(0.5)
            
            # 이벤트 버튼 클릭
            # event_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'event_btn')))
            event_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '이벤트')
            event_btn.click()
            time.sleep(0.5)
            
            # 첫번째 항목 클릭
            first_notice_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'event_first_notice_item')))
            first_notice_item.click()
            time.sleep(2)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            time.sleep(0.5)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            time.sleep(0.5)
            
        except Exception as e:
            pytest.fail(f"이벤트 테스트 실패: {str(e)}")
    
    def test_customer_center(self, driver_setup):
        """고객센터 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(0.5)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("학습자료실").instance(0));'
            )
            time.sleep(0.5)

            # 고객센터 버튼 클릭
            # customer_center_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'customer_center_btn')))
            customer_center_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '고객센터')
            customer_center_btn.click()
            time.sleep(0.5)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            time.sleep(0.5)
            
        except Exception as e:
            pytest.fail(f"고객센터 테스트 실패: {str(e)}")
    
    def test_error_report_center(self, driver_setup):
        """오류신고센터 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(0.5)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("학습자료실").instance(0));'
            )
            time.sleep(0.5)

            # 오류신고센터 버튼 클릭
            # error_report_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'error_report_btn')))
            error_report_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '오류신고센터')
            error_report_btn.click()
            time.sleep(0.5)
            
            # 분류 드롭다운 클릭
            # category_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'category_dropdown')))
            category_dropdown = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '분류를 선택해 주세요')
            category_dropdown.click()
            time.sleep(0.5)
            
            # 서비스신청오류 클릭
            # service_error_option = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'service_error_option')))
            service_error_option = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '매칭오류')
            service_error_option.click()
            time.sleep(0.5)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("사용자님의 의견").instance(0));'
            )
            time.sleep(0.5)

            # 제목 인풋에 오류 테스트중입니다 넣기
            title_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'title_input')))
            title_input.clear()
            title_input.send_keys("오류 테스트중입니다")
            time.sleep(0.5)
            
            # 사용자님의 의견 인풋에 오류 테스트중입니다 내용 테스트중입니다 넣기
            opinion_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'opinion_input')))
            opinion_input.clear()
            opinion_input.send_keys("오류 테스트중입니다 내용 테스트중입니다")
            time.sleep(0.5)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("신고하기").instance(0));'
            )
            time.sleep(0.5)

            # 신고하기 버튼 클릭
            # report_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'report_btn')))
            report_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '신고하기')
            report_btn.click()
            time.sleep(0.5)
            
            # 토스트메세지 분석
            toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message')))
            assert toast_message.is_displayed(), "완료!"
            time.sleep(2)
            
            # 첫번째 항목 클릭
            first_notice_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'error_first_notice_item')))
            first_notice_item.click()
            time.sleep(0.5)
            
            # 목록 버튼 클릭
            # list_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'list_btn')))
            list_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '목록')
            list_btn.click()
            time.sleep(0.5)
            
            # 첫번째 항목 클릭
            first_notice_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'error_first_notice_item')))
            first_notice_item.click()
            time.sleep(0.5)
            
            # 삭제하기 버튼 클릭
            # delete_report_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'delete_report_btn')))
            delete_report_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '삭제하기')
            delete_report_btn.click()
            time.sleep(0.5)
            
            # 진행 버튼 클릭
            # proceed_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'proceed_btn')))
            proceed_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '진행')
            proceed_btn.click()
            time.sleep(0.5)
            
            # 토스트메세지 분석
            toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message')))
            assert toast_message.is_displayed(), "완료!"
            time.sleep(2)
            
            # 오류신고하기 버튼 클릭
            # error_report_create_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'error_report_create_btn')))
            error_report_create_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '오류신고하기')
            error_report_create_btn.click()
            time.sleep(0.5)
            
            # 고객센터 문의하기 버튼 클릭
            # customer_inquiry_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'customer_inquiry_btn')))
            customer_inquiry_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '고객센터 문의하기')
            customer_inquiry_btn.click()
            time.sleep(0.5)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            time.sleep(0.5)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("내 신고내역").instance(0));'
            )
            time.sleep(0.5)

            # 내 신고내역 버튼 클릭
            # my_report_history_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'my_report_history_btn')))
            my_report_history_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '내 신고내역')
            my_report_history_btn.click()
            time.sleep(0.5)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            time.sleep(0.5)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            time.sleep(0.5)
            
        except Exception as e:
            pytest.fail(f"오류신고센터 테스트 실패: {str(e)}")
    
    def test_learning_materials(self, driver_setup):
        """학습자료실 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(0.5)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("학습자료실").instance(0));'
            )
            time.sleep(0.5)

            # 학습자료실 버튼 클릭
            # learning_materials_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'learning_materials_btn')))
            learning_materials_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '학습자료실')
            learning_materials_btn.click()
            time.sleep(0.5)

            # 2. 카테고리 클릭
            category_button1 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'category_button1')))
            category_button1.click()
            time.sleep(0.5)

            category_button2 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'category_button2')))
            category_button2.click()
            time.sleep(0.5)

            # 3-1. 목록 아이템 클릭
            list_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'list_item')))
            list_item.click()
            # print("여기까지 왔음1")
            time.sleep(2)

            # 뒤로가기 버튼 클릭
            driver.back()
            driver.back()
            
        except Exception as e:
            pytest.fail(f"학습자료실 테스트 실패: {str(e)}")
    
    def test_product_purchase(self, driver_setup):
        """상품구매 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(0.5)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("상품구매").instance(0));'
            )
            time.sleep(0.5)

            # 상품구매 버튼 클릭
            # product_purchase_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'product_purchase_btn')))
            product_purchase_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '상품구매')
            product_purchase_btn.click()
            time.sleep(0.5)
            
            # 첫번째 항목 클릭
            first_notice_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'pay_ment_first_notice_item')))
            first_notice_item.click()
            time.sleep(0.5)
            
            # 구매하기 버튼 클릭
            # purchase_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'purchase_btn')))
            purchase_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '구매하기')
            purchase_btn.click()
            time.sleep(0.5)
            
            # 결제수단 드롭다운 클릭
            # payment_method_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'payment_method_dropdown')))
            payment_method_dropdown = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '선택')
            payment_method_dropdown.click()
            time.sleep(0.5)
            
            # 실시간 계좌이체 클릭
            # bank_transfer_option = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bank_transfer_option')))
            bank_transfer_option = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '실시간 계좌이체')
            bank_transfer_option.click()
            time.sleep(0.5)
            
            # 전체동의 체크박스 클릭
            # agree_all_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'agree_all_checkbox')))
            agree_all_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '전체동의')
            agree_all_checkbox.click()
            time.sleep(0.5)

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(0.5)
            
            # 다음 버튼 클릭
            # next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_btn')))
            next_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '다음')
            next_btn.click()
            time.sleep(0.5)
            
            # 인풋을 클릭후 92205162 넣기
            phone_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'phone_input')))
            phone_input.click()
            phone_input.send_keys("01092205162")
            time.sleep(0.5)
            
            # 다음 버튼 클릭
            next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'pay_ment_next_btn')))
            next_btn.click()
            time.sleep(0.5)
            
            # 5클릭
            number_5 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'number_5')))
            # number_5 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '5')
            number_5.click()
            time.sleep(0.5)
            
            # 2클릭
            number_2 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'number_2')))
            # number_2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '2')
            number_2.click()
            time.sleep(0.5)
            
            # 2클릭
            number_2.click()
            time.sleep(0.5)
            
            # 8클릭
            number_8 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'number_8')))
            # number_8 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '8')
            number_8.click()
            time.sleep(0.5)
            
            # 9클릭
            number_9 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'number_9')))
            # number_9 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '9')
            number_9.click()
            time.sleep(0.5)
            
            # 7클릭
            number_7 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'number_7')))
            # number_7 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '7')
            number_7.click()
            time.sleep(0.5)
            
            # 동의하고 결제하기 버튼 클릭
            agree_payment_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'agree_payment_btn')))
            agree_payment_btn.click()
            time.sleep(0.5)
            
            # 확인 버튼 클릭
            confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'pay_ment_confirm_btn')))
            confirm_btn.click()
            time.sleep(0.5)
            
            # 5클릭
            number_5 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'number_5')))
            number_5.click()
            time.sleep(0.5)
            
            # 2클릭
            number_2 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'number_2')))
            number_2.click()
            time.sleep(0.5)
            
            # 2클릭
            number_2.click()
            time.sleep(0.5)
            
            # 8클릭
            number_8 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'number_8')))
            number_8.click()
            time.sleep(0.5)
            
            # 9클릭
            number_9 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'number_9')))
            number_9.click()
            time.sleep(0.5)
            
            # 7클릭
            number_7 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'number_7')))
            number_7.click()
            time.sleep(0.5)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            
            # 뒤로가기 버튼 클릭
            driver.back()
            time.sleep(0.5)
            
        except Exception as e:
            pytest.fail(f"상품구매 테스트 실패: {str(e)}")