from fpdf import FPDF


def export_pdf(df, winner):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(0, 10, "Cloud Referee – Decision Report", ln=True)

    for _, row in df.iterrows():
        pdf.ln(5)
        pdf.multi_cell(
            0,
            8,
            f"Service: {row['Service']}\n"
            f"Score: {row['Score']}\n"
            f"Pros: {row['Pros']}\n"
            f"Cons: {row['Cons']}\n"
        )

    pdf.ln(5)
    pdf.cell(0, 10, f"Recommended Choice: {winner['Service']}", ln=True)

    pdf.output("decision_report.pdf")
