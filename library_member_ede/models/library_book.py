from odoo import fields, models
class BookInherit(models.Model):
    _inherit = 'library.book.ede'
    is_available = fields.Boolean('Is Available ?')

    isbn = fields.Char(help="Use a valid ISBN-13 or ISBN-10")
    publisher_id = fields.Many2one(index=True)