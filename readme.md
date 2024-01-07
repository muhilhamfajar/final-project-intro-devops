# Final Project Intro to Devops

This project is designed to enhance the abilities of aspiring Software & Data Engineers by effectively implementing project deployments. This project will deploy a web application created during the Final Project of the Intro to Web Development & Architecture course. The deployment process will cover stages until the web application is accessible over the internet with a specific domain name.

### A. Background Problems
User have simple web apps that run in local. User want to their web apps can be accessible through internet using spesific domain. User also want to make it seamless testing and deployment during their development.

### B. What I've done

#### Part I: Server Preparation

 **1. Subscribe a vps**
 I subscribed VPS from [jagoanhosting.com](https://www.jagoanhosting.com/). I just subscribe for the basic and cheapest one. Next step after I have a vps, I have to install the docker, config for the firewall, and install github runner for my VPS that run from this repository. Please read this link to register the self hosted runner [how to register self-hosted runner](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners) and [how to run github runner as a background service](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/configuring-the-self-hosted-runner-application-as-a-service).
 
 **2. Buy domain**
 I bought domain also from [jagoanhosting.com](https://www.jagoanhosting.com/). After i buy domain I just need to do some setup to pointing my sub domain to my vps.
 
#### Part II: Compose the app
Create `Dockerfile` for each service. After create `Dockerfile` make sure to export the port then we can try to use on `docker-compose.yaml`. You can see this code [here](https://github.com/muhilhamfajar/final-project-intro-devops/blob/main/docker-compose.yaml). 
If you want to run just run this command in your project directory `docker-compose up --build`. 
Try access in local using `http://127.0.0.1:8080/` for frontend and `http://127.0.0.1:5000/` for backend.

#### Part III: Create CI / CD Pipeline

 **1. Create CI (Testing)**
This action will be running if there is triggered on pull request to main branch.
You can see testing pipeline process [here](https://github.com/muhilhamfajar/final-project-intro-devops/blob/main/.github/workflows/testing.yaml).
![Testing](https://github.com/muhilhamfajar/final-project-intro-devops/blob/main/storage/testing.png?raw=true)

 **2. Create CD (Build and Deployment)**
This action will be running if main branch just pushed / update.
You can see testing pipeline process [here](https://github.com/muhilhamfajar/final-project-intro-devops/blob/main/.github/workflows/build.yaml).
![Deploy](https://github.com/muhilhamfajar/final-project-intro-devops/blob/main/storage/deploy.png?raw=true)

 **3. Restrict the access for branch main / master**
I manage to restrict the main branch to control how the flow for people merged their changes.
![Protect branch](https://github.com/muhilhamfajar/final-project-intro-devops/blob/main/storage/protect-branch.png?raw=true)

#### Part IV: Configure web server using nginx
 **1. Install nginx**
I just follow this [digital ocean's tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04).

 **2. Create server block**
 In Nginx, a server block is a configuration block that defines settings for a specific virtual server. It allows you to define how Nginx should handle requests for a particular domain or IP address. Each server block typically includes configurations such as the server name, root directory, error pages, SSL settings, and more.
Here is my setting:
```console
server {
    server_name vps.ilhamfajar.space;

    location / {
        proxy_pass http://172.17.0.1:8080; # Vue.js frontend
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /admin {
        proxy_pass http://172.17.0.1:5000/login; # Flask Admin
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /api {
        proxy_pass http://172.17.0.1:5000/api; # Flask API
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/vps.ilhamfajar.space/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/vps.ilhamfajar.space/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}
server {
    if ($host = vps.ilhamfajar.space) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    listen 80;
    server_name vps.ilhamfajar.space;
    return 404; # managed by Certbot
}
``` 

#### Part V: Configure domain setting
I'm using `certbot` to secure from http to be https. I just follow this [tutorial](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-20-04).

### C. Result
You can access to this link [vps.ilhamfajar.space](http://vps.ilhamfajar.space/). 
Note: This web apps only available until 20th January 2024 since I just subscribe only one month.

![Result](https://github.com/muhilhamfajar/final-project-intro-devops/blob/main/storage/result.png?raw=true)
