#!/bin/bash
export DEBIAN_FRONTEND=noninteractive
set -e

echo "=== 1/5. Limpando travas do APT/DPKG ==="
sudo killall apt apt-get dpkg 2>/dev/null || true
sudo rm -f /var/lib/apt/lists/lock /var/cache/apt/archives/lock /var/lib/dpkg/lock*
sudo dpkg --configure -a --force-confold
