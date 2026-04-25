FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /app/bash_scripts/grid_run_tests.sh

CMD ["/bin/bash", "/app/bash_scripts/grid_run_tests.sh"]