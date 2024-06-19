from odoo import fields, models
class Book(models.Model):
    _name = 'library.book.LKA'
    _description = 'Book'

name = fields.Char(string='Title',
    help='Book cover title',
    required=True)
isbn = fields.Char(string='isbn')
active = fields.Boolean(string='active?', default=True)
date_published = fields.Date()
image = fields.Binary(string='cover')
publisher_id = fields.Many2one('res.partner', string='Publisher')
author_ids = fields.Many2many('res.partner', string='Authors')