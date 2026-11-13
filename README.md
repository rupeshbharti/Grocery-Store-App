# Grocery Store Management System

A small full-stack grocery store management app built with a Flask REST API, PostgreSQL, and a browser-based interface. It helps manage a product catalog and record customer orders. The application is intended to run locally; it requires a running PostgreSQL database and Flask backend, so a static live demo is not available.

## Features

- View the order history, including date, order number, customer, and total cost.
- Create orders for a customer with multiple products and quantities.
- Calculate line-item and order totals in the interface.
- Manage the product catalog by adding products with a unit of measure and price, or deleting products.
- Store products, units of measure, orders, and order details in PostgreSQL.

## Technology

- **Backend:** Python, Flask, psycopg2
- **Database:** PostgreSQL
- **Frontend:** HTML, CSS, JavaScript, jQuery, and Bootstrap

## Project structure

```text
.
├── Backend/
│   ├── server.py             # Flask API
│   ├── sql_connection.py     # PostgreSQL connection
│   ├── products_dau.py       # Product data operations
│   ├── order_dau.py          # Order data operations
│   └── uom_dau.py            # Unit-of-measure data operations
└── UI/
    ├── index.html            # Order history dashboard
    ├── manage-product.html   # Product management page
    ├── order.html            # New order page
    ├── css/
    └── js/
```

## Requirements

- Python 3
- PostgreSQL
- A PostgreSQL database with the tables and columns used by the app: `products`, `uom`, `orders`, and `order_details`. The repository does not include a database schema or seed data; add the required tables and at least one unit of measure before using the UI.

## Setup and run

1. **Create and prepare the PostgreSQL database.** Create the database and tables expected by the application, and insert unit-of-measure rows into `uom`. The code connects to a database named `Grocery Store` by default.

2. **Configure the database connection.** Edit `Backend/sql_connection.py` with your local PostgreSQL database name, user, password, host, and port.

3. **Install Python dependencies:**

   ```bash
   python -m pip install Flask psycopg2-binary
   ```

4. **Start the API** from the `Backend` directory:

   ```bash
   cd Backend
   python server.py
   ```

   The Flask API listens on `http://127.0.0.1:5000`.

5. **Serve the frontend** in a second terminal from the `UI` directory:

   ```bash
   cd UI
   python -m http.server 8000
   ```

6. Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser. Keep the API and PostgreSQL running while using the app.

The frontend's API URLs are configured in `UI/js/custom/common.js` and currently point to `http://127.0.0.1:5000`.

## API endpoints

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `GET` | `/getProducts` | List products and their units |
| `GET` | `/getUOM` | List units of measure |
| `GET` | `/getAllOrders` | List orders with their details |
| `POST` | `/insertProduct` | Add a product |
| `POST` | `/deleteProduct` | Delete a product |
| `POST` | `/insertOrder` | Save an order and its line items |

## Notes

- This project is configured for local development and is not deployed as a live website.
- Database connection values are currently stored in `Backend/sql_connection.py`; use local development credentials and avoid committing secrets.
- The frontend uses local API URLs, so the app will not work by opening the HTML files without also running the backend.
