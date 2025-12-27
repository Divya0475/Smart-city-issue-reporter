
---

```md
# Smart City Issue Reporting System

## Project Overview
The Smart City Issue Reporting System is a lightweight web application that allows citizens to report infrastructure-related problems such as potholes, broken streetlights, garbage overflow, and water leakage. The system captures location details, stores reports in a database, and generates a unique reference ID for each submission.

This project is implemented as a **Minimum Viable Product (MVP)** to demonstrate how digital platforms can support smart city initiatives and improve issue tracking and transparency.

---

## Features
- Citizen-friendly issue reporting form  
- Location selection (City, Area, Street)  
- Infrastructure issue selection  
- Unique reference ID generation for each report  
- Issue storage using SQLite database  
- Email confirmation trigger (simulated for demo)  
- Clean and calm user interface  
- Single-page form and success view  

---

## Technologies Used
- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS (internal styling)
- **Database:** SQLite
- **Email Notification:** Backend email trigger simulation
- **Deployment:** Render
- **Version Control:** Git & GitHub

---

## How the Application Works
1. The user fills in the issue reporting form with location details and email.
2. On submission, the backend generates a unique reference ID.
3. The issue details are stored in the SQLite database.
4. An email confirmation trigger is executed (simulated via backend logging).
5. The user is shown a success message with the reference ID.

---

## Email Trigger Implementation
For demonstration purposes, the email confirmation feature is simulated at the backend level using console logs. This approach is used due to SMTP security restrictions in local environments. The logic represents how confirmation emails would be sent in a production setup.

---

## Project Structure
```

smart-city-issue-reporting/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
└── README.md

```

---

## How to Run Locally
1. Clone the repository:
```

git clone <your-github-repo-link>

```
2. Navigate to the project folder:
```

cd smart-city-issue-reporting

```
3. Install dependencies:
```

pip install -r requirements.txt

```
4. Run the application:
```

python app.py

```
5. Open browser and visit:
```

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

```

---

## Deployment
The application is deployed using **Render** with Gunicorn as the production server. The live URL can be accessed from the Render dashboard after deployment.

---

## Future Enhancements
- Integration with real email services
- Sensor-based issue verification
- Admin dashboard for authorities
- Real-time issue status updates
- Mobile-friendly enhancements

---

## Author
Developed as part of the **Smart City Lab – Recruitment Task**.
```



