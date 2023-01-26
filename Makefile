file := VERSION
variable := $(shell cat ${file})

build:
	python setup.py bdist_wheel
	rm -rf build
deploy:
	python -m twine upload dist/cloud_watch_logs-${variable}-py3-none-any.whl
