#!/usr/bin/python
import openpyxl
def GetVCF(name, email, number, org):
	vcf = "BEGIN:VCARD"+"\n"
	vcf += "VERSION:2.1"+"\n"
	vcf += "FN:"+name+"\n"
	vcf += "ORG:"+org+"\n"
	vcf += "TEL;WORK;VOICE:"+str(number)+"\n"
	vcf += "EMAIL:"+email+"\n"
	vcf += "END:VCARD"
	return vcf
def ReadXLAndGenerateVCF(file_name):
	fd_vcf = open("contacts.vcf", "w")
	workbook = openpyxl.load_workbook(file_name)
	first_sheet = workbook.get_sheet_names()[0]
	worksheet = workbook.get_sheet_by_name(first_sheet)
	result_str =""
	result_vcf =""
	for row in worksheet.iter_rows():	
		#print (row)
		print("Name",row[0].value)
		print("Email",row[1].value)
		print("Mobile",row[2].value)
		print("Organisation",row[3].value)
		vcf_stream = GetVCF(row[0].value, row[1].value, row[2].value, row[3].value)
		fd_vcf.write(vcf_stream)
	fd_vcf.close()
def main():
	file_name = input("Enter xls FileName having name, email-id, number & organisation details of each person:")
	ReadXLAndGenerateVCF(file_name)

if __name__ == "__main__":
	main()
