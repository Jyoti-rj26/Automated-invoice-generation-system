import os
import datetime
from jinja2 import Environment, FileSystemLoader
import pdfkit  # you can also use WeasyPrint or ReportLab

def generate_invoice():
    today = datetime.date.today()
    invoice_data = {
        'date': today.strftime("%Y-%m-%d"),
        'client': 'Acme Corporation',
        'services': [
            {'description': 'Development work', 'rate': 50, 'hours': 20},
            {'description': 'Consulting', 'rate': 100, 'hours': 5}
        ],
    }

    invoice_data['total'] = sum(service['rate'] * service['hours'] for service in invoice_data['services'])

    # Load HTML template
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('invoice_template.html')
    html_out = template.render(invoice=invoice_data)

    # Save as PDF
    output_file = f"invoices/invoice_{today}.pdf"
    pdfkit.from_string(html_out, output_file)

    print(f"Invoice saved to {output_file}")

if __name__ == '__main__':
    generate_invoice()
