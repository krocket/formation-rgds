from odoo import fields, models


class Book(models.Model):
    _inherit = "library.book.sho"
    is_available = fields.Boolean('Is Available?')

    isbn = fields.Char(help="Use  valid ISBN-13 or ISBN-A0.")
    publisher_id = fields.Many2one(index=True)


