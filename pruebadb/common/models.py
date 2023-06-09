from django.db import models

# Create your models here.
class Bateria(models.Model):
    idbateria = models.IntegerField(db_column='idBateria', primary_key=True)  # Field name made lowercase.
    amperajebateria = models.IntegerField(db_column='amperajeBateria', blank=True, null=True)  # Field name made lowercase.
    voltajebateria = models.IntegerField(db_column='voltajeBateria', blank=True, null=True)  # Field name made lowercase.
    tipobateria = models.CharField(db_column='tipoBateria', max_length=60, blank=True, null=True)  # Field name made lowercase.
    idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='idProducto')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bateria'


class Filtro(models.Model):
    idfiltro = models.IntegerField(db_column='idFiltro', primary_key=True)  # Field name made lowercase.
    tipofiltro = models.CharField(db_column='tipoFiltro', max_length=60, blank=True, null=True)  # Field name made lowercase.
    vehiculofiltro = models.CharField(db_column='vehiculoFiltro', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='idProducto')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'filtro'


class Lampara(models.Model):
    idlampara = models.IntegerField(db_column='idLampara', primary_key=True)  # Field name made lowercase.
    voltajelampara = models.IntegerField(db_column='voltajeLampara', blank=True, null=True)  # Field name made lowercase.
    wattslampara = models.IntegerField(db_column='wattsLampara', blank=True, null=True)  # Field name made lowercase.
    tipolampara = models.CharField(db_column='tipoLampara', max_length=60, blank=True, null=True)  # Field name made lowercase.
    idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='idProducto')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lampara'


class Llanta(models.Model):
    idllanta = models.OneToOneField('Producto', models.DO_NOTHING, db_column='idLlanta', primary_key=True)  # Field name made lowercase.
    rodadollanta = models.IntegerField(db_column='rodadoLlanta', blank=True, null=True)  # Field name made lowercase.
    anchollanta = models.IntegerField(db_column='anchoLlanta', blank=True, null=True)  # Field name made lowercase.
    cantidadagujeros = models.IntegerField(db_column='cantidadAgujeros', blank=True, null=True)  # Field name made lowercase.
    distribucionagujeros = models.CharField(db_column='distribucionAgujeros', max_length=50, blank=True, null=True)  # Field name made lowercase.
    materialllanta = models.CharField(db_column='materialLlanta', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'llanta'


class Lubricentro(models.Model):
    idlubricentro = models.OneToOneField('Producto', models.DO_NOTHING, db_column='idLubricentro', primary_key=True)  # Field name made lowercase.
    descripcionlubricentro = models.CharField(db_column='descripcionLubricentro', max_length=250, blank=True, null=True)  # Field name made lowercase.
    medidalubricentro = models.CharField(db_column='medidaLubricentro', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tipolubricentro = models.CharField(db_column='tipoLubricentro', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idproducto = models.IntegerField(db_column='idProducto')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lubricentro'


class Movimientos(models.Model):
    idmovimiento = models.IntegerField(db_column='idMovimiento', primary_key=True)  # Field name made lowercase.
    idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='idProducto', blank=True, null=True)  # Field name made lowercase.
    tipomovimiento = models.CharField(db_column='tipoMovimiento', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fechamovimiento = models.DateField(db_column='fechaMovimiento', blank=True, null=True)  # Field name made lowercase.
    horamovimiento = models.TimeField(db_column='horaMovimiento', blank=True, null=True)  # Field name made lowercase.
    cantidadmovimiento = models.IntegerField(db_column='cantidadMovimiento', blank=True, null=True)  # Field name made lowercase.
    preciomovimiento = models.DecimalField(db_column='precioMovimiento', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movimientos'


class Neumatico(models.Model):
    idneumatico = models.OneToOneField('Producto', models.DO_NOTHING, db_column='idNeumatico', primary_key=True)  # Field name made lowercase.
    rodadoneumatico = models.IntegerField(db_column='rodadoNeumatico', blank=True, null=True)  # Field name made lowercase.
    perfilneumatico = models.IntegerField(db_column='perfilNeumatico', blank=True, null=True)  # Field name made lowercase.
    anchoneumatico = models.IntegerField(db_column='anchoNeumatico', blank=True, null=True)  # Field name made lowercase.
    indicevelocidad = models.CharField(db_column='indiceVelocidad', max_length=10, blank=True, null=True)  # Field name made lowercase.
    indicecarga = models.CharField(db_column='indiceCarga', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tiponeumatico = models.CharField(db_column='tipoNeumatico', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'neumatico'


class Persona(models.Model):
    idpersona = models.IntegerField(db_column='idPersona', primary_key=True)  # Field name made lowercase.
    apellidopersona = models.CharField(db_column='apellidoPersona', max_length=80, blank=True, null=True)  # Field name made lowercase.
    nombrepersona = models.CharField(db_column='nombrePersona', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'persona'


class Producto(models.Model):
    idproducto = models.AutoField(db_column='idProducto', primary_key=True)  # Field name made lowercase.
    nombreproducto = models.CharField(db_column='nombreProducto', max_length=200, blank=True, null=True)  # Field name made lowercase.
    preciocompra = models.DecimalField(db_column='precioCompra', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    precioventa = models.DecimalField(db_column='precioVenta', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    marcaproducto = models.CharField(db_column='marcaProducto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    descripcionproducto = models.CharField(db_column='descripcionProducto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    stockproducto = models.IntegerField(db_column='stockProducto', blank=True, null=True)  # Field name made lowercase.
    rubroproducto = models.CharField(db_column='rubroProducto', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedor(models.Model):
    cuit = models.IntegerField(db_column='CUIT', primary_key=True)  # Field name made lowercase.
    nombreopcional = models.CharField(db_column='nombreOpcional', max_length=120, blank=True, null=True)  # Field name made lowercase.
    direccionproveedor = models.CharField(db_column='direccionProveedor', max_length=120, blank=True, null=True)  # Field name made lowercase.
    telefonoproveedor = models.CharField(db_column='telefonoProveedor', max_length=20, blank=True, null=True)  # Field name made lowercase.
    correoproveedor = models.CharField(db_column='correoProveedor', max_length=60, blank=True, null=True)  # Field name made lowercase.
    idpersona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='idPersona')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proveedor'


class Usuario(models.Model):
    idusuario = models.IntegerField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    usuario = models.CharField(max_length=15, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=15, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    idpersona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='idPersona', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'
