# Deployment - Cloning - Setting up

---

## Table of Content

* [Environment Variables](#environment-variables)
  * [GitPod IDE](#gitpod-ide)
  * [Non-GitPod IDE](#non-gitpod-ide)
  * [Key-value Pairs](#key-value-pairs)

* [Initial Deployment](#initial-deployment)

* [Amazon AWS](#amazon-aws)
  * [S3 Bucket](#s3-bucket)
  * [IAM](#iam)
  * [Final AWS Steps](#final-aws-steps)

* [How to Fork it](#how-to-fork-it)

* [Making a Local Clone](#making-a-local-clone)

* [Email Setup](#email-setup)
  * [Gmail](#gmail)
  * [Outlook](#outlook)

* [Google Signup](#google-signup)

---

## Environment Variables

| Key | Where to find it |
|---|---|
| SECRET_KEY | Django secret key, available in settings.py when you create the project |
| DATABASE_URL | PostgreSQL URI, available in the Credentials part, Settings tab of Heroku Postgres |
| STRIPE_PUBLIC_KEY | Your Stripe public key, available on Stripe dashboard |
| STRIPE_SECRET_KEY | Your Stripe secret key, available on Stripe dashboard |
| STRIPE_WEBHOOK_SECRET | Your Stripe checkout webhook secret key, available on Stripe webhook dashboard |
| STRIPE_SUBSCRIPTION_WEBHOOK_SECRET | Your Stripe subscription webhook secret key, available on Stripe webhook dashboard |
| EMAIL_HOST_USER | Your email address |
| EMAIL_HOST_PASS | Your email password |
| AWS_SECRET_ACCESS_KEY | Your AWS secret access key, available on the spreadsheet that you can download after you created a user in AWS S3 |
| AWS_ACCESS_KEY_ID | Your AWS access key ID, available on the spreadsheet that you can download after you created a user in AWS S3 |
| USE_AWS | True |

---

## Deployment on Heroku

Steps:

1. Create `requirements.txt`  & `Procfile` so Heroku knows what to install and how to reads your files. To do so, type these commands in your terminal:
    * `pip3 freeze > requirements.txt`
    * `echo web: python run.py > Procfile`
2. Go to your Heroku profile and create a new app.
5. In the Deploy tab, select GitHub in the Deployment Method part and connect your repository. Once it's done, you can now enable Automatic Deploys.
8. In the Settings tab, click Reveal Config Vars and add all the variables shown above, with your own values.
10. In the Resources tab, find and add Heroku Postgres.
11. In your terminal, transfer your data to PostgreSQL by running `python3 manage.py makemigrations` and `python3 manage.py migrate`.
14. You need a superuser to access the Django admin panel so type `python3 manage.py createsuperuser` and follow the instructions.
14. In the Heroku Config Vars, you can add `DISABLE_COLLECTSTATIC`, value `1`.
19. In `settings.py` file, add your Heroku app name in the `ALLOWED_HOSTS` dict.

---

## Amazon AWS

### S3 Bucket

1. Create a new bucket.

2. In the Properties tab, turn on static website hosting, and add `index.html` and `error.html`.

3. In the Permissions tab, add this code snippet to the CORS config:

   ```python
    [
       {
         "AllowedHeaders": [
           "Authorization"
         ],
         "AllowedMethods": [
           "GET"
         ],
         "AllowedOrigins": [
           "*"
         ],
         "ExposeHeaders": []
       }
     ]
   ```

4. Now in Bucket Policy > Edit > Policy Generator > Policy Type > S3 Bucket Policy.

5. In Add Statements, Effect = Allow, Principal = `*`, Actions = `GetObject`, and finally copy-paste your ARN, click Add Statement.

6. Click 'Generate', copy the result and paste it into the Bucket Policy area.

7. On the Resource line, just add `/*` at the end of your ARN, and save.

8. Finally, in Access Control List, select List for Everyone (public access).

**IAM**

1. User Groups > Create New Group.
2. Policies > Create Policy > JSON > Import Managed Policy > AmazonS3FullAccess > Import.
3. On the Resource line, instead of `"*"` paste your ARN twice and add `/*` at the end of one, then save.
3. Click Next:Tags, Next:Review, give it a name and click Create Policy.
5. Back to User Groups > click on your group > Permissions > Add Permissions > Attach Policies > find the policy you just created > Add Permissions.
6. In Users > Add users > type a name > check the Access key - Programmatic access box > Next:Permissions.
7. Select the group you created > Next:Tags > Next:Reviews > Create user.
8. Download the spreadsheet, it gives you your `AWS_SECRET_ACCESS_KEY` and `AWS_ACCESS_KEY_ID`. 

**Final AWS Steps**

1. Back to Heroku, remove the `DISABLE_COLLECTSTATIC` variable from your Config Vars.
4. Back to AWS, in your S3 Bucket, create a `media` folder then Upload > Add files > upload all your product images.
6. In Permissions > Predefined ACLs > select Grant public-read access > Upload.

---

## Cloning

1. After you've copied the HTTPS or SSH link, located under the Code dropdown button on [The Pastry Box GitHub page](https://github.com/LuciusVH/the_pastry_box).
2. Open your preferred IDE, create a virtual environment and activate it.
3. Run the command `git clone` + the link you've copied on step #1.
4. Create your environment file `env.py` and add the variables detailed above.
5. Create a `.gitignore` file and add it your `env.py`.
6. Install all the requirements: open the terminal and run `pip3 install -r requirements.txt`.
7. Migrate the database models by typing `python3 manage.py makemigrations` & `python3 manage.py migrate`.
8. Create a Superuser by typing `python3 manage.py createsuperuser` and follow the instructions.
9. Run the project locally by typing `python3 manage.py runserver`.

---

## Gmail Setup

You need to authorize external connections to your Gmail account and set up a unique password for Django to connet to it. To do so:

1. In your Gmail, go to Manage your Google account.
1. In the Security tab, make sure to enable the 2-Step Verification.
1. Click just below on App passwords, enter your Google password when invited. 
1. Click on Select an app > Other > give it a name > Generate.
8. Copy the given password and paste it as your EMAIL_HOST_PASS variable, in your `env.py` file and Heroku Config Vars.
