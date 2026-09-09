.PHONY: setup run

setup:
	git clone https://github.com/kmille36/Colab-Cloud-Gaming.git /tmp/colab-gaming || true
	chmod +x /tmp/colab-gaming/moon-pair.sh

run: setup
	python3 main.py
