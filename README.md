# Google Login For Flask

There are many tutorials and libraries on Google Login with Flask. I've tried so many of them. Some of them are old, not working, missing deployment ....

But this one is neat, simple and it simply just works.

I put everything in one file for easy understanding.

I also included instructions for development and deployment.

## Usage

### For Development
1. create virtual environment
2. install several required packages

```
pip install Flask Authlib
```

3. Copy your keys into the file
4. run with
```
python wsgi_google_login.py
```

5. add callback url in google console
   1. for development add http://127.0.0.1:5000/auth
  
### For Deployment
1. for deployment add https://yourdomain.com/auth
   if you use blueprint, adjust accordingly
2. use SSL on server
3. comment out
   ```os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"```
4. remember to use app.run()
5. Set to publish once it works

## Strange Bugs
** this can be tricky **. Sometimes, you get mismatching URL error even though you've used correct url. Simply try to use https://www.yourdomain.com/auth will solve it.

## To do
Please message me if you know good solution for below:
- [ ] flask twitter login
- [ ] flask facebook login

## star project for future development

