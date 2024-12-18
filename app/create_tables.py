from .database import Base, engine
# from .models import User  # Importa todos los modelos que quieras crear

# Crear todas las tablas en la base de datos vinculada al engine
Base.metadata.create_all(bind=engine)

print("Tablas creadas con éxito")
