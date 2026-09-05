# Dev database, per mode

Render Phase 0 step 2 from this file when `stack.database` is not none. Pick the block for `environment.dev_database`, then the shell variant for `environment.shell`. The result ends with the `DATABASE_URL` the user puts in `.env`. SQLite needs no step: render one line saying the database file is created on first run.

## Docker Compose

Write `docker-compose.yml` at the project root during the build, then render the commands.

PostgreSQL:

```yaml
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_USER: {{slug}}
      POSTGRES_PASSWORD: {{slug}}
      POSTGRES_DB: {{slug}}
    ports:
      - "5432:5432"
    volumes:
      - db-data:/var/lib/postgresql/data
volumes:
  db-data:
```

MySQL: image `mysql:8`, environment `MYSQL_ROOT_PASSWORD`, `MYSQL_DATABASE`, `MYSQL_USER`, `MYSQL_PASSWORD`, port `3306`, volume at `/var/lib/mysql`. MongoDB: image `mongo:7`, port `27017`, volume at `/data/db`.

Commands, identical in every shell:

```
docker compose up -d
docker compose ps
```

Connection string for `.env`, PostgreSQL: `DATABASE_URL="postgresql://{{slug}}:{{slug}}@localhost:5432/{{slug}}"`. MySQL: `mysql://{{slug}}:{{slug}}@localhost:3306/{{slug}}`. MongoDB: `mongodb://localhost:27017/{{slug}}`.

The compose password is a local development password on a port only this machine reaches. Say so in one line so nobody reuses it anywhere else.

## Already installed on localhost

PostgreSQL, bash or zsh or fish:

```
createdb {{slug}}
```

PostgreSQL, PowerShell (psql is on the PATH after a standard install; otherwise use pgAdmin):

```
psql -U postgres -c "CREATE DATABASE {{slug}};"
```

MySQL, any shell:

```
mysql -u root -p -e "CREATE DATABASE {{slug}};"
```

Connection string: `DATABASE_URL="postgresql://<your user>:<your password>@localhost:5432/{{slug}}"`, with the placeholders left for the user to fill, since their local credentials are theirs. MongoDB needs no create step; the database appears on first write.

## Hosted connection string

Render two lines: "Create a database named `{{slug}}` in your provider's console, copy its connection string, and put it in `.env` as `DATABASE_URL`." Then: "Never paste it into the intake, the runbook, or a commit." No commands.

## After any mode: prove the connection

The build writes no code, so nothing project-specific can run yet. Render one check that needs only the database:

- Docker Compose, PostgreSQL: `docker compose exec db psql -U {{slug}} -d {{slug}} -c "select 1"`
- Localhost, PostgreSQL: `psql -d {{slug}} -c "select 1"`
- MySQL, either mode: `mysql -u root -p -e "select 1" {{slug}}`
- Hosted: "Open the database in your provider's console and confirm it is running."

Then one line: the first migration runs in Task 01, once the project exists.
