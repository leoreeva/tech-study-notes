#!/usr/bin/env bash
set -euo pipefail

ROOT="$PWD"
TOOLS="$ROOT/.tools"
JAVA_DIR="$TOOLS/java"
QD_DIR="$TOOLS/quarkdown"
QD_LIB="$QD_DIR/lib"
PUPPETEER_CACHE_DIR="$QD_LIB/puppeteer_cache"

mkdir -p "$TOOLS" "$QD_DIR" "$QD_LIB" "$PUPPETEER_CACHE_DIR"

echo "Checking Node/npm..."
node --version
npm --version

echo "Installing Java locally..."
if [ ! -x "$JAVA_DIR/bin/java" ]; then
  curl -fsSL \
    "https://api.adoptium.net/v3/binary/latest/17/ga/linux/x64/jre/hotspot/normal/eclipse" \
    -o /tmp/java17.tar.gz
  mkdir -p "$JAVA_DIR"
  tar -xzf /tmp/java17.tar.gz -C "$JAVA_DIR" --strip-components=1
fi

export JAVA_HOME="$JAVA_DIR"
export PATH="$JAVA_HOME/bin:$QD_DIR/bin:$PATH"

java -version

echo "Installing Quarkdown locally..."
curl -fsSL \
  "https://github.com/iamgio/quarkdown/releases/latest/download/quarkdown.zip" \
  -o /tmp/quarkdown.zip
rm -rf /tmp/quarkdown-unzip
mkdir -p /tmp/quarkdown-unzip
unzip -q /tmp/quarkdown.zip -d /tmp/quarkdown-unzip

rm -rf "$QD_DIR/bin" "$QD_DIR/libexec" "$QD_DIR/share"
cp -r /tmp/quarkdown-unzip/quarkdown/* "$QD_DIR/"

echo "Quarkdown version:"
"$QD_DIR/bin/quarkdown" --version

echo "Building site..."
"$QD_DIR/bin/quarkdown" c main.qd
