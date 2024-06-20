from odoo import fields, models

class library_member(models.Model):
    _inherit = 'library.book.adu'
    is_available = fields.Boolean('is Avalaible?')

    isbn = fields.Char(help='Use a valid ISBN-13 or ISBN-10.')
    publisher_id = fields.Many2one(index=True)