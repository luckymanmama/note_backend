# Use the official Python image as the base image
FROM python:3.10-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the poetry.lock and pyproject.toml files to the container
COPY poetry.lock pyproject.toml /app/


# Install Poetry in the container
RUN pip install --no-cache-dir poetry

# Install project dependencies from the pyproject.toml file
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
COPY . /app/
RUN alembic revision --autogenerate -m "Create tables"
RUN alembic upgrade head
EXPOSE 8000
# Command to start your FastAPI app (adjust this if your app has a different startup command)
CMD ["uvicorn", "main:fastapi_app", "--host", "0.0.0.0", "--reload",  "--port", "8000"]
