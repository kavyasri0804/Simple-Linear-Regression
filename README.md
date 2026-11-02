# Simple-Linear-Regression
Salary Prediction Using Simple Linear Regression
📌 Project Overview
This project demonstrates an end-to-end Machine Learning workflow using Simple Linear Regression to predict an employee's salary based on their years of experience.

The project covers:
- Data loading and preprocessing
- Exploratory data analysis and visualization
- Model training and evaluation
- Model serialization using Pickle
- Flask web application development
- Cloud deployment using Render
The dataset contains 30 records, with YearsExperience as the independent variable and Salary as the dependent variable.
🎯 Objectives
- Understand the relationship between years of experience and salary.
- Train a Simple Linear Regression model.
- Evaluate the model using regression metrics.
- Save and reload the trained model.
- Build a web interface that accepts experience as input and displays a predicted salary.
- Prepare the Flask application for cloud deployment.
📊 Dataset Description
The dataset contains the following columns:
Column	Description
YearsExperience	Independent variable (X); years of work experience
Salary	Dependent variable (Y); salary to be predicted


Example records:
YearsExperience	Salary
1.1	39343
1.3	46205
1.5	37731
...	...


Dataset size: 30 records

Train-test split: The project description specifies 80% training data (24 records) and 20% testing data (6 records).
Ensure the dataset filename and path used in the notebook match the files in your repository.

🧠 Machine Learning Algorithm
Simple Linear Regression
Simple Linear Regression is a supervised Machine Learning algorithm that models the relationship between one independent variable and one dependent variable.

In this project:
- X: Years of Experience
- Y: Salary
The model learns a best-fit straight line from the training data and uses it to predict salary for a given number of years of experience.
Linear Regression Equation
\[
Y = mX + c
\]
Where:
- Y = Predicted salary
- X = Years of experience
- m = Slope (coefficient)
- c = Intercept
The slope describes the estimated change in salary for each additional year of experience. The intercept is the model's estimated salary when experience is zero.
⚙️ Model Training
The project description specifies the following split:
Dataset	Records	Percentage
Training data	24	80%
Testing data	6	20%
Total	30	100%


The model is trained using Scikit-learn:
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
📈 Model Evaluation
The project description reports the following results:
Metric	Reported value
Training R² score	96%
Testing R² score	90%
Training loss	115
Testing loss	189


Important: Confirm these values against the output of your notebook before publishing. If the loss values are intended to represent MSE, verify their units and calculations; salary prediction errors can be large because salary is measured in currency units.
R² Score (Coefficient of Determination)
R² measures how much of the variation in the target values is explained by the regression model. A value closer to 1 generally indicates a better fit.
- 1.0 — perfect fit on the evaluated data
- 0.0 — no improvement over predicting the target mean, under the standard definition
- A negative score — worse than predicting the target mean
The reported training R² is 0.96 and testing R² is 0.90. Verify these values by running the notebook.
Mean Squared Error (MSE)
MSE is the average of the squared differences between actual and predicted values. Lower values indicate smaller squared prediction errors.
\[
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
\]
Root Mean Squared Error (RMSE)
RMSE is the square root of MSE and is expressed in the same units as the target variable.
\[
RMSE = \sqrt{MSE}
\]
Use the metrics calculated by the notebook when documenting final model performance.
💾 Saving the Model with Pickle
The trained model can be serialized to a file so the Flask application can load it without retraining:
import pickle

with open("SLR_MODEL.pkl", "wb") as file:
    pickle.dump(model, file)
Load the model in the application:
import pickle

with open("SLR_MODEL.pkl", "rb") as file:
    model = pickle.load(file)
Only load Pickle files from trusted sources.

🌐 Flask Web Application
The Flask application provides a simple interface for salary prediction.
Application workflow
1. The user enters their years of experience in an HTML form.
2. The form submits the input to the Flask backend.
3. Flask passes the input to the loaded regression model.
4. The model predicts the salary.
5. The predicted result is displayed on the webpage.
User enters experience
          ↓
      HTML form
          ↓
     Flask backend
          ↓
   Trained Pickle model
          ↓
   Salary prediction
          ↓
 Result displayed to user
Frontend
The HTML page is responsible for collecting the user's years of experience and displaying the predicted salary. CSS can be added to improve the design and responsiveness.
📦 Requirements
The application may use the following Python packages, depending on the imports in your code:
Flask
numpy
pandas
scikit-learn
gunicorn
Install dependencies with:
pip install -r requirements.txt
Make sure requirements.txt includes every package required by your application and notebook.
☁️ Deployment on Render
The Flask application can be deployed to Render as a Web Service.
1. Push the project files to a GitHub repository.
2. Sign in to Render and create a new Web Service.
3. Connect the GitHub repository.
4. Set the build command:
   pip install -r requirements.txt
5. Set the start command, if your Flask instance is named app in app.py:
   gunicorn app:app
6. Deploy the service and review the build and runtime logs if an error occurs.
The start command assumes that app.py contains a Flask application object named app and that the required model file is included at the path expected by the application.
🛠️ Technologies Used
- Python — programming language
- NumPy and Pandas — data handling
- Matplotlib — data visualization, if used in the notebook
- Scikit-learn — Linear Regression and evaluation metrics
- Pickle — model serialization
- Flask — web application backend
- HTML/CSS — web interface
- Gunicorn — WSGI server for deployment
- Render — cloud hosting platform
📂 Project Structure
The following is an example structure. Adjust filenames to match your actual repository.
Salary-Prediction-Project/
├── app.py
├── SLR_MODEL.pkl
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── notebook/
    └── SLR.ipynb
If your notebook or model uses a different filename, update the structure and application paths accordingly.
🚀 Run Locally
1. Clone or download this repository.
2. Create and activate a Python virtual environment (recommended).
3. Install dependencies:
   pip install -r requirements.txt
4. Confirm the trained model file is present at the path expected by app.py.
5. Start the Flask application:
   python app.py
6. Open the local address shown in the terminal.
For production deployment, use the configured Gunicorn start command rather than Flask's development server.
🔮 Future Enhancements
- Improve the interface with CSS or Bootstrap.
- Add input validation and clear error messages.
- Display a regression-line visualization.
- Compare additional regression models.
- Add automated tests.
- Use Docker and a CI/CD pipeline.
- Monitor application performance after deployment.


Conclusion
This project demonstrates how Simple Linear Regression can be used to estimate salary from years of experience. It combines model training and evaluation with Pickle-based model storage and a Flask interface, with deployment instructions for Render.

The prediction is an estimate based on the dataset and should not be treated as a guaranteed salary offer.
