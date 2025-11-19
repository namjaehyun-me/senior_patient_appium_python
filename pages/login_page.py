from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class LoginPage(BasePage):
    def _get_locator(self, element_name):
        """플랫폼별 로케이터 반환"""
        locators = {
            'android': {
                'username': (AppiumBy.XPATH, "//android.widget.EditText[@text='아이디를 입력해 주세요.']"),
                'password': (AppiumBy.XPATH, "//android.widget.EditText[@text='비밀번호를 입력해 주세요.']"),
                'login_button': (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='로그인']"),
                'popup_ok': (AppiumBy.XPATH, "//android.widget.Button[@resource-id='android:id/button1']"),
                'permission_allow': (AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_button']"),
                'password_skip': (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='다음에 변경']"),
                'mypage': (AppiumBy.XPATH, "//android.widget.TextView[@text='마이 페이지']"),
                'settings': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup'),
                'logout': (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='로그아웃']"),
                'error_msg': (AppiumBy.XPATH, "//android.widget.TextView[@text='이 필드는 필수 항목입니다!']"),
                'toast_msg': (AppiumBy.XPATH, "//android.widget.TextView[@text='아이디/이메일 또는 비밀번호를 잘못 입력했습니다.']"),
                'terms_of_change': (AppiumBy.ACCESSIBILITY_ID, "전체 동의"),
                'terms_of_change_go': (AppiumBy.ACCESSIBILITY_ID, "동의하고 계속하기")
            },
            'ios': {
                'username': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@value='아이디를 입력해 주세요.']"),
                'password': (AppiumBy.XPATH, "//XCUIElementTypeSecureTextField[@value='비밀번호를 입력해 주세요.']"),
                'login_button': (AppiumBy.ACCESSIBILITY_ID, "로그인"),
                'keybord_return': (AppiumBy.ACCESSIBILITY_ID, "Return"),
                'popup_ok': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='확인']"),
                'permission_allow': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='허용']"),
                'password_skip': (AppiumBy.ACCESSIBILITY_ID, "다음에 변경"),
                'mypage': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='home_tab.my_page, tab, 4 of 4']"),
                'settings': (AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='Mapa.'])[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]"),
                'logout': (AppiumBy.ACCESSIBILITY_ID, "로그아웃"),
                'error_msg': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='이 필드는 필수 항목입니다!']"),
                'toast_msg': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='아이디/이메일 또는 비밀번호를 잘못 입력했습니다.']"),
                'terms_of_change': (AppiumBy.ACCESSIBILITY_ID, "전체 동의"),
                'terms_of_change_go': (AppiumBy.ACCESSIBILITY_ID, "동의하고 계속하기")
            }
        }
        return locators[self.platform][element_name]

    
    def enter_input(self, userinfo, input_type):
        """통합 입력 메서드"""
        if input_type == "userid" or input_type == "username":
            self.send_keys(self._get_locator('username'), userinfo)
            # iOS에서 아이디 입력 후 키보드 닫기
            if self.platform == 'ios':
                self._close_keyboard_ios()
        elif input_type == "password":
            self.send_keys(self._get_locator('password'), userinfo)
            # iOS에서 비밀번호 입력 후 키보드 닫기
            if self.platform == 'ios':
                self._close_keyboard_ios()
        else:
            raise ValueError(f"지원하지 않는 input_type: {input_type}")
    
    def _close_keyboard_ios(self):
        """아이오에스 키보드 닫기"""
        import time
        try:
            # 방법 1: Return 버튼 클릭
            self.click_element(self._get_locator('keybord_return'))
            time.sleep(1)
        except:
            try:
                # 방법 2: Done 버튼 클릭
                done_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Done")
                done_button.click()
                time.sleep(1)
            except:
                try:
                    # 방법 3: 화면 탭으로 키보드 닫기
                    screen_size = self.driver.get_window_size()
                    # 화면 상단 영역 탭
                    x = int(screen_size['width'] / 2)
                    y = int(screen_size['height'] * 0.2)
                    self.driver.tap([(x, y)])
                    time.sleep(1)
                except:
                    # 모든 방법 실패
                    pass

    # def enter_username(self, username):
    #     self.send_keys(self.USERNAME_FIELD, username)
    
    # def enter_password(self, password):
    #     self.send_keys(self.PASSWORD_FIELD, password)
    
    def click_login(self):
        # iOS에서 로그인 버튼 클릭 전 키보드 닫기 확인
        if self.platform == 'ios':
            self._ensure_keyboard_closed_ios()
        self.click_element(self._get_locator('login_button'))
    
    def _ensure_keyboard_closed_ios(self):
        """아이오에스에서 키보드가 닫혔는지 확인"""
        import time
        try:
            # 키보드가 있는지 확인
            keyboard = self.driver.find_element(AppiumBy.CLASS_NAME, "XCUIElementTypeKeyboard")
            if keyboard.is_displayed():
                print("\n키보드가 열려있음. 닫는 중...")
                self._close_keyboard_ios()
        except:
            # 키보드가 없으면 OK
            pass
    
    def close_popup_if_present(self):
        """팝업이 있으면 닫기"""
        try:
            self.click_element(self._get_locator('popup_ok'))
        except:
            # 팝업이 없으면 무시
            pass
    
    def is_logged_in(self):
        """로그인 상태 확인"""
        try:
            # 로그인 화면의 아이디 입력 필드가 있으면 로그인 안됨
            self.find_element(self._get_locator('username'))
            return False
        except:
            # 에러 메시지가 있으면 로그인 화면에 있는 것
            try:
                # 빈 비밀번호 에러 메시지 확인
                self.driver.find_element(*self._get_locator('error_msg'))
                return False
            except:
                try:
                    # 잘못된 계정 토스트 메시지 확인
                    self.driver.find_element(*self._get_locator('toast_msg'))
                    return False
                except:
                    # 로그인 화면도 없고 에러 메시지도 없으면 로그인 됨
                    return True
    
    def go_to_mypage_if_logged_in(self):
        """로그인되어 있으면 마이페이지 버튼 클릭"""
        if self.is_logged_in():
            try:
                self.click_element(self.MY_PAGE_BUTTON)
            except:
                # 마이페이지 버튼이 없으면 무시
                pass
    
    def click_settings(self):
        """설정 버튼 클릭"""
        try:
            self.click_element(self.SETTINGS_BUTTON)
        except:
            # 설정 버튼이 없으면 무시
            pass
    
    def click_logout(self):
        """로그아웃 버튼 클릭"""
        try:
            self.click_element(self.LOGOUT_BUTTON)
        except:
            # 로그아웃 버튼이 없으면 무시
            pass
    
    def perform_logout_process(self):
        """로그아웃 전체 프로세스: 마이페이지 -> 설정 -> 로그아웃"""
        import time
        print("\n마이페이지를 클릭합니다.")
        self.click_element(self._get_locator('mypage'))
        time.sleep(2)
        print("\n설정을 클릭합니다.")
        self.click_element(self._get_locator('settings'))
        time.sleep(2)
        print("\n로그아웃을 클릭합니다.")
        self.click_element(self._get_locator('logout'))
        time.sleep(2)
        print("\n로그아웃 완료. 로그인 화면으로 이동했습니다.")
    
    def allow_permission_if_present(self):
        """알림 허용 팝업이 있으면 허용 버튼 클릭"""
        if self.platform == 'ios':
            self._handle_ios_permission_modal()
        else:
            try:
                self.click_element(self._get_locator('permission_allow'))
            except:
                pass
    
    def _handle_ios_permission_modal(self):
        """아이오에스 알림 허용 모달 처리"""
        import time
        time.sleep(2)  # 모달 로딩 대기
        
        # 방법 1: 일반적인 iOS 알림 버튼
        ios_permission_selectors = [
            (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='허용']"),
            (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='Allow']"),
            (AppiumBy.ACCESSIBILITY_ID, "허용"),
            (AppiumBy.ACCESSIBILITY_ID, "Allow"),
            # iOS 시스템 알림
            (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='허용' and @visible='true']"),
            (AppiumBy.XPATH, "//XCUIElementTypeAlert//XCUIElementTypeButton[2]"),  # 두번째 버튼 (보통 허용)
        ]
        
        for selector in ios_permission_selectors:
            try:
                element = self.driver.find_element(*selector)
                if element.is_displayed():
                    element.click()
                    print("\niOS 알림 허용 버튼 클릭 성공")
                    return
            except:
                continue
        
        # 방법 2: 좌표 기반 클릭 (모달이 화면 중앙에 있다고 가정)
        try:
            screen_size = self.driver.get_window_size()
            # 화면 오른쪽 하단 영역 클릭 (보통 허용 버튼 위치)
            x = int(screen_size['width'] * 0.7)  # 화면 너비의 70% 지점
            y = int(screen_size['height'] * 0.6)  # 화면 높이의 60% 지점
            self.driver.tap([(x, y)])
            print(f"\niOS 알림 모달 좌표 클릭: ({x}, {y})")
        except:
            print("\niOS 알림 모달 처리 실패 - 수동 처리 필요")
    
    def skip_password_change_if_present(self):
        """비밀번호 변경 화면이 있으면 '다음에 변경' 버튼 클릭"""
        try:
            self.click_element(self._get_locator('password_skip'))
        except:
            # 비밀번호 변경 화면이 없으면 무시
            pass
    
    def terms_of_change_page(self):
        """변경된 약관 페이지"""
        try:
            self.click_element(self._get_locator('terms_of_change'))
            self.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("동의하고 계속하기").instance(0));'
            )
            self.click_element(self._get_locator('terms_of_change_go'))
        except:
            # 해당 페이지가 없으면 패스
            pass
