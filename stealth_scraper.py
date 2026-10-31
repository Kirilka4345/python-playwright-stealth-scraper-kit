# -*- coding: utf-8 -*-
"""Synchronous browser-automation example. Patches do not guarantee access."""
import sys
import json
import time
import random
from pathlib import Path
from playwright.sync_api import sync_playwright

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

CONFIG = {
    "HEADLESS": True,
    "USER_DATA_DIR": ".stealth_profile",
    "WALLETS": {
        "TON": "UQCwrgVAYHvlJe87-eOAK01ZzMW42E17YnbCyWPPkKeLhEpP",
        "USDT_TRC20": "TXCYzTR3Br4MuWXUnGRvpA3EaYC7iyydYj",
        "EVM": "0x12f0a957bd351492252aac81198edba4c5a56790",
        "SOLANA": "2N9dzxxt3AQRfN52FAN4W3VXvVz1aCcfXdGgwi7sHaiD8"
    }
}

EVASION_SCRIPTS = [
    "Object.defineProperty(navigator, 'webdriver', {get: () => undefined});",
    "window.chrome = { runtime: {}, loadTimes: function() {}, csi: function() {}, app: {} };",
    "Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5]});",
    "Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});",
]

def run_stealth_scrape(target_url: str):
    print(f"[*] Starting stealth scrape on: {target_url}")
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=CONFIG["USER_DATA_DIR"],
            headless=CONFIG["HEADLESS"],
            args=[
                "--disable-dev-shm-usage",
                "--disable-blink-features=AutomationControlled",
                "--disable-infobars"
            ],
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
        )
        page = context.pages[0] if context.pages else context.new_page()
        for script in EVASION_SCRIPTS:
            page.add_init_script(script)

        page.goto(target_url, wait_until="domcontentloaded", timeout=30000)
        time.sleep(random.uniform(1.5, 3.0))

        title = page.title()
        content_len = len(page.content())
        print(f"[+] Successfully scraped '{title}' ({content_len} bytes)")
        context.close()
        return {"title": title, "bytes": content_len}

if __name__ == "__main__":
    test_url = "https://example.com"
    run_stealth_scrape(test_url)
