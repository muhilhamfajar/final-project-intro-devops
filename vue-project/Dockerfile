# FROM node:lts-alpine

# WORKDIR ./

# COPY package*.json ./

# RUN npm install

# COPY . .

# RUN npm run build

# EXPOSE 8080
# CMD [ "npm", "run", "preview" ]

FROM node:lts-alpine

WORKDIR /app
COPY . ./
RUN npm install

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
