# Hugging Face GHCR 

This repository provides a minimal example of deploying a Python-based Hugging Face web application using Docker and GitHub Container Registry (GHCR).

## Project Structure

```
huggingface-ghcr/
├── Dockerfile            # Docker configuration for building the image
├── LICENSE               # Project license (MIT)
├── Makefile              # Utility commands for building and pushing the image
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
└── webapp/
    └── main.py           # Entry point for the web application
```

## Features

- Containerized Hugging Face web app using Docker
- Easy push to [GitHub Container Registry (GHCR)](https://ghcr.io/)
- Simple `Makefile` for automation

## Usage

### Build Docker Image

```bash
make build
```

### Push to GHCR

Make sure you're logged in with:

```bash
echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin
```

Then push:

```bash
make push
```

### Run Locally

```bash
docker run -p 8000:8000 ghcr.io/<your-username>/huggingface-ghcr
```

## License

This project is licensed under the [MIT License](LICENSE).

---