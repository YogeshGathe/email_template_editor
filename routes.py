from flask import Blueprint, redirect, render_template, request, url_for, Markup

api = Blueprint('api', __name__)

@api.route("/")
def index():
    return redirect("/home")

@api.route("/home")
def home():
    return render_template('home.html')

@api.route("/edit_email_template", methods=['GET', 'POST'])
def edit():
    """
    This function will get the data from HTML form, use the 'update_email_template' function to update form data in email template,
    and will rediret to 'show_template' function to show the email.

    """
    if request.method=='POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        policy_number = request.form['policy_number']
        expiry_date = request.form['expiry_date']

        template_path = 'templates/email_template1.html'

        updated_template = update_email_template(template_path, fname, lname, email, policy_number, expiry_date)

        return redirect(url_for('api.show_template', updated_template=Markup(updated_template)))

    return render_template('home.html')


@api.route('/show_template')
def show_template():
    """
    Function to show the update email.

    """
    updated_template = request.args.get('updated_template')
    return render_template('show_template.html', updated_template=updated_template)


def update_email_template(template_path, fname, lname, email, policy_number, expiry_date):
    """
    Function to update the email template saved in 'templates' folder """
    with open(template_path, 'r') as file:
        template = file.read()

    template = template.replace('{{fname}}', fname)
    template = template.replace('{{lname}}', lname)
    template = template.replace('{{email}}', email)
    template = template.replace('{{policy_number}}', policy_number)
    template = template.replace('{{expiry_date}}', expiry_date)

    return template