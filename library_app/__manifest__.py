{'name': 'Library Management Application',
 'description': 'Library books, members and book borrowing.',
 'author': 'Daniel Reis',
 'depends': ['base','sales_team'],
 'data': [
    'security/library_security.xml',
    'security/ir.model.access.csv',
    'views/library_menu.xml',
    'views/book_view.xml',
    'views/book_category_view.xml',
    'views/book_list_template.xml',
    'reports/library_book_report.xml',
    'reports/library_book_sql_report.xml',
 ],
 'demo': [
    'data/res.partner.csv',
    'data/library.book.csv',
    'data/book_demo.xml',
 ],
 'application': True,
 'installable': True,
}
