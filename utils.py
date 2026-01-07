from fpdf import FPDF

def export_pdf(df, winner):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, "Cloud Referee Decision Report\n\n")

    for i, row in df.iterrows():
        pdf.multi_cell(0, 10, f"Service: {row['Service']}")
        pdf.multi_cell(0, 10, f"Score: {row['Score']}")
        pdf.multi_cell(0, 10, f"Pros: {row['Pros']}")
        pdf.multi_cell(0, 10, f"Cons: {row['Cons']}")
        pdf.multi_cell(0, 10, "\n")

    pdf.multi_cell(0, 10, f"Recommended: {winner['Service']}")

    # Return PDF as bytes
    pdf_bytes = pdf.output(dest='S').encode('latin1')  # << fixed here
    return pdf_bytes
