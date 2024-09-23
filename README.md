
# Managing patients and their assessments

# Project setup

1. **Clone the Repository**  
   Run the following commands:
   ```bash
   git clone https://github.com/Forevgit/TestTask.git
   ```

2. **Set Up the Environment Variables**  
   Create a `.env` file in the root directory, you can check .env.example:
   ```bash
   DB_NAME=task_management
   DB_USER=task_user
   DB_PASSWORD=secret
   DB_HOST=db
   DB_PORT=5432
   SECRET_KEY=your_secret_key
   DEBUG=True
   ```

3. **Create a virtual environment**  
   Run the following command:
   ```bash
   python(python3) -m venv .venv
   ```

4. **Activate a virtual environment**  
   Run the following command:
   ```bash
   source .venv/bin/activate
   ```

5. **Set All Project Dependencies**  
   Run the following command:
   ```bash
   pip install -r requirements.txt
   ```

6. **Run database migrations**  
   Run the following command:
   ```bash
   python(python3) manage.py makemigrations
   python(python3) manage.py migrate
   ```
   
7. **Create superuser**  
   ```bash
   python(python3) manage.py runserver
   ```
   
6. **Access the Project**  
   web application available at [http://localhost:8000](http://localhost:8000).

7. **API Endpoints**  
   Use this URL [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) to see primary endpoints.


# Assumptions you made during development

1. **Only the doctor treating the patient has access to the patient**
2. **Attach a few questions to the patient assessment**
3. **Validation was created to verify the patient's birthday and birthday**
4. **All questions are stored in a separate table and are related to the assessment**

# Challenges you faced and how you overcame them.
1. Challenge: A doctor can only view his patients
Solution: Created a many-to-one relationship, many patients can have 1 doctor
2. Challenge: Implementation of questions for evaluation
Solution: Created a relationship, many questions for 1 assessment
3. Challenge: Getting the patient's age
Solution: Dynamically calculate age when obtaining patient data.
This can also be calculated at the database level if there are many patients

# Any additional features or improvements you added
1. Swagger-Integration
2. Validation for final_score and date of birth
3. Pagination, filtering and sorting
# Process of deployment to AWS
There is a CodeCommit service, it needs to be synchronized with the repository on the git you will need to add SHH keys 
and write several yml files for git hub action, then you need to build everything that is on CodeCommit in image
CodeBuild(here you also need to write yml 1-2pcs) and throw either on S3 bucket, And then everything needs to be
deployed on ECS and create a task that starts the container and create a service that will control this task,
for the database you will need to create an additional RDS, Jwt can be implemented using AWS Lambda
