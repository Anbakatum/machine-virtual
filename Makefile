.PHONY: setup run

setup:
	-chmod +x *.sh
	-./01_system_cleanup.sh
	-./02_install_tailscale.sh
	-./03_install_sunshine.sh
	-./04_start_display.sh
	-./05_start_services.sh

run: setup
	python3 main.py
