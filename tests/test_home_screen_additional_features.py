import pytest
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
import time
from conftest import * 

class TestHomeScreenAditionalFeatures:
    
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
                # TODO: Android 요소들 - 실제 요소 확인 후 수정 필요
                'visit_care_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="방문요양 찾기, 찾기"]'),
                # 'visit_care_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="방문요양 찾기"]'),
                'intro_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="소개보기"]'),
                'apply_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="방문요양서비스 신청하기"]'),
                'not_family_checkbox': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="아니오, 가족이 아닙니다."]'),
                'register_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="등록하기"]'),
                'location_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="장소 선택"]'),
                'address_input': (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="region_name"]'),
                'search_btn': (AppiumBy.XPATH, '//android.widget.Button[@text="검색"]'),
                'first_result': (AppiumBy.XPATH, '//android.widget.Button[@text="경기 가평군 가평읍 가화로 225-3 (S타운)"]'),
                'confirm_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="확인"]'),
                'confirm_btn2': (AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]'),
                'confirm_btn_2': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/button1")'),
                'confirm_btn3': (AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]'),
                'confirm_btn4': (AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]'),
                'confirm_btn5': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="확인"])[2]'),
                'next_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="다음"]'),
                'next_btn1': (AppiumBy.XPATH, '//android.widget.TextView[@text="다음"]'),
                'next_btn2': (AppiumBy.XPATH, '//android.widget.TextView[@text="다음"]'),
                'calendar_next': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup'),
                'calendar_date': (AppiumBy.XPATH, '//android.widget.TextView[@text="18"]'),
                # 'start_time_dropdown': (AppiumBy.XPATH, '//android.widget.EditText[@text="선택"]'),
                'start_time_dropdown': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]'),
                # 'time_11': (AppiumBy.XPATH, "//android.widget.TextView[@text='11:00']"),
                'duration_dropdown': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="선택"]'),
                'three_hours': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="3시간"]'),
                'load_info_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="정보 불러오기"]'),
                'kim_younghee': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="김영희, 1등급, 여성, 41세, 자가거동자가보행"]'),
                'gender_any': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="성별무관"]'),
                'no_proceed': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="진행안함"]'),
                'kind_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="친절함"]'),
                'agree_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="네, 동의합니다."]'),
                'auto_match_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="자동매칭"]'),
                'main_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="메인이동"]'),
                'back_btn1': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]'),
                'back_btn2': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup'),
                'back_btn3': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup'),
                'back_btn4': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]'),
                'ltc_facility_btn': (AppiumBy.XPATH, "//android.widget.TextView[@text='장기요양기관 찾기']"),
                'location_access': (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button"),
                'region_dropdown': (AppiumBy.XPATH, "//android.widget.Spinner"),
                'nationwide': (AppiumBy.XPATH, "//android.widget.TextView[@text='전국']"),
                'find_facility_btn': (AppiumBy.XPATH, "//android.widget.TextView[@text='시설 찾기']"),
                'second_heart_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="C, 요양원, 모두케어, 경기 구리시 동구릉로 427, 9061.25 km"]/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup'),
                'second_heart_btn_in': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup'),
                'toast_message': (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="toastAnimatedContainer"]/android.view.ViewGroup'),
                'second_item': (AppiumBy.XPATH, "(//android.widget.LinearLayout)[2]"),
                'consult_btn': (AppiumBy.XPATH, "//android.widget.TextView[@text='상담신청']"),
                'name_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="대상자의 이름을 입력하세요"]'),
                'grade_dropdown': (AppiumBy.XPATH, "//android.widget.Spinner"),
                'dementia_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="치매"]'),
                'female_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="여성"]'),
                'sms_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="문자"]'),
                'birth_year_dropdown': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="선택하세요"]'),
                'year_2024': (AppiumBy.XPATH, "//android.widget.TextView[@text='2024']"),
                'phone_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="연락처 번호를 입력하세요"]'),
                # 'consult_time_dropdown': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]'),
                # 'consult_time_dropdown': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]'),
                'consult_time_dropdown': (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().textContains("상담받기 편한 시간대")''.fromParent(new UiSelector().className("android.view.ViewGroup"))'),
                'send_btn': (AppiumBy.XPATH, "//android.widget.TextView[@text='보내기']"),
                'admission_support_btn': (AppiumBy.XPATH, "//android.widget.TextView[@text='입소지원']"),
                'hong_gildong_checkbox': (AppiumBy.XPATH, "//android.widget.CheckBox[@text='홍길동']"),
                'home_btn': (AppiumBy.XPATH, "//android.widget.TextView[@text='홈으로']"),
                'back_bth2': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'back_bth3': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]'),
                'back_btn4': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'back_btn5': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]'),
                'housekeeping_btn': (AppiumBy.XPATH, "//android.widget.TextView[@text='가사돌봄']"),
                'apply_housekeeping_btn': (AppiumBy.XPATH, "//android.widget.TextView[@text='가사돌봄서비스 신청하기']"),
                'service_checkbox1': (AppiumBy.XPATH, '//android.widget.TextView[@text="바닥청소"]'),
                'service_checkbox2': (AppiumBy.XPATH, '//android.widget.TextView[@text="설거지"]'),
                'service_checkbox3': (AppiumBy.XPATH, '//android.widget.TextView[@text="빨래 및 건조"]'),
                'service_checkbox4': (AppiumBy.XPATH, '//android.widget.TextView[@text="쓰레기 배출"]'),
                'service_checkbox5': (AppiumBy.XPATH, '//android.widget.TextView[@text="식사 준비 및 정리"]'),
                'under_18_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="18평 미만"]'),
                'under_1_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="1개 이하"]'),
                'alone_checkbox': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="독거"]'),
                'yes_checkbox_1': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="아니오"])[1]'),
                'yes_checkbox_2': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="예"])[2]'),
                'housekeeping_calendar_date': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="13"]/android.view.ViewGroup'),
                'housekeeping_start_time_dropdown': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[2]'),
                'duration_dropdown_housekeeping': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="30분"]'),
                'one_hour': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="1시간 30분"]'),
                # 간병인 관련 로케이터
                'caregiver_btn': (AppiumBy.XPATH, "//android.widget.TextView[@text='간병인']"),
                'caregiver_apply_btn': (AppiumBy.XPATH, "//android.widget.TextView[@text='간병인 신청하기']"),
                'term_care_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="기간제 간병 (24시간 옆에서 케어해 드립니다)"]'),
                # 'start_date_input': (AppiumBy.XPATH, '(//android.widget.EditText[@text="날짜 선택"])[1]'),
                'start_date_input': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("날짜 선택").instance(0)'),
                'year_2026': (AppiumBy.XPATH, "//android.widget.TextView[@text='2026']"),
                'month_10': (AppiumBy.XPATH, "//android.widget.TextView[@text='10월']"),
                'day_22': (AppiumBy.XPATH, "//android.widget.TextView[@text='22']"),
                'start_date_dropdown': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="선택"])[1]'),
                'time_16': (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'end_date_dropdown': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="선택"])[2]'),
                'home_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="집"]'),
                'detail_address_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="상세주소"]'),
                'surgery_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="수술"]'),
                'general_room_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="일반실"]'),
                'hourly_rate_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="시급을 입력하세요"]'),
                'caregiver_notice_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="간병 공고"]'),
                'no_problem_btn': (AppiumBy.XPATH, "//android.widget.TextView[@text='이상없음']"),
                'agree_caregiver_btn': (AppiumBy.XPATH, "//android.widget.TextView[@text='네, 동의합니다.']"),
                'register_caregiver_btn': (AppiumBy.XPATH, "//android.widget.TextView[@text='등록��기']"),
                'mony_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="시급 제안"]'),
                # 동행
                'hope_mony_input': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[6]'),
                'meeting_place_add_btn': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]'),
                'visit_place_add_btn': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup[1]'),
                'confirm_btn6': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="확인"])[1]'),
                'confirm_btn7': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="확인"]'),
                'same_return_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="복귀장소가 만남장소와 동일합니다."]'),
                'patient_location_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="예시) 서울시 강남구"]'),
                'pass_keyboard_btn': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup'),
                # 검색 관련 로케이터
                'search_icon_btn': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'loction_access_modal': (AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]'),
                'search_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="검색"]'),
                'hanmaeum_nursing_home_name': (AppiumBy.XPATH, '//android.widget.TextView[@text="한마음요양원"]'),
                'hanmaeum_nursing_home': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="요양원, 한마음요양원, 서울 강남구 개포로20길 31, 9078.96 km"]/android.view.ViewGroup'),
                'hanmaeum_heart_btn': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup'),
                'first_item_checkbox': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="2, 홍길동 (부), 남성, 56세, 4등급"]'),
                'search_confirm_btn': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="확인"])[2]'),
                # 'search_confirm_btn': (AppiumBy.XPATH, '(//android.widget.TextView[@text="확인"])[2]'),
                # 알림 관련 로케이터
                'notification_bell_btn': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]'),
                'first_notification_item': (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'notification_detail_content': (AppiumBy.XPATH, '//android.widget.TextView'),
                'notification_back_btn': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'first_notification_x_btn': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(22)'),
                'proceed_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="진행"]'),
                'notification_list_back_btn': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]'),
                # 햄버거 메뉴 관련 로케이터
                'hamburger_menu_btn': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]'),
                # 'hamburger_menu_btn': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(14)'),
                'menu_visit_care_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="방문요양 찾기"]'),
                'menu_companion_service_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="동행서비스"]'),
                'menu_caregiver_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="간병인 찾기"]'),
                'menu_ltc_facility_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="장기요양기관찾기"]'),
                'menu_housekeeping_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="가사돌봄"]'),
                'menu_my_info_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="내 정보 관리"]'),
                'menu_family_info_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="가족정보관리"]'),
                'menu_service_history_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="서비스 이용내역"]'),
                'menu_favorite_institutions_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="관심기관"]'),
                'menu_payment_management_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="결제관리"]'),
                'menu_certificate_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="증명서 발급"]'),
                'menu_notice_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="공지사항"]'),
                'menu_event_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="이벤트"]'),
                'menu_faq_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="자주 묻는 질문"]'),
                'menu_customer_center_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="고객센터"]'),
                'menu_suggestion_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="앱 기능 건의함"]'),
                'menu_notification_settings_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="알림설정"]'),
                'menu_back_btn': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]'),
            },
            'ios': {
                # TODO: iOS 요소들 - 실제 요소 확인 후 수정 필요
                'visit_care_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='방문요양찾기']"),
                'intro_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='소개보기']"),
                'apply_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='방문요양서비스 신청하기']"),
                'not_family_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@name,'아니오')]"),
                'register_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='등록하기']"),
                'location_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='장소 선택']"),
                'address_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField"),
                'search_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='검색']"),
                'first_result': (AppiumBy.XPATH, "(//XCUIElementTypeStaticText)[1]"),
                'confirm_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='확인']"),
                'next_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='다음']"),
                'calendar_next': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='다음']"),
                'start_time_dropdown': (AppiumBy.XPATH, "//XCUIElementTypePicker"),
                'time_11': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='11:00']"),
                'duration_dropdown': (AppiumBy.XPATH, "//XCUIElementTypePicker"),
                'three_hours': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='3시간']"),
                'load_info_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='정보불러오기']"),
                'kim_younghee': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='김영희']"),
                'gender_any': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='성별무관']"),
                'no_proceed': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='진행안함']"),
                'kind_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='친절함']"),
                'agree_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[contains(@name,'동의합니다')]"),
                'auto_match_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@name,'자동매칭')]"),
                'main_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='메인이동']"),
                'ltc_facility_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='장기요양기관 찾기']"),
                'region_dropdown': (AppiumBy.XPATH, "//XCUIElementTypePicker"),
                'nationwide': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='전국']"),
                'find_facility_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='시설 찾기']"),
                'second_heart_btn': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='하트'])[2]"),
                'toast_message': (AppiumBy.XPATH, "//XCUIElementTypeStaticText"),
                'second_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[2]"),
                'consult_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='상담신청']"),
                'name_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='이름']"),
                'grade_dropdown': (AppiumBy.XPATH, "//XCUIElementTypePicker"),
                'dementia_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='치매']"),
                'female_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='여성']"),
                'sms_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='문자']"),
                'birth_year_dropdown': (AppiumBy.XPATH, "//XCUIElementTypePicker"),
                'year_2024': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='2024']"),
                'phone_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='전화번호']"),
                'consult_time_dropdown': (AppiumBy.XPATH, "//XCUIElementTypePicker"),
                'send_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='보내기']"),
                'admission_support_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='입소지원']"),
                'hong_gildong_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='홍길동']"),
                'home_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='홈으로']"),
                'housekeeping_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='가사돌봄']"),
                'apply_housekeeping_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='가사돌봄서비스 신청하기']"),
                'under_18_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='18평 미만']"),
                'under_1_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='1개 이하']"),
                'alone_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='독거']"),
                'yes_checkbox_1': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='예'])[1]"),
                'yes_checkbox_2': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='예'])[2]"),
                'housekeeping_start_time_dropdown': (AppiumBy.XPATH, "//XCUIElementTypePicker"),
                'duration_dropdown_housekeeping': (AppiumBy.XPATH, "//XCUIElementTypePicker"),
                'one_hour': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='1시간']"),
                # 간병인 관련 로케이터
                'caregiver_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='간병인']"),
                'caregiver_apply_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='간병인 신청하기']"),
                'term_care_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='기간제 간병']"),
                'start_date_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='시작 날짜 설정']"),
                'year_2026': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='2026']"),
                'month_10': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='10월']"),
                'day_22': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='22']"),
                'time_16': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='16:00']"),
                'home_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='집']"),
                'detail_address_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='상세주소']"),
                'surgery_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='수술']"),
                'general_room_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='일반실']"),
                'hourly_rate_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='시급']"),
                'caregiver_notice_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='간병 공고']"),
                'no_problem_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='이상없음']"),
                'agree_caregiver_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='네, 동의합니다.']"),
                'register_caregiver_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='등록기']"),
                'mony_input': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='등록기']"),
                # 동행
                'hope_mony_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='희망 시급']"),
                'meeting_place_add_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='추가']"),
                'visit_place_add_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='추가']"),
                'confirm_btn6': (AppiumBy.XPATH, "(//XCUIElementTypeStaticText[@name='확인'])[1]"),
                'confirm_btn7': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='확인']"),
                'same_return_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@name,'동일합니다')]"),
                # 검색 관련 로케이터
                'search_icon_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='돋보기']"),
                'search_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='검색어를 입력하세요']"),
                'hanmaeum_nursing_home': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='한마음요양원']"),
                'hanmaeum_heart_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='하트']"),
                'first_item_checkbox': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='체크박스'])[1]"),
                'search_confirm_btn': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='체크박스'])[1]"),
                # 알림 관련 로케이터
                'notification_bell_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='종']"),
                'first_notification_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'notification_detail_content': (AppiumBy.XPATH, "//XCUIElementTypeStaticText"),
                'notification_back_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='뒤로가기']"),
                'first_notification_x_btn': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='삭제'])[1]"),
                'proceed_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='진행']"),
                'notification_list_back_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='뒤로가기']"),
                # 햄버거 메뉴 관련 로케이터
                'hamburger_menu_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='메뉴']"),
                'menu_visit_care_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='방문요양 찾기']"),
                'menu_companion_service_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='동행서비스']"),
                'menu_caregiver_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='간병인 찾기']"),
                'menu_ltc_facility_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='장기요양기관찾기']"),
                'menu_housekeeping_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='가사돌봄']"),
                'menu_my_info_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='내 정보 관리']"),
                'menu_family_info_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='가족정보관리']"),
                'menu_service_history_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='서비스 이용내역']"),
                'menu_favorite_institutions_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='관심기관']"),
                'menu_payment_management_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='결제관리']"),
                'menu_certificate_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='증명서 발급']"),
                'menu_notice_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='공지사항']"),
                'menu_event_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='이벤트']"),
                'menu_faq_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='자주 묻는 질문']"),
                'menu_customer_center_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='고객센터']"),
                'menu_suggestion_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='앱 기능 건의함']"),
                'menu_notification_settings_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='알림설정']"),
                'menu_back_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='뒤로가기']"),
            }
        }
        
        return locators[platform][element_name]
    
    def _get_date_locator(self, driver, day):
        """날짜별 로케이터 반환"""
        platform = self._get_platform(driver)
        if platform == 'android':
            return (AppiumBy.XPATH, f"//android.widget.TextView[@text='{day}']") 
        else:
            return (AppiumBy.XPATH, f"//XCUIElementTypeStaticText[@name='{day}']")
    
    def _get_checkbox_locator(self, driver, index):
        """체크박스 인덱스별 로케이터 반환"""
        platform = self._get_platform(driver)
        if platform == 'android':
            return (AppiumBy.XPATH, f"(//android.widget.CheckBox)[{index}]")
        else:
            return (AppiumBy.XPATH, f"(//XCUIElementTypeButton[@name='체크박스'])[{index}]")
    
    def _show_second_match(driver, text="선택하세요", max_swipes=8):
        size = driver.get_window_size()
        for _ in range(max_swipes):
            els = driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().textContains("{text}")')
            # 화면 안에 최소 2개가 보이면 종료
            if len(els) >= 2:
                return driver.swipe(size['width']//2, int(size['height']*0.8), size['width']//2, int(size['height']*0.2), 400)

    def test_search_and_nursing_home_registration(self, driver_setup):
        """검색 및 한마음요양원 등록 테스트"""
        # driver가 딕셔너리인 경우 실제 driver 객체 추출
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            # 홈 화면 진입 확인
            time.sleep(2)
            
            # 돋보기 버튼 클릭
            search_icon_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'search_icon_btn')))
            search_icon_btn.click()
            time.sleep(1)
            
            # 위치 권한 모달
            loction_access_modal = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'loction_access_modal')))
            loction_access_modal.click()
            time.sleep(1)
            
            # 검색 인풋에 한마음 넣기
            search_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'search_input')))
            search_input.clear()
            search_input.send_keys("한마음")
            time.sleep(1)
            
            # 한마음요양원 클릭
            hanmaeum_nursing_home_name = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'hanmaeum_nursing_home_name')))
            hanmaeum_nursing_home_name.click()
            time.sleep(1)
            

            hanmaeum_nursing_home_name = driver.find_elements(*self._get_locator(driver, 'hanmaeum_nursing_home_name'))
            print(f"검색된 한마음요양원 개수: {len(hanmaeum_nursing_home_name)}")
            # 한마음요양원 클릭
            if len(hanmaeum_nursing_home_name) == 1:
                time.sleep(0.5)
                
                hanmaeum_nursing_home = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'hanmaeum_nursing_home_name')))
                hanmaeum_nursing_home.click()
                time.sleep(1)

                # 한마음요양원 하트 클릭
                hanmaeum_heart_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'hanmaeum_heart_btn')))
                hanmaeum_heart_btn.click()
                time.sleep(1)

                # 스크롤해서 아래로 내려가서 상담신청 버튼 클릭
                driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                    '.scrollIntoView(new UiSelector().textContains("상담신청").instance(0));'
                )
                time.sleep(1)
                
                consult_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "상담신청")
                consult_btn.click()
                time.sleep(1)
                
                # 이름 인풋에 "김동라그미"라고 넣기
                name_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'name_input')))
                name_input.clear()
                name_input.send_keys("김동라그미")
                time.sleep(1)
                
                # 등급 드롭다운 클릭
                grade_dropdown = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "선택")
                grade_dropdown.click()
                time.sleep(1)
                
                # 1등급 클릭
                grade_1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1등급")
                grade_1.click()
                time.sleep(1)
                
                # 치매 체크박스 클릭
                dementia_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'dementia_checkbox')))
                dementia_checkbox.click()
                time.sleep(1)
                
                # 여성 체크박스 클릭
                female_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'female_checkbox')))
                female_checkbox.click()
                time.sleep(1)
                
                driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                    '.scrollIntoView(new UiSelector().textContains("선택하세요").instance(0));'
                )
                time.sleep(1)
                
                # 문자 체크박스 클릭
                sms_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'sms_checkbox')))
                sms_checkbox.click()
                time.sleep(1)
                
                # 어르신의 출생 연도 드롭다운 클릭
                birth_year_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'birth_year_dropdown')))
                birth_year_dropdown.click()
                time.sleep(1)
                
                # 2024 클릭
                year_2024 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "2024")
                year_2024.click()
                time.sleep(1)
                
                # 상담 받으실 전화번호 인풋에 "01092205162" 넣기
                phone_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'phone_input')))
                phone_input.clear()
                phone_input.send_keys("01092205162")
                time.sleep(1)
                
                try:
                    driver.find_element(
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                        '.scrollIntoView(new UiSelector().textContains("선택하세요").instance(1));'
                    )
                except:
                    driver.swipe(500, 1500, 500, 500, 1000)
                time.sleep(1)
                
                # 상담받기 편한 시간대 드롭다운 클릭
                try:
                    consult_time_dropdown = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("선택하세요").instance(1)')
                except:
                    consult_time_dropdown = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("선택하세요")')
                consult_time_dropdown.click()
                time.sleep(1)
                
                # 11:00로 시간 설정
                # time_11 = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='11:00']")
                # time_11.click()
                # time.sleep(1)
                
                # 확인 버튼 클릭
                confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn3')))
                confirm_btn.click()
                time.sleep(1)
                
                # 보내기 버튼 클릭
                send_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "보내기")
                send_btn.click()
                time.sleep(1)
                
                # 입소지원 버튼 클릭
                admission_support_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "입소지원")
                admission_support_btn.click()
                time.sleep(1)
                
                # 홍길동 항목 체크박스 클릭
                hong_gildong_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "2, 홍길동 (부), 남성, 56세, 4등급")
                hong_gildong_checkbox.click()
                time.sleep(1)
                
                driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                    '.scrollIntoView(new UiSelector().textContains("확인").instance(0));'
                )
                time.sleep(1)
                
                # 확인 버튼 클릭
                confirm_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
                confirm_btn.click()
                time.sleep(1)
                
                # 홈으로 버튼 클릭
                home_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'home_btn')))
                home_btn.click()
                time.sleep(1)
                
                # 돋보기 버튼 클릭
                search_icon_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'search_icon_btn')))
                search_icon_btn.click()
                time.sleep(1)
                
                # 검색 인풋에 한마음 넣기
                search_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'search_input')))
                search_input.clear()
                search_input.send_keys("한마음")
                time.sleep(1)
                
                # 한마음요양원 클릭
                hanmaeum_nursing_home_name = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'hanmaeum_nursing_home_name')))
                hanmaeum_nursing_home_name.click()
                time.sleep(1)
                
                driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                    '.scrollIntoView(new UiSelector().textContains("입소지원").instance(0));'
                )
                time.sleep(1)
                
                # 입소지원 버튼 클릭
                admission_support_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "입소지원")
                admission_support_btn.click()
                time.sleep(1)
                
                # 첫번째 항목 체크박스 클릭
                first_item_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_item_checkbox')))
                first_item_checkbox.click()
                time.sleep(1)
                
                driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                    '.scrollIntoView(new UiSelector().textContains("확인").instance(0));'
                )
                time.sleep(1)
                
                # 확인 버튼 클릭
                confirm_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
                confirm_btn.click()
                time.sleep(1)
                
                # 확인 버튼 클릭
                confirm_btn = driver.find_element(*self._get_locator(driver, '(//android.view.ViewGroup[@content-desc="확인"])[2]'))

                if len(confirm_btn) == 1:
                    confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'search_confirm_btn')))
                    confirm_btn.click()
                    time.sleep(1)
                else:
                    pass
                
                # 홈으로 버튼 클릭
                home_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'home_btn')))
                home_btn.click()
                time.sleep(1)
                driver.back()
                driver.back()
                driver.back()
                pass
            else:
                driver.back()
            # time.sleep(1)
            
            
        except Exception as e:
            pytest.fail(f"검색 및 한마음요양원 등록 테스트 실패: {str(e)}")
    
    def test_notification_management(self, driver_setup):
        """알림 관리 테스트"""
        # driver가 딕셔너리인 경우 실제 driver 객체 추출
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            # 홈 화면 진입 확인
            time.sleep(2)
            
            # 알림 종 버튼 클릭
            notification_bell_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'notification_bell_btn')))
            notification_bell_btn.click()
            time.sleep(1)
            
            # 목록에서 첫번째 항목 클릭
            first_notification_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_notification_item')))
            first_notification_item.click()
            time.sleep(1)
            
            # 뒤로가기 버튼 클릭
            driver.back()

            # 첫번째 항목의 X 버튼 클릭
            first_notification_x_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_notification_x_btn')))
            first_notification_x_btn.click()
            time.sleep(1)
            
            # 진행 버튼 클릭
            proceed_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "진행")
            proceed_btn.click()
            time.sleep(1)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            
        except Exception as e:
            pytest.fail(f"알림 관리 테스트 실패: {str(e)}")
    
    def test_hamburger_menu_navigation(self, driver_setup):
        """햄버거 메뉴 내비게이션 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 햄버거 메뉴 버튼 클릭
            hamburger_menu_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'hamburger_menu_btn')))
            hamburger_menu_btn.click()
            time.sleep(1)
            
            # 각 메뉴 항목 클릭 및 뒤로가기
            menu_items = [
                'menu_visit_care_btn', 'menu_companion_service_btn', 'menu_caregiver_btn',
                'menu_ltc_facility_btn', 'menu_housekeeping_btn', 'menu_my_info_btn',
                'menu_family_info_btn', 'menu_service_history_btn', 'menu_favorite_institutions_btn',
                'menu_payment_management_btn', 'menu_certificate_btn', 'menu_notice_btn',
                'menu_event_btn', 'menu_faq_btn', 'menu_customer_center_btn',
                'menu_suggestion_btn', 
                'menu_notification_settings_btn'
            ]
            
            for menu_item in menu_items:
                menu_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, menu_item)))
                menu_btn.click()
                time.sleep(0.5)

                try:
                    loction_access_modal = driver.find_elements(*self._get_locator(driver, 'loction_access_modal'))
                    print(f"장기요양 위치 권한 모달 개수: {len(loction_access_modal)}")
                    # 장기요양 위치 권한 모달
                    if len(loction_access_modal) == 1:
                        print("장기요양 위치 권한 모달 표시됨")
                        loction_access_modal[0].click()
                        print("장기요양 위치 권한 모달 클릭됨")
                        time.sleep(0.5)

                except:
                    pass
                driver.back()
                time.sleep(0.5)

                if menu_item == 'menu_certificate_btn':
                    driver.find_element(
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                        '.scrollIntoView(new UiSelector().textContains("알림설정").instance(0));'
                    )
                    time.sleep(0.5)
            
            # 마지막 뒤로가기
            driver.back()
            time.sleep(1)
            
        except Exception as e:
            pytest.fail(f"햄버거 메뉴 내비게이션 테스트 실패: {str(e)}")