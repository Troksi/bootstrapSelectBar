from flask import Flask, render_template ,request, jsonify, redirect, make_response, url_for


class Company:
    def __init__(self,
                 company_profile_id,
                 company_name="",
                 company_description="",
                 website="",
                 year_of_foundation=0,
                 total_number_of_employees=0,
                 percentage_of_staff_growth=0,
                 percentage_of_it_staff=0,
                 location="",
                 specialization="",
                 theme=""):
        self.company_profile_id = company_profile_id
        self.company_name = company_name
        self.company_description = company_description
        self.website = website
        self.year_of_foundation = year_of_foundation
        self.total_number_of_employees = total_number_of_employees
        self.percentage_of_staff_growth = percentage_of_staff_growth
        self.percentage_of_it_staff = percentage_of_it_staff
        self.location = location
        self.specialization = specialization
        self.theme = theme

    def to_string(self):
        return str(self)#.replace('\n','<br>')
    
    def __str__(self) -> str:
        return ('Company:\n id:{}\n name:{}\n description:{}\n website:{}\n year of foundation:{}\n total number of employees:{}\n percentage of staff growth:{}\n percentage of it staff:{}\n location:{}\n specialization:{}\n theme:{}'.format(
            self.company_profile_id,
            self.company_name,
            self.company_description,
            self.website,
            self.year_of_foundation,
            self.total_number_of_employees,
            self.percentage_of_staff_growth,
            self.percentage_of_it_staff,
            self.location,
            self.specialization,
            self.theme))


class Template:
    def __init__(self, template_id, sales_profile_id, template_name, template_description="", template_tags=""):
        self.template_id = template_id
        self.sales_profile_id = sales_profile_id
        self.template_name = template_name
        self.template_description = template_description
        self.template_tags = template_tags


class SalesProfile:

    company_profile = None

    def __init__(self, sales_profile_id, user_profile_id, company_profile_id, sales_description=''):
        self.sales_profile_id = sales_profile_id
        self.user_profile_id = user_profile_id
        self.company_profile_id = company_profile_id
        self.sales_description = sales_description

class LinkedinProfile:
    publications: []
    experiance: []
    education: []
    skills: []
    tags: []
    def __init__(self,
                 linkedin_profile_id,
                 linkedin_profile_name="",
                 linkedin_profile_description="",
                 linkedin_link=""):
        self.linkedin_profile_id = linkedin_profile_id
        self.linkedin_profile_name = linkedin_profile_name
        self.linkedin_profile_description = linkedin_profile_description
        self.linkedin_link = linkedin_link
        self.publications = []
        self.experiance = []
        self.education = []
        self.skills = []
        self.tags = []


app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('home.html')

@app.route('/', methods=['GET'])
def dashboard_page():
    sales_profile = SalesProfile(1,1,1)
    sales_profile.company_profile = Company(1,'Main Company','Main description','web')
    templates = [Template(1,1,'First template','same text','Example'),
                 Template(1,1,'First template','same text','Example'),
                 Template(1,1,'First template','same text','Example')]
    company_profiles = [Company(2,'Same Company 1','des 1'),
                        Company(3,'Same Company 2','des 2'),
                        Company(4,'Same Company 3','des 3')]
    linkedin_profiles = [LinkedinProfile(1,'Jon Smit','Cool gay')]
    return render_template('selectAllText.html', 
                           sales=sales_profile, 
                           templates=templates, 
                           company_profiles=company_profiles,
                           linkedin_profiles=linkedin_profiles)

# @app.route('/dashboard', methods=['POST'])
# def login():
#     data = request.json  # Get the JSON data from the POST request
#     login = data.get('login')
#     password = data.get('password')
#     login = login if login is not None else ''
#     password = password if password is not None else ''
#     return  make_response("Secces", 200)
    
#     return  make_response("Invalid password", 401)

if __name__ == '__main__':
    app.run()
