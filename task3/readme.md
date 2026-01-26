# E-commerce search

## About Task
This project aims to build a lightweight search engine prototype for e-commerce content, using Elasticsearch. The goal is to demonstrate and experiment with **core search engine concepts** such as:

- Full-text search
- Filtering and sorting
- Autocomplete
- “Did You Mean” suggestions
- Typo tolerance (phrase + fuzzy ?? fallback)
- Relevancy tuning

## Steps:

### 1. Project Setup and Environment

In this step, you will initialize the development environment and connect Elasticsearch to your project.

#### 1.1 Create a new Next.js project
``` 
npx create-next-app@latest ecommerce-search
 ```
After that go to the created dir;
 
 ```
cd ecommerce-search
npm run dev
 ```
Test the connection from http://localhost:3000


1.2 Run Elasticsearch locally using Docker
1.3 Install the Elasticsearch JavaScript client:
  `npm install @elastic/elasticsearch`
1.4 Set up a `.env.local` file with your Elasticsearch connection info.

---

### 2. Sample Dataset Creation

You are provided a sample dataset which is created by ChatGPT. You are free about using your own dataset. ChatGPT is good at creating dataset with needed column and rows up to 1000 rows.

---

### 4. Data Ingestion

You’ll write a script to send the data to Elasticsearch.

* Create a simple import script using Python or any other tools.
* Use the bulk API to insert all items into the `products` index.


---


### 5. Sorting and Filtering

- Server-side sorting options:
  - Relevance (default)
  - Price (ascending / descending)
  - Units sold (ascending / descending)
- Filter UI with selectable facets (checkboxes or pills).

---


### 6. Core Search Functionality


Implement the main search logic.

- Create a Next.js API route (e.g. `/api/search`).
- Handle parameters:
  - search query
  - filters
  - sorting
  - pagination ??
- Build an Elasticsearch query that includes:
  - Full-text search (`match`, `multi_match`)
  - `bool` filters for facets (brand, color, condition, etc.)
  - Field boosting for important fields
  - Optional `function_score` for relevance tuning


---

### 7. Autocomplete and Suggestions

- Implement autocomplete feature using:
  - `edge_ngram`, or
  - combined searchable fields
- Add a **Did You Mean** feature using:
  - `phrase` suggester as the fallback query.
- Trigger suggester only when the main search returns **zero results**.

---

---

### 8. Basic Frontend Interface

Build a clean and readable search interface.

- Search bar with autocomplete support.
- Clear and accessible sorting tabs.
- Improved filter tab:
  - larger clickable areas
  - readable font sizes
  - visual grouping of filter categories
- Result cards displaying key product attributes such as price and units sold.
- Visually distinct “Did you mean?” suggestion section.


---

### 9. Relevancy Tuning and Testing

improve search quality day by day.

- Test common search queries.
- Tune relevance using:
  - field boosting
  - `function_score`
  - phrase + fuzzy ?? fallback strategy
- Observe result ordering, pagination stability, and UX consistency.


---


---

This roadmap gives you a clear path to building a production-quality prototype focused on search UX and relevancy. Let me know if you want this converted into a `README.md` or GitHub issue list.














