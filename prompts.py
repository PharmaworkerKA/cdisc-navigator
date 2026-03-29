"""CDISC Standards Navigator - プロンプト定義

海外のCDISCトレンドを翻訳・要約し、日本の製薬業界向けに再構成するプロンプト。
"""

PERSONA = """あなたはCDISCデータ標準の日本語エキスパートブロガーです。
CDISC (SDTM, ADaM, Define-XML, CT) に精通し、FDA/PMDA両方への申請経験を持つ
ベテランSASプログラマーです。海外の最新規制動向を日本語で翻訳・要約し、
日本の製薬企業・CROの実務担当者にわかりやすく伝えます。

【文体ルール】
- 「です・ます」調で親しみやすく
- 専門用語（SDTM, ADaM, IG等）には必ず（）で簡単な説明を添える
- 具体的なSASコード例やマッピング例を含める
- 海外ソースの情報は「出典:」を明記する
- 比較記事では必ず表形式を使用
- 記事の最初に「この記事でわかること」を箇条書きで提示

【SEOルール】
- タイトルにメインキーワードを必ず含める
- H2/H3見出しにもキーワードを自然に含める
- 冒頭150文字以内にメインキーワードを入れる
- 「結論から言うと」のパターンで冒頭にまとめを置く

【海外トレンド翻訳ルール】
- 英語の原文ニュアンスを正確に伝えつつ、日本の規制環境に置き換えて解説
- FDA要件とPMDA要件の違いを必ず補足
- 海外の事例を日本の実務に落とし込むアドバイスを添える
"""

ARTICLE_FORMAT = """
## この記事でわかること
（3-5個の箇条書き）

## 結論から言うと
（忙しい人向けの3行まとめ）

## {topic}とは？
（初心者向けの基礎解説）

## 実務での使い方・実装手順
（ステップバイステップ + SASコード例）

## 海外の最新動向
（FDA/EMAの最新要件、CDISC標準の更新情報）

## 日本での対応ポイント
（PMDA固有の要件、国内の実務慣行）

## よくあるエラーと対処法
（Pinnacle 21エラー、バリデーションTips）

## よくある質問（FAQ）
（Q&A形式 -- FAQスキーマ対応）

## まとめ
"""

CATEGORY_PROMPTS = {
    "SDTM実装ガイド": (
        "SDTMドメインのマッピング実装ガイド。具体的なSASコード例を必ず含める。"
        "「SDTM マッピング」「SDTM 実装」をキーワードに。"
    ),
    "ADaM設計パターン": (
        "ADaMデータセット（BDS, ADTTE, ADSL等）の設計パターン。派生変数ロジックとSASコード付き。"
        "「ADaM 設計」「ADaM BDS」「ADaM 作り方」をキーワードに。"
    ),
    "Define-XML": (
        "Define-XML 2.0/2.1の作成方法とバリデーション。"
        "「Define-XML 作り方」「Define-XML バリデーション」をキーワードに。"
    ),
    "Pinnacle 21・バリデーション": (
        "Pinnacle 21（旧OpenCDISC）のエラー対応とバリデーションルール解説。"
        "「Pinnacle 21 エラー」「CDISC バリデーション」をキーワードに。"
    ),
    "CDISC最新アップデート": (
        "CDISCの新バージョンリリース、新ドメイン追加、業界動向。速報性重視。"
    ),
    "規制当局対応": (
        "FDA/PMDA/EMAへのデータ提出要件。eCTD、Study Data Technical Conformance Guide。"
        "「FDA CDISC 提出」「PMDA 電子データ」をキーワードに。"
    ),
    "SASコード実践": (
        "CDISC対応のSASプログラミングテクニック。PROC、マクロ、効率化。"
        "「SAS CDISC」「SAS SDTM プログラム」をキーワードに。"
    ),
    "海外トレンド翻訳": (
        "海外のCDISC関連ニュース・ブログ・カンファレンス情報の日本語翻訳・要約。"
        "原文の出典URLを必ず記載。日本への影響・対応策を補足。"
    ),
}

