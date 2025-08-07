# Vite + FastAPI + Supabase Full-Stack Template

- React frontend powered by Vite & Mantine component library
- FastAPI backend with Docker support
- Supabase Postgres database & optional authentication

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-github-org>/vite-fastapi-template.git
cd vite-fastapi-template
```

**Install dependencies for both frontend and backend:**

```bash
cd frontend && npm install
cd ../server && pip install -r requirements.txt
cd ..
```

### 2. Backend Setup

1.  Install dependencies

    ```bash
    cd server
    pip install -r requirements.txt
    ```

1.  Configure `.env`:
    ```bash
    cp .env.example .env
    ```
    - `PROJECT_NAME`: container name
    - `PORT`: port for the server
    - `SUPABASE_URL` and `SUPABASE_KEY`: Supabase project credentials
    - `DATABASE_URL` and `DATABASE_KEY`: Credentials for Postgres database
1.  Initialize the database, creating a super user, initializing tables, and data:
    ```bash
    make init_db
    ```
1.  Build and run the Docker container:

    ```bash
    make build
    make run

    # QoL
    make make      # Runs build + run
    make rebuild   # Runs stop + build + run if a container is already running
    ```

1.  Stop or clean up:
    ```bash
    make stop     # stops the running container
    make clean    # removes the image
    ```

#### Database Migrations

1. Install Alembic (if not already installed):
   ```bash
   pip install alembic
   ```
2. Create a new migration script:
   ```bash
   alembic revision --autogenerate -m "Initial migration"
   ```
3. Apply migrations:
   ```bash
   alembic upgrade head
   ```
   Read more about how to use Alembic [here](https://alembic.sqlalchemy.org/en/latest/tutorial.html).

### 3. Frontend Setup

1. Install dependencies

   ```bash
   cd frontend
   npm install
   ```

1. Copy and configure `.env`
   ```bash
   cp .env.example .env
   ```
   - `VITE_API_URL`: backend URL (e.g. `http://localhost:8181`)
   - `VITE_SUPABASE_URL` and `VITE_SUPABASE_KEY`: your Supabase credentials
1. Start the dev server:
   ```bash
   npm run dev
   ```

## Makefile Info

Optional command lines that might make dev experience a bit smoother.

Usage:

```bash
make <target>                             # At the respective root
make -C /full/path/to/project <target>    # From anywhere else
```

#### Frontend Makefile

| Target | Description                            |
| ------ | -------------------------------------- |
| `run`  | Launch Vite dev server (`npm run dev`) |

#### Backend Makefile

| Target    | Description                                                                                     |
| --------- | ----------------------------------------------------------------------------------------------- |
| `build`   | Build the Docker image (`docker build -t $(IMAGE_NAME) .`)                                      |
| `run`     | Run the container (`docker run --rm --name $(CONTAINER_NAME) -p $(PORT):$(PORT) $(IMAGE_NAME)`) |
| `stop`    | Stop the running container (`docker stop $(CONTAINER_NAME)`)                                    |
| `clean`   | Stop container and remove image (`make stop && docker rmi $(IMAGE_NAME)`)                       |
| `make`    | Alias for `build` + `run`                                                                       |
| `rebuild` | Stop, build, and run again                                                                      |
| `init_db` | Initialize database and seed initial data (`python -m app.db.init_db`)                          |

##

Backend builds upon [AtticusZeller's FastAPI template](https://github.com/AtticusZeller/fastapi_supabase_template).
