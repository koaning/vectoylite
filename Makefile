commit:
	python -m pip install --upgrade nbdev
	nbdev_clean
	nbdev_export
	git add .
	git commit -m "Added more stuff"

install:
	python -m pip install -e . nbdev pre-commit
	pre-commit install
	nbdev_install_hooks
