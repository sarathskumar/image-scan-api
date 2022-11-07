Step 1:Clone this repo

Step 2: Build the docker image
docker build -t imagename .

Step 3: Run a container with this image
docker run -d -p5000:5000 --name containername imagename

Step 4: Open your browser 
http://127.0.0.1:5000

Step 5: Click on the /imagescan api

Step 6: Put your public image url their
example : dmathai/prom-pushgateway-ttl


Step 7: Deploy this application in our GKE cluster and scan private image registry

If you want to scan your gcr repository, create a gcp service account in IAM and give role(Container Registry Service Agent) to pull the images.

Then we can implement this in two ways 
1. deploy with service account JSON key
2. deploy with workload identity
    
If you want do with normal with some risk you can choose the service account JSON key.In this case you need to create a service account
JSON key and add this as a secret in your cluster
Then got to deploy folder and apply kubectl apply -f deployment-key.yaml

If you want to do with workload identity, then create a kubernetes service account and bind your kubernetes service account with gcp service account
Then add the kubernetes service account name in the deployment manifest
Go to the deploy folder and apply kubectl apply -f deployment-workload.yaml
