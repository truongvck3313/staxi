import os
import time
import subprocess
#18/12
os.environ['WDM_LOG_LEVEL'] = '0'
os.environ['WDM_LOCAL'] = '1'
import socket
from seleniumwire import webdriver   # QUAN TRỌNG: selenium-wire
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from typing import Optional
from selenium.webdriver import Chrome

driver: Optional[Chrome] = None
chrome_process = None





def is_port_open(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("127.0.0.1", port)) == 0



def get_driver(excelpathdownload=None, capa=None):
    global chrome_process

    # ====== PHẦN THÊM (CHỈ THÊM) ======
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

    # Kết nối Selenium với Chrome thật
    options = webdriver.ChromeOptions()
    options.debugger_address = "127.0.0.1:9222"
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('window-size=1920x1480')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('window-size=1920x1480')
    options.add_argument("--disable-background-networking")
    options.add_argument("--disable-sync")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-default-apps")
    options.add_argument("--disable-gcm")          # <-- FIX LỖI LOG CỦA BẠN
    options.add_argument("--no-first-run")
    options.add_argument("--no-service-autorun")
    options.add_argument("--disable-session-crashed-bubble")
    options.add_argument("--disable-infobars")

    # ===== DOWNLOAD PREFS (GIỮ LOGIC CŨ CỦA BẠN) =====
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

    # ===== SELENIUM-WIRE OPTIONS (CHỐNG HTTP2) =====
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

    # ===== 2. AUTO TẢI CHROME DRIVER =====
    driver_path = ChromeDriverManager().install()

    # ===== 3. KHỞI TẠO DRIVER =====
    driver = webdriver.Chrome(
        driver_path,
        options=options,
        desired_capabilities=capa,
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
        driver.quit()
    except:
        pass

    driver = None
    chrome_process = None

    driver = get_driver()

    # 🔥 DÒNG QUYẾT ĐỊNH
    var_stx.driver = driver

    return driver












