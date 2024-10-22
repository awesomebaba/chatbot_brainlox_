from bs4 import BeautifulSoup

# Open and read the HTML file
with open('page_source.html', 'r', encoding='utf-8') as html_file:
    content = html_file.read()

# Parse using BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

with open('formatted_data.txt', 'w', encoding='utf-8') as output_file:
    # Find all course boxes (divs containing course information)
    courses = soup.find_all('div', class_='single-courses-box')

    # Loop through each course and extract relevant information
    for course in courses:
        # course title
        title_tag = course.find('h3')
        title = title_tag.get_text(strip=True) if title_tag else 'No title'

        #  course description
        description_tag = course.find('p')
        description = description_tag.get_text(strip=True) if description_tag else 'No description'

        # number of lessons (handling comments and text)
        lessons = 'No lessons info'
        lessons_tag = course.find('ul', class_='courses-box-footer')
        if lessons_tag:
            for li in lessons_tag.find_all('li'):
                if 'Lessons' in li.get_text():
                    # lessons from text and comments
                    lessons_text = ''.join(li.stripped_strings)
                    lessons = lessons_text.split()[0]  # Extract the number (usually the first part)
                    break

        # price per session
        price_tag = course.find('span', class_='price-per-session')
        price = price_tag.get_text(strip=True) if price_tag else 'No price info'

        # extracted data into the output file
        output_file.write(f"Course Title: {title}\n")
        output_file.write(f"Description: {description}\n")
        output_file.write(f"Lessons: {lessons}\n")
        output_file.write(f"Price per session: {price}\n")
        output_file.write("="*40 + "\n")  # Separator between courses

print("Data extraction complete! Structured data saved in 'formatted_data.txt'.")
