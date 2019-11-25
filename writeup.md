# Project Firewagon: CSEC-380 Writeup
--------------------

## Act 3
--------------------
1. Provide a link to the test cases you generated for this activity.

    > https://github.com/oneNutW0nder/firewagon/tree/master/tests

2. How do you ensure that users that navigate to the protected pages cannot bypass authentication requirements?

    > When a user requests a protected page, the web application checks for a valid cookie that is set when a user logs in. When a user logs out, the cookie is expired. If the cookie is expired, or not set when a user tries to access a protected page, they are redirected to the _login_ page. 

3. How do you protect against session fixation?

    > To prevent session fixation, we do not include session ids in the URL field and we invalidate old sessions before we give a new one. Also, each time a user logs in a new session ID is created. Upon logout the session ID is invalidated and set to _NULL_ in our database. 

4. How do you ensure that if your database gets stolen passwords aren’t exposed?

    > Passwords in our database are hashed and salted. They are hashed and salted using the python _bcrypt_ library. This combination of _salt+hash_ makes it difficult for attackers to crack our hashes. The _salts_ make it harder for attackers to carry out _rainbow table_ attacks. However, these measures will not stop attackers from cracking the hash of a weak password. In order to get users to make good, strong passwords, we could implement a password policy that checks the user's password at registration to make sure it meets the requirements. 

5. How do you prevent password brute force?
    > Currently, we do not prevent password brute force attacks. However, this could be prevented by introducting a rate limit. This would only allow attackers to send a request to try a password every couple of seconds, instead of as fast as the server can handle them. Also, we could implement a lockout feature which checks to see how many times a user has a failed login attempt and lock the user out for a predetermined time before they can try to login again. This would only allow attackers to try a handful of passwords at a time before waiting for the lockout period to finish. 
6. How do you prevent username enumeration?

    > The only thing that we do to prevent username enumeration is at the login page. When a user fails a login attempt, the error message tells them that they have an _Invalid username or password_ instead of specifying which one is invalid. To add further protections against username enumeration, we could add heavy rate limiting to the registration page to prevent attackers from collecting usernames through failed registrations. Also, making sure load/processing times for successful or failed actions will prevent timing attacks. An attacker could observe that a login/registration attempt with a valid username takes longer than an attempt with an invalid username. 

7. What happens if your sessionID is predictable, how do you prevent that?

    > If our sessionID is predictable an attacker could brute force or predict sessionID's for users. We prevent this by generating a random string of 64 characters and use that as the sessionID. 

## Act 4
--------------------
1. How do you prevent XSS is this step when displaying the username of the user who uploaded the video?

    > We do not directly prevent XSS when displaying a username. Instead, we display the user's ID number instead of their username when they upload a video. This prevents a user from doing XSS via their username. In the future, if we display usernames, we can sanitize the username before it is stored in the database so that rendering on a template is safer. We can sanitize the username by HTML encoding special charaters. We could also use a python library that specializes in sanatization. 

2. How do you ensure that users can’t delete videos that aren’t their own?

    > To prevent random user's deleting your videos, we check to see if your user ID matches the user ID of the owner of the video. However, the user ID that is checked is not passed in a request, it is the ID that is stored in the database for a user. This prevents spoofing user IDs in the request. Also, we do not display the _delete video_ button to users that do not own the video (granted, this does not stop an attacker from sending the proper request to the endpoint). 

## Act 5
--------------------
1. How would you fix your code so that these issues were no longer present?

> To fix our code we could use the actual SQLAlchemy functions that handle input sanatization and some security for us. Instead, we are using raw SQL commands and making pure user input part of the query.

2. What are the limitations, if any that, of the SQL Injection issues you’ve included? 

> There are not many limitations. Having access to running SQL commands allows an attacker to delete the entire database which, if things are not backed up, would lead to massive down time. An attacker can even run system commands through SQL injection. This effectively allows an attacker to whatever they wish with our system.

## Act 6
--------------------
1. How would you fix your code so that this issue is no longer present?

    > I would fix the code by removing the functionality that was being set in place to allow previewing a video from a URL as a result of a GET request on the upload endpoint using the content parameter. This resulted in not only videos being previewed, but any sort of request sent to it, either external or internal.

2. How does your test demonstrate SSRF as opposed to just accessing any old endpoint.

    > The test I've performed for testing out the SSRF vulnerability makes and attempt to reach both a remote asset webpage with an HTTP request, as well as reaching internal assets by using the file:// URI for the request.

## Act 7
--------------------
1. How would you fix your code so that this issue is no longer present?

    > To prevent the command injection vulnerability by passing the url input to a os.system() call using wget, you'd replace the os.system() call to a safer way to retrieve a file from a url, like urllib's request.urlretrieve method. The system call would allow input to have a semicolon to execute commands are the wget, while urllib.request.urlretrieve() would avoid a system command and sanatize input.
