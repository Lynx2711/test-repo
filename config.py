DATABASE_PASSWORD = "prod-password-123"
AWS_SECRET_KEY = "aws-secret-abc"
API_KEY = "sk-live-xyz789"
DEBUG = True

def connect_db():
    return f"postgresql://admin:prod-password-123@localhost/db"