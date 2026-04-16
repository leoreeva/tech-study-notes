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
  curl -L -o /tmp/jdk17.tar.gz \
    https://github.com/adoptium/temurin17-binaries/releases/latest/download/OpenJDK17U-jdk_x64_linux_hotspot.tar.gz
  mkdir -p "$JAVA_DIR"
  tar -xzf /tmp/jdk17.tar.gz -C "$JAVA_DIR" --strip-components=1
fi

export JAVA_HOME="$JAVA_DIR"
export PATH="$JAVA_HOME/bin:$QD_DIR/bin:$PATH"

java -version

echo "Installing Puppeteer locally..."
npm init -y --prefix "$QD_LIB" >/dev/null 2>&1 || true
npm install puppeteer --prefix "$QD_LIB"

echo "Installing Quarkdown locally..."
curl -L https://github.com/iamgio/quarkdown/releases/latest/download/quarkdown.zip -o /tmp/quarkdown.zip
rm -rf /tmp/quarkdown-unzip
mkdir -p /tmp/quarkdown-unzip
unzip -q /tmp/quarkdown.zip -d /tmp/quarkdown-unzip
rm -rf "$QD_DIR/bin" "$QD_DIR/libexec" "$QD_DIR/lib" "$QD_DIR/share" 2>/dev/null || true
cp -r /tmp/quarkdown-unzip/quarkdown/* "$QD_DIR/"

export QD_NPM_PREFIX="$QD_LIB"
export PUPPETEER_CACHE_DIR="$PUPPETEER_CACHE_DIR"

echo "Quarkdown version:"
"$QD_DIR/bin/quarkdown" --version

echo "Building site..."
"$QD_DIR/bin/quarkdown" c main.qd
