import pytest
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
import time
from conftest import * 

class TestHomeScreenMatching:
    
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
                'second_heart_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="C, 요양원, 모두케어, 경기 구리시 동구릉로 427, 9061.25 km"]/android.view.ViewGroup[3]/android.view.ViewGroup'),
                'second_heart_btn_in': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup'),
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
                # 'hope_mony_input': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[5]'),
                'hope_mony_input': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("희망하는 시급을 동행인에게 제안하세요")'),
                # 'hope_mony_input': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[5]'),
                'hope_mony_input2': (AppiumBy.XPATH, '//android.widget.EditText[@text="희망하는 시급을 동행인에게 제안하세요"]'),
                # 'hope_mony_input2': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("희망하는 시급을 동행인에게 제안하세요")'),
                'meeting_place_add_btn': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]'),
                'visit_place_add_btn': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup[1]'),
                'confirm_btn6': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="확인"])[1]'),
                'confirm_btn7': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="확인"]'),
                'same_return_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="복귀장소가 만남장소와 동일합니다."]'),
                'patient_location_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="예시) 서울시 강남구"]'),
                'pass_keyboard_btn': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup'),
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
                'second_heart_btn_in': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='하트'])[2]"),
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
                'hope_mony_input2': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='희망 시급']"),
                'meeting_place_add_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='추가']"),
                'visit_place_add_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='추가']"),
                'confirm_btn6': (AppiumBy.XPATH, "(//XCUIElementTypeStaticText[@name='확인'])[1]"),
                'confirm_btn7': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='확인']"),
                'same_return_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@name,'동일합니다')]"),
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

    # def test_visit_care_service_registration(self, driver):
    def test_visit_care_service_registration(self, driver_setup):
        """방문요양찾기 서비스 신청 테스트"""
        # driver가 딕셔너리인 경우 실제 driver 객체 추출
        if isinstance(driver_setup, dict):
            actual_driver = driver_setup['driver']
        else:
            actual_driver = driver_setup
        wait = WebDriverWait(actual_driver, 10)
        # action = TouchAction(actual_driver)
        # deviceSize = actual_driver.get_window_size()
        # screenWidth = deviceSize['width']
        # screenHeight = deviceSize['height']
        try:
            # 홈 화면 진입 확인
            time.sleep(2)
            
            # 방문요양찾기 버튼 클릭
            # visit_care_btn = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'visit_care_btn')))
            visit_care_btn = actual_driver.find_element(AppiumBy.ACCESSIBILITY_ID, "방문요양 찾기, 찾기")
            visit_care_btn.click()
            time.sleep(1)
            
            # 소개보기 버튼 클릭
            # intro_btn = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'intro_btn')))
            # intro_btn.click()
            # time.sleep(2)
            
            # # 다시 앱으로 돌아오기 (뒤로가기)
            # driver.back()
            # time.sleep(1)
            
            # 방문요양서비스 신청하기 클릭
            apply_btn = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'apply_btn')))
            apply_btn.click()
            time.sleep(1)
            
            # "아니오, 가족이 아닙니다." 체크박스 클릭
            not_family_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'not_family_checkbox')))
            not_family_checkbox.click()
            time.sleep(1)
            
            # 등록하기 버튼 클릭
            register_btn = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'register_btn')))
            register_btn.click()
            time.sleep(1)
            
            # 장소 선택 버튼 클릭
            location_btn = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'location_btn')))
            location_btn.click()
            time.sleep(1)
            
            # 인풋에 "다산순환로20" 입력
            address_input = wait.until(EC.presence_of_element_located(self._get_locator(actual_driver, 'address_input')))
            address_input.clear()
            address_input.send_keys("s")
            time.sleep(1)
            
            # 돋보기 버튼 클릭
            search_btn = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'search_btn')))
            search_btn.click()
            time.sleep(2)
            
            # 첫번째 항목 클릭
            first_result = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'first_result')))
            first_result.click()
            time.sleep(1)
            
            # 확인 버튼 클릭
            confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'confirm_btn')))
            confirm_btn.click()
            time.sleep(1)
            
            # container_locator = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView')
            # next_btn_find_element = wait.until(EC.presence_of_element_located(container_locator))
            # action.long_press(None,screenWidth/2,screenHeight*0.8).move_to(None,screenWidth/2,screenHeight*0.1).release().perform()
            # 화면 전체를 위에서 아래로 스크롤
            # actions = ActionBuilder(actual_driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            # actions.pointer_action.move_to_location(200, screenHeight*0.2)  # 화면 하단 90% 지점에서 시작
            # actions.pointer_action.pointer_down()
            # actions.pointer_action.move_to_location(200, screenHeight*0.1)  # 화면 상단 10% 지점까지 이동
            # actions.pointer_action.pointer_up()
            # actions.perform()
            # mobile: scroll 명령어로 스크롤
            # print("스크롤 시도",screenHeight*0.8, screenHeight*0.2)
            # try:
            #     actual_driver.execute_script('mobile: scroll', {'direction': 'down'})
            # except:
            #     # 대체 방법: 좌측 가장자리에서 스크롤
            #     actual_driver.swipe(50, screenHeight*0.8, 50, screenHeight*0.2, 1000)
            # actual_driver.swipe(50, 1472, 50, 368, 1000)
            # actual_driver.execute_script("mobile: scroll", {
            #     "elementId": next_btn_find_element.id,     # iOS는 elementId 키, 일부 문서엔 element로 표기되기도
            #     "direction": "down",            # "up" | "down" | (드라이버별로 "left" | "right")
            #     "percent": 0.85   # 한 번에 어느 정도 스크롤할지 (0~1)
            # })
            # time.sleep(1)
            # actual_driver.execute_script('mobile: scroll', {
            #     'direction': 'down',
            # })
            # actual_driver.execute_script('mobile: scrollGesture', { 'direction': 'down', 'elementId': next_btn.id })

            actual_driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(1)
            # 다음 버튼 클릭
            next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'next_btn')))
            next_btn.click()
            time.sleep(1)
            
            # 캘린더에서 > 버튼 클릭
            calendar_next = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'calendar_next')))
            calendar_next.click()
            time.sleep(1)
            
            # 1~30까지 랜덤한 날짜 클릭
            # //android.view.ViewGroup[@content-desc="28"]
            # random_day = random.randint(1, 30)
            # date_btn = wait.until(EC.element_to_be_clickable(self._get_date_locator(actual_driver, random_day)))
            date_btn = wait.until(EC.element_to_be_clickable(self._get_date_locator(actual_driver, 'calendar_date')))
            # date_btn = actual_driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("18")')
            date_btn.click()
            time.sleep(1)
            # driver.swipe(actual_driver, 708, 2433, 666, 792)
            # actual_driver.swipe(708, 2433, 666, 792, 1000)
            actual_driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )

            # 방문 시작시간 드롭다운 클릭
            start_time_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'start_time_dropdown')))
            start_time_dropdown.click()
            time.sleep(1)
            
            # 11:00로 시간 설정
            # time_11 = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'time_11')))
            # time_11.click()
            # time.sleep(1)
            
            # 확인 버튼 클릭
            # //android.widget.Button[@resource-id="android:id/button1"]
            # confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'confirm_btn2')))
            confirm_btn = actual_driver.find_element(AppiumBy.XPATH, "confirm_btn2")
            confirm_btn.click()
            time.sleep(1)
            
            # 방문시간 드롭다운 클릭
            duration_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'duration_dropdown')))
            duration_dropdown.click()
            time.sleep(1)
            
            # 3시간 클릭
            three_hours = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'three_hours')))
            three_hours.click()
            time.sleep(1)

            actual_driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            # actual_driver.swipe(650, 2535, 842, 403, 1000)
            time.sleep(1)
            
            # 다음 버튼 클릭
            # //android.view.ViewGroup[@content-desc="다음"]
            # next_btn1 = wait.until(EC.element_to_be_clickable(AppiumBy.XPATH, '//android.widget.TextView[@text="다음"]'))
            # next_btn1 = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="다음"]')))
            # next_btn_element = actual_driver.find_element(*self._get_locator(actual_driver, 'next_btn1'))
            # TouchAction(actual_driver).tap(next_btn_element).perform()
            # next_btn1 = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text="다음"]')))
            next_btn_element = actual_driver.find_element(*self._get_locator(actual_driver, 'next_btn1'))

            # mobile: clickGesture로 클릭
            actual_driver.execute_script('mobile: clickGesture', {
                'elementId': next_btn_element.id
            })
            print("다음버튼 클릭")
            # next_btn1.click()
            time.sleep(1)
            
            # 정보불러오기 버튼 클릭
            load_info_btn = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'load_info_btn')))
            load_info_btn.click()
            time.sleep(1)
            
            # 김영희 항목 클릭
            kim_younghee = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'kim_younghee')))
            kim_younghee.click()
            time.sleep(1)

            # actual_driver.swipe(646, 2635, 668, 221, 1000)
            actual_driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            
            time.sleep(1)
            # 다음 버튼 클릭
            element = actual_driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            element.click()
            # next_btn_element2 = actual_driver.find_element(*self._get_locator(actual_driver, 'next_btn2'))
            # print("다음버튼 클릭", next_btn_element2)
            # # mobile: clickGesture로 클릭
            # actual_driver.execute_script('mobile: clickGesture', {
            #     'elementId': next_btn_element2.id
            # })
            time.sleep(1)
            
            # 성별무관 버튼 클릭
            gender_any = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'gender_any')))
            gender_any.click()
            time.sleep(1)
            
            # 진행안함 버튼 클릭
            no_proceed = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'no_proceed')))
            no_proceed.click()
            time.sleep(1)
            
            actual_driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(1)

            # 친절함 버튼 클릭
            kind_btn = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'kind_btn')))
            kind_btn.click()
            time.sleep(1)

            # actual_driver.swipe(571, 2577, 603, 411, 1000)
            # actual_driver.find_element(
            #     AppiumBy.ANDROID_UIAUTOMATOR,
            #     'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
            #     '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            # )
            time.sleep(1)
            
            # 다음 버튼 클릭
            next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'next_btn')))
            next_btn.click()
            time.sleep(1)
            
            # actual_driver.swipe(578, 2906, 478, 282, 1000)
            # time.sleep(1)
            # actual_driver.swipe(728, 2735, 735, 793, 1000)
            actual_driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(1)

            # 다음 버튼 클릭
            next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'next_btn')))
            next_btn.click()
            time.sleep(1)
            
            # "네, 동의합니다." 버튼 클릭
            agree_btn = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'agree_btn')))
            agree_btn.click()
            time.sleep(1)
            
            # 등록하기 버튼 클릭
            # //android.view.ViewGroup[@content-desc="등록하기"]
            register_btn = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'register_btn')))
            register_btn.click()
            time.sleep(1)
            
            # 자동매칭 체크박스 클릭
            # auto_match_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'auto_match_checkbox')))
            # auto_match_checkbox.click()
            # time.sleep(1)
            
            # actual_driver.swipe(525, 2720, 425, 664, 1000)
            actual_driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(1)

            # 다음 버튼 클릭
            # //android.view.ViewGroup[@content-desc="다음"]
            next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'next_btn')))
            next_btn.click()
            time.sleep(1)
            
            # 메인이동 버튼 클릭
            main_btn = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'main_btn')))
            main_btn.click()
            time.sleep(1)
            
            # 뒤로가기 버튼 클릭
            back_btn = wait.until(EC.element_to_be_clickable(self._get_locator(actual_driver, 'back_btn1')))
            back_btn.click()
            # actual_driver.back()
            time.sleep(1)
            
        except Exception as e:
            pytest.fail(f"방문요양찾기 테스트 실패: {str(e)}")
    
    def test_long_term_care_facility_search(self, driver_setup):
        """장기요양기관 찾기 테스트"""
        # driver가 딕셔너리인 경우 실제 driver 객체 추출
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            # 홈 화면 진입 확인
            time.sleep(2)
            
            # 장기요양기관 찾기 버튼 클릭
            # ltc_facility_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'ltc_facility_btn')))
            # ltc_facility_btn.click()
            ltc_facility_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "장기요양기관\n찾기, 찾기")
            ltc_facility_btn.click()
            time.sleep(1)

            location_access_btn = driver.find_element(*self._get_locator(driver, 'location_access'))
            location_access_btn.click()
            
            # 시도/ 드롭다운 클릭
            # region_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'region_dropdown')))
            region_dropdown = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "시/도")
            region_dropdown.click()
            time.sleep(1)
            
            # 전국 클릭
            # nationwide = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'nationwide')))
            nationwide = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "전국")
            nationwide.click()
            time.sleep(1)

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("시설 찾기").instance(0));'
            )
            time.sleep(1)
            
            # 시설 찾기 버튼 클릭
            # find_facility_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'find_facility_btn')))
            find_facility_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "시설 찾기")
            find_facility_btn.click()
            time.sleep(2)
            
            # 두번째 항목의 하트 버튼 클릭
            second_heart_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'second_heart_btn')))
            # second_heart_btn = driver.find_element(AppiumBy.XPATH, 'second_heart_btn')
            second_heart_btn.click()
            time.sleep(1)
            
            # 관심기업으로 등록이 되었다는 토스트메세지 확인
            # toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message')))
            # assert "시설" in toast_message.text or "추가" in toast_message.text or "제거" in toast_message.text
            # time.sleep(2)
            
            # 두번째 항목 클릭
            # second_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'second_item')))
            second_item = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "C, 요양원, 모두케어, 경기 구리시 동구릉로 427, 9061.25 km")
            second_item.click()
            time.sleep(1)

            second_heart_btn_in = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'second_heart_btn_in')))
            # second_heart_btn = driver.find_element(AppiumBy.XPATH, 'second_heart_btn')
            second_heart_btn_in.click()
            time.sleep(1)
            
            # 스크롤해서 아래로 내려가서 상담신청 버튼 클릭
            # driver.swipe(500, 1500, 500, 500, 1000)  # 스크롤 다운
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("입소지원").instance(0));'
            )
            time.sleep(1)

            # consult_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'consult_btn')))
            consult_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "상담신청")
            consult_btn.click()
            time.sleep(1)
            
            # 이름 인풋에 "김동라그미" 입력
            name_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'name_input')))
            name_input.clear()
            name_input.send_keys("김동라그미")
            time.sleep(1)
            
            # 등급 드롭다운 클릭
            # grade_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'grade_dropdown')))
            grade_dropdown = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "선택")
            grade_dropdown.click()
            time.sleep(1)

            # 1등급 클릭
            # //android.view.ViewGroup[@content-desc="1등급"]
            grade_dropdown = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1등급")
            grade_dropdown.click()
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
            # year_2024 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'year_2024')))
            year_2024 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "2024")
            year_2024.click()
            time.sleep(1)
            
            # 상담 받으실 전화번호 인풋에 "01092205162" 입력
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
                # 두 번째 "선택하세요"가 없으면 일반 스크롤
                driver.swipe(500, 1500, 500, 500, 1000)
            # self._show_second_match(driver, '선택하세요', 8)
            # driver.swipe(500, 1500, 500, 500, 1000)  # 스크롤 다운
            time.sleep(1)
            
            # 상담받기 편한 시간대 드롭다운 클릭
            try:
                # 두 번째 "선택하세요" 시도
                consult_time_dropdown = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("선택하세요").instance(1)')
            except:
                # 첫 번째 "선택하세요" 사용
                consult_time_dropdown = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("선택하세요")')
            consult_time_dropdown.click()
            time.sleep(1)
            
            # 11:00로 시간 설정
            # time_11 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'time_11')))
            # time_11.click()
            # time.sleep(1)
            
            # 확인 버튼 클릭
            confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn3')))
            confirm_btn.click()
            time.sleep(1)
            
            # 보내기 버튼 클릭
            # send_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'send_btn')))
            send_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "보내기")
            send_btn.click()
            time.sleep(1)
            
            # 입소지원 버튼 클릭
            # admission_support_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'admission_support_btn')))
            admission_support_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "입소지원")
            admission_support_btn.click()
            time.sleep(1)
            
            # 홍길동 항목 체크박스 클릭
            # hong_gildong_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'hong_gildong_checkbox')))
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
            # confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn4')))
            confirm_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_btn.click()
            time.sleep(1)
            
            # 모달 확인 버튼 (클릭한 가족의 입소신청서를 확인중이라는 모달)
            home_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn5')))
            # home_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홈으로")
            home_btn.click()
            time.sleep(1)

            # 뒤로가기 버튼 클릭
            # back_bth = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'back_bth2')))
            # back_bth.click()
            driver.back()
            # time.sleep(1)

            # driver.find_element(
            #     AppiumBy.ANDROID_UIAUTOMATOR,
            #     'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
            #     '.scrollIntoView(new UiSelector().textContains("전화번호").instance(0));'
            # )
            # time.sleep(1)

            # 뒤로가기 버튼 클릭
            # back_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'back_bth3')))
            # back_btn.click()
            driver.back()
            # time.sleep(1)

            # 뒤로가기 버튼 클릭
            # back_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'back_btn4')))
            # back_btn.click()
            # time.sleep(1)
            driver.back()

            # driver.find_element(
            #     AppiumBy.ANDROID_UIAUTOMATOR,
            #     'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
            #     '.scrollIntoView(new UiSelector().textContains("장기요양기관 찾기").instance(0));'
            # )
            # time.sleep(1)

            # 뒤로가기 버튼 클릭
            # back_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'back_btn5')))
            # back_btn.click()
            # time.sleep(1)
            driver.back()
            
        except Exception as e:
            pytest.fail(f"장기요양기관 찾기 테스트 실패: {str(e)}")
    
    def test_housekeeping_service_registration(self, driver_setup):
        """가사돌봄 서비스 신청 테스트"""
        # driver가 딕셔너리인 경우 실제 driver 객체 추출
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            # 홈 화면 진입 확인
            time.sleep(2)
            
            # 가사돌봄 버튼 클릭
            # housekeeping_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'housekeeping_btn')))
            housekeeping_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "가사돌봄, 찾기")
            housekeeping_btn.click()
            time.sleep(1)
            
            # 소개보기 버튼 클릭
            # intro_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'intro_btn')))
            # intro_btn.click()
            # time.sleep(2)
            
            # # 다시 앱으로 돌아오기
            # driver.back()
            # time.sleep(1)
            
            # 가사돌봄서비스 신청하기
            # apply_housekeeping_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'apply_housekeeping_btn')))
            apply_housekeeping_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "가사돌봄서비스 신청하기")
            apply_housekeeping_btn.click()
            time.sleep(1)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(1)

            # 다음 버튼 클릭
            # next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_btn')))
            next_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next_btn.click()
            time.sleep(1)
            
            # 장소선택 버튼 클릭
            # location_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'location_btn')))
            location_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "장소 선택")
            location_btn.click()
            time.sleep(1)
            
            # 인풋에 "다산순환로20" 입력
            address_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'address_input')))
            address_input.clear()
            address_input.send_keys("s")
            time.sleep(1)
            
            # 돋보기 버튼 클릭
            search_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'search_btn')))
            search_btn.click()
            time.sleep(2)
            
            # 첫번째 항목 클릭
            first_result = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_result')))
            first_result.click()
            time.sleep(1)
            
            # 확인 버튼 클릭
            confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn')))
            confirm_btn.click()
            time.sleep(1)

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(1)
            
            # 다음 버튼 클릭
            # next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_btn')))
            next_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next_btn.click()
            time.sleep(1)
            
            
            # 서비스 1개째 체크박스 클릭
            service_checkbox1 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'service_checkbox1')))
            service_checkbox1.click()
            time.sleep(0.5)
            # 서비스 2개째 체크박스 클릭
            service_checkbox2 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'service_checkbox2')))
            service_checkbox2.click()
            time.sleep(0.5)
            # 서비스 3개쩨 체크박스 클릭
            service_checkbox3 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'service_checkbox3')))
            service_checkbox3.click()
            time.sleep(0.5)

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(1)
            
            # 서비스 4개째 체크박스 클릭
            service_checkbox4 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'service_checkbox4')))
            service_checkbox4.click()
            time.sleep(0.5)
            # 서비스 5개쨰 체크박스 클릭
            service_checkbox5 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'service_checkbox5')))
            service_checkbox5.click()
            time.sleep(0.5)

            # 다음 버튼 클릭
            next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_btn')))
            next_btn.click()
            time.sleep(1)
            
            # 18평 미만 체크박스 클릭
            under_18_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'under_18_checkbox')))
            under_18_checkbox.click()
            time.sleep(1)
            
            # 1개 이하 체크박스 클릭
            under_1_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'under_1_checkbox')))
            under_1_checkbox.click()
            time.sleep(1)

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("반려동물을 키우시나요?").instance(0));'
            )
            time.sleep(1)
            
            # 독거 체크박스 클릭
            alone_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'alone_checkbox')))
            alone_checkbox.click()
            time.sleep(1)
            
            # 아니오 체크박스 클릭
            yes_checkbox_1 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'yes_checkbox_1')))
            yes_checkbox_1.click()
            time.sleep(1)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(1)

            # 예 체크박스 클릭
            yes_checkbox_2 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'yes_checkbox_2')))
            yes_checkbox_2.click()
            time.sleep(1)
            
            # 다음 버튼 클릭
            next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_btn')))
            next_btn.click()
            time.sleep(1)
            
            # 1-30까지 랜덤한 날짜 클릭
            date_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'housekeeping_calendar_date')))
            date_btn.click()
            time.sleep(1)

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(1)
            
            # 가사돌봄 시작시간 드롭다운 클릭
            start_time_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'housekeeping_start_time_dropdown')))
            start_time_dropdown.click()
            time.sleep(1)
            
            # 11:00로 시간 설정
            # time_11 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'time_11')))
            # time_11.click()
            # time.sleep(1)
            
            # 확인 버튼 클릭
            confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn2')))
            confirm_btn.click()
            time.sleep(1)
            
            # 신청 시간 드롭다운 클릭
            # duration_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'duration_dropdown_housekeeping')))
            duration_dropdown = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "30분")
            duration_dropdown.click()
            time.sleep(1)
            
            # 1시간 클릭
            # one_hour = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'one_hour')))
            one_hour = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1시간 30분")
            one_hour.click()
            time.sleep(1)
            
            # 다음 버튼 클릭
            next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_btn')))
            next_btn.click()
            time.sleep(1)
            
            # 정보불러오기 버튼 클릭
            load_info_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'load_info_btn')))
            load_info_btn.click()
            time.sleep(1)
            
            # 김영희 항목 클릭
            kim_younghee = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'kim_younghee')))
            kim_younghee.click()
            time.sleep(1)

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(1)
            
            # 다음 버튼 클릭
            next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_btn')))
            next_btn.click()
            time.sleep(1)

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("등록하기").instance(0));'
            )
            time.sleep(1)
            
            # "네, 동의합니다." 버튼 클릭
            agree_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'agree_btn')))
            agree_btn.click()
            time.sleep(1)
            
            # 등록하기 버튼 클릭
            register_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'register_btn')))
            register_btn.click()
            time.sleep(1)
            
            # 메인이동 버튼 클릭
            main_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'main_btn')))
            main_btn.click()
            time.sleep(1)
            
            # 뒤로가기 버튼 클릭
            back_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'back_btn2')))
            back_btn.click()
            time.sleep(1)
            
        except Exception as e:
            pytest.fail(f"가사돌봄 서비스 테스트 실패: {str(e)}")
    
    def test_caregiver_service_registration(self, driver_setup):
        """간병인 서비스 신청 테스트"""
        # driver가 딕셔너리인 경우 실제 driver 객체 추출
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            # 홈 화면 진입 확인
            time.sleep(2)
            
            # 간병인 버튼 클릭
            caregiver_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "간병인 찾기, 찾기")
            caregiver_btn.click()
            time.sleep(1)
            
            # 간병인 신청하기 버튼 클릭
            caregiver_apply_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "간병인서비스 신청하기")
            caregiver_apply_btn.click()
            time.sleep(1)

            els = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "새로 등록")
            # 화면 안에 최소 2개가 보이면 종료
            print("els length:", len(els), type(len(els)))
            if len(els) == 1:
                els[0].click()
                # time.sleep(1)
            else:
                pass
            
            # 기간제 간병 체크박스 클릭
            term_care_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'term_care_checkbox')))
            term_care_checkbox.click()
            time.sleep(1)

            # 다음 버튼 클릭
            # next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_btn')))
            # next_btn.click()
            # time.sleep(1)

            # 시작 날짜 설정 인풋 클릭
            # start_date_input = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'start_date_input')))
            start_date_input = driver.find_element(*self._get_locator(driver, 'start_date_input'))
            start_date_input.click()
            time.sleep(1)
            
            # 2026년 10월 22일 설정
            # year_2026 = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='2026']")
            # year_2026.click()
            # time.sleep(1)
            
            # month_10 = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='10월']")
            # month_10.click()
            # time.sleep(1)
            
            # day_22 = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='22']")
            # day_22.click()
            # time.sleep(1)
            
            # 확인 버튼 클릭
            # start_date_input = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn2')))
            confirm_btn = driver.find_element(*self._get_locator(driver, 'confirm_btn_2'))
            confirm_btn.click()
            time.sleep(1)
            
            # 선택 드롭다운 클릭
            start_date_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'start_date_dropdown')))
            # start_time_dropdown = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "선택")
            start_date_dropdown.click()
            time.sleep(1)
            
            # 시간 항목의 첫번쨰 클릭
            time_16 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'time_16')))
            time_16.click()
            time.sleep(1)

            # 선택 드롭다운 클릭
            # end_date_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'end_date_dropdown')))
            # end_date_dropdown.click()
            # time.sleep(1)
            
            # # 시간 항목의 첫번쨰 클릭
            # time_16 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'time_16')))
            # time_16.click()
            # time.sleep(1)

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
                # new UiSelector().description("다음")
            )
            time.sleep(1)
            
            # 다음 버튼 클릭
            next_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next_btn.click()
            time.sleep(1)
            
            # 집 체크박스 클릭
            home_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '집')
            home_checkbox.click()
            time.sleep(1)
            
            # 다음 버튼 클릭
            next_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next_btn.click()
            time.sleep(1)
            
            # 장소선택 버튼 클릭
            location_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "장소 선택")
            location_btn.click()
            time.sleep(1)
            
            # 인풋에 "다산순환로20" 입력
            address_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'address_input')))
            address_input.clear()
            address_input.send_keys("s")
            time.sleep(1)
            
            # 돋보기 버튼 클릭
            search_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'search_btn')))
            search_btn.click()
            time.sleep(2)
            
            # 첫번째 항목 클릭
            first_result = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_result')))
            first_result.click()
            time.sleep(1)

            # 상세주소 인풋에 "1층" 넣기
            detail_address_input = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'detail_address_input')))
            detail_address_input.clear()
            detail_address_input.send_keys("1층")
            time.sleep(1)
            
            # 확인 버튼 클릭
            confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn')))
            confirm_btn.click()
            time.sleep(1)

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(1)
            
            # 다음 버튼 클릭
            # next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_btn')))
            next_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next_btn.click()
            time.sleep(1)

            # 정보불러오기 버튼 클릭
            load_info_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'load_info_btn')))
            load_info_btn.click()
            time.sleep(1)
            
            # 김영희 항목 클릭
            kim_younghee = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'kim_younghee')))
            kim_younghee.click()
            time.sleep(1)

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(1)

            # 다음 버튼 클릭
            element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            element.click()
            time.sleep(1)
            
            # 수술 체크박스 클릭
            surgery_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '수술')
            surgery_checkbox.click()
            time.sleep(1)

            els2 = driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(31)')
            # 화면 안에 최소 1개가 보이면 종료
            # print("els length:", len(els), type(len(els)))
            if len(els2) == 1:
                els2[0].click()
                time.sleep(1)
            else:
                pass
            
            # 일반실 체크박스 클릭
            general_room_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '일반실')
            general_room_checkbox.click()
            time.sleep(1)

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("치매").instance(0));'
            )
            time.sleep(1)
            
            # 치매 체크박스 클릭
            dementia_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '치매')
            dementia_checkbox.click()
            time.sleep(1)

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(1)
            
            # 다음 버튼 클릭
            next_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next_btn.click()
            time.sleep(1)
            
            # 성별무관 체크박스 클릭
            gender_any = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '성별무관')
            gender_any.click()
            time.sleep(1)
            
            # 진행안함 체크박스 클릭
            no_proceed = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '진행안함')
            no_proceed.click()
            time.sleep(1)            

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("친절함").instance(0));'
            )
            time.sleep(1)
            
            # 친절함 체크박스 클릭
            kind_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '친절함')
            kind_btn.click()
            time.sleep(1)

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(1)
            
            # 다음 버튼 클릭
            next_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next_btn.click()
            time.sleep(1)

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("이상없음").instance(0));'
            )
            time.sleep(1)
            
            # 이상없음 버튼 클릭
            no_problem_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이상없음")
            no_problem_btn.click()
            time.sleep(1)
            
            # "네, 동의합니다." 버튼 클릭
            agree_caregiver_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "네, 동의합니다.")
            agree_caregiver_btn.click()
            time.sleep(1)
            
            # 등록하기 버튼 클릭
            register_caregiver_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "등록하기")
            register_caregiver_btn.click()
            time.sleep(1)
            
            # 간병 공고 체크박스 클릭
            caregiver_notice_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '간병공고, 환자 상태를 확인하고 간병인들이 보호자님께 직접 간병비를 제안합니다. 프로필, 돌봄경력 등 지원서를 확인하고 간병인을 선택해 보세요')
            caregiver_notice_checkbox.click()
            time.sleep(1)
            
            # 시급제안 인풋에 20000 넣기
            hourly_rate_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'mony_input')))
            hourly_rate_input.clear()
            hourly_rate_input.send_keys("20000")
            time.sleep(1)

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(1)
            
            # 다음 버튼 클릭
            next_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next_btn.click()
            time.sleep(1)
            
            # 메인이동 버튼 클릭
            main_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'main_btn')))
            main_btn.click()
            time.sleep(1)
            
            # 뒤로가기 버튼 클릭
            back_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'back_btn3')))
            back_btn.click()
            time.sleep(1)
            
        except Exception as e:
            pytest.fail(f"간병인 서비스 테스트 실패: {str(e)}")
    
    def test_companion_service_registration(self, driver_setup):
        """동행서비스 신청 테스트"""
        # driver가 딕셔너리인 경우 실제 driver 객체 추출
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            # 홈 화면 진입 확인
            time.sleep(2)
            
            # 동행서비스 버튼 클릭
            companion_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "동행서비스, 찾기")
            companion_btn.click()
            time.sleep(1)

            # 동행서비스 신청하기 버튼 클릭
            companion_apply_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "동행서비스 신청하기")
            companion_apply_btn.click()
            time.sleep(1)
            # 다음 버튼 클릭
            next_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next_btn.click()
            time.sleep(1)
            
            # "저의 가족 혹은 지인이 받을거에요." 체크박스 클릭
            family_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '저의 가족 혹은 지인이 받을거에요.')
            family_checkbox.click()
            time.sleep(1)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(1)

            # 다음 버튼 클릭
            next_btn2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next_btn2.click()
            time.sleep(1)

            # 정보불러오기 버튼 클릭
            load_info_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'load_info_btn')))
            load_info_btn.click()
            time.sleep(1)
            
            # 김영희 항목 클릭
            kim_younghee = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'kim_younghee')))
            kim_younghee.click()
            time.sleep(1)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(1)
            
            # 다음 버튼 클릭
            next_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next_btn.click()
            time.sleep(1)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("요약").instance(0));'
            )
            time.sleep(1)
            
            # 희망하는 시급을 동행인에게 제안하세요 인풋에 20000 넣기
            # hourly_rate_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'hope_mony_input')))
            hourly_rate_input = driver.find_element(*self._get_locator(driver, 'hope_mony_input'))
            hourly_rate_input.click()
            # hourly_rate_input.clear()
            # hourly_rate_input.send_keys("20000")

            hourly_rate_input2 = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'hope_mony_input2')))
            # hourly_rate_input2 = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="희망하는 시급을 동행인에게 제안하세요"]')
            # hourly_rate_input2.clear()
            hourly_rate_input2.send_keys("20000")
            time.sleep(1)

            pass_key = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'pass_keyboard_btn')))
            pass_key.click()
            time.sleep(1)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(1)
            
            # 다음 버튼 클릭
            next_btn3 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next_btn3.click()
            time.sleep(1)
            
            # 만남장소의 + 버튼 클릭
            meeting_place_add_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'meeting_place_add_btn')))
            meeting_place_add_btn.click()
            time.sleep(1)
            
            # 인풋에 새말로103 넣기
            address_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'address_input')))
            address_input.clear()
            address_input.send_keys("s")
            time.sleep(1)
            
            # 돋보기 버튼 클릭
            search_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'search_btn')))
            search_btn.click()
            time.sleep(2)
            
            # 첫번째 항목 클릭
            first_result = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_result')))
            first_result.click()
            time.sleep(1)
            
            # 확인 버튼 클릭
            confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn6')))
            confirm_btn.click()
            time.sleep(1)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(1)
            
            # 다음 버튼 클릭
            next_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next_btn.click()
            time.sleep(1)
            
            # 방문장소의 + 버튼 클릭
            visit_place_add_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'visit_place_add_btn')))
            visit_place_add_btn.click()
            time.sleep(1)
            
            # 인풋에 다산순환로20 넣기
            address_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'address_input')))
            address_input.clear()
            address_input.send_keys("s")
            time.sleep(1)
            
            # 돋보기 버튼 클릭
            search_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'search_btn')))
            search_btn.click()
            time.sleep(2)
            
            # 첫번째 항목 클릭
            first_result = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_result')))
            first_result.click()
            time.sleep(1)
            
            # 확인 버튼 클릭
            confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn7')))
            confirm_btn.click()
            time.sleep(1)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(1)
            
            # 다음 버튼 클릭
            next_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next_btn.click()
            time.sleep(1)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(1)
            
            # 복귀장소가 만남장소와 동일합니다. 체크박스 클릭
            same_return_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'same_return_checkbox')))
            same_return_checkbox.click()
            time.sleep(1)
            
            # 다음 버튼 클릭
            next_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next_btn.click()
            time.sleep(1)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(1)

            # 환자분이 사시는 곳은 어디인가요? 인풋에 강서구 넣기
            patient_location_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'patient_location_input')))
            patient_location_input.clear()
            patient_location_input.send_keys("강서구")
            time.sleep(1)
            
            # 키보드 엔터 클릭
            driver.press_keycode(66)  # Enter key
            time.sleep(1)

            # 다음 버튼 클릭
            next_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next_btn.click()
            time.sleep(1)
            
            # 상관없음 체크박스 클릭
            no_matter_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '상관없음')
            no_matter_checkbox.click()
            time.sleep(1)
            
            # 없음 체크박스 클릭
            none_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '없음')
            none_checkbox.click()
            time.sleep(1)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(1)
            
            # 다음 버튼 클릭
            next_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next_btn.click()
            time.sleep(1)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(1)
            
            # 다음 버튼 클릭
            next_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next_btn.click()
            time.sleep(1)
            
            # 다음 버튼 클릭
            next_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next_btn.click()
            time.sleep(1)
            
            # 네, 동의합니다. 체크박스 클릭
            agree_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '네, 동의합니다.')
            agree_checkbox.click()
            time.sleep(1)
            
            # 네, 확인하였습니다. 체크박스 클릭
            confirm_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '네, 확인하였습니다.')
            confirm_checkbox.click()
            time.sleep(1)
            
            # 다음 버튼 클릭
            next_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next_btn.click()
            time.sleep(1)
            
            # 메인이동 버튼 클릭
            main_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'main_btn')))
            main_btn.click()
            time.sleep(2)
            
            # # 뒤로가기 버튼 클릭
            # back_btn4 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'back_btn4')))
            # back_btn4.click()
            # time.sleep(1)
            try:
                # 방법 1: 일반적인 뒤로가기 버튼
                back_btn4 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'back_btn4')))
                back_btn4.click()
            except:
                driver.back()
            time.sleep(1)
            
        except Exception as e:
            pytest.fail(f"동행서비스 테스트 실패: {str(e)}")