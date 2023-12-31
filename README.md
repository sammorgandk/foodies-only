# Foodies Only Web Service

The Foodies Only Web Service is a Flask-based application that allows users to find the closest San Francisco food truck based on a provided address.

## Accessing the App from a Public Browser

Open a web browser and type the IP address of the public EC2 instance followed by :5000 here:

[http://18.216.0.120:5000/](http://18.216.0.120:5000/)

To find the closest food truck to a specific address, use the `/address/<address>` endpoint:

[http://18.216.0.120:5000/address/123 Main St, San Francisco, CA](http://18.216.0.120:5000/address/123%20Main%20St,%20San%20Francisco,%20CA)


## Prerequisites to Run the App Locally

Before running the application locally, make sure you have the following installed:

- [Python](https://www.python.org/downloads/) (3.9 or higher)
- [Docker](https://docs.docker.com/get-docker/)
- [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli)

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

The application uses a `requirements.txt` file to specify the required Python packages.

## Deployment

Terraform is used to create the EKS cluster on AWS. Then, after building the Docker image, we use Kubernetes to deploy the image to the EKS cluster.

### Create the EKS Cluster on AWS

To deploy the EKS cluster on AWS run:

```bash
terraform init
```

to initialize a working directory, then run:

```bash
terraform apply
```

### Deploy to EKS Cluster

After the creation of a namespace on AWS, create kubeconfig file by running:

```bash
aws eks update-kubeconfig --region us-east-2 --name foodies-only
```

then run:

```bash
kubectl apply -f eks-deploy.yaml
```

to deploy to cluster.

Then run this command to run shell in specified pod:

```bash
kubectl exec -it foodies-only-deploy-<mypodId> -n foodies-only -- /bin/bash
```

## Future Enhancements

- Use Google Maps direction API and calculate travel time between user and nearest food truck
- Utilize S3 for data storing and use Lambda functions for file processing
- Store AWS credentials securely using environment variables or AWS IAM roles
- Use AWS KMS for encryption (ex: api keys and environment variables)
- Enhance the UI for a better user experience
- Use other AWS services like CodeDeploy to build out CI/CD pipelines
- Set up CloudWatch dashboard for deployment monitoring
