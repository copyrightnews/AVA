#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SERVICE_FILE="$SCRIPT_DIR/ava-ui.service"

if [ ! -f "$SERVICE_FILE" ]; then
  echo "Error: ava-ui.service not found in $SCRIPT_DIR"
  exit 1
fi

echo "Installing AVA UI service..."
echo "Make sure you've edited ava-ui.service with your username and paths first!"
echo ""

sudo cp "$SERVICE_FILE" /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable ava-ui
sudo systemctl start ava-ui
sudo systemctl status ava-ui
