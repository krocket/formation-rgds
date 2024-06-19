from odoo import fields, models
class Book(models.Model):
    _name = 'library.book.ede'
    _description = 'Book'

    name = fields.Char(strin='Title', required=True)
    isbn = fileds.Char(string='ISBN')
    active = fields.Boolean(string='Active?', default=True)
    date_published = fields.Date()
    image = fields.Binary(string='Cover')
    published_id = fields.Many2one('res.partner', string='Publisher')
    authors_ids = fields.Many2many('res.partner', string='Authors')