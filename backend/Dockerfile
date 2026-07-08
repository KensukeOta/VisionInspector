FROM python:3.12-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV UV_LINK_MODE=copy
ENV UV_PROJECT_ENVIRONMENT=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN apt-get update && apt-get install -y \
    git \
    curl \
    libglib2.0-0 \
    libgl1 \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./

RUN uv sync --no-dev --frozen

COPY . .

ARG PADIM_CHECKPOINT_URL=https://github.com/KensukeOta/VisionInspector/releases/download/v1.0.0/padim_bottle.ckpt

RUN mkdir -p checkpoints

RUN curl -fL \
    "$PADIM_CHECKPOINT_URL" \
    -o checkpoints/padim_bottle.ckpt \
    && test -s checkpoints/padim_bottle.ckpt \
    && ls -lh checkpoints \
    && file checkpoints/padim_bottle.ckpt

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]