.PHONY: docs
TEST_IMAGE_NAME := fed-install-test
TEST_CONTAINER_RUN := docker run -ti --rm -v ${PWD}:/src:Z $(TEST_IMAGE_NAME)
TEST_TARGET := tests/
MANPAGE_SOURCE_PATH := docs/fed-install.1.md
MANPAGE_PATH := docs/fed-install.1

default: test

test-container-image:
	docker build --tag=$(TEST_IMAGE_NAME) .

docs: $(MANPAGE_PATH)

$(MANPAGE_PATH): $(MANPAGE_SOURCE_PATH)
	go-md2man -in docs/fed-install.1.md -out $(MANPAGE_PATH)

test:
	$(TEST_CONTAINER_RUN) make exec-test TEST_TARGET=$(TEST_TARGET)

# install:
# 	install -m 0755 ./fed-install $(DESTDIR)/usr/bin/
# 	install -m 0644 ./docs/fed-install.1 $(DESTDIR)/usr/share/man/man1/

exec-test:
	py.test-3 -vv $(TEST_TARGET)
