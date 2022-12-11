# Blood Pressure Early Warning And Detection
 Django Web App that Helps Patients monitor and log their blood pressure over time to provide heuristic data and provide feedback.


## Contributors:

-       Jyothi Cameron: Project Manager / Team Lead
-       Matthew Delva: Release Manager / Software Architect
-       Richard Johnston: Primary Developer / Tester
-       Austin Strand: Additional Developer
-       Derek Perkins: Secondary developer / Documentation
-       Abdulla Almarri: Secondary Developer / Documentation

Actions include:

-    Advise them of abnormal blood pressure readings, whether current or sustained
-    Prompting a survey about possible side effects and gauging their responses, then relaying informational links
-    Alerting the patient about the risk of hypertension or asking them if they need to contact 911 for emergency service.

## Usage
1. run `pip install -r requirements.txt`
2. CD into dj_bpewad
3. run `python manage.py runserver`

## Admin usage
### Logging on to admin
1. Go to http://127.0.0.1:8000/admin
2. Log on with an admin account

### Creating an admin account
1. Use Ctrl+c to cancel the running Django instance
2. run `python manage.py createsuperuser`
3. Follow the prompts to create an admin account
4. run `python manage.py runserver` to start Django