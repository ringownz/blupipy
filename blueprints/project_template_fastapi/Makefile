#answers?="default_project\n default_project\n shortdescription\n \n \n \n Default Person\n default@email.com\n \n \n"
answers?= answers.txt
output=$(shell pwd)/projects/

help:  ## Show help
	# From https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

init:  ## Initialize builder container
	docker build -t project_template_fastapi .

create: ## Creates new project
	docker run -it --rm -v "$(shell pwd):/project_template_fastapi" project_template_fastapi create
	cp -a output/. $(output)
	rm -Rf output/

clean:  # Removes build container
	docker image rm project_template_fastapi
