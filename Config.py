Database = {
    "databaseName": "payments.db",
    "createTablesQuery": """
        CREATE TABLE IF NOT EXISTS accounts (account_id INTEGER PRIMARY KEY, account_name varchar(200));
        CREATE TABLE IF NOT EXISTS contacts (contact_id INTEGER PRIMARY KEY, contact_first_name  varchar(200) , contact_middle_name varchar(200) , contact_last_name varchar(200) , contact_address varchar(200) , contact_city varchar(40) , contact_state varchar(2) , contact_zip varchar(10) , contact_phone varchar(20) , contact_email varchar(400) , account_id INTEGER );
        CREATE TABLE IF NOT EXISTS credit_cards (credit_card_id INTEGER PRIMARY KEY, credit_card char(16) , credit_card_pin char(4) , account_id INTEGER );
        CREATE TABLE IF NOT EXISTS payments (payment_id INTEGER PRIMARY KEY, payment_amount money , invoice_number varchar(10) , account_id INTEGER );
        CREATE TABLE IF NOT EXISTS invoices (invoice_id INTEGER PRIMARY KEY, invoice_number varchar(10) , invoice_total_amount money , invoice_current_amount money , account_id INTEGER );
        CREATE TABLE IF NOT EXISTS something (invoice_id INTEGER, invoice_number varchar(10) , invoice_total_amount money , invoice_current_amount money , account_id INTEGER );
        """
}

HTML = {
    "header":"""
        <html lang="en"><head><meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="hi"><meta name="author" content="">
        <title>test.com</title><link href="/static/styles/bootstrap.min.css" rel="stylesheet"></head>
        """,
    "insertForm": """
        <body>
        <div class="container">
        <form action="/{0}" method="POST">""",
    "index": """<body><div>Oh good, everything started up right! Add a table name to the end of the URL!</div></body></html>""",
    "selectTable": """<body><table class="table table-striped"><thead><tr>"""
}
