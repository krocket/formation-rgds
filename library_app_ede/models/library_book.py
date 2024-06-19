from odoo import fields, models
from odoo.exceptions import UserError
class Book(models.Model):
    _name = 'library.book.ede'
    _description = 'Book'

    name = fields.Char(string='Title', required=True)
    isbn = fields.Char(string='ISBN')
    active = fields.Boolean(string='Active?', default=True)
    date_published = fields.Date()
    image = fields.Binary(string='Cover')
    publisher_id = fields.Many2one('res.partner', string='Publisher')
    authors_ids = fields.Many2many('res.partner', string='Authors')
    def _check_isbn(self):
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 13:
            ponderations = [1, 3] * 6
            terms = [a * b for a, b in zip(digits[:12], ponderations)]
            remain = sum(terms) % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check
    def button_check_isbn(self):
            for book in self:
                if not book.isbn:
                    raise UserError('Please provide an ISBN for %s' % book.name)
                if book.isbn and not book._check_isbn():
                    raise UserError('%s is an invalid ISBN' % book.isbn)
                return True
    def write(self, vals):
        records = super(Book, self).write(vals)
        for record in records:
            record.butonn_check_isbn()