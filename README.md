# Hackathon Backend

1. Pip install
`pip install -r requirements.txt`

2. Start Postgres local
`docker-compose -f docker-compose-postgres.yml up --build`

3. Add migration
`alembic revision --autogenerate -m "DESCRIPTION_HERE"`

4. Update migration to database
`alembic upgrade head`

5. Start server
`uvicorn src.main:app --reload --log-level debug`