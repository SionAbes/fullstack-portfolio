
run-backend:
	docker-compose -p dev -f fastapi-master-api/docker-compose.yaml build --force-rm --pull --build-arg BUILDKIT_INLINE_CACHE=1
	docker-compose -p dev -f fastapi-master-api/docker-compose.yaml up -d -V

clean:
	docker-compose -p dev -f fastapi-master-api/docker-compose.yaml down -v --remove-orphans

openapi-generate: openapi-generate-fastapi

openapi-generate-fastapi:
	rm -rf fastapi-master-api/app/api/tmp/ && \
	rm -rf fastapi-master-api/app/api/models && \
	mkdir -p fastapi-master-api/app/api/models && \
	docker run --rm \
    --user $(shell id -u):$(shell id -g) \
    -v $(shell pwd):/local openapitools/openapi-generator-cli:$(OPENAPI_GEN_VERSION) generate \
    -i "/local$(API_SPEC)" \
    -g python-fastapi \
    -o /local/fastapi-master-api/app/api/tmp/ \
    --global-property models \
    --additional-properties=packageName=app.api && \
    mv fastapi-master-api/app/api/tmp/src/app/api/models/* fastapi-master-api/app/api/models/ && \
  	rm -rf fastapi-master-api/app/api/tmp/

openapi-serve:
	cd openapi-spec && \
	yarn serve
	
pre-commit-init:
	pre-commit install --install-hooks

pre-commit-update:
	pre-commit autoupdate
	
test-fastapi:
	docker-compose -p test -f utils/pytest/docker-compose.fastapi.yml up -d
	docker-compose -p test -f utils/pytest/docker-compose.fastapi.yml logs --follow api-fastapi

clean-test-fastapi:
	docker-compose -p test -f utils/pytest/docker-compose.fastapi.yml down -v --remove-orphans