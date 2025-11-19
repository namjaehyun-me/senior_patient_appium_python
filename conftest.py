import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from base_driver import BaseDriver
from pages.login_page import LoginPage
import time

def pytest_addoption(parser):
    """pytest 명령행 옵션 추가"""
    try:
        parser.addoption(
            "--platform", 
            action="store", 
            default="android", 
            help="플랫폼 선택: android 또는 ios"
        )
    except ValueError:
        # --platform 옵션이 이미 존재하는 경우 무시
        pass

@pytest.fixture(scope="session")
def platform(request):
    """세션 범위 플랫폼 설정"""
    return request.config.getoption("--platform")

@pytest.fixture(scope="function")
def driver_setup(platform, request):
    """드라이버 설정 및 자동 로그인 미들웨어 (test_login.py 제외)"""
    print(f"\n=== 테스트 환경 설정 시작 (플랫폼: {platform}) ===")
    
    # 드라이버 초기화
    base_driver = BaseDriver(platform)
    driver = base_driver.start_driver()
    login_page = LoginPage(driver)
    wait = WebDriverWait(driver, 10)
    
    # test_login.py인 경우 자동 로그인 건너뛰기
    if "test_login" in request.node.fspath.basename:
        print("\n🔓 로그인 테스트 파일 - 자동 로그인 건너뛰기")
    else:
        # 자동 로그인 수행
        print("\n🔐 자동 로그인 시작...")
        try:
            # 팝업 처리
            login_page.close_popup_if_present()
            time.sleep(1)
            
            # 로그인 상태 확인
            if not login_page.is_logged_in():
                print("로그인이 필요합니다. 자동 로그인을 진행합니다.")
                
                # 로그인 수행
                login_page.enter_input("evankim2", "userid")
                login_page.enter_input("teammapa123@", "password")
                login_page.click_login()
                
                # 로그인 후 처리
                time.sleep(1)
                login_page.skip_password_change_if_present()
                time.sleep(1)
                login_page.allow_permission_if_present()
                time.sleep(1)
                
                print("✅ 자동 로그인 완료")
            else:
                print("✅ 이미 로그인된 상태입니다.")
                
        except Exception as e:
            print(f"❌ 자동 로그인 실패: {e}")
            # 로그인 실패해도 테스트는 계속 진행
            pass
    
    print("=== 테스트 환경 설정 완료 ===\n")
    
    # 테스트에 필요한 객체들 반환
    yield {
        'driver': driver,
        'base_driver': base_driver,
        'login_page': login_page,
        'wait': wait,
        'platform': platform
    }
    
    # 테스트 완료 후 정리
    print("\n=== 테스트 환경 정리 시작 ===")
    base_driver.quit_driver()
    print("=== 테스트 환경 정리 완료 ===")

@pytest.fixture(scope="function")
def ensure_login(driver_setup, request):
    """테스트 중 로그인 상태 재확인 (필요시 사용, test_login.py 제외)"""
    def _ensure_login():
        # test_login.py인 경우 재로그인 건너뛰기
        if "test_login" in request.node.fspath.basename:
            print("\n🔓 로그인 테스트 파일 - 재로그인 건너뛰기")
            return
            
        driver = driver_setup['driver']
        login_page = driver_setup['login_page']
        
        if not login_page.is_logged_in():
            print("\n🔄 로그인 상태가 해제되었습니다. 재로그인을 진행합니다.")
            login_page.enter_input("evankim2", "userid")
            login_page.enter_input("teammapa123@", "password")
            login_page.click_login()
            
            time.sleep(2)
            login_page.skip_password_change_if_present()
            time.sleep(1)
            login_page.allow_permission_if_present()
            time.sleep(2)
            print("✅ 재로그인 완료")
    
    return _ensure_login

