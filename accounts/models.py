from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

#Creando clase para hacer un account normal
class MyAccountManager(BaseUserManager):
    
    def create_user(self, username, first_name, last_name, email, phone_number, password=None):

        #Verificando que tenga email y username
        if not email:
            raise ValueError('Falta Email.') #raise sirve para disparar una respuesta en caso de que algo se cumpla
        if not username:
            raise ValueError('Falta nombre de usuario.')
        #Fin de la verificacion
        if not phone_number:
            raise ValueError('Falta numero telefonico')

        #Creando el objeto usuario, se usa self para crear el propio objeto de su propia clase modelo
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number,
        )

        user.set_password(password) #Para el password se debe usar la funcion setPassword
        user.save(using=self._db) #los administradores predeterminando de Django usan using para definir en la base de datos subyacente que
        #debe usar el administrador para poder guardarlo, es opcional, es para definir a cual base de datos usara el admin
        #Leer esta pagina para mas informacion https://stackoverflow.com/questions/57667334/what-is-the-value-of-self-db-by-default-in-django
        return user
        
        # Creando un super usuario
    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            first_name=first_name,
            last_name= last_name,
            username= username,
            password = password,
        )

        #Seteandoles las propiedades del admin a este objeto, recuerda, se puede usar cualquier atributo desde la clase de los modelos creados abajo en class User
        user.is_admin = True
        user.is_staff = True
        user.is_superadmin = True
        user.is_active = True
        #fin del seteo

        user.save(using=self._db)
        return user


#fin de la clase


#AbstractBaseUser es una funcion de django para personalizar el usuario
class User(AbstractBaseUser):

    #Campos opcionales para creacion de usuario (personalizadas)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20)
    company_name = models.CharField(max_length=150, blank=True, default='')

    #Fin de campos opcionales

    #Campos obligatorios que pide django para creacion de usuario
    date_joined = models.DateTimeField(auto_now=True) # auto_now es inalterable, se usa para definir el momento que se creo
    last_login = models.DateTimeField(auto_now_add=True) # auto_now_add, se usa para actualizar la fecha de la ultima modificacion
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    #Fin de campos obligatorios

    USERNAME_FIELD = 'email' # Para pedir iniciar sesion con el correo en vez de con el nombre de usuario

    #Campos requeridos para crearse un usuario 
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    #Instanciando el objeto para poder crear los usuarios
    objects = MyAccountManager()

    def __str__(self):
        return self.email

    # Funcion para verificar si tiene permisos de administrador
    def has_perm(self, perm, obj=None):
        return self.is_admin
    # Fin de funcion para verificar permisos

    # Funcion para darle permisos de los modulos en caso de ser admin
    def has_module_perms(self, add_label):
        return True
    # Fin de funcion