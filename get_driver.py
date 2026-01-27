from seleniumwire import webdriver   # vẫn dùng selenium-wire
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import subprocess
import socket
from typing import Optional
from selenium.webdriver import Chrome

from typing import Optional
from subprocess import Popen

chrome_process: Optional[Popen] = None


driver: Optional[Chrome] = None


def is_port_open(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("127.0.0.1", port)) == 0


def get_driver(excelpathdownload=None, capa=None):
    global chrome_process

    # ===== 1. MỞ CHROME DEBUG MODE NẾU CHƯA CÓ =====
    if not is_port_open(9222):
        chrome_process = subprocess.Popen([
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            "--remote-debugging-port=9222",
            "--user-data-dir=C:/ChromeDebug",

            "--disable-session-crashed-bubble",
            "--disable-infobars",
            "--no-first-run",
            "--no-default-browser-check",
            "--disable-restore-session-state",

            "--disable-backgrounding-occluded-windows",
            "--disable-renderer-backgrounding",
            "--start-maximized"
        ])

    # ===== 2. CHROME OPTIONS =====
    options = webdriver.ChromeOptions()
    options.debugger_address = "127.0.0.1:9222"

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("window-size=1920x1480")
    options.add_argument("--disable-background-networking")
    options.add_argument("--disable-sync")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-default-apps")
    options.add_argument("--disable-gcm")
    options.add_argument("--no-first-run")
    options.add_argument("--no-service-autorun")
    options.add_argument("--disable-session-crashed-bubble")
    options.add_argument("--disable-infobars")

    # ===== 3. DOWNLOAD PREFS =====
    if excelpathdownload:
        prefs = {
            "download.default_directory": str(excelpathdownload),
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
            "profile.exit_type": "Normal",
            "profile.exited_cleanly": True
        }
        options.add_experimental_option("prefs", prefs)

    # ===== 4. SELENIUM-WIRE OPTIONS =====
    seleniumwire_options = {
        'mitmproxy_opts': ['--no-http2'],
        'filter_urls': ['gps.binhanh.vn'],
        'disable_encoding': True,
        'max_body_size': 0,
        'request_storage_base_dir': None,
        'capture_ws': False,
        'mitmproxy_logging': False,
        'ignore_patterns': [
            '*google-analytics.com*',
            '*googletagmanager.com*',
            '*gstatic.com*',
            '*google.com*',
            '*fonts.googleapis.com*',
            '*connect.facebook.net*',
            '*zalo.me*',
            '*page.widget.zalo.me*',
            '*webv2gpscenterhub.binhanh.vn*',
        ]
    }

    # ===== 5. TẠO SERVICE CHO CHROMEDRIVER (STYLE MỚI SELENIUM 4) =====
    service = Service(ChromeDriverManager().install())

    # ===== 6. KHỞI TẠO DRIVER =====
    driver = webdriver.Chrome(
        service=service,
        options=options,
        seleniumwire_options=seleniumwire_options
    )

    return driver







def reset_browser():
    import var_stx
    global driver, chrome_process

    try:
        if driver is not None:
            driver.quit()
    except Exception:
        pass

    try:
        if chrome_process is not None:
            # Ưu tiên terminate cho nhẹ, nếu chưa chết thì mới kill
            chrome_process.terminate()
            chrome_process.wait(timeout=3)
    except Exception:
        try:
            if chrome_process is not None:
                chrome_process.kill()
        except Exception:
            pass

    driver = None
    chrome_process = None

    driver = get_driver()
    var_stx.driver = driver

    return driver

