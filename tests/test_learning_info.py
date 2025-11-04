import pytest
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
import time
from conftest import * 

class TestLearningInfo:
    
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
                # 학습자료실 관련 로케이터
                'learning_info_button': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("학습 정보")'),
                'category_button1': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(0)'),
                'category_button2': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(24)'),
                'list_item': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'list_item_youtube': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="▶"])[2]/android.view.ViewGroup'),
            },
            'ios': {
                # 학습자료실 관련 로케이터
                'learning_info_button': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='마이페이지']"),
                'category_button1': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='마이페이지']"),
                'category_button2': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='마이페이지']"),
                'list_item': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='마이페이지']"),
                'list_item_youtube': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='마이페이지']"),
            }
        }
        
        return locators[platform][element_name]
    
    def test_learning_info_navigation(self, driver_setup):
        """학습정보 네비게이션 테스트: 메인 -> 학습정보 -> 카테곣리 -> 목록 -> 아이템 상세"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)

        # 드라이버 설정 및 로그인 상태 확인
        # self.driver = driver_setup['driver']
        # self.base_driver = driver_setup['base_driver']
        # self.login_page = driver_setup['login_page']
        # self.wait = driver_setup['wait']
        # self.platform = driver_setup['platform']
        
        # print(f"\n📱 테스트 시작 - 플랫폼: {self.platform}")
        print("✅ 자동 로그인 완료 상태로 테스트 진행")
        
        # 필요시 로그인 상태 재확인 (일반적으로는 이미 로그인된 상태)
        # ensure_login()  # 필요한 경우에만 주석 해제
        
        print("\n=== 학습정보 네비게이션 테스트 시작 ===")
        
        # 1. 메인페이지에서 바텀 네비게이션의 학습정보 버튼 클릭
        print("\n1. 바텀 네비게이션의 학습정보 버튼 클릭")
        try:
            time.sleep(0.5)

            learning_info_button = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'learning_info_button')))
            learning_info_button.click()
            time.sleep(0.5)
            print("✓ 학습정보 버튼 클릭 완료")
        except Exception as e:
            print(f"✗ 학습정보 버튼 클릭 실패: {e}")
            raise
        
        # 2. 카테고리 클릭
        print("\n2. 카테고리 클릭")
        try:
            category_button1 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'category_button1')))
            category_button1.click()
            time.sleep(0.5)

            category_button2 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'category_button2')))
            category_button2.click()
            time.sleep(0.5)

            print("✓ 카테고리 클릭 완료")
        except Exception as e:
            print(f"✗ 카테고리 클릭 실패: {e}")
            raise
        
        # 3. 목록 아이템 클릭
        print("\n3. 목록 아이템 클릭")
        try:
            list_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'list_item')))
            list_item.click()
            time.sleep(3)
            print("✓ 목록 아이템 클릭 완료")
        except Exception as e:
            print(f"✗ 목록 아이템 클릭 실패: {e}")
            raise

        # 3. 아이템 상세의 유튜브 재생 버튼 클릭
        print("\n4. 아이템 상세의 유튜브 재생 버튼 클릭")
        try:
            list_item_youtube = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'list_item_youtube')))
            list_item_youtube.click()
            time.sleep(3)
            print("✓ 아이템 상세의 유튜브 재생 버튼 완료")
        except Exception as e:
            print(f"✗ 아이템 상세의 유튜브 재생 버튼 실패: {e}")
            raise

        # 5. 뒤로가기 버튼 클릭
        print("\n5. 뒤로가기 버튼 클릭")
        driver.back()

        print("\n=== 학습정보 네비게이션 테스트 완료 ===")
        assert True, "학습정보 네비게이션 테스트 성공"