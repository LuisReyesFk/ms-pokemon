from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurar la URL de conexión a la base de datos PostgreSQL existente
SQLALCHEMY_DATABASE_URL = "postgresql://luis:finkargo@localhost/fastapi_db"

# Crear el motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear la sesión local de la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarar el modelo base
Base = declarative_base()
