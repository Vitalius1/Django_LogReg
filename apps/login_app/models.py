from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+.[^@\s]+$")

class UserManager(models.Manager):
    def registerVal(self, postData):
        results = {"status":True, 'errors':[]}
        user = []
        if not postData['first_name'] or len(postData['first_name']) < 3:
            results['status'] = False
            results['errors'].append("First name must be at least 3 characters long.")
        if not postData['last_name'] or len(postData['last_name']) < 3:
            results['status'] = False
            results['errors'].append("Last name must be at least 3 characters long.")
        if not postData['email'] or len(postData['email']) < 5 or not re.match(EMAIL_REGEX, postData['email']):
            results['status'] = False
            results['errors'].append("Email must be at least 5 characters long.")
        if not postData['password'] or len(postData['password']) < 5 or postData['password'] != postData['confirm_pass']:
            results['status'] = False
            results['errors'].append("Password must be at least 5 characters long and matches your confirm password.")

        if results['status'] == True:
            user = User.objects.filter(email = postData['email'])
        if len(user) != 0:
            results['status'] = False
            results['errors'].append("User already exists. Try another email.")

        return results

    def loginVal(self, postData):
        results = {"status":True, 'errors':[], 'user':None}
        if len(postData['email']) < 3:
            results['status'] = False
            results['errors'].append('Something went wrong!!!')
        else:
            user = User.objects.filter(email = postData['email'])
            if len(user) <= 0:
                results['status'] = False
                results['errors'].append('Something went wrong!!!')
            elif len(postData['password']) < 5 or postData['password'] != user[0].password:
                results['status'] = False
                results['errors'].append('Something went wrong!!!')
            else:
                results['user'] = user[0]
        return results
        print "***************************"
class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    objects = UserManager()
