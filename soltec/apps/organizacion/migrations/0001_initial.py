# Generated by Django 2.0.6 on 2020-08-05 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('almacen_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('clave', models.CharField(max_length=10)),
                ('descripcion', models.CharField(max_length=40)),
                ('id_domicilio', models.SmallIntegerField(unique=True)),
                ('status', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'almacen',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AlmacenComunic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'almacen-comunic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comunicaciones',
            fields=[
                ('comunic_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('tipo_id', models.SmallIntegerField(unique=True)),
                ('descrip', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'comunicaciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cuentas',
            fields=[
                ('cuenta_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('banco_id', models.SmallIntegerField(unique=True)),
                ('rfc', models.CharField(max_length=13)),
                ('cuenta', models.CharField(max_length=20)),
                ('clabe', models.CharField(max_length=20)),
                ('swift', models.CharField(max_length=20)),
                ('moneda', models.CharField(max_length=3)),
                ('status', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'cuentas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('empleado_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('consec', models.SmallIntegerField()),
                ('rfc', models.CharField(max_length=13)),
                ('nombre', models.CharField(max_length=80)),
                ('ap', models.CharField(max_length=80)),
                ('am', models.CharField(max_length=80)),
                ('id_domicilio', models.SmallIntegerField(unique=True)),
                ('usuario_id', models.SmallIntegerField()),
                ('contrasena', models.CharField(max_length=20)),
                ('correo', models.CharField(max_length=50)),
                ('status', models.SmallIntegerField()),
                ('puesto_id', models.SmallIntegerField(unique=True)),
            ],
            options={
                'db_table': 'empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmpleadoRol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'empleado-rol',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrgAlmacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'org-almacen',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Organizacion',
            fields=[
                ('id_org', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('consec', models.SmallIntegerField()),
                ('sucursal_id', models.SmallIntegerField(unique=True)),
                ('rfc', models.CharField(max_length=13)),
                ('empresa', models.CharField(max_length=80)),
                ('comercial', models.CharField(max_length=80)),
                ('id_usuario', models.SmallIntegerField()),
                ('domicilio_id', models.SmallIntegerField()),
                ('comunic_id', models.SmallIntegerField()),
                ('status', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'organizacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrgBancos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'org-bancos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrgComunic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'org-comunic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('rol_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('descrip', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'rol',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('consec', models.SmallIntegerField()),
                ('rfc', models.CharField(max_length=13)),
                ('nombre', models.CharField(max_length=80)),
                ('ap', models.CharField(max_length=80)),
                ('am', models.CharField(max_length=80)),
                ('contrasena', models.CharField(max_length=20)),
                ('status_id', models.SmallIntegerField(unique=True)),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsuarioComunic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'usuario-comunic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('banco', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='organizacion.Cuentas')),
                ('descrip', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'banco',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrgAmbSist',
            fields=[
                ('fk_id_org', models.OneToOneField(db_column='FK_id_org', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='organizacion.Organizacion')),
                ('id_horario', models.SmallIntegerField()),
                ('tiempo_logout', models.SmallIntegerField()),
                ('color_fondo', models.TextField()),
                ('color_letra', models.TextField()),
                ('tipo_letra', models.CharField(max_length=40)),
                ('formato_fecha', models.DateField()),
                ('zona_horaria', models.SmallIntegerField()),
                ('moneda', models.SmallIntegerField()),
                ('logotipo', models.BinaryField()),
            ],
            options={
                'db_table': 'org-amb-sist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('puesto', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='organizacion.Empleado')),
                ('descrip', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'puesto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('fk_sucursal', models.OneToOneField(db_column='FK_sucursal_id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='organizacion.Organizacion')),
                ('clave', models.CharField(max_length=10)),
                ('id_domicilio', models.SmallIntegerField(unique=True)),
                ('nombre', models.CharField(max_length=80)),
                ('status', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'sucursal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoComunic',
            fields=[
                ('fk_tipo', models.OneToOneField(db_column='FK_tipo_id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='organizacion.Comunicaciones')),
                ('descrip', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tipo_comunic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsuarioStatus',
            fields=[
                ('fk_status', models.OneToOneField(db_column='FK_status_id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='organizacion.Usuario')),
                ('descrip', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'usuario-status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id_domicilio', models.OneToOneField(db_column='id_domicilio', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='organizacion.Sucursal')),
                ('consec', models.SmallIntegerField()),
                ('id_pais', models.SmallIntegerField(unique=True)),
                ('id_estado', models.SmallIntegerField(unique=True)),
                ('id_municipio', models.SmallIntegerField(unique=True)),
                ('id_poblacion', models.SmallIntegerField(unique=True)),
                ('id_colonia', models.SmallIntegerField(unique=True)),
                ('id_calle', models.SmallIntegerField(unique=True)),
                ('calle_int', models.SmallIntegerField()),
                ('calle_ext', models.SmallIntegerField()),
                ('cp', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'domicilio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Calle',
            fields=[
                ('id_calle', models.OneToOneField(db_column='id_calle', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='organizacion.Domicilio')),
                ('id_colonia', models.SmallIntegerField()),
                ('descrip', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'calle',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Colonia',
            fields=[
                ('id_colonia', models.OneToOneField(db_column='id_colonia', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='organizacion.Domicilio')),
                ('id_poblacion', models.SmallIntegerField()),
                ('descrip', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'colonia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id_pais', models.SmallIntegerField()),
                ('id_estado', models.OneToOneField(db_column='id_estado', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='organizacion.Domicilio')),
                ('descrip', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'estado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id_municipio', models.OneToOneField(db_column='id_municipio', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='organizacion.Domicilio')),
                ('id_estado', models.SmallIntegerField()),
                ('descrip', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'municipio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id_pais', models.OneToOneField(db_column='id_pais', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='organizacion.Domicilio')),
                ('descrip', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'pais',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Poblacion',
            fields=[
                ('id_poblacion', models.OneToOneField(db_column='id_poblacion', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='organizacion.Domicilio')),
                ('id_municipio', models.SmallIntegerField()),
                ('descrip', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'poblacion',
                'managed': False,
            },
        ),
    ]
