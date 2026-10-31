# -*- coding: utf-8 -*-
"""Unit tests for Python Playwright Stealth Scraper Kit."""
import unittest
import sys
from pathlib import Path

# Add parent directory to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from stealth_scraper import CONFIG, EVASION_SCRIPTS

class TestStealthScraper(unittest.TestCase):
    def test_config_wallets(self):
        """Verify wallet configuration addresses are present and valid."""
        wallets = CONFIG.get("WALLETS", {})
        self.assertIn("TON", wallets)
        self.assertIn("USDT_TRC20", wallets)
        self.assertIn("EVM", wallets)
        self.assertIn("SOLANA", wallets)
        self.assertTrue(wallets["TON"].startswith("UQ"))
        self.assertTrue(wallets["USDT_TRC20"].startswith("T"))
        self.assertTrue(wallets["EVM"].startswith("0x"))

    def test_evasion_scripts(self):
        """Verify stealth evasion scripts contain essential anti-fingerprinting patches."""
        scripts_joined = " ".join(EVASION_SCRIPTS)
        self.assertIn("navigator, 'webdriver'", scripts_joined)
        self.assertIn("window.chrome", scripts_joined)
        self.assertIn("plugins", scripts_joined)
        self.assertIn("languages", scripts_joined)

    def test_config_defaults(self):
        """Verify default configuration flags."""
        self.assertTrue(CONFIG.get("HEADLESS"))
        self.assertEqual(CONFIG.get("USER_DATA_DIR"), ".stealth_profile")

if __name__ == "__main__":
    unittest.main()
