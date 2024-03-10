# ERMA

## Project Setup

To get started with this Flask project, follow these steps:

1. **Clone the repository:**

   ```
   git clone https://github.com/v4k0nd/erma-py-flask.git
   cd erma-py-flask
   ```

2. **Create a virtual environment:**

   ```
   curl https//pyenv.run | bash
   pyenv install 3.7.16
   pyenv local 3.7.16
   python3 -m venv .venv
   ```

3. **Activate the virtual environment:**

   - On Windows:
     ```
     .\.venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```
     source .venv/bin/activate
     ```

4. **Install the dependencies:**

   ```
   pip install -r requirements.txt
   ```

5. **Copy the `.env.example` file to `.env` and adjust it to your needs:**

   ```
   cp .env.example .env
   ```

6. **Run the Flask application:**
   ```
   flask run
   ```

### Using a Shell Script

```bash
chmod +x setup.sh
./setup.sh
```
