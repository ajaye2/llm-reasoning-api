# llm-reasoning-api

```bash
conda create -n llm-reasoning-api python=3.11
```

```bash
conda activate llm-reasoning-api
```

```bash
pip install -r requirements.txt
```


## Setup Instructions

1. Clone the repository:
   ```bash
   git clone --recursive https://github.com/ajaye2/llm-reasoning-api
   ```

2. Run the setup script to install dependencies:
   ```bash
   ./setup_dependencies.sh
   ```

3. Start the API locally:
   ```bash
   uvicorn api.main:app --reload
   ```
