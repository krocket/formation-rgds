from odoo import api, fields, models
from odoo.exceptions import UserError
class Book(models.Model):
    _name = 'library.book.lka'
    _description = 'Book'

    name = fields.Char(string='Title', help='Book cover title', required=True)
    isbn = fields.Char('ISBN')
    active = fields.Boolean(string='active?', default=True)
    date_published = fields.Date()
    image = fields.Binary(string='cover')
    publisher_id = fields.Many2one('res.partner', string='Publisher')
    author_ids = fields.Many2many('res.partner', string='Authors')

    def _check_isbn(self):
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 13:
            ponderators = [1, 3] * 6
            total = sum(a * b for a, b in zip(digits[:12], ponderators))
            remain = total % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check

    def button_check_isbn(self):
      for book in self:
        if not book.isbn:
            raise UserError('Please provide an ISBN13 for %s' % book.name)
        if book.isbn and not book._check_isbn():
            raise UserError('%s is an invalid ISBN' % book.isbn)
      return True

    