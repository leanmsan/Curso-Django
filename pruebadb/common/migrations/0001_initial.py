# Generated by Django 4.2 on 2023-05-03 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bateria',
            fields=[
                ('idbateria', models.IntegerField(db_column='idBateria', primary_key=True, serialize=False)),
                ('amperajebateria', models.IntegerField(blank=True, db_column='amperajeBateria', null=True)),
                ('voltajebateria', models.IntegerField(blank=True, db_column='voltajeBateria', null=True)),
                ('tipobateria', models.CharField(blank=True, db_column='tipoBateria', max_length=60, null=True)),
            ],
            options={
                'db_table': 'bateria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Filtro',
            fields=[
                ('idfiltro', models.IntegerField(db_column='idFiltro', primary_key=True, serialize=False)),
                ('tipofiltro', models.CharField(blank=True, db_column='tipoFiltro', max_length=60, null=True)),
                ('vehiculofiltro', models.CharField(blank=True, db_column='vehiculoFiltro', max_length=100, null=True)),
            ],
            options={
                'db_table': 'filtro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lampara',
            fields=[
                ('idlampara', models.IntegerField(db_column='idLampara', primary_key=True, serialize=False)),
                ('voltajelampara', models.IntegerField(blank=True, db_column='voltajeLampara', null=True)),
                ('wattslampara', models.IntegerField(blank=True, db_column='wattsLampara', null=True)),
                ('tipolampara', models.CharField(blank=True, db_column='tipoLampara', max_length=60, null=True)),
            ],
            options={
                'db_table': 'lampara',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movimientos',
            fields=[
                ('idmovimiento', models.IntegerField(db_column='idMovimiento', primary_key=True, serialize=False)),
                ('tipomovimiento', models.CharField(blank=True, db_column='tipoMovimiento', max_length=10, null=True)),
                ('fechamovimiento', models.DateField(blank=True, db_column='fechaMovimiento', null=True)),
                ('horamovimiento', models.TimeField(blank=True, db_column='horaMovimiento', null=True)),
                ('cantidadmovimiento', models.IntegerField(blank=True, db_column='cantidadMovimiento', null=True)),
                ('preciomovimiento', models.DecimalField(blank=True, db_column='precioMovimiento', decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'movimientos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('idpersona', models.IntegerField(db_column='idPersona', primary_key=True, serialize=False)),
                ('apellidopersona', models.CharField(blank=True, db_column='apellidoPersona', max_length=80, null=True)),
                ('nombrepersona', models.CharField(blank=True, db_column='nombrePersona', max_length=80, null=True)),
            ],
            options={
                'db_table': 'persona',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idproducto', models.AutoField(db_column='idProducto', primary_key=True, serialize=False)),
                ('nombreproducto', models.CharField(blank=True, db_column='nombreProducto', max_length=200, null=True)),
                ('preciocompra', models.DecimalField(blank=True, db_column='precioCompra', decimal_places=2, max_digits=10, null=True)),
                ('precioventa', models.DecimalField(blank=True, db_column='precioVenta', decimal_places=2, max_digits=10, null=True)),
                ('marcaproducto', models.CharField(blank=True, db_column='marcaProducto', max_length=100, null=True)),
                ('descripcionproducto', models.CharField(blank=True, db_column='descripcionProducto', max_length=100, null=True)),
                ('stockproducto', models.IntegerField(blank=True, db_column='stockProducto', null=True)),
                ('rubroproducto', models.CharField(blank=True, db_column='rubroProducto', max_length=10, null=True)),
            ],
            options={
                'db_table': 'producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('cuit', models.IntegerField(db_column='CUIT', primary_key=True, serialize=False)),
                ('nombreopcional', models.CharField(blank=True, db_column='nombreOpcional', max_length=120, null=True)),
                ('direccionproveedor', models.CharField(blank=True, db_column='direccionProveedor', max_length=120, null=True)),
                ('telefonoproveedor', models.CharField(blank=True, db_column='telefonoProveedor', max_length=20, null=True)),
                ('correoproveedor', models.CharField(blank=True, db_column='correoProveedor', max_length=60, null=True)),
            ],
            options={
                'db_table': 'proveedor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idusuario', models.IntegerField(db_column='idUsuario', primary_key=True, serialize=False)),
                ('usuario', models.CharField(blank=True, max_length=15, null=True)),
                ('pass_field', models.CharField(blank=True, db_column='pass', max_length=15, null=True)),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Llanta',
            fields=[
                ('idllanta', models.OneToOneField(db_column='idLlanta', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='common.producto')),
                ('rodadollanta', models.IntegerField(blank=True, db_column='rodadoLlanta', null=True)),
                ('anchollanta', models.IntegerField(blank=True, db_column='anchoLlanta', null=True)),
                ('cantidadagujeros', models.IntegerField(blank=True, db_column='cantidadAgujeros', null=True)),
                ('distribucionagujeros', models.CharField(blank=True, db_column='distribucionAgujeros', max_length=50, null=True)),
                ('materialllanta', models.CharField(blank=True, db_column='materialLlanta', max_length=30, null=True)),
            ],
            options={
                'db_table': 'llanta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lubricentro',
            fields=[
                ('idlubricentro', models.OneToOneField(db_column='idLubricentro', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='common.producto')),
                ('descripcionlubricentro', models.CharField(blank=True, db_column='descripcionLubricentro', max_length=250, null=True)),
                ('medidalubricentro', models.CharField(blank=True, db_column='medidaLubricentro', max_length=50, null=True)),
                ('tipolubricentro', models.CharField(blank=True, db_column='tipoLubricentro', max_length=100, null=True)),
                ('idproducto', models.IntegerField(db_column='idProducto')),
            ],
            options={
                'db_table': 'lubricentro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Neumatico',
            fields=[
                ('idneumatico', models.OneToOneField(db_column='idNeumatico', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='common.producto')),
                ('rodadoneumatico', models.IntegerField(blank=True, db_column='rodadoNeumatico', null=True)),
                ('perfilneumatico', models.IntegerField(blank=True, db_column='perfilNeumatico', null=True)),
                ('anchoneumatico', models.IntegerField(blank=True, db_column='anchoNeumatico', null=True)),
                ('indicevelocidad', models.CharField(blank=True, db_column='indiceVelocidad', max_length=10, null=True)),
                ('indicecarga', models.CharField(blank=True, db_column='indiceCarga', max_length=10, null=True)),
                ('tiponeumatico', models.CharField(blank=True, db_column='tipoNeumatico', max_length=50, null=True)),
            ],
            options={
                'db_table': 'neumatico',
                'managed': False,
            },
        ),
    ]
