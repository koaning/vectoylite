commit:
	nbdev_clean
	nbdev_export
	git add .
	git commit -m "Added more stuff"

install:
	python -m pip install -e .