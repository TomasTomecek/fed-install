TEST_IMAGE_NAME := fed-install-test
TEST_CONTAINER_RUN := docker run -t --rm -v ${PWD}:/src:Z $(TEST_IMAGE_NAME)

default: test

test-container-image:
	docker build --tag=$(TEST_IMAGE_NAME) .

test: test-container-image
	$(TEST_CONTAINER_RUN) make exec-test

exec-test:
	py.test-3 -vv tests
