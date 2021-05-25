# Greetings API

This is a simple greetings API. It sets an initial greeting of "hello world", but also gives the user the option to add additional greetings.

## Overview

The Greetings API has four routes:
 * GET
   * `/` - redirects to OpenAPI/Swagger interactive API documentation (`/docs`)
   * `/greetings/` - returns a JSON response list of greetings from the database
   * `/greetings/{greeting_id}` - returns a JSON response of greeting, based on the greeting's id (`{greeting_id}`) in the database.
     ```json
     {"message":"hello world","id":1}
     ```
 * POST
   * `/greetings/` - creates a greeting if a matching one does not already exist.
     Expects a JSON payload of `{"message":"<greeting message>"}`

## Running the API

The API can be run via Docker Compose:

 * Docker compose
   
   ```bash
   docker-compose up -d
   ```

## Using the API

The API path for retrieving greetings is `/greetings/`.  One can visit in the browser http://localhost:8000/greetings/
or via curl command `curl http://localhost:8000/greetings/`

This returns a JSON array of existing greetings stored in the database.

Other options for using the API include:

### Create Greeting

```bash
curl -X 'POST' \
  'http://localhost:8000/greetings/' \
  -H 'Content-Type: application/json' \
  -d '{
  "message": "howdy"
}'
```

### Retrieve Specific Greeting

Example for getting the greeting with id=1

```bash
curl -X 'GET' 'http://localhost:8000/greetings/1'
```

### Alternative to cURL (Using the Swagger UI)

The Greetings API uses FastAPI, which includes interactive API documentation (provided by [Swagger UI](https://github.com/swagger-api/swagger-ui)). Open in the browser by visiting http://localhost:8000/docs (or get redirected from http://localhost:8000/)

