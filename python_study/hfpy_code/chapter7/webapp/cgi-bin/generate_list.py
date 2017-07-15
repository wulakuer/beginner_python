import athletemodel
import glob
import yate
import cgi

data_files=glob.glob("data/*.txt")
athletes=athletemodel.put_to_store(data_files)
print(yate.start_response())
print(yate.include_header("Atheletes list"))
print(yate.start_form("generate_timing_data.py"))
print(yate.para("Please select one athlete from the list below:"))
for each in athletes:
	print(yate.radio_button("which_athlete",athletes[each].name))
print(yate.end_form())
print(yate.include_footer({"Home":"../index.html"}))


form_data=cgi.FieldStorage()
athlete_name=form_data['which_athlete'].value
