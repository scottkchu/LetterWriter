jobs = [
    ["McDonalds", "Server"],
    ["Google", "Software Engineer"]
]

for i in jobs:
    #Opening cover letter template
    template = open("template.txt", "r")

    #Creating and opening new cover letter
    new_coverLetter = i[0] + i[1]
    coverLetter = open(new_coverLetter + ".txt", "w")
    
    for line in template:
        if "COMPANY NAME" in line:
            coverLetter.write(line.replace("COMPANY NAME", i[0]))
        elif "JOB POSITION" in line:
            coverLetter.write(line.replace("JOB POSITION", i[1]))
        else:
            coverLetter.write(line)

    template.close()
    coverLetter.close()












