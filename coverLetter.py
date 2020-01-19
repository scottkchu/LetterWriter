import indeed_scraper
import linkedin_scraper

if __name__ == '__main__':
    jobs1 = linkedin_scraper.linkedin()
    jobs2 = indeed_scraper.indeed()

    all_jobs = jobs1+jobs2

    for i in all_jobs:
        #Opening cover letter template
        template = open("template.txt", "r")

        #Creating and opening new cover letter

        if "/" in i[0]:
            i[0] = i[0].replace("/", " - ")
        elif "/" in i[1]:
            i[1] = i[1].replace("/", " - ")
        if "." in i[0]:
            i[0] = i[0].replace(".", "")
        elif "." in i[1]:
            i[1] = i[1].replace(".", "")

        new_coverLetter = i[0] + i[1]
        
        coverLetter = open(new_coverLetter + ".txt", "w")
        
        for line in template:
            if "COMPANY NAME" and "JOB POSITION" in line:
                coverLetter.write(line.replace("COMPANY NAME", i[0]).replace("JOB POSITION", i[1]))
            elif "COMPANY NAME" in line:
                coverLetter.write(line.replace("COMPANY NAME", i[0]))
            elif "JOB POSITION" in line:
                coverLetter.write(line.replace("JOB POSITION", i[1]))
            else:
                coverLetter.write(line)

        template.close()
        coverLetter.close()













