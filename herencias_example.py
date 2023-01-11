class canino(models.Model):
    _name = 'canino'
    _description = 'Clase base para caninos'
    
    largo_cola = fields.Integer(string="largo cola", required=False, )
    tipo_oreja = fields.Char(string="tipo oreja", required=False, )
   
class perro(models.Model):
    _name = 'perro'
    _inherit = 'canino'
    _description = 'Clase para perros crea nueva tabla que hereda de caninos'
    
    raza = fields.Selection(string="Raza", selection=[('sh', 'Sharpei'), 
                                                      ('do', 'Dobberman')], required=False, )
class zorro(models.Model):
    _inherit = 'canno'
    _description = 'Extiende la clase base caninos y le añade nuevo campo para color de pelaje'
    
    color_pelaje = fields.Char(string="Color Pelaje", required=False, )
    
