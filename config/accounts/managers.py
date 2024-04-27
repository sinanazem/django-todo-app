from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    
    def create_user(self,email, first_name, last_name, phone_number, password):
        if not email:
            raise ValueError("User Must have email!")
        
        if not first_name:
            raise ValueError("User Must have first_name!")
        
        if not last_name:
            raise ValueError("User Must have last_name!")
        
        if not phone_number:
            raise ValueError("User Must have phone_number!")
        
        user = self.model(email=self.normalize_email(email),
                          first_name=first_name,
                          last_name=last_name,
                          phone_number=phone_number)
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, first_name, last_name, phone_number, password):
        
        user = self.create_user(email=email,
                                first_name=first_name,
                                last_name=last_name,
                                phone_number=phone_number,
                                password=password)
        user.is_admin = True
        user.save(using=self._db)
        
        return user