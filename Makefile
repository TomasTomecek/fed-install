.PHONY: docs
TEST_IMAGE_NAME := fed-install-test
TEST_CONTAINER_RUN := docker run -t --rm -v ${PWD}:/src:Z $(TEST_IMAGE_NAME)
MANPAGE_PATH := docs/fed-install.1

default: test

test-container-image:
	docker build --tag=$(TEST_IMAGE_NAME) .

docs: $(MANPAGE_PATH)

$(MANPAGE_PATH):
	go-md2man -in docs/fed-install.1.md -out $(MANPAGE_PATH)

test:
	$(TEST_CONTAINER_RUN) make exec-test

exec-test:
	py.test-3 -vv tests
