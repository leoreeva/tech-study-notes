#!/usr/bin/env bash
set -e

# Example: install Quarkdown, then build
# Adjust this to your preferred install method/version.
curl -fsSL https://raw.githubusercontent.com/quarkdown-labs/get-quarkdown/main/install.sh | bash

export PATH="$HOME/.local/bin:$PATH"

quarkdown c main.qd
