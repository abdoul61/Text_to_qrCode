# This code can be use to convert an image to a pdf


# 1- install the pdf library as follow: 
# pip3 install fpdf


def converTopdf(l,x,y,w,h):

	from fpdf import FPDF


	# Nex promp the user to enter a list of image/s to be converted
	# we will call it l

	pdf = FPDF()

	for image in l:
		pdf.add_page()
		pdf.image(image,x,y,w,h)
		pdf.output("yourFile.pdf","F")



lst = input("Enter a list of image to convert")
x = input("Enter x value : ")

y = input("Enter y value : ")

w = input("Enter  w value : ")


h = input("Enter h value : ")



converTopdf(lst,x,y,w,h)
