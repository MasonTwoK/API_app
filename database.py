# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./API_VIA_PYTHON.db"
# # If you were using a PostgreSQL database instead,
# # you would just have to uncomment the line:
# # SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# ) # connect_args={"check_same_thread": False} is needed only for SQLite.
#   # It's not needed for other databases.

# # Q: I do not understand this
# # Create a SessionLocal class
# # Each instance of the SessionLocal class will be a database session. The class itself is not a database session yet.
# # But once we create an instance of the SessionLocal class, this instance will be the actual database session.
# # We name it SessionLocal to distinguish it from the Session we are importing from SQLAlchemy.
# # We will use Session (the one imported from SQLAlchemy) later.
# # To create the SessionLocal class, use the function sessionmaker:

# # Q: What do we do in the next line?
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()