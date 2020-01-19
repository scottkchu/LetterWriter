## Inspiration
Finding your first SWE/CS internship can be hard. Most students apply to hundreds of positions before they land their first internship. To speed up the application process LetterWriter helps generate new cover letters for every position you're applying to!

## What it does
LetterWriter uses Beautiful Soup to scrape SWE/CS job postings on Linkedin and Indeed. The information is passed to a text parsing program that will generate new custom cover letters.

## Future Improvements
There are so many job positions in the tech industry and cover letters must cater to different roles. We want to extend LetterWriter so that it utilizes more advance scraping and creates cover letters that better suit the roles you are applying to!

## Try it out!
```bash
git clone https://github.com/howtobescott/LetterWriter.git
pip3 install google-search
pip3 install requests
pip3 install beautifulsoup4
cd LetterWriter
python3 coverLetter.py
```
* Simply change the template.txt file to your own template cover letter. Use "JOB POSITION" and "COMPANY NAME" as place holders in your template.
* Cover letters should appear in the same working directory once the program is done running.

## Contributions
* Byron Tung - Computer Science Student @ University of Alberta
* Steven Truong - Computer Science Student @ University of Alberta
* Scott Chu - Software Engineering Student @ University of Alberta
