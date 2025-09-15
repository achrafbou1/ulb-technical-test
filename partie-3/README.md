# 🚀 Partie 3

This repository contains a simple Interface that displays the API data from PsyEL API.
## ✨ Tools & Libraries

- **Nuxt** opinionated framework based on Vue.js for the frontend
- **Nuxt-UI + TailwindCSS** ready components and CSS library
- **Docker** for containerization
- **Makefile** for automating common and useful commands
- **Typescript + ESLint** for type safety and code quality

## 🏗️ Project Structure

```bash
ulb-technical-test/
├── partie-3/
│ ├── app/ --> Application code
│   ├── assets --> Static assets / CSS & Tailwind configuration
│   ├── components --> Custom reusable components across the application
│   ├── composables --> Reusable functions (HTTP calls)
│   ├── layouts --> Reusable Navbar and footer
│   ├── pages
│   ├── schemas --> Type checking for API responses
```
## 🚀 Getting started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Make](https://www.gnu.org/software/make/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation

1. **Clone the repository**
   ```bash
   git clone git@github.com:achrafbou1/ulb-technical-test.git
   cd ulb-technical-test/partie-3
   ```
2. **Build**
    ```bash
   make build
   ```
3. **Run**
    ```bash
   make run
   ```

## General comments

- Deepseek AI was used to help with responsiveness and resolving inconsistencies and conflicts between libraries 
while setting up the project in addition to best practices in terms of reusability and modularity of the code
- For the sake of simplicity, the environment variable for the API is hardcoded in nuxt.config.ts and the frontend
is deployed using Server side rendering. In a production setting, the API URL should be defined in the environment and
the frontend should be built at compile time (SSG) and it's static assets served using Nginx or some other proxy/web server.