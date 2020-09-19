# TODO: create a regex for phone numbers
# TODO: create a regex for email addresses
# get text off the clipboard
# extract email and phone

import re, pyperclip 
phoneRegex = re.compile(r'''
#dash, no dash, extensions
(
((\d\d\d)|(\(\d\d\d\)))?
(\s|-)
\d\d\d
-
\d\d\d\d
(((ext(\.)?\s|x)
(\d(2,5)))?
))
''', re.VERBOSE)

emailRegex = re.compile(r'''
#name @ and domain
[a-zA-Z0-9_.+]+
@
[a-zA-Z0-9_.+]+
''', re.VERBOSE)

text = "Oscar Morrison508-405-5015morriso963@live.comChad Hewitt607-718-7246hewit4282@att.netLou Espinoza882-284-1717lespinoza86@me.comGerman Juarez276-391-3652juare3314@hotmail.comChase Bullock920-671-2378cbullock@icloud.comMargarito Farley975-201-8332mfarley26@sbcglobal.netRamiro Wright822-403-4750wrigh2662@aol.comEddy Sherman231-595-3324esherman@hotmail.comClinton Doyle631-975-3387cdoyle@me.comMonroe Stevens305-907-3140mstevens60@hotmail.comClay Tyler412-638-7724ctyler25@me.comRuben Graves724-723-3759wthg6@gmail.comLane Kirk881-337-7390lkirk72@optonline.netShayne Collier757-809-2413scollier53@comcast.netOtha Brock407-774-5107othab30@comcast.netRobby Jordan915-287-5137rjordan@verizon.netBret Garcia910-869-3090bgarcia71@aol.comMarcellus Velasquez606-276-4621slzcwg65@gmail.comDarell Kane882-280-7095dkane58@yahoo.comHerb Joseph509-429-1943herbj15@gmail.comSergio Watts541-475-7662swatts20@yahoo.comJarrett Colon309-508-1355jcolon51@live.comGraig Lester740-267-4233glester8@att.netTyler Alvarado501-409-1473talvarado94@msn.comHarris Duran801-504-1087dura5281@aol.comNestor Page559-670-5302npage@aol.comPerry Ellison201-665-2121pellison64@msn.comEarl Cantrell352-331-5192ecantrell11@msn.comModesto Strong802-352-7505mstrong36@icloud.com"
extractPhone = phoneRegex.findall(text)
extractEmail = emailRegex.findall(text)

print(extractEmail)

allnumbers = []
for number in extractPhone:
    allnumbers.append(number[0])
print(allnumbers)