@pytest.fixture(scope="function")
def toast_analyzer(driver_setup):
    """토스트 메시지 분석 미들웨어"""
    def _analyze_toast(timeout=5, expected_messages=None):
        """
        토스트 메시지를 분석하고 결과를 반환
        
        Args:
            timeout (int): 토스트 대기 시간 (초)
            expected_messages (list): 예상되는 메시지 목록
            
        Returns:
            dict: {
                'found': bool,
                'message': str,
                'type': str,  # 'success', 'error', 'warning', 'info'
                'matched_expected': bool
            }
        """
        driver = driver_setup['driver']
        platform = driver_setup['platform']
        wait = WebDriverWait(driver, timeout)
        
        result = {
            'found': False,
            'message': '',
            'type': 'unknown',
            'matched_expected': False
        }
        
        # 플랫폼별 토스트 선택자
        toast_selectors = {
            'android': [
                (AppiumBy.XPATH, "//android.widget.Toast"),
                (AppiumBy.XPATH, "//*[contains(@class, 'Toast')]"),
                (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, '성공') or contains(@text, '실패') or contains(@text, '오류') or contains(@text, '완료')]"),
                (AppiumBy.XPATH, "//android.widget.TextView[@text='아이디/이메일 또는 비밀번호를 잘못 입력했습니다.']"),
                (AppiumBy.XPATH, "//android.widget.TextView[@text='이 필드는 필수 항목입니다!']"),
                (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, '로그인')]"),
                (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, '로그아웃')]"),
                (AppiumBy.XPATH, "//*[contains(@text, '저장') or contains(@text, '삭제') or contains(@text, '수정')]"),
            ],
            'ios': [
                (AppiumBy.XPATH, "//XCUIElementTypeAlert"),
                (AppiumBy.XPATH, "//XCUIElementTypeStaticText[contains(@name, '성공') or contains(@name, '실패') or contains(@name, '오류')]"),
                (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='아이디/이메일 또는 비밀번호를 잘못 입력했습니다.']"),
                (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='이 필드는 필수 항목입니다!']"),
            ]
        }
        
        print(f"\n🔍 토스트 메시지 분석 시작 ({platform}, {timeout}초 대기)...")
        
        # 토스트 메시지 찾기
        for selector in toast_selectors.get(platform, []):
            try:
                element = wait.until(EC.presence_of_element_located(selector))
                if element.is_displayed():
                    message = element.get_attribute('text') or element.get_attribute('name') or element.text
                    if message:
                        result['found'] = True
                        result['message'] = message.strip()
                        result['type'] = _classify_message_type(message)
                        
                        # 예상 메시지와 비교
                        if expected_messages:
                            result['matched_expected'] = any(expected in message for expected in expected_messages)
                        
                        print(f"✅ 토스트 발견: '{message}' (타입: {result['type']})")
                        return result
            except:
                continue
        
        # 토스트를 찾지 못한 경우
        print("❌ 토스트 메시지를 찾지 못했습니다.")
        return result
    
    def _classify_message_type(message):
        """메시지 내용에 따른 타입 분류"""
        message_lower = message.lower()
        
        # 성공 메시지
        success_keywords = ['성공', '완료', '저장', 'success', 'complete', 'saved']
        if any(keyword in message_lower for keyword in success_keywords):
            return 'success'
        
        # 오류 메시지
        error_keywords = ['오류', '실패', '잘못', '필수', 'error', 'failed', 'wrong', 'invalid']
        if any(keyword in message_lower for keyword in error_keywords):
            return 'error'
        
        # 경고 메시지
        warning_keywords = ['경고', '주의', 'warning', 'caution']
        if any(keyword in message_lower for keyword in warning_keywords):
            return 'warning'
        
        # 정보 메시지
        info_keywords = ['알림', '정보', 'info', 'notice']
        if any(keyword in message_lower for keyword in info_keywords):
            return 'info'
        
        return 'unknown'
    
    return _analyze_toast

@pytest.fixture(scope="function")
def toast_helper(toast_analyzer):
    """토스트 도우미 함수들"""
    def wait_for_success_toast(timeout=5):
        """성공 토스트 대기"""
        result = toast_analyzer(timeout=timeout)
        return result['found'] and result['type'] == 'success'
    
    def wait_for_error_toast(timeout=5, expected_errors=None):
        """오류 토스트 대기"""
        result = toast_analyzer(timeout=timeout, expected_messages=expected_errors)
        return result['found'] and result['type'] == 'error'
    
    def assert_toast_message(expected_message, timeout=5):
        """특정 토스트 메시지 확인"""
        result = toast_analyzer(timeout=timeout, expected_messages=[expected_message])
        assert result['found'], f"토스트 메시지를 찾지 못했습니다."
        assert expected_message in result['message'], f"예상 메시지 '{expected_message}'를 찾지 못했습니다. 실제: '{result['message']}'"
        return result
    
    return {
        'wait_for_success': wait_for_success_toast,
        'wait_for_error': wait_for_error_toast,
        'assert_message': assert_toast_message,
        'analyze': toast_analyzer
    }

