# Shopper's Stop Price Monitor

A lightweight tool to track product prices and availability from Shopper’s Stop.  
This is intended as a **weekend project** for structured scraping and price monitoring (focused mainly on **shoes**).

---

## Features

- Fetch product details and cache raw JSON for debugging
- Extract **current price** and **original price** (to track discounts)
- Check availability for specific shoe sizes (returns boolean + stock count)
- Log product price & availability history
- Run checks automatically at set intervals (30 mins / 1 hour)
- Console notifications when price/availability conditions are met

---

## Planned Roadmap

### Basic Functionality
1. **Fetch product data**
   - `get_listing_details`: Fetch and cache the raw JSON response for a given product URL.
   - `get_listing_price`: Extract both current and original price from JSON.
   - `check_availability`: For a given size, return whether it’s available + number of units.

2. **Automation**
   - Schedule this process to run every 30 mins / 1 hour.
   - Add retry & rate-limiting to avoid site blocking.

3. **Logging**
   - Maintain a history of product price and availability.

---

### Future Improvements
- **Email notifier**  
  Replace console notifications with emails.

- **Database storage**  
  Store structured data in SQLite (user, items, logs). Example schemas:
  - **Users**: `user_id, name, email`
  - **Items**: `item_id, item_name, item_seller`
  - **Logger**: `timestamp, item_id, size, price, availability`

- **Advanced features**  
  - Track price trends over time (plot graphs).
  - Alert on percentage price drop (not just fixed values).
  - Support more categories beyond shoes.

---

## Setup

### Virtual Environment
```bash
python -m venv scrape-venv


## venv setup (Good Practice)

**Create a venv:**
```bash
python -m venv scrape-venv
```
*(you can replace `scrape-venv` with any name you like)*

**Activate in PowerShell:**
```powershell
.\scrape-venv\Scripts\Activate.ps1
```

**Activate in Command Prompt:**
```cmd
scrape-venv\Scriptsctivate
```

---

## Code Quality Check

Before pushing changes, make sure to run:
```bash
flake8 .
```
