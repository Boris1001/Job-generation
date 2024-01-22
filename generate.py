import xlwt
import random
import requests

# Helper function to generate specific text based on column name
def generate_text(column_name):
    if column_name == "ID":
        return str(random.randint(10000, 99999))  # Generating a random 5-digit ID
    elif column_name == "Название вакансии":
        job_titles = ["Разработчик", "Бухгалтер", "Менеджер по продажам", "HR-менеджер", "Маркетолог"]
        return random.choice(job_titles)
    elif column_name == "Навыки":
        skills = ["Python, SQL", "Управление командой", "Продажи, CRM", "Рекрутинг, HR", "Digital-маркетинг, SEO"]
        return random.choice(skills)
    elif column_name == "Опыт работы":
        experience_years = random.randint(1, 10)
        return f"{experience_years} года опыта"
    else:  # For "Описание" and "Требования"
        response = requests.get("https://loripsum.net/api")
        return response.text[:2048]

# Генерируем базу вакансий
def generate_vacancies():
    vacancies = [("ID", "Название вакансии", "Описание", "Требования")]
    num_vacancies = random.randint(5, 10)

    for i in range(num_vacancies):
        vacancy_id = generate_text("ID")
        title = generate_text("Название вакансии")
        description = generate_text("Описание")
        requirements = generate_text("Требования")
        vacancies.append((vacancy_id, title, description, requirements))

    return vacancies

# Генерируем базу резюме
def generate_resumes():
    resumes = [("ID", "Навыки", "Опыт работы")]
    num_resumes = random.randint(10, 15)

    for i in range(num_resumes):
        resume_id = generate_text("ID")
        skills = generate_text("Навыки")
        experience = generate_text("Опыт работы")
        resumes.append((resume_id, skills, experience))

    return resumes

# Записываем базу вакансий в XLS файл
def write_vacancies_to_excel(vacancies):
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("Vacancies")

    for row, vacancy in enumerate(vacancies):
        for col, field in enumerate(vacancy):
            sheet.write(row, col, field)

    workbook.save("vacancies.xls")

# Записываем базу резюме в XLS файл
def write_resumes_to_excel(resumes):
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("Resumes")

    for row, resume in enumerate(resumes):
        for col, field in enumerate(resume):
            sheet.write(row, col, field)

    workbook.save("resumes.xls")

# Генерируем базы данных и записываем их в XLS файлы
vacancies = generate_vacancies()
resumes = generate_resumes()

write_vacancies_to_excel(vacancies)
write_resumes_to_excel(resumes)