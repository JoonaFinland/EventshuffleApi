First time run:
`docker volume create --name=psql-dev`

Start the backend:
`docker-compose -f docker-compose.yaml up --build`


Run tests:
`docker-compose -f docker-compose-test.yaml up --build --exit-code-from test`