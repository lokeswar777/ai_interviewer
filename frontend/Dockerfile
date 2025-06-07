# Use an official Node runtime as the base image
FROM node:18-alpine

# Set working directory in the container
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the frontend code
COPY . .

# Make port 3000 available
EXPOSE 3000

# Start the React development server
CMD ["npm", "start"]
