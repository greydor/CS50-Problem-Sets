from fpdf import FPDF




def main():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 34)
    pdf.image("shirtificate.png", y = 80,  w = 190)
    pdf.cell(190, 50, "CS50 Shirtificate", align = "C", new_x = "LMARGIN", new_y = "TMARGIN")
    pdf.set_font("helvetica", "B", 22)
    pdf.set_text_color(r = 255)
    pdf.cell(190, 250, input("Enter name: ") + " took CS50" , align = "C")
    pdf.output("shirtificate.pdf")








if __name__ == "__main__":
    main()