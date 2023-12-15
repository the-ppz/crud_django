*******************************************************************
    ***** Creando Maquinas Virtuales *****
    0 - Crear la carpeta y entrar en ella

    1 - Crear Maquina Virtual  
        python -m venv prueba1

    2 - Entrar a la subcarpeta Scripts
        activate -> para apagar la maquina virtual -> deactivate

    3 - Instalar Django y todo lo necesario como Base de Datos, etc
        pip install django
    
    4 - Nota siempre estar en el entorno virtual activo

    5 - Regresar a la carpeta Raiz del proyecto

    6 - Verificar Paquetes de nuestro Entorno Virtual
        pip freeze --local
*******************************************************************


*******************************************************************
    ***** Creando Proyecto Web *****
    	django-admin startproject proyecto1
	django-admin startproject proyecto1 .  -> Me crea una sola carpeta  

    2 - Verificar si esta corriendo -> NOTA: Estar sobre el proyecto (Proyecto Web - Primera Carpeta)
        python manage.py runserver
*******************************************************************


*******************************************************************
    ***** Crear la App *****
    - Dentro de la Carpeta del Proyecto Web    	
	python manage.py startapp clientes
*******************************************************************


*******************************************************************
    ***** Comandos para las Migraciones de los Modelos *****
    - OJO la Maquina Virtual debe estar prendida
    
    - en admin.py:
	from .models import *
	admin.site.register(SO) -> para cada modelo creado    	

    - En la carpeta del Proyecto Web:
	python manage.py migrate
	python manage.py makemigrations
*******************************************************************


*******************************************************************
    ***** Crear Administrador *****
    - En la carpeta del Proyecto Web:
	python manage.py createsuperuser

	frank 1234
*******************************************************************


*******************************************************************
    ***** Instalar Django-crispy-forms *****
    - En la carpeta del Proyecto Web:
	pip install django-crispy-forms
    - En settings.py del proyecto (Proyecto Web - Segunda Carpeta o Carpeta con el mismo nombre del Proyecto)
	INSTALLED_APPS = [
	   	'crispy_forms',
	]
	CRISPY_TEMPLATE_PACK='bootstrap4'

