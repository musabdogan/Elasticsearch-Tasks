# E-commerce search and fine-tuning for Search relevancy

## About Task
This project aims to build a lightweight search engine prototype for e-commerce content, using Elasticsearch. The goal is to demonstrate features such as filtering, autocomplete, suggesters, and query relevancy tuning with minimal setup.Search bar will contain Elastic features like filters, suggesters (did you mean), auto-complete and more. After the task, you will have learned how to create search engine and make fine tuning on it.

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


---

### 3. Index and Mapping in Elasticsearch

In this step, you’ll define how Elasticsearch stores and analyzes your data.

* Create an index called `media_items`.
* Define a mapping schema with appropriate field types:

  * `text` fields for full-text search 
  * `keyword` fields for filters 
  * `integer` and `float` for `release_year` and `rating`
* Add a custom analyzer or use `completion` field for autocomplete on `title`.

---

### 4. Data Ingestion

You’ll write a script to load the data into Elasticsearch.

* Create a simple import script (e.g., `scripts/import.js`) using the client.
* Use the bulk API to insert all items into the `media_items` index.
* Refresh the index after insertion and verify the data with a simple query.

---

### 5. Core Search Functionality

Now you’ll implement the basic search logic using Elasticsearch Query DSL.

* Create an API route in Next.js (e.g., `/api/search`).
* Handle input parameters: search term, filters, pagination, and sorting.
* Implement a query that includes:

  * Full-text `match` search on `title` and `description`
  * `bool` filters for `type`, `genres`, `platforms`
  * Boosting important fields (e.g., `title^3`)
  * Pagination (`from`, `size`) and optional sort by rating or release\_year

---

### 6. Autocomplete and Suggestions

Enhance the search bar with dynamic suggestions and typo correction.

* Implement autocomplete using:

  * `completion` field with `suggest` API, or
  * `edge_ngram` analyzer for prefix matching
* Add a "Did you mean" feature using:

  * `term` or `phrase` suggester on the `title` field
* Expose a new API route for autocomplete or integrate it into the main route

---

### 7. Basic Frontend Interface

Build a minimal UI for interacting with the search engine.

* Create a search bar with autocomplete suggestions.
* Add filter options (checkboxes or dropdowns for type/genre/platform).
* Display paginated search results (title, rating, etc.).
* Show "Did you mean" suggestions if relevant.

---

### 8. Relevancy Tuning and Testing

Focus on improving search quality through scoring and relevance strategies.

* Define test cases and evaluate whether results are meaningful.
* Apply relevance techniques:

  * Boost specific fields using `^`
  * Use `function_score` to prioritize results by `rating` or `recency`
  * Add `fuzziness` for typo tolerance
* Monitor and adjust queries based on observed results.

---

### 9. Deployment and Documentation

Deploy your working POC and document it for others (or future you).

* Deploy frontend (e.g., to Vercel).
* Use Elastic Cloud for production Elasticsearch or expose your local instance.
* Add a `README.md` with:

  * Project overview
  * Setup instructions
  * Sample queries and screenshots
  * Known limitations or ideas for next steps

---

This roadmap gives you a clear path to building a production-quality prototype focused on search UX and relevancy. Let me know if you want this converted into a `README.md` or GitHub issue list.














