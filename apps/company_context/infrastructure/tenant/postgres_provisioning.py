import os
import re
import psycopg
from psycopg import sql
from django.db import connection

class PostgreSQLTenantProvisioningService:
    """Infrastructure adapter for database-per-company provisioning.

    It creates the tenant database only. Running the tenant's migrations should be
    handled by the deployment/provisioning worker after creation.
    """
    def _db_name(self, company_code):
        prefix=os.getenv('TENANT_DB_NAME_PREFIX','school_tenant_')
        safe=re.sub(r'[^a-z0-9_]+','_',company_code.lower()).strip('_')
        return f'{prefix}{safe}'[:63]
    def provision(self, company_id, company_code):
        db_name=self._db_name(company_code)
        admin=os.getenv('TENANT_DB_ADMIN','postgres')
        password=os.getenv('TENANT_DB_PASSWORD','')
        host=os.getenv('TENANT_DB_HOST','localhost')
        port=os.getenv('TENANT_DB_PORT','5432')
        with psycopg.connect(host=host,port=port,user=admin,password=password,dbname='postgres',autocommit=True) as conn:
            exists=conn.execute('SELECT 1 FROM pg_database WHERE datname=%s',(db_name,)).fetchone()
            if not exists: conn.execute(sql.SQL('CREATE DATABASE {}').format(sql.Identifier(db_name)))
        return db_name
    def initialize(self, database_name):
        # Hook for the tenant migration runner. Do not run Django migrations from a request.
        return database_name
    def deactivate(self, database_name):
        return database_name
