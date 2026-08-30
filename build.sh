#!/usr/bin/env bash
# Netlify から呼ばれるビルド本体。
#   記事リポジトリ(blogposts) が __posts/ に、このリポジトリが __hugo/ に置かれている前提。
set -euo pipefail

HUGO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
POSTS="${POSTS_DIR:-__posts}"

echo "▶ 豆論文リポジトリを取得（wikilink 解決に使う）"
rm -rf __published
git clone --depth 1 --quiet https://github.com/choiyaki/Published.git __published
echo "  豆論文 $(find __published -name '*.md' | wc -l | tr -d ' ') 本"

echo "▶ 記事を content/ へ変換"
rm -rf "$HUGO_ROOT/content"
python3 "$HUGO_ROOT/blogbuild.py" "$POSTS" __published "$HUGO_ROOT/content"

echo "▶ Hugo ビルド"
hugo --gc --minify --source "$HUGO_ROOT" --destination "$PWD/public"

echo "▶ 検索インデックスを生成 (Pagefind)"
# amp/ 以下は各ページの複製なので、検索結果が二重に出ないよう除いてインデックスする。
PF_SRC="$(mktemp -d)"
cp -a "$PWD/public/." "$PF_SRC/"
rm -rf "$PF_SRC/amp"
npx --yes pagefind --site "$PF_SRC"
rm -rf "$PWD/public/pagefind"
cp -a "$PF_SRC/pagefind" "$PWD/public/pagefind"
rm -rf "$PF_SRC"

echo "✅ public/ に出力しました"
