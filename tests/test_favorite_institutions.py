import pytest
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
import time
from conftest import *

class TestFavoriteInstitutions:
    
    def _get_platform(self, driver):
        """플랫폼 확인"""
        if isinstance(driver, dict):
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
                'hamburger_menu_btn': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]'),
                'favorite_institutions_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="관심기관"]'),
                'first_institution_item': (AppiumBy.XPATH, '(//android.view.ViewGroup[@clickable="true"])[1]'),
                'institution_heart_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="하트"]'),
                'back_btn': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]'),
                # 바텀 메뉴 관심기관 관련 로케이터
                'bottom_favorite_institutions_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="관심기관"]'),
                # 'first_favorite_heart_btn': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(21)'),
                'first_favorite_heart_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="숲데이케어센터, 2018.04.19, 60 명 정원, 서울 동작구 상도로68길 1-20"]/android.view.ViewGroup[2]/android.view.ViewGroup/com.horcrux.svg.SvgView'),
                'toast_message': (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="toastAnimatedContainer"]'),
                # 'toast_message': (AppiumBy.ID, 'toastAnimatedContainer'),
                # 'toast_message': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("toastAnimatedContainer")'),
                'hanmaeum_nursing_home_name': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="재가복지센터, 숲데이케어센터, 서울 동작구 상도로68길 1-20"]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'),
                'search_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="검색"]'),
                # 'search_icon_btn': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'search_icon_btn': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'loction_access_modal': (AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]'),
            },
            'ios': {
                'hamburger_menu_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='메뉴']"),
                'favorite_institutions_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='관심기관']"),
                'first_institution_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'institution_heart_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='하트']"),
                'back_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='뒤로가기']"),
                # 바텀 메뉴 관심기관 관련 로케이터
                'bottom_favorite_institutions_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='관심기관']"),
                'first_favorite_heart_btn': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='하트'])[1]"),
                'toast_message': (AppiumBy.XPATH, "//XCUIElementTypeStaticText"),
                'hanmaeum_nursing_home_name': (AppiumBy.XPATH, "//XCUIElementTypeStaticText"),
                'search_input': (AppiumBy.XPATH, "//XCUIElementTypeStaticText"),
                'search_icon_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText"),
                'loction_access_modal': (AppiumBy.XPATH, "//XCUIElementTypeStaticText"),
            }
        }
        
        return locators[platform][element_name]
    
    def test_favorite_institutions_management(self, driver_setup):
        """바텀 메뉴 관심기관 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(0.5)
            
            # 바텀 메뉴에서 관심기관 클릭
            bottom_favorite_institutions_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_favorite_institutions_btn')))
            bottom_favorite_institutions_btn.click()
            time.sleep(1)
            
            # 첫번째 항목의 하트 클릭
            first_favorite_heart_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_favorite_heart_btn')))
            first_favorite_heart_btn.click()
            time.sleep(1)
            
            # 관심기업 해제 토스트메세지가 잘 뜨는지 확인
            toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message')))
            # assert toast_message.is_displayed(), "이 시설을 즐겨찾기 목록에서 제거했습니다!"
            # time.sleep(1)
            assert toast_message.is_displayed(), "이 시설을 즐겨찾기 목록에서 제거했습니다!"
            time.sleep(0.5)

            # driver.back()
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
            pytest.fail(f"바텀 메뉴 관심기관 테스트 실패: {str(e)}")