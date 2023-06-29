from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password):
        if not email:
            raise ValueError('Email is required!')
        if not nickname:
            raise ValueError('full name is required')

        user = self.model(email=self.normalize_email(email), nickname=nickname)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, nickname, password):
        user = self.create_user(email, nickname, password)
        user.is_admin = True
        user.save(using=self.db)
        return user
