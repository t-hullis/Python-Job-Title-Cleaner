
job_titles = {
    "Customer Success Manager" : ["CMS","C.S.M", "Customer Success Manager"],
    "Marketing Manager" : ["Marketing Manager","MM" ],
    "CTO" : ["CTO","Chief Technology Officer"],
    "UX web-designer" : ["UX web-designer"],
    "Sales Manager" : ["Sales Manager"],
    "Product Owner" : ["Product Owner"]
}

# TEST JOBS
job1= "Customer Success Manager"
job2= "MM"

for key, value in job_titles.items():
    if job2 in value:
        print(f"{job2} belongs to key: {key}")




# if job not in job_titles:
    """
    Here you could send an email to sales ops manager, notifying them to add 
    this new job title to list of job titles or to the job title acronyms, 
    as it has never been seen before.
    Could look into replacing this with a simple machine learning model?

    """