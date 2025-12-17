import os
import time
import subprocess
#17/12
os.environ['WDM_LOG_LEVEL'] = '0'
os.environ['WDM_LOCAL'] = '1'

from seleniumwire import webdriver   # QUAN TRỌNG: selenium-wire
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_driver(excelpathdownload=None, capa=None):
    subprocess.Popen([
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "--remote-debugging-port=9222",
        "--user-data-dir=C:/ChromeDebug",
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

    # ===== DOWNLOAD PREFS (GIỮ LOGIC CŨ CỦA BẠN) =====
    if excelpathdownload:
        prefs = {
            "download.default_directory": str(excelpathdownload),
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
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
