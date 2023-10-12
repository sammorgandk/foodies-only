# Foodies Only Web Service

The Foodies Only Web Service is a Flask-based application that allows users to find the closest San Francisco food truck based on a provided address.

## Prerequisites

Before running the application, make sure you have the following installed:

- [Python](https://www.python.org/downloads/) (3.9 or higher)
- [Docker](https://docs.docker.com/get-docker/)

## Getting Started

Clone this repository to your local machine:

```bash
git clone https://github.com/sammorgandk/foodies-only.git
cd foodies-only
```

## Build and Run with Docker

You can run the application in a Docker container. First, build the Docker image:

```bash
docker build -t foodies-only .
```

Then, run the container:

```bash
docker run -p 5000:5000 foodies-only
```

The application will be accessible at `http://localhost:5000`.

## Usage

### Find the Closest Food Truck

To find the closest food truck to a specific address, use the `/address/<address>` endpoint. For example:

- `http://localhost:5000/address/123 Main St, San Francisco, CA`

### API Endpoints

- `/address/<address>`: Find the closest food truck to the provided address.

## Configuration

The application uses a `requirements.txt` file to specify the required Python packages. If you need to add or update dependencies, modify this file and rebuild the Docker image.

## Contributing

Contributions are welcome! If you have ideas or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.