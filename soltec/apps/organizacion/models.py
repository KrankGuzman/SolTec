from django.db import models


class Almacen(models.Model):
    almacen_id = models.SmallIntegerField(primary_key=True)
    clave = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=40)
    id_domicilio = models.SmallIntegerField(unique=True)
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'almacen'


class AlmacenComunic(models.Model):
    fk_almacen = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='FK_almacen_id', blank=True, null=True)  # Field name made lowercase.
    fk_comunic = models.ForeignKey('Comunicaciones', models.DO_NOTHING, db_column='FK_comunic_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'almacen-comunic'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Banco(models.Model):
    banco = models.OneToOneField('Cuentas', models.DO_NOTHING, primary_key=True)
    descrip = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'banco'


class Calle(models.Model):
    id_calle = models.OneToOneField('Domicilio', models.DO_NOTHING, db_column='id_calle', primary_key=True)
    id_colonia = models.SmallIntegerField()
    descrip = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'calle'


class Colonia(models.Model):
    id_colonia = models.OneToOneField('Domicilio', models.DO_NOTHING, db_column='id_colonia', primary_key=True)
    id_poblacion = models.SmallIntegerField()
    descrip = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'colonia'


class Comunicaciones(models.Model):
    comunic_id = models.SmallIntegerField(primary_key=True)
    tipo_id = models.SmallIntegerField(unique=True)
    descrip = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'comunicaciones'


class Cuentas(models.Model):
    cuenta_id = models.SmallIntegerField(primary_key=True)
    banco_id = models.SmallIntegerField(unique=True)
    rfc = models.CharField(max_length=13)
    cuenta = models.CharField(max_length=20)
    clabe = models.CharField(max_length=20)
    swift = models.CharField(max_length=20)
    moneda = models.CharField(max_length=3)
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cuentas'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Domicilio(models.Model):
    id_domicilio = models.OneToOneField('Empleado', models.DO_NOTHING, db_column='id_domicilio', primary_key=True)
    id_domicilio = models.OneToOneField('Sucursal', models.DO_NOTHING, db_column='id_domicilio', primary_key=True)
    consec = models.SmallIntegerField()
    id_pais = models.SmallIntegerField(unique=True)
    id_estado = models.SmallIntegerField(unique=True)
    id_municipio = models.SmallIntegerField(unique=True)
    id_poblacion = models.SmallIntegerField(unique=True)
    id_colonia = models.SmallIntegerField(unique=True)
    id_calle = models.SmallIntegerField(unique=True)
    calle_int = models.SmallIntegerField()
    calle_ext = models.SmallIntegerField()
    cp = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'domicilio'


class Empleado(models.Model):
    empleado_id = models.SmallIntegerField(primary_key=True)
    consec = models.SmallIntegerField()
    sucursal = models.ForeignKey('Organizacion', models.DO_NOTHING)
    rfc = models.CharField(max_length=13)
    nombre = models.CharField(max_length=80)
    ap = models.CharField(max_length=80)
    am = models.CharField(max_length=80)
    id_domicilio = models.SmallIntegerField(unique=True)
    usuario_id = models.SmallIntegerField()
    contrasena = models.CharField(max_length=20)
    correo = models.CharField(max_length=50)
    status = models.SmallIntegerField()
    puesto_id = models.SmallIntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'empleado'


class EmpleadoRol(models.Model):
    fk_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='FK_empleado_id', blank=True, null=True)  # Field name made lowercase.
    fk_rol = models.ForeignKey('Rol', models.DO_NOTHING, db_column='FK_rol_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empleado-rol'


class Estado(models.Model):
    id_pais = models.SmallIntegerField()
    id_estado = models.OneToOneField(Domicilio, models.DO_NOTHING, db_column='id_estado', primary_key=True)
    descrip = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'estado'


class Municipio(models.Model):
    id_municipio = models.OneToOneField(Domicilio, models.DO_NOTHING, db_column='id_municipio', primary_key=True)
    id_estado = models.SmallIntegerField()
    descrip = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'municipio'


class OrgAlmacen(models.Model):
    fk_id_org = models.ForeignKey('Organizacion', models.DO_NOTHING, db_column='FK_id_org', blank=True, null=True)  # Field name made lowercase.
    fk_almacen = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='FK_almacen_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'org-almacen'


class OrgAmbSist(models.Model):
    fk_id_org = models.OneToOneField('Organizacion', models.DO_NOTHING, db_column='FK_id_org', primary_key=True)  # Field name made lowercase.
    id_horario = models.SmallIntegerField()
    tiempo_logout = models.SmallIntegerField()
    color_fondo = models.TextField()  # This field type is a guess.
    color_letra = models.TextField()  # This field type is a guess.
    tipo_letra = models.CharField(max_length=40)
    formato_fecha = models.DateField()
    zona_horaria = models.SmallIntegerField()
    moneda = models.SmallIntegerField()
    logotipo = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'org-amb-sist'


class OrgBancos(models.Model):
    fk_cuenta = models.ForeignKey(Cuentas, models.DO_NOTHING, db_column='FK_cuenta_id', blank=True, null=True)  # Field name made lowercase.
    fk_id_org = models.ForeignKey('Organizacion', models.DO_NOTHING, db_column='FK_id_org', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'org-bancos'


class OrgComunic(models.Model):
    fk_id_org = models.ForeignKey('Organizacion', models.DO_NOTHING, db_column='FK_id_org', blank=True, null=True)  # Field name made lowercase.
    fk_comunic = models.ForeignKey(Comunicaciones, models.DO_NOTHING, db_column='FK_comunic_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'org-comunic'


class Organizacion(models.Model):
    id_org = models.SmallIntegerField(primary_key=True)
    consec = models.SmallIntegerField()
    sucursal_id = models.SmallIntegerField(unique=True)
    rfc = models.CharField(max_length=13)
    empresa = models.CharField(max_length=80)
    comercial = models.CharField(max_length=80)
    id_usuario = models.SmallIntegerField()
    domicilio_id = models.SmallIntegerField()
    comunic_id = models.SmallIntegerField()
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'organizacion'


class Pais(models.Model):
    id_pais = models.OneToOneField(Domicilio, models.DO_NOTHING, db_column='id_pais', primary_key=True)
    descrip = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'pais'


class Poblacion(models.Model):
    id_poblacion = models.OneToOneField(Domicilio, models.DO_NOTHING, db_column='id_poblacion', primary_key=True)
    id_municipio = models.SmallIntegerField()
    descrip = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'poblacion'


class Puesto(models.Model):
    puesto = models.OneToOneField(Empleado, models.DO_NOTHING, primary_key=True)
    descrip = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'puesto'


class Rol(models.Model):
    rol_id = models.SmallIntegerField(primary_key=True)
    descrip = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'rol'


class Sucursal(models.Model):
    fk_sucursal = models.OneToOneField(Organizacion, models.DO_NOTHING, db_column='FK_sucursal_id', primary_key=True)  # Field name made lowercase.
    clave = models.CharField(max_length=10)
    id_domicilio = models.SmallIntegerField(unique=True)
    nombre = models.CharField(max_length=80)
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'


class TipoComunic(models.Model):
    fk_tipo = models.OneToOneField(Comunicaciones, models.DO_NOTHING, db_column='FK_tipo_id', primary_key=True)  # Field name made lowercase.
    descrip = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_comunic'


class Usuario(models.Model):
    id_usuario = models.SmallIntegerField(primary_key=True)
    consec = models.SmallIntegerField()
    rfc = models.CharField(max_length=13)
    nombre = models.CharField(max_length=80)
    ap = models.CharField(max_length=80)
    am = models.CharField(max_length=80)
    contrasena = models.CharField(max_length=20)
    status_id = models.SmallIntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class UsuarioComunic(models.Model):
    fk_id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='FK_id_usuario', blank=True, null=True)  # Field name made lowercase.
    fk_comunic = models.ForeignKey(Comunicaciones, models.DO_NOTHING, db_column='FK_comunic_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario-comunic'


class UsuarioStatus(models.Model):
    fk_status = models.OneToOneField(Usuario, models.DO_NOTHING, db_column='FK_status_id', primary_key=True)  # Field name made lowercase.
    descrip = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'usuario-status'
