# run in local 
## Install Poetry

    pip install poetry

## Install library

    poetry install

## Active library

    poetry shell

## Check data status

    python ./app/backend_pre_start.py

## Run migrations

    alembic upgrade head

## Initial data

    python ./app/initial_data.py

## Start

    uvicorn app.main:app --reload

If you created a new model in `./backend/app/app/models/`, make sure to import it in `./backend/app/app/db/base.py`, that Python module (`base.py`) that imports all the models will be used by Alembic.

After changing a model (for example, adding a column), inside the container, create a revision, e.g.:

    alembic revision --autogenerate -m "Add customm"


