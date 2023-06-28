from bs4 import BeautifulSoup
import requests
import time

# Jobs Filtration by owned skill
skills = ['Python', 'Java', 'JavaScript', 'C++', 'HTML']
print("Enter skills that you are not familiar with (one per line). Enter 'done' when finished.")

unfamiliar_skills = []
while True:
    skill = input(">")
    if skill == 'done':
        break
    unfamiliar_skills.append(skill)

print(f'Filtering out {unfamiliar_skills}')

filtered_skills = [skill.lower()
                   for skill in skills if skill.lower() not in unfamiliar_skills]


def find_jobs():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    # print(html_text)

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):

        published_data = job.find('span', class_="sim-posted").text
        if 'few' in published_data:
            company_name = job.find(
                'h3', class_='joblist-comp-name').text.replace(" ", "")
            job_skills = job.find(
                'span', class_='srp-skills').text.replace(" ", "")

            # show link of the specific jobs
            job_link = job.header.h2.a['href']

            if any(skill in job_skills.lower() for skill in filtered_skills):
                with open(f'saveFile/{index}.txt', 'w') as f:
                    f.write(f'Company Name: {company_name}\n')
                    f.write(f'Required Skills: {job_skills}\n')
                    f.write(f'Job Link: {job_link}')
                print(f'File save: {index}')

                # print(posted)
                # print(company_name)
                # print(skills)

                # print(f'''
                # company Name:{company_name}
                # Required Skills:{skills}
                # Post time: {published_data}
                # ''')

                # Prettifying the jobs paragraph
                # print(f'Company Name: {company_name.strip()}')
                # print(f'Required Skills: {skills.strip()}')
                # print(f'Job Link: {job_link}')
                # print('')


if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)
