# base.py

Base model that gets inherited, and always has a related owner.

- This project uses Supabase Auth to identify owners and constrain records to require an owner. Change it depending on your own setup.
- Ownership and cascadings helps clean up all records during user deletion.

# users.py

Model that captures Supabase Auth's user table model.

- If using Supabase, this table is automatically created and thus should not be migrated

# Adding new models

1. Precheck: Ensure alembic is installed, initiated, and `alembic/env.py` is configured
2. Create a new `table.py` and define the table there
3. Import that model into this directory's `__init__.py`
4. `cd` into where `alembic.ini` exists and run `alembic revision --autogenerate -m "create <YOUR_TABLE_NAME> table"`
5. In the new .py file created in the versions folder, add `import sqlmodel`
6. Run `alembic upgrade head`
