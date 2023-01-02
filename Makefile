install:
	pip install -r ci/requirements.txt

build:
	python ci/build.py

py-test:
	black ci/