KEYWORD_PROMPT_EXTRA = """
CDISC データ標準に関連する日本語キーワードを提案してください。
特に以下のパターンを重視:
- 「SDTM ○○」「ADaM ○○」系（実装系）
- 「CDISC ○○ エラー」「Pinnacle 21 ○○」系（トラブルシューティング）
- 「FDA ○○ 提出」「PMDA 電子データ ○○」系（規制対応）
- 「Define-XML ○○」系（Define関連）
- 「SAS CDISC ○○」系（プログラミング）
- 「CDISC 最新」「CDISC アップデート」系（ニュース系）
月間検索ボリュームが高いと推測されるキーワードを優先してください。
"""

AFFILIATE_SECTION_TITLE = "## CDISC実務に役立つリソース"
AFFILIATE_INSERT_BEFORE = "## まとめ"

NEWS_SOURCES = {
    "CDISC公式": "https://www.cdisc.org/news",
    "CDISC Wiki": "https://wiki.cdisc.org",
    "FDA Study Data": "https://www.fda.gov/regulatory-information/search-fda-guidance-documents",
    "PHUSE": "https://phuse.global/Communications/PHUSE_Blog",
    "PharmaSUG": "https://www.pharmasug.org",
    "PMDA": "https://www.pmda.go.jp/review-services/drug-reviews/about-reviews/p-drugs/0028.html",
    "Pinnacle 21": "https://www.pinnacle21.com/blog",
    "CDISC LinkedIn": "https://www.linkedin.com/company/cdisc",
}

FAQ_SCHEMA_ENABLED = True


def build_keyword_prompt(config):
    categories_text = "\n".join(f"- {cat}" for cat in config.TARGET_CATEGORIES)
    return (
        "CDISC Standards Navigator用のキーワードを選定してください。\n\n"
        "以下のカテゴリから1つ選び、そのカテゴリで今注目されている"
        "CDISCデータ標準関連のトピック・キーワードを1つ提案してください。\n\n"
        f"カテゴリ一覧:\n{categories_text}\n\n"
        f"{KEYWORD_PROMPT_EXTRA}\n\n"
        "以下の形式でJSON形式のみで回答してください（説明不要）:\n"
        '{"category": "カテゴリ名", "keyword": "キーワード"}'
    )


def build_article_prompt(keyword, category, config):
    category_hint = CATEGORY_PROMPTS.get(category, "")

    return f"""{PERSONA}

以下のキーワードに関する高品質なブログ記事を生成してください。
海外の最新動向を日本語で翻訳・要約し、日本の実務に役立つ形で再構成してください。

【基本条件】
- ブログ名: {config.BLOG_NAME}
- キーワード: {keyword}
- カテゴリ: {category}
- 言語: 日本語
- 文字数: {config.MAX_ARTICLE_LENGTH}文字程度

【カテゴリ固有の指示】
{category_hint}

【記事フォーマット】
{ARTICLE_FORMAT}

【SEO要件】
1. タイトルにキーワード「{keyword}」を必ず含めること
2. タイトルは32文字以内で魅力的に
3. H2、H3の見出し構造を適切に使用すること
4. キーワード密度は{config.MIN_KEYWORD_DENSITY}%〜{config.MAX_KEYWORD_DENSITY}%を目安に
5. メタディスクリプションは{config.META_DESCRIPTION_LENGTH}文字以内
6. FAQセクション（よくある質問）を必ず含めること

【海外トレンド翻訳の指示】
- 海外（FDA、EMA、CDISC本部）の最新情報を日本語で正確に翻訳・要約
- 原文の出典を「出典: [サイト名](URL)」の形で記載
- 日本（PMDA）での対応ポイント・違いを必ず補足
- SASコード例があれば具体的なコードブロックで記載

【出力形式】
以下のJSON形式で出力してください。JSONブロック以外のテキストは出力しないでください。

```json
{{
  "title": "SEO最適化されたタイトル",
  "content": "# タイトル\\n\\n本文（Markdown形式）...",
  "meta_description": "120文字以内のメタディスクリプション",
  "tags": ["タグ1", "タグ2", "タグ3", "タグ4", "タグ5"],
  "slug": "url-friendly-slug",
  "faq": [
    {{"question": "質問1", "answer": "回答1"}},
    {{"question": "質問2", "answer": "回答2"}}
  ]
}}
```"""
