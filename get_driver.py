import os
os.environ['WDM_LOG_LEVEL'] = '0'
os.environ['WDM_LOCAL'] = '1'

from seleniumwire import webdriver   # QUAN TRỌNG: selenium-wire
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_driver(excelpathdownload=None, capa=None):
    """
    - Selenium 3.14.1
    - Tự động tải ChromeDriver
    - Dùng Chrome cá nhân (profile riêng)
    - Có download prefs
    - Có selenium-wire options
    """

    # ===== 1. CHROME OPTIONS =====
    options = Options()
    options.add_argument("--start-maximized")

    # 👉 DÙNG CHROME CÁ NHÂN (PROFILE RIÊNG – AN TOÀN)
    chrome_profile = r"C:/ChromeDebug"
    options.add_argument(f"--user-data-dir={chrome_profile}")

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
