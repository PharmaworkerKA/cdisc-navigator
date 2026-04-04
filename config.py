"""CDISC Standards Navigator - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "CDISC Standards Navigator"
BLOG_DESCRIPTION = (
    "CDISCデータ標準（SDTM・ADaM・Define-XML）の実務ノウハウを毎日更新。"
    "海外の最新規制動向を日本語で翻訳・要約し、現場で使えるコード例とともに解説。"
)
BLOG_URL = "https://pharmaworkerka.github.io/cdisc-navigator"
BLOG_TAGLINE = "CDISC標準の実務情報を日本語で発信"
BLOG_LANGUAGE = "ja"

GITHUB_REPO = "PharmaworkerKA/cdisc-navigator"
GITHUB_BRANCH = "gh-pages"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

TARGET_CATEGORIES = [
    "SDTM実装ガイド",
    "ADaM設計パターン",
    "Define-XML",
    "Pinnacle 21・バリデーション",
    "CDISC最新アップデート",
    "規制当局対応",
    "SASコード実践",
    "海外トレンド翻訳",
]

THEME = {
    "primary": "#2563eb",
    "accent": "#1e3a5f",
    "gradient_start": "#2563eb",
    "gradient_end": "#1d4ed8",
    "dark_bg": "#0f172a",
    "dark_surface": "#1e293b",
    "light_bg": "#f0f9ff",
    "light_surface": "#ffffff",
}

MAX_ARTICLE_LENGTH = 4000
ARTICLES_PER_DAY = 1
SCHEDULE_HOURS = [8]

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 75
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

AFFILIATE_LINKS = {
    "SAS認定資格": {
        "url": "https://www.sas.com/ja_jp/certification.html",
        "text": "SAS認定資格を取得する",
        "description": "SASプログラミングの公式認定",
    },
    "Amazon CDISC書籍": {
        "url": "https://www.amazon.co.jp",
        "text": "AmazonでCDISC関連書籍を探す",
        "description": "CDISC・臨床データ標準の参考書",
    },
    "Udemy SAS講座": {
        "url": "https://www.udemy.com",
        "text": "UdemyでSAS/CDISC講座を探す",
        "description": "動画で学ぶCDISC実装",
    },
    "楽天 医薬品開発書籍": {
        "url": "https://www.rakuten.co.jp",
        "text": "楽天で医薬品開発の書籍を探す",
        "description": "製薬・臨床開発の参考書",
    },
}
AFFILIATE_TAG = "musclelove07-22"

ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")
ADSENSE_ENABLED = bool(ADSENSE_CLIENT_ID)

DASHBOARD_HOST = "127.0.0.1"
DASHBOARD_PORT = 8090

# Google Analytics (GA4)
GOOGLE_ANALYTICS_ID = "G-CSFVD34MKK"

# Google Search Console 認証ファイル
SITE_VERIFICATION_FILES = {
    "googlea31edabcec879415.html": "google-site-verification: googlea31edabcec879415.html",
}
