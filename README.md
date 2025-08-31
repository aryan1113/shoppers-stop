# Shopper's Stop

This is going to be just structured scraping, intended as a weekend project.

[Example JSON link](https://www.shoppersstop.com/_next/data/cOvKwJilpXWjxUCkIBzz3/ADIDAS-Upvibe-Synthetic-Lace-Up-Men-s-Sports-Shoes/p-FMADIU5066_GREY.json)

---

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
