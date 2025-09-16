# 🚀 Partie 2

This repository contains the implementation of the reporting/grade generation for PsyEL API.
## ✨ Tools & Libraries

- **Pandas** for data manipulation, cleaning and loading
- **Pydantic** for input validation of requests and responses and environment settings
- **Docker** for containerization
- **Makefile** for automating common and useful commands
- **DeepSeek AI** for documentation and best practices

## 🏗️ Project Structure

```bash
ulb-technical-test/
├── partie-2/
│ ├── generators/
│   ├── base.py --> Base class that defines ETL pipeline steps to implement
│   ├── bulletin.py --> Logic to generate bulletin data
│   ├── rapport_anomalies.py --> Logic to generate anomaly reports
├── interface.py --> API Interface class to interact with the API endpoints 
├── settings.py --> Constants and environment variables
```
## 🚀 Getting started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Make](https://www.gnu.org/software/make/)

### Installation

1. **Clone the repository**
   ```bash
   git clone git@github.com:achrafbou1/ulb-technical-test.git
   cd ulb-technical-test/partie-2
   ```
2. **Build**
    ```bash
   make build
   ```
3. **Run**
    ```bash
   make run
   ```
   
## Output / Generated Files

After running the project scripts for **partie-2** and waiting about 20 seconds, the following files will be generated in the `partie-2/` folder:

- `bulletin.csv` → CSV file containing the processed bulletin data.
- `rapport_anomalies.json` → JSON file containing the report of detected anomalies.