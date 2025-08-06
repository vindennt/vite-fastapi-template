IMAGE_NAME = akasha-showdown-server
CONTAINER_NAME = akasha-showdown-server
PORT = 8181

.PHONY: build run stop clean make rebuild init_db

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run --rm --name $(CONTAINER_NAME) -p $(PORT):$(PORT) $(IMAGE_NAME)

stop:
	docker stop $(CONTAINER_NAME)

clean: stop
	docker rmi $(IMAGE_NAME)

make:
	$(MAKE) build
	$(MAKE) run

rebuild:
	$(MAKE) stop
	$(MAKE) build
	$(MAKE) run

init_db:
	python -m app.db.init_db