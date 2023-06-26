from fpdf import FPDF
import datetime as dt

WIDTH = 210
HEIGHT = 297
pdf = FPDF()
total_images=0
report_days = 0

def from_date(report_days):
    new_date = (dt.datetime.today() - dt.timedelta(report_days))
    new_date = str(new_date).split(' ')[0]
    return str(dt.datetime.strptime(new_date, "%Y-%m-%d").strftime("%B %d, %Y"))


def create_title(pdf):
    pdf.set_font('Arial', 'B', 30)
    pdf.ln(60)
    pdf.write(25, '''EQUITY RESEARCH REPORT''')
    pdf.ln(5)
    pdf.set_font('Arial', '', 20)
    pdf.ln(5)
    pdf.write(25, '''Foreshadow The Week''')





def equistat_high_correlation_report(report_days, total_images):
    pdf = FPDF()
    # First Page
    pdf.add_page()
    pdf.image('resources/letterhead_2_cropped.png', 0, 0, WIDTH)

    # pdf.ln(150)
    # period_to_print = f'From {from_date(report_days)} to {dt.datetime.today().strftime("%B %d, %Y")}'
    # pdf.write(25, str(period_to_print))

    create_title(pdf)

    # Report Content
    # pdf.add_page()
    for image_no in range(1, total_images, 2):
        pdf.add_page()

        pdf.image(f"img/{image_no}.png", 10, 10, WIDTH - 5)
        pdf.image(f"img/{image_no + 1}.png", 10, 150, WIDTH - 5)
        pdf.image('resources/letterhead_bottom.png', 0, 290, WIDTH)

    pdf.output(f'reports/EQUISTAT High Correlation Report {report_days} days.pdf', 'F')


def create_report(report_name, total_images):
    pdf = FPDF()
    # First Page
    pdf.add_page()
    pdf.image('resources/letterhead_2_cropped.png', 0, 0, WIDTH)

    create_title(pdf)


    for image_no in range(1, total_images, 2):
        pdf.add_page()
        pdf.image(f"img/{image_no}.png", 10, 10, WIDTH - 5)
        pdf.image(f"img/{image_no + 1}.png", 10, 150, WIDTH - 5)
        pdf.image('resources/letterhead_bottom.png', 0, 290, WIDTH)

    # For Two Columns
    # pdf.image("test.png", 5, 30, WIDTH/2 - 5)
    #
    # plot_daily_count_countries(["US", "India"], filename = "test2.png")
    # pdf.image("test.png", WIDTH/2 + 5, 30, WIDTH/2-5)

    pdf.output(f'reports/{report_name}.pdf', 'F')


