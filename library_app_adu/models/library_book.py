from odoo import fields, models


class Book_ADU(models.model):
    _name = 'library.book.adu'
    _description = 'Book'

    name = fields.Char(string='Title', required=True)
    isbn = fields.Char(string='ISBN')
    active = fields.Boolean(string='Active?', default=True)
    date_published = fields.Date()
    image = fields.binary(string='Cover')
    publisher_id = fields.Many2one('res.partner', string='Publisher')
    author_ids = fields.Many2many('res.partner', string='Authors')
