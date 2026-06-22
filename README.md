# bankerio

A Python CLI tool to automatically classify and summarize bank statement transactions by category.

I built this because I was manually calculating my monthly spending across categories — a tedious process prone to human error. A 60-euro discrepancy one month was the last straw.

## What it does

- Reads ABN AMRO CSV exports
- Filters out personal transfers by IBAN
- Lets you define your own spending categories and keywords at runtime
- Outputs a total per category and a list of unclassified transactions to review manually

## Stack

- Python
- pandas

## Installation

```bash
pip install git+https://github.com/BDKI-Data-Company/bankerio_public.git
```

## Usage

```bash
bankerio-public transactions/your_file.csv
```

A demo transactions file is included in the `transactions/` folder to try it out.

## Note

This is the public version of a private repo I built for personal use, tailored to my own bank and spending habits. This version is more generic and exists to showcase the work. Commit history is lighter as a result.