@pytest.fixture(scope="function")
def error_checker(driver_setup):
    """오류 확인 미들웨어 - 모든 행동 후 자동 오류 감지"""
    def _check_errors(action_name="액션", timeout=3):
        """
        현재 화면에서 오류 상황을 확인
        
        Args:
            action_name (str): 수행한 액션 이름
            timeout (int): 오류 감지 대기 시간
            
        Returns:
            dict: {
                'has_error': bool,
                'error_type': str,  # 'crash', 'toast_error', 'dialog_error', 'network_error', 'none'
                'error_message': str,
                'action_name': str
            }
        """
        driver = driver_setup['driver']
        platform = driver_setup['platform']
        wait = WebDriverWait(driver, timeout)
        
        result = {
            'has_error': False,
            'error_type': 'none',
            'error_message': '',
            'action_name': action_name
        }
        
        print(f"\n🔍 '{action_name}' 후 오류 확인 시작...")
        
        # 1. 앱 크래시 확인
        try:
            current_activity = driver.current_activity
            if not current_activity or 'crash' in current_activity.lower():
                result['has_error'] = True
                result['error_type'] = 'crash'
                result['error_message'] = f"앱 크래시 감지: {current_activity}"
                print(f"❌ 앱 크래시 감지: {current_activity}")
                return result
        except Exception as e:
            result['has_error'] = True
            result['error_type'] = 'crash'
            result['error_message'] = f"드라이버 연결 오류: {str(e)}"
            print(f"❌ 드라이버 연결 오류: {e}")
            return result
        
        # 2. 오류 대화상자 확인
        error_dialog_selectors = {
            'android': [
                (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, '오류') or contains(@text, '실패') or contains(@text, 'Error') or contains(@text, 'Failed')]"),
                (AppiumBy.XPATH, "//android.app.AlertDialog"),
                (AppiumBy.XPATH, "//android.widget.Button[@text='확인' or @text='OK' or @text='닫기']"),
                (AppiumBy.ID, "android:id/message"),
                (AppiumBy.XPATH, "//*[contains(@text, '네트워크') and contains(@text, '오류')]"),
                (AppiumBy.XPATH, "//*[contains(@text, '서버') and contains(@text, '오류')]"),
            ],
            'ios': [
                (AppiumBy.XPATH, "//XCUIElementTypeAlert"),
                (AppiumBy.XPATH, "//XCUIElementTypeStaticText[contains(@name, '오류') or contains(@name, 'Error')]"),
                (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='확인' or @name='OK']"),
            ]
        }
        
        for selector in error_dialog_selectors.get(platform, []):
            try:
                element = wait.until(EC.presence_of_element_located(selector))
                if element.is_displayed():
                    error_text = element.get_attribute('text') or element.get_attribute('name') or element.text or '알 수 없는 오류'
                    result['has_error'] = True
                    result['error_type'] = 'dialog_error'
                    result['error_message'] = error_text.strip()
                    print(f"❌ 오류 대화상자 발견: '{error_text}'")
                    return result
            except:
                continue
        
        # 3. 오류 토스트 확인
        toast_error_selectors = {
            'android': [
                (AppiumBy.XPATH, "//android.widget.Toast"),
                (AppiumBy.XPATH, "//android.widget.TextView[@text='아이디/이메일 또는 비밀번호를 잘못 입력했습니다.']"),
                (AppiumBy.XPATH, "//android.widget.TextView[@text='이 필드는 필수 항목입니다!']"),
                (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, '실패') or contains(@text, '오류')]"),
            ],
            'ios': [
                (AppiumBy.XPATH, "//XCUIElementTypeStaticText[contains(@name, '실패') or contains(@name, '오류')]"),
            ]
        }
        
        for selector in toast_error_selectors.get(platform, []):
            try:
                element = wait.until(EC.presence_of_element_located(selector))
                if element.is_displayed():
                    toast_text = element.get_attribute('text') or element.get_attribute('name') or element.text
                    if toast_text and ('오류' in toast_text or '실패' in toast_text or '잘못' in toast_text or '필수' in toast_text):
                        result['has_error'] = True
                        result['error_type'] = 'toast_error'
                        result['error_message'] = toast_text.strip()
                        print(f"❌ 오류 토스트 발견: '{toast_text}'")
                        return result
            except:
                continue
        
        # 4. 네트워크 오류 확인
        network_error_selectors = {
            'android': [
                (AppiumBy.XPATH, "//*[contains(@text, '네트워크') or contains(@text, '인터넷') or contains(@text, '연결')]"),
                (AppiumBy.XPATH, "//*[contains(@text, 'Network') or contains(@text, 'Internet') or contains(@text, 'Connection')]"),
            ],
            'ios': [
                (AppiumBy.XPATH, "//XCUIElementTypeStaticText[contains(@name, '네트워크') or contains(@name, 'Network')]"),
            ]
        }
        
        for selector in network_error_selectors.get(platform, []):
            try:
                element = wait.until(EC.presence_of_element_located(selector))
                if element.is_displayed():
                    network_text = element.get_attribute('text') or element.get_attribute('name') or element.text
                    if network_text:
                        result['has_error'] = True
                        result['error_type'] = 'network_error'
                        result['error_message'] = network_text.strip()
                        print(f"❌ 네트워크 오류 발견: '{network_text}'")
                        return result
            except:
                continue
        
        # 오류가 없는 경우
        print(f"✅ '{action_name}' 수행 후 오류 없음")
        return result
    
    return _check_errors

