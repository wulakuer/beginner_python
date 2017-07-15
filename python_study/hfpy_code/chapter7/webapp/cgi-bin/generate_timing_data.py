import yate
import athletemodel
import athletelist
import cgi
import cgitb

cgitb.enable()

athletes=athletemodel.get_from_store()
form_data=cgi.FieldStorage()
athlete_name=form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header("Time Data Page"))

if athlete_name:
    print(yate.header(athletes[athlete_name].name +athletes[athlete_name].dob+"'s timing data top 3 are:"))
    #tops=athletes[athlete_name].top3
    print(yate.u_list(athletes[athlete_name].top3))
    
print(athlete_name)
print(yate.include_footer({"Home":"../index.html","Another Athlete":"generate_list.py"}))
