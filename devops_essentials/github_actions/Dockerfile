# Use the official Node.js 14 image as the base image
FROM node:14

# Set the working directory inside the container to /app
WORKDIR /app

# Copy package.json and package-lock.json files to the working directory
COPY package*.json ./

# Install the dependencies specified in package.json
RUN npm install

# Copy all files from the current directory to the working directory in the container
COPY . .

# Expose port 8080 to the host, so that the application is accessible
EXPOSE 8080

# Define the command to run the application
CMD ["node", "app.js"]