@pytest.fixture(scope="function")
def safe_action(driver_setup, error_checker):
    """안전한 액션 수행 미들웨어 - 모든 행동 후 자동 오류 검사"""
    def _safe_click(locator, action_name="클릭", timeout=10):
        """안전한 클릭 수행"""
        driver = driver_setup['driver']
        wait = WebDriverWait(driver, timeout)
        
        try:
            print(f"\n👆 {action_name} 시도 중...")
            element = wait.until(EC.element_to_be_clickable(locator))
            element.click()
            time.sleep(1)  # 액션 완료 대기
            
            # 오류 검사
            error_result = error_checker(action_name)
            if error_result['has_error']:
                print(f"⚠️ {action_name} 후 오류 발생: {error_result['error_message']}")
                return {'success': False, 'error': error_result}
            
            print(f"✅ {action_name} 성공")
            return {'success': True, 'error': None}
            
        except Exception as e:
            print(f"❌ {action_name} 실패: {str(e)}")
            return {'success': False, 'error': {'has_error': True, 'error_type': 'action_failed', 'error_message': str(e)}}
    
    def _safe_send_keys(locator, text, action_name="텍스트 입력", timeout=10):
        """안전한 텍스트 입력"""
        driver = driver_setup['driver']
        wait = WebDriverWait(driver, timeout)
        
        try:
            print(f"\n✏️ {action_name} 시도 중: '{text}'")
            element = wait.until(EC.element_to_be_clickable(locator))
            element.clear()
            element.send_keys(text)
            time.sleep(1)
            
            # 오류 검사
            error_result = error_checker(action_name)
            if error_result['has_error']:
                print(f"⚠️ {action_name} 후 오류 발생: {error_result['error_message']}")
                return {'success': False, 'error': error_result}
            
            print(f"✅ {action_name} 성공")
            return {'success': True, 'error': None}
            
        except Exception as e:
            print(f"❌ {action_name} 실패: {str(e)}")
            return {'success': False, 'error': {'has_error': True, 'error_type': 'action_failed', 'error_message': str(e)}}
    
    def _safe_swipe(start_x, start_y, end_x, end_y, action_name="스와이프", duration=1000):
        """안전한 스와이프"""
        driver = driver_setup['driver']
        
        try:
            print(f"\n👆 {action_name} 시도 중...")
            driver.swipe(start_x, start_y, end_x, end_y, duration)
            time.sleep(1)
            
            # 오류 검사
            error_result = error_checker(action_name)
            if error_result['has_error']:
                print(f"⚠️ {action_name} 후 오류 발생: {error_result['error_message']}")
                return {'success': False, 'error': error_result}
            
            print(f"✅ {action_name} 성공")
            return {'success': True, 'error': None}
            
        except Exception as e:
            print(f"❌ {action_name} 실패: {str(e)}")
            return {'success': False, 'error': {'has_error': True, 'error_type': 'action_failed', 'error_message': str(e)}}
    
    return {
        'click': _safe_click,
        'send_keys': _safe_send_keys,
        'swipe': _safe_swipe,
        'check_errors': error_checker
    }