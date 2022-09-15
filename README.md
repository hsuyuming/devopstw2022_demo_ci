### Install VSCode extension
- CloudCode
- Python

### Install skaffold
- Install page: https://skaffold.dev/docs/install/
```cmd
# For Linux x86_64 (amd64)
curl -Lo skaffold https://storage.googleapis.com/skaffold/releases/latest/skaffold-linux-amd64 && \
sudo install skaffold /usr/local/bin/
```
- check skaffold version
```
jupyter@abehsu-devops-demo:~/devopstw2022_demo$ skaffold version
v1.39.2
```

### Install helm
```cmd
# Use this script to install Helm requires root privilege
curl -o get-helm-3.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod u+x get-helm-3.sh
./get-helm-3.sh
helm version
helm -h
```

### skaffold build cmd example
```cmd
export IMAGE_TAG=0.1.0 && skaffold build -p docker_with_kubectl_artifactory_envtag --file-output tags.json -v debug
```

### skaffold test cmd example
```cmd
skaffold test --build-artifacts=tags.json -v debug
```

### skaffold render cmd example
```cmd
skaffold render -p docker_with_kubectl_local  --build-artifacts=tags.json --digest-source=local --output=k8s-manifest.yaml
```

### skaffold apply cmd example
```cmd
skaffold apply k8s-manifest.yaml --kubeconfig=/home/jupyter/.kube/config --kube-context=minikube
```

### skaffold build + skaffold render (helm)
```cmd
skaffold build -p docker_with_local_helm_chart --file-output tags_2.json -v debug
skaffold render -p docker_with_local_helm_chart  --build-artifacts=tags_2.json --digest-source=local --output=test.yaml -v debug
Underlying cmd: helm --kube-context <xxxxx> template fastapi-helm fastapi_demo/helm_charts --set-string image.repository=fastapi_demo,image.tag=53cbd2806ace683653baa26349f9f75b040e2238@sha256:b63604dac287822b81fe7aa8f27c57a6163d22a2f8f01927456f6e7f9557077c -f fastapi_demo/helm_charts/values.yaml
```

### How to create helm repository on GCP Artifact Registry
```cmd
helm package ~/devopstw2022_demo/fastapi_demo/helm_charts

gcloud auth application-default print-access-token | helm registry login -u oauth2accesstoken \
--password-stdin us-west1-docker.pkg.dev

helm push skaffold-helm-fastapi-0.0.1.tgz oci://docker.io/devopstw22
rm -f skaffold-helm-fastapi-0.0.1.tgz
```

### Cloudbuild cmd example  
```cmd
gcloud builds submit . --config=cloudbuild.yaml --worker-pool=projects/xxxxxx/locations/us-west1/workerPools/xxxxxx --gcs-log-dir=gs://dev-devops-day-default/build-logs --region us-west1
```

### Setup sonarqube
```cmd
docker run -d --name sonarqube -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true -p 9000:9000 sonarqube:latest
```

### Reference
- skaffold CLI: https://skaffold.dev/docs/references/cli/
- sonarqube setup: https://docs.sonarqube.org/latest/setup/get-started-2-minutes/