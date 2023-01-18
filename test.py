
job_titles = {
    "Customer Success Manager" : ["CMS","C.S.M", "Customer Success Manager"],
    "Marketing Manager" : ["Marketing Manager","MM" ],
    "CTO" : ["CTO","Chief Technology Officer"],
    "UX web-designer" : ["UX web-designer"],
    "Sales Manager" : ["Sales Manager"],
    "Product Owner" : ["Product Owner"]
}

# TEST JOBS
test_job_title = "MM"

for key, value in job_titles.items():
    if test_job_title in value:
        print(f"{test_job_title} belongs to key: {key}")
        test_job_title = key


print(test_job_title)

"""
Under here you could set up code to send an email to sales ops manager, notifying them to add 
this new job title to list of job titles or to the job title acronyms, 
as it has never been seen before.
Could look into replacing this with a simple machine learning model?
"""
if test_job_title in job_titles.values():
    print("nooo")

