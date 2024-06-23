from fastcrud import FastCRUD

from .models import User, EmailLog

crud_users = FastCRUD(User)
crud_email_logs = FastCRUD(EmailLog)
