# problem : Find Duplicate Emails
# link : https://leetcode.com/problems/find-duplicate-emails/
# Difficulty : Easy
# logic : group by + Having clause


"""SELECT email
FROM person
GROUP BY email
HAVING COUNT(email)>1;"""
