# Step 1: Use Python 3.12 as the base image
FROM python:3.12-alpine

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file into the container
COPY requirements.txt .

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application code into the container
COPY . .

# Step 6: Expose the port (default port for Django is 8000)
EXPOSE 8000

# Step 7: Command to run Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
